# Generated by Django 3.1.5 on 2021-04-16 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smoking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borough',
            name='id',
        ),
        migrations.RemoveField(
            model_name='fine',
            name='id',
        ),
        migrations.RemoveField(
            model_name='smokingareatype',
            name='id',
        ),
        migrations.AlterField(
            model_name='borough',
            name='boroughcode',
            field=models.AutoField(max_length=64, primary_key=True, serialize=False, verbose_name='자치구 코드'),
        ),
        migrations.AlterField(
            model_name='fine',
            name='finecode',
            field=models.AutoField(max_length=64, primary_key=True, serialize=False, verbose_name='과태료 코드'),
        ),
        migrations.AlterField(
            model_name='smokingarea',
            name='boroughcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borough_smoking', to='smoking.borough', verbose_name='자치구 코드'),
        ),
        migrations.AlterField(
            model_name='smokingarea',
            name='typecode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smoking_type', to='smoking.smokingareatype', verbose_name='유형 코드'),
        ),
        migrations.AlterField(
            model_name='smokingareatype',
            name='typecode',
            field=models.AutoField(max_length=64, primary_key=True, serialize=False, verbose_name='유형 코드'),
        ),
    ]
