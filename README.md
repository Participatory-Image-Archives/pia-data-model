# PIA Data Model
Data model for the [_Participatory Knowledge Practices in Analogue and Digital Image Archives_ (PIA)](https://about.participatory-archives.ch) project.

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
|`dsp-migration`| Cleaning up the SGV - now EKWS - Metadata according to the SGV ontology on the DaSCH Service Platform(DSP) as well as a way to find all IIIF Image API URLs on DSP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|`ontology`| Old (hosted on Salsah) and current (hosted on DSP) SGV ontology as well as the PIA Data Model in Schema.org and Linked Art (work in progress)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|`salsah-export`| Metadata extracted from https://salsah.org with the help of a [repository bearing the same name](https://github.com/Participatory-Image-Archives/salsah-export) for the purpose of populating the PIA Database (PostgreSQL).  All resource types' metadata from the SGV – now EKWS – have been extracted, except for `Images` where only two collections relevant to the PIA project are available (SGV_10 and SGV_12). In most folders can be found two XML files (unresolved and resolved properties) as well as a CSV file.  In this directory are also available the `Geonames` and `properties` containing JSON files extracted from the Salsah API, a CSV which comprises all ASV places (`asv_places.csv` - SGV_05) as well as the SGV ontology needed for the database migration (`sgv.json`). The latter is a duplicate that is necessary for populating the database. The current EKWS ontology can be accessed at https://api.dasch.swiss/ontology/0812/ekws/v2.  |

### Data Model Diagrams and Flowcharts
We use Miro to create diagrams and flowcharts. Here are some work-in-progress designs that can be viewed:

- PIA Data Flows and Outputs: https://miro.com/app/board/o9J_l_66_DQ=/
- RDF Data Model: https://miro.com/app/board/o9J_l87sD7U=/
- PIA ER Diagram: https://miro.com/app/board/o9J_l_UazRc=/

## Licenses and citation
### To cite this repository
Demleitner A., Raemy J.A. (2024). PIA Data Model.
[![DOI](https://zenodo.org/badge/363361989.svg)](https://zenodo.org/badge/latestdoi/363361989) 

Or, alternatively, use the "Cite this repository" function 
