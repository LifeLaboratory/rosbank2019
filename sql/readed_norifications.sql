-- Table: public.readed_norifications

-- DROP TABLE public.readed_norifications;

CREATE TABLE public.readed_norifications
(
  id_readed_norifications integer,
  id_norifications integer,
  id_user integer,
  status text
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.readed_norifications
  OWNER TO postgres;
