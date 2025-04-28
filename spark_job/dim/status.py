from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def parse_status(*fact_dfs: DataFrame) -> DataFrame:
    return (
        fact_dfs[0].select(col("level").cast("string"))
        .unionAll(fact_dfs[1].select(col("level").cast("string")))
        .unionAll(fact_dfs[2].select(col("level").cast("string")))
        .unionAll(fact_dfs[3].select(col("level").cast("string")))
        .unionAll(fact_dfs[4].select(col("level").cast("string")))
        .dropna()
        .dropDuplicates()
    )
