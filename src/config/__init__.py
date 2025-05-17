from dynaconf import Dynaconf, ValidationError, Validator


settings = Dynaconf(
    settings_files=['settings.toml', '.secrets.toml'],
    validators=[
        Validator('kafka.bootstrap_servers', must_exist=True, messages={"must_exist_true": "Kafka bootstrap servers must be set."}),
        Validator('kafka.client_id', must_exist=True, messages={"must_exist_true": "Kafka client id must be set."}),
        Validator('kafka.group_id', must_exist=True, messages={"must_exist_true": "Kafka group id must be set."}),
        Validator('kafka.auto_offset_reset', must_exist=True, messages={"must_exist_true": "Kafka auto_offset_reset must be set."}),
        Validator('kafka.topic', must_exist=True, messages={"must_exist_true": "Kafka topic must be set."}),
    ]
)