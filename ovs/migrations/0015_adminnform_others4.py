# Generated by Django 5.1.1 on 2025-01-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ovs', '0014_adminnform_others1_adminnform_others2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminnform',
            name='others4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
