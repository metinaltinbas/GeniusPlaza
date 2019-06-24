FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/development.txt \
    && rm -rf /requirements

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ADD . /code/
