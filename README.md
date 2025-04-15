# Log_Monitoring_System

Log_simulation을 활용하여 대규모 커머스 MSA 시스템의 로그를 실시간 모니터링하고 Batch 기반으로 트렌드 등을 정리할 수 있는 시스템을 구축하는 프로젝트이다.

## TODO
- ✔ 로그 시뮬레이터 설치

### 실시간 모니터링 시스템
- docker compose로 환경 구성
    - fluent
    - kafka
    - flink
    - clickhouse
    - grafana

- fluent와 kafka 연결
- fluent와 ls 연결
- clickhouse 구성
- flink 구성 
    - kafka - flink 연결
    - flink - clickhouse 연결

- grafana 구성 및 연결

### 배치 데이터 처리 시스템
- docker compose 구성 추가
    - airflow
    - spark scheduler
    - spark worker
    - IceBerg
    - minIO

- DAG 설계
- spark 연결 테스트
- 데이터 시각화 툴 아직 선택안함 -> 해볼것