FROM python:3.9-alpine
  
WORKDIR py_med

COPY requirements.txt requirements.txt
COPY medicine.py medicine.py

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "medicine.py"]