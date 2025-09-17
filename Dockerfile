# syntax=docker/dockerfile:1.4


# Stage 1: build
FROM python:3.13-slim-bookworm AS build

RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv

WORKDIR /src
COPY pyproject.toml uv.lock README.md ./

RUN uv sync --frozen

COPY ./app ./app
COPY ./tests ./tests

RUN uv build


# Stage 2: development
FROM python:3.13-slim-bookworm AS development

ARG UID=1000
ARG GID=1000

RUN groupadd -g ${GID} -r devgroup && \
    useradd -u ${UID} -g devgroup devuser

# Install uv in development stage
RUN pip install uv

COPY --from=build --chown=${UID}:${GID} /src /src
COPY pyproject.toml uv.lock README.md ./

RUN mkdir -p /home/devuser && chown -R devuser:devgroup /home/devuser


USER devuser

ENV PATH=/src/.venv/bin:$PATH
ENV PYTHONPATH=/src
ENV UV_PROJECT_ENVIRONMENT=/src/.venv
ENV UV_CACHE_DIR=/home/devuser/.cache/uv

CMD ["uv", "run", "trading-game"]