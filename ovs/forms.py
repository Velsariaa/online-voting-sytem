from django import forms
from .models import adminnform, registrationform, loginform, contactform, credentialsform, resetpass, comelecform, voteform
from django.forms import ModelForm
from .models import Candidate


#admin
class adminnform(forms.ModelForm):
    class Meta:
        model = adminnform
        fields = ['institute', 'startdate', 'enddate', 'positions', 'others1', 'others2', 'others3', 'others4', 'others5']

#registration
class registrationform(forms.ModelForm):
    confpass = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = registrationform
        fields = ['fname', 'mname', 'lname', 'age', 'gender', 'suffix', 'idtype', 'idnum', 'uid', 'password', 'confpass', 'emailadd', 'contact']
        widgets = {
            'password': forms.PasswordInput(),
        }

#login
class loginform(forms.ModelForm):
    class Meta:
        model = loginform
        fields = ['uid', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

#contactus
class contactform(forms.ModelForm):
    class Meta:
        model = contactform
        fields = ['fn', 'ln', 'cont', 'emailad', 'feedback']

#candidacyform
# class candidacyform(forms.ModelForm):
#     class Meta:
#         model = candidacy_form
#         fields = ['fullname', 'position', 'cotn', 'emailaddr', 'birth', 'statement']

class Candidacyform(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['fullname', 'cotn', 'emailaddr', 'birth', 'position', 'statement', 'credential1', 'credential2', 'credential3', 'credential4']

#credentials
class credentialsform(forms.ModelForm):
    class Meta:
        model = credentialsform
        fields = ['resume', 'quali', 'letter', 'others']
        
#resetpass
class resetpass(forms.ModelForm):
    class Meta:
        model = resetpass
        fields = ['uid', 'newpass', 'confirmpass']
        
#comelec
class comelecform(forms.ModelForm):
    class Meta:
        model = comelecform
        fields = [
            'fname', 'mname', 'lname', 'age', 'gender', 'suffix', 
            'idtype', 'idnum', 'uid', 'emailadd', 'contact'
        ]
        widgets = {
            'gender': forms.Select(),
            'suffix': forms.Select(),
            'idtype': forms.Select(),
        }

    # def clean_uid(self):
    #     uid = self.cleaned_data.get('uid')
    #     if comelec.objects.filter(uid=uid).exists():
    #         raise forms.ValidationError("User ID already exists.")
    #     return uid
    

    #comelecupdate
# class updateform (forms.ModelForm):
#     fname = forms.CharField()
#     mname = forms.CharField()
#     lname = forms.CharField()
#     age = forms.CharField()
#     uid = forms.CharField()
#     class Meta:
#         model = comelec
#         fields = [
#             'fname', 'mname', 'lname', 'age', 'uid'
#         ]

class updateform(forms.Form):
     fname = forms.CharField()
     mname = forms.CharField()
     lname = forms.CharField()
     age = forms.CharField()
     uid = forms.CharField()
     

class voteform(forms.ModelForm):
    class Meta:
        model = voteform
        fields = ['vote1', 'vote2', 'vote3']

    vote1 = forms.ChoiceField(choices=[], widget=forms.RadioSelect())
    vote2 = forms.ChoiceField(choices=[], widget=forms.RadioSelect())
    vote3 = forms.ChoiceField(choices=[], widget=forms.RadioSelect())

        
class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['fullname', 'cotn', 'emailaddr', 'birth', 'position', 'statement', 
                  'credential1', 'credential2', 'credential3', 'credential4']