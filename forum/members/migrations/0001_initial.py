# Generated by Django 4.1 on 2022-08-22 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='answerforum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theaseranswer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('theaser_text', models.CharField(max_length=255)),
                ('theaseranswer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='registieren',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benutzername', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('repeatpassword', models.CharField(max_length=255)),
            ],
        ),
    ]
