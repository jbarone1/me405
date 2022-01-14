"""! @file    main.py
     @brief   Sets sawtooth duty cycle for LED on Nucleo
     @details Program sets up timer and channel on Nucleo responsible for
              the LED. The program loops and sets brightness as a sawtooth
              wave, repeating after 5 seconds
     @author  Jack Barone
     @author  Luke Sandor
     @author  Jackson Meyers
     @date    1/4/2022
     @copyright (c) 2258 by Nobody and released under GNU Public License v3

"""


def led_setup():
    """!
    @brief     Sets up the led pin location, timer, and channel
    @details   Uses pyb library to setup hardware used for LED control
    @return    ch1 object 
    """
    pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer (2, freq=2000)
    ch1 = tim2.channel (1, pyb.Timer.PWM_INVERTED, pin=pinA0)
    return ch1

def led_brightness(ch1, bright):
    """!
    @brief         Responsible for setting the PWM of the LED
    @details       Function takes in a brightness value between 0 and 100, and sets the
                   the duty cycle for ch1
    @param ch1     ch1 object setup in led_setup()
    @param bright  desired duty cycle 
    """
    ch1.pulse_width_percent (bright)
   
if __name__ == "__main__":
    while(1):
        brightness = 0
        for brightness in range(100):
            led_brightness(led_setup(), brightness)
            pyb.delay(50)