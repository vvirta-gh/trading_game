FROM python:3.12-slim AS base

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

# Copy the rest of the application
COPY . .

EXPOSE 8000

CMD ["uv", "run", "trading-game"]