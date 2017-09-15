from Simulator.simulator import Simulator

if __name__ == "__main__":
    '''
    Runner code to start the training and game play.
    '''
    alpha_value = 0.4
    gamma_value = 0.95
    epsilon_value = 0.02
    num_games = 100000
#    mean = 5.34
#    var = 27
#    based on 10 games

#    mean = 8.77
#    var = 33
#    based on 100 games

#    mean = 8
#    std = 6.6
#    based on 100 games



    
#    alpha_value = 0.8
#    gamma_value = 0.95
#    epsilon_value = 0.04
#    num_games = 100000
    
    pong = Simulator(num_games, alpha_value, gamma_value, epsilon_value)
    pong.train_agent()
    pong.play_game()