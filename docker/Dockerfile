FROM python:3.8-slim-buster

ENV CITY_NAME=Москва
ENV OPENWEATHER_API_KEY=d0fc3409700ca80d231ea8402ca0b872

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . . 

ENTRYPOINT ["python3", "weather_api.py", "run"]