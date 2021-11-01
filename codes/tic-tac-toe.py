# 三目並べ ver. CUI

class TicTacToe:
    def __init__(self):
        self.OPEN = 0
        self.FIRST = 1
        self.SECOND = 2
        self.DRAW = 3
        self.turn = 1
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        # テスト用の棋譜
        self.log1 = [[0,0],[1,1],[1,0],[2,0],[0,2],[0,1],[2,1],[2,2],[1,2],[self.DRAW]]
        self.log2 = [[0,0],[1,0],[1,1],[2,2],[0,1],[2,0],[2,1],[self.FIRST]]
        self.log3 = [[0,1],[0,0],[2,1],[1,1],[2,2],[2,0],[1,0],[0,2],[self.SECOND]]

    # 手番に関する操作
    def show_turn(self):
        if self.turn == self.FIRST:
            return ('先手')
        elif self.turn == self.SECOND:
            return ('後手')
        else:
            return ('手番の値が不適切です')

    def init_turn(self):
        self.turn = self.FIRST

    def change_turn(self):
        if self.turn == self.FIRST:
            self.turn = self.SECOND
        else:
            self.turn = self.FIRST

    # 手番関連のテスト
    def test_turn(self):
        self.init_turn()
        print(self.show_turn(), "の番です")
        self.change_turn()
        print(self.show_turn(), "の番です")
        self.change_turn()
        print(self.show_turn(), "の番です")

    # 盤面に関する操作
    def show_board(self):
        s = ' : 0 1 2\n---------\n'
        for i in range(3):
            s = s + str(i) + ': '
            for j in range(3):
                cell = ''
                if self.board[i][j] == self.OPEN:
                    cell = ' '
                elif self.board[i][j] == self.FIRST:
                    cell = 'O'
                elif self.board[i][j] == self.SECOND:
                    cell = 'X'
                else:
                    cell = '?'
                s = s + cell + ' '
            s = s + '\n'
        return s

    def init_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = self.OPEN

    def examine_board(self, i, j):
        return self.board[i][j]

    def set_board(self, i, j, t):
        if (i>=0) and (i<3) and (j>=0) and (j<3):
            if (t>0) and (t<3):
                if self.examine_board(i, j) == 0:
                    self.board[i][j] = t
                    return 'OK'
                else:
                    return 'Not empty'
            else:
                return 'Illegal turn'
        else:
            return 'Illegal slot'

    # 盤面関連のテスト1
    def test_board1(self):
        self.init_board()
        print(self.show_board())
        print(self.set_board(0,0,1))
        print(self.show_board())
        print(self.set_board(1,1,2))
        print(self.show_board())
        print(self.set_board(1,1,1))
        print(self.show_board())

    # 勝敗判定
    def check_board_horizontal(self, t):
        for i in range(3):
            if (self.board[i][0] == t) and (self.board[i][1] == t) and (self.board[i][2] == t):
                return True
        return False

    def check_board_vertical(self, t):
        for i in range(3):
            if (self.board[0][i] == t) and (self.board[1][i] == t) and (self.board[2][i] == t):
                return True
        return False

    def check_board_diagonal(self, t):
        if (self.board[0][0] == t) and (self.board[1][1] == t) and (self.board[2][2] == t):
            return True
        else:
            return False

    def check_board_inverse_diagonal(self, t):
        if (self.board[0][2] == t) and (self.board[1][1] == t) and (self.board[2][0] == t):
            return True
        else:
            return False

    def is_win_simple(self, t):
        if self.check_board_horizontal(t):
            return True
        if self.check_board_vertical(t):
            return True
        if self.check_board_diagonal(t):
            return True
        if self.check_board_inverse_diagonal(t):
            return True
        return False

    def is_win_actual(self, t):
        if not self.is_win_simple(t):
            return False
        if t == self.FIRST:
            if self.is_win_simple(self.SECOND):
                return False
        if t == self.SECOND:
            if self.is_win_simple(self.FIRST):
                return False
        return True

    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.OPEN:
                    return False
        return True

    def is_draw(self):
        if self.is_win_simple(self.FIRST):
            return False
        if self.is_win_simple(self.SECOND):
            return False
        if not self.is_full():
            return False
        return True

    # 盤面に関するテスト2
    def test_board2(self):
        self.init_board()
        self.board[0][0] = self.FIRST
        self.board[1][0] = self.FIRST
        self.board[2][0] = self.FIRST
        print("HORIZONTSL FIRST: " , self.check_board_horizontal(self.FIRST))
        print("HORIZONTSL SECOND: ", self.check_board_horizontal(self.SECOND))
        print("VERTICAL FIRST: "   , self.check_board_vertical(self.FIRST))
        print("VERTICAL SECOND: "  , self.check_board_vertical(self.SECOND))

    # 棋譜に関する操作
    def replay_log(self, log):
        self.init_board()
        self.init_turn()
        print(self.show_board())
        for m in log:
            if len(m) == 2:
                print(self.show_turn(), "のターンです")
                print(self.set_board(m[0], m[1], self.turn))
                print(self.show_board())
                print("IS WIN", self.turn, ": ", self.is_win_actual(self.turn))
                self.change_turn()
            else:
                print("RESULT IN LOG: ", m[0])
        print("IS WIN FIRST: ", self.is_win_actual(self.FIRST))
        print("IS WIN SECOND: ", self.is_win_actual(self.SECOND))
        print("IS DRAW: ", self.is_draw())

    # ログ関連のテスト
    def test_log(self):
        print("LOG1")
        self.replay_log(self.log1)
        print("LOG2")
        self.replay_log(self.log2)
        print("LOG3")
        self.replay_log(self.log3)

    # すべてのテスト
    def test_all(self):
        print("")
        print("=====================")
        print("=テストを開始します=")
        print("=====================")
        print("")
        self.test_turn()
        print("")
        self.test_board1()
        print("")
        self.test_board2()
        print("")
        self.test_log()
        print("")
        print("=====================")
        print("=テストを終了します=")
        print("=====================")

    # 実際にプレイ
    def play(self):
        self.init_turn()
        self.init_board()
        print(self.show_board())
        self.log = []

        while True:
            print(self.show_turn(), "の番です")
            while True:
                row = int(input("行を入力してください（0 ~ 2）"))
                column = int(input("列を入力してください（0 ~ 2）"))
                result = self.set_board(row, column, self.turn)
                print(result)
                if result == "OK":
                    break
                print("不適切な入力です。再度入力ください")
            print(self.show_board())
            if self.is_draw():
                print("引き分けです")
                break
            if self.is_win_actual(self.turn):
                print(self.show_turn(), "の勝ちです")
                break
            print("aaaaaaaaaaaaa")
            self.change_turn()

        if len(self.log) > 0:
            self.replay_log(self.log)
        else:
            print("棋譜は作成されていません")

if __name__ == "__main__":
    print("三目並べ")
    t = TicTacToe()
    #t.test_all()
    t.play()
