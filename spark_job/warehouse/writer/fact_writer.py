# warehouse/writer/fact_writer.py
from warehouse.sink import write_to_clickhouse

def write_fact_streams(fact_auth, fact_order, fact_payment, fact_notify, fact_inventory, fact_etc):
    return [
        fact_auth.writeStream
            .outputMode("append")
            .foreachBatch(lambda df, _: write_to_clickhouse(df, "fact_auth"))
            .start(),

        fact_order.writeStream
            .outputMode("append")
            .foreachBatch(lambda df, _: write_to_clickhouse(df, "fact_order"))
            .start(),

        fact_payment.writeStream
            .outputMode("append")
            .foreachBatch(lambda df, _: write_to_clickhouse(df, "fact_payment"))
            .start(),

        fact_notify.writeStream
            .outputMode("append")
            .foreachBatch(lambda df, _: write_to_clickhouse(df, "fact_notify"))
            .start(),

        fact_inventory.writeStream
            .outputMode("append")
            .foreachBatch(lambda df, _: write_to_clickhouse(df, "fact_inventory"))
            .start(),

        fact_etc.writeStream
            .outputMode("append")
            .foreachBatch(lambda df, _: write_to_clickhouse(df, "fact_etc"))
            .start()
    ]
