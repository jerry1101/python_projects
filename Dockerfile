FROM python:alpine3.6

#add app folder and assign working folder
RUN mkdir /app
WORKDIR /app

#install python
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
#copy source code
COPY . .
#optional
LABEL maintainer="jerry11 <jhung@totalwine.com>" \
      version="1.0"
# commands to start server
CMD [ "python", "./comp1.py" ]
