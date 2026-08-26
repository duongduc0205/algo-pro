from algo_pro.config import Settings, get_settings


def main() -> None:
    settings = get_settings()
    print(f"algo-pro [{settings.trading_env}] live={settings.is_live}")


__all__ = ["Settings", "get_settings", "main"]
