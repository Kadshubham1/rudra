# Generated by Django 5.0.6 on 2024-10-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('date', models.DateField()),
                ('department', models.CharField(choices=[('Physiotherapy', 'Physiotherapy'), ('Physical Health', 'Physical Health'), ('Treatments', 'Treatments')], max_length=20)),
                ('comments', models.TextField(blank=True)),
            ],
        ),
    ]
