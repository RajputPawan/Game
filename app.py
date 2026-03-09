from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class TicTacToe:
    def __init__(self):
        self.board = [''] * 9
        self.current_player = 'X'

    def make_move(self, pos):
        if self.board[pos] or self.winner():
            return False, "Invalid move or game over"
        self.board[pos] = self.current_player
        if self.winner():
            return True, f"Player {self.current_player} wins!"
        if self.is_full():
            return True, "It's a draw!"
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return False, "OK"

    def winner(self):
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return next((self.board[i] for i in wins if self.board[i] == self.board[i+1] == self.board[i+2]), None)

    def is_full(self):
        return all(self.board)

game = TicTacToe()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move/<int:pos>')
def move(pos):
    ended, msg = game.make_move(pos)
    return jsonify({'board': game.board, 'current': game.current_player, 'ended': ended, 'message': msg})

@app.route('/reset')
def reset():
    global game
    game = TicTacToe()
    return jsonify({'board': game.board, 'current': game.current_player, 'ended': False, 'message': 'New game!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
