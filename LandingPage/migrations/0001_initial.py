# Generated by Django 3.1.4 on 2021-07-14 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=20)),
                ('e_mail', models.EmailField(max_length=254)),
                ('u_message', models.TextField()),
            ],
        ),
    ]