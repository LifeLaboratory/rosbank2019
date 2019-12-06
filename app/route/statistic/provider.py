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
