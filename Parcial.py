empleado={}
cantidad=int(input(f"\nCuantos empleados desea registra: "))
for i in range(cantidad):
    print(f"Estudiante No. {i+1} ")
    codigo=input("Ingrese codigo: ")
    nombre = input("Ingrese nombre del empleado: ")
    departamento = input("Ingrese el departamento donde labora: ")
    anios_antiguedad=input("Ingrese los años de antiguedad: ")

 empleado[codigo]={      #Creacion del diccionario con clave principal carnet
        "nombre":nombre,
        "departamento":departamento,
        "anios_antiguedad":anios_antiguedad,
    }
desempenio[empleado] = {
    "puntualidad": puntualidad,
    "equipo":equipo,
    "productividad":productividad,
}
contacto[empleado]={
    "telefono":telefono,
    "correo":correo
}





