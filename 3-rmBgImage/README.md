A simple flask app to remove the background of an image with [Rembg](https://github.com/danielgatis/rembg) model

### Usage

> Using docker (no need to install)

`docker run -p 5000:5000 auenkr/rm-image-bg`

### To run locally

## Note
`
Download the model and save as in ./model/u2net.onnx

Model : https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx
`

> Normal Install

1. Install python

2. Add virtual env (optional)

3. `pip install -r requirements.txt`

4. `python app.py`

5. Open [http://localhost:5000/](http://localhost:5000/)

> With Docker

1a. On linux `docker compose up`

1b. On Windows `docker-compose up`

2. Open [http://localhost:5000/](http://localhost:5000/)