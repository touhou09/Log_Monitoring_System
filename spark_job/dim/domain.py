from pyspark.sql import DataFrame

def parse_domain(fact_etc: DataFrame) -> DataFrame:
    return fact_etc.select("domain").dropna().dropDuplicates()
