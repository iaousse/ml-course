---
title: "Chapitre 2 — Collecte et Prétraitement des Données"
---

# Collecte et Prétraitement des Données

```{prf:remark} Objectifs du chapitre
:class: tip

- Identifier les principales stratégies de collecte de données (bases de données, web scraping, API).
- Comprendre l'importance de la représentativité d'un échantillon.
- Appliquer les techniques de nettoyage, d'encodage et de mise à l'échelle des données.
- Construire un pipeline de prétraitement avec `Pandas` et `Scikit-Learn`.
```

*a remplir : introduction du chapitre.*

## 2.1 Stratégies de collecte de données

*a remplir*

```{list-table} Sources de données courantes
:label: tbl-sources-donnees
:header-rows: 1

* - Source
  - Exemple
* - Bases de données
  - SQL, NoSQL
* - Web Scraping
  - `BeautifulSoup`, `Scrapy`
* - APIs
  - REST, GraphQL
```

## 2.2 Représentativité et biais statistiques

*a remplir*

```{prf:remark} À retenir
:class: important
Un échantillon non représentatif introduit un biais qui se propage à toutes les étapes
du modèle, même si l'algorithme est parfaitement implémenté.
```

## 2.3 Nettoyage des données (imputation)

*a remplir*

## 2.4 Encodage des variables catégorielles

*a remplir : One-Hot Encoding, Label Encoding.*

## 2.5 Mise à l'échelle : Standardisation vs Normalisation

*a remplir*

```{math}
:label: eq-standardisation
x' = \frac{x - \mu}{\sigma}
```

```{math}
:label: eq-normalisation
x' = \frac{x - x_{min}}{x_{max} - x_{min}}
```

Voir [](#eq-standardisation) et [](#eq-normalisation) : le choix entre ces deux transformations
dépend de la sensibilité de l'algorithme aux distances (voir TD 1).

## 2.6 Résumé du chapitre

```{prf:remark} À retenir
:class: important

- La qualité du modèle final dépend directement de la qualité du prétraitement.
- La mise à l'échelle est indispensable pour les algorithmes basés sur des distances (KNN, K-Means, PCA).
```

## 2.7 Exercices

```{exercise}
:label: ex-pretraitement-1

Expliquer pourquoi la mise à l'échelle des variables est nécessaire avant d'appliquer
l'algorithme des $K$ plus proches voisins.
```

```{solution} ex-pretraitement-1
:label: sol-pretraitement-1
:class: dropdown

*a remplir : corrigé détaillé.*
```
