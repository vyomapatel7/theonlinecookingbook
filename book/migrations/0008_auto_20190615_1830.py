# Generated by Django 2.0.13 on 2019-06-15 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20190615_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]