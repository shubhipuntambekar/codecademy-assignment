FROM python:3.11-bookworm
LABEL authors="shubhi"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV NAME dev

CMD ["python", "app.py"]