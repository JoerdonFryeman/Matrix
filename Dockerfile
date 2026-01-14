FROM python:3.13-alpine
WORKDIR /app
COPY main.py .
COPY core/ ./core
CMD ["python", "main.py"]