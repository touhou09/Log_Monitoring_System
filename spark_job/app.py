from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, split, trim, to_timestamp, col

spark = SparkSession.builder \
    .appName("KafkaSimpleLogParsing") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "payment_topic,inventory_topic,notify_topic,auth_topic,etc_topic") \
    .option("startingOffsets", "latest") \
    .load() \
    .selectExpr("CAST(value AS STRING) as log")

# 1. timestamp 추출
df = df.withColumn("timestamp_raw", expr("substring_index(substring_index(log, ']', 1), '[', -1)"))

# 2. log 본문 추출
df = df.withColumn("body", expr("substring_index(log, '] ', -1)"))

# 3. logger 와 message 분리 (가장 마지막 ` : ` 기준으로 자름)
df = df.withColumn("logger", expr("trim(substring_index(body, ' : ', 1))")) \
       .withColumn("message_raw", expr("trim(substring_index(body, ' : ', -1))"))

# 4. 컬럼 정리 + timestamp 형식 맞추기 + message에서 맨 끝에 남은 `"}"` 제거
final_df = df.select(
    to_timestamp("timestamp_raw", "yyyy-MM-dd HH:mm:ss").alias("timestamp"),
    "logger",
    expr("regexp_replace(message_raw, '\"}$', '')").alias("message")
)

query = final_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()