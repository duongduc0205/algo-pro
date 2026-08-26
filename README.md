# Algo Pro

Modular Python system for market data, research, backtesting, paper trading, and live execution. Live trading is never enabled by default.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Setup

```powershell
uv sync --group dev
Copy-Item .env.example .env
```

Edit `.env` for local paths and credentials. Do not commit `.env`.

## Commands

```powershell
uv run pytest
uv run ruff check .
uv run algo-pro
```

## Trading modes

`TRADING_ENV` may be `development`, `research`, `backtest`, `paper`, or `live`.

Live execution requires **both**:

- `TRADING_ENV=live`
- `LIVE_TRADING_ENABLED=true`

Copying `.env.example` leaves live trading off.
