# PIA Data Model
Data model for the _Participatory Knowledge Practices in Analogue and Digital Image Archives_ (PIA) project. This repository is tied to the user stories and use cases listed on https://github.com/Participatory-Image-Archives/pia-stories. 

This repository is structured in the following manner: 
| Directory       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|`data-curation`| Curated extracts of the SGV (_Schweizerische Gesellschaft für Volkskunde_) metadata                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|`dbml model`| Logical structure of the PIA database and SQL extracts (schema and populated PostgreSQL files)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|`iiif`| IIIF Manifest boilerplates, architecture overview and scripts to create IIIF-compliant resources                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|`ontology`| Current SGV ontology and RDF Data Model (in progress - not yet available)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|`salsah-export`| Metadata extracted from https://salsah.org with the help of a [private repository bearing the same name](https://github.com/Participatory-Image-Archives/salsah-export) for the purpose of populating the PIA Database (PostgreSQL).  All resource types' metadata from the SGV have been extracted, except for `Images` where only two collections relevant to the PIA project are available (SGV_10 and SGV_12). In most folders can be found two XML files (unresolved and resolved properties) as well as a CSV file.  In this directory are also available the `Geonames` and `properties` containing JSON files extracted from the Salsah API, a CSV which comprises all ASV places (`asv_places.csv` - SGV_05) as well as the current SGV ontology (`sgv.json`). The latter is a duplicate that is necessary for populating the database. |

## Data Model Diagrams and Flowcharts

We use Miro to create diagrams and flowcharts. Here are some work-in-progress designs that can be viewed:

- PIA Data Flows and Outputs: https://miro.com/app/board/o9J_l_66_DQ=/
- RDF Data Model: https://miro.com/app/board/o9J_l87sD7U=/

### To cite this repository
Demleitner A., Raemy J.A. (2021). PIA Data Model (version 0.1.1). DOI: https://doi.org/10.5281/zenodo.5142606
[![DOI](https://zenodo.org/badge/363361989.svg)](https://zenodo.org/badge/latestdoi/363361989) 

Or, alternatively, use the "Cite this repository" function 

