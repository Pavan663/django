# Generated by Django 2.0.7 on 2018-07-16 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]