import time

import OpenWebPortal as OWP

#OWP.start()
OWP.start()


a=OWP.OWP("Lights", True, "bool")
b=OWP.OWP("Sound", False, "bool")
c=OWP.OWP("Volume", 10, "int")
d=OWP.OWP("Name", "tester", "string")
e=OWP.OWP("colour", "#555555", "colour")

while True:
    time.sleep(5)
