from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_feature_user(args):
        query = """
  select 
    *
  from "user_features" uf
  join "features" f using(id_features)
  where "id_user" = {id_user}
                  """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_feature(args):
        query = """
    insert into "features" ("name") 
    VALUES ('{name}')
    returning "id_features"
                  """
        return Sql.exec(query=query, args=args)
