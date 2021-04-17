import time

import OpenWebPortal as OWP

#OWP.start()
OWP.start()


x=OWP.OWP("Lights", True, "bool")
y=OWP.OWP("Sound", False, "bool")
z=OWP.OWP("volume", 10, "int")

while True:
    time.sleep(5)
