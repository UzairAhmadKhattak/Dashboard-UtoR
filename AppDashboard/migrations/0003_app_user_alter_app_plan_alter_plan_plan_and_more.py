# Generated by Django 4.2.8 on 2023-12-05 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppDashboard', '0002_app_plan_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='app',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='AppDashboard.plan'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='plan',
            field=models.CharField(choices=[('0 dollars', '0 dollars'), ('10 dollars', '10 dollars'), ('25 dollars', '25 dollars')], default='0 dollars', max_length=15),
        ),
        migrations.DeleteModel(
            name='UserAndApp',
        ),
    ]