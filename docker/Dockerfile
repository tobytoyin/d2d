FROM ubuntu:latest

ARG PYTHON_VERSION=3.11

# setup linux & pythonX version
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install -y python${PYTHON_VERSION} python-is-python3

# set alias
RUN echo 'alias python3=python${PYTHON_VERSION}' >> ~/.bashrc
RUN echo 'alias python=python${PYTHON_VERSION}' >> ~/.bashrc

# install pip
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install poetry setuptools

# # move contents
WORKDIR /working
COPY . /working

# install requirements
# depending on poetry or pip
RUN poetry env use python${PYTHON_VERSION} \
    && poetry install --with dev

ENTRYPOINT [ "/bin/bash" ]
