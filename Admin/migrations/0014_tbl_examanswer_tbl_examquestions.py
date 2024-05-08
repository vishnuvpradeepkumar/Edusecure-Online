# Generated by Django 5.0.1 on 2024-03-11 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_tbl_questions_exam_id'),
        ('Guest', '0002_tbl_teacher_teacher_status'),
        ('Teacher', '0013_alter_tbl_exam_exam_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_examanswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examanswer_content', models.CharField(max_length=2048)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_teacher')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_examquestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.tbl_exam')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_questions')),
            ],
        ),
    ]