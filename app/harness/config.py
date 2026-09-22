from __future__ import annotations

import os
from dataclasses import dataclass


def _env(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


@dataclass(frozen=True)
class Settings:
    env: str
    skin: str
    named_human: str
    named_role: str
    named_org: str
    demo_token: str
    tf_base_url: str
    tf_api_key: str
    tf_model_observe: str
    tf_model_judge: str
    tf_model_generate: str
    tf_endpoint_observe: str
    tf_endpoint_judge: str
    decision_backend: str
    auto_allow: bool

    @property
    def is_demo(self) -> bool:
        return self.env != "dev"


def load_settings() -> Settings:
    return Settings(
        env=_env("ENV", "demo"),
        skin=_env("SKIN", "stub"),
        named_human=_env("NAMED_HUMAN"),
        named_role=_env("NAMED_ROLE"),
        named_org=_env("NAMED_ORG"),
        demo_token=_env("DEMO_TOKEN"),
        tf_base_url=_env("TF_BASE_URL"),
        tf_api_key=_env("TF_API_KEY"),
        tf_model_observe=_env("TF_MODEL_OBSERVE", "Qwen/Qwen3-VL-8B-Instruct"),
        tf_model_judge=_env("TF_MODEL_JUDGE", "Qwen/Qwen3-8B"),
        tf_model_generate=_env("TF_MODEL_GENERATE", "Qwen/Qwen3-8B"),
        tf_endpoint_observe=_env("TF_ENDPOINT_OBSERVE"),
        tf_endpoint_judge=_env("TF_ENDPOINT_JUDGE"),
        decision_backend=_env("DECISION_BACKEND", "tf_json"),
        auto_allow=_env("AUTO_ALLOW", "0") == "1",
    )
