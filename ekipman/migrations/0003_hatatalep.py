# Generated by Django 5.0.3 on 2024-03-30 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekipman', '0002_alter_ekipman_ekipmanturu_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HataTalep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aciklama', models.CharField(max_length=500, verbose_name='Ekleyen Personel')),
                ('cozulmeDurumu', models.BooleanField(default=False, verbose_name='Çözülme Durumu')),
                ('eklenmeTarihi', models.DateField(verbose_name='Eklenme Tarihi')),
                ('ekleyenPersonel', models.CharField(max_length=50, verbose_name='Ekleyen Personel')),
            ],
        ),
    ]
