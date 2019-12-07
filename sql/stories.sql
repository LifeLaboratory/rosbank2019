-- Table: public.stories

-- DROP TABLE public.stories;

CREATE TABLE public.stories
(
  id_stories integer NOT NULL DEFAULT nextval('stories_id_stories_seq'::regclass),
  id_user integer,
  id_creator integer,
  type integer DEFAULT 1,
  CONSTRAINT stories_pk PRIMARY KEY (id_stories)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.stories
  OWNER TO postgres;

-- Index: public.stories_id_stories_uindex

-- DROP INDEX public.stories_id_stories_uindex;

CREATE UNIQUE INDEX stories_id_stories_uindex
  ON public.stories
  USING btree
  (id_stories);

