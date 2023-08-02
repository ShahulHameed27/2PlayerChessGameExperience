import datetime

class ChessGame:
    def __init__(self):
        self.board = [
            ['B_R', 'B_N', 'B_B', 'B_Q', 'B_K', 'B_B', 'B_N', 'B_R'],
            ['B_P', 'B_P', 'B_P', 'B_P', 'B_P', 'B_P', 'B_P', 'B_P'],
            [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
            [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
            [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
            [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
            ['W_P', 'W_P', 'W_P', 'W_P', 'W_P', 'W_P', 'W_P', 'W_P'],
            ['W_R', 'W_N', 'W_B', 'W_Q', 'W_K', 'W_B', 'W_N', 'W_R']
        ]
        self.player = 1
        self.current_coin = None
        self.moves = [] 

    def get_possible_moves(self, row, col):
        coin = self.board[row][col][2:]

        if coin == 'P':
            return self.get_possible_moves_pawn(row, col)
        elif coin == 'N':
            return self.get_possible_moves_knight(row, col)
        elif coin == 'R':
            return self.get_possible_moves_rook(row, col)
        elif coin == 'B':
            return self.get_possible_moves_bishop(row, col)
        elif coin == 'Q':
            return self.get_possible_moves_queen(row, col)
        elif coin == 'K':
            return self.get_possible_moves_king(row, col)

    def get_possible_moves_pawn(self, row, col):
        color = self.board[row][col][0]  

        if color == 'W':
            direction = -1  
        else:
            direction = 1  

        possible_moves = []

        new_row = row + direction
        if 0 <= new_row <= 7 and self.board[new_row][col] == ' - ':
            k=chr(col+ord('a'))+str(new_row+1)
            possible_moves.append(k)

        if ((color == 'W' and row == 6) or (color == 'B' and row == 1)) and self.board[row + 2 * direction][col] == ' - ':
            k=chr(col+ord('a'))+str((row+2*direction)+1)
            possible_moves.append(k)

        for dc in [-1, 1]: 
            new_col = col + dc
            if 0 <= new_col <= 7:
                target = self.board[row + direction][new_col]
                if target != ' - ' and target[0] != color:
                    k=chr(new_col+ord('a'))+str(row+direction+1)
                    possible_moves.append(k)

        return possible_moves

    def get_possible_moves_knight(self, row, col):
        possible_moves = []
        moves_offsets = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)]

        for dr, dc in moves_offsets:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                target = self.board[new_row][new_col]
                if target == ' - ' or target[0] != self.board[row][col][0]:
                    k=chr(new_col+ord('a'))+str(new_row+1)
                    possible_moves.append(k)

        return possible_moves

    def get_possible_moves_rook(self, row, col):
        possible_moves = []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while 0 <= new_row <= 7 and 0 <= new_col <= 7:
                target = self.board[new_row][new_col]
                if target == ' - ':
                    k=chr(new_col+ord('a'))+str(new_row+1)
                    possible_moves.append(k)
                elif target[0] != self.board[row][col][0]:
                    k=chr(new_col+ord('a'))+str(new_row+1)
                    possible_moves.append(k)
                    break
                else:
                    break
                new_row, new_col = new_row + dr, new_col + dc

        return possible_moves

    def get_possible_moves_bishop(self, row, col):
        possible_moves = []

        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while 0 <= new_row <= 7 and 0 <= new_col <= 7:
                target = self.board[new_row][new_col]
                if target == ' - ':
                    k=chr(new_col+ord('a'))+str(new_row+1)
                    possible_moves.append(k)
                elif target[0] != self.board[row][col][0]:
                    k=chr(new_col+ord('a'))+str(new_row+1)
                    possible_moves.append(k)
                    break
                else:
                    break
                new_row, new_col = new_row + dr, new_col + dc

        return possible_moves

    def get_possible_moves_queen(self, row, col):
        possible_moves = []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while 0 <= new_row <= 7 and 0 <= new_col <= 7:
                target = self.board[new_row][new_col]
                if target == ' - ':
                    k=chr(new_col+ord('a'))+str(new_row+1)
                    possible_moves.append(k)
                elif target[0] != self.board[row][col][0]:
                    k=chr(new_col+ord('a'))+str(new_row+1)
                    possible_moves.append(k)
                    break
                else:
                    break
                new_row, new_col = new_row + dr, new_col + dc

        return possible_moves

    def get_possible_moves_king(self, row, col):
        possible_moves = []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                target = self.board[new_row][new_col]
                if target == ' - ' or target[0] != self.board[row][col][0]:
                    k=chr(new_col+ord('a'))+str(new_row+1)
                    possible_moves.append(k)

        return possible_moves

    def print_board(self):
        print("   a   b   c   d   e   f   g   h")
        for row_num, row in enumerate(self.board, 10):
            print(f"{abs(row_num-9)} {' '.join(row)} {abs(row_num-9)}")
        print("   a   b   c   d   e   f   g   h")

    def simulate_moves(self, row, col, moves):

        original_piece = self.board[row][col]
        for move in moves:
            new_col, new_row = ord(move[0]) - ord('a'), int(move[1]) - 1
            if not (0 <= new_col <= 7) or not (0 <= new_row <= 7):
                continue

            self.board[new_row][new_col] = self.board[row][col]
            self.board[row][col] = ' - '

            opponent_color = 'B' if original_piece[0] == 'W' else 'W'
            for r in range(8):
                for c in range(8):
                    piece = self.board[r][c]
                    if piece[0] == opponent_color:
                        possible_moves = self.get_possible_moves(r, c)
                        if f"{chr(new_col + ord('a'))}{new_row + 1}" in possible_moves:
                            self.board[row][col] = original_piece  
                            self.board[new_row][new_col] = ' - '  
                            return True

            self.board[row][col] = original_piece  
            self.board[new_row][new_col] = ' - '  

        return False

    def check_coin_capture(self, position):
        col, row = ord(position[0]) - ord('a'), int(position[1]) - 1
        if not (0 <= col <= 7) or not (0 <= row <= 7):
            print("Invalid position. Try again.")
            return

        coin = self.board[row][col]
        if coin == ' - ':
            print("No coin at this position. Try again.")
            return

        color = coin[0]
        if color == 'W':
            opponent_color = 'B'
        else:
            opponent_color = 'W'

        possible_moves = self.get_possible_moves(row, col)
        if self.simulate_moves(row, col, possible_moves):
            print(f"The {coin} in {position} can capture your piece on the next opponent's turn.")
        else:
            print("Safe place")

    def make_move(self, move):
        self.moves.append(move)

    def save_game(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"game_{timestamp}.txt"

        with open(filename, "w") as file:
            file.write("Game Details:\n")
            for move in self.moves:
                file.write(move + "\n")

    def start_game(self):
        ends= 0
        while True:
            self.print_board()
            position = input(f"Player {self.player}, choose a coin (e.g., b1): ")
            if position.lower() == 'exit':
                ends=1
                break
            if position.lower() == 'print':
                self.print_board()
                continue
            if "--help" in position:
                self.check_coin_capture(position)
                continue

            col, row = ord(position[0]) - ord('a'), int(position[1]) - 1
            if not (0 <= col <= 7) or not (0 <= row <= 7):
                print("Invalid position. Try again.")
                continue

            coin = self.board[row][col]
            if coin == ' - ':
                print("No coin at this position. Try again.")
                continue

            if self.player == 1 and not coin.startswith("W_"):
                print("Not your coin. Try again.")
                continue
            elif self.player == 2 and not coin.startswith("B_"):
                print("Not your coin. Try again.")
                continue
            piece=""
            if coin.endswith("_K"):
                piece="King"
            elif coin.endswith("_N"):
                piece="Knight"
            elif coin.endswith("_R"):
                piece="Rook"
            elif coin.endswith("_Q"):
                piece="Queen"
            elif coin.endswith("_P"):
                piece="Pawn"  
            self.current_coin = (row, col)
            print(f"Selected coin: {piece}")

            possible_moves = self.get_possible_moves(row, col)
            print(f"Possible moves: {possible_moves}")

            new_position = input("Enter the new position to move the coin: ")
            if "--help" in new_position:
                new_positions,help=new_position.split(" ")
                self.check_coin_capture(position)
                new_col, new_row = ord(new_positions[0]) - ord('a'), int(new_positions[1]) - 1
                new_position=new_positions
            else:
                new_col, new_row = ord(new_position[0]) - ord('a'), int(new_position[1]) - 1
            
            if new_position in possible_moves:
                if self.board[new_row][new_col] != ' - ':

                    captured_coin = self.board[new_row][new_col]
                    captured_piece=""
                    if captured_coin.endswith("_K"):
                        captured_piece="King"
                    elif captured_coin.endswith("_N"):
                        captured_piece="Knight"
                    elif captured_coin.endswith("_R"):
                        captured_piece="Rook"
                    elif captured_coin.endswith("_Q"):
                        captured_piece="Queen"
                    elif captured_coin.endswith("_P"):
                        captured_piece="Pawn"  
                    captured_move = f"{('White' if self.player == 1 else 'Black')} {piece} at {position} has been captured {captured_piece} at {new_position}"
                    self.make_move(captured_move)
                else:

                    move = f"{('White' if self.player == 1 else 'Black')} {piece} at {position} has been moved to {new_position}"
                    self.make_move(move)
                
                self.board[new_row][new_col] = self.board[row][col]
                self.board[row][col] = ' - '
                self.player = 1 if self.player == 2 else 2

            else:
                print("Invalid move. Try again.")
            
        if ends==1:
            self.save_game()


if __name__ == "__main__":
    chess_game = ChessGame()
    chess_game.start_game()
