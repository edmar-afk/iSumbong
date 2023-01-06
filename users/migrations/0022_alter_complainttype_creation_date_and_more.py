# Generated by Django 4.0.5 on 2022-10-09 01:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0021_alter_complainttype_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complainttype',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 9, 1, 23, 40, 641636, tzinfo=utc), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='complainttype',
            name='updation_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 9, 1, 23, 40, 641636, tzinfo=utc), verbose_name='Last Updated'),
        ),
        migrations.AlterField(
            model_name='tblecomplaint',
            name='complainant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tblecomplaint',
            name='complaint_regDate',
            field=models.DateField(default=datetime.datetime(2022, 10, 9, 1, 23, 40, 641636, tzinfo=utc), verbose_name='Complaint Submitted Date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_regDate',
            field=models.DateField(default=datetime.datetime(2022, 10, 9, 1, 23, 40, 641636, tzinfo=utc), verbose_name='Registered Date'),
        ),
    ]
