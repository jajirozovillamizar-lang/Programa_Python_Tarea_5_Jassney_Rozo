#Nombre del estudiante: Jassney Jimena Rozo Villamizar
#Grupo:213022_323
#Programa:Ingenieria Multimedia
#Codigo fuente: autoria propia

#------------------------------------------------------

#R1 menu con los productos y precios en una matriz

menu_postres = [
    ["Helado de brownie", "Helados", 15000],
    ["Banana Split", "Helados", 20000],
    ["Cheesecake de frutos rojos", "Pasteles", 20000],
    ["Torta de chocolate", "Pasteles", 18000],
    ["Malteada de oreo", "Bebidas", 12000],
    ["Granizado de milo", "Bebidas", 10000]
]



#R2 Establecer las condiciones para el descuento 

def aplicar_descuento(precio_base, categoria_producto):
    # Definimos nuestras reglas
    categoria_objetivo = "Helados"
    umbral = 18000
    
    if categoria_objetivo == categoria_producto and precio_base > umbral:
        descuento = 0.15 * precio_base  # 15% de descuento
        precio_final = precio_base - descuento
    else:
        
        precio_final = precio_base
    
    return precio_final # Debe mostrarse el valor

# R3 mostrar el menu al cliente

compra_realizada=[] #(R7)aca se guardaran los productos que el cliente compre para moestarr el resumen al final de la compra
total_a_pagar = 0
continuar = "si"

print("Bienvenido a Dulces Delicias, a continuacion te presento nuestro menu de postres y bebidas")
while continuar.lower() == "si": 
    
    print("\n")

    for i, postre in enumerate(menu_postres):
        nombre = postre[0]
        precio = postre[2]
        print(f"{i}. {nombre} - ${precio}")

    print("\n")

    
    #R4 dar la eleccion al cliente
    print("¿Que postre deseas hoy?")
    seleccion=int(input("Ingresa el numero correspondiente al postre que deseas llevar"))   

    if seleccion >= 0 and seleccion <= 5:

        #R5 mostrar el precio final despues de pasar la eleccion por la funcion y ver si aplica descuento o no  
        postre_seleccionado = menu_postres[seleccion]
        precio_actual = postre_seleccionado[2]
        categoria_actual = postre_seleccionado[1]
        nombre_actual = postre_seleccionado[0]

        precio_final = aplicar_descuento(precio_actual, categoria_actual)
        print("\n")
        print(f"El precio final de {nombre_actual} es ${precio_final}")

        # Guardamos los datos del postre actual en la lista de historial (R7)
        compra_realizada.append([nombre_actual, precio_actual, precio_final])


        total_a_pagar += precio_final
        
    else:   
        print("¡Ese número no está en el menú! Por favor, intenta de nuevo.")   

        
        #R6 preguntar si desea ordenar algo mas, validando que la respuesta sea si o no, y en caso de no serlo, pedir que responda nuevamente hasta que lo haga correctamente
    print("\n")
    while True:
        continuar = input("¿Deseas ordenar algo mas? (si/no): ").lower()
        
        if continuar == "si" or continuar == "no":
            break  
        else:
            print(" Por favor responde únicamente 'si' o 'no'.")
    
print("-" * 50)
print("\n")

#R7 salida de los datos finales, total a pagar y despedida
print("Gracias por tu compra, esperamos haber endulzado tu dia y vuelvas pronto a Dulces Delicias")
print("Resumen de la compra:")
for item in compra_realizada:
    # item[0]=nombre, item[1]=precio base, item[2]=precio con descuento
    print(f"- {item[0]} | Precio Base: ${item[1]} | Pago Final: ${item[2]}")
print("\n")
print(f"Total a pagar: ${total_a_pagar}")