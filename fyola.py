#FYOLA WAHYU KANAYA SALSABILA
#12220031
#tugas plot grafik

import string
import matplotlib.pyplot as plt
punc = string.punctuation

#membuka file txt
file = open('preambule-uud-1945.txt')
file=file.read().lower()
unik={}

#mencari huruf unik dengan tidak memperhatikan tanda baca dan besar kecil huruf
for huruf in file:
    if huruf not in punc:
        if huruf != " " and huruf !="\n":
            unik[huruf] = unik.get(huruf, 0) + 1

list=[]
#melakukan input tuple kedalam sebuah list
for k, v in unik.items():
    list.append((v, k))

#sortir dari huruf yang paling banyak
list = sorted(list, reverse=True)

sbx = []
sby = []
#output huruf unik
for value, key in list:
    print ("huruf" , key, "ada", value)
    #input key dan value ke sebuah list
    sbx.append(key) 
    sby.append(value)

# Code untuk membuat bar charts 
plt.bar(sbx, sby, color ='green',width = 0.7)
plt.xlabel("Huruf Unik")
plt.ylabel("Jumlah Huruf Unik")
plt.title("Huruf Unik dan Jumlahnya")
plt.savefig("Bar Plot Hitung Huruf")
plt.show()