from set import Set
from cifrado import Participant,Conection
from simple_term_menu import TerminalMenu

def clear():
    print('\n'*70)


def menu(x, y):
    print(y)
    terminal_menu = TerminalMenu(x)
    choice = terminal_menu.show()
    clear()
    return choice


def title():
    print("\n"*75+'*'*67+'\n'+'*'*8 + "PROYECTO INTEGRADOR: Módulo I, Teoria de Conjutnos "+ '*'*8 +'\n'+'*'*8+f"{'Santiago Cossio Schondube':<51}"+'*'*8+'\n'+'*'*8+f"{'Fernando Ulloa Garcia':<51}"+'*'*8+'\n'+'*'*8+f"{'Pablo Enrique Estrada Samaniego':<51}"+'*'*8+'\n'+'*'*67)


def calculator():
    u = Set(True)
    sets = {}
    while True:
        calculator_selection = menu(["Creación de conjuntos","Operaciones de conjuntos","Funciones de verificación","Salir"],"Elije una opcion:")
        match calculator_selection:
            case 0:
                selection = menu(["A","B","C"],"Elije una opcion")
                sets[selection] = Set(False)
                selection2 = menu(["Manualmente","Aleatoreamente"],"Como asignar valores:")
                if selection2 == 0:
                    userset = input("Ingresa el conjunto con elementos separados por comas\n")
                    userset = userset.split(',')
                    sets[selection].userset(userset)
                    clear()
                    print(sets[selection].set)
                else:
                    sets[selection].randset(menu(["Numeros","Caractares"],"Que tipo de valores tiene el conjunto:"))
                u.set += sets[selection].set
                u.set = u.remove_dupes(u.set)

            case 1:
                selection2 = menu(["Unión","Intersección","Diferencia","Diferencia simétrica","Complemento"],"Elige una operacion:")
                a = menu(["A","B","C"], "Elige el primer conjunto:")
                if selection2 != 4:
                    b = menu(["A","B","C"], "Elige el segundo conjunto:")
                match selection2:
                    case 0:
                        print(sets[a].union(sets[b].set))
                    case 1:
                        print(sets[a].interseccion(sets[b].set))
                    case 2:
                        print(sets[a].diferencia(sets[b].set))
                    case 3:
                        print(sets[a].diferencia_simetrica(sets[b].set))
                    case 4:
                        print(sets[a].complemento(u.set))
            case 2:
                selection2 = menu(["Subconjunto","Subconjunto propio","Conjuntos disjuntos", "Igualidad de conjuntos"],"Elige una funcion de verificacion")
                a = menu(["A","B","C"], "Elije el primer conjunto")
                b = menu(["A","B","C"], "Elije el segundo conjunto")
                clear()
                match selection2:
                    case 0:
                        print(sets[a].subconjunto(sets[b].set))
                    case 1:
                        print(sets[a].subconjunto_propio(sets[b].set))
                    case 2:
                        print(sets[a].disjunto(sets[b].set))
                    case 3:
                        print(sets[a].igualdad(sets[b].set))
            case 3:
                break

def cifrado():
    emisores = Participant([])
    receptores = Participant([])
    llaves = Participant([])
    conexiones = Conection([])
    while True:
        selection = menu(["Gestión de Emisores","Gestion de Receptores","Gestión de llaves","Creación de conexiones","Verificación de propiedades de funciones","Verificación de propiedades de relaciones","Calculadora de conjuntos","salir"],"Elije una opcion")
        match selection:
            case 0:
                while True:
                    selection2 = menu(["Agregar usuario","Eliminar usuario","Ver usuarios","salir"],"Elije una opcion")
                    match selection2:
                        case 0:
                            emisores.add_user(input("Ingresar usuario: "))
                        case 1:
                            emisores.remove_user(input("Ingresar usuario: "))
                        case 2:
                            print(emisores.users)
                        case 3:
                            break
            case 1:
                while True:
                    selection2 = menu(["Agregar usuario","Eliminar usuario","Ver usuarios","salir"],"Elije una opcion")
                    match selection2:
                        case 0:
                            receptores.add_user(input("Ingresar usuario: "))
                        case 1:
                            receptores.remove_user(input("Ingresar usuario: "))
                        case 2:
                            print(receptores.users)
                        case 3:
                            break
            case 2:
                while True:
                    selection2 = menu(["Agregar llave","Eliminar llave","Ver llaves","salir"],"Elije una opcion")
                    match selection2:
                        case 0:
                            llaves.add_user(input("Ingresar llave: "))
                        case 1:
                            llaves.remove_user(input("Ingresar llave: "))
                        case 2:
                            print(llaves.users)
                        case 3:
                            break

            case 3:
                em = menu(emisores.users,"Elige emisor:")
                re = menu(receptores.users,"Elige receptor:")
                lla = menu(llaves.users,"Elije llave:")
                conexiones.add_conection(em,re,lla)
            case 4:
                selection2 = menu(["Agregar usuario","Eliminar usuario","Ver usuarios","salir"],"Elije una opcion")
            case 5:
                pass
            case 6:
                pass
            case 7:
                break

if __name__ == "__main__":
    title()
    while True:
        selection = menu(["Calculadora de Conjuntos","Sistema de Cifrado de Mensajes","Salir"],"Elije una opcion")
        match selection:
            case 0:
                calculator()
            case 1:
                cifrado()
            case 2:
                break

