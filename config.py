config = {
    'db_host': "localhost",
    'db_user': "root",
    'db_password': "",
    'db_name': "expenses"
}

def get(key, default=None):
    return config.get(key, default)