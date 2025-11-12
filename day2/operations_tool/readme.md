# Mini outil de calcul textuel — PLAN COMPLET

Objectif : lire un fichier `operations.txt` contenant une liste d'expressions arithmétiques simples (ex: `3 + 2`, `5 * 4`), évaluer **de façon sûre**, et écrire les résultats dans `results.txt`.

## A. Arborescence de fichiers recommandée

```
day2/
 ├─ operations_tool/
 │    ├─ __init__.py
 │    ├─ parser.py           # parse les lignes en AST/structure sûre
 │    ├─ evaluator.py       # exécute les opérations de façon sécurisée
 │    ├─ io_utils.py        # lecture/écriture fichiers + validations
 │    ├─ main.py            # CLI / orchestration (exécution du tool)
 │    └─ sample_files/
 │         ├─ operations.txt
 │         └─ results.txt   # généré par le script
 ├─ examples.py
 └─ exercises.py
```

> Mets ce dossier `operations_tool` dans `day2/`.
>  éxécution du script :
```bash
cd day2 
python -m operations_tool.main operations_tool/sample_files/operations.txt operations_tool/sample_files/results.txt
```



---

## B. Format attendu pour `operations.txt`

* Une expression par ligne.
* Expressions supportées : addition `+`, soustraction `-`, multiplication `*`, division `/`, parenthèses `()`, puissances `**`, espaces tolérés.
* Exemples valides :

  ```
  3 + 2
  5 * (4 + 1)
  10 / 2
  2 ** 8
  -5 + 3
  ```
* Lignes vides et commentaires (préfixe `#`) seront ignorés.

---

## C. Principes de sécurité (important)

Ne jamais utiliser `eval()` directement sur l’entrée. On utilisera :

* Le module `ast` pour parser l’expression et n’autoriser que les nœuds sûrs (Num, BinOp, UnaryOp, Expression, etc.).
* Refuser tout appel de fonction, attribut, noms ou autres nœuds dangereux.

## Améliorations possible (roadmap & monétisation)

1. **Interface CLI améliorée**

   * Utilise `typer` (facile) pour options (`--input`, `--output`, `--precision`, `--safe-mode`).

2. **API Web légère**

   * Exposer un endpoint FastAPI pour uploader un fichier et recevoir `results.txt`. (Plus tard : hébergement sur Heroku/Render/Cloud Run).

3. **Parser étendu**

   * Support variables simples (`x = 3`, `x * 2`) avec environnement isolé.
   * Support fonctions math avancées via whitelist (`sqrt`, `log`) — mais uniquement via mapping sécurisé (`math.sqrt`) et pas `eval`.

4. **Monétisation**

   * Outil SaaS simple : upload de fichiers d'expressions pour batch processing (abonnement mensuel pour volumes).
   * Version entreprise : intégration à des pipelines ETL (extraction/validation de rules) — facturation par job.
   * Pack de scripts personnalisés pour PME (ex: transformation de feuilles clients en calculs) + support payant.

5. **Logging & Monitoring**

   * Ajoute logs, métriques (nombre d'opérations, taux d'erreur) pour suivi business.

6. **Packaging**

   * transforme en package pip/CLI pour distribution (`setup.cfg` / `pyproject.toml`).

---

## Checklist pour toi — ce que tu dois commit & push

* `day2/operations_tool/parser.py`
* `day2/operations_tool/evaluator.py`
* `day2/operations_tool/io_utils.py`
* `day2/operations_tool/main.py`
* `day2/operations_tool/sample_files/operations.txt`
* (optionnel) `day2/operations_tool/sample_files/results.txt` output
* tests minimalistes

---

## H. Conseils mentors (bonnes pratiques)

* Écris des docstrings pour chaque fonction (doc + exemples).
* Ajoute validations et tests unitaires pour parse/evaluator edge-cases.
* Garde tout small & simple — sécurité d'abord.
* Fais des commits atomiques et messages explicites (ex: `feat: add safe AST parser`).