import copy


class Bot:
    def __init__(self):
        self.level = 1
        self.player = 2

    # Minimax without Alpha Beta Pruning
    
    def Minimax(self, board, maximizing):
        case = board.Result()

        if case == 1:
            return 1, None
        if case == 2:
            return -1, None
        elif board.IsBoardFull():
            return 0, None
        
        if maximizing:
            maximumEvaluation = float('-inf')
            emptyBoardFields = board.GetEmptyBoardFields()

            move = None

            for (fieldX, fieldY) in emptyBoardFields:
                currentBoard = copy.deepcopy(board)
                currentBoard.MarkField(fieldX, fieldY, 1)

                evaluation = self.Minimax(currentBoard, False)[0]

                if evaluation > maximumEvaluation:
                    maximumEvaluation = evaluation
                    move = (fieldX, fieldY)
            
            return maximumEvaluation, move 
    

    def AlphaBetaMinimax(self, board, maximizing, alpha, beta):
        case = board.Result()

        if case == 1:
            return 1, None
        if case == 2:
            return -1, None
        elif board.IsBoardFull():
            return 0, None
        
        if maximizing:
            maximumEvaluation = float('-inf')
            emptyBoardFields = board.GetEmptyBoardFields()

            move = None

            for (fieldX, fieldY) in emptyBoardFields:
                currentBoard = copy.deepcopy(board)
                currentBoard.MarkField(fieldX, fieldY, 1)

                evaluation = self.AlphaBetaMinimax(currentBoard, False, alpha, beta)[0]

                if evaluation > maximumEvaluation:
                    maximumEvaluation = evaluation
                    move = (fieldX, fieldY)

                alpha = max(alpha, maximumEvaluation)
                if maximumEvaluation >= beta:
                    break
            
            return maximumEvaluation, move

        else:
            minimumEvaluation = float('inf')
            emptyBoardFields = board.GetEmptyBoardFields()

            move = None

            for (fieldX, fieldY) in emptyBoardFields:
                currentBoard = copy.deepcopy(board)
                currentBoard.MarkField(fieldX, fieldY, self.player)

                evaluation = self.AlphaBetaMinimax(currentBoard, True, alpha, beta)[0]

                if evaluation < minimumEvaluation:
                    minimumEvaluation = evaluation
                    move = (fieldX, fieldY)

                beta = min(beta, minimumEvaluation)
                if minimumEvaluation <= alpha:
                    break
            
            return minimumEvaluation, move

    def Evaluation(self, board, alpha=float('-inf'), beta=float('inf')):
        evaluation, move = self.AlphaBetaMinimax(board, False, alpha, beta)
        #evaluation, move = self.Minimax(board, False)
        
        print(f'Evaluation: {evaluation}')

        return move