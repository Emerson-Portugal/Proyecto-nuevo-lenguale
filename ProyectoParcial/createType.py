import LL1
import Lexico

# debe imprimir nuestras varibles
array = [ ]

class analizador:
  def __init__(self, lexema, tipo, categoria , funcion_padre, line = None):        
    self.lexema = lexema
    self.tipo = tipo 
    self.categoria = categoria 
    self.funcion_padre = funcion_padre
    self.line = line

def agregar(lexema, tipo, categoria, funcion_padre):
  node_symbol = analizador(lexema, tipo, categoria, funcion_padre)
  array.append(node_symbol)
  print("Soy tu padre",node_symbol.lexema)

#esta funcion es para que no se repitan las variables
def encontrar(lexema, funcion_padre):
  for symbol in array:
    if symbol.lexema == lexema and symbol.funcion_padre == funcion_padre:
      return symbol

def eliminar():
    print()

print(array)

### -------------- Primera tarea --------- Buscar varibales creadas--------
def buscarVariables(root):
    ## variable generales---------------------
#     global var_function, var_assign, var_declaration
# # nombre de la funcion creada----------- 
#     if root.symbol.symbol == "FUNCTION" :
#         var_function = root.children[1]
#         print("Nombre de la funcion ", var_function.lexeme)
#       #  print("Nombre de la funcion ", root.symbol.symbol.lexeme)

# # nombre de la funcion creada------------ y termindo funcion 
#     if root.symbol.symbol == "FUNCTION" and root.symbol.symbol == "fin_llave":
#         var_function = root.children[1]
#         print("La funcion a terminado")



    if root.symbol.symbol == "id":
        nodo_lexema = root.father
        nodo_tipo = root.father.children[0]
        if nodo_lexema.symbol.symbol == "DECLARATION":
            if nodo_tipo.symbol.symbol == "TYPE":
                categoria = "variable"
                padre = "def"
                agregar(nodo_lexema.children[1].lexeme, nodo_tipo.children[0].lexeme, categoria, padre)
                #print("Ya esta", nodo_tipo.children[0].lexeme )
                #print(" Hola", nodo_lexema.children[1].lexeme)
                #print(categoria)



    for child in root.children:
        buscarVariables(child)







if __name__ == "__main__":
    prueba = open("ProyectoParcial\practica.txt")
    tokens = Lexico.get_tokens(prueba)
    tokens.append(['$', None, None])
    root, node_list = LL1.principal(tokens)
    buscarVariables(root)


