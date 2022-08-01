class ConnectionError(Exception):
    pass


class DatabaseConnection:

    def __init__(self) -> None:
        self._fl_connection_open = False

    def connect(self, login=None, password=None):
        self._fl_connection_open = True
        raise ConnectionError

    def close(self):
        self._fl_connection_open = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

with DatabaseConnection() as conn:
    conn.connect()