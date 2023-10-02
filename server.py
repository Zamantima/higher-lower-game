from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media1.giphy.com/media/IgBMDZCU5IRUFKGhpy/giphy.gif?cid=ecf05e4745nuejkvy1v5jnv9nz8mjhi3uast66cn5nodho13&ep=v1_gifs_related&rid=giphy.gif&ct=g'>"

@app.route("/<int:user_input>")
def user_guess(user_input):
    rand_num = random.randint(0,9)
    if rand_num > user_input:
        return "<h2> Too Low, try again!</h2>" \
               "<img src='https://media4.giphy.com/media/UMngtBP8VVDfZXacO8/giphy.gif?cid=ecf05e47wakul89gvffmsz828lv8evbrlor49wxtl1l3og6f&ep=v1_gifs_related&rid=giphy.gif&ct=g'>"
    elif rand_num < user_input:
        return "<h2> Too High, try again!</h2>" \
               "<img src='https://media0.giphy.com/media/d2gFGczwI6R2zCG6xK/giphy.gif?cid=ecf05e47wakul89gvffmsz828lv8evbrlor49wxtl1l3og6f&ep=v1_gifs_related&rid=giphy.gif&ct=g'>"
    else:
        return "<h2> You found me</h2>" \
               "<img src='https://media2.giphy.com/media/3ofSBgqPwM6R31U3YY/giphy.gif?cid=ecf05e47l7hyj1qoarc8d0nebctspzfj2ca0rds5uhuyn98s&ep=v1_gifs_related&rid=giphy.gif&ct=g'>"




if __name__ == "__main__":
    app.run(port=8000, debug=True)
