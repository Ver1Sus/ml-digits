# ML-digits
FastAPI project (Python 3.9) with pretrained SVM.
Provides versionized routes for digit recognition from data-array, or picture (`image` group).
SQLite DB contain requests, prediction time, response, which used for analytic routes (`analytics` group).
Also, `healtcheck` for requirement monitoring

## Project map
```
ml-digits/
├── app/
│   ├── main.py                    # Entry point for the FastAPI app
│   ├── api/                       
│   │   ├── v1/                    # Version 1 of your API 
│   │   │   ├── endpoints/         # Contains all the endpoint route handlers
│   │   │   ├── models/            # Contains SVM (for future - Pydantic models and database models)
│   │   │   ├── schemas/           # Pydantic schemas for request and response validation
│   │   │   ├── services/          # Business logic, processing image mechanism
│   │   │   ├── utils/             # Reusable functions
│   │   ├── config.py              # Configuration settings
│
└── tests/                         # API tests and unit-tests
```


## How to run
### cmd
1. Use python3.9
2. Install poetry `pip install poetry`
3. Install dependencies `poetry install --without test --no-root`
4. Start the app `uvicorn app.main:app  --host 0.0.0.0 --port 8001 --reload`
5. Visit http://127.0.0.1:8000/docs for openapi

### Docker
1. `docker build -t ml-digits .`
2. `docker run -ti -p 8000:8000 ml-digits`
3. Visit http://127.0.0.1:8000/docs for openapi


## TODO
1. Queue manager (Kafka) between DB, if the project expected high RPS.
2. ORM (SQLAlchemy), if the project expected scaling or complicated relationships.
3. Auth, if the project expected security.
