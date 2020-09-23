n = int(input("oricare numar mai mic ca 10000: "))

n1 = n % 10
n2  = (n // 10) % 10

print("ultima cifra= ", n1)
print("penultima cifra=",n2)
print("restul impartirii la 9=",n%9)
print("catul impartirii la 9=",n/9)

suma_cifrelor = 0
for cifra in str(n):
 suma_cifrelor += int(cifra)

print("suma cifrelor=",suma_cifrelor)






