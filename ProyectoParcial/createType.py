import LL1
import Lexico
from collections import Counter
from crearAsembly import convertir
from crearAsembly import inicializarVar

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
  # Aqui  se envia el papa  -> root
  #  root.children -> saca los hijos de papa 
  stack = root.children
  # creamos un array para  comparar 
  arr = []
  valor = []
  signo = []
  while len(stack) > 0:

    if stack[0].symbol.symbol == "OPER":
      signo.append(stack[0].children[0].lexeme)
    # En este caso --- buscamos el papa donde se encuentra las variables
    if stack[0].symbol.symbol == 'TERM':
      # agregamos e los hijos  al arrray creado
      arr.append(stack[0].children[0].symbol.symbol)
      valor.append(stack[0].children[0].lexeme)
    temp = stack[0].children
    stack.pop(0)

    # vamos a iterrar sobre los valores para insertalos en el stack 
    for i in temp:
      stack.insert(0, i)
  ty = arr[0]

  flag = False
  for j in arr:
    if j != ty:
      flag = True
      break
  if flag:
    return "Error",valor, signo
  return ty, valor, signo


###------------------------------------------------------------------------------
def pack(root):
  stack = root.children
  valor_id = []
  while len(stack) > 0:
    if stack[0].symbol.symbol == 'DECLARATION':
      valor_id.append(stack[0].children[1].lexeme)
    temp = stack[0].children
    stack.pop(0)
    for i in temp:
      stack.insert(0, i) 
  inicializarVar(valor_id)



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
      expresion, valor, signo = identificado(root)

      aux = root


      #inicializarVar(variable)

      for i  in (array):
          for j in range(len(valor)):
            if i.lexema == valor[j]:
              expresion = i.categoria


 
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
        
        if nodo_tipo.children[0].lexeme == "bool" and  expresion == "BOOLEAN" :
            print("VARIABLE CREADA -> EN LINEA ->", variable.line)
            tipo = "id"
            categoria = expresion
            padre = padre_asigando
            agregar(variable.lexeme, tipo, categoria, padre)

        elif nodo_tipo.children[0].lexeme == "int" and  expresion == "num": 
            print("VARIABLE CREADA -> EN LINEA ->", variable.line)
            tipo = "id"
            categoria = expresion
            padre = padre_asigando

            convertir(variable, signo, valor)
            agregar(variable.lexeme, tipo, categoria, padre)

        else:
          print("ERROR DE TIPOS -> EN LINEA ->", variable.line)


# Asigacion de variables-------------------------------------------------

  if root.symbol.symbol == 'ASSIGN' and root.father.symbol.symbol != 'DECLARATION' and root.father.symbol.symbol != 'FUNCTION':
    sub_valor = root.children[0]

    valor = identificado(root)
    flag = False
    for i in array:

      if i.lexema == sub_valor.lexeme and i.categoria == valor:
        print('VARIABLE EN USO -> EN LINEA ->', sub_valor.line )
        flag = True
      elif i.lexema == sub_valor.lexeme and i.categoria != valor:
        print('ERROR DE ASIGACION -> EN LINEA ->', sub_valor.line )
        flag = True

    if not flag:
        print('VARIABLE NO CREADA -> ERROR EN LINEA ->',  sub_valor.line )
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

#pack(root)
buscarVariables(root)



for symbol in array:
  print(symbol.lexema, symbol.tipo, symbol.categoria, symbol.funcion_padre)



