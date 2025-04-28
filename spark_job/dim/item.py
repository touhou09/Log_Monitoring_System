from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def parse_item(fact_inventory: DataFrame, fact_order: DataFrame) -> DataFrame:
    df1 = fact_inventory.select(col("item_id").cast("string"))
    df2 = fact_order.select(col("product_id").cast("string")).withColumnRenamed("product_id", "item_id")
    return df1.union(df2).dropna().dropDuplicates()
