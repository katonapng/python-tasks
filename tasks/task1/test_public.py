import pytest

from .task import good_string


class Case:
    def __init__(self, name: str, n: int, k: int, s: str):
        self._name = name
        self.n = n
        self.k = k
        self.s = s

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name = 'base',
        n = 3,
        k = 4,
        s = 'dog'
    ),
    Case(
        name = 'base 2',
        n = 1,
        k = 3,
        s = 'o'
    ),
    Case(
        name = 'none',
        n = 1,
        k = 4,
        s = None
    ),
    Case(
        name = 'empty string',
        n = 0,
        k = 4,
        s = None
    ),
    Case(
        name = 'k = 0',
        n = 1,
        k = 0,
        s = None
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = good_string(n=case.n, k=case.k)
    assert answer == case.s

