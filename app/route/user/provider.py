from app.api.base.base_sql import Sql


class Provider:
    """
    Класс для работы с авторизацией и регистрацией пользователей
    """
    @staticmethod
    def auth_user(args):
        """
        Авторизовать пользователя
        :param args:
        :return:
        """
        query = """
    select "id_user"
    from "users"
    where ("login" = '{login}'
      and "password" = '{password}'
      )
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def check_user(args):
        """
        Проверить существует ли пользователь
        :param args:
        :return:
        """
        query = """
  select 1
  from "users"
  where ("login" = '{login}'
    and "password" = '{password}'
    )
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def register_user(args):
        """
        Зарегистрировать пользователя
        :param args:
        :return:
        """
        query = """
    insert into "users"("login", "password", "is_admin", "id_profile") 
    VALUES ('{login}', 
    '{password}', 
    '{is_admin}',
    '{id_profile}')
    returning "id_user"
    """
        return Sql.exec(query=query, args=args)
