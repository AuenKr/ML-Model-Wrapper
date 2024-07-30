FROM python:3.11.3-slim-buster

RUN apt-get update && apt-get install -y libusb-1.0-0-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# To generate movie Suggestion model
RUN python server/model/movieRecommendationModel.py

EXPOSE 5000

CMD [ "flask", "--app", "server/app.py", "run", "--host=0.0.0.0", "--debug" ]


