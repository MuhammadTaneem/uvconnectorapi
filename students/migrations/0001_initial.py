# Generated by Django 3.2.9 on 2021-11-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('student_id', models.IntegerField()),
                ('nick_name', models.CharField(max_length=32, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('birth_day', models.IntegerField(null=True)),
                ('birth_month', models.IntegerField(null=True)),
                ('image', models.ImageField(default='images/logo.png', upload_to='images/')),
                ('blood_group', models.CharField(max_length=12, null=True)),
                ('blood_doner', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]