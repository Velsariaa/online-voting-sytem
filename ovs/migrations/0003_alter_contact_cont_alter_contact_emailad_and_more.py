# Generated by Django 5.1.1 on 2024-10-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ovs', '0002_alter_contact_cont'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cont',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='contact',
            name='emailad',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='feedback',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fn',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='ln',
            field=models.CharField(max_length=100),
        ),
    ]
