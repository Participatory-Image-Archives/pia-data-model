-- SQL dump generated using DBML (dbml-lang.org)
-- Database: PostgreSQL
-- Generated at: 2021-07-09T08:23:34.853Z

CREATE TABLE "Image" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "oldnr" varchar,
  "collection" int,
  "signature" varchar,
  "title" varchar,
  "original_title" varchar,
  "date" date[],
  "salsah_date" varchar,
  "sequence_number" varchar,
  "comment" int,
  "geography" int,
  "objecttype" int,
  "model" int,
  "format" int
);

CREATE TABLE "Keyword" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "label" varchar,
  "alt_label" varchar[],
  "description" varchar,
  "origin" varchar,
  "aat_id" int,
  "aat_url" varchar
);

CREATE TABLE "Images_Keywords" (
  "image_id" int,
  "keyword_id" int
);

CREATE TABLE "Comment" (
  "id" SERIAL PRIMARY KEY,
  "comment" varchar[]
);

CREATE TABLE "Geography" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "geonames_id" int,
  "geonames_url" varchar,
  "latitude" float,
  "longitude" float
);

CREATE TABLE "ObjectType" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "comment" varchar,
  "aat_id" int,
  "aat_url" varchar
);

CREATE TABLE "Model" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "comment" varchar,
  "aat_id" int,
  "aat_url" varchar
);

CREATE TABLE "Format" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "comment" varchar
);

CREATE TABLE "Person" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "name" varchar,
  "alt_name" varchar[],
  "title" varchar,
  "family" varchar,
  "gnd_id" int,
  "gnd_url" varchar,
  "birthplace" int,
  "deathplace" int,
  "birthdate" date[],
  "deathdate" date[],
  "salsah_birthdate" varchar,
  "salsah_deathdate" varchar,
  "job" varchar[],
  "description" text,
  "literature" varchar[],
  "comment" int
);

CREATE TABLE "Images_Content" (
  "image_id" int,
  "person_id" int
);

CREATE TABLE "Images_People" (
  "image_id" int,
  "person_id" int
);

CREATE TABLE "Images_Copyright" (
  "image_id" int,
  "person_id" int
);

CREATE TABLE "Collection" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "Album" (
  "id" SERIAL PRIMARY KEY,
  "collection" int,
  "description" text,
  "comment" varchar,
  "signature" varchar
);

CREATE TABLE "Images_Album" (
  "image_id" int,
  "album_id" int
);

CREATE TABLE "Document" (
  "id" SERIAL PRIMARY KEY,
  "object_type" int,
  "model" int,
  "format" int
);

CREATE TABLE "Map" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "MapEntry" (
  "id" SERIAL PRIMARY KEY,
  "map" int,
  "map_geography" int,
  "map_legend_entry" int
);

CREATE TABLE "MapGeography" (
  "id" SERIAL PRIMARY KEY,
  "geography" int
);

CREATE TABLE "MapLegend" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "MapLegendEntry" (
  "id" SERIAL PRIMARY KEY
);

CREATE TABLE "MapLegend_MapLegendEntries" (
  "map_legend_entry_id" int,
  "map_legend_id" int
);

ALTER TABLE "Image" ADD FOREIGN KEY ("collection") REFERENCES "Collection" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("comment") REFERENCES "Comment" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("geography") REFERENCES "Geography" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("objecttype") REFERENCES "ObjectType" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("model") REFERENCES "Model" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("format") REFERENCES "Format" ("id");

ALTER TABLE "Images_Keywords" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_Keywords" ADD FOREIGN KEY ("keyword_id") REFERENCES "Keyword" ("id");

ALTER TABLE "Person" ADD FOREIGN KEY ("birthplace") REFERENCES "Geography" ("id");

ALTER TABLE "Person" ADD FOREIGN KEY ("deathplace") REFERENCES "Geography" ("id");

ALTER TABLE "Person" ADD FOREIGN KEY ("comment") REFERENCES "Comment" ("id");

ALTER TABLE "Images_Content" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_Content" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Images_People" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_People" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Images_Copyright" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_Copyright" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Album" ADD FOREIGN KEY ("collection") REFERENCES "Collection" ("id");

ALTER TABLE "Images_Album" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_Album" ADD FOREIGN KEY ("album_id") REFERENCES "Album" ("id");

ALTER TABLE "Document" ADD FOREIGN KEY ("object_type") REFERENCES "ObjectType" ("id");

ALTER TABLE "Document" ADD FOREIGN KEY ("model") REFERENCES "Model" ("id");

ALTER TABLE "Document" ADD FOREIGN KEY ("format") REFERENCES "Format" ("id");

ALTER TABLE "MapEntry" ADD FOREIGN KEY ("map") REFERENCES "Map" ("id");

ALTER TABLE "MapEntry" ADD FOREIGN KEY ("map_geography") REFERENCES "MapGeography" ("id");

ALTER TABLE "MapEntry" ADD FOREIGN KEY ("map_legend_entry") REFERENCES "MapLegendEntry" ("id");

ALTER TABLE "MapGeography" ADD FOREIGN KEY ("geography") REFERENCES "Geography" ("id");

ALTER TABLE "MapLegend_MapLegendEntries" ADD FOREIGN KEY ("map_legend_entry_id") REFERENCES "MapLegendEntry" ("id");

ALTER TABLE "MapLegend_MapLegendEntries" ADD FOREIGN KEY ("map_legend_id") REFERENCES "MapLegend" ("id");

COMMENT ON TABLE "Collection" IS 'Brunner, Kreis, Atlas, etc';

COMMENT ON TABLE "Album" IS 'Right now not defined, if representing physical or virtual album';
