from app.api.base.base_sql import Sql


class Provider:
    """
    Класс для работы с функционалом в бд
    """
    @staticmethod
    def get_feature_user(args):
        """
        Получить используемый функционал по ид пользователя
        :param args:
        :return:
        """
        query = """
  select 
    uf.*
    , f.*
    , us."name" as user_name
  from user_features uf
  join features f using("id_features")
  join users us using("id_user")
  where "id_user" = {id_user}
  """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_feature(args):
        """
        Добавить функионал
        :param args:
        :return:
        """
        query = """
  insert into features ("name") 
  VALUES ('{name}')
  returning "id_features"
  """
        return Sql.exec(query=query, args=args)
