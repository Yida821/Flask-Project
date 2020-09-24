from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField, RadioField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField("Login")


class FormCollection(FlaskForm):
    first_name = StringField("First Name: ", validators=[DataRequired(), Length(min=1, max=20)])
    last_name = StringField("Last Name: ", validators=[DataRequired(), Length(min=1, max=20)])
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=4, max=20)])
    gender = RadioField('Gender: ', validators=[DataRequired()], choices = [('M','Male'),('F','Female')])
    order_type = RadioField("Order Type: ", validators=[DataRequired()], choices = [('D','Domestic'),('I','International')])
    address1 = StringField("Address1: ", validators=[DataRequired(), Length(min=4, max=100)])
    address2 = StringField("Address2: ", validators=[DataRequired(), Length(min=4, max=100)])
    city = StringField("City: ", validators=[DataRequired()])
    state = SelectField("State: ", choices=[('Choose','Choose'), ('AL', 'Alabama'),
    ('AZ', 'Arizona'),('AR', 'Arkansas'),('CA', 'California'),('CO', 'Colorado'),('CT', 'Connecticut'),
    ('DE', 'Delaware'),('DC', 'District of Columbia'),('FL', 'Florida'),('GA', 'Georgia'),('ID', 'Idaho'),
    ('IL', 'Illinois'),('IN', 'Indiana'),('IA', 'Iowa'),('KS', 'Kansas'),('KY', 'Kentucky'),('LA', 'Louisiana'),
    ('ME', 'Maine'),('MD', 'Maryland'),('MA', 'Massachusetts'),('MI', 'Michigan'),('MN', 'Minnesota'),('MS', 'Mississippi'),
    ('MO', 'Missouri'),('MT', 'Montana'),('NE', 'Nebraska'),('NV', 'Nevada'),('NH', 'New Hampshire'),('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),('NY', 'New York'),('NC', 'North Carolina'),('ND', 'North Dakota'),('OH', 'Ohio'),
    ('OK', 'Oklahoma'),('OR', 'Oregon'),('PA', 'Pennsylvania'),('RI', 'Rhode Island'),('SC', 'South Carolina'),('SD', 'South Dakota'),
    ('TN', 'Tennessee'),('TX', 'Texas'),('UT', 'Utah'),('VT', 'Vermont'),('VA', 'Virginia'),('WA', 'Washington'),
    ('WV', 'West Virginia'),('WI', 'Wisconsin'),('WY', 'Wyoming')], validators=[DataRequired()])
    
    zipcode = StringField("Zipcode: ", validators=[DataRequired(), Length(min=4, max=20)])
    message = TextAreaField("Message: ", validators=[DataRequired(), Length(min=4, max=500)])
    checkbox = BooleanField("Remeber Me: ", default=False)
    submit = SubmitField("Submit")
    photo = FileField()

class UploadForm(FlaskForm):
    file = FileField()
    submit = SubmitField("Upload File")

class ProfileForm(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    pasword = StringField()
    check_box = StringField()
    radio = StringField()

    file_photo = StringField()
  #  state = SelectField()
  #  city = StringField()
  #  zipcode = StringField()
  #  date = StringField()





    
class FormUtil():

    @staticmethod
    def get_choices(my_list):
        # print("my_list",my_list)
        tuple_options = [(x, x) for x in my_list]
        # print(tuple_options)
        return tuple_options
        #my_field.choices = tuple_options



class TablesForm(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    dob = StringField()

class EmployeeForm(FlaskForm):
    file = FileField()



class GroupUploadForm(FlaskForm):
    file_csv = FileField()

class BankForm(FlaskForm):
    file_csv = FileField()
