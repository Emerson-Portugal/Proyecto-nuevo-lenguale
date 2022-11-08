import LL1
import Lexico

# debe imprimir nuestras varibles

### -------------- Primera tarea --------- Buscar varibales creadas--------


def buscarVariables(root):



    # if root.symbol.symbol == "id":
    #     node_hermano = root.father.children[0] 
    #     print("Usansdo ID", node_hermano.lexeme)

## ------------recorremos ---- para encontrar FUNCTION--------------
    # if root.symbol.symbol == "FUNCTION":
    #     tercer_hijo = root.children[1]
    #     gbl_nombre_function = tercer_hijo.lexeme
    #     print("Funcion", gbl_nombre_function)

    if root.symbol.symbol == "TYPE":
        node_hermano1 = root.father.children[1]
        

        if node_hermano1.symbol.symbol == "id":
            print("varible creada", node_hermano1.lexeme)
        
        else:
            node_hermano2 = node_hermano1.father.children[1]
            print("varibale usada", node_hermano2.lexeme)



    for child in root.children:
        buscarVariables(child)



if __name__ == "__main__":
    prueba = open("ProyectoParcial\practica.txt")
    tokens = Lexico.get_tokens(prueba)
    tokens.append(['$', None, None])

    root, node_list = LL1.principal(tokens)
    buscarVariables(root)


