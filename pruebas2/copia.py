# ------------------------------------------------------------
import ply.lex as lex

# r'atring' -> r significa que la cadena es tradada sin caracteres de escape,
# es decir r'\n' seria un \ seguido de n (no se interpretaria como salto de linea)

 # List of token names.   This is always required

reserved = {
  'imprimir' : 'IMPRIMIR',
  'definir' : 'DEFINIR',
  'si' : 'CONDICIONAL_SI',
  'sino' : 'CONDICIONAL_SINO',
  'fin' : 'FIN_SI',
  'verdadero' : 'VERDADERO',
  'falso' : 'FALSO',
  'mientras' : 'MIENTRAS',
  'para' : 'PARA',
  'en' : 'EN',
  'rango' : 'RANGO',
  'final' : 'FIN_BUCLE',
  'retornar' : 'RETORNAR',
  'entero' : 'VAR_ENTERO',
  'cadena' : 'VAR_CADENA',
  'flotante' : 'VAR_FLOTANTE',
  'booleano' : 'VAR_BOOLEANO',
  'finalizar' : 'FIN_CODIGO'
}

tokens = [
    'ID',
    'NUM',
    'OPERADOR_SUM',
    'OPERADOR_REST',
    'OPERADOR_MULT',
    'OPERADOR_DIV',
    'PAR_IZQ',
    'PAR_DER',
    'COMENTARIO_UNO',
    'COMENTARIO_DOS',
    'COMP_MENOR_QUE',
    'COMP_MAYOR_QUE',
    'IGUAL',
    'COMA',
    'COR_IZQ',
    'COR_DER',
    'DOS_PUNTOS',
    'CADENA'
    
] + list(reserved.values())
 
 # Regular expression rules for simple tokens
#t_NUMERO  = r'\d+'
t_OPERADOR_SUM    = r'\+'
t_OPERADOR_REST   = r'\-'
t_OPERADOR_MULT   = r'\*'
t_OPERADOR_DIV  = r'\/'
t_PAR_IZQ = r'\('
t_PAR_DER  = r'\)'
t_COR_IZQ = r'\{'
t_COR_DER = r'\}'
t_IMPRIMIR = r'imprimir'
t_DEFINIR = r'definir'
t_VERDADERO = r'verdadero'
t_FALSO = r'falso'
t_CONDICIONAL_SI = r'si'
t_CONDICIONAL_SINO = r'sino'
t_FIN_SI = r'fin'
t_MIENTRAS = r'mientras' 
t_PARA = r'para'
t_EN = r'en'
t_RANGO = r'rango'
t_FIN_BUCLE = r'final'
t_COMP_MAYOR_QUE = r'\>'
t_COMP_MENOR_QUE = r'\<'
t_IGUAL = r'\='
t_RETORNAR = r'\retornar'
t_COMA = r'\,'
t_DOS_PUNTOS = r'\:'
 # A regular expression rule with some action code

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)  # guardamos el valor del lexema  
    #print("se reconocio el numero")
    return t
def t_CADENA(t):
  r'\"([a-zA-Z0-9" "".""_""-"]+)"'
  t.type = reserved.get(t.value, 'CADENA')
  return t

def t_COMENTARIO_UNO(t):
  r'\#([a-zA-Z0-9" "]+)'
  t.type = reserved.get(t.value, 'COMENTARIO_UNO')
  return t

def t_COMENTARIO_DOS(t):
  r'\@([a-zA-Z0-9" ""\n"]+)@'
  t.type = reserved.get(t.value, 'COMENTARIO_DOS')
  return t

def t_ID(t):
  r'[a-zA-Z]+([a-zA-Z0-9]*)'
  t.type = reserved.get(t.value, 'ID')
  return t
  
 # Define a rule so we can track line numbers
def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
 # A string containing ignored characters (tabs)
t_ignore  = ' \t'
 
 # Error handling rule
def t_error(t):
    print("Caracter Ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()

# Leer Input.txt
fileObject = open("pruebas2\Input.txt", "r")
data = fileObject.read()
print(data)
 
# Give the lexer some input
lexer.input(data)

# Tokenize
tokens2 = []
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    #print(tok)
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
    tokens2.append({'type': tok.type.lower(), 'lexeme':str(tok.value).lower(), 'line': tok.lineno})

tokens2.append({'type':'$', 'lexeme':'$', 'line': tokens2[-1]['line']})
print(tokens2)