FROM python:3.10.14
ENV PYTHONUNBUFFERED 1

WORKDIR /usr

RUN pip install --upgrade pip

#RUN pip install unsloth

RUN pip install --upgrade pip
RUN pip install "unsloth[cu124-torch250] @ git+https://github.com/unslothai/unsloth.git"

RUN pip install pandas

RUN apt-get update
RUN apt-get install -y cmake

EXPOSE 8080
CMD [ "python", "/usr/tuning/fine_tune.py" ]