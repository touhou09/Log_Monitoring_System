from pyspark.sql import DataFrame

def parse_logger(base_df: DataFrame) -> DataFrame:
    return base_df.select("logger").dropna().dropDuplicates()
