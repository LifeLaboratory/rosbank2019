-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE public.users
(
  id_user integer NOT NULL DEFAULT nextval('users_id_user_seq'::regclass),
  login text,
  password text,
  is_admin boolean,
  id_profile integer,
  name text,
  CONSTRAINT users_pk PRIMARY KEY (id_user)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.users
  OWNER TO postgres;

-- Index: public.users_id_user_uindex

-- DROP INDEX public.users_id_user_uindex;

CREATE UNIQUE INDEX users_id_user_uindex
  ON public.users
  USING btree
  (id_user);

