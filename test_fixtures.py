import pytest


class Maithani:

    def where_is_aniket(self):
        return "PyDelhi Conf 2017"


@pytest.fixture
def pydelhi_conf():
    return Maithani()


def test_where_is_aniket(pydelhi_conf):
    where = pydelhi_conf.where_is_aniket()
    assert where == "PyDelhi Conf 2017"
