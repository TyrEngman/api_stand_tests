import configuration
import requests
import data

def post_new_user(user_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.USERS_PATH,
        json=user_body
    )

def get_users_table():
    return requests.get(
        configuration.URL_SERVICE + configuration.USERS_TABLE_PATH
    )
