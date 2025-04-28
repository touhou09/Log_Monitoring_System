from pyspark.sql.functions import year, month, dayofmonth, hour, minute, col
from pyspark.sql import DataFrame

def parse_time(df: DataFrame) -> DataFrame:
    return (
        df.filter(col("timestamp").isNotNull())
        .withColumn("year", year("timestamp"))
        .withColumn("month", month("timestamp"))
        .withColumn("day", dayofmonth("timestamp"))
        .withColumn("hour", hour("timestamp"))
        .withColumn("minute", minute("timestamp"))
        .select("timestamp", "year", "month", "day", "hour", "minute")
    )
