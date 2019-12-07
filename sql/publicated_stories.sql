-- Table: public.publicated_stories

-- DROP TABLE public.publicated_stories;

CREATE TABLE public.publicated_stories
(
  id_publicated_stories integer NOT NULL DEFAULT nextval('publicated_stories_id_publicated_stories_seq'::regclass),
  id_user integer,
  id_stories integer,
  CONSTRAINT publicated_stories_pk PRIMARY KEY (id_publicated_stories)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.publicated_stories
  OWNER TO postgres;

-- Index: public.publicated_stories_id_publicated_stories_uindex

-- DROP INDEX public.publicated_stories_id_publicated_stories_uindex;

CREATE UNIQUE INDEX publicated_stories_id_publicated_stories_uindex
  ON public.publicated_stories
  USING btree
  (id_publicated_stories);

-- Index: public.publicated_stories_id_user_id_stories_uindex

-- DROP INDEX public.publicated_stories_id_user_id_stories_uindex;

CREATE UNIQUE INDEX publicated_stories_id_user_id_stories_uindex
  ON public.publicated_stories
  USING btree
  (id_user, id_stories);

