
import time
from enum import Enum


class Status(Enum):
	"""Status enumeration"""
    NO_DATA = 255
    PENDING = 254
    FAILED = 2
    SUCCESS = 1

def continuous_mode(enabled=0):
	if (enabled == 0):


def write_command(address, command):
	""" asnoteuhaoe """
    # Write to address

    # Wait at least 300ms
    time.sleep(0.3)


def read_command(address, command):
    """ dosucaoeuhsd """
    #read from address
    #Wait at least 300ms before the next command
    time.sleep(0.3)


class UART():
	"""
	To handle serial comms of over UART bus
	"""


class I2C():
	"""
	To handle serial comms using the I2C protocol
	"""




