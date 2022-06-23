# Generated by Django 4.0.5 on 2022-06-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='usernet',
            name='technology',
            field=models.ManyToManyField(related_name='users', to='profiles.technology'),
        ),
    ]