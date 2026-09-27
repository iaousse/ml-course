---
title: "Chapitre 6 — Séries Temporelles (Time Series)"
---

# Séries Temporelles (Time Series)

```{prf:remark} Objectifs du chapitre
:class: tip

- Identifier les spécificités de la modélisation temporelle par rapport aux données classiques.
- Définir tendance, saisonnalité, autocorrélation et stationnarité.
- Construire des variables décalées (*lag features*) pour une approche ML.
- Valider un modèle temporel sans fuite de données (*data leakage*).
```

*a remplir : introduction du chapitre.*

## 6.1 Spécificités de la modélisation temporelle

*a remplir*

```{prf:remark} Attention
:class: warning
Les observations d'une série temporelle ne sont pas indépendantes : l'ordre chronologique
doit être préservé lors de la validation du modèle.
```

## 6.2 Tendance, saisonnalité et autocorrélation

*a remplir*

## 6.3 Stationnarité

*a remplir*

```{note} Lien avec le TD
:class: dropdown
La transformation d'une série non stationnaire (différenciation) est traitée en détail
dans le TD dédié à ce chapitre.
```

## 6.4 Création de variables décalées (*lag features*)

*a remplir*

```{math}
:label: eq-lag-feature
x_t^{(k)} = y_{t-k}
```

## 6.5 Validation temporelle stricte (*Time Series Split*)

*a remplir : éviter la fuite de données (*data leakage*) en respectant l'ordre chronologique.*

## 6.6 Résumé du chapitre

```{prf:remark} À retenir
:class: important

- Une série temporelle ne peut pas être mélangée aléatoirement avant validation.
- Les variables décalées permettent de reformuler un problème temporel en un problème supervisé classique.
```

## 6.7 Exercices

```{exercise}
:label: ex-series-1

Expliquer pourquoi une validation croisée classique (`KFold`) est inadaptée à une série
temporelle.
```

```{solution} ex-series-1
:label: sol-series-1
:class: dropdown

*a remplir : corrigé détaillé.*
```
