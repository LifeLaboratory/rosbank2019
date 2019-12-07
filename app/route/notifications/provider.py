from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def insert_notification(args):
        query = """
  insert into notifications ("name", "url") 
  VALUES ('{name}', '{url}')
  returning "id_notification"
  """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_notifications_users(args):
        query = """
  insert into notifications_users ("id_notification", "id_user", "status", "time", "active") 
  VALUES ('{id_notification}', '{id_user}', '{status}', NOW(), True)
  """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_notifications(args):
        query = """
  select notifications.* from notifications_users
  join notifications on notifications.id_notification = notifications_users.id_notification
  where id_user = {id_user} and active is True and NOW() > time
  """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_profile(args):
        query = """
  update profile
    set "description" = '{description}'
    where "id_profile" = {id_profile}
    """
        return Sql.exec(query=query, args=args)
