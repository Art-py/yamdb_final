# Generated by Django 2.2.16 on 2022-05-05 19:14

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[reviews.validators.validate_username], verbose_name='Имя пользователя'),
        ),
    ]
