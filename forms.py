from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Regexp

class SearchForm(Form):
    right_ascension = TextField(
        'Right Ascension', validators=[DataRequired(), Regexp('^[0-9][0-9]h[0-9][0-9]m[0-9\.]+s$')]
    )
    declination = TextField(
        'Declination', validators=[DataRequired(), Regexp('^(\+|\-)?[0-9][0-9]d[0-9][0-9]m[0-9\.]+s$')]
    )
