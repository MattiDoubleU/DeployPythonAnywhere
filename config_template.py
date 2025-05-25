config = {
    'db_host': "Luciernagas.mysql.pythonanywhere-services.com",
    'db_user': "Luciernagas",
    'db_password': "rootroot",
    'db_name': "Luciernagas$Expenses"
}

def get(key, default=None):
    return config.get(key, default)