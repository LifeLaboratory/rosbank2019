from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_profile(args):
        query = """
        select 
          users.*
          , description
        from "users"
        left join profile on profile.id_profile = users.id_profile
        where "id_user" = {id_user}
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
