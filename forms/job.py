from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    leader_id = IntegerField('Номер начальника', validators=[DataRequired()])
    work_size = IntegerField("Время работы", validators=[DataRequired()])
    collaborators = StringField("Номера работяг", validators=[DataRequired()])
    is_finished = BooleanField('Работа закончена')
    submit = SubmitField('Применить')
