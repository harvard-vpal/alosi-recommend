FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY ./requirements/ ./requirements/
RUN pip install -r requirements/requirements.txt
ADD . ./

EXPOSE 8000
