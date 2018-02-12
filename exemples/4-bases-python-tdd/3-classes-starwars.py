class ForceSensitive:
    capacites_base = ["soulever des objets"]
    nb_instances = 0

    def __init__(self, nom, capacites=[]):
        self.nom = nom
        self.capacites = self.capacites_base + capacites
        ForceSensitive.nb_instances += 1

    def nb_capacites(self):
        return len(self.capacites)

    def __str__(self):
        return "Je suis {nom} ({genre}) et j'ai {nb} capacités :\n  - {capacites}\n".format(
            nom=self.nom, genre=type(self).__name__, nb=self.nb_capacites(), capacites="\n  - ".join(self.capacites)
        )

class Jedi(ForceSensitive):
    capacites_base = [
        "soulever des objets",
        "combattre au sabre laser",
        "influencer les esprits"
    ]

class JediBadass(ForceSensitive):
    capacites_base = [
        "soulever des objets",
        "combattre au sabre laser",
        "influencer les esprits",
        "réapparaître comme fantôme"
    ]

class Sith(ForceSensitive):
    capacites_base = [
        "soulever des objets",
        "combattre au sabre laser",
        "envoyer des éclairs"
    ]

leia = ForceSensitive("Leia", ["jouer à Mary Poppins"])
rey = Jedi("Rey", ["à peu près tout faire en fait"])
luke = Jedi("Luke", ["lancer un sabre avec classe", "entrer en lévitation"])
obiwan = JediBadass("Obiwan", ["balancer des punchlines de ouf"])
empereur = Sith("L'Empereur", ["dissimuler la Force", "manipuler et trahir"])
snoke = ForceSensitive("Snoke", [ "envoyer des éclairs", "troller mes subordonnés","skyper par télépathie"])

print("\nIl y a {nb_force_sensitives} ForceSensitive en circulation.\n".format(
    nb_force_sensitives=ForceSensitive.nb_instances
))
for personnage in [leia, rey, luke, obiwan, empereur, snoke]:
    print(personnage)