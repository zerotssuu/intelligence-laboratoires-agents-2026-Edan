# fantomesAgents.py
# -----------------
# Ajout du cours Intelligence artificielle (Labo Pacman) au code de Berkeley.
#
# Le nom de ce fichier doit finir par « Agents.py » : c'est ainsi que pacman.py
# trouve les agents qu'on lui passe avec -g (fantômes) ou -p (Pacman).
#
# Lancer :  python3 pacman.py -g FantomeDuLabo -l smallClassic

import util
from game import Actions
from ghostAgents import GhostAgent
from util import manhattanDistance

# Étape 3 : ma librairie de machine d'états (labo Machines d'états, série noire)
from machineEtats import MachineEtats


# Réglages du comportement
DISTANCE_PROCHE = 3      # en cases (distance de Manhattan) : en dessous, Pacman est PROCHE
PROB_PREFERENCE = 0.8    # VUE et VUE_PEUR : probabilité de prendre la meilleure direction
AFFICHER_ETATS = True    # afficher en console chaque changement d'état


class FantomeDuLabo(GhostAgent):
    """Un fantôme guidé par une machine d'états doublée :
    mode NORMAL (SEUL, VUE, PROCHE) et mode PEUR (SEUL_PEUR, VUE_PEUR, PROCHE_PEUR)."""

    # Mini-modif 6 : la couleur propre à ce fantôme (rose fuchsia)
    COULEUR = (1.0, 0.0, 0.8)

    ETATS = ['SEUL', 'VUE', 'PROCHE', 'SEUL_PEUR', 'VUE_PEUR', 'PROCHE_PEUR']

    def __init__(self, index):
        super().__init__(index)
        self.cheminParcouru = []   # étape 2 : les positions visitées par ce fantôme
        # L'affichage choisit la couleur d'un fantôme selon son index dans GHOST_COLORS :
        # on remplace la couleur de notre index par la nôtre.
        try:
            import graphicsDisplay
            graphicsDisplay.GHOST_COLORS[index] = graphicsDisplay.formatColor(*FantomeDuLabo.COULEUR)
        except ImportError:
            pass   # pas d'affichage graphique (mode -q ou -t)

        # Étape 3 : la machine d'états du fantôme
        self.machine = FantomeDuLabo.construireMachine()
        self.avaitPeur = False

    # ------------------------------------------------------------------
    # La machine d'états : exactement la matrice état-transition du README
    # ------------------------------------------------------------------
    @staticmethod
    def construireMachine():
        machine = MachineEtats(FantomeDuLabo.ETATS, initial='SEUL')
        situations = {'pacman_hors_vue': 'SEUL', 'pacman_en_vue': 'VUE', 'pacman_proche': 'PROCHE'}
        for normal in ['SEUL', 'VUE', 'PROCHE']:
            peur = normal + '_PEUR'
            # La situation change : on reste dans la même moitié de la machine
            for evenement, destination in situations.items():
                machine.ajouter_transition(evenement, normal, destination)
                machine.ajouter_transition(evenement, peur, destination + '_PEUR')
            # La peur change : on passe à l'autre moitié en gardant la situation
            machine.ajouter_transition('capsule_mangee', normal, peur)
            machine.ajouter_transition('capsule_mangee', peur, peur)
            machine.ajouter_transition('peur_finie', normal, normal)
            machine.ajouter_transition('peur_finie', peur, normal)
        return machine

    def registerInitialState(self, state):
        # Appelé par Game.run() au début de chaque partie
        super().registerInitialState(state)
        self.machine.forcer_etat('SEUL')
        self.avaitPeur = False

    # ------------------------------------------------------------------
    # Les capteurs : transformer le GameState en événements
    # ------------------------------------------------------------------
    @staticmethod
    def arrondir(position):
        return (int(position[0] + 0.5), int(position[1] + 0.5))

    @staticmethod
    def estEnVue(positionFantome, positionPacman, murs):
        """Vrai si Pacman est sur la même ligne ou la même colonne, sans mur entre les deux."""
        fx, fy = FantomeDuLabo.arrondir(positionFantome)
        px, py = FantomeDuLabo.arrondir(positionPacman)
        if fy == py:
            return not any(murs[x][fy] for x in range(min(fx, px) + 1, max(fx, px)))
        if fx == px:
            return not any(murs[fx][y] for y in range(min(fy, py) + 1, max(fy, py)))
        return False

    def mettreAJourMachine(self, state):
        etatAvant = self.machine.etat

        # 1. La peur (capsule mangée ou peur terminée)
        aPeur = state.getGhostState(self.index).scaredTimer > 0
        if aPeur and not self.avaitPeur:
            self.machine.declencher('capsule_mangee')
        elif not aPeur and self.avaitPeur:
            self.machine.declencher('peur_finie')
        self.avaitPeur = aPeur

        # 2. La situation, par ordre de priorité : proche, puis en vue, puis hors de vue
        positionFantome = state.getGhostPosition(self.index)
        positionPacman = state.getPacmanPosition()
        if manhattanDistance(positionFantome, positionPacman) <= DISTANCE_PROCHE:
            self.machine.declencher('pacman_proche')
        elif FantomeDuLabo.estEnVue(positionFantome, positionPacman, state.getWalls()):
            self.machine.declencher('pacman_en_vue')
        else:
            self.machine.declencher('pacman_hors_vue')

        if AFFICHER_ETATS and self.machine.etat != etatAvant:
            print("Fantôme %d : %s -> %s" % (self.index, etatAvant, self.machine.etat))

    # ------------------------------------------------------------------
    # Les actions : une distribution de probabilités selon l'état
    # ------------------------------------------------------------------
    def distributionSelonDistance(self, state, actionsPermises, plusLoin, probMeilleure):
        """Donne probMeilleure aux actions qui rapprochent le plus (ou éloignent le plus si
        plusLoin) de Pacman, et répartit le reste entre toutes les actions permises."""
        vitesse = 0.5 if state.getGhostState(self.index).scaredTimer > 0 else 1.0
        x, y = state.getGhostPosition(self.index)
        positionPacman = state.getPacmanPosition()
        distances = []
        for action in actionsPermises:
            dx, dy = Actions.directionToVector(action, vitesse)
            distances.append(manhattanDistance((x + dx, y + dy), positionPacman))
        meilleure = max(distances) if plusLoin else min(distances)
        meilleuresActions = [a for a, d in zip(actionsPermises, distances) if d == meilleure]

        distribution = util.Counter()
        for action in meilleuresActions:
            distribution[action] += probMeilleure / len(meilleuresActions)
        for action in actionsPermises:
            distribution[action] += (1 - probMeilleure) / len(actionsPermises)
        distribution.normalize()
        return distribution

    def getDistribution(self, state):
        """Retourne une note par action permise : le jeu tire l'action au hasard selon ces notes."""
        actionsPermises = state.getLegalActions(self.index)
        distribution = util.Counter()
        if len(actionsPermises) == 0:
            return distribution

        self.cheminParcouru.append(state.getGhostPosition(self.index))
        self.mettreAJourMachine(state)
        etat = self.machine.etat

        if etat in ('SEUL', 'SEUL_PEUR'):      # au hasard
            for action in actionsPermises:
                distribution[action] = 1.0
            distribution.normalize()
            return distribution
        if etat == 'VUE':                       # poursuivre
            return self.distributionSelonDistance(state, actionsPermises, False, PROB_PREFERENCE)
        if etat == 'PROCHE':                    # ATTAQUER
            return self.distributionSelonDistance(state, actionsPermises, False, 1.0)
        if etat == 'VUE_PEUR':                  # s'éloigner
            return self.distributionSelonDistance(state, actionsPermises, True, PROB_PREFERENCE)
        return self.distributionSelonDistance(state, actionsPermises, True, 1.0)   # PROCHE_PEUR : FUIR
