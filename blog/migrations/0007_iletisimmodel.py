# Generated by Django 4.0 on 2021-12-23 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_yorummodel_options_alter_yorummodel_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='IletisimModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('isim_soyisim', models.CharField(max_length=150)),
                ('mesaj', models.TextField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'İletisim',
                'verbose_name_plural': 'İletisim',
                'db_table': 'iletisim',
            },
        ),
    ]
