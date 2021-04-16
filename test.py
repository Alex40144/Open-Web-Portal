import OpenWebPortal as OWP
import time

OWP.start()


x=OWP.OWP("Lights", True)

while True:
    time.sleep(5)
    print(x.value)