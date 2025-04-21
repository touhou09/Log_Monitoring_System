import asyncio
import aiohttp
from kafka import KafkaProducer
import json

# 🚀 시뮬레이터에서 사용하는 서비스 이름 기준
SERVICES = [
    "order",
    "payment",
    "inventory",
    "notify",
    "auth",
    "etc"
]

KAFKA_HOST = "kafka:9092"
API_BASE = "http://log_simulator:8000/stream"

def get_topic_name(service: str) -> str:
    return f"{service}_topic"

async def forward_stream(service: str, topic: str, producer: KafkaProducer):
    url = f"{API_BASE}/{service}"
    print(f"[forwarder] connecting to {url} → Kafka({topic})")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                async for line in resp.content:
                    msg = line.decode("utf-8").strip()
                    if msg:
                        print(f"[→Kafka] {topic}: {msg}")
                        producer.send(topic, {
                            "service": service,
                            "message": msg
                        })
    except Exception as e:
        print(f"[error] failed to connect to {url}: {e}")

async def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_HOST,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

    tasks = []
    for service in SERVICES:
        topic = get_topic_name(service)
        tasks.append(forward_stream(service, topic, producer))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())