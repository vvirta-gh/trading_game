# Trading Game

A small Python 3.12 project simulating basic stock trading mechanics with a simple Rich-powered CLI. Includes unit tests for the pricing engine and a Docker image. Uses uv for packaging and lockfile management.

![CI](https://github.com/vvirta-gh/trading-game/actions/workflows/ci.yml/badge.svg?branch=main)

## Features

- Stock model with buy/sell price dynamics (configurable)
- Player model and basic game loop with a menu UI
- Rich-based terminal UI components (work in progress)
- Pytest test suite with coverage
- Reproducible installs with uv and lockfile
- GitHub Actions CI (tests + Docker build/publish)

## Requirements

- Python 3.12+
- uv (recommended) or pip

## Quick Start

- Clone the repo and open a terminal in the project root.

Install dependencies with uv (recommended)

- `uv sync --frozen`

Alternatively with pip:

- `python -m venv .venv && source .venv/bin/activate`
- `pip install -e .`

Run the CLI entrypoint (demo)

- `uv run demo-game`  # starts the menu UI from `app.game`

## Other scripts

- `uv run trading-game`  # logs a random number (current default entry)
- `uv run test`          # run all tests
- `uv run test-stock`    # run stock tests only
- `uv run test-player`   # run player tests only

## Running Tests

- `uv run pytest -q --maxfail=1 --disable-warnings --cov --cov-report=term-missing`

## Format check (Black)

- `uv run black --check .`
- To format: `uv run black .`

## Docker

Build locally:

- `docker build -t trading-game:local .`

Run (uses the project's default script entry `trading-game`):

- `docker run --rm -it trading-game:local`

Note: The Dockerfile currently runs `uv run trading-game`. To start the menu game by default, either run `uv run demo-game` inside the container or change the final CMD to that command.

## Configuration

Stock pricing parameters are defined in `app/config/stock_config.py`:

- `price_change_weights` – weights for market impact, scarcity, log factor, volatility
- `market_sensitivity`, `volatility_range`, `max_price_change`, `normal_supply`

Game/UI constants in `app/utils/constants.py`.

## CI/CD

### GitHub Actions workflow at `.github/workflows/ci.yml`

- Test job: installs dependencies with uv, checks formatting (Black), runs pytest with coverage
- Docker jobs: on push to `main`, builds and pushes an image to GHCR (`ghcr.io/<owner>/<repo>`); on version tags `v*.*.*`, publishes semver tags

To enable image publishing, ensure GitHub Packages (GHCR) is enabled for the repository/organization. The workflow uses the built-in `GITHUB_TOKEN` with `packages: write` permission.

### Project Structure

- `app/models/` – Core domain models (`Stock`, `Player`)
- `app/config/` – Tweakable pricing configuration
- `app/utils/` – UI/game constants
- `app/ui/` – UI components and interface (WIP)
- `app/game.py` – Menu-based game loop (interactive)
- `app/main.py` – Simple example entry (script target `trading-game`)
- `tests/` – Unit tests

### Roadmap

- Add a Docker image to the repository
- Implement portfolio view and leaderboard
- Position tracking in `Player` (quantities, average cost)
- Align game defaults with constants and tests
- Improve CLI UX and error handling

    > Tip: Replace `vvirta-gh/trading-game` in the CI badge URL with your actual GitHub slug to show build status.
