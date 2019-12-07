-- Table: public.action_profile

-- DROP TABLE public.action_profile;

CREATE TABLE public.action_profile
(
  id_action integer,
  id_profile integer
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.action_profile
  OWNER TO postgres;
