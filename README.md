<p align="center">
    <h1 align ="center"> Media Recommendation Engine</h1>
</p>
<a href="https://codecov.io/gh/tiangolo/fastapi" target="_blank">
    <img src="https://cdn.activestate.com/wp-content/uploads/2019/12/RecommendationEngine.png" alt="Coverage">
</a>
<p align="center">
    <em>Media Recommendation Engine, an API that recommends content such as movies, tv shows, anime, songs etc. Built with FastAPI.</em>
</p>
<p align="center">

<a href="https://codecov.io/gh/tiangolo/fastapi" target="_blank">
    <img src="https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/badge/sklearn-darkorange.svg?style=flat&logo=scikit-learn&logoColor=white" alt="Supported Python versions">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/badge/FastAPI-darkgreen.svg?style=flat&logo=fastapi&logoColor=white" alt="Supported Python versions">
</a>

<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white" alt="Supported Python versions">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat" alt="Supported Python versions">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/github/repo-size/Nneji123/Media-Recommendation-Engine" alt="Supported Python versions">
</a>
</p>

## Table of Contents
- [Features](#features)
- [API Reference](#api-reference)
- [Screenshots](#screenshots)
- [Demo](#demo)
- [Run on Local Machine](#running-on-local-machine-:computer:)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Technologies Used](#technologies-used)
- [FAQ](#faq)
- [License](#license)

## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform

## API Reference

#### Go to home directiory

```http
  GET /api/home
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.
## How it works


## Screenshots

## Demo


## Running on Local Machine :computer:

1. Clone the repository to your local machine:
```bash
git clone https://github.com/Nneji123/Media-Recommendation-Engine.git
```    

2. Install the requirements:
```bash
cd Media-Recommendation-Engine
pip install -r requirements.txt
```
3. Open a bash/cmd in the directory and run:
```
uvicorn app:app --reload --port 8000
```
4. After the above steps have been carried out you can now view the documentation of the API.

To visit the FastAPI documentation go to http://localhost:8000/docs with a web browser.
    
## Running Load Tests with Locust
1. Make sure the API is running already from the above steps.
2. Install locust:
```bash
pip install locust
```
3. Run locust tests
```bash
  cd tests
  locust -f locust_test_load.py
```
4. Set 



## Deployment
Assuming you have git and heroku cli installed just carry out the following steps:

1. Clone the repository

```
git clone https://github.com/Nneji123/Media-Recommendation-Engine.git
```

2. Change the working directory

```
cd Media-Recommendation-Engine
```

3. Create the heroku app

``` 
heroku create your-app-name 
```

Replace **your-app-name** with the name of your choosing.

4. Set the heroku cli git remote to that app

```
heroku git:remote your-app-name
```

5. Set the heroku stack setting to container
 
```
heroku stack:set container
```

6. Push to heroku
```
git push heroku main
```

## Contributing

Contributions are always welcome!

See `CONTRIBUTING.MD` for ways to get started.

Please adhere to this project's `code of conduct`.


## FAQ

#### What is this API used for?

This API can be used to suggest recommendations for an end user such as movies, games, songs etc.

#### Question 2

Answer 2

## License

[MIT](https://github.com/Nneji123/Media-Recommendation-Engine/blob/main/LICENSE)









