FROM python:3.6.8
MAINTAINER Yanuz Nurchalik
RUN mkdir /backend
COPY . /backend
RUN pip install -r /backend/requirements.txt
WORKDIR /backend
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
