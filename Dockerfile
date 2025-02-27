FROM python:3.10
ENV PYTHONUNBUFFERED 1

WORKDIR /usr

COPY requirements.txt /usr

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "python", "api/main.py" ]