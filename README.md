Je teste de faire un site pour mon institut en utilisant [Hugo](https://gohugo.io/).

# Documentation

## Information à renseigner pour chaque membre

Dans le header des fichiers `content/people/prenom.nom.md` ou le tableur.

Nécessaire :

- `id` un identifiant, par exemple celui d'INSERM (recommendé)
- `first_name`/`last_name` prénom(s) et nom de famille
- `email` email institutionnel
- `team` équipe ou plateforme d'appartenance. Voir [liste équipes/plateformes](#ids-equipes-plateformes).
- `position` position dans l'institut, par exemple *Doctorant*
    - Dans le tableur `position_en` renseigne la version anglaise, par exemple *PhD Student*

Autres informations :

- `phone` numéro de téléphone
- `room` batiment/bureau
- `subteam` sous-équipe (pour l'équipe 2 pour l'instant). Options: ???

Pour gérer les publications :

- `oa_id` l'identifiant OpenAlex à utiliser pour extraire périodiquement les publications. 
    - Chercher sur [OpenAlex](https://openalex.org/) puis utiliser l'identifiant dans l'adresse de la page *Author*, par exemple *a5048124649* pour [https://openalex.org/authors/a5048124649](https://openalex.org/authors/a5048124649).
- `selected_dois` liste de DOIs des publications à afficher en priorité sur la page perso/équipe. 
    - Séparés par `;` sans espaces, par exemple: `10.1038/s41586-023-05896-x;10.1126/science.abg8871;10.1186/s13059-020-1941-7`.

Pour les anciens membres :

- `alumni` (ancienne) équipe. Même option que pour `team`.
- `alumni_position` comme pour `position`
    - `alumni_position_en` pour la version en anglais

## IDs Équipes Plateformes

- `eq1`/.../`eq6` pour les équipes 1, ..., 6.
- `platform-digestive` modèles digestifs
- `platform-organoid` organoides
- `platform-bip` BIP

## Images

Où placer des images ?

- visage des membres dans: [`static/images/people/`](static/images/people/)
    - image carrée, pas trop grande (ex 400x400)
    - nom fichier utilisant l'identifiant inserm, ex `jean.monlong.png`
- pour une page d'équipe/plateforme: `static/images/ID_EQUIPE/` avec `ID_EQUIPE` correspondant à l'équipe/plateforme (voir [liste équipes/plateformes](#ids-equipes-plateformes)

## Tester le site localement

```sh
hugo server --disableFastRender
```

## Icon de Font Awesome

https://fontawesome.com/v5/search

# Documentation avancé

## Menus

- Français: [`config/_default/menus.toml`](config/_default/menus.toml)
- Anglais: [`config/_default/menus.en.toml`](config/_default/menus.en.toml)

## Informations pour les pages "spéciales"

- Page d'accueil [`data/fr/homepage.yml`](data/fr/homepage.yml)/[`data/en/homepage.yml`](data/en/homepage.yml)
- Liste des équipes [`data/fr/teams.yml`](data/fr/teams.yml)/[`data/en/teams.yml`](data/en/teams.yml)
- Liste des plateformes [`data/fr/platforms.yml`](data/fr/platforms.yml)/[`data/en/platforms.yml`](data/en/platforms.yml)
- Liste des services [`data/fr/services.yml`](data/fr/services.yml)/[`data/en/services.yml`](data/en/services.yml)

## List de membres d'une équipe

Le shortcode qui s'utilise avec `{{< people-list >}}` est défini dans [layouts/shortcodes/people-list.html](layouts/shortcodes/people-list.html).

Pour l'équipe 2 (pour l'instant), on veut peut-être lister les membres de sous-équipes avec le shortcode `{{< people-list-subteam compath >}}` défini dans [layouts/shortcodes/people-list-subteam.html](layouts/shortcodes/people-list-subteam.html).

Pour les anciens membres: `{{< former-people-list >}}` défini dans [layouts/shortcodes/former-people-list.html](layouts/shortcodes/former-people-list.html).

## Liste des tous les membres de l'IRSD

[layouts/_default/peoples.html](layouts/_default/peoples.html)

## Couleur et autres contrôles esthétique

[assets/sass/custom.scss](assets/sass/custom.scss)

## Listes des publications

- Page globale: [layouts/_default/pubs.html](layouts/_default/pubs.html)
- Pour une équipe: [layouts/shortcodes/team-publications.html](layouts/shortcodes/team-publications.html)
- Pour un membre: [layouts/shortcodes/people-publications.html](layouts/shortcodes/people-publications.html)

# TODO list

1. Fix le bug avec les listes de gens https://github.com/metafizzy/isotope/issues/1575
2. Mettre en place une fonctionnalité de gallerie d'image
3. Améliorer la gestion des membres et alumnis, en prenant en compte la période d'activité pour les publications?

# Pour plus tard, pour remplir le site plus facilement

- https://markdownviewer.org/
    - Pour que les néophytes de markdown testent leur contenu
- https://grist.numerique.gouv.fr/
    - Pour partager un tableur avec les informations de chaque membre et automatiser la création de pages
- https://docs.numerique.gouv.fr/
    - Pas parfait, mais pourrait aider à faire faire les premières pages plus facilement.

# Info du thème

## Hugo HTML5 UP Arcana

This is a [Hugo](https://gohugo.io/) port of the
[Arcana template](https://html5up.net/arcana) from
[HTML5 UP](https://html5up.net/).
Check out the [live demo](https://sec.gd/hugo/themes/arcana/).

[![Screenshot](https://raw.githubusercontent.com/half-duplex/hugo-arcana/main/images/tn.png)](https://raw.githubusercontent.com/half-duplex/hugo-arcana/main/images/screenshot.png)

### Configuration
See the exampleSite folder. The elements on the homepage are defined in
`data/homepage.yml`, where you can choose which appear and configure them.

In case of multilingual websites, you can define your homepage within
the language directory of the specific language,
e.g. `data/en/homepage.yml` for English.
If the configuration does not exist, the content in `data/homepage.yml` is used.

The mostly-empty `_index.md` files are required for marking of the active menu
item to work correctly.

You can add your own styles in your site's `assets/sass/custom.scss`, which is
included at the end of the theme's `main.scss`.

### Multilingual
Translations for template content like the contact form
are located in the `i18n` directory.
Please feel free to contribute more languages into this directory.

### Showcase
If you use this theme and would like to be listed here, add your site in a pull
request!
- [Theme Demo Site](https://sec.gd/hugo/themes/arcana/)
- [Alichampi](https://alichampi.com/)
- [Odesa Regional Organization of Red Cross Society of Ukraine](https://od.redcross.org.ua/)
- [BOMnipotent Supply Chain Security Hosting](https://www.bomnipotent.de)

