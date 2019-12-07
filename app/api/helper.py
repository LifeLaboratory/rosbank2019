from app.api.base import base_name as names
from app.api.base.base_sql import Sql


def get_id_user_by_profile(args):
    query = """
    select id_user from "users" where id_profile = {id_profile}
            """
    return Sql.exec(query=query, args=args)


def get_id_user_by_profiles(args):
    query = """
    select id_user from "users" where id_profile = any(array{id_profile})
            """
    return Sql.exec(query=query, args=args)


def get_admins(args):
    query = """
    select id_user from "users" where is_admin is TRUE
            """
    return Sql.exec(query=query, args=args)
