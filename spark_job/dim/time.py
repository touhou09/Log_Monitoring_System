from pyspark.sql.functions import year, month, dayofmonth, hour, minute
from pyspark.sql import DataFrame

def parse_time(df: DataFrame) -> DataFrame:
    return (
        df.select("timestamp")
        .dropna()
        .dropDuplicates()
        .withColumn("year", year("timestamp"))
        .withColumn("month", month("timestamp"))
        .withColumn("day", dayofmonth("timestamp"))
        .withColumn("hour", hour("timestamp"))
        .withColumn("minute", minute("timestamp"))
    )
