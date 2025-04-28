from pyspark.sql.functions import regexp_extract, col

def parse_inventory(df):
    return df.filter(col("topic") == "inventory_topic") \
             .withColumn("item_id", regexp_extract("message", r"itemId=(ITEM-\w+)", 1).cast("string")) \
             .withColumn("remaining", regexp_extract("message", r"remaining=(\d+)", 1).cast("int")) \
             .filter(col("remaining").isNotNull()) \
             .select("timestamp", "item_id", "remaining", "level")
