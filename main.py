from set import Set
from simple_term_menu import TerminalMenu

def menu(x, y):
    print(y)
    terminal_menu = TerminalMenu(x)
    return terminal_menu.show()
    clear()


def clear():
    print('\n'*70)


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
                pass
            case 3:
                break


if __name__ == "__main__":
    title()
    while True:
        selection = menu(["Calculadora de Conjuntos","Sistema de Cifrado de Mensajes"],"Elije una opcion")
        calculator()

