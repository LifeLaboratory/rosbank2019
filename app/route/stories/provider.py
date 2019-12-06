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
    def insert_stories(args):
        query = """
        insert into "stories" ("id_user", "id_creator")
        VALUES ({id_user}, {id_user})
        returning id_stories 
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_image(args):
        query = """
        insert into "images" ("id_stories", "url", position)
        VALUES ({id_stories}, '{url}', {position}) 
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def select_status(args):
        query = """
        select True from step_action where id_user = {id_user} and id_stories = {id_stories}
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_status(args):
        query = """
        insert into "step_action" ("id_stories", "id_user", "is_open", "is_view", "time", "is_like") 
    VALUES ({id_stories}, {id_user}, {is_open}, {is_view}, NOW(), {is_like}::boolean)
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_status(args):
        query = """
        update "step_action" 
          set "is_open" = {is_open}, 
              "is_view" = {is_view},
              "is_like" = {is_like}::boolean,
              "time" = NOW()
          where "id_user" = {id_user} and "id_stories" = {id_stories}
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
