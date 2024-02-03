FROM python:3.10
WORKDIR /usr/src/bot
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]