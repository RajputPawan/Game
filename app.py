from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Global game state
board = [''] * 9
current = 'X'
game_over = False


def check_winner():
    """Return 'X' or 'O' if someone wins, 'Draw' if draw, or None if game continues."""
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    for a, b, c in wins:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if '' not in board:
        return 'Draw'
    return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/move/<int:pos>')
def move(pos):
    global current, game_over

    # Basic validation
    if pos < 0 or pos > 8:
        return jsonify(board=board, current=current,
                       message="Invalid move position.")

    # If game is already over, just tell the client
    if game_over:
        return jsonify(board=board, current=current,
                       message="Game over. Press New Game.")

    # Make a move if cell is free
    if board[pos] == '':
        board[pos] = current

        winner = check_winner()
        if winner == 'Draw':
            game_over = True
            message = "It's a draw! Press New Game."
        elif winner:
            game_over = True
            message = f"Player {winner} wins! Press New Game."
        else:
            # Switch player
            current = 'O' if current == 'X' else 'X'
            message = f"Player {current}'s turn"
    else:
        message = "Cell already taken!"

    return jsonify(board=board, current=current, message=message)


@app.route('/reset')
def reset():
    global board, current, game_over
    board = [''] * 9
    current = 'X'
    game_over = False
    return jsonify(board=board, current=current)


if __name__ == '__main__':
    # Host/port chosen so it works both locally and in Docker
    app.run(host='0.0.0.0', port=5000, debug=True)
