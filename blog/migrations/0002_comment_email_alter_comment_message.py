# Generated by Django 4.0.6 on 2022-07-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=108, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(max_length=120, verbose_name='Message'),
        ),
    ]