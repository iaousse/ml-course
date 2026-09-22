---
title: "Chapitre 5 — Apprentissage Non Supervisé et Réduction de Dimension"
---

# Apprentissage Non Supervisé et Réduction de Dimension

```{prf:remark} Objectifs du chapitre
:class: tip

- Modéliser des données non étiquetées.
- Appliquer les algorithmes de clustering $K$-Means et DBSCAN.
- Comprendre la malédiction de la dimensionnalité.
- Appliquer l'Analyse en Composantes Principales (PCA) pour réduire la dimension.
```

*a remplir : introduction du chapitre.*

## 5.1 Modélisation sur données non étiquetées

*a remplir*

## 5.2 L'algorithme $K$-Means

*a remplir*

```{math}
:label: eq-kmeans-cout
J = \sum_{k=1}^{K} \sum_{x_i \in C_k} \| x_i - \mu_k \|^2
```

```{note} Lien avec le TD 4
:class: dropdown
Les itérations analytiques de l'algorithme $K$-Means sont détaillées dans le
[TD 5](../td/td5_kmeans_convergence.md).
```

## 5.3 DBSCAN et limites du clustering

*a remplir*

## 5.4 La malédiction de la dimensionnalité

*a remplir*

## 5.5 Analyse en Composantes Principales (PCA)

*a remplir*

```{prf:remark} À retenir
:class: important
La PCA projette les données sur les directions de variance maximale, obtenues comme
vecteurs propres de la matrice de covariance.
```

## 5.6 Résumé du chapitre

```{prf:remark} À retenir
:class: important

- Le clustering ne nécessite pas d'étiquettes, contrairement à la classification.
- La PCA est un outil de réduction de dimension utile avant clustering ou visualisation.
```

## 5.7 Exercices

```{exercise}
:label: ex-clustering-1

Décrire la méthode du coude (*elbow method*) et son utilité pour choisir le nombre de
clusters $K$.
```

```{solution} ex-clustering-1
:label: sol-clustering-1
:class: dropdown

*a remplir : corrigé détaillé.*
```
