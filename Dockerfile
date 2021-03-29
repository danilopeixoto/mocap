FROM python:3.6

LABEL description "A real-time application to capture and stream hand motion data."
LABEL version "1.0.0"
LABEL maintainer "Danilo Peixoto <danilopeixoto@outlook.com>"

WORKDIR /usr/src/mocap/
COPY . .

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install --upgrade pip && pip install .
RUN rm -rf /usr/src/mocap/

ENTRYPOINT ["mocap"]
