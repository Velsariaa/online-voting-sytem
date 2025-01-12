# Generated by Django 5.1.1 on 2024-10-15 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateTimeField(verbose_name='Start Date')),
                ('enddate', models.DateTimeField(verbose_name='End Date')),
                ('institute', models.CharField(choices=[('OPTION_1', 'Option 1'), ('OPTION_2', 'Option 2'), ('OPTION_3', 'Option 3')], max_length=50, verbose_name='Institute')),
            ],
        ),
        migrations.CreateModel(
            name='candidacyform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, verbose_name='Full Name')),
                ('cotn', models.CharField(max_length=15, verbose_name='Contact Number')),
                ('emailaddr', models.EmailField(max_length=100, verbose_name='Email Address')),
                ('birth', models.DateField(verbose_name='Date of Birth')),
                ('position', models.CharField(choices=[('SELECT', 'Select'), ('OPTION_1', 'Option 1'), ('OPTION_2', 'Option 2')], max_length=50, verbose_name='Position')),
                ('statement', models.TextField(verbose_name='Statement')),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn', models.CharField(max_length=100, verbose_name='First Name')),
                ('ln', models.CharField(max_length=100, verbose_name='Last Name')),
                ('cont', models.CharField(max_length=15, verbose_name='Contact Number')),
                ('emailad', models.EmailField(max_length=100, verbose_name='Email Address')),
                ('feedback', models.TextField(verbose_name='Feedback')),
            ],
        ),
        migrations.CreateModel(
            name='credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='static/credentials/resume', verbose_name='Resume')),
                ('quali', models.FileField(upload_to='static/credentials/qualifications', verbose_name='Qualification')),
                ('letter', models.FileField(upload_to='static/credentials/letters', verbose_name='Letter')),
                ('others', models.FileField(upload_to='static/credentials/others', verbose_name='Other Documents')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=150, unique=True, verbose_name='User ID')),
                ('password', models.CharField(max_length=150, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100, verbose_name='First Name')),
                ('mname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Middle Name')),
                ('lname', models.CharField(max_length=100, verbose_name='Last Name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('gender', models.CharField(choices=[('SELECT', 'Select'), ('MALE', 'Male'), ('FEMALE', 'Female')], max_length=10, verbose_name='Gender')),
                ('suffix', models.CharField(blank=True, choices=[('NONE', 'None'), ('SR', 'Sr.'), ('JR', 'Jr.'), ('II', 'II')], max_length=10, null=True, verbose_name='Suffix')),
                ('idtype', models.CharField(choices=[('OPTION_1', 'Option 1'), ('OPTION_2', 'Option 2'), ('OPTION_3', 'Option 3')], max_length=10, verbose_name='ID Type')),
                ('idnum', models.CharField(max_length=100, verbose_name='ID Number')),
                ('uid', models.CharField(max_length=100, unique=True, verbose_name='User ID')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('confpass', models.CharField(max_length=100, verbose_name='Confirm Password')),
                ('emailadd', models.EmailField(max_length=100, verbose_name='Email Address')),
                ('contact', models.CharField(max_length=15, verbose_name='Contact Number')),
            ],
        ),
    ]
