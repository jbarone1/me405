import pyb

class Encoder:
    ''' @brief Interface with quadrature encoders
        @details Python class for the encoder 
    '''
    def __init__(self,pin1,pin2,timeIDX):
        ''' @brief Constructs an encoder object
            @param pin1     Pin on Nucleo for encoder channel 1
            @param pin2     Pin on Nucleo for encoder channel 2
            @param timeIDX  Timer number associated with encoder
        '''
        self.period = 2**16-1
        self.tim = pyb.Timer(timeIDX,prescaler=0,period=self.period)
        self.ch1 = self.tim.channel(1,pyb.Timer.ENC_A,pin=pin1)
        self.ch2 = self.tim.channel(2,pyb.Timer.ENC_B,pin=pin2)
        self.position = 0
        self.delta = 0
        self.currentT = 0
        self.lastT = 0
        
    def update(self):
        ''' @brief Updates encoder position and delta
        '''
        self.currentT = self.tim.counter()
        self.delta = self.currentT - self.lastT
                
        if self.delta >= self.period/2:
            self.delta -= self.period
        elif self.delta <= -self.period/2:
            self.delta += self.period
        else:
            pass
                
        self.position += self.delta
        self.lastT = self.currentT

    def get_position(self):
        ''' @brief Returns encoder position
            @return The position of the encoder shaft
        '''
        return self.position


    def set_position(self, position):
        ''' @brief Sets encoder position
            @param position The new position of the encoder shaft
        '''
        self.position = position

    def get_delta(self):
        ''' @brief Returns encoder delta
            @return The change in position of the encoder shaft
                    between the two most recent updates
        '''
        return self.delta