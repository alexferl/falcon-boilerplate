# https://falcon.readthedocs.io/en/stable/user/faq.html#how-do-i-manage-my-database-connections


class Resource:
    def __init__(self, db):
        self._db = db
