from unittest.mock import MagicMock


class Inner:

    def _foo(self):
        return "real inner method"

    def boo(self):
        return self._foo()

inner = Inner()

inner._foo = MagicMock(return_value="fake inner method")

print(inner.boo())
