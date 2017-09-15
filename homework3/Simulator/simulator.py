import random
import statistics
from MDP.MDP import MDP

class Simulator:
    
    def __init__(self, num_games=0, alpha_value=0, gamma_value=0, epsilon_value=0):
        '''
        Setup the Simulator with the provided values.
        :param num_games - number of games to be trained on.
        :param alpha_value - 1/alpha_value is the decay constant.
        :param gamma_value - Discount Factor.
        :param epsilon_value - Probability value for the epsilon-greedy approach.
        '''
        self.num_games = num_games       
        self.epsilon_value = epsilon_value       
        self.alpha_value = alpha_value       
        self.gamma_val = gamma_value

        # Your Code Goes Here!
        self.action_list = [0, 0.04, -0.04]

        self.Q_table = dict()
        
        #self.Q_table = dict()
        for i in range(12): 
            for j in range(12):
                for a in range(-1,2,2):
                    for b in range(-1,2,1): 
                        for c in range(12): 
                            self.Q_table[(i,j,a,b,c)] = [0, 0, 0]
        
    
    def f_function(self, game):
        '''
        Choose action based on an epsilon greedy approach
        :return action index from 0 to 2
        '''
        action_selected = None
        
        # Your Code Goes Here!
        x = random.uniform(0,1)
        if x < self.epsilon_value:
            y = random.randint(0,2)
            #action_selected = self.action_list[y]
        else:
            #given a state s, find the max Q correspond to the state
            state = game.find_state()
            y = self.Q_table[state].index(max(self.Q_table[state]))
            #action_selected = self.action_list[y]
            
        return y


    def train_agent(self):
        '''
        Train the agent over a certain number of games.
        '''
        # Your Code Goes Here!
        print ("Training")        
        for i in range(self.num_games):
            game = MDP(0.5, 0.5, 0.03, 0.01, 0.5-0.2/2)
            game.discretize_state()    #decretize the first state
            end_sign = False

            while not end_sign:
                
                act = self.f_function(game) 
                cur_idx = game.find_state()    #get current game index
                
                end_sign, reward = game.simulate_one_time_step(act)    #simulate one time step
                game.discretize_state()                                #discretize
                next_idx = game.find_state()                           #next game index
                
                utility_list = self.Q_table[next_idx]  #(q1,q2,q3)     #get next game utility
                max_q_next = max(utility_list)                         
                
                self.Q_table[cur_idx][act] = (1-self.alpha_value)*self.Q_table[cur_idx][act]+self.alpha_value*(self.gamma_val*max_q_next + reward) 
                #game.print_state()
            #print "===end round==="
        
        pass

    def play_game(self):
        '''
        Simulate an actual game till the agent loses.
        '''
        # Your Code Goes Here!
        num_game = 1000
        result = []
        
        for i in range(num_game):
            print ("Round: " + str(i + 1))
            paddle_height = 0.2
            end_sign = False
            counter = 0
            
            game = MDP(0.5, 0.5, 0.03, 0.01, 0.5-0.2/2)
            game.discretize_state()
            while not end_sign:
                action = self.f_function(game)
                end_sign, reward = game.simulate_one_time_step(action)
                game.discretize_state()
                if reward==1:
                    counter += 1

            print "Rebound:" + str(counter)
            result.append(counter)
        print "the mean is " + str(statistics.mean(result))
        print "the variance is " + str(statistics.stdev(result))
        
        pass

