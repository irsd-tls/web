# Table avec information des membres

- `people.csv`

## TODO

- ajouter 
    - position alumni fr/en
    - selected DOIs?
    - sous-équipe

# OpenAlex pour extraire les publications

https://github.com/J535D165/pyalex

- page IRSD ? https://openalex.org/institutions/i4210122796
    - Pas toujours...

## Install OpenAlex

```sh
python3 -m venv venv
source venv/bin/activate
pip3 install pyalex
```

## Get publication info for all articles from the IRSD authors

```sh
source venv/bin/activate

python3 get_openalex_info.py
```

# Création de pages à partir de la table

```sh
python3 update_people_pages.py
```

