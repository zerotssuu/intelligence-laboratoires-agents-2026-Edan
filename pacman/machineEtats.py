# machineEtats.py
# ---------------
# Ma librairie de machine d'états, écrite au labo Machines d'états (série noire),
# réutilisée telle quelle dans le fantôme du labo Pacman.


class MachineEtats:
    """Machine d'états maison : une table [état][événement] -> nouvel état."""

    def __init__(self, etats, initial):
        if initial not in etats:
            raise ValueError(f"État initial inconnu : {initial}")
        self.etats = list(etats)
        self.etat = initial
        # La matrice état-transition elle-même : une ligne (dictionnaire) par état
        self.table = {etat: {} for etat in self.etats}

    def ajouter_transition(self, evenement, source, destination):
        if source not in self.etats or destination not in self.etats:
            raise ValueError(f"État inconnu dans {source} -> {destination}")
        self.table[source][evenement] = destination

    def declencher(self, evenement):
        """Lit la case (état actuel, événement) et change d'état."""
        nouvel_etat = self.table[self.etat].get(evenement)
        if nouvel_etat is None:
            raise ValueError(f"Aucune transition pour '{evenement}' depuis {self.etat}")
        self.etat = nouvel_etat
        return self.etat

    def forcer_etat(self, etat):
        if etat not in self.etats:
            raise ValueError(f"État inconnu : {etat}")
        self.etat = etat

    def afficher_matrice(self):
        evenements = sorted({e for ligne in self.table.values() for e in ligne})
        print(f"{'':13}" + "".join(f"{e:22}" for e in evenements))
        for etat, ligne in self.table.items():
            cases = "".join(f"{ligne.get(e, '-'):22}" for e in evenements)
            print(f"{etat:13}{cases}")
