import math

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # X is maximizer, O is minimizer
    
    def print_board(self):
        print("\n   0   1   2")
        for i in range(3):
            print(f"{i}  {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]}")
            if i < 2:
                print("  ---|---|---")
    
    def is_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            return True
        
        return False
    
    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))
    
    def get_empty_cells(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
    
    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False
    
    def undo_move(self, row, col):
        self.board[row][col] = ' '
    
    def evaluate(self):
        if self.is_winner('X'):
            return 1
        elif self.is_winner('O'):
            return -1
        else:
            return 0
    
    def minimax(self, depth, is_maximizing):
        score = self.evaluate()
        
        # Terminal cases
        if score == 1 or score == -1:
            return score
        
        if self.is_board_full():
            return 0
        
        if is_maximizing:
            best_score = -math.inf
            for row, col in self.get_empty_cells():
                self.board[row][col] = 'X'
                score = self.minimax(depth + 1, False)
                self.board[row][col] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for row, col in self.get_empty_cells():
                self.board[row][col] = 'O'
                score = self.minimax(depth + 1, True)
                self.board[row][col] = ' '
                best_score = min(score, best_score)
            return best_score
    
    def get_best_move(self):
        best_score = -math.inf
        best_move = None
        
        print("\nAnalyzing moves:")
        for row, col in self.get_empty_cells():
            self.board[row][col] = 'X'
            score = self.minimax(0, False)
            self.board[row][col] = ' '
            
            print(f"Move ({row},{col}): score = {score}")
            
            if score > best_score:
                best_score = score
                best_move = (row, col)
        
        return best_move
    
    def play_game(self):
        print("Tic-Tac-Toe with Minimax AI")
        print("You are O, AI is X")
        self.print_board()
        
        while not self.is_board_full() and not self.is_winner('X') and not self.is_winner('O'):
            if self.current_player == 'X':
                # AI turn
                print("\nAI is thinking...")
                row, col = self.get_best_move()
                self.make_move(row, col, 'X')
                print(f"AI plays at ({row},{col})")
                self.current_player = 'O'
            else:
                # Human turn
                try:
                    row = int(input("\nEnter row (0-2): "))
                    col = int(input("Enter col (0-2): "))
                    
                    if self.make_move(row, col, 'O'):
                        self.current_player = 'X'
                    else:
                        print("Invalid move! Try again.")
                        continue
                except ValueError:
                    print("Invalid input! Please enter numbers.")
                    continue
            
            self.print_board()
        
        # Game over
        if self.is_winner('X'):
            print("\nAI wins!")
        elif self.is_winner('O'):
            print("\nYou win!")
        else:
            print("\nIt's a draw!")

# Example usage for minimax demonstration
def minimax_example():
    game = TicTacToe()
    
    # Set up a sample position
    moves = [(0, 0, 'X'), (0, 1, 'O'), (1, 1, 'X'), (2, 0, 'O')]
    
    print("Sample game position:")
    for row, col, player in moves:
        game.make_move(row, col, player)
    
    game.print_board()
    
    print("\nMinimax analysis:")
    best_move = game.get_best_move()
    print(f"\nBest move for X: {best_move}")

if __name__ == "__main__":
    choice = input("Enter 1 for minimax demo, 2 for full game: ")
    if choice == '1':
        minimax_example()
    else:
        game = TicTacToe()
        game.play_game()