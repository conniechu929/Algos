# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        queue = collections.deque([])
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if (i in [0, len(board)-1] or j in [0, len(board[0])-1]) and board[i][j] == 'O':
                    queue.append((i,j))
        # print "QUEUE:", queue
        while len(queue) > 0:
            # print "QUEUE INSIDE WHILE LOOP:", queue
            i, j = queue.popleft() #deque.popleft() is faster for deque than a list.pop(0)
            # print "i:", i
            # print "j:",j
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == 'O':
            # if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j] == "O":
                board[i][j] = '#'
                queue.append((i-1, j))
                queue.append((i+1, j))
                queue.append((i, j+1))
                queue.append((i, j-1))

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
