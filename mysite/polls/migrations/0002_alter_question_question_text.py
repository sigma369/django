# Generated by Django 4.2.7 on 2024-02-18 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=400, verbose_name='Question Text'),
        ),
    ]
