# Generated by Django 3.1.1 on 2020-10-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("program", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="program",
            name="title",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
