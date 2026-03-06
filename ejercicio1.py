# Ejercicio 1

# Escribe un script que haga lo siguiente: dado un texto tamaño N, deberá
# decir las veces que ese texto aparece en un párrafo de tamaño M.
# Ejemplo:
# Parrafo: "La logística Digital es un concepto que surge de la integración
# entre la logística tradicional y la era digital.
# Con el auge del correo electrónico y las descargas digitales reemplazando
# productos físicos, podríamos estar hablando de un golpe devastador para la
# industria de la logística, pero, de hecho, ha ocurrido algo muy diferente.
# El sector de la logística ha introducido las innovaciones digitales."

# texto: “logística”
# Salida: “4 ocurrencias encontradas”

PARRAFO = """La logística Digital es un concepto que surge de la integración
entre la logística tradicional y la era digital.
Con el auge del correo electrónico y las descargas digitales reemplazando
productos físicos, podríamos estar hablando de un golpe devastador para la
industria de la logística, pero, de hecho, ha ocurrido algo muy diferente.
El sector de la logística ha introducido las innovaciones digitales."""

text = "Digital"


class Solution:
    def __init__(self):
        pass

    # Method to transform a string in a list of characters
    def text_to_list(self, text: str) -> list:
        text_list = list()
        i = 0
        while i < len(text):
            # If the text has accents, return the character without them.
            character = self.normalize_accents(text[i])

            # If the text has upper characters get it in lower
            character = self.normalize_upper(text[i])

            text_list.append(character)
            i += 1
        return text_list

    # Method to detect if a character is an alphanumeric
    def is_alphanumeric(self, character: str) -> bool:
        if (
            (character >= "A" and character <= "Z")
                or (character >= "a" and character <= "z")
                or (character >= "0" and character <= "9")):
            return True
        return False

    # Method to detect accents and return the character without it
    def normalize_accents(self, character: str) -> str:
        if character == "á" or character == "Á":
            return "a"
        if character == "é" or character == "É":
            return "e"
        if character == "í" or character == "Í":
            return "i"
        if character == "ó" or character == "Ó":
            return "o"
        if character == "ú" or character == "Ú":
            return "u"
        if character == "ü" or character == "Ü":
            return "u"
        if character == "ñ" or character == "Ñ":
            return "n"
        return character

    # Method to detect an upper character and return it in lower version
    def normalize_upper(self, character: str) -> str:
        # Get the ascii value of character to use it like numbers
        assci_value = ord(character)

        # The 65 and 90, represents A and Z values in ASCII table
        if 65 <= assci_value <= 90:
            # return the ascci_value adding 32, because is the same
            # charaacter but in lower
            return chr(assci_value + 32)
        return character


if __name__ == "__main__":
    solution = Solution()

    # Transform string in a list of chars
    text_list = solution.text_to_list(text=text)

    seen = 0
    comparation = []

    # Loop through PARRAFO
    i = 0
    while i < len(PARRAFO):
        # Each loop through in string is a character, so save it
        # and remove the accents in case the character has one
        character = solution.normalize_accents(PARRAFO[i])

        # For each character normalize the upper and return it in lower
        character = solution.normalize_upper(PARRAFO[i])

        # if character is not a blank space and is an alpahnumeric character,
        # can add it to comparation list unitl found one
        if character != " " and solution.is_alphanumeric(character):
            comparation.append(character)
        else:
            # if found a blank space or non alpahnumeric characher we have a
            # word in a comparation list, so do a comaration with our text_list
            if comparation == text_list:
                seen += 1

            # clear the comparation list after each word
            comparation = list()
        i += 1

    print(f"{seen} ocurrencias encontradas")
