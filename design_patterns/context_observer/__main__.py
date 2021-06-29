from kpis import KPIs
from hourlykpi import HourlyKpi
from nexthourlykpi import NextHourlyKpi
from logger import LOGGER


kpis = KPIs()
currentKPIs = HourlyKpi(kpis)
currentKPIs = NextHourlyKpi(kpis)

kpis.set_kpis(10,10,10)
kpis.set_kpis(1,1,1)
kpis.set_kpis(50,50,1)
LOGGER.info("detach")
kpis.detach(currentKPIs)
kpis.set_kpis(100,111,222)
