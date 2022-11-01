import pandas as pd
# salida
import sys
# Graficador
import graphviz

from Lexico import get_tokens

fp = open("ProyectoParcial\practica.txt")
guardar_token = get_tokens(fp)


counter = 0
cont = 0
dot = graphviz.Digraph('round-table', comment='parser')
# Para acceder a los datos del archivo CSV, necesitamos una función read_csv() que recupere los datos en forma de Dataframe.
# index_col: Si no hay ninguno, no se muestran números de índice junto con los registros.
syntax_table = pd.read_csv("ProyectoParcial\sys.csv", index_col=0)
# Cree un gráfico creando una instancia de un nuevo objeto Graph o Digraph:
# dot = graphviz.Digraph('round-table', comment='The Round Table')
arbol = graphviz.Graph(comment="Arbol Generedo")


# Recorrer el stack
def print_stack():
    print("\nStack:")
    for e in stack:
        # print("Este es el symbol en stack")
        print(e.symbol, end=" ")
        # print("Este es el is_terminal en stack")
        # print(e.is_terminal, end=" ")
    print()


# Recorrer el tokens
def print_input():
    print("\ntokens:")
    for t in tokens:
        print(t["type"], end=" ")
    print()


# Reemplazar valores /token_type - > Es el primer elemento de tu input
def update_stack(stack, token_type):
    production = syntax_table.loc[stack[0].symbol][token_type]

    # lo que se envia
    #print("Valores de ingreso a la tabla")
    #print(stack[0].symbol, token_type)
    # En que paso en encuentra
    print("\nproceso")
    print(production)
    print()

    #   Error Sintactico
    if (pd.isna(production)):
        print("Error.....")
        sys.exit()

# Aqui pasar de E -> xy a xy
    elementos = production.split(" ")
    #print("Soy el elemento")
    #print(elementos)
    father = elementos[0]
    #print("Soy el padre")
    #print(father)
    # Que es Dot
    # print(dot.source)
    if (elementos[0] in dot.source):
        #print("Como llegue aqui")
        # print(dot.source)
        position = dot.source.rfind(elementos[0])
        #print("Como llegue position")
        # print(position)
        value = dot.source[position]
        #print("Como llegue value")
        # print(value)
        #print("Como llegue value  + algo")

    # elminina los valores
    elementos.pop(0)
    elementos.pop(0)
    # eliminar de la pila
    stack.pop(0)
# -----------------------------------------------------------------------------
    # eliminar de la pila
    # father =  stack.pop(0)
    # IMPLEMENTA UNA FUNCION QUE ME RETORNE UNA INSTACIA A NODE PARSE A PARTIR DE FATHER.ID
    # SERA LA VARIABLE NODE_FATHER

    if elementos[0] == "''":  # nulo
        return

# Vamos a insertar el elemetos a stack pero primero a E

    for i in range(len(elementos) - 1, -1, -1):
        symbol = node_stack(elementos[i], not elementos[i].isupper())
        stack.insert(0, symbol)
        #print("Que es symbol -> solo un lemento")
        # print(elementos[i])
        #print("Que es stack aqui")
        # print(elementos[i].isupper())
    print_stack()

  # creamos y vinculamos el nodo padre al nodo hijo
    for i in range(0, len(elementos)):
        key = str(len(dot.source))
        if (elementos[i] in dot.source):

            dot.node(elementos[i], elementos[i])
            #print("------------PPP")
            #print(elementos[i])
            #print("------------EEE")
            #print(elementos[i])

            if (father == elementos[i]):
                # Equita que sea redundante
                dot.edge(father, elementos[i] + key)
                # Aqui me impirmio ID -> despues de T
                #print("------------YYY")
                #print(father)
                #print("------------AAA")
                #print(elementos[i]+ key)


          #  print("IF father -> "+father+" Se conecta con (elementos[i]+key) -> "+ (elementos[i]+key))
            if (father != elementos[i]):
                # los identifica a cada uno
                dot.edge(father, elementos[i])
                #print("------------XXX")
                #print(father)
                #print("------------ZZZ")
                #print(elementos[i])

          #  print("IF father -> "+father+" Se conecta con elementos[i] -> "+elementos[i])
        else:
          #  print("ELSE father -> " + father + " Se conecta con elementos[i] -> " + elementos[i])



            if (father != elementos[i]):
                dot.edge(father, elementos[i])
                # Es aqui la modifocacion ------------------- ayuda
                #print("------------OOO")
                #print(father)
                #print("------------GGG")
                #print(elementos[i] + key )

    print_stack()

# ------------------------------------------------------------------------------
    # node_father -> BUSCAR
    # node_primario = node_parser(symbol,None,[],node_father,None)
    # node_father.children.append(node_primario)
# se va a generar los nodos y sus relaciones


# Nodo principal -> Se encarga de mover
class node_stack:

    def __init__(self, symbol, is_terminal):
        # cada Stack -> tendra un id para identificarlo propiamente !!!
        global counter
        #print("Este el counter en node_stack")
        # print(counter)
        self.id = counter
        self.symbol = symbol  # simbolo de la gramatica
        self.is_terminal = is_terminal
        counter += 1
        #print("Este el symbol en node_stack")
        # print(symbol)
        #print("Este el is_terminal en node_stack")
        # print(is_terminal)


# Las Hojas
class node_parser:

    def __init__(self, node_st, lexeme=None, children=[], father=None, line=None):
        self.node_st = node_st
        self.lexeme = lexeme
        self.line = line
        self.children = children
        self.father = father


#  Entrada para el Stak
stack = []
symbol_1 = node_stack('$', True)  # numero 0 en stack
symbol_2 = node_stack('PROGRAM', False)  # numero 1 en stack
stack.insert(0, symbol_1)
stack.insert(0, symbol_2)
# ------------------------------------------------------------------
# Creaer el node -> raiz -> symbol_2
# raiz = node_parser(symbol_2)
#print("Este es el stack")
#print(stack)

#  Entrada para el Input -> se modifica
# lexema -> tu como usuario has ingresado
# type -> tipo (identificador)
tokens = guardar_token
# Empezamos las condicionales

while True:
    print("ITERATION ...")
    print_stack()
    print_input()
    if stack[0].symbol == '$' and tokens[0]['type'] == '$':
        print("Todo bien!")
        break

    if stack[0].is_terminal:
        # Cuando Ambos son iguales osea Terminales
        print("Que haces")
        print(stack[0].is_terminal)

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

# renderizar arbol
dot.render('arbol.gv').replace('\\', '/')
dot.render('arbol.gv', view=True)

#print(dot.source)
