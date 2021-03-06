# Generated by Django 3.1.2 on 2020-10-30 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subjectcategory',
            options={'verbose_name': 'Направление подготовки', 'verbose_name_plural': 'Направления подготовки'},
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('e', 'легкий'), ('m', 'средний'), ('h', 'продвинутый')], default='e', max_length=1),
        ),
    ]
