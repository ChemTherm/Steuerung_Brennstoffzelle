# from TinkerForgeHelperLib.src.TinkerForgeHelperLib import TFH

from TinkerForgeHelperLib.tinkerforge_lib import TFH
from time import sleep

TFH("127.0.0.1", 4223, {})

sleep(200)
print("fertig")