def mencarikataterpanjang(kalimat):
    kataterpanjang=""
    kata2=kalimat.split()
    for kata in kata2:
        if len(kata)>len(kataterpanjang):
            kataterpanjang=kata
    return kataterpanjang

kalimat=input("Masukkan sebuah kalimat: ")

print("Kata terpanjang dalam kalimat tersebut adalah:",mencarikataterpanjang(kalimat))