from pyspark.sql import DataFrame

def parse_item(fact_inventory: DataFrame, fact_order: DataFrame) -> DataFrame:
    df1 = fact_inventory.select("item_id")
    df2 = fact_order.select("product_id").withColumnRenamed("product_id", "item_id")
    return df1.union(df2).dropna().dropDuplicates()
