empleado = {}
cantidad = int(input(f"\nCuantos empleados desea registrar: "))
for i in range(cantidad):
    print(f"Empleado No. {i+1} ")
    codigo = input("Ingrese codigo: ")
    nombre = input("Ingrese nombre del empleado: ")
    departamento = input("Ingrese el departamento donde labora: ")
    anios_antiguedad = input("Ingrese los años de antiguedad: ")

    print("\n***Evaluacion de desempeño de 0 a 10***")
    puntualidad = float(input("Calificacion de puntualidad: "))
    equipo = float(input("Calificacion de trabajo en equipo: "))
    productividad = float(input("Calificacion por productividad: "))

    print("\n***Contactos***")
    telefono = input("Ingrese numero de telefono: ")
    correo = input("Ingrese correo electronico: ")

    empleado[codigo] = {
        "datos_personales": {
            "nombre": nombre,
            "departamento": departamento,
            "anios_antiguedad": anios_antiguedad
        },
        "evaluacion_desempenio": {
            "puntualidad": puntualidad,
            "equipo": equipo,
            "productividad": productividad
        },
        "contacto": {
            "telefono": telefono,
            "correo": correo
        }
    }

print("\nINFORMACION DEL EMPLEADO:")
for codigo, datos in empleado.items():
    print(f"\nCódigo del empleado: {codigo}")
    print(f"Nombre: {datos['datos_personales']['nombre']}")
    print(f"Departamento: {datos['datos_personales']['departamento']}")
    print(f"Años de antigüedad: {datos['datos_personales']['anios_antiguedad']}")

    print("Evaluación de desempeño:")
    suma = 0
    contador = 0
    for clave, valor in datos['evaluacion_desempenio'].items():
        print(f"  {clave.capitalize()}: {valor}")
        suma += valor
        contador += 1

    promedio = suma / contador
    print(f"Promedio de desempeño: {promedio:.2f}")

    print("contacto: ")
    for clave, valor in datos['contacto'].items():
        print(f"  {clave.capitalize()}")









