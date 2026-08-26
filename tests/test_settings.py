from pathlib import Path

from algo_pro.config import Settings, TradingEnv


def test_settings_fixture_uses_temp_data_dir(settings: Settings) -> None:
    assert settings.data_dir.is_dir()
    assert settings.data_dir != Path("data")


def test_live_requires_env_and_flag() -> None:
    live_without_flag = Settings(
        _env_file=None,
        trading_env=TradingEnv.LIVE,
        live_trading_enabled=False,
    )
    assert live_without_flag.is_live is False

    flag_without_live_env = Settings(
        _env_file=None,
        trading_env=TradingEnv.PAPER,
        live_trading_enabled=True,
    )
    assert flag_without_live_env.is_live is False

    live = Settings(
        _env_file=None,
        trading_env=TradingEnv.LIVE,
        live_trading_enabled=True,
    )
    assert live.is_live is True


def test_empty_broker_secrets_are_none() -> None:
    settings = Settings(_env_file=None, broker_api_key="", broker_api_secret="")
    assert settings.broker_api_key is None
    assert settings.broker_api_secret is None
