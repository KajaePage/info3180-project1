from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import DataRequired


class PropertyForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    bedrooms = StringField('bedrooms', validators=[DataRequired()])
    bathroom = StringField('bathrooms', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    price = StringField('price',validators=[DataRequired()])
    type = SelectField('type', choices = [(status, status) for status in ["House","Apartment"]], validators = [DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    photo = FileField('photo', validators=[FileRequired(),FileAllowed(['jpg','png'], 'Only Image Files!')])
    submit = SubmitField(label='Add Property')