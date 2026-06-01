print ("Bienvenue dans le décodeur de messages secrets !")
print ("Veuillez entrer le message codé que vous souhaitez décoder :")
message_a_decoder = input()

def ASCII_converter (message_a_decoder):
    for caractere in message_a_decoder: # boucle qui parcourt chaque caractère du message à décoder       
        code_to_ASCII = ord(caractere)  # Convertit le caractère en son code ASCII
        # ASCII_to_code = chr(code_to_ASCII) # Convertit le code ASCII en caractère
        caracactere_valeur = {caractere: code_to_ASCII} # crée un dictionnaire avec le caractère et sa valeur ASCII
        # valeur_caractere = {code_to_ASCII: caractere} # crée un dictionnaire avec la valeur ASCII et le caractère correspondant
        print(caracactere_valeur) # affiche le dictionnaire pour chaque caractère
        # print(valeur_caractere) # affiche le dictionnaire pour chaque code ASCII
