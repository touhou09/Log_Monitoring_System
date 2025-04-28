FROM bitnami/spark:3.5

USER root

# 필요한 유틸리티 설치 + ClickHouse JAR 다운로드 + pip 설치
RUN apt-get update && \
    apt-get install -y wget curl && \
    wget https://repo1.maven.org/maven2/com/clickhouse/clickhouse-jdbc/0.4.6/clickhouse-jdbc-0.4.6.jar \
    -P /opt/bitnami/spark/jars && \
    pip install --upgrade pip && \
    pip install pyspark

USER 1001

# 애플리케이션 복사
WORKDIR /app
COPY . /app
ENV PYTHONPATH="/app"