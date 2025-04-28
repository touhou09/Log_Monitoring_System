from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def parse_logger(base_df: DataFrame) -> DataFrame:
    return base_df.select(col("logger").cast("string")).dropna().dropDuplicates()
