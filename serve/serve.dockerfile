ARG PYTHON_VERSION=3.10.2

FROM python:${PYTHON_VERSION}-slim as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY pyproject.toml poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM python:${PYTHON_VERSION}-slim as build-stage

WORKDIR /serve

COPY --from=requirements-stage /tmp/requirements.txt /serve/requirements.txt

RUN pip install --no-cache-dir -r /serve/requirements.txt

COPY . /serve

EXPOSE 8000

CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "8000", "app.main:app" ]