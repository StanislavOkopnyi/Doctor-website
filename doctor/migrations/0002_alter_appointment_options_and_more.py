# Generated by Django 4.2.1 on 2023-05-30 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['-sent_date']},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='accepted_dat',
            field=models.DateField(null=True),
        ),
    ]