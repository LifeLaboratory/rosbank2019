from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def auth_user(args):
        query = """
    select "@user"
    from "users"
    where ("login" = '{login}'
      and "password" = '{password}'
      )
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def check_user(args):
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
        query = """
    insert into "users"("login", "password", "fio", "description", "photo", "email", "number") 
    VALUES ('{login}', 
    '{password}', 
    '{fio}',
    '{description}',
    '{photo}', 
    '{email}', 
    '{number}')
    returning "@user"
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_user_id(args):
        query = """
    select "@user"
    from "users"
    where "login" = '{login}'
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_user_info(args):
        query = """
            select *
            from "users"
            where "@user" = '{@login}'
                        """
        return Sql.exec(query=query, args=args)
