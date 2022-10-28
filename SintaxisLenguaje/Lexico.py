import ply.lex as lex


reserved = {
  'true' : 'true',
  'false' : 'false',
  'if' : 'if',
  'return' : 'return',
  'int' : 'int',
  'bool' : 'bool',
  'def': 'def'
}
tokens = [
	'id',
	'num',
	'addition', 
	'subtract', 
	'multiplication', 
	'division', 
	'equal',
	'mayor',
	'minor',
	'lparem',
	'rparem',
  'ini_llave',
	'fin_llave',
	'dotcomma',
	'comma'
]+ list(reserved.values())

# Regular expression rules for simple tokens
t_addition = r'\+'
t_subtract = r'\-'
t_multiplication = r'\*'
t_division = r'\/'
t_equal = r'\='
t_mayor = r'\>'
t_minor = r'\<'
t_lparem = r'\('
t_rparem = r'\)'
t_ini_llave = r'\{'
t_fin_llave = r'\}'
t_dotcomma = r'\;'
t_comma = r'\,'




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

def t_id(t):
  r'[a-zA-Z]+([a-zA-Z0-9]*)'
  t.type = reserved.get(t.value, 'id')
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

# Traenis la informacion de un txt
fp = open("SintaxisLenguaje\practica.txt")
data = fp.read()
print(data)
fp.close()


# Give the lexer some input
lexer.input(data)
l_tok=[]
toktok=[]

while True:
	uni_tok=[]
	tok = lexer.token()
	if not tok : break
	print (tok)
	uni_tok.append(tok.type)
	uni_tok.append(tok.value)
	toktok.append(tok.value)
	l_tok.append(uni_tok)
print(l_tok)



    