# Generated by Django 5.0.3 on 2024-04-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0003_alter_complaint_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='contact_number',
            field=models.CharField(max_length=11),
        ),
    ]