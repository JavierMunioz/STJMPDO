# Generated by Django 4.1 on 2022-09-07 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistApp', '0005_tareastable_usuario_alter_tareastable_nombretarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareastable',
            name='usuario',
            field=models.CharField(max_length=50, null=True, verbose_name='usuario'),
        ),
    ]
