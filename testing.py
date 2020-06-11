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
    print('release')
    time.sleep(1)
    kit.stepper1.release()


def main():
    test1()


if __name__ == "__main__":
    main()

    



