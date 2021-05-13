# Generated by Django 3.2.2 on 2021-05-12 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=60, null=True)),
                ('cpf', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.IntegerField()),
            ],
        ),
    ]
