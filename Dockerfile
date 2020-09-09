FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10

RUN pip3 install --no-cache-dir fastapi uvicorn

COPY ./app /app

# EXPOSE 80

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
