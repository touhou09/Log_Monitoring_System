"""
Log Simulator

다양한 형태의 테스트용 로그를 생성하여 Kafka로 전송하는 스크립트입니다.
부하 테스트 및 다양한 시나리오 검증을 목적으로 사용됩니다.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from config import TEMPLATE_DIR

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

class SimulatorBase(ABC):
    def __init__(self, template_file):
        self.template = env.get_template(template_file)

    @abstractmethod
    def generate_log(self, now: datetime) -> dict:
        pass

    def generate_logs(self, now: datetime, count: int) -> list:
        return [self.generate_log(now) for _ in range(count)]

    def render(self, data: dict) -> str:
        return self.template.render(**data)