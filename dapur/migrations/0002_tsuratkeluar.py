# Generated by Django 3.1.2 on 2020-11-18 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TSuratKeluar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nomor_surat', models.CharField(max_length=100)),
                ('Tanggal_surat', models.DateField()),
                ('Kategori', models.CharField(choices=[('Biasa', 'Biasa'), ('Segera', 'Segera'), ('Mendesak', 'Mendesak')], max_length=50)),
                ('Klasifikasi', models.CharField(choices=[('Umum', 'Umum'), ('Khusus', 'Khusus'), ('Kilat', 'Kilat')], max_length=50)),
                ('Tujuan', models.CharField(max_length=100)),
                ('Tembusan', models.CharField(max_length=100)),
                ('Perihal', models.TextField(default='Default ')),
                ('Attachment', models.FileField(upload_to='filekeluar/attachments/')),
            ],
        ),
    ]
