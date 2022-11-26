variable_ar = []
variable_sub = []
def inicioD(): #inicio del assembly
    file = open("ProyectoParcial/variables.txt", "a")
    file.write(".data\n")
    file.close()


def inicioT(): #inicio del assembly
    file = open("ProyectoParcial/variables.txt", "a")
    file.write(".text\n")
    file.close()

def crearMain(): #main del assembly
    file = open("ProyectoParcial/variables.txt", "a")
    file.write("\nmain:\n")
    file.close()

def fin(): #fin del assembly
    file = open("ProyectoParcial/variables.txt", "a")
    file.write("\n\njr $ra")
    file.close()

def inicializarVar(variable):
    inicioD()
    valor_res = variable[::-1]
    for i in range(len(valor_res)):
        file = open("ProyectoParcial/variables.txt", "a")
        file.write("var_"+ str(valor_res[i])+":    "".word      ""0:1" + "\n")
        file.close()
    inicioT()
    crearMain()

# print(signo)
# print(valor)
# print(variable.lexeme)

def convertir(variable, signo, valor):
    file = open("ProyectoParcial/variables.txt", "a")
    valor_res = valor[::-1]
    signo_res = signo[::-1]
    index = len(signo_res)
    index_signo = 0
    variable_ar.append(variable)

    if len(signo_res) > 0:
            for j in range(len(valor_res)):
                if j == 0:
                        if valor_res[j] == variable_ar[0].lexeme: 
                            file.write("\n\nla   $t0," + "   var_"+variable_ar[0].lexeme)
                            file.write("\nlw  " + "$a0," + "  0($t0)")
                        else:
                            file.write("\nli $a0,    "  + str(valor_res[j]) + "\n") 
                if  j >= 1:

                    if valor_res[j] == variable_ar[0].lexeme: 
                        file.write("\n\nsw  " + "$a0,  " + "0($sp)")
                        file.write("\naddiu  " + "$sp,  " + "$sp,  " + "-4" + "\n")
                        file.write("\n\nla $t0, var_"+variable_ar[0].lexeme +"\nlw $a0, 0($t0)")
                    else:
                        file.write("\n\nsw  " + "$a0,  " + "0($sp)")
                        file.write("\naddiu  " + "$sp,  " + "$sp,  " + "-4" + "\n")
                        file.write("\nli $a0,   "  + str(valor_res[j]) + "\n")
                        
                    if index_signo < index:
                        if signo_res[index_signo] == "+":
                            file.write("\nlw   " + "$t1,   "  + "4($sp) \n")
                            file.write("add  " + "$a0,  "   "$a0,  " + "$t1 \n")
                            file.write("\naddiu  "  + "$sp  "+ "$sp  " + "4")
                            index_signo += 1

            file.write("\n\nla   " +"$t0,  " + "var_"+variable.lexeme)
            file.write("\nsw  " +"$a0,  "+ "0($t0)")
            file.write("\n\nli $v0, 1")
            file.write("\nsyscall")
            file.write("\n\njr $ra ")
            file.close()

    else:  
        file.write("\nli $a0,    "  + str(valor_res[0]) + "\n") 
        file.write("\nla   $t0," + "   var_"+variable.lexeme)
        file.write("\nsw  " + "$a0," + "  0($t0)")
        file.close()