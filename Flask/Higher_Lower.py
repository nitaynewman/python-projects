from flask import Flask
import random


num = random.randint(0, 9)
print(num)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1><b>Guess a number between 0 and 9</b></h1> <img href="https://media.giphy.com/media/b6mOpV0p0GgQ37T9m0/giphy.gif"/>'

@app.route('/<int:guess>/')
def guess_number(guess):
  if guess == num:
    return '<h1><b>You guessed it!</b></h1> <img href="https://media.giphy.com/media/L5ALYguzXR5rW/giphy-downsized-large.gif />'
  elif guess > num:
    return '<h1><b>You guessed to high!</b></h1> <img href="https://media.giphy.com/media/gvTYmbKCwkaly/giphy.gif />'
  else:
    return '<h1><b>You guessed to low!</b></h1> <img href="https://media.giphy.com/media/HSvpy6Jk396SI/giphy.gif />'

if __name__ == '__main__':
    app.run(debug=True)