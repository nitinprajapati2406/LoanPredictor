# Generated by Django 4.2.4 on 2023-09-18 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoanAnalysisApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='interest',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]