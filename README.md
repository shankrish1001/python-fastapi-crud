python-fastapi-crud/
├── main.py
├── database.py
├── models.py
├── schemas.py
└── crud.py


Install uvicorn
pip install uvicorn

Required packages:
pip install fastapi uvicorn sqlalchemy psycopg2-binary

Run the App
uvicorn main:app --reload

Swagger UI:
http://127.0.0.1:8000/docs

