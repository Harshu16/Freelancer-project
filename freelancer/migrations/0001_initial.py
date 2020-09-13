# Generated by Django 3.1 on 2020-09-12 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('free_id', models.AutoField(primary_key=True, serialize=False)),
                ('free_name', models.CharField(max_length=50)),
                ('free_domain', models.CharField(max_length=50)),
                ('free_phone', models.CharField(default='', max_length=50)),
                ('free_email', models.EmailField(default='', max_length=50)),
                ('free_password1', models.CharField(max_length=50)),
                ('free_password2', models.CharField(max_length=50)),
            ],
        ),
    ]