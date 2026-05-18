from ds_python_interpreter import ds_python_interpreter

md_content = """# Guide Complet des Balises Markdown

Ce guide répertorie toutes les syntaxes Markdown standards et étendues pour vous aider à rédiger des documents structurés.

---

## 1. Titres (Headings)
On utilise le symbole `#` suivi d'un espace.

# Titre Niveau 1 (H1)
## Titre Niveau 2 (H2)
### Titre Niveau 3 (H3)
#### Titre Niveau 4 (H4)
##### Titre Niveau 5 (H5)
###### Titre Niveau 6 (H6)

---

## 2. Emphase (Formatage du texte)

| Style | Syntaxe | Résultat |
| :--- | :--- | :--- |
| **Gras** | `**texte**` ou `__texte__` | **Texte en gras** |
| *Italique* | `*texte*` ou `_texte_` | *Texte en italique* |
| ***Gras & Italique*** | `***texte***` | ***Texte combiné*** |
| ~~Barré~~ | `~~texte~~` | ~~Texte barré~~ |

---

## 3. Listes

### Listes à puces (Non ordonnées)
Utilisez `*`, `-` ou `+`.
* Élément 1
* Élément 2
  * Sous-élément 2.1
  * Sous-élément 2.2

### Listes numérotées (Ordonnées)
1. Premier élément
2. Deuxième élément
   1. Sous-élément numéroté
   2. Un autre

### Listes de tâches (Checklists)
- [x] Tâche terminée
- [ ] Tâche à faire
- [ ] Autre chose

---

## 4. Liens et Images

### Liens
- [Lien externe](https://www.google.com)
- [Lien avec titre](https://www.google.com "Survolez-moi")
- Lien automatique : <https://www.google.com>

### Images
Syntaxe : `![Texte alternatif](URL_de_l_image)`
![Logo Markdown](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)

---

## 5. Citations (Blockquotes)

> C'est ainsi que l'on crée une citation.
> 
> > On peut même imbriquer des citations.

---

## 6. Code

### Code en ligne
Utilisez des accents graves (backticks) : `print("Hello World")`.

### Blocs de code
Utilisez trois accents graves (```) et spécifiez le langage pour la coloration syntaxique.

```python
def saluer(nom):
    print(f"Bonjour {nom}")
