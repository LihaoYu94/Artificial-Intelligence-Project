import random
import math

class MDP:
    
    def __init__(self, 
                 ball_x=None,
                 ball_y=None,
                 velocity_x=None,
                 velocity_y=None,
                 paddle_y=None,
                 ):
        '''
        Setup MDP with the initial values provided.
        '''
        self.create_state(
            ball_x=ball_x,
            ball_y=ball_y,
            velocity_x=velocity_x,
            velocity_y=velocity_y,
            paddle_y=paddle_y,

        )
        
        # the agent can choose between 3 actions - stay, up or down respectively.
        self.actions = [0, 0.04, -0.04]
        
    def create_state(self,
              ball_x=None,
              ball_y=None,
              velocity_x=None,
              velocity_y=None,
              paddle_y=None):
        '''
        Helper function for the initializer. Initialize member variables with provided or default values.
        '''
        self.paddle_height = 0.2
        self.ball_x = ball_x if ball_x != None else 0.5
        self.ball_y = ball_y if ball_y != None else 0.5
        self.velocity_x = velocity_x if velocity_x != None else 0.03
        self.velocity_y = velocity_y if velocity_y != None else 0.01
        self.paddle_y = 0.5

        self.d_ball_x = None
        self.d_ball_y = None
        self.d_velocity_x = None
        self.d_velocity_y = None
        self.d_paddle_y = None
        self.cur_state = None



    
    def simulate_one_time_step(self, action_selected):
        '''
        :param action_selected - Current action to execute.
        Perform the action on the current continuous state.
        '''

        # Your Code Goes Here!
        reward = 0
        end_status = False 
        
        #update paddle
        self.paddle_y += self.actions[action_selected]

        if self.paddle_y < 0:
          self.paddle_y = 0

        if self.paddle_y > 1-0.2:
          self.paddle_y = 1-0.2

        self.ball_x += self.velocity_x 
        self.ball_y += self.velocity_y

        #ball y is always 0 < y < 1
        #x is always 0 < x 
        if self.ball_y < 0:
            self.ball_y = -self.ball_y
            self.velocity_y = -self.velocity_y

        if self.ball_y > 1:
            self.ball_y = 2 - self.ball_y
            self.velocity_y = -self.velocity_y

        if self.ball_x < 0:
            self.ball_x = -self.ball_x
            self.velocity_x = -self.velocity_x
        
        if self.ball_x >= 1 and self.ball_y >= self.paddle_y and self.ball_y <= self.paddle_y + 0.2:  
            self.ball_x = 2 - self.ball_x 
            u = random.uniform(-0.015, 0.015)
            v = random.uniform(-0.03, 0.03)
            self.velocity_x = -self.velocity_x + u
            self.velocity_y = -self.velocity_y + v
            
            # vecolity constrains on velocity x
                          
            reward = 1

        elif self.ball_x >= 1:
            self.ball_x = 1
            reward = -1
            end_status = True
            
            
        if abs(self.velocity_x) <= 0.03:
            if self.velocity_x < 0:
                self.velocity_x = -0.04
            else:
                self.velocity_x =  0.04

        if abs(self.velocity_y) >= 1:
            if self.velocity_y > 0:
                self.velocity_y = 1
            else:
                self.velocity_y = -1

        if abs(self.velocity_x) >= 1:
            if self.velocity_x > 0:
                self.velocity_x = 1
            else: 
                self.velocity_x = -1
        
        return end_status, reward
    
    def discretize_state(self):
        '''
        Convert the current continuous state to a discrete state.
        '''
        # Your Code Goes Here!

        if self.velocity_x >= 0:
            self.d_velocity_x = 1
        else:
            self.d_velocity_x = -1

        if self.velocity_y >= 0.015:
            self.d_velocity_y = 1
        elif self.velocity_y <= -0.015:
            self.d_velocity_y = -1
        else:
            self.d_velocity_y = 0

        self.d_ball_x = self.ball_x * 12
        self.d_ball_y = self.ball_y * 12

        self.d_ball_x = math.floor(self.d_ball_x)
        self.d_ball_y = math.floor(self.d_ball_y)

        if self.d_ball_x >= 12:
            self.d_ball_x = 11

        if self.d_ball_y >= 12:
            self.d_ball_y = 11

        temp = 12 * self.paddle_y / (1 - self.paddle_height)
        self.d_paddle_y = math.floor(temp)

        if self.d_paddle_y >= 12:
            self.d_paddle_y = 11

        pass

    def print_state(self):
        print self.ball_x, self.ball_y, self.velocity_x, self.velocity_y, self.paddle_y
        pass

    def print_d_state(self):
        print self.d_ball_x, self.d_ball_y, self.d_velocity_x, self.d_velocity_y, self.d_paddle_y
        pass

    def find_state(self):
        #find the current discrete state of game
        return (self.d_ball_x, self.d_ball_y, self.d_velocity_x, self.d_velocity_y, self.d_paddle_y)









