CREATE DATABASE IF NOT EXISTS analytics;

CREATE TABLE analytics.fact_auth (
    timestamp DateTime,
    user_id String,
    level String
) ENGINE = MergeTree() ORDER BY timestamp;

CREATE TABLE analytics.fact_order (
    timestamp DateTime,
    user_id String,
    product_id String,
    level String
) ENGINE = MergeTree() ORDER BY timestamp;

CREATE TABLE analytics.fact_payment (
    timestamp DateTime,
    user_id String,
    amount UInt32,
    level String
) ENGINE = MergeTree() ORDER BY timestamp;

CREATE TABLE analytics.fact_notify (
    timestamp DateTime,
    user_id String,
    notif_type String,
    level String
) ENGINE = MergeTree() ORDER BY timestamp;

CREATE TABLE analytics.fact_inventory (
    timestamp DateTime,
    item_id String,
    remaining UInt8,
    level String
) ENGINE = MergeTree() ORDER BY timestamp;

CREATE TABLE analytics.fact_etc (
    timestamp DateTime,
    domain String,
    level String
) ENGINE = MergeTree() ORDER BY timestamp;

CREATE TABLE analytics.dim_user (
    user_id String
) ENGINE = MergeTree() ORDER BY user_id;

CREATE TABLE analytics.dim_item (
    item_id String,
    product_id String
) ENGINE = MergeTree() ORDER BY item_id;

CREATE TABLE analytics.dim_status (
    level String
) ENGINE = MergeTree() ORDER BY level;

CREATE TABLE analytics.dim_logger (
    logger String
) ENGINE = MergeTree() ORDER BY logger;

CREATE TABLE analytics.dim_time (
    timestamp DateTime,
    year UInt16,
    month UInt8,
    day UInt8,
    hour UInt8,
    minute UInt8
) ENGINE = MergeTree() ORDER BY timestamp;

CREATE TABLE analytics.dim_domain (
    domain String
) ENGINE = MergeTree() ORDER BY domain;