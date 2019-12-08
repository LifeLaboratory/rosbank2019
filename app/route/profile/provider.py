from app.api.base.base_sql import Sql


class Provider:
    """
    Класс для работы с профилем в бд
    """
    @staticmethod
    def get_profile(args):
        """
        Получить профиль пользователя
        :param args:
        :return:
        """
        query = """
  select 
    *
  from profile
  """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_profile(args):
        """
        Обновить профиль пользователя
        :param args:
        :return:
        """
        query = """
  update profile
    set "description" = '{description}'
    where "id_profile" = {id_profile}
    """
        return Sql.exec(query=query, args=args)
