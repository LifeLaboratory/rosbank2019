from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_profile(args):
        query = """
        select 
          "@user"
          , "fio"
          , "description"
          , "photo"
          , "email"
          , "number"
        from "users"
        where "@user" = {user}
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_profile(args):
        query = """
        update "users" 
          set "fio" = '{fio}'
            , "description" = '{description}'
            , "photo" = '{photo}'
            , "email" = '{email}'
            , "number" = '{number}'
          where "@user" = {user}
        """
        return Sql.exec(query=query, args=args)
