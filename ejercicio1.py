# Ejercicio 1

# Escribe un script que haga lo siguiente: dado un texto tamaño N, deberá decir las veces que ese texto aparece en un
# párrafo de tamaño M.
# Ejemplo:
# Parrafo: “La logística Digital es un concepto que surge de la integración entre la logística tradicional y la era digital.
# Con el auge del correo electrónico y las descargas digitales reemplazando productos físicos, podríamos estar
# hablando de un golpe devastador para la industria de la logística, pero, de hecho, ha ocurrido algo muy diferente. El
# sector de la logística ha introducido las innovaciones digitales.”
# texto: “logística”
# Salida: “4 ocurrencias encontradas”

PARRAFO = """La logística Digital es un concepto que surge de la integración entre la logística tradicional y la era digital.
Con el auge del correo electrónico y las descargas digitales reemplazando productos físicos, podríamos estar
hablando de un golpe devastador para la industria de la logística, pero, de hecho, ha ocurrido algo muy diferente. El
sector de la logística ha introducido las innovaciones digitales."""

text = "logística"

class Solution():
    def __init__(self):
        pass

    # Method to transform a string in a list of characters
    def text_to_list(self, text: str) -> list:
        text_list = list()
        i = 0
        while i < len(text):
            text_list.append(text[i])
            i += 1
        return text_list


if __name__ == "__main__":
    solution = Solution()
    
    # Transform string in a list of chars
    text_list = solution.text_to_list(text=text)
    print(text_list)
    
    seen = 0
    comparation = []
    
    # Loop through PARRAFO
    i = 0
    while i < len(PARRAFO):
        # Each loop through in string is a character, so save it
        character = PARRAFO[i]
        
        # if character is not a blank space, can add it to comparation list unitl found one
        if character != ' ':
            comparation.append(character)
        else:
            # if found a blank space we have a word in a comparation list, so comparte this with our text_list
            print(f"comparting {comparation} == {text_list} --> {comparation == text_list}")
            if comparation == text_list:
                seen += 1

            # clear the comparation list after each word
            comparation = list()
        i += 1
        

print(f"{seen} ocurrencias encontradas")