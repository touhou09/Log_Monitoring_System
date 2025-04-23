from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, split, trim, to_timestamp, col, regexp_extract

from factor.auth import parse_auth
from factor.order import parse_order
from factor.payment import parse_payment
from factor.notify import parse_notify
from factor.inventory import parse_inventory
from factor.etc import parse_etc

from dim.user import parse_user
from dim.item import parse_item
from dim.time import parse_time
from dim.domain import parse_domain
from dim.logger import parse_logger
from dim.status import parse_status

import sys, os

spark = SparkSession.builder.appName("KafkaStructuredFactParsing").getOrCreate()

sys.path.append('/app')  # 또는 os.getcwd() 사용

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "payment_topic,inventory_topic,notify_topic,auth_topic,etc_topic,order_topic") \
    .option("startingOffsets", "latest") \
    .load() \
    .selectExpr("CAST(topic AS STRING) as topic", "CAST(value AS STRING) as log")

# 공통 파싱
df = df.withColumn("timestamp_raw", expr("substring_index(substring_index(log, ']', 1), '[', -1)")) \
       .withColumn("body", expr("substring_index(log, '] ', -1)")) \
       .withColumn("level", split(col("body"), " ")[0]) \
       .withColumn("logger", expr("trim(substring_index(body, ' : ', 1))")) \
       .withColumn("message_raw", expr("trim(substring_index(body, ' : ', -1))"))

base_df = df.select(
    col("topic"),
    to_timestamp("timestamp_raw", "yyyy-MM-dd HH:mm:ss").alias("timestamp"),
    "level",
    "logger",
    expr("regexp_replace(message_raw, '\"}$', '')").alias("message")
)

# 각 fact 테이블 처리
fact_auth = parse_auth(base_df)
fact_order = parse_order(base_df)
fact_payment = parse_payment(base_df)
fact_notify = parse_notify(base_df)
fact_inventory = parse_inventory(base_df)
fact_etc = parse_etc(base_df)

dim_user = parse_user(fact_auth, fact_order, fact_payment, fact_notify)
dim_item = parse_item(fact_inventory, fact_order)
dim_status = parse_status(fact_auth, fact_order, fact_payment, fact_notify, fact_inventory)
dim_logger = parse_logger(base_df)
dim_time = parse_time(fact_payment)
dim_domain = parse_domain(fact_etc)

query = fact_auth.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()