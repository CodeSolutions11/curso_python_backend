
## TODO: El ámbito de las variables - (Scope)
# ? El ámbito determina dónde una variable puede ser accedida en el código

# Built-in scope - funciones integradas de Python
#print(len([1, 2, 3]))

# Variable global - global scope
variable_global = "Soy global"

def funcionExterna():
    # Enclosing scope
    variable_enclosing = "Soy enclosing"

    def funcionInterna():
        # Local scope
        variable_local = "Soy local"

        print(variable_local)
        print(variable_enclosing)
        print(variable_global)
        print(len)

    funcionInterna()


funcionExterna()
#! print(variable_enclosing) #! ERROR