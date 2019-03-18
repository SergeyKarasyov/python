from datetime import datetime

import pytest

from pylib.date_module import str2datetime


def test_str2datetime():
    dateString = 'Jun 1 2005  1:33PM'
    dateToCompare = datetime.strptime(dateString, '%b %d %Y %I:%M%p')
    assert dateToCompare == str2datetime(dateString)
