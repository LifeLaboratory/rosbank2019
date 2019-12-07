-- Table: public.profile

-- DROP TABLE public.profile;

CREATE TABLE public.profile
(
  id_profile integer NOT NULL DEFAULT nextval('profile_id_profile_seq'::regclass),
  description text,
  CONSTRAINT profile_pk PRIMARY KEY (id_profile)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.profile
  OWNER TO postgres;

-- Index: public.profile_id_profile_uindex

-- DROP INDEX public.profile_id_profile_uindex;

CREATE UNIQUE INDEX profile_id_profile_uindex
  ON public.profile
  USING btree
  (id_profile);

