from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from stockTicker import stockExists, mmdict_tf

class stockInput(FlaskForm):
    symbol = StringField('Symbol',
                           validators=[DataRequired(), Length(min=1, max=5)])
                           
    def validate_symbol(self,field):
        if not stockExists(field.data):
            raise ValidationError("Stock does not exist")
                           
    month = StringField('Month',
                        validators=[DataRequired(), Length(min=1,max=10)])
    def validate_month(self,field):
        if not mmdict_tf(field.data):
            raise ValidationError("Month is not correct format")
                        
    year = StringField('Year', 
                        validators=[DataRequired(), Length(min=4,max=4)])
    def validate_year(self,field):
        if field.data not in [str(i) for i in list(range(1900,2018))]:
            raise ValidationError("Year is not correct format")
                  
    submit = SubmitField('Confirm')

class goBack(FlaskForm):
    back = SubmitField("Back")