# warehouse/writer/dim_writer.py
from warehouse.sink import write_to_clickhouse

def write_dim_streams(dim_time, dim_user, dim_item, dim_domain, dim_logger, dim_status):
    return [
        dim_time.writeStream
            .outputMode("append")
            .foreachBatch(lambda df, _: write_to_clickhouse(df, "dim_time"))
            .start(),

        dim_user.writeStream
            .outputMode("append")
            .foreachBatch(lambda df, _: write_to_clickhouse(df, "dim_user"))
            .start(),

        dim_item.writeStream
            .outputMode("append")
            .foreachBatch(lambda df, _: write_to_clickhouse(df, "dim_item"))
            .start(),

        dim_domain.writeStream
            .outputMode("append")
            .foreachBatch(lambda df, _: write_to_clickhouse(df, "dim_domain"))
            .start(),

        dim_logger.writeStream
            .outputMode("append")
            .foreachBatch(lambda df, _: write_to_clickhouse(df, "dim_logger"))
            .start(),

        dim_status.writeStream
            .outputMode("append")
            .foreachBatch(lambda df, _: write_to_clickhouse(df, "dim_status"))
            .start()
    ]