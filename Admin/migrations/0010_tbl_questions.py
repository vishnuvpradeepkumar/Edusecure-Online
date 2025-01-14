# Generated by Django 5.0.1 on 2024-03-03 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_tbl_admin_tbl_section_delete_tbl_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_batch')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_section')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_subject')),
            ],
        ),
    ]
