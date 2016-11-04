"""
# timd a simplified way to time your python applications

Timd provides a simple way of timing segments of your code by providing a single
class "Measure" that does two things:
    1. It writes the execution duration of your code as a log message (at info
        level)
    2. It stores the execution time for later evaluation

## Examples

The following is some setup code:

    >>> import sys
    >>> sys.stderr = sys.stdout
    >>> import logging


### Example 1: Using context manager for logging

timd is best illustrated using examples

    >>> from timd import Measure
    >>> logging.basicConfig(level=logging.INFO)
    >>> with Measure():
    ...     x = sum([4]*1000)                               # doctest: +ELLIPSIS
    INFO:root:Execution took ...s


### Example 2: Using decorator version for logging

We can also decorate functions with a `Measure`:

    >>> from timd import Measure
    >>> @Measure()
    ... def myfunction():
    ...     return sum([4]*1000)
    >>> print(myfunction())                                 # doctest: +ELLIPSIS
    INFO:root:Execution took ...s
    4000

Note that every time my function is called, we will receive a log message.


### Example 3: Using multiple `Measure` objects to track times

In some cases, we want to track times associated with different types of
operations. This following example illustrates a more complex use of
different `Measure` objects:

    >>> from timd import Measure
    >>> logger = logging.getLogger('times')
    >>> trackers = {'printing': Measure('Printing took {}s', logger),
    ...             'logical operations': Measure('Logical operation took {}s',
    ...                                           logger)}
    >>> with trackers['printing']:
    ...     print('Starting')                               # doctest: +ELLIPSIS
    Starting
    INFO:times:Printing took ...s
    >>> t = trackers['printing']
    >>> @t
    ... def show_formatted(c):
    ...     print('The condition was {}'.format(c))
    >>> for x in range(3):
    ...     with trackers['logical operations']:
    ...         condition = x % 3 == 0
    ...     show_formatted(condition)                       # doctest: +ELLIPSIS
    INFO:times:Logical operation took ...s
    The condition was True
    INFO:times:Printing took ...s
    INFO:times:Logical operation took ...s
    The condition was False
    INFO:times:Printing took ...s
    INFO:times:Logical operation took ...s
    The condition was False
    INFO:times:Printing took ...s

Note that we defined a separate logger for our time measurements, so that we can
use the functionality of the `logging` module to send timing statements to e.g.
a separate logfile. Furthermore, each logger stores information about it
tracked:

    >>> total_printing = sum(trackers['printing'].times)
    >>> total_logic = sum(trackers['logical operations'].times)
    >>> print('Time spent printing: {}s, Time spent with logic: {}s'.format(
    ...     total_printing, total_logic))                   # doctest: +ELLIPSIS
    Time spent printing: ...s, Time spent with logic: ...s
"""

__version__ = '0.0.1'

from timd.measure import Measure

if __name__ == "__main__":
    import doctest
    doctest.testmod()
