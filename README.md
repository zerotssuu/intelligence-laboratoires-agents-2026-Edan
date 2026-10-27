# 🤖 Laboratoires Agents - L'évolution de l'agent

> **Énoncé complet** : https://intelligence.projet.autos/labo-agents/  
> **Remise : 7 jours après chaque labo** (dates dans le calendrier des rencontres)  
> **Total du module : 10 %** = série noire 3 % + série rouge 4 % + série violette 3 %

| Série | L'agent | Points | Règle |
|---|---|---|---|
| ⬛ Noire | déterministe | 3 % | les 2 labos obligatoires |
| 🟥 Rouge | entraîné | 4 % | 1 labo au choix |
| 🟪 Violette | cognitif | 3 % | obligatoire |

---

## ⬛ SÉRIE NOIRE - L'agent déterministe (3 %, les deux labos obligatoires)

### 🎛️ LABO MACHINES D'ÉTATS (1 %)

#### Partie 1 : Superhéros narcoleptique - Machine d'états avec `transitions`
**Template** : https://github.com/pytransitions/transitions#quickstart  
📁 **Mon notebook Colab** : 🔴 LIEN À REMPLIR

#### Partie 2 : Les états FAIM / BIEN / PEUR - Machine d'états comportementale
**Matrice état-transition** : voir la diapo du cours  
📁 **Mon notebook Colab (avec la librairie, puis avec ma propre classe)** : 🔴 LIEN À REMPLIR

📑 **Mes réponses aux questions :**
- Listez les états ? 🔴 À COMPLÉTER
- Listez les événements ? 🔴 À COMPLÉTER
- Quel événement pourrait-on ajouter ? 🔴 À COMPLÉTER

---

### 👻 LABO PACMAN (2 %)

**Code de départ** : https://intelligence.projet.autos/labo-agents/pacman-depart.zip (le Pacman de Berkeley, `pac3man`, corrigé pour Python 3)  

#### Partie 1 : Reverse engineering du code
📁 **Diagramme UML de l'héritage des agents** : 🔴 LIEN VERS IMAGE GITHUB À REMPLIR

📑 **La responsabilité de chaque classe :**
```
🔴 À COMPLÉTER ICI (une ligne par classe)
```

📑 **La machine d'état qui existe déjà :**
- Les états ? 🔴 À COMPLÉTER
- Les événements ? 🔴 À COMPLÉTER

#### Partie 2 : Mini-modifications réalisées
- [ ] Affichage de la grille légèrement modifié
- [ ] Création des fantômes annulée
- [ ] Fantômes qui tournent toujours à droite
- [ ] Message en console quand Pacman s'approche
- [ ] Chemin parcouru par un fantôme mémorisé
- [ ] Ma propre classe de fantôme, avec sa couleur, instanciée dans le jeu

#### Partie 3 : Ma machine d'état comportementale dans le fantôme
**Ma librairie de machine d'états importée (celle du labo Machines d'états)** : 🔴 LIEN VERS LE FICHIER À REMPLIR  
📁 **Illustration de la machine d'états ou tableau état-transition** : 🔴 LIEN VERS IMAGE GITHUB À REMPLIR

📑 **Les états de mon fantôme et ce qu'il fait dans chacun :**
```
🔴 À COMPLÉTER ICI (par exemple VUE, SEUL = action au hasard, PROCHE = FUIR...)
```

#### Partie 3 : Parsing (FSM)
**Outils** : https://ivanzuzak.info/noam/webapps/fsm_simulator/ , https://madebyevan.com/fsm/ ou https://app.diagrams.net/

📁 **Image de la machine d'états `if(a==b)`** : 🔴 LIEN VERS IMAGE GITHUB À REMPLIR  
📁 **Image de la machine d'états finale (`if(false)`, `if(0)`)** : 🔴 LIEN VERS IMAGE GITHUB À REMPLIR

> **Note :** placez vos images dans votre dépôt GitHub  
> **Option 1 - Lien simple :** `[Voir l'image](chemin/vers/image.png)`  
> **Option 2 - Afficher l'image :** `![Description](chemin/vers/image.png)`

