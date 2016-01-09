from django.db import models
from identityApp.models import Mahasiswa, Dosen

# Create your models here.
class Mata_Kuliah(models.Model):
    id_mk = models.CharField(max_length=10, primary_key=True, default='')
    nama_mk= models.CharField(max_length=200)
    jumlah_sks = models.IntegerField()
    mk_semester = models.IntegerField()

    class Meta:
        db_table = "Mata_Kuliah"

    def __str__(self):
        return self.id_mk

KELAS = (
    ('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'),('G','G'),('H','H'),('I','I'),('J','J'),('X','X'),
)

class KRS(models.Model):
    id_krs = models.AutoField(primary_key=True)
    nim = models.ForeignKey(
        Mahasiswa,
        default='',
        on_delete=models.CASCADE,
    )
    id_mk = models.ForeignKey(
        Mata_Kuliah,
        default='',
        on_delete=models.CASCADE,
    )
    nik = models.ForeignKey(
        Dosen,
        default='',
        on_delete=models.CASCADE,
    )
    kelas = models.CharField(choices=KELAS, null=True, max_length=1, default='A')
    ambil_di_smt = models.IntegerField(default=1)

    class Meta:
        db_table = "KRS"

    def __str__(self):
        return str(self.id_krs)