from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class PokemonSearchForm(FlaskForm):
    name = StringField('Pokemon Name', validators=[DataRequired()])
    submit = SubmitField()

class CatchForm(FlaskForm):
    submit = SubmitField(label="Catch")
    catch = HiddenField()
