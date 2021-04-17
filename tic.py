# ----- tic tac toe -----(shortened)
import random
turn = 1
table = 9 * [" "]
win_moves = [{0, 1, 2}, {0, 4, 8}, {0, 3, 6}, {3, 4, 5}, {6, 7, 8}, {1, 4, 7}, {2, 4, 6}, {2, 5, 8}]
num = [0, 1, 2, 3, 4, 5, 6, 7, 8]
X_pos = []
O_pos = []
duo_sets = []
win = 0
print("-----> Player is [X], Computer is [O] <-----")
print()

# win checker
def win_check(moves, pos, table):
    seq = []
    for i in pos:
        for j in pos:
            for k in pos:
                if i!=j and i!=k and j!=k:
                    test = {i, j, k}
                    if test not in seq:
                        seq.append(test)

    win_count = 0
    win_char = None
    for w_moves in moves:
        for cp_moves in seq:
            if cp_moves == w_moves:  # If Player/Computer wins
                win_count += 1
                cp_moves = list(cp_moves)
                win_char = table[cp_moves[0]]
                break
        if win_count == 1:
            break
    return win_count, win_char
# ---------------------------------------------------------------------------------
# Duo sequence maker
def duo_seq(moves, pos, num_list):  # Only the duo sequence is searched whose 3rd incoming element will make a win
    count = 0
    seq = []
    move = None
    for i in pos:
        for j in pos:
            if i != j:
                test = {i, j}
                if test not in seq:
                    for m in moves:
                        if test.issubset(m):
                            cp = m.difference(test)
                            cp = list(cp)
                            if cp[0] in num_list:
                                seq = test
                                move = cp[0]
                                count += 1
                                break
            if count == 1: break
        if count == 1: break
    if count == 0: seq = set()
    return move
# ---------------------------------------------------------------------------------
# Printing elements in the table
def print_table(table):
    for i in range(3):
        for j in range(9):
            if j == 0:
                print(table[3*i], end="")
            elif j == 4:
                print(table[1+3*i], end="")
            elif j == 8:
                print(table[2+3*i], end="")
            elif j == 2 or j == 6:
                print('|', end="")
            else:
                print(' ', end="")

        print()
        if i != 2:
            for k in range(9):
                print('-', end="")
            print()
# ****************************************************************************************************
while turn <= 5:
    Xtwo_seq = None
    Otwo_seq = None
    test_set = None
    c_move = None
    go = 0
    # ------- Player move -------
    while go < 1:
        try:
            p_move = int(input("Play your move [1-9]: "))
        except:
            print("Invalid move!, try again.")
        else:
            if (p_move-1) not in num:
                print("Invalid move!, try again.")
            else:
                go += 1

    table[p_move - 1] = "X"
    X_pos.append(p_move-1)
    num.remove(p_move-1)

    # Check if player has won or not, if yes then exit the loop
    if turn >= 4:
        win, char = win_check(win_moves, X_pos, table)
        if win == 1:
            break

    # ------- Computer move -------
    if turn == 1:  # First computer move
        c_move = random.choice(num)
        table[c_move] = "O"
        O_pos.append(c_move)
        num.remove(c_move)
        print_table(table)
    elif turn == 5:
        print("------- Deuce -------")
        break
    else:
        if turn >= 3:  # Check if win possible for computer
            Otwo_seq = duo_seq(win_moves, O_pos, num)
            if Otwo_seq is not None:
                c_move = Otwo_seq
                table[c_move] = "O"
                O_pos.append(c_move)
                num.remove(c_move)
                print_table(table)
            if turn >= 3:  # Check if computer has won or not, if yes then exit the loop
                win, char = win_check(win_moves, O_pos, table)
                if win == 1:
                    break

        if Otwo_seq is None:  # Defend if player's nxt move is win
            Xtwo_seq = duo_seq(win_moves, X_pos, num)
            if Xtwo_seq is not None:
                c_move = Xtwo_seq
                table[c_move] = "O"
                O_pos.append(c_move)
                num.remove(c_move)
                print_table(table)

        if Xtwo_seq is None and Otwo_seq is None:  # Attack, if nxt 2 moves can lead computer to win
            for ind1 in win_moves:
                for ind2 in O_pos:
                    ind2 = {ind2}
                    if ind2.issubset(ind1):
                        test_set = ind1.difference(ind2)
                        test_set = list(test_set)
                        if test_set[0] in num and test_set[1] in num:
                            c_move = test_set[0]
                            table[c_move] = "O"
                            O_pos.append(c_move)
                            num.remove(c_move)
                            print_table(table)
                            break
                if c_move is not None: break

        if turn >= 2 and c_move is None:  # Play a random move if none of the above is True
            c_move = random.choice(num)
            table[c_move] = "O"
            O_pos.append(c_move)
            num.remove(c_move)
            print_table(table)
    turn += 1

print()
if char == 'X':
    print("----- Congratulations! You won -----")
elif char == 'O':
    print("----- Oops! You lost -----")
