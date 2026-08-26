from enum import StrEnum
from functools import lru_cache
from pathlib import Path

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class TradingEnv(StrEnum):
    DEVELOPMENT = "development"
    RESEARCH = "research"
    BACKTEST = "backtest"
    PAPER = "paper"
    LIVE = "live"


class Settings(BaseSettings):
    """Runtime settings. Live trading requires an explicit env and flag."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    trading_env: TradingEnv = TradingEnv.DEVELOPMENT
    live_trading_enabled: bool = False
    broker_api_key: SecretStr | None = None
    broker_api_secret: SecretStr | None = None
    data_dir: Path = Field(default=Path("data"))

    @field_validator("broker_api_key", "broker_api_secret", mode="before")
    @classmethod
    def empty_secret_to_none(cls, value: object) -> object:
        if value == "":
            return None
        return value

    @property
    def is_live(self) -> bool:
        return self.trading_env is TradingEnv.LIVE and self.live_trading_enabled


@lru_cache
def get_settings() -> Settings:
    return Settings()
