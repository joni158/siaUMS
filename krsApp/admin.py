from django.contrib import admin
from .models import Mata_Kuliah, KRS

# Register your models here.

class MataKuliahAdmin(admin.ModelAdmin):
	list_display = ["id_mk", "nama_mk", "jumlah_sks","mk_semester"]
	class Meta:
		model = Mata_Kuliah
admin.site.register(Mata_Kuliah, MataKuliahAdmin)

class KRSAdmin(admin.ModelAdmin):
	list_display = ["id_krs", "nim", "id_mk","kelas","nik","ambil_di_smt"]
	class Meta:
		model = KRS
admin.site.register(KRS, KRSAdmin)