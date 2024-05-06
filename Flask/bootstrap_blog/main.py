from flask import Flask, render_template, request
import smtplib
import requests

# the link to the json data: https://www.npoint.io/docs/086dce16d96c242c69ed
posts = requests.get('https://api.npoint.io/086dce16d96c242c69ed').json()


app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

PASSWORD = 'nitay2k1'
EMAIL = 'nitaynewman@gmail.com'

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)



def send_email(name, email, phone, message):
    email_message = f'Subject: New Blog Message \n\nName: {name} \nEmail: {email} \nPhone: {phone} \nMessage: {message}'
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=email_message)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, image=requested_post['image'])

if __name__ == "__main__":
    app.run(debug=True)