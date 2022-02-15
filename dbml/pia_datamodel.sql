-- SQL dump generated using DBML (dbml-lang.org)
-- Database: PostgreSQL
-- Generated at: 2022-02-15T09:15:41.376Z

CREATE TABLE "locations" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "geonames_id" int,
  "geonames_uri" varchar,
  "geonames_code" varchar,
  "geonames_code_name" varchar,
  "geonames_division_level" varchar,
  "wiki_url" varchar,
  "geometry" varchar,
  "latitude" float,
  "longitude" float,
  "origin" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "dates" (
  "id" SERIAL PRIMARY KEY,
  "date" date,
  "date_string" varchar,
  "type" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "keywords" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "label" varchar,
  "description" varchar,
  "origin" varchar,
  "aat_id" int,
  "aat_url" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "alt_labels" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "keyword_alt_label" (
  "keyword_id" int,
  "alt_label_id" int
);

CREATE TABLE "comments" (
  "id" SERIAL PRIMARY KEY,
  "comment" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "documents" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "file_name" varchar,
  "original_file_name" varchar,
  "base_path" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "document_collection" (
  "document_id" int,
  "collection_id" int
);

CREATE TABLE "document_image" (
  "document_id" int,
  "image_id" int
);

CREATE TABLE "people" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "name" varchar,
  "title" varchar,
  "family" varchar,
  "gnd_id" int,
  "gnd_url" varchar,
  "birthplace" int,
  "deathplace" int,
  "description" text,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "person_date" (
  "person_id" int,
  "date_id" int
);

CREATE TABLE "person_comment" (
  "person_id" int,
  "comment_id" int
);

CREATE TABLE "person_job" (
  "person_id" int,
  "job_id" int
);

CREATE TABLE "person_literature" (
  "person_id" int,
  "literature_id" int
);

CREATE TABLE "person_alt_label" (
  "person_id" int,
  "alt_label_id" int
);

CREATE TABLE "jobs" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "literatures" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "images" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "oldnr" varchar,
  "signature" varchar,
  "title" varchar,
  "original_title" varchar,
  "location_id" int,
  "file_name" varchar,
  "original_file_name" varchar,
  "base_path" varchar,
  "salsah_date" varchar,
  "sequence_number" varchar,
  "verso_id" int,
  "object_type_id" int,
  "model_id" int,
  "format_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "image_date" (
  "image_id" int,
  "date_id" int
);

CREATE TABLE "image_person" (
  "image_id" int,
  "person_id" int
);

CREATE TABLE "image_copyright" (
  "image_id" int,
  "person_id" int
);

CREATE TABLE "image_image" (
  "image_a" int,
  "image_b" int
);

CREATE TABLE "image_keyword" (
  "image_id" int,
  "keyword_id" int
);

CREATE TABLE "image_comment" (
  "image_id" int,
  "comment_id" int
);

CREATE TABLE "image_collection" (
  "image_id" int,
  "collection_id" int
);

CREATE TABLE "object_types" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "comment" varchar,
  "aat_id" int,
  "aat_url" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "models" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "comment" varchar,
  "aat_id" int,
  "aat_url" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "formats" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "comment" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "collections" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "label" varchar,
  "signature" varchar,
  "description" text,
  "default_image" varchar,
  "embedded_video" varchar,
  "origin" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "collection_comment" (
  "collection_id" int,
  "comment_id" int
);

CREATE TABLE "collection_person" (
  "collection_id" int,
  "person_id" int
);

CREATE TABLE "collection_literature" (
  "collection_id" int,
  "literature_id" int
);

CREATE TABLE "collection_date" (
  "collection_id" int,
  "date_id" int
);

CREATE TABLE "collection_alt_label" (
  "collection_id" int,
  "alt_label_id" int
);

CREATE TABLE "sets" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "description" varchar,
  "signatures" varchar,
  "collection_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "albums" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "title" varchar,
  "label" varchar,
  "signature" varchar,
  "description" text,
  "object_type_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "album_collection" (
  "album_id" int,
  "collection_id" int
);

CREATE TABLE "album_date" (
  "album_id" int,
  "date_id" int
);

CREATE TABLE "album_person" (
  "album_id" int,
  "person_id" int
);

CREATE TABLE "album_image" (
  "album_id" int,
  "image_id" int
);

CREATE TABLE "album_comment" (
  "album_id" int,
  "comment_id" int
);

CREATE TABLE "maps" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "description" varchar,
  "tiles" int,
  "origin" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "map_layers" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "map_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "map_linked_map_layer" (
  "map_id" int,
  "map_layer_id" int
);

CREATE TABLE "map_keys" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "map_id" int,
  "icon" varchar,
  "icon_file_name" varchar,
  "original_icon_file_name" varchar,
  "map_key_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "map_entries" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "description" varchar,
  "type" int,
  "complex_data" varchar,
  "image_id" int,
  "map_layer_id" int,
  "location_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "map_entry_map_key" (
  "map_entry_id" int,
  "map_key_id" int
);

CREATE TABLE "pia_docs" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "description" varchar,
  "content" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "pia_doc_collection" (
  "pia_doc_id" int,
  "collection_id" int
);

CREATE TABLE "map_collection" (
  "map_id" int,
  "collection_id" int
);

ALTER TABLE "images" ADD FOREIGN KEY ("location_id") REFERENCES "locations" ("id");

ALTER TABLE "images" ADD FOREIGN KEY ("verso_id") REFERENCES "images" ("id");

ALTER TABLE "images" ADD FOREIGN KEY ("object_type_id") REFERENCES "object_types" ("id");

ALTER TABLE "images" ADD FOREIGN KEY ("model_id") REFERENCES "models" ("id");

ALTER TABLE "images" ADD FOREIGN KEY ("format_id") REFERENCES "formats" ("id");

ALTER TABLE "sets" ADD FOREIGN KEY ("collection_id") REFERENCES "collections" ("id") ON DELETE CASCADE;

ALTER TABLE "albums" ADD FOREIGN KEY ("object_type_id") REFERENCES "object_types" ("id");

ALTER TABLE "map_keys" ADD FOREIGN KEY ("map_id") REFERENCES "maps" ("id") ON DELETE CASCADE;

ALTER TABLE "map_entries" ADD FOREIGN KEY ("map_layer_id") REFERENCES "map_layers" ("id") ON DELETE CASCADE;

COMMENT ON TABLE "dates" IS 'Type can be either:
  1: date, a simple date with unclear definition (often it designates)
  2: start_date, in case of a daterange
  3: end_date, in case of a daterange
  4: birth_date, for a person
  5: death_date, for a person';

COMMENT ON TABLE "people" IS 'A person can have
- dates (dates, birth, death)
- comments
- jobs
- related literature
- alternative names (alt_labels)';

COMMENT ON TABLE "images" IS 'An image can have
- dates 
- people, displayed or as copyright
- references to other images
- keywords
- comments
- a location

…can be
- in several collections (original salsah, newly made ones)';

COMMENT ON TABLE "image_date" IS 'TODO: Should years be described as date ranges? (zb 1937 => 1937-01-01 - 1937-12-31)';

COMMENT ON TABLE "maps" IS 'A map can have

- layers
- map keys (legend)
- entries';

COMMENT ON TABLE "map_entries" IS 'Type can be either:
  1: precise, which is a marker placed on the map by hand; leading to the creation of a location
  2: complex, which is mutiple markers, a shape or line or an image; stores the information in complex_data
  3: image, overlaying the map; stores information in complex_data
  4: image, as marker; leading to the creation of a location';
