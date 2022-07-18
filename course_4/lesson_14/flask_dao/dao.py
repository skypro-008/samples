
class SampleDAO:

    def __init__(self, connection):
        self.connection = connection

    def get_all(self):
        """ Получает список всех элементов """

        # формируем запрос
        query = "SELECT * FROM shop"

        # получаем курсор
        cursor = self.connection.cursor()

        #  выполняем запрос
        cursor.execute(query)
        result = cursor.fetchall()
        return result



