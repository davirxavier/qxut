FROM python:3.8
ARG DockerHOME=/home/app/webapp
ARG TempHOME=/tmp/qxut

RUN mkdir -p $DockerHOME
RUN mkdir -p $TempHOME

COPY requirements.txt $TempHOME
WORKDIR $TempHOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENABLE_REMOTE_DB "True"
ENV DATABASE_URL ""

COPY . $DockerHOME
COPY --chmod=0755 *.sh $DockerHOME
EXPOSE 8000
ENTRYPOINT ["/home/app/webapp/entrypoint.sh"]