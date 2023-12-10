# DRY (Don't Repeat Yourself)
print("==== FUNCIONES ====")

def saludar(nombre):
  print(f"Hola me llamo {nombre}")

saludar("Linder")

def sumar(n1=0, n2=0):
  print(f"n1 {n1} n2 {n2}")
  return n1 + n2

print(sumar(30, 15))
print(sumar(n2=10, n1=20))

def saludar2(nombre, apellido, edad):
  print(f"Hola me llamo {nombre} {apellido} y tengo {edad} años de edad")

saludar2("Pepe", "Perez", 30)
saludar2(edad=25, nombre="Juan", apellido="Zapata")

print("==== ARGS ====")
def avarage(*notas):
    print(notas)
    suma=0
    for nota in notas:
       suma+=nota
    print(suma/len(notas))

avarage(10,20,17,18,15,12)
print("-"*40)

print("==== Kwargs ====")

def persona(**datos):
   #diccion key:value
#    print(datos)
    print("===Keys===")
    for key in datos.keys():
       print(key)

    print("===Values===")
    for values in datos.values():
       print(values)

    print("===Items===")
    for key, value in datos.items():
       print(key, value)

persona(
   name="Marcos",
   lastname="Arellano",
   phone_number="99999",
   dni=8888888,
   age=55,
   is_developer=True
)