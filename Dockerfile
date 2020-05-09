FROM ubuntu:latest
MAINTAINER Swapnil Lonkar "sl59640n@pace.edu"
RUN apt-get update && apt-get install -y
RUN apt install python3-pip -y
COPY . /app
WORKDIR /app
RUN pip3 install flask
ENTRYPOINT ["python3"]
CMD ["app.py"]