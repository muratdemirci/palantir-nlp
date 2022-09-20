# Palantir NLP service

A REST API for communicate [data crawler service](https://github.com/muratdemirci/palantir-crawler).
Makes sentimental analysis on crawled text of tweets and provides polarity score.

> Uses PostgreSQL as its database and makes authentication with (jwt).

## Libraries and tools used

- [NLTK](https://pypi.org/project/nltk/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)

### Getting Started

Clone this repository and install dependencies

```
> git clone https://github.com/muratdemirci/palantir-nlp.git
> cd palantir-nlp

> pip install flask
> pip install nltk
```

Go to python console and download dataset, if you're using [NLTK](https://pypi.org/project/nltk/) for the first time

#### Run development

```
>>> import nltk

>>> nltk.download([
    "names",
    "stopwords",
    "state_union",
    "twitter_samples",
    "movie_reviews",
    "averaged_perceptron_tagger",
    "vader_lexicon",
    "punkt",
])

>>> exit()
```

#### Build and run for production

```
>>> flask run

### API documentation

## User sends data and api return polarity score

### Request

`POST http://localhost:5000/data`

    curl -i -H 'Accept: application/json' -d 'text=I love bitcoin' http://localhost:5000/data

### Response

    HTTP/1.1 201 Created
    Date: Sun, 18 Sep 2022 12:36:31 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /data/2
    Content-Length: 35

{
    "score": 0.6369,
    "success": true
}
```

# Licence

MIT

### About this project

Palantir is a micro-saas project which is analyses tweets of crypto influencers to predict the direction of the market.  
This project was made for [Teknasyon Hackathon '22 - Yüzük Kardeşliği](https://teknasyon.com/tech/hackathon22/#/).  
We took 2nd place among 13 teams.  
![mordor idman yurdu :)](https://raw.githubusercontent.com/muratdemirci/palantir-be/dio/hackathonwin.jpeg "mordor idman yurdu :))")
