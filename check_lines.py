def check_lines(board: list):
    """
    checks whether there are no two or more identical digits in one line and returns True or False
    >>> check_lines(["*1**4***5","**3***27*","4***2**6*","*76**91**", \
    "**83**3**","*4**8**3*","***7*1**8","2**5***4*","*6***2**9"])
    False
    """
    for line in range(len(board)):
        curr_line_lst = set()
        for col in range(len(board[0])):
            if board[line][col] != "*":
                if board[line][col] in curr_line_lst:
                    return False
                else:
                    curr_line_lst.add(board[line][col])
    return True
