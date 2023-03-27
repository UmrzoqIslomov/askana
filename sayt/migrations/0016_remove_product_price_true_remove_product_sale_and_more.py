# Generated by Django 4.1.6 on 2023-02-12 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sayt', '0015_alter_like_commentary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_true',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sale',
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procent', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sayt.product')),
            ],
        ),
    ]
