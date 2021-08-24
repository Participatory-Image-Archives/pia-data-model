-- SQL dump generated using DBML (dbml-lang.org)
-- Database: PostgreSQL
-- Generated at: 2021-08-24T10:29:59.164Z

CREATE TABLE "locations" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "geonames_id" int,
  "geonames_url" varchar,
  "latitude" float,
  "longitude" float,
  "place_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "places" (
  "id" SERIAL PRIMARY KEY,
  "asv_id" varchar,
  "label" varchar,
  "collection_id" int,
  "location_id" int,
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

CREATE TABLE "images" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "oldnr" varchar,
  "signature" varchar,
  "title" varchar,
  "original_title" varchar,
  "file_name" varchar,
  "original_file_name" varchar,
  "salsah_date" varchar,
  "sequence_number" varchar,
  "location" int,
  "collection" int,
  "verso" int,
  "objecttype" int,
  "model" int,
  "format" int,
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

CREATE TABLE "collections" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "label" varchar,
  "signature" varchar,
  "description" text,
  "default_image" varchar,
  "embedded_video" varchar,
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

CREATE TABLE "albums" (
  "id" SERIAL PRIMARY KEY,
  "salsah_id" int,
  "title" varchar,
  "label" varchar,
  "signature" varchar,
  "description" text,
  "objecttype" int,
  "collection" int,
  "created_at" timestamp,
  "updated_at" timestamp
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

CREATE TABLE "documents" (
  "id" SERIAL PRIMARY KEY,
  "object_type" int,
  "model" int,
  "format" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "maps" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "description" varchar,
  "map_key_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "map_layers" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "map" int,
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
  "map_id" int,
  "place_id" int,
  "location_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "map_keys" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "map_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "map_key_entries" (
  "id" SERIAL PRIMARY KEY,
  "label" varchar,
  "icon" varchar,
  "icon_file_name" varchar,
  "original_icon_file_name" varchar,
  "map_key_id" int,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "map_entry_map_key_entry" (
  "map_entry_id" int,
  "map_key_entry_id" int
);

ALTER TABLE "locations" ADD FOREIGN KEY ("place_id") REFERENCES "places" ("id");

ALTER TABLE "places" ADD FOREIGN KEY ("location_id") REFERENCES "locations" ("id");

ALTER TABLE "images" ADD FOREIGN KEY ("location") REFERENCES "locations" ("id");

ALTER TABLE "images" ADD FOREIGN KEY ("collection") REFERENCES "collections" ("id");

ALTER TABLE "images" ADD FOREIGN KEY ("verso") REFERENCES "images" ("id");

ALTER TABLE "images" ADD FOREIGN KEY ("objecttype") REFERENCES "object_types" ("id");

ALTER TABLE "images" ADD FOREIGN KEY ("model") REFERENCES "models" ("id");

ALTER TABLE "images" ADD FOREIGN KEY ("format") REFERENCES "formats" ("id");

ALTER TABLE "image_keyword" ADD FOREIGN KEY ("image_id") REFERENCES "images" ("id");

ALTER TABLE "image_keyword" ADD FOREIGN KEY ("keyword_id") REFERENCES "keywords" ("id");

ALTER TABLE "albums" ADD FOREIGN KEY ("objecttype") REFERENCES "object_types" ("id");

ALTER TABLE "albums" ADD FOREIGN KEY ("collection") REFERENCES "collections" ("id");

ALTER TABLE "album_person" ADD FOREIGN KEY ("album_id") REFERENCES "albums" ("id");

ALTER TABLE "album_person" ADD FOREIGN KEY ("person_id") REFERENCES "people" ("id");

ALTER TABLE "album_image" ADD FOREIGN KEY ("album_id") REFERENCES "albums" ("id");

ALTER TABLE "album_image" ADD FOREIGN KEY ("image_id") REFERENCES "images" ("id");

ALTER TABLE "documents" ADD FOREIGN KEY ("object_type") REFERENCES "object_types" ("id");

ALTER TABLE "documents" ADD FOREIGN KEY ("model") REFERENCES "models" ("id");

ALTER TABLE "documents" ADD FOREIGN KEY ("format") REFERENCES "formats" ("id");

ALTER TABLE "maps" ADD FOREIGN KEY ("map_key_id") REFERENCES "map_keys" ("id");

ALTER TABLE "map_layers" ADD FOREIGN KEY ("map") REFERENCES "maps" ("id");

ALTER TABLE "map_entries" ADD FOREIGN KEY ("image_id") REFERENCES "images" ("id");

ALTER TABLE "map_entries" ADD FOREIGN KEY ("place_id") REFERENCES "places" ("id");

ALTER TABLE "map_entries" ADD FOREIGN KEY ("map_id") REFERENCES "maps" ("id") ON DELETE CASCADE;

ALTER TABLE "map_keys" ADD FOREIGN KEY ("map_id") REFERENCES "maps" ("id") ON DELETE CASCADE;

ALTER TABLE "map_key_entries" ADD FOREIGN KEY ("map_key_id") REFERENCES "map_keys" ("id") ON DELETE CASCADE;

COMMENT ON TABLE "places" IS 'A Place is an unprecise concept related to geography.';

COMMENT ON TABLE "dates" IS 'Type can be either:
  1: date, a simple date with unclear definition (often it designates)
  2: start_date, in case of a daterange
  3: end_date, in case of a daterange
  4: birth_date, for a person
  5: death_date, for a person';

COMMENT ON TABLE "images" IS 'An image can have
- dates
- people, displayed or as copyright
- references to other images
- keywords
- comments';

COMMENT ON TABLE "map_entries" IS 'Type can be either:
  0: place, refering to a place and getting coordinates from there
  1: precise, which is a marker placed on the map by hand; leading to the creation of a location
  2: complex, which is mutiple markers, a shape or line or an image; stores the information in complex_data
  3: image, image placed by hand; stores information in complex_data';
