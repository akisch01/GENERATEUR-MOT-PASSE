import random
import string

def generate_password(length, complexity):
    if complexity == "simple":
        characters = string.ascii_letters
    elif complexity == "intermediate":
        characters = string.ascii_letters + string.digits
    else:  # complex
        characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        length = int(input("Entrez la longueur du mot de passe : "))
        complexity = input("Choisissez la complexité (simple, intermediate, complex) : ")
        
        if complexity not in ["simple", "intermediate", "complex"]:
            print("Complexité invalide, veuillez choisir 'simple', 'intermediate', ou 'complex'.")
            continue
        
        password = generate_password(length, complexity)
        print(f"Votre mot de passe généré est : {password}")
        
        while True:
            choice = input("Voulez-vous générer un autre mot de passe ? (oui/non) : ").lower()
            if choice == "oui":
                break
            elif choice == "non":
                print("Merci d'utiliser notre générateur de mots de passe. À bientôt !")
                return
            else:
                print("Choix invalide, veuillez répondre par 'oui' ou 'non'.")

# Lancer le programme
main()

