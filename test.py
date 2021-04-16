import OpenWebPortal as OWP
import time

#OWP.start()
OWP.start()


x=OWP.OWP("Lights", True)
y=OWP.OWP("Sound", False)

while True:
    time.sleep(5)
    print("x" + str(x.value))
    print("y" + str(y.value))