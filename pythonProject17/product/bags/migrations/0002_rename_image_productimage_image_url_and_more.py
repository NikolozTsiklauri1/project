# Generated by Django 4.2.11 on 2024-04-25 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bags', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image',
            new_name='image_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('ნაჭრის მხარჩანთა', 'ნაჭრის მხარჩანთა'), ('ნაჭრის ზურგჩანთა', 'ნაჭრის ზურგჩანთა')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='no description'),
        ),
    ]
