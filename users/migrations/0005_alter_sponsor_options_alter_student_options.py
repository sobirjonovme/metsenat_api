# Generated by Django 4.1.1 on 2022-10-01 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_sponsor_options_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsor',
            options={'ordering': ['-create_at']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-create_at']},
        ),
    ]
