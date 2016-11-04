import time
import logging


class Measure(object):

    def __init__(self, msg='Execution took {}s', logger=logging):
        self.msg = msg
        self.logger = logger
        self.times = []
        self.t0 = None

    def __enter__(self):
        self.t0 = time.time()

    def __exit__(self, *args):
        dt = time.time() - self.t0
        self.t0 = None
        self.times.append(dt)
        self.logger.info(self.msg.format(dt))

    def __call__(self, fun):

        def newfun(*args, **kwargs):
            with self:
                return fun(*args, **kwargs)

        return newfun
