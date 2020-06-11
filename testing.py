import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper


def test1():
    kit = MotorKit()
    print('onestep')
    time.sleep(1)
    kit.stepper1.onestep()
    print('next step')
    time.sleep(2)
    kit.stepper1.onestep()
    print('3rd step')
    time.sleep(1)
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    print('release')
    time.sleep(1)
    kit.stepper1.release()

def test2():
    kit = MotorKit()
    for i in range(600):
        # kit.stepper1.onestep()
        msg = 'move no {}'.format(i)
        print(msg)
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)
    
    time.sleep(1)
    
    for i in range(600):
        # kit.stepper1.onestep()
        msg = 'move no {}'.format(i)
        print(msg)
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleep(0.01)
    kit.stepper1.release()



def main():
    #test1()
    test2()

if __name__ == "__main__":
    main()
