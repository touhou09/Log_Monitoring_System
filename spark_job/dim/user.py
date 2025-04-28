from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def parse_user(*fact_dfs: DataFrame) -> DataFrame:
    return (
        fact_dfs[0].select(col("user_id").cast("string"))
        .unionAll(fact_dfs[1].select(col("user_id").cast("string")))
        .unionAll(fact_dfs[2].select(col("user_id").cast("string")))
        .unionAll(fact_dfs[3].select(col("user_id").cast("string")))
        .dropna()
        .dropDuplicates()
    )
