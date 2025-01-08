from django.db import models
from django.contrib.auth.hashers import check_password

class adminnform(models.Model):
    institute = models.CharField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField()
    positions = models.TextField(null=True)
    others1 = models.CharField(max_length=255, blank=True, null=True)
    others2 = models.CharField(max_length=255, blank=True, null=True)
    others3 = models.CharField(max_length=255, blank=True, null=True)
    others4 = models.CharField(max_length=255, blank=True, null=True)
    others5 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.institute

    
#registration
class registrationform(models.Model):
    gender_choices = [
        ('SELECT', 'Select'),
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    ]
    suffix_choices = [
        ('NONE', 'None'),
        ('Sr.', 'Sr.'),
        ('Jr.', 'Jr.'),
        ('II', 'II'),
    ]
    idtype_choices = [
        ('OPTION 1', 'Option 1'),
        ('OPTION 2', 'Option 2'),
        ('OPTION 3', 'Option 3'),
    ]
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    suffix = models.CharField(max_length=10, choices=suffix_choices)
    idtype = models.CharField(max_length=10, choices=idtype_choices)
    idnum = models.CharField(max_length=100)
    uid = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    emailadd = models.EmailField(max_length=100)
    contact = models.CharField(max_length=15)
    
    def __str__(self):
        return f'{self.fname} {self.mname} {self.lname} {self.uid} {self.password}'
    

#login
class loginform(models.Model):
    uid = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'loginform'
    

#contact
class contactform(models.Model):
    fn = models.CharField(max_length=100)
    ln = models.CharField(max_length=100)
    cont = models.CharField(max_length=15)
    emailad = models.EmailField(max_length=100)
    feedback = models.TextField()
    
    def __str__(self):
        return f'{self.fn} {self.ln} {self.cont} {self.emailad} {self.feedback}'


#candidacyform
class candidacy_form(models.Model):
    position_choices = [
        ('SELECT', 'Select'),
        ('OPTION 1', 'Option 1'),
        ('OPTION 2', 'Option 2'),
    ]
    fullname = models.CharField(max_length=100)
    position = models.CharField(max_length=50, choices=position_choices)
    cotn = models.CharField(max_length=15)
    emailaddr = models.EmailField(max_length=100)
    birth = models.DateField()
    statement = models.TextField()
    
    def __str__(self):
        return f'{self.fullname} {self.position}'
    
#credentials
class credentialsform(models.Model):
    resume = models.FileField(upload_to='static/credentials/resume')
    quali = models.FileField(upload_to='static/credentials/qualifications')
    letter = models.FileField(upload_to='static/credentials/letters')
    others = models.FileField(upload_to='static/credentials/others')
    
    def __str__(self):
        return f'{self.resume} {self.quali} {self.letter} {self.others}'
    
class resetpass(models.Model):
    uid = models.CharField(max_length=150, unique=True)
    newpass = models.CharField(max_length=150)
    confirmpass = models.CharField(max_length=150)
    
    def __str__(self):
        return f'{self.uid}'
    
#comelec
class comelecform(models.Model):
    GENDER_CHOICES = [
        ('SELECT', 'Select'),
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    ]
    SUFFIX_CHOICES = [
        ('NONE', 'None'),
        ('Sr.', 'Sr.'),
        ('Jr.', 'Jr.'),
        ('II', 'II'),
    ]
    IDTYPE_CHOICES = [
        ('OPTION 1', 'Option 1'),
        ('OPTION 2', 'Option 2'),
        ('OPTION 3', 'Option 3'),
    ]

    fname = models.CharField(max_length=100, verbose_name="First Name")
    mname = models.CharField(max_length=100, verbose_name="Middle Name", blank=True)
    lname = models.CharField(max_length=100, verbose_name="Last Name")
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='SELECT')
    suffix = models.CharField(max_length=10, choices=SUFFIX_CHOICES, default='NONE')
    idtype = models.CharField(max_length=10, choices=IDTYPE_CHOICES, default='OPTION 1')
    idnum = models.CharField(max_length=100, verbose_name="ID Number")
    uid = models.CharField(max_length=100, unique=True, verbose_name="User ID")
    emailadd = models.EmailField(max_length=100, verbose_name="Email Address")
    contact = models.CharField(max_length=15, verbose_name="Contact Number")

    def __str__(self):
        return f'{self.fname} {self.mname} {self.lname} ({self.uid})'
    

class MovieInfo(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='candidates/')

    def __str__(self):
        return self.name

# Vote model for storing votes submitted by users
class voteform(models.Model):
    voter_id = models.IntegerField() 
    vote1 = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, related_name='vote1')
    vote2 = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, related_name='vote2')
    vote3 = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, related_name='vote3')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vote by User {self.voter_id} at {self.timestamp}"