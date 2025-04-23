from pyspark.sql.functions import regexp_extract, col

def parse_payment(df):
    return df.filter(col("topic") == "payment_topic") \
             .withColumn("user_id", regexp_extract("message", r"userId=(\w+)", 1)) \
             .withColumn("amount", regexp_extract("message", r"amount=(\d+)", 1).cast("int")) \
             .select("timestamp", "user_id", "amount", "level")
