# Generated by Django 4.2.4 on 2023-11-03 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_alter_documento_fecharegistro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documento',
            old_name='fechaRegistro',
            new_name='fecha_registro',
        ),
    ]
