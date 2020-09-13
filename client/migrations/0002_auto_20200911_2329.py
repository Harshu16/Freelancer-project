# Generated by Django 3.1 on 2020-09-12 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_email',
            field=models.EmailField(default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=50)),
                ('task_domain', models.CharField(default='', max_length=50)),
                ('task_rate', models.IntegerField(default='')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='client.client')),
            ],
        ),
    ]