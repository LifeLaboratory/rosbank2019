from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def publicate_storie(args):
        query = """
        insert into "publicated_stories" ("id_stories", "id_user") 
    VALUES ({id_stories}, {id_user})
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_notifications_users(args):
        query = """
        insert into "notifications_users" ("id_notification", "id_user", "status") 
    VALUES ('{id_notification}', '{id_user}', '{status}')
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_notifications(args):
        query = """
        select notifications.* from notifications_users
        join notifications on notifications.id_notification = notifications_users.id_notification
        where id_user = {id_user}
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
