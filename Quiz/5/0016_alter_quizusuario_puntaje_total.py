# Generated by Django 4.1.1 on 2022-10-10 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0015_alter_quizusuario_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizusuario',
            name='puntaje_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Puntaje Total'),
        ),
    ]
