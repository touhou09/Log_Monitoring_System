FROM bitnami/spark:3.5

WORKDIR /app

COPY app.py /app/app.py

# 추가 패키지 설치 필요시 아래처럼 설정 가능
USER root
RUN pip install --upgrade pip && \
    pip install pyspark

USER 1001
