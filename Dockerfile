FROM python:latest

WORKDIR /

COPY main.py ./
COPY pyproject.toml ./
COPY poetry.lock ./
COPY app/ ./app/

RUN apt update
RUN apt install curl -y
RUN curl -sSL https://install.python-poetry.org | python -

RUN ~/.local/share/pypoetry/venv/bin/poetry config virtualenvs.create false
RUN ~/.local/share/pypoetry/venv/bin/poetry install

CMD ["python", "-u", "main.py"]
