from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    description = TextField('Description', widget=TextArea())
    photo = FileField('Image', validators=[
        FileRequired(),
         FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])