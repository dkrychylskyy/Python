nom = input("Quel est ton nom ?\n")

# Remarque 1: les valeurs booleennes en Python sont True et False
# Remarque 2: pas de do/while en Python => break pour quitter la boucle
while True:
    age = input("Quel âge as-tu ?\n")

    # Equivalent du try/catch en Java, JavaScript, PHP...
    try:
        age_converti = int(age)
    # Si la valeur saisie n'est pas convertible en entier,
    # une exception de type ValueError est generee
    except ValueError:
        print("La valeur '%s' n'est pas entière, recommence!" % (age))

    break

print("Tu t'appelles {nom} et tu as {age} ans.".format(nom=nom, age=age))