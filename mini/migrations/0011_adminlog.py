# Generated by Django 2.2 on 2019-05-10 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0010_auto_20190509_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]