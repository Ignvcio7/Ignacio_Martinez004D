productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], 
         '2175HD': [327990,4],
         'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], 
        '123FHD': [290890,32], 
        '342FHD': [444990,7],
        'GF75HD': [749990,2],
        'UWU131HD': [349990,1],
        'FS1230HD': [249990,0],}
def valida_texto(msg_input):
    while True:
        texto = input(msg_input).strip()
        if texto != "":
            return texto
        else:
            print("Debe ingresar por lo menos un cáracter.")

def valida_numero_entero_positivo(msg_input):
    while True:
        try:
            numero = int(input(msg_input))
            if numero <0:
                print("Debe ingresar un numero entero positivo mayor a 0")
                continue
        except ValueError:
            print("Solo debe ingresar numeros.")

def buscar_nombre(nombre_marca):
    for i in productos:
        if productos[i][0].lower() == nombre_marca.lower():
            note_encontrado = productos[i]
            note_encontrado.insert(0,1)
            return note_encontrado

def stock_marca(marca:str):
    stock_producto = 0
    for i in productos:
        if productos[i][0].lower() == marca.lower():
            for j in stock:
                if j == i:
                    stock_producto += int(stock[j][1])
                    break
    print(f"El stock disponible es de: {stock_producto}")

def buscar_por_precio(precio_minimo, precio_maximo):
    for i in stock:
        if stock[i][0] >= precio_minimo and stock[i][0] <= precio_maximo:
            print(stock[i])

def actualizar_precio(modelo,precio):
    note_encontrado = buscar_nombre(modelo)
    if note_encontrado != None:
        for i in stock:
            if i.lower() == note_encontrado[0].lower():
                stock[i][0] = precio
                print(productos[i])
                return True
            else:
                return False

def menu():
    while True:
        try:
            print("*** MENU PRINCIPAL ***")
            print("Stock marca")
            print("Busqueda por precio")
            print("Actualizar precio")
            print("Salir")

            opcion = int(input("Ingrese una opción: "))
            if opcion < 1 or opcion > 4:
                print("Opción ingresada no existe (1/4)")

            elif opcion == 1:
                nombre_marca = valida_texto("Ingrese el nombre de la marca que desea buscar: ")
                stock_marca(nombre_marca)

            elif opcion == 2:
                precio_minimo = valida_texto("Ingrese el precio minimo que desea buscar")
                precio_maximo = valida_texto("Ingrese el precio maximo que desea buscar")
                buscar_por_precio(precio_minimo,precio_maximo)

            elif opcion == 3:
                modelo = valida_texto("Ingrese el nombre de el modelo: ")
                precio = valida_numero_entero_positivo("Ingrese el nuevo precio a asignar: ")
                actualizar_precio(modelo,precio)

            elif opcion == 4:
                break
        except ValueError:
            print("Ingrese una opción valida")
menu()