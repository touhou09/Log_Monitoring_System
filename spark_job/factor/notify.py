from pyspark.sql.functions import regexp_extract, col

def parse_notify(df):
    return df.filter(col("topic") == "notify_topic") \
             .withColumn("user_id", regexp_extract("message", r"userId=(\w+)", 1)) \
             .withColumn("notif_type", regexp_extract("message", r"type=(\w+)", 1)) \
             .select("timestamp", "user_id", "notif_type", "level")
