# Generated by Django 4.0.4 on 2022-04-18 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amscapp', '0012_fields_alter_choice_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amscapp.fields'),
        ),
    ]
