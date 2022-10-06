from python
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/DanteOnline/hack-the-python.git
WORKDIR ./hack-the-python
RUN pip install -r requirements.txt
ENTRYPOINT python runall.py
