import LL1
import Lexico
from collections import Counter

# debe imprimir nuestras varibles
prueba = open("ProyectoParcial\practica.txt")
tokens = Lexico.get_tokens(prueba)
tokens.append(['$', None, None])
root, node_list = LL1.principal(tokens)


class analizador:
  def __init__(self, lexema, tipo, categoria , funcion_padre, line = None):        
    self.lexema = lexema
    self.tipo = tipo 
    self.categoria = categoria 
    self.funcion_padre = funcion_padre
    self.line = line

array = [ ]
array_muerte = [ ]
funcion = "def"


def identificado(root):
  stack = root.children
  arr = []
  while len(stack) > 0:
    if stack[0].symbol.symbol == 'TERM':
      arr.append(stack[0].children[0].symbol.symbol)
    temp = stack[0].children
    stack.pop(0)
    for i in temp:
      stack.insert(0, i)
  ty = arr[0]
  flag = False
  for j in arr:
    if j != ty:
      flag = True
      break
  if flag:
    return "Error"
  return ty




# Aqui agregamos los valores --------------------------------------------
def agregar(lexema, tipo, categoria, funcion_padre):
    node_symbol = analizador(lexema, tipo, categoria, funcion_padre)
    array.append(node_symbol)


#esta funcion es para que no se repitan las variables
def encontrar(lexema):
  valor = False
  for symbol in array:
    if symbol.lexema == lexema:
      valor = True
  return valor  


def buscarVariables(root):

# Creacion de funciones-------------------------------------------------

  if root.symbol.symbol == "FUNCTION":
    if encontrar(root.children[1].lexeme):
      print("FUNCION YA  CREADA -> ERROR EN LINEA ->", root.children[1].line)
    else:
      print("FUNCION CREADA CORRECTAMENTE")
      tipo = "FUNCION"
      categoria = None
      padre = "LIBRE"
      agregar(root.children[1].lexeme, tipo, categoria, padre)

# Creacion de variables--------------------------------------------------
  if (root.symbol.symbol == 'DECLARATION'):
      variable = root.children[1]
      nodo_tipo = root.children[0]
      expresion = identificado(root)     
      aux = root
 
      # Vamos a comprovar si esta o no es una funcion------------------
      while aux.symbol.symbol != 'FUNCTION':
        if aux.father == None:
          break
        aux = aux.father

      padre_asigando = "LIBRE"
      ## tomanos el nombre de la funcion perteneciente 
      if aux.symbol.symbol == 'FUNCTION':
        padre_asigando = aux.children[1].lexeme

      if encontrar(variable.lexeme):
        print("VARIABLE YA CREADA -> ERROR EN LINEA ->", variable.line)
      else:
        print("VARIABLE CREADA -> EN LINEA ->", variable.line)
        if nodo_tipo.children[0].lexeme == "bool" and  expresion == "BOOLEAN" :
            tipo = "id"
            categoria = expresion
            padre = padre_asigando
            agregar(variable.lexeme, tipo, categoria, padre)

        elif nodo_tipo.children[0].lexeme == "int" and  expresion == "num": 
            tipo = "id"
            categoria = expresion
            padre = padre_asigando
            agregar(variable.lexeme, tipo, categoria, padre)

        else:
          print("ERROR DE TIPOS -> EN LINEA ->", variable.line)


# Asigacion de variables-------------------------------------------------

  if root.symbol.symbol == 'id' and root.father.symbol.symbol != 'DECLARATION' and root.father.symbol.symbol != 'FUNCTION':
    flag = False
    for i in array:
      if i.lexema == root.lexeme:
        print('VARIABLE EN USO -> EN LINEA ->', root.line )
        flag = True

    if not flag:
      print('VARIABLE NO CREADA -> ERROR EN LINEA ->', root.line )
      #return


## Eliminacion de los valores de las funciones -------------------------------------

  if root.symbol.symbol == 'fin_llave' and root.father.symbol.symbol == 'FUNCTION':

    count = 0
    for i in array:
      if i.funcion_padre == root.father.children[1].lexeme:
        count = count + 1

    while count > 0:
      for j in array:
        if j.funcion_padre == root.father.children[1].lexeme:
          array.remove(j)
      count = count - 1





  for child in root.children:
    buscarVariables(child)

        
buscarVariables(root)






for symbol in array:
  print(symbol.lexema, symbol.tipo, symbol.categoria, symbol.funcion_padre)




