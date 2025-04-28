FROM python:latest

RUN apt-get update
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./ ./
ENTRYPOINT ["python", "runall.py"]
