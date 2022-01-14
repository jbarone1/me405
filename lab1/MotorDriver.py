class MotorDriver:
    '''! 
    This class implements a motor driver for an ME405 kit. 
    '''

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        '''! 
        Creates a motor driver by initializing GPIO
        pins and turning the motor off for safety. 
        @param en_pin (There will be several of these)
        '''
        tim = pyb.Timer(timer,freq=2000)
        in1 = pyb.         pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
        tim2 = pyb.Timer (2, freq=2000)
        ch1 = tim2.channel (1, pyb.Timer.PWM_INVERTED, pin=pinA0)

    def set_duty_cycle (self, level):
        '''!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        '''
        print ('Setting duty cycle to ' + str (level))