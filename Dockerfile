FROM python:3.9


RUN mkdir -p /opt/app
COPY . /opt/app
WORKDIR /opt/app

RUN pip install -r requirements.txt
#CMD ["cd", "opentutorials"] #프로젝트 폴더 이동
CMD ["/opt/app/start-dev-server.sh"]

EXPOSE 8000
