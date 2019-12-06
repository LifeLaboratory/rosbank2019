from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_profile(args):
        query = """
        select 
          *
        from "profile"
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_profile(args):
        query = """
        update "profile" 
          set "description" = '{description}'
          where "id_profile" = {id_profile}
        """
        return Sql.exec(query=query, args=args)
