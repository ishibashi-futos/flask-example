import pytest
import utils

def test_ok_add():
  result = utils.add(1, 2)
  assert result == 3
