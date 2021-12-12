# PIA Data Model
Data model for the [_Participatory Knowledge Practices in Analogue and Digital Image Archives_ (PIA)](https://github.com/Participatory-Image-Archives/) project.

## Contents
- [Description](#description)
    - [Data Model Diagrams and Flowcharts](#data-model-diagrams-and-flowcharts)
- [Installation and usage](#installation-and-usage)
    - [DBML Model](#dbml-model)
- [Licenses and citation](#licenses-and-citation)

## Description
This repository is structured in the following manner: 
| Directory       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|`data-curation`| Curated extracts of the SGV (_Schweizerische Gesellschaft für Volkskunde_) metadata                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|`dbml model`| Logical structure of the PIA database and SQL extracts (schema and populated PostgreSQL files)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|`iiif`| IIIF Manifest boilerplates, architecture overview and scripts to create IIIF-compliant resources                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|`ontology`| Old and Current SGV ontology as well as the PIA Data Model in Schema.org and Linked Art (work in progress)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|`salsah-export`| Metadata extracted from https://salsah.org with the help of a [repository bearing the same name](https://github.com/Participatory-Image-Archives/salsah-export) for the purpose of populating the PIA Database (PostgreSQL).  All resource types' metadata from the SGV have been extracted, except for `Images` where only two collections relevant to the PIA project are available (SGV_10 and SGV_12). In most folders can be found two XML files (unresolved and resolved properties) as well as a CSV file.  In this directory are also available the `Geonames` and `properties` containing JSON files extracted from the Salsah API, a CSV which comprises all ASV places (`asv_places.csv` - SGV_05) as well as the current SGV ontology (`sgv.json`). The latter is a duplicate that is necessary for populating the database. |

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

The process generates the sql file which than can be used to setup a database. Don't forget to add usage rights to your postgresql user.

```bash
sudo -u postgres -i
psql
create database pia;
exit;
psql pia < pia_populated.sql
psql
\c pia
grant all privileges on all tables in schema public to {user};
grant all privileges on all sequences in schema public to {user};
```

## Licenses and citation
### To cite this repository
Demleitner A., Raemy J.A. (2021). PIA Data Model (version 0.2.2). DOI: https://doi.org/10.5281/zenodo.5142606
[![DOI](https://zenodo.org/badge/363361989.svg)](https://zenodo.org/badge/latestdoi/363361989) 

Or, alternatively, use the "Cite this repository" function 
