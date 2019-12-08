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
with 
  count_is_feature as (
    select
      uf."id_user", 
    count(1) filter(where "is_web" is true) as "count_web",
    count(1) filter(where "is_android" is true) as "count_android"
  from
    user_features uf
  join features f on uf."id_features" = f."id_features"
  group by uf."id_user"
  ),
  count_is_statistic as (
    select
      uf."id_user", 
      uf."id_action", 
    count(1) filter(where "platform" = 'web') as "count_web",
    count(1) filter(where "platform" = 'android') as "count_android"
  from statistic_action uf
  group by uf."id_user", 
      uf."id_action"
  ),
  feature as (
    select
      uf."id_user",
      array_agg(json_build_object(
        'name', f."name",
        'is_android', uf."is_android",
        'is_web', uf."is_web", 
        'count_web', cif."count_web",
        'count_android', cif."count_android"
      )) array_f
    from
      user_features uf
    join features f on uf."id_features" = f."id_features"
    join count_is_statistic cif on cif."id_user" = uf."id_user" and "id_action" = uf."id_features"
    group by uf."id_user"
  ),
    actions_agg as (
      select
    id_profile,
    id_user,
    count(1) filter(where "platform" = 'web') as web,
    count(1) filter(where "platform" = 'android') as android,
    count(*) all_request
  from statistic_action sta
  join action ac on ac."id_action" = sta."id_action"
  group by id_profile, id_user
  order by 4 desc
    )

    select
      pr."id_profile",
      pr."description",
      array_agg(
        json_build_object(
          'id_user',u."id_user",
          'name', u."name",
          'feature', f.array_f,
          'web', act_agg.web,
          'android', act_agg.android,
          'all_request', act_agg.all_request
        )
      ) users
    from profile pr
    join users u on pr."id_profile" = u."id_profile"
    left join actions_agg act_agg on act_agg.id_profile = pr.id_profile and act_agg.id_user = u.id_user
    left join feature f on u."id_user" = f."id_user"
    group by pr.id_profile
  """
        return Sql.exec(query=query)
