from app.api.base.base_sql import Sql


class Provider:
    """
    Класс для работы со статистикой в бд
    """
    @staticmethod
    def statistic(args):
        """
        Добавить статистику в бд
        :param args:
        :return:
        """
        query = """
  insert into statistic_action("id_user", "id_action", "platform")
  values ({id_user}, {id_action}, '{platform}')
  """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_statistic(args):
        """
        Получить статистику
        :param args:
        :return:
        """
        query = """
  select
    ac."names",
    count(1) filter(where "platform" = 'web') as web,
    count(1) filter(where "platform" = 'android') as android,
    count(*) all_request
  from statistic_action sta
  join action ac on ac."id_action" = sta."id_action"
  where "id_user" = {id_user}
  group by "names"
  order by 4 desc
  """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_statistic_list():
        """
        Получить всю статистику по пользователям
        :return:
        """
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
