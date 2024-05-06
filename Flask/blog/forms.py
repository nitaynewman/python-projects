from wtforms import StringField, SubmitField, DateField, URLField
from wtforms.validators import DataRequired, URL
from flask_wtf import FlaskForm

class CreatePostForm(FlaskForm):
    title = StringField("enter title", validators=[DataRequired()])
    subtitle=StringField("enter subtitle", validators=[DataRequired()])
    body=StringField("enter text", validators=[DataRequired()])
    img_url=URLField("enter URL", validators=[DataRequired(), URL()])
    author=StringField("enter name of the author", validators=[DataRequired()])
    date=DateField("enter date", validators=[DataRequired()])
    submit = SubmitField()