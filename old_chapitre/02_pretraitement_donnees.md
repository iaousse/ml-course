Old content but gold:

::: {.callout-note title="Outil moderne : interroger des fichiers avec SQL" collapse="true"}
Un outil récent particulièrement apprécié des équipes de Data Science est **DuckDB** : un moteur SQL embarqué, capable d'exécuter des requêtes SQL directement sur des fichiers CSV ou Parquet, sans nécessiter l'installation d'un serveur de base de données. Il permet de traiter efficacement des fichiers bien plus volumineux que la mémoire disponible, ce qui en fait une alternative de plus en plus utilisée à `pandas` pour l'exploration de gros volumes de données tabulaires.
:::


::: {.callout-tip title="Mettre en place l'environnement de collecte avec `uv`"}
Comme introduit au chapitre 1 (§4.3), on déclare les dépendances nécessaires à ce chapitre dans le projet géré par `uv` :

```bash
uv add pandas polars requests beautifulsoup4 scrapy sqlalchemy
```

Chaque source de la @tbl-sources-donnees correspond ainsi à une ou plusieurs bibliothèques dédiées : `sqlalchemy` pour les bases relationnelles, `requests` pour interroger une API REST, `beautifulsoup4` pour le *scraping* ponctuel.
:::