# Generated by Django 2.2.2 on 2020-04-10 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Категория товаров')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Сорт продуктов')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Порода дерева')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена')),
                ('length', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Длина')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('rating', models.PositiveIntegerField(default=0, verbose_name='Рейтинг продукта')),
                ('date', models.DateField(auto_now=True)),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото продукта')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория товара')),
                ('sort', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Sort', verbose_name='Сорт')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Species', verbose_name='Порода дерева')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Order')),
            ],
        ),
    ]
