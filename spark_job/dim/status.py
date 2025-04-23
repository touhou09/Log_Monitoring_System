from pyspark.sql import DataFrame

def parse_status(*fact_dfs: DataFrame) -> DataFrame:
    return (
        fact_dfs[0].select("level")
        .unionAll(fact_dfs[1].select("level"))
        .unionAll(fact_dfs[2].select("level"))
        .unionAll(fact_dfs[3].select("level"))
        .unionAll(fact_dfs[4].select("level"))
        .dropna()
        .dropDuplicates()
    )
