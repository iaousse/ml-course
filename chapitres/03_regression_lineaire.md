---
title: "Chapitre 3 — Workflow ML et Régression Linéaire"
---

# Workflow ML et Régression Linéaire

```{prf:remark} Objectifs du chapitre
:class: tip

- Décrire le cycle de vie complet d'un modèle de Machine Learning.
- Définir les notions de biais, de variance et de sur-apprentissage.
- Formuler le modèle de régression linéaire simple et sa fonction de coût (MSE).
- Construire un pipeline `Scikit-Learn` de bout en bout.
```

*a remplir : introduction du chapitre.*

## 3.1 Le cycle de vie d'un modèle

*a remplir*

```{prf:remark} À retenir
:class: important

Collecte → Prétraitement → Entraînement (Train) → Validation → Test → Déploiement.
```

## 3.2 Le modèle linéaire simple

*a remplir*

```{math}
:label: eq-modele-lineaire
\hat{y} = w_0 + w_1 x
```

## 3.3 Fonction de coût : l'erreur quadratique moyenne (MSE)

*a remplir*

$$
\text{MSE}(w) = \frac{1}{n} \sum_{i=1}^{n} \big(y_i - \hat{y}_i\big)^2
$$

```{note} Lien avec le TD 3
:class: dropdown
La dérivation analytique de cette fonction de coût et la résolution par la méthode des
moindres carrés sont traitées en détail dans le [TD 3](../td/td3_gradients_et_regression.md).
```

## 3.4 Validation de la performance : Train/Test Split

*a remplir*

## 3.5 Résumé du chapitre

```{prf:remark} À retenir
:class: important

- Le sur-apprentissage se corrige en évaluant le modèle sur un jeu de test indépendant.
- La régression linéaire minimise la MSE, résolue analytiquement ou par descente de gradient.
```

## 3.6 Exercices

```{exercise}
:label: ex-regression-1

Expliquer pourquoi il est indispensable de séparer les données en un ensemble
d'entraînement et un ensemble de test avant d'évaluer un modèle.
```

```{solution} ex-regression-1
:label: sol-regression-1
:class: dropdown

*a remplir : corrigé détaillé.*
```
