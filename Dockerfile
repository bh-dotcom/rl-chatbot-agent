FROM python:3.10-slim
WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r server/requirements.txt
RUN pip install --no-cache-dir -r frontend/requirements.txt

RUN chmod +x start.sh

EXPOSE 8000 8501
CMD ["./start.sh"]
