---
title: "Bioinformatics Research In Disease Genomics (BRIDGe)"
description: "Équipe 4"
menu: menu
weight: 80
layout: team
team: eq4
leader:
  - sarah.djebali
  - jean.monlong
image: images/eq4/banner_eq4.png
image_alt: "Equipe 4 IRSD"
tags: ["bioinformatics"]
---

*Mots-clés* : Génomique, Relation gène-enhancer, Variants structurels, Pangénome.

## Programme de recherche

L’équipe Bioinformatics Research In Disease Genomics (BRIDGe) étudie l’**impact fonctionnel des variations génomiques sur les maladies**. Bien que notre recherche soit fondamentalement sans a priori hypothétique, notre objectif est d’appliquer nos méthodes et analyses en priorité aux maladies digestives étudiées au sein du laboratoire, afin de tirer parti de l’expertise locale et de valider nos résultats.

Bien que de nombreuses études d’association pangénomiques (GWAS) aient identifié des milliers de variants associés à des maladies courantes, deux problèmes majeurs entravent une compréhension approfondie des mécanismes biologiques sous-jacents à ces maladies et le développement de nouveaux traitements :

1. les variants causaux réels restent très souvent inconnus,
1. l’ensemble des variants identifiés n’explique pas entièrement l’héritabilité de la maladie. En réalité, ces deux problèmes découlent du fait que :
1. seuls les petits variants (SNP) sont testés pour leur association avec la maladie,
1. la grande majorité des variants associés sont situés dans des régions régulatrices non codantes du génome.

Pour ces raisons, nous concentrons nos efforts sur :

1. L’extension des études d’association à des variants plus longs et complexes, tels que les variants structurels (SV, comme les duplications, délétions, insertions et translocations), en utilisant des approches pangénomiques ;
1. La dérivation d’annotations fonctionnelles génomiques spécifiques à des types cellulaires et leur intégration dans les études sur les maladies ;
1. L’intégration des variants structurels et des annotations fonctionnelles pour améliorer le diagnostic moléculaire dans les études sur les maladies génétiques rares.

{{< img2 "images/eq4/enhancer-gene_orig.png" "images/eq4/tubemap-for-website_orig.png" "60%" >}}

## Membres

{{< people-list >}}

### Anciens membres

{{< former-people-list >}}

## Outils et méthodes

- Analyse de séquençage du transcriptome (RNA-seq, miRNA-seq)
- Analyse de la conformation 3D de l’ADN (Hi-C, *promoter capture* Hi-C)
- Méthodes multi-omiques intégratives (ex. : *mixOmics*)
- Analyse de séquençage du génome à partir de données de lectures courtes (Illumina) ou longues (Oxford Nanopore)
- Analyse de données de séquençage utilisant des pangénomes humains (construction de pangénomes, alignement de lectures, appel de variants)
- Tests d’association pangénomique (GWAS)
- Appel de variants pour les maladies rares à partir de données de lectures longues (assemblage *de novo* phasé, variants structurels, annotation), y compris pour les régions complexes (ex. : module RCCX)

Les membres de l’équipe ont contribué à plusieurs logiciels publics, dont certains sont mis en avant ci-dessous :

- **ChimPipe** : un outil pour détecter de nouveaux transcrits chimériques et gènes de fusion à partir de données RNA-seq.
  [GitHub](https://github.com/Chimera-tools/ChimPipe), [Rodríguez-Martín et al. BMC Genomics 2017](https://doi.org/10.1186/s12864-016-3404-9)
- **TAGADA** : un pipeline complet pour l’analyse RNA-seq, incluant des modules pour créer des annotations de transcrits novateurs et quantifier l’expression des gènes et des transcrits.
  *GitHub, Kurylo, Guyomar, Foissac et Djebali. NAR Genomics and Bioinformatics 2023*
- **PaintorPipe** : un pipeline pour réaliser des analyses de *fine-mapping* des résultats de GWAS en utilisant diverses annotations fonctionnelles.
  *GitHub, Gerber et al. Bioinformatics Advances 2024*
- **sveval** : un package R pour manipuler et évaluer les performances des variants structurels.
  *GitHub, Heller, Hickey, Monlong et al. Genome Biology 2020*
- **vg** : une boîte à outils pour manipuler des pangénomes et analyser des données de séquençage, incluant l’alignement rapide de lectures *Giraffe*.
  *GitHub, Sirén, Monlong, Chang, Novak, Eizenga et al. Science 2021*
- **Minigraph-Cactus** : un pipeline de construction de pangénomes à partir d’assemblages génomiques de haute qualité.
  *GitHub, Hickey, Monlong et al. Nature Biotechnology 2024*
- **Parakit** : un outil basé sur le pangénome pour caractériser le module complexe RCCX à partir de données de lectures longues.
  *GitHub, Monlong et al. medRxiv 2025*

## Recruitement

Nous sommes activement à la recherche de nouveaux membres pour élargir notre équipe et accueillons avec enthousiasme des chercheurs en génomique et bioinformatique. Certains projets pourraient bénéficier de nouvelles expertises, notamment :

- des compétences avancées en statistiques pour contribuer à l’imputation de variants ;
- des connaissances en transcriptomique monocellulaire pour enrichir notre caractérisation cellulaire spécifique de la régulation des gènes ;
- ou encore des compétences en apprentissage automatique (*machine learning*) pour aider à prédire les éléments fonctionnels du génome ou les variants non codants fonctionnels.

Des recherches complémentaires pourraient également inclure des approches intégrant davantage de variants (par exemple, les variants structurels) ou des variants dotés de meilleures annotations fonctionnelles (par exemple, dans les régions régulatrices spécifiques à certaines cellules). Cela pourrait concerner, entre autres, le développement de métriques évolutives plus fines ou de scores de risque polygéniques.

N’hésitez pas à contacter **Sarah et Jean** si vous êtes intéressé(e) par une collaboration au sein de notre équipe !

## Publications

{{< team-publications >}}
