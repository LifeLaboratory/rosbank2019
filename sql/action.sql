-- Table: public.action

-- DROP TABLE public.action;

CREATE TABLE public.action
(
  id_action integer NOT NULL DEFAULT nextval('action_id_action_seq'::regclass),
  description text,
  names text,
  id_profile integer,
  CONSTRAINT action_pk PRIMARY KEY (id_action)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.action
  OWNER TO postgres;

-- Index: public.action_id_action_uindex

-- DROP INDEX public.action_id_action_uindex;

CREATE UNIQUE INDEX action_id_action_uindex
  ON public.action
  USING btree
  (id_action);

