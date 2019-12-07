-- Table: public.user_features

-- DROP TABLE public.user_features;

CREATE TABLE public.user_features
(
  id_features integer,
  id_user integer,
  is_android boolean DEFAULT false,
  is_web boolean DEFAULT false
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.user_features
  OWNER TO postgres;
