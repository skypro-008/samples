class SimpleDAO:

    def __init__(self):
        self._data = []
        self._create_data()


    def _create_data(self):
        data = [
            {
                "pk": 1,
                "full_name": "Jane Snake",
                "skills": ["Python", "Go", "Linux"]
            },
            {
                "pk": 2,
                "full_name": "Sheri Torres",
                "skills": ["Java", "Swify", "Fortran", "Basic"]
            },
            {
                "pk": 3,
                "full_name": "Burt Stein",
                "skills": ["Planning", "Negotiation", "Management", "Sales"]
            },
            {
                "pk": 4,
                "full_name": "Bauer Adkins",
                "skills": ["HTML", "CSS", "JavaScript", "React", "Node.js"]
            }
        ]
        self._data = data

    def get_all(self):
        return self._data

    def get_by_pk(self, pk):
        data = self._data
        for element in data:
            if element['pk'] == pk:
                return element

