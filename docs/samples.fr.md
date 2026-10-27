# Exemples exécutables

Les exemples ci-dessous sont également disponibles sous forme de scripts dans le [répertoire samples](https://github.com/georchestra/geo-utils/tree/main/samples). Exécutez-les depuis la racine du dépôt ou après l’installation du package. Ils nécessitent une instance geOrchestra accessible et un compte autorisé à utiliser les services concernés.

Chaque script définit des constantes modifiables `SERVER`, `USERNAME` et `PASSWORD` près du début du fichier. Remplacez les valeurs indicatives par l’URL de votre instance et votre compte avant l’exécution ; l’outil de modification XML n’utilise que `SERVER`.

## Exemples de la bibliothèque

- [API Console](https://github.com/georchestra/geo-utils/blob/main/samples/console_api_demo.py) : lit l’utilisateur configuré par défaut. `--apply` crée puis supprime des ressources de test temporaires. `--update-user-description` modifie la description de l’utilisateur configuré.

```bash
python samples/console_api_demo.py
python samples/console_api_demo.py --apply
```

- [Client combiné](https://github.com/georchestra/geo-utils/blob/main/samples/georchestra_client_demo.py) : liste les moissonnages filesystem actifs et peut lire une fiche avec `--uuid UUID`. `--assign-harvests` modifie les affectations. `--batch-edit` modifie la fiche sélectionnée et doit être utilisé avec `--uuid`.

```bash
python samples/georchestra_client_demo.py --uuid UUID
python samples/georchestra_client_demo.py --uuid UUID --batch-edit
```

- [API GeoNetwork](https://github.com/georchestra/geo-utils/blob/main/samples/geonetwork_api_demo.py) : lit les informations du site et les thésaurus par défaut. `--thesaurus-file FICHIER` téléverse un thésaurus ; `--overwrite-metadata FICHIER` remplace et publie une fiche.

```bash
python samples/geonetwork_api_demo.py
python samples/geonetwork_api_demo.py --thesaurus-file vocabulaire.rdf
```

- [Outil de métadonnées et thésaurus](https://github.com/georchestra/geo-utils/blob/main/samples/metadata_thesaurus_demo.py) : ajoute un mot-clé GeoNetwork au fichier de métadonnées fourni et écrit par défaut dans `sample_meta3.xml`. Utilisez `--output FICHIER` pour choisir une autre destination.

```bash
python samples/metadata_thesaurus_demo.py metadata.xml --output mise-a-jour.xml
```

- [Outil de modification XML](https://github.com/georchestra/geo-utils/blob/main/samples/meta_manipulation_demo.py) : ajoute un élément de thésaurus ISO 19139 hérité et écrit par défaut dans `<entrée>.new`.

```bash
python samples/meta_manipulation_demo.py metadata.xml
```

- [Identifiants de ressources en double](https://github.com/georchestra/geo-utils/blob/main/samples/detection_duplicate_id_ressource.py) : exemple existant de détection des identifiants de ressources en double.

Les modifications distantes nécessitent une option explicite. Vérifiez le script et l’instance cible avant d’utiliser `--update-user-description`, `--assign-harvests`, `--batch-edit`, `--thesaurus-file` ou `--overwrite-metadata`.

## Autres outils en ligne de commande

Ces fichiers sont des utilitaires autonomes, et non des démonstrations de la bibliothèque ; leurs points d’entrée `main()` sont conservés :

- [Créateur LDIF LDAP](https://github.com/georchestra/geo-utils/blob/main/ldap/creatorldif.py), avec les instructions dans le [README LDAP](https://github.com/georchestra/geo-utils/blob/main/ldap/README.md).
- [Générateur de liens proxy](https://github.com/georchestra/geo-utils/blob/main/proxy/proxy_links.py), avec les instructions dans le [README proxy](https://github.com/georchestra/geo-utils/blob/main/proxy/README.md).
