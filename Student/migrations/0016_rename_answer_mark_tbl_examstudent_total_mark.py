# Generated by Django 5.0.1 on 2024-04-12 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0015_rename_exstudent_id_tbl_examstudent_student_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_examstudent',
            old_name='answer_mark',
            new_name='total_mark',
        ),
    ]