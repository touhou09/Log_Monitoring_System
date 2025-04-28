from pyspark.sql.functions import regexp_extract, col

def parse_etc(df):
    return df.filter(col("topic") == "etc_topic") \
             .withColumn("domain", regexp_extract("message", r"(\w+) action completed successfully", 1).cast("string")) \
             .select("timestamp", "domain", "level")
