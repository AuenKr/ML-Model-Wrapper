### Model Wrapper

Wrap the ML model and provide the http endpoint

1. Object detection endpoint

> POST /object

    Input
    ```
    form data :
    {
        image : "path_to_image"
    }
    ```

    Output
    ```
    {
    "result": [
        {
            "bounding_box": {
                "height": 270,
                "origin_x": 100,
                "origin_y": 65,
                "width": 363
            },
            "categories": [
                {
                    "category_name": "cat",
                    "display_name": "",
                    "index": 16,
                    "score": 0.6875
                }
            ]
        },
        {
            "bounding_box": {
                "height": 174,
                "origin_x": 28,
                "origin_y": 216,
                "width": 579
            },
            "categories": [
                {
                    "category_name": "couch",
                    "display_name": "",
                    "index": 62,
                    "score": 0.4609375
                }
            ]
        }]
    }

2. Movie Suggestion endpoint

> POST /movies

    Input
    ```
    Body data :
    {
        "movie_title": "Movie_name",
        "count": No_of_suggested_movies
    }
    ```

    Output
    ```
    {
        "movies": [
            "Batman Returns",
            "The Dark Knight Rises",
            "The Dark Knight",
            "Batman Begins",
            "Batman Forever"
        ]
    }



### To run locally

> Normal Install

1. Install python

2. Add virtual env (optional)

3. `pip install -r requirements.txt`

4. Add default model `python server/model/movieRecommendationModel.py`

5. `python server/app.py`

> With Docker

1. On linux `docker compose up`

2. On Windows `docker-compose up`
