import random

def crearListaNotas(list_materia):
    """Crea una lista de calificaciones para una asignatura de forma
    aleatoria.

    Args:
        list_materia[list[str, int]]: Lista que contiene el nombre y los
            créditos de una asignatura.

    return:
        list_notas[list[str, int, <float x4>]: Lista de calificaciones
            de una asignatura los valores son elegidos al azar.
    """

    # Ciclo para crear 4 calificaciones al azar
    for i in range(4):

        # 10% de probabilidad de que la calificación sea 5.0
        if random.randint(0, 10) == 1:
            nota = 5.0
        else:
            # Valor entero de la nota + valor decimal de la nota
            nota = random.randint(0, 4) + random.random()

        # Redondear a 2 decimales
        nota = round(nota, 1)

        # Agregar el valor de la calificación a list_notas
        list_materia.append(nota)

    # Retornar el valor de list_notas al final del ciclo
    return list_materia


def crearListaMaterias(facultad):
    """Crea una lista de materias y sus respectivas notas al azar.

    Args:
        facultad[str]: Nombre de la facultad a la que pertenece la
            asignatura, si está vacía se elegirá una facultad al azar.

    Return:
        listMaterias[list[str, int]]: Lista de materias con sus
            respectivas notas
    """


    materias_Biologia = [
        ["Microbiología Aplicada", 4],
        ["Biología de la conservación", 4],
        ["Biotecnología Molecular", 2],
        ["Inglés", 2],
        ["Biología de Vertebrados", 4]
        ]

    materias_Psicologia = [
        ["Psicología del desarrollo I", 4],
        ["Antropología", 3],
        ["Inglés", 2],
        ["Psicopatología", 2],
        ["Clínica IV", 4],
        ["Neurociencias III", 3]
        ]

    materias_Admin = [
        ["Introducción a la ciencia Económica", 4],
        ["Costos", 2],
        ["Gestión de lo Público", 2],
        ["Álgebra y Programación Lineal", 2],
        ["Inglés", 2],
        ["Microeconomía I", 4]
        ]

    materias_Medicina = [
        ["La célula", 7],
        ["Pediatría", 9],
        ["Inglés", 2],
        ]

    materias_Industrial = [
        ["Termodinámica", 3],
        ["Procesos Industriales", 3],
        ["Termodinámica", 3],
        ["Ingeniería de Materiales", 3],
        ["Operaciones", 3],
        ["Ingeniería de Métodos", 3]
        ]

    creditos = 0

    if facultad == "":
        materias = random.randint(1, 5)
        if materias == 1:
            return materias_Biologia
        elif materias == 2:
            return materias_Psicologia
        elif materias == 3:
            return materias_Admin
        elif materias == 4:
            return materias_Medicina
        else:
            return materias_Industrial

    else:
        if facultad == "Biología":
            return materias_Biologia
        elif facultad == "Psicología":
            return materias_Psicologia
        elif facultad == "Administración":
            return materias_Admin
        elif facultad == "Medicina":
            return materias_Medicina
        else:
            return materias_Industrial


def facultades():
    """Función para crear listas de facultades
    Return:
        lista_facultades[list]: Lista de calificaciones con las facultades."""

    while True:
        print("Seleccione Facultad:")
        print("Opción 1: Biología")
        print("Opción 2: Psicología")
        print("Opción 3: Administración")
        print("Opción 4: Medicina")
        print("Opción 5: Aleatoria")
        print("Opción 6: Todas")
        seleccion = int(input("Seleccione una opción: "))

        if seleccion not in range(1, 7):
            print()
            print("==================================")
            print("Opción Inválida, intente de nuevo.")
            print("==================================")
            print()
            continue

        if seleccion == 1:
            print()
            print("==================================")
            print("Calificaciones Biología:")
            print("==================================")
            print()
            materias = crearListaMaterias("Biología")

        elif seleccion == 2:
            print()
            print("==================================")
            print("Calificaciones Psicología:")
            print("==================================")
            print()
            materias = crearListaMaterias("Psicología")

        elif seleccion == 3:
            print()
            print("==================================")
            print("Calificaciones Administración:")
            print("==================================")
            print()
            materias = crearListaMaterias("Administración")

        elif seleccion == 4:
            print()
            print("==================================")
            print("Calificaciones Medicina:")
            print("==================================")
            print()
            materias = crearListaMaterias("Medicina")

        elif seleccion == 5:
            print()
            print("==================================")
            print("Calificaciones al azar:")
            print("==================================")
            print()
            materias = crearListaMaterias("")

        else:
            print()
            print("===================================")
            print("Calificaciones Todas las Facultades:")
            print("===================================")
            print()

            lista_facultades = []
            facultades_list = ["Biología", "Psicología", "Administración", "Medicina", "Industrial"]
            for facultad in facultades_list:
                sublist_facultades = []
                sublist_facultades.append(facultad)
                sublist_facultades.append(crearListaMaterias(facultad))
                lista_facultades.append(sublist_facultades)
            return lista_facultades

        for element in materias:
            element = crearListaNotas(element)

        return materias


print(facultades())









