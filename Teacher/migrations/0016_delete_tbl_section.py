# Generated by Django 5.0.1 on 2024-04-05 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0016_delete_tbl_questions'),
        ('Teacher', '0015_alter_tbl_exam_subjectid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_section',
        ),
    ]
