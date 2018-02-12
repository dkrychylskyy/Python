# Renvoie la date passée en paramètre, augmentée d'un mois
def meme_jour_mois_prochain(date):

	# Découpe la chaîne et renvoie une liste
	# (équivalent des tableaux en Java, JS...)
	jour_mois_annee = date.split('/')

	# On devrait avoir 3 éléments exactement
	if len(jour_mois_annee) != 3:
		raise ValueError("La date attendue est au format JJ/MM/AAAA\n")

	# On tente de convertir les éléments en entiers
	try:
		jour = int(jour_mois_annee[0])
		mois = int(jour_mois_annee[1])
		annee = int(jour_mois_annee[2])

		if mois == 12:
			annee += 1
			mois = 1
		else:
			mois += 1

		return "{:02d}/{:02d}/{:04d}".format(jour, mois, annee)

	except ValueError:
		raise ValueError("La date attendue est au format JJ/MM/AAAA\n")

# Verifie que ça marche
print(meme_jour_mois_prochain("12/02/2018"))
print(meme_jour_mois_prochain("27/12/2018"))
print(meme_jour_mois_prochain("27/toto/2018"))
