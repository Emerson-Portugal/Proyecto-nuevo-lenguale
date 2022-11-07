import LL1
import Lexico

# debe imprimir nuestras varibles

### -------------- Primera tarea --------- Buscar varibales creadas--------
def buscarVariables(root):
    #print(root.symbol.symbol)
    #hijo = root.children[0]
    for hijo in root.children:
        if hijo.symbol.symbol == "TYPE":
            node_hermano = hijo.father.children[1] 
            print("varible creada", node_hermano.lexeme)
        buscarVariables(hijo)


if __name__ == "__main__":
    prueba = open("ProyectoParcial\practica.txt")
    tokens = Lexico.get_tokens(prueba)
    tokens.append(['$', None, None])

    root, node_list = LL1.principal(tokens)
    buscarVariables(root)


