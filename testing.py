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
    for i in range(300):
        # kit.stepper1.onestep()
        msg = 'move no {}'.format(i)
        print(msg)
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(0.01)
    
    time.sleep(1)
    
    for i in range(300):
        # kit.stepper1.onestep()
        msg = 'move no {}'.format(i)
        print(msg)
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        time.sleep(0.001)
    kit.stepper1.release()
    
    time.sleep(1)
    
    for i in range(300):
        # kit.stepper1.onestep()
        msg = 'move no {}'.format(i)
        print(msg)
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
        time.sleep(0.01)
    kit.stepper1.release()

    time.sleep(1)
    
    for i in range(300):
#         kit.stepper1.onestep()
        msg = 'move no {}'.format(i)
        print(msg)
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)
        time.sleep(0.01)
    kit.stepper1.release()
    
def open(steps):
    kit = MotorKit()
    for i in range(steps):
        msg = 'move no {}'.format(i)
        print(msg)
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)
        time.sleep(0.01)
    kit.stepper1.release()

def close(steps):
    kit = MotorKit()
    for i in range(steps):
        msg = 'move no {}'.format(i)
        print(msg)
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.MICROSTEP)
        time.sleep(0.01)
    kit.stepper1.release()
    


def main():
    # test1()
    # test2()
    
    open(800)
    
    time.sleep(2)
    
    close(800)
    

if __name__ == "__main__":
    main()
