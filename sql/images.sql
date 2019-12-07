-- Table: public.images

-- DROP TABLE public.images;

CREATE TABLE public.images
(
  id_image integer NOT NULL DEFAULT nextval('images_id_image_seq'::regclass),
  id_stories integer,
  url text,
  "position" integer,
  description text,
  CONSTRAINT images_pk PRIMARY KEY (id_image)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.images
  OWNER TO postgres;

-- Index: public.images_id_image_uindex

-- DROP INDEX public.images_id_image_uindex;

CREATE UNIQUE INDEX images_id_image_uindex
  ON public.images
  USING btree
  (id_image);

