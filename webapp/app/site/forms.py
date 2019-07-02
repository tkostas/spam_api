from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    text_area = TextAreaField('Message', render_kw={'rows': 10}, validators=[DataRequired()])
    submit = SubmitField('Submit text', id="msg-btn")
