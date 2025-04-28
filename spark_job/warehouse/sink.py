def write_to_clickhouse(df, table_name):
    try:
        print(f"[📥 ClickHouse] Writing to {table_name}")
        df.show(5, truncate=False)

        df.write \
            .format("jdbc") \
            .option("url", "jdbc:clickhouse://clickhouse:8123/analytics") \
            .option("driver", "com.clickhouse.jdbc.ClickHouseDriver") \
            .option("dbtable", table_name) \
            .option("user", "default") \
            .option("password", "") \
            .mode("append") \
            .save()
    except Exception as e:
        import traceback
        print(f"[❌ ERROR] Failed writing {table_name} to ClickHouse: {e}")
        traceback.print_exc()