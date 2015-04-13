
import time
from enum import Enum

#Status Enumeration
class Status(Enum):
	NO_DATA = 255 
	PENDING = 254
	FAILED = 2
	SUCCESS = 1

def write_command(adr, cmd):
	#Write to address
	
	#Wait at least 300ms
	sleep(0.3)

def read_command(adr, cmd):
	#read from address
	#Wait at least 300ms before the next command
	sleep(0.3)