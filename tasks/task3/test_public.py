import pytest

from .task import cipher


class Case:
    def __init__(self, name: str, s: str, k: int, character: str):
        self._name = name
        self.s = s
        self.k = k
        self.character = character

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        s = 'cute2dog3',
        k = 10,
        character = 'o'
    ),
    Case(
        name='base 2',
        s = 'no23',
        k = 5,
        character = 'n'
    ),
    Case(
        name='empty string',
        s = '',
        k = 5,
        character = None
    ),
    Case(
        name='no words',
        s = '23',
        k = 5,
        character = None
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = cipher(s = case.s, k = case.k)
    assert answer == case.character
