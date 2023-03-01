def totalderet(bilanganawal,selisihbilangan,banyaksuku):
    hasil=(banyaksuku/2)*((2*bilanganawal)+(banyaksuku-1)*selisihbilangan)
    print("Total dari deret aritmatika tersebut adalah : ",hasil)

print("================= BARIS ARITMATIKA ===============")
bilanganawal=int(input("Masukkan bilangan awal : "))
selisihbilangan=int(input("Masukkan selisih bilangan : "))
banyaksuku=int(input("Masukkan banyaknya suku : "))
totalderet(bilanganawal,selisihbilangan,banyaksuku)

