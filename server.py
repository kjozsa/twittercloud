from flask import Flask
from flask import send_file
from threading import Thread
from io import BytesIO

import wcloud
from twitter_fetch import fetch_tweets

app = Flask(__name__)


@app.route('/')
def static_from_file():
    with open('input.txt', 'r') as file:
        text = file.read().replace('\n', '')
    image = wcloud.render2image(text)
    return serve_pil_image(image)


@app.route('/<username>')
def index(username):
    text = fetch_tweets(username)
    image = wcloud.render2image(text)
    return serve_pil_image(image)


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


if __name__ == '__main__':
    Thread(target=app.run).run()
