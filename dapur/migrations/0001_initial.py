# Generated by Django 3.1.2 on 2020-11-10 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_surat', models.CharField(max_length=100)),
                ('tanggal_surat', models.DateField()),
                ('kategori', models.CharField(choices=[('Biasa', 'Biasa'), ('Segera', 'Segera'), ('Mendesak', 'Mendesak')], max_length=50)),
                ('klasifikasi', models.CharField(choices=[('Kilat', 'Kilat'), ('Express', 'Express'), ('Biasa', 'Biasa')], max_length=50)),
                ('pengirim', models.CharField(max_length=100)),
                ('perihal', models.TextField(default='DataFlair Django tutorials')),
                ('attachment', models.FileField(upload_to='filesimpan/attachments/')),
            ],
        ),
    ]
