import numpy as np

to_string = lambda a : "ABCDEFGH"[a[0]] + str(a[1]+1)
to_array = lambda s : np.array(["ABCDEFGH".index(s[0]),int(s[1])-1])

class Reversi()
	
	def __init__(self, players, board = None):
		self.players = players
        self.board = np.zeros((8,8), dtype=str)
        self.board[3,[3,4]] = ['x','o']
        self.board[4,[3,4]] = ['o','x']
        self.nplayer='x'

## Weightage board
BOARD_SCORE = np.array( [[9,3,3,3,3,3,3,9],
                         [3,1,1,1,1,1,1,3],
                         [3,1,1,1,1,1,1,3],
                         [3,1,1,1,1,1,1,3],
                         [3,1,1,1,1,1,1,3],
                         [3,1,1,1,1,1,1,3],
                         [3,1,1,1,1,1,1,3],
                         [9,3,3,3,3,3,3,9]])

	def possible_moves(self):
		 #Only moves that lead to flipped pieces are allowed
        arr = [to_string((i,j)) for i in range(8) for j in range(8)
            if (self.board[i,j] == 0)
            and (pieces_flipped(self.board, (i,j), self.nplayer) != [])]
		if (arr == [])
			return [to_string((i,j)) for i in range(8) for j in range(8)
				if (self.board[i,j] == 0)
				and (piece_has_adjacent(self.board, (i,j), self.nplayer))]
		else
			return arr
			
	#Returns flipped pieces - needs to be changed
	def pieces_flipped(board, pos, nplayer):
    
    flipped = []
	for 


	
	if __name__ == "__main__":
		input = input()
		maxMoveCount = 60
		while(maxMoveCount > 0)
			if(input=="start")
				##start action
				make_move()
			else
				##wait for opponent move
				user_input = input()
				update_board()
				make_move()
