---
title: "Chapitre 4 — Classification et Optimisation des Modèles"
---

# Classification et Optimisation des Modèles

```{prf:remark} Objectifs du chapitre
:class: tip

- Comparer les algorithmes de classification (régression logistique, KNN, arbres, forêts aléatoires).
- Distinguer paramètres et hyperparamètres d'un modèle.
- Évaluer un classifieur à l'aide de la matrice de confusion et des métriques associées.
- Optimiser un modèle par recherche sur grille (`GridSearchCV`).
```

*a remplir : introduction du chapitre.*

## 4.1 Algorithmes de classification

*a remplir*

```{list-table} Algorithmes de classification étudiés
:label: tbl-classification-algos
:header-rows: 1

* - Algorithme
  - Principe
* - Régression logistique
  - Modèle linéaire + fonction sigmoïde
* - K-Plus Proches Voisins (KNN)
  - Vote majoritaire des voisins les plus proches
* - Arbre de décision
  - Partitionnement récursif de l'espace des variables
* - Forêt aléatoire
  - Agrégation de plusieurs arbres de décision
```

## 4.2 Paramètres vs Hyperparamètres

*a remplir*

## 4.3 Matrice de confusion et métriques d'évaluation

*a remplir*

```{math}
:label: eq-precision
\text{Précision} = \frac{TP}{TP + FP}
```

```{math}
:label: eq-rappel
\text{Rappel} = \frac{TP}{TP + FN}
```

```{note} Compromis Précision/Rappel
:class: dropdown
Ce compromis est essentiel dans les contextes de classes déséquilibrées, comme le montre
le TD 3.
```

## 4.4 Validation Train/Validation/Test

*a remplir*

## 4.5 Résumé du chapitre

```{prf:remark} À retenir
:class: important

- Le choix des hyperparamètres doit être validé sur un ensemble distinct de l'entraînement.
- Le F1-Score est préférable à l'exactitude sur des classes déséquilibrées.
```

## 4.6 Exercices

```{exercise}
:label: ex-classification-1

Expliquer dans quel contexte la métrique de rappel doit être privilégiée par rapport
à la précision.
```

```{solution} ex-classification-1
:label: sol-classification-1
:class: dropdown

*a remplir : corrigé détaillé.*
```
