FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .


RUN flask init-db
RUN python main.py


EXPOSE 5000
CMD ["python", "app.py"]