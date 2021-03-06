# Generated by Django 3.2 on 2021-09-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domilang', '0011_alter_user_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(default='none', max_length=32)),
                ('period', models.CharField(default='none', max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='available',
            field=models.ManyToManyField(blank=True, related_name='taught_by', to='domilang.Periods'),
        ),
    ]
