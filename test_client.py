from client import getRatio
import pytest

def test_getRatio():
    with pytest.raises(ZeroDivisionError):
        getRatio(3/0)
    
