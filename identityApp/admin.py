from django.contrib import admin
from .models import Fakultas, Jurusan, Mahasiswa, Dosen

# Register your models here.

class FakultasAdmin(admin.ModelAdmin):
	list_display = ["id_fakultas", "nama_fakultas", "singkatan"]
	class Meta:
		model = Fakultas
admin.site.register(Fakultas, FakultasAdmin)

class JurusanAdmin(admin.ModelAdmin):
	list_display = ["id_jurusan", "nama_jurusan", "nama_fakultas"]
	class Meta:
		model = Jurusan
admin.site.register(Jurusan, JurusanAdmin)

class MahasiswaAdmin(admin.ModelAdmin):
	list_display = ["id_mhs", "nim", "nama_mhs","tanggal_lahir","alamat","jenis_kelamin","tahun_ajaran","nama_jurusan","password_SSO","password_SIA"]
	class Meta:
		model = Mahasiswa
admin.site.register(Mahasiswa, MahasiswaAdmin)

class DosenAdmin(admin.ModelAdmin):
	list_display = ["id_dosen","nik","nama_dosen","tanggal_lahir","alamat","jenis_kelamin","password_adum","password_SIA"]
	class Meta:
		model = Dosen
admin.site.register(Dosen, DosenAdmin)