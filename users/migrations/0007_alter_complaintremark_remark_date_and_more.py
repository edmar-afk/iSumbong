# Generated by Django 4.0.5 on 2022-10-04 09:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_complaintremark_remark_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintremark',
            name='remark_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 4, 9, 26, 42, 997535, tzinfo=utc), verbose_name='Remark Date'),
        ),
        migrations.AlterField(
            model_name='complainttype',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 4, 9, 26, 42, 997535, tzinfo=utc), verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='complainttype',
            name='updation_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 4, 9, 26, 42, 997535, tzinfo=utc), verbose_name='Last Updated'),
        ),
        migrations.AlterField(
            model_name='tblecomplaint',
            name='complaint_regDate',
            field=models.DateField(default=datetime.datetime(2022, 10, 4, 9, 26, 42, 997535, tzinfo=utc), verbose_name='Complaint Submitted Date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_regDate',
            field=models.DateField(default=datetime.datetime(2022, 10, 4, 9, 26, 42, 997535, tzinfo=utc), verbose_name='Registered Date'),
        ),
    ]
