# Generated by Django 4.2.1 on 2024-06-14 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prjapp', '0013_customerproduct_amazon_uk_10_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards_search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(blank=True, null=True)),
                ('cards', models.TextField(blank=True, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prjapp.customerproduct')),
            ],
        ),
        migrations.DeleteModel(
            name='Cards_Class',
        ),
    ]
