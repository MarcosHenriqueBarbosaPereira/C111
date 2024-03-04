loja1 = {"Samsumg", "Apple", "Motorola"}
loja2 = {"Xiaomi", "LG", "Apple", "Sony", "Tesla"}

#Número de marcas que estão presentes em cada loja
print("Número de modelos na loja 1: ", len(loja1))
print("Número de modelos na loja 2: ", len(loja2))

#Marcas que estão presentes em cada loja
print("Marcas na loja 1: ", loja1)
print("Marcas na loja 2: ", loja2)

#Marcas que estão presentes em ambas as lojas
print("Marcas presentes em ambas as lojas: ", loja1.intersection(loja2))