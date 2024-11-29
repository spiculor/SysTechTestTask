
FROM python:3.10


WORKDIR /app


COPY ./app /app/app
COPY ./tests /app/tests
COPY ./requirements.txt /app/requirements.txt
COPY ./data.txt /app/data.txt


RUN pip install --no-cache-dir -r /app/requirements.txt


RUN python -m spacy download ru_core_news_sm


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