**📑 Explication à ajouter :**
- Comment améliorer le programme en tolérant des espaces ? 🔴 À COMPLÉTER

---

## 🟥 SÉRIE ROUGE - L'agent entraîné (4 %, un labo au choix)

**Mon choix :**
- [ ] 🐦 Sorti du Nid (Hummingbird)
- [ ] 🏛️ Temples Maya
- [ ] ⚽ Équipe Soccer (Hugging Face)

### 🐦 Sorti du Nid
**Formation** : https://learn.unity.com/course/ml-agents-hummingbirds  
**Scène de départ** : HummingbirdScene_1.0.zip (pas le code source : c'est la solution)

📁 **Mon code GitHub (les fichiers .cs, plusieurs commits par module)** : 🔴 LIEN À REMPLIR  
📁 **Le cerveau généré (.onnx ou .nn)** : 🔴 LIEN À REMPLIR  
📁 **Captures d'écran TensorBoard** : 🔴 LIEN À REMPLIR

### 🏛️ Temples Maya
**Cours** : https://github.com/simoninithomas/unity_ml_agents_course

📁 **Cube sauteur de mur : fichier yaml + répertoire results** : 🔴 LIEN À REMPLIR  
📁 **Pyramides (Curious Agent) : fichier yaml + répertoire results** : 🔴 LIEN À REMPLIR  
📁 **Aventure Maya : fichier yaml + répertoire results** : 🔴 LIEN À REMPLIR

### ⚽ Équipe Soccer
**Cours** : https://huggingface.co/learn/deep-rl-course/unit5/introduction

**Mon compte Hugging Face** : 🔴 LIEN À REMPLIR  
📁 **Snowball Target : mon modèle publié sur le Hub** : 🔴 LIEN À REMPLIR  
📁 **Pyramides : mon modèle publié sur le Hub** : 🔴 LIEN À REMPLIR

> **Remise (pour tous les ateliers ML-Agents)** : voir le guide Expérience ML-Agent lié dans l'énoncé.

---

## 🟪 SÉRIE VIOLETTE - L'agent cognitif (3 %)

**Modèle de langage utilisé** : 🔴 À COMPLÉTER (local avec Ollama : quel modèle ? ou API : quel fournisseur ?)  
⚠️ **Aucune clé d'API dans ce dépôt** : variable d'environnement ou fichier ignoré par Git.

### Partie 1 : Les outils (boucle ReAct) - 1 %
📁 **`agent.py` et `prix.txt`** : 🔴 LIEN À REMPLIR  
📁 **Transcription console où l'agent déclenche un outil de lui-même** : 🔴 LIEN À REMPLIR

### Partie 2 : La mémoire (gestion du contexte) - 1 %
📁 **Transcription des 8 tours (budget affiché, résumé visible)** : 🔴 LIEN À REMPLIR

📑 **Que perd-on dans un résumé, et comment le choisir ?**
```
🔴 À COMPLÉTER ICI
```

### Partie 3 : Le harnais (sécurité) - 1 %
📁 **Code du harnais (liste blanche, lecture seule, confirmation)** : 🔴 LIEN À REMPLIR  
📁 **`journal.txt` de l'attaque bloquée (`piege.txt`)** : 🔴 LIEN À REMPLIR

📑 **Quelles permissions, pourquoi, et ce qu'un harnais ne peut pas empêcher :**
```
🔴 À COMPLÉTER ICI
```

---

## 📑 Feuille-synthèse

**N'oubliez pas de compléter la section Agents & États de votre feuille-synthèse avec :**

- [ ] Concepts clés des machines d'états (états, transitions, événements)
- [ ] La machine d'états appliquée à un agent de jeu (le fantôme de Pacman)
- [ ] Concepts clés des ML-Agents (observations, actions, récompenses)
- [ ] Spécificités Unity pour l'IA (Agent, Academy, Behavior Parameters)
- [ ] Processus d'entraînement avec TensorBoard
- [ ] L'agent cognitif : outils (ReAct), gestion du contexte, sécurité du harnais
- [ ] Qui écrit la décision ? Cerveau dessiné, entraîné, cognitif : la comparaison

---

*Mise à jour : [Date] par [Nom]*
