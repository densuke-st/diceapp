FROM python:alpine3.12
WORKDIR /work
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]
