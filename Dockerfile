FROM python:3.11.4 as builder


WORKDIR /app

COPY requirements.txt ./

RUN --mount=target=/var/lib/apt/lists,type=cache,sharing=locked \
    --mount=target=/var/cache/apt,type=cache,sharing=locked \
    rm -f /etc/apt/apt.conf.d/docker-clean && \
    apt-get update && \
    apt-get install -y build-essential

RUN --mount=type=cache,target=/root/.cache/pip \
    python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip setuptools && \
    /opt/venv/bin/pip install --use-feature=fast-deps --prefer-binary --no-cache-dir -r requirements.txt

FROM python:3.11.4-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY ./ /app

RUN adduser ubuntu

RUN chown -R ubuntu:ubuntu /app
RUN chmod -R 755 /app
RUN chmod +x ./scripts/*


USER ubuntu

CMD ["bash", "scripts/entrypoint.sh"]
