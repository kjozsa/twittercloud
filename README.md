## Playing around with Twitter + WordCloud API

![](https://raw.githubusercontent.com/kjozsa/twittercloud/main/sample.png)

## Setup 
(use `virtualenv` if you know it..)
```
export TWITTER_CONSUMER_KEY=<your_key>
export TWITTER_CONSUMER_SECRET=<your_secret>
pip install -f requirements.txt
python server.py
```

## Usage
* `http://localhost:5000/` - render sample content
* `http://localhost:5000/<twitter_username>` - render real content from Twitter
