# Labo Pacman : le code de départ

Le Pacman conçu par l'université de Berkeley (UC Berkeley, cours CS188) pour enseigner l'intelligence
artificielle, dans sa version Python 3 ([jspacco/pac3man](https://github.com/jspacco/pac3man), dossier
`multiagent`, commit bf603da). On y améliore l'intelligence des fantômes ou de Pacman avec une machine
d'états.

## Ce qui change par rapport au dépôt d'origine

- Seul le dossier `multiagent` est gardé. L'autograder du projet Minimax de Berkeley est retiré : il ne sert
  pas à ce labo et il ne démarre plus depuis Python 3.12 (il importe le module `imp`, supprimé).
- `game.py` : 6 lignes `print >>sys.stderr, ...` (syntaxe Python 2, qui plantait au moment d'afficher
  l'erreur) sont corrigées en `print(..., file=sys.stderr)`.
- `graphicsDisplay.py` : `GHOST_VEC_COLORS` est une vraie liste (en Python 3, `map()` ne se découpe pas).
- `pacman.py` : quand un fichier `...Agents.py` ne s'importe pas, l'erreur est **affichée** au lieu d'être
  ignorée en silence.
- Ajouts : ce `README.md` et le squelette `fantomesAgents.py`. Le README d'origine de Berkeley est gardé
  sous le nom `README-berkeley-projet-multiagent.md`.

## Installer

1. Python 3.8 ou plus (testé avec Python 3.11). Vérifier : `python3 --version` (sous Windows : `python --version`).
2. Tkinter, la librairie graphique :
   - Windows et macOS : elle est incluse avec l'installateur de python.org, rien à faire.
   - Linux (Debian, Ubuntu) : `sudo apt install python3-tk`
   - Vérifier : `python3 -c "import tkinter"` ne doit rien afficher.
   - Attention : `pip install tk` n'installe **pas** Tkinter (c'est un autre paquet qui porte ce nom).
3. Décompresser le zip, puis dans un terminal : `cd pacman-depart`

## Lancer

| Commande | Ce qu'elle fait |
|---|---|
| `python3 pacman.py` | Une partie au clavier (touches W A S D ou les flèches) |
| `python3 pacman.py -l smallClassic` | Une autre grille (voir le dossier `layouts/`) |
| `python3 pacman.py -k 1` | Seulement 1 fantôme (`-k 0` : aucun fantôme) |
| `python3 pacman.py -g DirectionalGhost` | Des fantômes qui poursuivent Pacman au lieu d'errer au hasard |
| `python3 pacman.py -g FantomeDuLabo` | **Vos** fantômes, définis dans `fantomesAgents.py` |
| `python3 pacman.py -p ReflexAgent` | Pacman joue seul avec l'agent réflexe de `multiAgents.py` |
| `python3 pacman.py --frameTime 0.2` | Ralentir le jeu (0 = le plus vite possible) |
| `python3 pacman.py -z 0.7` | Réduire (ou agrandir) la fenêtre |
| `python3 pacman.py -t` | Affichage en texte dans le terminal, sans fenêtre |
| `python3 pacman.py -h` | Toutes les options |

Grilles disponibles : `capsuleClassic`, `contestClassic`, `mediumClassic` (par défaut), `minimaxClassic`,
`openClassic`, `originalClassic`, `smallClassic`, `testClassic`, `trappedClassic`, `trickyClassic`.

## Les fichiers

| Fichier | Rôle général |
|---|---|
| `pacman.py` | Le point d'entrée : les options de lancement et les règles du jeu (Pacman, fantômes) |
| `game.py` | Le moteur : agents, directions, positions, grille, déroulement d'une partie |
| `ghostAgents.py` | Les fantômes fournis par Berkeley |
| `pacmanAgents.py`, `keyboardAgents.py`, `multiAgents.py` | Les Pacman fournis (automatiques, au clavier, du projet Berkeley) |
| `fantomesAgents.py` | **Ajout du cours** : le squelette de votre fantôme |
| `graphicsDisplay.py`, `graphicsUtils.py` | L'affichage graphique (Tkinter) |
| `textDisplay.py` | L'affichage en texte |
| `layout.py`, `layouts/*.lay` | La lecture des grilles et les grilles elles-mêmes (des fichiers texte) |
| `util.py` | Outils communs : distances, files, distributions de probabilités |

Le détail des classes, de leur héritage et de leurs responsabilités, c'est justement la première étape du
labo : à vous de le dessiner.

## Où chercher pour les mini-modifications

Des pistes, pas des solutions :

| Mini-modification | Où chercher |
|---|---|
| Modifier l'affichage de la grille | Les constantes de couleur en haut de `graphicsDisplay.py`, ou une grille de `layouts/` (`%` = mur, `.` = nourriture, `o` = capsule, `P` = Pacman, `G` = fantôme) |
| Annuler la création des fantômes | L'option `-k` dans `pacman.py`, puis l'endroit où la liste des fantômes est construite |
| Fantômes qui tournent toujours à droite | La classe `Directions` de `game.py` (`LEFT`, `RIGHT`, `REVERSE`) et `getLegalActions` des fantômes dans `pacman.py` : un fantôme ne peut ni s'arrêter ni faire demi-tour |
| Afficher en console quand Pacman s'approche | Dans votre fantôme : `state.getPacmanPosition()`, `state.getGhostPosition(self.index)` et `util.manhattanDistance(a, b)` |
| Mémoriser le chemin d'un fantôme | Un attribut de liste dans votre classe de fantôme (le squelette en prévoit un) |
| Votre fantôme avec sa propre couleur | `GHOST_COLORS` et `getGhostColor` dans `graphicsDisplay.py` : la couleur dépend du **numéro** du fantôme, pas de sa classe. À vous de trouver comment la relier à votre classe |

## Votre fantôme et votre machine d'états

1. Ouvrir `fantomesAgents.py` : la classe `FantomeDuLabo` est un fantôme qui choisit une action permise au
   hasard. Lancer `python3 pacman.py -g FantomeDuLabo -l smallClassic` pour la voir jouer.
2. **Piège à connaître** : `pacman.py` cherche les agents passés avec `-g` ou `-p` seulement dans les
   fichiers dont le nom finit par `Agents.py`. Un fantôme écrit dans `monFantome.py` reste introuvable.
3. Pour la machine d'états : copier le fichier `.py` de votre librairie (celle du labo Machines d'états)
   dans ce répertoire, puis l'importer en haut de `fantomesAgents.py` (la ligne est prête, en commentaire).
   Si l'import échoue, le message `ATTENTION : impossible d'importer ...` dit maintenant pourquoi.
4. Informations utiles pour les transitions (dans `getDistribution(self, state)`) :

| Pour savoir... | Écrire |
|---|---|
| Les actions permises au fantôme | `state.getLegalActions(self.index)` |
| La position du fantôme | `state.getGhostPosition(self.index)` |
| La position de Pacman | `state.getPacmanPosition()` |
| La distance entre deux positions | `util.manhattanDistance(positionA, positionB)` |
| Les positions de tous les fantômes | `state.getGhostPositions()` |
| Si le fantôme est effrayé (Pacman a mangé une capsule) | `state.getGhostState(self.index).scaredTimer > 0` |

`getDistribution` retourne un `util.Counter` : une note pour chaque action permise (plus la note est haute,
plus l'action a de chances d'être choisie). Une seule action à 1 et les autres absentes : le fantôme la
choisit à coup sûr.

## Licence et attribution

The Pacman AI projects were developed at UC Berkeley (http://ai.berkeley.edu). La notice de licence est
conservée en tête de chaque fichier d'origine. Ce code de départ ne contient aucune solution des projets de
Berkeley.
