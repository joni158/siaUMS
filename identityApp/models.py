from django.db import models

# Create your models here.

class Fakultas(models.Model):
    id_fakultas = models.CharField(max_length=10, primary_key=True)
    nama_fakultas = models.CharField(max_length=200)
    singkatan = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = "Fakultas"

    def __str__(self):
        return self.nama_fakultas


class Jurusan(models.Model):
    id_jurusan = models.CharField(max_length=10, primary_key=True)
    nama_jurusan = models.CharField(max_length=100, unique=True)
    nama_fakultas = models.ForeignKey(
        Fakultas,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "Jurusan"

    def __str__(self):
        return self.nama_jurusan

JENISKELAMIN = (
	    ('L', 'Laki-laki'),
	    ('P', 'Perempuan'),
	)

class Mahasiswa(models.Model):
    id_mhs = models.AutoField(primary_key=True)
    nim = models.CharField(max_length=12, unique=True)
    nama_mhs = models.CharField(max_length=100)
    tanggal_lahir = models.DateField(auto_now_add=False, auto_now=False)
    alamat = models.TextField()
    jenis_kelamin = models.CharField(choices=JENISKELAMIN, null=True, max_length=1, default='L')
    tahun_ajaran = models.CharField(max_length=10)
    password_SSO = models.CharField(max_length=12,default='123456789')
    password_SIA = models.CharField(max_length=14,default='123456789')
    nama_jurusan = models.ForeignKey(
        Jurusan,
        on_delete=models.CASCADE,
    )
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        db_table = "Mahasiswa"
        ordering = ('-tahun_ajaran','nama_mhs')

    def __str__ (self):
        return self.nim

class Dosen(models.Model):
    id_dosen = models.AutoField(primary_key=True)
    nik = models.CharField(max_length=12, unique=True)
    nama_dosen = models.CharField(max_length=100)
    tanggal_lahir = models.DateField(auto_now_add=False, auto_now=False)
    alamat = models.TextField()
    jenis_kelamin = models.CharField(choices=JENISKELAMIN, null=True, max_length=1, default='L')
    password_adum = models.CharField(max_length=12,default='123456789')
    password_SIA = models.CharField(max_length=14,default='123456789')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        db_table = "Dosen"
        ordering = ('nik','nama_dosen')

    def __str__ (self):
        return self.nik