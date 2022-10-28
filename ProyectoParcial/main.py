import pandas as pd
# salida 
import sys
# Graficador
import graphviz

counter = 0

syntax_table = pd.read_csv("ProyectoParcial\sysntax.csv", index_col=0)
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

## Empeamos la construccion del Grama
    elementos = production.split(" ")

    #Sera  el primer nodo del arbol
    sourc = elementos[0]

    ## se empieza el grafo

    if(elementos[0] in arbol.source):
        aux = arbol.source[arbol.source.rfind(elementos[0])]
        i = 1
        while(True):
            if(arbol.source[arbol.source.rfind(elementos[0])+i] == '"'):
                    break
            else:
                aux = aux + arbol.source[arbol.source.rfind(elementos[0])+i]
                i = i + 1
        sourc = aux.strip()

## Aqui pasar de E -> xy a xy

    elementos.pop(0)
    elementos.pop(0)
# eliminar de la pila
    stack.pop(0)

## Si hay un espacio se ignora pero ese valor debe consederarse en el grafico
    if elementos[0] == "''":  # nulo
        for f in range(len(elementos)):
            if(elementos[f] in arbol.source):
                key = str(len(arbol.source))
                arbol.node(elementos[f]+key, "𝓔")   # nodo del arbol
                arbol.edge(sourc, elementos[f]+key)  #Coneccion de nodo

            if(elementos[f] not in arbol.source): ## vemos si el nodo pertenece a su padre
                arbol.node(elementos[f], "𝓔")           ## Es el nodo del abol
                arbol.edge(sourc, elementos[f])       ## es la coleccion de nodos        
        return

#Vamos a insertar el elemetos a stack pero primero a E
    
    for i in range(len(elementos)-1, -1, -1):
        symbol = node_stack(elementos[i], not elementos[i].isupper())
        stack.insert(0, symbol)
   # print_stack()

## se va a generar los nodos y sus relaciones

    for f in range(len(elementos)):
        if(elementos[f] in arbol.source):
            key = str(len(arbol.source))
            arbol.node(elementos[f]+key, elementos[f])
            arbol.edge(sourc, elementos[f]+key)

        if(elementos[f] not in arbol.source):
            arbol.node(elementos[f], elementos[f])
            arbol.edge(sourc, elementos[f])


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
symbol_2 = node_stack('EXP', False)
stack.insert(0, symbol_1)
stack.insert(0, symbol_2)

#  Entrada para el Input -> se modifica

tokens = [
                {'type':'id','lexema':'id', 'line': '1' },
                {'type':'equal','lexema':'equal', 'line': '1' },
                {'type':'true','lexema':'id', 'line': '1' },
                {'type':'$','lexema':'$', 'line': '1' }
                ]
# Empezamos las condicionales

while True:
    print("ITERATION ...")
    print_stack()
    print_input()
    if stack[0].symbol == '$' and tokens[0]['type'] == '$':
        print("Todo bien! \n")
        break

    # Cuando Ambos son iguales osea Terminales
    if stack[0].is_terminal:
        print("terminales ... \n")
        if stack[0].symbol == tokens[0]['type']:
            stack.pop(0)
            tokens.pop(0)
        else:
            print("ERROR sintáctico")
            break
    # Cuando Son diferentes y se tiene que reemplazar segun la tabla
    else:
        update_stack(stack, tokens[0]['type'])


arbol.render(filename="arbol", format="png")
