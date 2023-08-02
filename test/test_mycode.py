from mycode import log_something

import ray


def test_logging_with_ray(caplog):
    log_something()
    assert len(caplog.messages) == 1
