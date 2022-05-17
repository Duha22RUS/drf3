# Generated by Django 4.0.4 on 2022-04-18 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amscapp', '0010_alter_patient_address_alter_patient_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Выбор для вопросов', 'verbose_name_plural': 'Выборы для вопросов'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='answerlet',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answermulty',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answernum',
        ),
        migrations.AlterField(
            model_name='question',
            name='questname',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100, verbose_name='Вариант ответа')),
                ('Choices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amscapp.question')),
            ],
            options={
                'verbose_name': 'Для выбора',
                'verbose_name_plural': 'Для выборов',
            },
        ),
    ]