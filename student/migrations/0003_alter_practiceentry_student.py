# Generated by Django 4.2.3 on 2023-11-15 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_name_alter_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practiceentry',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]