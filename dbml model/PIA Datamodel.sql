CREATE TABLE "Image" (
  "id" int PRIMARY KEY,
  "oldnr" varchar,
  "signature" varchar,
  "title" varchar,
  "original_title" varchar,
  "date" varchar,
  "exact_date" date,
  "exact_time" time,
  "daterange_start" date,
  "daterange_end" date,
  "sequence_number" varchar,
  "subject" int,
  "comment" int,
  "geography" int,
  "object_type" int,
  "model" int
);

CREATE TABLE "Keyword" (
  "id" int PRIMARY KEY,
  "name" varchar,
  "description" varchar,
  "origin" varchar
);

CREATE TABLE "Images_Keywords" (
  "image_id" int,
  "keyword_id" int
);

CREATE TABLE "Subject" (
  "id" int PRIMARY KEY
);

CREATE TABLE "Comment" (
  "id" int PRIMARY KEY
);

CREATE TABLE "Geography" (
  "id" int PRIMARY KEY,
  "geonames_id" int,
  "geonames_url" varchar,
  "label" varchar
);

CREATE TABLE "ObjectType" (
  "id" int PRIMARY KEY,
  "label" varchar
);

CREATE TABLE "Model" (
  "id" int PRIMARY KEY,
  "label" varchar
);

CREATE TABLE "Person" (
  "id" int PRIMARY KEY,
  "name" varchar
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

CREATE TABLE "Album" (
  "id" int PRIMARY KEY
);

CREATE TABLE "Images_Album" (
  "image_id" int,
  "album_id" int
);

CREATE TABLE "Collection" (
  "id" int PRIMARY KEY
);

CREATE TABLE "Images_Collection" (
  "image_id" int,
  "collection_id" int
);

CREATE TABLE "Album_Collection" (
  "album_id" int,
  "collection_id" int
);

ALTER TABLE "Image" ADD FOREIGN KEY ("subject") REFERENCES "Subject" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("comment") REFERENCES "Comment" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("geography") REFERENCES "Geography" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("object_type") REFERENCES "ObjectType" ("id");

ALTER TABLE "Image" ADD FOREIGN KEY ("model") REFERENCES "Model" ("id");

ALTER TABLE "Images_Keywords" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_Keywords" ADD FOREIGN KEY ("keyword_id") REFERENCES "Keyword" ("id");

ALTER TABLE "Images_Content" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_Content" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Images_People" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_People" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Images_Copyright" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_Copyright" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Images_Album" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_Album" ADD FOREIGN KEY ("album_id") REFERENCES "Album" ("id");

ALTER TABLE "Images_Collection" ADD FOREIGN KEY ("image_id") REFERENCES "Image" ("id");

ALTER TABLE "Images_Collection" ADD FOREIGN KEY ("collection_id") REFERENCES "Collection" ("id");

ALTER TABLE "Album_Collection" ADD FOREIGN KEY ("album_id") REFERENCES "Album" ("id");

ALTER TABLE "Album_Collection" ADD FOREIGN KEY ("collection_id") REFERENCES "Collection" ("id");
