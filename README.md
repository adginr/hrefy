# Short link project

Sample project of link shorter in portfolio
[Demo Youtube Vide](https://www.youtube.com/watch?v=6Bf0E708Y3U)

## Features

- Create short link with lifetime constrain
- Update short name
- Update lifetime
- Remove link

## Extra

- Short link is always unique
- Links Lifetime within 1 and 365 day

### Install with docker

```sh
cd hrefy
docker-compose up
```

### Alternative Install

```sh
# Before install you should have at least:
yarn --version
1.22.17
poetry --version
1.11.13
python3 --version
3.10.2
node --vesion
16.13.2
```

```bash
# Get last copy of the project
# SSH
git clone git@github.com:kolin-engineer/hrefy.git
# or HTTPS
git clone https://github.com/kolin-engineer/hrefy.git
```

```bash
# [1]
# install dependecies
cd client
yarn install # or npm install
yarn dev # or npm run dev

cd ../serve
# [2]
poetry shell
poetry install
# or
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

# Make migrations
alembic upgrade head # creates sqlite3 db

# Run test
pytest -v

# start server
uvicorn app.main:app --reload
```

## Explore

```sh
http://localhost:8000/docs # OpenAPI
http://localhost:3000 # Client side
```

#### backend stack:

- python@3.10
- fastapi@0.74
- sqlalchemy@1.4
- uvicorn

#### front stack:

- vue3 (vite pm)
- tailwindcss
- bulma
- ohmyfetch

> None: Tested on python3.10
