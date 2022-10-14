FROM python:3
WORKDIR /app

COPY requirements.txt requirements.txt
# RUN pip3 install csv 
# RUN pip3 install sqlite3
# RUN pip3 install pandas 
RUN pip3 install -r requirements.txt

COPY . . 
# COPY ./classify.py .
# COPY ./train.py .
