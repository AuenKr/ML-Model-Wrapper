FROM python:3.11.3-slim-buster

RUN apt-get update

RUN apt-get install ffmpeg libsm6 libxext6  -y

# Model Download https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx
COPY ./model/u2net.onnx /root/.u2net/u2net.onnx

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]