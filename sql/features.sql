-- Table: public.features

-- DROP TABLE public.features;

CREATE TABLE public.features
(
  id_features integer NOT NULL DEFAULT nextval('features_id_features_seq'::regclass),
  name text,
  CONSTRAINT features_pkey PRIMARY KEY (id_features)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.features
  OWNER TO postgres;
