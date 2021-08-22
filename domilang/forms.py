from django import forms

NIVEL_CHOICES =(
    ("Elementary", "Elementary"),
    ("Intermediate", "Intermediate"),
    ("Advanced", "Advanced")
)

class LogInForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password")
    confirmation = forms.CharField(label="Confirm Password")

class ProfileForm(forms.Form):
    first_name = forms.CharField(label="First Name", required=False)
    last_name = forms.CharField(label="Last Name", required=False)
    native_lan = forms.CharField(label="Native Language", required=False)
    foto = forms.ImageField(required=False)
    pais = forms.CharField(label="Country", required=False)
    franja = forms.CharField(label="Time Zone", required=False)
    nivel = forms.ChoiceField(choices = NIVEL_CHOICES, label="Level", required=False)
    study_lan = forms.CharField(label="Study Language", required=False)
    phone = forms.CharField(label="Phone", required=False)