# Generated by Django 4.0 on 2021-12-23 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_yazilarmodel_yazar_alter_yorummodel_yazan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yorummodel',
            old_name='guncellenme_tarihi',
            new_name='duzenlenme_tarihi',
        ),
    ]
