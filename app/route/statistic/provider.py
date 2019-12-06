from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def statistic(args):
        query = """
    insert into "statistic_action"("id_user", "id_action", "platform")
    values ('{id_user}', '{id_action}', '{platform}'
      )
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_statistic(args):
        query = """
        select
          ac."names",
          count(1) filter(where "platform" = 'web') as web,
          count(1) filter(where "platform" = 'android') as android,
          count(*) all_request
        from statistic_action sta
        join action ac on ac."id_action" = sta."id_action"
        where "id_user" = '{id_user}'
        group by "names"
        order by 4 desc 
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_statistic_list():
        query = """
        select
          pr."id_profile",
          pr."description",
          array_agg(json_build_object('id_user',u."id_user", 'name', u."name") order by "name") users
        from profile pr
        join users u on pr."id_profile" = u."id_profile"
        group by pr.id_profile
        """
        return Sql.exec(query=query)
