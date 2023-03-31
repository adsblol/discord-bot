FROM python:3-alpine

WORKDIR /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

STOPSIGNAL SIGKILL
CMD ["python3", "app.py"]
ENV PYTHONUNBUFFERED=1
