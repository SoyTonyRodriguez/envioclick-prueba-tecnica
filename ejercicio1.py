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

text = "Digitales"


class Solution:
    # Class constructor.
    def __init__(self):
        pass

    # Convert a text string into a list of normalized characters.
    # During the process, accents are removed and uppercase letters
    # are converted to lowercase to ensure consistent comparisons.
    def text_to_list(self, text: str) -> list:
        text_list = list()

        # Iterate through the text character by character.
        i = 0
        while i < len(text):
            # Normalize the character if it contains an accent.
            character = self.normalize_accents(text[i])

            # Convert the character to lowercase if it is uppercase.
            character = self.normalize_upper(character)

            # Append the normalized character to the resulting list.
            text_list.append(character)
            i += 1
        return text_list

    # Determine whether a character is alphanumeric.
    # A character is considered valid if it is a letter (A-Z, a-z)
    # or a digit (0-9).
    def is_alphanumeric(self, character: str) -> bool:
        if (
            (character >= "A" and character <= "Z")
                or (character >= "a" and character <= "z")
                or (character >= "0" and character <= "9")):
            return True
        return False

    # Replace accented characters with their non-accented equivalents.
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

        # If the character does not contain an accent, return it unchanged.
        return character

    # Convert uppercase characters to lowercase using ASCII values.
    def normalize_upper(self, character: str) -> str:
        # Obtain the ASCII value of the character.
        assci_value = ord(character)

        # ASCII values 65–90 correspond to uppercase letters (A–Z).
        if 65 <= assci_value <= 90:
            # Adding 32 converts the character to its lowercase equivalent.
            return chr(assci_value + 32)
        return character


if __name__ == "__main__":
    # Create an instance of the solution class.
    solution = Solution()

    # Convert the search text into a list of normalized characters.
    text_list = solution.text_to_list(text=text)

    # Counter for the number of occurrences found.
    seen = 0

    # Temporary buffer used to store the characters of the current
    # word being evaluated in the paragraph.
    current_word = list()

    # Iterate through the paragraph character by character.
    i = 0
    while i < len(PARRAFO):
        # Normalize the current character by removing accents.
        character = solution.normalize_accents(PARRAFO[i])

        # Convert the character to lowercase if necessary.
        character = solution.normalize_upper(character)

        # If the character is alphanumeric and not a space,
        # it is considered part of a word.
        if character != " " and solution.is_alphanumeric(character):
            # If a space or non-alphanumeric character is found,
            # the current word has finished.
            current_word.append(character)
        else:
            # Compare the detected word with the target text.
            if current_word == text_list:
                seen += 1

            # Reset the buffer to start building the next word.
            current_word = list()
        i += 1

    # Handle the case where the paragraph ends with a word
    # and no separator character appears afterwards.
    if current_word == text_list:
        seen += 1

    print(f"{seen} ocurrencias encontradas")
