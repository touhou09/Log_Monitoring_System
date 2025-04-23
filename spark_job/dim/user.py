from pyspark.sql import DataFrame

def parse_user(*fact_dfs: DataFrame) -> DataFrame:
    return (
        fact_dfs[0].select("user_id")
        .unionAll(fact_dfs[1].select("user_id"))
        .unionAll(fact_dfs[2].select("user_id"))
        .unionAll(fact_dfs[3].select("user_id"))
        .dropna()
        .dropDuplicates()
    )
