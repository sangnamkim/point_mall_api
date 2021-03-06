# Generated by Django 2.2.3 on 2019-08-20 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_auto_20190820_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AlterField(
            model_name='categoryitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorys', to='item.Item'),
        ),
        migrations.AlterField(
            model_name='historyitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Item'),
        ),
        migrations.AlterField(
            model_name='useritem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Item'),
        ),
    ]
