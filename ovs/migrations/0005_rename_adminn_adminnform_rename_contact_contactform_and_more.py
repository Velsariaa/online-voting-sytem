# Generated by Django 5.1.1 on 2024-10-20 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ovs', '0004_remove_registration_confpass_alter_adminn_enddate_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='adminn',
            new_name='adminnform',
        ),
        migrations.RenameModel(
            old_name='contact',
            new_name='contactform',
        ),
        migrations.RenameModel(
            old_name='credentials',
            new_name='credentialsform',
        ),
        migrations.RenameModel(
            old_name='login',
            new_name='loginform',
        ),
        migrations.RenameModel(
            old_name='registration',
            new_name='registrationform',
        ),
    ]
