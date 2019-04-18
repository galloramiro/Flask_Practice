from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed


class DataLoaderForm(FlaskForm):
    gen_data = FileField('Gen File', validators=[FileAllowed(['txt', 'csv'])] )
    submit = SubmitField('Update')

