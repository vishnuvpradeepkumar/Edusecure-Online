# Generated by Django 5.0.1 on 2024-04-05 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0015_delete_tbl_examquestions'),
        ('Student', '0005_delete_tbl_answer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_questions',
        ),
    ]