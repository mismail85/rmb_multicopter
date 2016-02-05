PACKET_HEADER1 = 0x02
PACKET_HEADER2 = 0xB5

REQUEST_CONFIG = 1
REQUEST_GYRO_ACC = 2

SET_CONFIG = 101

INFO_SUCCESS = 201
INFO_FAILURE = 202

from .serialmanager import SerialManager
from .serialwriter import SerialWriter
from .serialreader import SerialReader
