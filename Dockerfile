FROM python:3.6.1-alpine
RUN pip install flask
COPY sequencia_fibo.py /sequencia_fibo.py
CMD ["python","sequencia_fibo.py"]
