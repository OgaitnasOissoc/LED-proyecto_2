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

            case 1:
                pass
            case 2:
                pass
            case 3:
                break


if __name__ == "__main__":
    title()
    while True:
        selection = menu(["Calculadora de Conjuntos","Sistema de Cifrado de Mensajes"],"Elije una opcion")
        calculator()

