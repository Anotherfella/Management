# Generated by Django 2.2 on 2019-05-09 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0007_registrations_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='WORKER_REGISTER1',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='WORKER_REGISTER',
        ),
        migrations.AddField(
            model_name='registrations',
            name='domain',
            field=models.CharField(default='civil', max_length=100),
            preserve_default=False,
        ),
    ]
