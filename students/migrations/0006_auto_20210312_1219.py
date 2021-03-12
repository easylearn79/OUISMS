# Generated by Django 2.2.2 on 2021-03-12 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_studentclassinfo_class_short_form'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='fathers_name',
            new_name='dept',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='fathers_nid',
            new_name='fees',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='mothers_name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='name',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='fathers_img',
            new_name='qrcode',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='mothers_img',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='mothers_nid',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='mothers_number',
        ),
    ]