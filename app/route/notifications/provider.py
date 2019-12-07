from app.api.base.base_sql import Sql


class Provider:
    """
    Класс для работы с уведомлеиями в бд
    """
    @staticmethod
    def insert_notification(args):
        """
        Добавить уведомление
        :param args:
        :return:
        """
        query = """
  insert into notifications ("name", "url", "id_stories") 
  VALUES ('{name}', '{url}', {id_stories})
  returning "id_notification"
  """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_notifications_users(args):
        """
        Отправить уведомление пользователю
        :param args:
        :return:
        """
        query = """
  insert into notifications_users ("id_notification", "id_user", "status", "time", "active") 
  VALUES ('{id_notification}', '{id_user}', '{status}', NOW(), True)
  """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_notifications(args):
        """
        Получить уведомления для пользователя
        :param args:
        :return:
        """
        query = """
  select notifications.* from notifications_users
  join notifications on notifications.id_notification = notifications_users.id_notification
  where id_user = {id_user} and active is True and NOW() > time
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
