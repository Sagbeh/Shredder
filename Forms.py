from flask_wtf import FlaskForm
from wtforms import SubmitField,SelectField, IntegerField, StringField,PasswordField, validators
# create the registration form
class RegistrationForm(FlaskForm):
    # all fields required
    user = StringField("Username", [validators.DataRequired("Please enter a username.")])
    password = PasswordField("Password", [validators.DataRequired("Please enter a password.")])
    email = StringField("Email Address", [validators.email("Please enter a valid email address.")])
    submit = SubmitField("Send")
# create the order form
class ProgressionForm(FlaskForm):

    cid = IntegerField("Client ID: ", [validators.required("Value must be an integer.")])
    pVal = IntegerField("Enter Amount to Increase or Decrease Weight", [validators.required("Value must be an integer.")])
    submit = SubmitField("Send")
# create the close order form
class StartForm(FlaskForm):
    # all fields required
    cid = IntegerField("Client ID: ", [validators.required("Value must be an integer.")])
    bench = IntegerField("Bench: ", [validators.required("Value must be an integer.")])
    seatedDip = IntegerField("Seated Dip: ", [validators.required("Value must be an integer.")])
    unilateralRow = IntegerField("Unilateral Row: ", [validators.required("Value must be an integer.")])
    frontPulldown = IntegerField("Front Pulldown: ", [validators.required("Value must be an integer.")])
    latPulldown = IntegerField("Lat Pulldown: ", [validators.required("Value must be an integer.")])
    curl = IntegerField("Curl: ", [validators.required("Value must be an integer.")])
    seatedHammer = IntegerField("Seated Hammer : ", [validators.required("Value must be an integer.")])
    lateralRaise = IntegerField("Lateral Raise: ", [validators.required("Value must be an integer.")])
    tricepExtension = IntegerField("Tricep Extension: ", [validators.required("Value must be an integer.")])
    shoulderRaise = IntegerField("Shoulder Raise: ", [validators.required("Value must be an integer.")])
    rearFly = IntegerField("Rear Fly: ", [validators.required("Value must be an integer.")])
    obliqueActivation = IntegerField("Oblique Activation: ", [validators.required("Value must be an integer.")])
    lowerBackActivation = IntegerField("Lower Back Activations: ", [validators.required("Value must be an integer.")])
    abActivation = IntegerField("Ab Activation: ", [validators.required("Value must be an integer.")])
    medicineBall = IntegerField("Medicine Ball: ", [validators.required("Value must be an integer.")])
    lowerBackPlank = IntegerField("Lower Back Plank: ", [validators.required("Value must be an integer.")])
    sideSpin = IntegerField("Side Spin: ", [validators.required("Value must be an integer.")])
    lunges = IntegerField("Lunges: ", [validators.required("Value must be an integer.")])
    horizontalCalf = IntegerField("Horizontal Calf: ", [validators.required("Value must be an integer.")])
    mtsLegExtension = IntegerField("MTS Leg Extension: ", [validators.required("Value must be an integer.")])
    legCurl = IntegerField("Leg Curl: ", [validators.required("Value must be an integer.")])
    hipAbduction = IntegerField("Hip Abduction: ", [validators.required("Value must be an integer.")])
    legPress = IntegerField("Leg Press: ", [validators.required("Value must be an integer.")])

    submit = SubmitField("Submit")

class DeleteCustomerForm(FlaskForm):

    cid = IntegerField("Client ID: ", [validators.required("Value must be an integer.")])
    submit = SubmitField("Submit")
# create the search customer form
class SearchCustomerForm(FlaskForm):

    cid = IntegerField("Customer ID: ", [validators.required("Value must be an integer.")])
    submit = SubmitField("Submit")
