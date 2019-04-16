from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed


class DataLoaderForm(FlaskForm):
    gen_data = FileField('Gen File', validators=[FileAllowed(['txt', 'csv'])] )

