import chess
import chess.engine


class chessCheater:
    def __init__(self) -> None:
        self.engine = chess.engine.SimpleEngine.popen_uci(
            r"C:\Users\mdp72\Downloads\stockfish_15.1_win_x64_avx2\stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2")
        self.board = chess.Board()

    def square_to_uci(self, square):
        return chr(int(square[-2]) + 96) + square[-1]

    def uci_to_square(self, uci):
        return str(ord(uci[-2]) - 96) + uci[-1]

    def uci_to_index(self, uci):
        return (ord(uci[-2]) - 97, int(uci[-1]) - 1)

    def push_move(self, start_square, end_square):
        start_uci, end_uci = self.square_to_uci(
            start_square), self.square_to_uci(end_square)
        move = start_uci + end_uci
        try:
            self.board.push_uci(start_uci +  end_uci)
            move = start_uci + end_uci
        except:
            self.board.push_uci(end_uci +  start_uci)
            move = end_uci +  start_uci
        moved_piece = "b" + \
            str(self.board.piece_at(chess.square(
                *self.uci_to_index(start_uci)))).lower()
        return (moved_piece, move)

    def get_move(self):
        response = self.engine.play(self.board, chess.engine.Limit(time=0.1))
        self.board.push(response.move)
        full_uci = str(response.move)
        start_uci, end_uci = full_uci[:2], full_uci[2:]
        moved_piece = "w" + \
            str(self.board.piece_at(chess.square(
                *self.uci_to_index(end_uci)))).lower()
        return (moved_piece, self.uci_to_square(start_uci), self.uci_to_square(end_uci))

# board = chess.Board()
# engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\mdp72\Downloads\stockfish_15.1_win_x64_avx2\stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2")

# cheat = chessCheater()
# print(cheat.square_to_uci("square-11"))
# print(cheat.uci_to_square("d2"))
# if cheat.get_move():
#     print(True)
# # print(board)
# # while not board.is_game_over():
# #     result = engine.play(board, chess.engine.Limit(time=0.1))
# #     board.push(result.move)
# #     print(str(result.move))
# #     print(type(str(result.move)))
# #     break
# # print(board)

# engine.quit()
