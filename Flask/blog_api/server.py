from flask import Flask, render_template, redirect, url_for
from flask import requests
from post import Post
import datetime as dt


year = dt.datetime.now().year

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("blogs.html", all_posts=post_objects, year=year)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=year)


if __name__ == "__main__":
    app.run(debug=True)