# 📑 Cahier des Charges : Projet "La Boîte à Outils Secrète"

Ce document définit les spécifications, la structure et la méthodologie de travail pour le développement de l'application de chiffrement et déchiffrement de messages (variante du Code César).

## 1. Objectifs du Projet

* Développer une application en ligne de commande (CLI) permettant de chiffrer et   déchiffrer des messages textuels.

* Mettre en pratique la gestion des versions avec Git, le travail en branches collaboratives et la résolution de fusions (merges).

## 2. Architecture du Projet & Workflow Git

Le projet suivra une structure modulaire où chaque développeur travaille de manière isolée avant la phase de synchronisation finale.

### 📁 Structure finale attendue du dépôt

```
boite-a-outils-secrete/

│
├── encodeur.py      # Développé par le Développeur A
├── decodeur.py      # Développé par le Développeur B
└── main.py          # Interface principale (Développeur B, puis fusion)
```

### 🌿 Gestion des Branches Git

1. **Dépôt Initial :** Création d'un dossier vide (ou avec un README.md) sur la branche principale (main ou master).

2. **Branche Développeur A :** `feature/chiffrement`

3. **Branche Développeur B :** `feature/dechiffrement-ui`

4. **Fin de Sprint :** Fusion (Merge) des deux branches dans la branche principale.

## 3.  Spécifications Techniques

**🧑‍💻 Développeur A : Module Chiffrement (`encodeur.py`)**

* **Mission** : Concevoir la logique de transformation du texte clair en texte secret.

* **Fonction principale à développer :**

    * `chiffrer\_cesar(texte: str, decalage: int) -> str`

* **Contraintes techniques :**

    * Gérer le dépassement de l'alphabet (ex: avec un décalage de 3, 'Z' devient 'C').

    * *Optionnel mais recommandé :* Préserver la casse (majuscules/minuscules) et ne pas modifier les espaces ou la ponctuation.

**🧑‍💻 Développeur B : Module Déchiffrement & UI (`decodeur.py` & `main.py`)**

* **Mission 1 (Logique) :** Créer le module inverse dans decodeur.py.

    * Fonction : `dechiffrer\_cesar(texte\_code: str, decalage: int) -> str` (Souvent équivalent à appeler le chiffrement avec un décalage négatif).

* **Mission 2 (Interface) :** Créer le point d'entrée de l'application dans `main.py`.

    * Développer un menu textuel interactif en console.

    * Exemple de flux :

```
--- LA BOÎTE À OUTILS SECRÈTE ---

1. Chiffrer un message
2. Déchiffrer un message
3. Quitter

Choix :
```

## 4. Intégration et Fusion (Fin de Sprint)

C'est le moment clé du projet où le travail des deux développeurs s'assemble.

1. **Fusionner** la branche `feature/chiffrement` dans `main`.

2. **Fusionner** la branche `feature/dechiffrement-ui` dans `main`.

3. **Liaison des modules :** Dans le fichier `main.py`, le Développeur B (ou l'équipe ensemble) devra importer les fonctions des deux fichiers :

```python
import encodeur
import decodeur
# Exemple d'utilisation dans le menu :
# texte\_chiffre = encodeur.chiffrer\_cesar(message, cle)
```

## 5. Critères d'Acceptation (Pour valider le projet)

* [ ] Le code ne génère aucune erreur d'exécution lors des imports.

* [ ] Si on chiffre le message `"HELLO"` avec un décalage de `3`, on obtient `"KHOOR"`.

* [ ] Si on passe `"KHOOR"` dans le décodeur avec le même décalage, on retrouve `"HELLO"`.

* [ ] L'historique Git montre clairement le travail séparé dans les deux branches distinctes avant la fusion.


