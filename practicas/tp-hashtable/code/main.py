import dictionary as d
#D = [5, 28, 19, 15, 20, 33, 12, 17, 10]
N = 5
D = [None] * N
print(d.func_hash(D , 9))
#--------Insert--------
#Si el diccionario esta vacio:
d.insert(D , 0 , "H0")
d.insert(D , 1 , "H1")
d.insert(D , 2 , "H2")
d.insert(D , 3 , "H3")
d.insert(D , 4 , "H4")
d.insert(D , 5 , "H5")
#Si no esta vacio:
d.insert(D , 10 , "H10")
d.insert(D , 9 , "H9")
#Si en la key ya hay un valor que ya estaba entonces:
d.insert(D , 20 , "H0")

print("--------Search--------")
#--------Search--------
print(d.search(D , 0))
print(d.search(D , 3))
print(d.search(D , 5))
print(d.search(D , 10))
print(d.search(D , 100))

print("--------FIN--------")
