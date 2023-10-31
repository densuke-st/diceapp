FROM python:alpine3.12
WORKDIR /work
COPY app.py .
RUN pip install bottle
EXPOSE 80
CMD ["python", "app.py"]
