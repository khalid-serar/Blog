from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField,TextAreaField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.validators import InputRequired


class CommentForm(FlaskForm):
    title = StringField('Comment title', validators = [InputRequired()])
    comment = TextAreaField('Comment review')
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField('Blog title', validators = [InputRequired()])
    content = TextAreaField('Blog content', validators = [InputRequired()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')    

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')    