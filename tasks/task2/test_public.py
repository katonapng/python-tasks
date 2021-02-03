import pytest

from .task import modified_string


class Case:
    def __init__(self, name: str, s: str, modified: str):
        self._name = name
        self.s = s
        self.modified = modified

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        s = 'abbc',
        modified = 'abcb'
    ),
    Case(
        name='none',
        s = 'bbbc',
        modified = None
    ),
    Case(
        name='empty string',
        s = '',
        modified = ''
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    answer = modified_string(s=case.s)
    assert answer == case.modified
