from pyspark.sql.functions import regexp_extract, col

def parse_order(df):
    return df.filter(col("topic") == "order_topic") \
             .withColumn("user_id", regexp_extract("message", r"userId=(\w+)", 1)) \
             .withColumn("product_id", regexp_extract("message", r"productId=(\w+)", 1)) \
             .select("timestamp", "user_id", "product_id", "level")
