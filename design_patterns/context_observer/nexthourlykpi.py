from observer.AbsObserver import AbsObserver
from logger import LOGGER

class NextHourlyKpi(AbsObserver):
    _open_tickets = -1
    _closed_tickets = -1
    _new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self._open_tickets = self._kpis.open_tickets
        self._closed_tickets = self._kpis.closed_tickets
        self._new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        LOGGER.info('forecasted open tasks: {}'.format(self._open_tickets))
        LOGGER.info('forecasted new tasks: {}'.format(self._new_tickets))
        LOGGER.info('forecasted closed tasks: {}'.format(self._closed_tickets))


