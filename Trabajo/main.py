import pandas as pd
# salida 
import sys
# Graficador
import graphviz

counter = 0
cont = 0

syntax_table = pd.read_csv("ProyectoParcial\syntax_table.csv", index_col=0)
arbol = graphviz.Graph(comment = "Arbol Generedo")

## Recorrer el stack
def print_stack():
    print("\nStack:")
    for e in stack:
        print(e.symbol, end=" ")
    print()


## Recorrer el tokens
def print_input():
    print("\ntokens:")
    for t in tokens:
        print(t["type"],end=" ")
    print()


## Reemplazar valores /token_type - > Es el primer elemento de tu input
def update_stack(stack, token_type):
    production = syntax_table.loc[stack[0].symbol][token_type]

# En que paso en encuentra
    print("\nproceso")
    print(production)
    print()

#   Error Sintactico
    if(pd.isna(production)):
        print("Error.....")
        sys.exit()


## Aqui pasar de E -> xy a xy
    elementos = production.split(" ")
    elementos.pop(0)
    elementos.pop(0)
# eliminar de la pila
    stack.pop(0)

    if elementos[0] == "''":  # nulo
        return

#Vamos a insertar el elemetos a stack pero primero a E
    
    for i in range(len(elementos)-1, -1, -1):
        symbol = node_stack(elementos[i], not elementos[i].isupper())
        stack.insert(0, symbol)
    print_stack()



# Nodo principal -> Se encarga de mover 
class node_stack:
  def __init__(self, symbol, is_terminal):
    global counter
    self.id = counter 
    self.symbol = symbol        # simbolo de la gramatica
    self.is_terminal = is_terminal
    counter += 1

# Las Hojas 
class node_parser:
    def __init__(self, node_st, lexeme=None, children=[], father=None, line=None):
        self.node_st = node_st
        self.lexeme = lexeme
        self.line = line
        self.children = children
        self.father = father


#  Entrada para el Stark
stack = [ ]
symbol_1 = node_stack('$', True)
symbol_2 = node_stack('E', False)
stack.insert(0, symbol_1)
stack.insert(0, symbol_2)

#  Entrada para el Input -> se modifica

tokens = [
                {'type':'id','lexema':'x', 'line': '1' },
                {'type':'+','lexema':'+', 'line': '1' },
                {'type':'id','lexema':'y', 'line': '1' },
                {'type':'$','lexema':'$', 'line': '1' }
                ]
# Empezamos las condicionales

while True:
    print("ITERATION ...")
    print_stack()
    print_input()
    if stack[0].symbol == '$' and tokens[0]['type'] == '$':
        print("Todo bien!")
        break

    # Cuando Ambos son iguales osea Terminales
    if stack[0].is_terminal:
        print("terminales ...")
        if stack[0].symbol == tokens[0]['type']:
            stack.pop(0)
            tokens.pop(0)
        else:
            print("ERROR sintáctico")
            break



    # Cuando Son diferentes y se tiene que reemplazar segun la tabla
    else:
        update_stack(stack, tokens[0]['type'])

