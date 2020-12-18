FROM python:3.7.5-buster

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install --upgrade pipenv

COPY airflow-dev/Pipfile.lock .
COPY airflow-dev/Pipfile .
RUN pipenv install --system --ignore-pipfile --deploy

RUN mkdir -p /root/airflow/dags

ADD . /root/airflow/dags

COPY airflow-dev/entrypoint.sh .

CMD ./entrypoint.sh
