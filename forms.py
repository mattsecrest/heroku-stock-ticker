from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class stockInput(FlaskForm):
    symbol = StringField('Symbol',
                           validators=[DataRequired(), Length(min=1, max=5)])
    month = StringField('Month',
                        validators=[DataRequired(), Length(min=1,max=10)])
    year = StringField('Year', 
                        validators=[DataRequired(), Length(min=2,max=4)])
    submit = SubmitField('Confirm')

class goBack(FlaskForm):
    back = SubmitField("Back")