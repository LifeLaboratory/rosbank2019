-- Table: public.statistic_action

-- DROP TABLE public.statistic_action;

CREATE TABLE public.statistic_action
(
  id_statistic_action integer NOT NULL DEFAULT nextval('statistic_action_id_statistic_action_seq'::regclass),
  id_action integer,
  id_user integer,
  platform text,
  CONSTRAINT statistic_action_pk PRIMARY KEY (id_statistic_action)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.statistic_action
  OWNER TO postgres;

-- Index: public.statistic_action_id_statistic_action_uindex

-- DROP INDEX public.statistic_action_id_statistic_action_uindex;

CREATE UNIQUE INDEX statistic_action_id_statistic_action_uindex
  ON public.statistic_action
  USING btree
  (id_statistic_action);

