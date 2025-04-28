from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def parse_domain(fact_etc: DataFrame) -> DataFrame:
    return fact_etc.select(col("domain").cast("string")).dropna().dropDuplicates()
