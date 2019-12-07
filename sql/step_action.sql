-- Table: public.step_action

-- DROP TABLE public.step_action;

CREATE TABLE public.step_action
(
  id_step_action integer NOT NULL DEFAULT nextval('step_action_id_step_action_seq'::regclass),
  id_stories integer,
  is_open boolean,
  id_user integer,
  is_view boolean,
  "time" timestamp without time zone,
  is_like boolean,
  CONSTRAINT step_action_pk PRIMARY KEY (id_step_action)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.step_action
  OWNER TO postgres;

-- Index: public.step_action_id_step_action_uindex

-- DROP INDEX public.step_action_id_step_action_uindex;

CREATE UNIQUE INDEX step_action_id_step_action_uindex
  ON public.step_action
  USING btree
  (id_step_action);

-- Index: public.step_action_id_stories_uindex

-- DROP INDEX public.step_action_id_stories_uindex;

CREATE UNIQUE INDEX step_action_id_stories_uindex
  ON public.step_action
  USING btree
  (id_stories, id_user);

