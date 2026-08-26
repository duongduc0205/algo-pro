import sys

import numpy
import pandas
import pydantic_settings

import algo_pro
from algo_pro.config import Settings, TradingEnv


def test_python_version() -> None:
    assert sys.version_info >= (3, 12)


def test_core_imports() -> None:
    assert algo_pro.__name__ == "algo_pro"
    assert numpy.__name__ == "numpy"
    assert pandas.__name__ == "pandas"
    assert pydantic_settings.__name__ == "pydantic_settings"


def test_default_settings_are_not_live() -> None:
    settings = Settings(_env_file=None)
    assert settings.trading_env is TradingEnv.DEVELOPMENT
    assert settings.live_trading_enabled is False
    assert settings.is_live is False
