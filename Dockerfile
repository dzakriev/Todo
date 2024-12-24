FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir  --upgrade -r requirements.txt

COPY . .

VOLUME app/data

CMD ["fastapi", "run", "main.py", "--port", "80"]
