"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
#import codeskulptor
#codeskulptor.set_timeout(60)

# for the provided
#EMPTY = 1
#PLAYERX = 2
#PLAYERO = 3 
#DRAW = 4

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    #make a copy of the current board
    board0 = board.clone()
    #print str(board0)
    if board0.check_win() == provided.PLAYERO:
        return SCORES[provided.PLAYERO], (-1, -1)
    elif board0.check_win() == provided.PLAYERX:
        return SCORES[provided.PLAYERX], (-1, -1)
    elif board0.check_win() == provided.DRAW:
        return SCORES[provided.DRAW], (-1, -1)
    else:
        empty_squares = board0.get_empty_squares()
        all_possible_move_dict = {}
        for empty_square in empty_squares:
            board_clone = board0.clone()
            #change the cloned board
            board_clone.move(empty_square[0],empty_square[1],player)
            #switch player
            new_player = provided.switch_player(player)
            # recursive call to the original function
            next_score , (next_row, next_col) = mm_move(board_clone, new_player)
            all_possible_move_dict[next_score] = (empty_square[0], empty_square[1])
            if player == provided.PLAYERO:
                if next_score == -1:
                    break
            if player == provided.PLAYERX:
                if next_score == 1:
                    break
            
            
            
        if player == provided.PLAYERO:
            
            return min(all_possible_move_dict.keys()), all_possible_move_dict[min(all_possible_move_dict.keys())]
        else:
            return max(all_possible_move_dict.keys()), all_possible_move_dict[max(all_possible_move_dict.keys())]
        
    
    #the current level is taking max
    #the next level is taking min 
    # finally times the -1 or 1
    #the basis case
    #how to write recursion
    #how to record the board result and the move
    #As you recursively call your minimax function, you should create a copy of the board to pass to the next level
    
    #return 0, (-1, -1)

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]


#board = provided.TTTBoard(3,0, [[2,3,2],[2,3,2],[3,2,3]])
#print str(board)
#mm_move(board, provided.PLAYERO)
# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.
#print mm_move(board, provided.PLAYERX)


provided.play_game(move_wrapper, 1, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, move_wrapper, 1, False)
