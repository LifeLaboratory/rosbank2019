from app.api.base import base_name as names
from app.api.base.base_sql import Sql


def get_id_user_by_profile(args):
    """
    Получить список ид пользователей по ид профиля
    :param args:
    :return:
    """
    query = """
    select id_user from "users" where id_profile = {id_profile}
            """
    return Sql.exec(query=query, args=args)


def get_all_profile():
    """
    Получить список всех профайлов
    :return:
    """
    query = """
    select distinct id_profile 
    from "users"
    """
    return Sql.exec(query=query)


def get_id_user_by_profiles(args):
    """
    Массовый метод получения списка ид пользователей по сипску ид профиля
    :param args:
    :return:
    """
    query = """
    select id_user from "users" where id_profile = any(array{id_profile})
            """
    return Sql.exec(query=query, args=args)


def get_admins(args):
    """
    Получить список ид пользователей являющихся администраторами
    :param args:
    :return:
    """
    query = """
    select id_user from "users" where is_admin is TRUE
            """
    return Sql.exec(query=query, args=args)


def get_admins_ids(args):
    """
    Метод возвращает список id администраторов
    :param args:
    :return:
    """
    result = []
    admins_ids = get_admins(args)
    for admin_id in admins_ids:
        result.append(admin_id.get(names.ID_USER))
    return result
