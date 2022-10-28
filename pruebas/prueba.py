import ply.lex as lex

reservadas = ['FUNC_CUERPO','LIF','LNO','LWHILX','LPARA','LLADRA','RETORN', 'INT', 'DEC', 'VOID', 'Y', 'O',
              'LMAYOR','LMENOR','LHASTA','PASOS','IMPRIMIR'
		]

tokens = reservadas+['IDENTIFICADOR','INT', 'MAS','MIN','POR','DIV','MAYORIGUAL','MENORIGUAL',
                'PREMULTIPLICACION','PREDIVISION','MODULO', 'IGUAL','MENOR','MAYOR',
		'PARIZQ', 'PARDER', 'LLAVEIZQ','LLAVEDER', 'COMA', 'PUNTOCOMA', 'DOSPUNTOS',
                'COMILLAS', 'COMENTARIO', 'INCREMENTO', 'DECREMENTO', 'COMPARCION', 'DIFERENTE', 'STRING', 'FLOAT'
		]

t_ignore = '\t '
t_MAS = r'\+'
t_MIN = r'\-'
t_POR = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_IGUAL = r'='
t_MAYORIGUAL = r'\+='
t_MENORIGUAL = r'\-='
t_PREMULTIPLICACION = r'\*='
t_PREDIVISION = r'\/='
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_COMA = r','
t_PUNTOCOMA = r';'
t_DOSPUNTOS = r':'
t_COMILLAS = r'"'
t_COMENTARIO = r'\->'
t_INCREMENTO = r'\++'
t_DECREMENTO = r'\--'
t_COMPARCION = r'\:\)'
t_DIFERENTE = r'\:\('


def t_IDENTIFICADOR(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):
	r'\#.*'
	pass

def t_INT(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print ("caracter ilegal no declarado'%s'" % t.value[0])
	t.lexer.skip(1)

def t_PRINT(t):
        r'print'
        t.value=str(t.value)
        return t


fp = open("pruebas\ejem3.txt")
cadena = fp.read()
print(cadena)
fp.close()

analizador = lex.lex()

analizador.input(cadena)
l_tok=[]
toktok=[]

while True:
	uni_tok=[]
	tok = analizador.token()
	if not tok : break
	print (tok)
	uni_tok.append(tok.type)
	uni_tok.append(tok.value)
	toktok.append(tok.value)
	l_tok.append(uni_tok)
print(l_tok)