nombre=input("Ingrese el nombre del archivo csv que quiere poner en MySql\n")
csv=open(nombre,"r")
p = csv.read()
print (p)
