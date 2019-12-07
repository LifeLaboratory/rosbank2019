-- Table: public.notifications_users

-- DROP TABLE public.notifications_users;

CREATE TABLE public.notifications_users
(
  id_notifications_users integer NOT NULL DEFAULT nextval('notifications_users_id_notifications_users_seq'::regclass),
  id_notification integer,
  id_user integer,
  status text,
  "time" timestamp without time zone,
  active boolean,
  CONSTRAINT notifications_users_pk PRIMARY KEY (id_notifications_users)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.notifications_users
  OWNER TO postgres;

-- Index: public.notifications_users_id_notifications_users_uindex

-- DROP INDEX public.notifications_users_id_notifications_users_uindex;

CREATE UNIQUE INDEX notifications_users_id_notifications_users_uindex
  ON public.notifications_users
  USING btree
  (id_notifications_users);

