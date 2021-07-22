# PIA Data Model
Data model for the _Participatory Knowledge Practices in Analogue and Digital Image Archives_ (PIA) project. This repository is tied to the user stories and use cases listed on https://github.com/Participatory-Image-Archives/pia-stories. 

This repository is structured in the following manner: 
- `data-curation`: curated extracts of the SGV (_Schweizerische Gesellschaft für Volkskunde_) metadata
- `dbml model`: logical structure of the PIA database and SQL extract
- `iiif`: IIIF Manifest boilerplates, architecture overview and scripts to create IIIF-compliant resources
- `ontology`: current SGV ontology and RDF Data Model (in progress - not yet available)
- `salsah-export`: metadata extracted from https://salsah.org for the purpose of populating the PIA Database. All resource types' metadata from the SGV have been extracted, except for `Images` where only two collections relevant to the PIA project are available (SGV_10 and SGV_12). In most folders can be found two XML files (unresolved and resolved properties) as well as a CSV file. In this directory are also available the Geonames and properties containing JSON files extracted from the Salsah API, a CSV which comprises all ASV (SGV_05) places as well as the current SGV ontology. 

## Data Model Diagrams and Flowcharts

We use Miro to create diagrams and flowcharts. Here are some work-in-progress designs that can be viewed:

- PIA Data Flows and Outputs: https://miro.com/app/board/o9J_l_66_DQ=/
- RDF Data Model: https://miro.com/app/board/o9J_l87sD7U=/


