angka=input("Masukkan sekumpulan bilangan (pisahkan dengan koma):")
list_angka=list(map(int,angka.split(",")))

angkamax=lambda list_angka: max(list_angka)
angkamin=lambda list_angka: min(list_angka)

print("Bilangan terbesar dari kumpulan bilangan yang di input adalah",angkamax(list_angka))
print("Bilangan terkecil dari kumpulan bilangan di input adalah",angkamin(list_angka))