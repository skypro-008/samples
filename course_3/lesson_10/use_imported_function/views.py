from flask import request


class MainViews:

    def page_index(self):
        return request.values.get("name", "не задано")


main_views = MainViews()
