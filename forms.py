from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

class SearchForm(Form):
    right_ascension = TextField(
        'Right Ascension', validators=[DataRequired()]
    )
    declination = TextField(
        'Declination', validators=[DataRequired()]
    )
