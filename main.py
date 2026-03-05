from set import Set
from simple_term_menu import TerminalMenu

def menu(x):
    terminal_menu = TerminalMenu(x)
    return terminal_menu.show()


def clear():
    print('\n'*70)


def title():
    print("\n"*75+'*'*67+'\n'+'*'*8 + "PROYECTO INTEGRADOR: Módulo I, Teoria de Conjutnos "+ '*'*8 +'\n'+'*'*8+f"{'Santiago Cossio Schondube':<51}"+'*'*8+'\n'+'*'*8+f"{'Fernando Ulloa Garcia':<51}"+'*'*8+'\n'+'*'*8+f"{'Pablo Enrique Estrada Samaniego':<51}"+'*'*8+'\n'+'*'*67)


def main_menu():
    print("Elige una opcion:")
    return menu(["Calculadora de Conjuntos","Sistema de Cifrado de Mensajes"])


def calculator():
    u = Set(True)
    sets = {}
    while True:
        print("Elige una opcion:")
        calculator_selection = menu(["Creación de conjuntos","Operaciones de conjuntos","Funciones de verificación","Salir"])
        clear()
        match calculator_selection:
            case 0:
                selection = menu(["A","B","C"])
                sets[selection] = Set(False)
                clear()
                selection2 = menu(["Asignar valores manualmente","Asignar valores aleatoreamente"])
                clear()
                if selection2 == 0:
                    userset = input("Ingresa el conjunto con elementos separados por comas\n")
                    userset.split(',')
                    sets[selection].userset(userset)
                    clear()
                else:
                    print("Que tipo de valores deberia tener el conjunto")
                    sets[selection].randset(menu(["Numeros","Caractares"]))
                    clear()

            case 1:
                pass
            case 2:
                pass
            case 3:
                break


if __name__ == "__main__":
    title()
    while True:
        selection = main_menu()
        clear()
        calculator()

