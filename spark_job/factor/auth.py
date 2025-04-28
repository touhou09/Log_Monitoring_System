from pyspark.sql.functions import regexp_extract, col

def parse_auth(df):
    return df.filter(col("topic") == "auth_topic") \
             .withColumn("user_id", regexp_extract("message", r"userId=(\w+)", 1).cast("string")) \
             .select("timestamp", "user_id", "level")