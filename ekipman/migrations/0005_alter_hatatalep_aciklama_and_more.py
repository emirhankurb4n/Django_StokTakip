# Generated by Django 5.0.3 on 2024-04-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekipman', '0004_alter_hatatalep_aciklama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hatatalep',
            name='aciklama',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='hatatalep',
            name='cozulmeDurumu',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Çözülme Durumu'),
        ),
        migrations.AlterField(
            model_name='hatatalep',
            name='eklenmeTarihi',
            field=models.DateField(blank=True, null=True, verbose_name='Eklenme Tarihi'),
        ),
        migrations.AlterField(
            model_name='hatatalep',
            name='ekleyenPersonel',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ekleyen Personel'),
        ),
    ]