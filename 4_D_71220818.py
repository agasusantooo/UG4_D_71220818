angka=input("Masukkan sekumpulan bilangan (pisahkan dengan koma):")
list_angka=list(map(int,angka.split(",")))

angkamax=lambda list_angka: max(list_angka)
angkamin=lambda list_angka: min(list_angka)

print(angkamax(list_angka))
print(angkamin(list_angka))