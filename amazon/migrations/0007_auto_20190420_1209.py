# Generated by Django 2.1.7 on 2019-04-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0006_remove_employee_de_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='women_shops_clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'women_shops_clothes',
            },
        ),
        migrations.DeleteModel(
            name='employee_de',
        ),
    ]
