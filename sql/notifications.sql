-- Table: public.notifications

-- DROP TABLE public.notifications;

CREATE TABLE public.notifications
(
  id_notification integer NOT NULL DEFAULT nextval('notifications_id_notification_seq'::regclass),
  name text,
  url text,
  id_stories integer,
  CONSTRAINT notifications_pk PRIMARY KEY (id_notification)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.notifications
  OWNER TO postgres;

-- Index: public.notifications_id_notification_uindex

-- DROP INDEX public.notifications_id_notification_uindex;

CREATE UNIQUE INDEX notifications_id_notification_uindex
  ON public.notifications
  USING btree
  (id_notification);

