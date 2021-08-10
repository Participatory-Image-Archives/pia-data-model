# PIA Data Model
Data model for the [_Participatory Knowledge Practices in Analogue and Digital Image Archives_ (PIA)](https://github.com/Participatory-Image-Archives/) project. This repository is tied to the user stories and use cases listed on https://github.com/Participatory-Image-Archives/pia-stories. 

## Contents
- [Description](#description)
    - [Data Model Diagrams and Flowcharts](#data-model-diagrams-and-flowcharts)
- [Installation and usage](#installation-and-usage)
    - [DBML Model](#dbml-model)

## Description
This repository is structured in the following manner: 
- `data-curation`: curated extracts of the SGV (_Schweizerische Gesellschaft für Volkskunde_) metadata
- `dbml model`: logical structure of the PIA database and SQL extract
- `iiif`: IIIF Manifest boilerplates, architecture overview and scripts to create IIIF-compliant resources
- `ontology`: current SGV ontology and RDF Data Model (in progress - not yet available)
- `salsah-export`: metadata extracted from https://salsah.org. All resource types' metadata from the SGV have been extracted, except for Images where only two collections relevant to the PIA project are available. In most folders can be found two XML files (unresolved and resolved properties) as well as a CSV file.

### Data Model Diagrams and Flowcharts
We use Miro to create diagrams and flowcharts. Here are some work-in-progress designs that can be viewed:

- PIA Data Flows and Outputs: https://miro.com/app/board/o9J_l_66_DQ=/
- RDF Data Model: https://miro.com/app/board/o9J_l87sD7U=/
- PIA ER Diagram: https://miro.com/app/board/o9J_l_UazRc=/

## Installation and usage
### DBML Model
The files in `dbml model` are the single origins of technical truth for the PIA database. The model is developed in close relation with the PIA ER diagram found in [Data Model Diagrams and Flowcharts](#data-model-diagrams-and-flowcharts). The folder contains

- `pia_datamodel.dbml`, a description of the model written in database markup language
- `pia_datamodel.sql`, a conversion of the model into sql
- `pia_populated.sql`, an export of the populated database

DBML is the [Database Markup Language](https://www.dbml.org/) and it aids in writing abstract database schemas. We regularly generate [a documentation of the PIA dbml model](https://dbdocs.io/thgie/pia_datamodel) via [dbdocs.io](https://dbdocs.io).

After installing the [dbml command line tool](https://www.dbml.org/cli/#installation), the sql file can be generated with the following commands

```bash
cd dbml\ model/
dbml2sql pia_datamodel.dbml
````

The process generates the sql file which than can be used to setup a database.