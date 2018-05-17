FROM python:3.6
ADD src /server
ADD requirements.txt /server/requirements.txt
WORKDIR /server
RUN pip install -r requirements.txt