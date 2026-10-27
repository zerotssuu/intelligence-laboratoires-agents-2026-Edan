# fantomesAgents.py
# -----------------
# Ajout du cours Intelligence artificielle (Labo Pacman) au code de Berkeley.
#
# Le nom de ce fichier doit finir par « Agents.py » : c'est ainsi que pacman.py
# trouve les agents qu'on lui passe avec -g (fantômes) ou -p (Pacman).
#
# Lancer :  python3 pacman.py -g FantomeDuLabo -l smallClassic

import util
from ghostAgents import GhostAgent
from util import manhattanDistance

# Étape 3 : importer votre librairie de machine d'états (son fichier .py copié dans ce répertoire).
# Remplacer machineEtats et MachineEtats par les noms de votre fichier et de votre classe.
# from machineEtats import MachineEtats


class FantomeDuLabo(GhostAgent):
    """Un fantôme de départ : à chaque tour, il choisit une action permise au hasard.
    À vous de le rendre intelligent."""

    def __init__(self, index):
        super().__init__(index)
        self.cheminParcouru = []   # étape 2 : les positions visitées par ce fantôme

    def getDistribution(self, state):
        """Retourne une note par action permise : le jeu tire l'action au hasard selon ces notes."""
        actionsPermises = state.getLegalActions(self.index)
        positionFantome = state.getGhostPosition(self.index)
        positionPacman = state.getPacmanPosition()
        distancePacman = manhattanDistance(positionFantome, positionPacman)

        # TODO étape 2 : afficher en console quand Pacman s'approche (distancePacman)
        # TODO étape 2 : mémoriser positionFantome dans self.cheminParcouru
        # TODO étape 3 : mettre à jour la machine d'états (VUE, SEUL, PROCHE...) et
        #                choisir l'action selon l'état : PROCHE = FUIR, SEUL = au hasard

        distribution = util.Counter()
        for action in actionsPermises:
            distribution[action] = 1.0
        distribution.normalize()
        return distribution
