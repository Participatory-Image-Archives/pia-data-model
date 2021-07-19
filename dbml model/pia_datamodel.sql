-- SQL dump generated using DBML (dbml-lang.org)
-- Database: PostgreSQL
-- Generated at: 2021-07-19T10:55:24.942Z

CREATE TABLE "Image" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "oldnr" varchar,
  "signature" varchar,
  "title" varchar,
  "original_title" varchar,
  "date" date[],
  "salsah_date" varchar,
  "sequence_number" varchar,
  "comment" int,
  "location" int,
  "collection" int,
  "verso" int,
  "objecttype" int,
  "model" int,
  "format" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "References_Images" (
  "image_a" int,
  "image_b" int
);

CREATE TABLE "Keyword" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "label" varchar,
  "alt_label" varchar[],
  "description" varchar,
  "origin" varchar,
  "aat_id" int,
  "aat_url" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "Images_Keywords" (
  "image_id" int,
  "keyword_id" int
);

CREATE TABLE "Comment" (
  "id" SERIAL PRIMARY KEY,
  "comment" varchar[],
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "Location" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "geonames_id" int,
  "geonames_url" varchar,
  "latitude" float,
  "longitude" float,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "ObjectType" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "comment" varchar,
  "aat_id" int,
  "aat_url" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "Model" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "comment" varchar,
  "aat_id" int,
  "aat_url" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "Format" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "comment" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
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
  "comment" int,
  "created_at" timestamp,
  "updated_at" timestamp
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
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "title" varchar[],
  "label" varchar,
  "signature" varchar,
  "description" text,
  "default_image" varchar,
  "embedded_video" varchar,
  "date" date[],
  "salsah_date" varchar[],
  "literature" varchar[],
  "comment" int,
  "indexing" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "Collections_People" (
  "collection_id" int,
  "person_id" int
);

CREATE TABLE "Album" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "title" varchar,
  "label" varchar,
  "signature" varchar,
  "description" text,
  "date" date[],
  "salsah_date" varchar[],
  "objecttype" int,
  "collection" int,
  "comment" int,
  "indexing" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "Albums_People" (
  "album_id" int,
  "person_id" int
);

CREATE TABLE "Albums_Images" (
  "album_id" int,
  "image_id" int
);

CREATE TABLE "Document" (
  "id" SERIAL PRIMARY KEY,
  "object_type" int,
  "model" int,
  "format" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "Map" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "legend" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "MapLayer" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "map" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "MapEntry" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "map" int,
  "map_location" int,
  "map_legend_entry" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "Place" (
  "id" SERIAL PRIMARY KEY,
  "asv_id" varchar,
  "label" varchar,
  "collection" int,
  "location" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "Legend" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "LegendEntry" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "legend" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

ALTER TABLE "Image" ADD FOREIGN KEY ("comment") REFERENCES "Comment" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("location") REFERENCES "Location" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("collection") REFERENCES "Collection" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("verso") REFERENCES "Image" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("objecttype") REFERENCES "ObjectType" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("model") REFERENCES "Model" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("format") REFERENCES "Format" ("id");

ALTER TABLE "Images_Keywords" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_Keywords" ADD FOREIGN KEY ("keyword_id") REFERENCES "Keyword" ("id");

ALTER TABLE "Person" ADD FOREIGN KEY ("birthplace") REFERENCES "Location" ("id");

ALTER TABLE "Person" ADD FOREIGN KEY ("deathplace") REFERENCES "Location" ("id");

ALTER TABLE "Person" ADD FOREIGN KEY ("comment") REFERENCES "Comment" ("id");

ALTER TABLE "Images_Content" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_Content" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Images_People" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_People" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Images_Copyright" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_Copyright" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Collection" ADD FOREIGN KEY ("comment") REFERENCES "Comment" ("id");

ALTER TABLE "Collection" ADD FOREIGN KEY ("indexing") REFERENCES "Comment" ("id");

ALTER TABLE "Collections_People" ADD FOREIGN KEY ("collection_id") REFERENCES "Collection" ("id");

ALTER TABLE "Collections_People" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Album" ADD FOREIGN KEY ("objecttype") REFERENCES "ObjectType" ("id");

ALTER TABLE "Album" ADD FOREIGN KEY ("collection") REFERENCES "Collection" ("id");

ALTER TABLE "Album" ADD FOREIGN KEY ("comment") REFERENCES "Comment" ("id");

ALTER TABLE "Album" ADD FOREIGN KEY ("indexing") REFERENCES "Comment" ("id");

ALTER TABLE "Albums_People" ADD FOREIGN KEY ("album_id") REFERENCES "Album" ("id");

ALTER TABLE "Albums_People" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Albums_Images" ADD FOREIGN KEY ("album_id") REFERENCES "Album" ("id");

ALTER TABLE "Albums_Images" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Document" ADD FOREIGN KEY ("object_type") REFERENCES "ObjectType" ("id");

ALTER TABLE "Document" ADD FOREIGN KEY ("model") REFERENCES "Model" ("id");

ALTER TABLE "Document" ADD FOREIGN KEY ("format") REFERENCES "Format" ("id");

ALTER TABLE "Map" ADD FOREIGN KEY ("legend") REFERENCES "Legend" ("id");

ALTER TABLE "MapLayer" ADD FOREIGN KEY ("map") REFERENCES "Map" ("id");

ALTER TABLE "MapEntry" ADD FOREIGN KEY ("map") REFERENCES "Map" ("id");

ALTER TABLE "MapEntry" ADD FOREIGN KEY ("map_location") REFERENCES "Place" ("id");

ALTER TABLE "MapEntry" ADD FOREIGN KEY ("map_legend_entry") REFERENCES "LegendEntry" ("id");

ALTER TABLE "Place" ADD FOREIGN KEY ("collection") REFERENCES "Collection" ("id");

ALTER TABLE "Place" ADD FOREIGN KEY ("location") REFERENCES "Location" ("id");

ALTER TABLE "LegendEntry" ADD FOREIGN KEY ("legend") REFERENCES "Legend" ("id");

COMMENT ON TABLE "Place" IS 'This entity captures the Concept of the ASV Gemeinde but doesn"t describe an actual location with coordinates.';
