FROM alpine
 
WORKDIR /usr/local/av-project

ADD . .

RUN apk add gcc python3 py3-pip python3-dev musl-dev linux-headers g++ libffi-dev openssl-dev # tini

RUN pip3 install -r requirements.txt

ENV FLASK_APP=av-project
ENV FLASK_ENV=development

EXPOSE 5000

CMD [ "python","compile_rules.py"]
CMD [ "python","api_flask_app.py"]
