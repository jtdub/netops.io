FROM python:3.10-slim-bullseye

ENV PATH="${PATH}:/root/.local/bin"

EXPOSE 8000

WORKDIR /opt/netopsio

VOLUME /opt/netopsio

COPY ../pyproject.toml .

COPY ../poetry.lock .

# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends nmap iputils-ping traceroute curl mariadb-client libmariadb-dev gcc && \
    apt-get autoremove -y && \
    apt-get clean all && \
    rm -rf /var/lib/apt/lists/*

# hadolint ignore=DL3059
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -o /tmp/install-poetry.py && \
    python /tmp/install-poetry.py && \
    rm -f /tmp/install-poetry.py

# hadolint ignore=DL3059
RUN poetry config virtualenvs.create false && \
    poetry config installer.parallel false && \
    poetry install
