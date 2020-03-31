"""
Kingsheep Agent Template
"""

from config import *


"""code for parsing a List into a tree """

""" @author Claudia Jurado Santos
    @email tony@tonypoer.io
    
    tree_parser.py --> parse a list into a tree.
                       Only leaf nodes have values.
                       I'm intending to running minimax algorithms on these trees for a competitive game AI
    
    Data should be in the following format: 
    [(x,y,v),(x,y,v)...(x,y,v)] being X and Y the coordinates and x the value of the node. 
    
    Note that Leaves must be **tuples**
    
    Usage:  python tree_parser.py [filename]
        File should have data in the format shown above. 
"""
from queue import SimpleQueue
from ast import literal_eval
import sys



##########################
###### PARSE DATA ########
##########################
possible_goals= [(0, 0, 0), (2, 4, 2), (2, 5, 3), (2, 6, 4), (2, 12, 10),(4, 5, 6)]

class GameNode:
    def __init__(self, parent,x,y):
        
        self.value = None    # an int
        self.parent = parent  # a node reference
        self.children = []    # a list of nodes
        self.x = x
        self.y = y

    def addChild(self, childNode):
        self.children.append(childNode)
    def addValue(self, val):
        self.value = val
    def getValue(self):
        return self.value 
    def getChildren(self): 
        return self.children
    def getParent(self): 
        return self.parent
    def getX(self):
        return self.x
    def getY(self):
        return self.y
            
class GameTree:
    def __init__(self):        
        self.root = None

    def getRoot(self):
        return self.root
        
    def build_tree(self, data_list): #here we are gonna introduce the list

        """
        :param data_list: Take data in list format
        :return: Parse a tree from it
        """
        self.root = GameNode(data_list[0],data_list[0][1],data_list[0][0]) #the first possition of the list will be the root
        data_list.remove(data_list[0]) #remove the first element 
        self.sub_tree(data_list, self.root)
    
    def sub_tree(self, data_list,parent):
        if len(data_list)==0: #in case our list is empty
            return
        if len(data_list)==1:
            tree_node = GameNode(parent,data_list[0][1],data_list[0][0])
            tree_node.addValue(data_list[0][2]) #we only add value to the node is a leaf 
            parent.addChild(tree_node) # We add a leaf in the tree
            return
        #if the list contain more than one node: 
        x=0
        for elem in data_list:
            auxlist= data_list.copy()
            tree_node = GameNode(parent,data_list[x][1],data_list[x][0])
            parent.addChild(tree_node)
            auxlist.remove(auxlist[x])
            x+=1
            self.sub_tree(auxlist,tree_node)

    
    def searchtree(self):  #method used to check if the tree was corrected implemented
        
        queue = SimpleQueue()

        if not(self.root==None): 
            rot= self.getRoot()
            print(rot.getX(),rot.getY())
            aux= rot.getChildren()
            for i in aux:
                print(i.getX())
            print('Hasta aqui los hijos del root')
            for elem in aux: 
                queue.put(elem)
            while(not queue.empty()): 
                x = queue.get()
                print('child')
                print(x.getX(),x.getY(),'padre',x.getParent().getX(),x.getParent().getY())

                for elem in x.getChildren():
                    queue.put(elem)


class AlphaBeta:
    # print utility value of root node (assuming it is max)
    # print names of all nodes visited during search
    def __init__(self, game_tree):
        self.game_tree = game_tree  # GameTree
        self.root = game_tree.getRoot()  # GameNode
        
    def getRootX(self): 
        return self.root.getX()
    def getRootY(self): 
        return self.root.getY()

    def getRoot(self): 
        return self.root

    def is_leaf(self,node): 
        return len(node.getChildren())==0 

    def alpha_beta_search(self, node):
        infinity = float('inf') #unbounded upper value for comparison
        best_val = -infinity  #alpha 
        beta = infinity       #beta 

        successors = node.getChildren()
        best_state = None          #it has to be node type 
        for state in successors:
            value = self.min_value(state, best_val, beta)
            if value > best_val:
                best_val = value
                best_state = state
        
        #print('AlphaBeta:  Utility Value of Root Node: = ' , str(best_val))
        #print('AlphaBeta:  Best State is: ' , best_state.getX())
        return best_state

    def max_value(self, node, alpha, beta):
        #print("AlphaBeta-->MAX: Visited Node :: " , '(',node.getX(),node.getY(),')') 
        if self.is_leaf(node): #if is_leaf(node)
            return node.getValue() # return the value
        infinity = float('inf') 
        value = -infinity               #v =-infinite 

        successors = node.getChildren()
        for state in successors:    #for each child of node 
            value = max(value, self.min_value(state, alpha, beta))
            if value >= beta:
                return value  #here is the prune 
            alpha = max(alpha, value) #best already explored option root for the maximizer
        return value

    def min_value(self, node, alpha, beta):
        #print('AlphaBeta-->MIN: Visited Node :: ' ,'(',node.getX(),node.getY(),')') 
        if self.is_leaf(node):
            return node.getValue()
        infinity = float('inf')
        value = infinity # v= infinite

        successors = node.getChildren()
        for state in successors:
            value = min(value, self.max_value(state, alpha, beta))
            if value <= alpha:
                return value       #prune
            beta = min(beta, value) #best already explored option for the minimizer

        return value
    #                     #
    #   UTILITY METHODS   #
    #                     #

    # successor states in a game tree are the child nodes...
    """def getSuccessors(self, node):
        node.getChildren()"""

    # return true if the node has NO children (successor states)
    # return false if the node has children (successor states)
    def isTerminal(self, node):
        assert node is not None
        return len(node.children) == 0

    """def getUtility(self, node):
        assert node is not None
        return node.value"""

                         
##########################
#### class_name ####
##########################


def get_class_name():
    return 'MyFAgent'


class MyFAgent:
    """Example class for a Kingsheep player"""

    def __init__(self):
        self.name = "CJ"
        self.uzh_shortname = "clsant"

    def get_player_position(self, figure, field):
        x = [x for x in field if figure in x][0]
        return (field.index(x), x.index(figure))

    """ index() function which searches for given element from start of the list and
     returns the lowest index where the element appears. return = (y,x) where the figure was found"""
    

    # defs for sheep
    def food_present(self, field):
        food_present = False

        for line in field:
            for item in line:
                if item == CELL_RHUBARB or item == CELL_GRASS:
                    food_present = True
                    break
        return food_present

    """look for all the Rhubarb and Grass and keep it in a list of tuples (x,y,v) where the x and y are the parametres for the position of 
        the item and v is the value that represents the distance to the item"""
    def possible_goals(self, player_number, field):
        possible_goals = []
        leng =6 

        if player_number == 1:
            sheep_position = self.get_player_position(CELL_SHEEP_1, field)
        else:
            sheep_position = self.get_player_position(CELL_SHEEP_2, field)

        y_position = 0
        for line in field:
            x_position = 0
            for item in line:
                if item == CELL_RHUBARB or item == CELL_GRASS:
                    value =abs(y_position-sheep_position[0])+abs(x_position -sheep_position[1])
                    if item == CELL_RHUBARB:
                        value -= 1  # Rhubanrd is more value than grass distances care less
                    possible_goals.append((y_position, x_position, value))#we add the tupple to the list we will parser later
                x_position += 1
            y_position += 1
        short_list = []
        x= 0
        for elem in possible_goals:
            if len(short_list)<leng:
                short_list.append(possible_goals[x])
                
            else: 
                y=0
                for elem in short_list: 
                    if possible_goals[x][2]<short_list[y][2]:
                        short_list[y]=possible_goals[x]
                    y+=1
            x+=1


        short_list.insert(0, (0,0,0))#we add a first element we are not going to check as a root

        return short_list 

    def gather_closest_goal(self, closest_goal, field, figure):  # closest_goal will be a node type
        # takes player position
        figure_position = self.get_player_position(figure, field)
        
        distance_x = figure_position[1] - closest_goal[1]
        distance_y = figure_position[0] - closest_goal[0]


        if distance_x == 0:
            # print('item right above/below me')
            if distance_y > 0:
                if self.valid_move(figure, figure_position[0] - 1, figure_position[1], field):
                    return MOVE_UP
                else:
                    return MOVE_RIGHT  
            else:
                if self.valid_move(figure, figure_position[0] + 1, figure_position[1], field):
                    return MOVE_DOWN
                else:
                    return MOVE_RIGHT
        elif distance_y == 0:
            # print('item right beside me')
            if distance_x > 0:
                if self.valid_move(figure, figure_position[0], figure_position[1] - 1, field):

                    return MOVE_LEFT
                else:
                    return MOVE_UP
            else:
                if self.valid_move(figure, figure_position[0], figure_position[1] + 1, field):
                    return MOVE_RIGHT
                else:
                    return MOVE_UP

        else:
            # go left or up
            if distance_x > 0 and distance_y > 0:
                if self.valid_move(figure, figure_position[0], figure_position[1] - 1, field):
                    return MOVE_LEFT
                else:
                    return MOVE_UP

            # go left or down
            elif distance_x > 0 and distance_y < 0:
                if self.valid_move(figure, figure_position[0], figure_position[1] - 1, field):
                    return MOVE_LEFT
                else:
                    return MOVE_DOWN

            # go right or up
            elif distance_x < 0 and distance_y > 0:
                if self.valid_move(figure, figure_position[0], figure_position[1] + 1, field):
                    return MOVE_RIGHT
                else:
                    return MOVE_UP

            # go right or down
            elif distance_x < 0 and distance_y < 0:
                if self.valid_move(figure, figure_position[0], figure_position[1] + 1, field):
                    return MOVE_RIGHT
                else:
                    return MOVE_DOWN

            else:
                # print('fail')
                return MOVE_NONE

    def gather_closest_goalS(self, closest_goal, field, figure): # closest_goal will be a node type
        # takes player position
        figure_position = self.get_player_position(figure, field)
        distance_x = figure_position[1] - closest_goal.getX()
        distance_y = figure_position[0] - closest_goal.getY()

        if distance_x == 0:
            # print('item right above/below me')
            if distance_y > 0:
                if self.valid_move(figure, figure_position[0] - 1, figure_position[1], field):
                    return MOVE_UP
                else:
                    return MOVE_RIGHT  
            else:
                if self.valid_move(figure, figure_position[0] + 1, figure_position[1], field):
                    return MOVE_DOWN
                else:
                    return MOVE_RIGHT
        elif distance_y == 0:
            # print('item right beside me')
            if distance_x > 0:
                if self.valid_move(figure, figure_position[0], figure_position[1] - 1, field):

                    return MOVE_LEFT
                else:
                    return MOVE_UP
            else:
                if self.valid_move(figure, figure_position[0], figure_position[1] + 1, field):
                    return MOVE_RIGHT
                else:
                    return MOVE_UP

        else:
            # go left or up
            if distance_x > 0 and distance_y > 0:
                if self.valid_move(figure, figure_position[0], figure_position[1] - 1, field):
                    return MOVE_LEFT
                else:
                    return MOVE_UP

            # go left or down
            elif distance_x > 0 and distance_y < 0:
                if self.valid_move(figure, figure_position[0], figure_position[1] - 1, field):
                    return MOVE_LEFT
                else:
                    return MOVE_DOWN

            # go right or up
            elif distance_x < 0 and distance_y > 0:
                if self.valid_move(figure, figure_position[0], figure_position[1] + 1, field):
                    return MOVE_RIGHT
                else:
                    return MOVE_UP

            # go right or down
            elif distance_x < 0 and distance_y < 0:
                if self.valid_move(figure, figure_position[0], figure_position[1] + 1, field):
                    return MOVE_RIGHT
                else:
                    return MOVE_DOWN

            else:
                # print('fail')
                return MOVE_NONE

    def wolf_close(self, player_number, field):
        if player_number == 1:
            sheep_position = self.get_player_position(CELL_SHEEP_1, field)
            wolf_position = self.get_player_position(CELL_WOLF_2, field)
        else:
            sheep_position = self.get_player_position(CELL_SHEEP_2, field)
            wolf_position = self.get_player_position(CELL_WOLF_1, field)

        if (abs(sheep_position[0] - wolf_position[0]) <= 2 and abs(sheep_position[1] - wolf_position[1]) <= 2):
            # print('wolf is close')
            return True
        return False

    def valid_move(self, figure, x_new, y_new, field):
        # Neither the sheep nor the wolf, can step on a square outside the map. Imagine the map is surrounded by fences.
        if x_new > FIELD_HEIGHT - 1:
            return False
        elif x_new < 0:
            return False
        elif y_new > FIELD_WIDTH - 1:
            return False
        elif y_new < 0:
            return False

        # Neither the sheep nor the wolf, can enter a square with a fence on.
        if field[x_new][y_new] == CELL_FENCE:
            return False

        # Wolfs can not step on squares occupied by the opponents wolf (wolfs block each other).
        # Wolfs can not step on squares occupied by the sheep of the same player .
        if figure == CELL_WOLF_1:
            if field[x_new][y_new] == CELL_WOLF_2:
                return False
            elif field[x_new][y_new] == CELL_SHEEP_1:
                return False
        elif figure == CELL_WOLF_2:
            if field[x_new][y_new] == CELL_WOLF_1:
                return False
            elif field[x_new][y_new] == CELL_SHEEP_2:
                return False

        # Sheep can not step on squares occupied by the wolf of the same player.
        # Sheep can not step on squares occupied by the opposite sheep.
        if figure == CELL_SHEEP_1:
            if field[x_new][y_new] == CELL_SHEEP_2 or \
                    field[x_new][y_new] == CELL_WOLF_1:
                return False
        elif figure == CELL_SHEEP_2:
            if field[x_new][y_new] == CELL_SHEEP_1 or \
                    field[x_new][y_new] == CELL_WOLF_2:
                return False

        return True

    def run_from_wolf(self, player_number, field):
        if player_number == 1:
            sheep_position = self.get_player_position(CELL_SHEEP_1, field)
            wolf_position = self.get_player_position(CELL_WOLF_2, field)
            sheep = CELL_SHEEP_1
        else:
            sheep_position = self.get_player_position(CELL_SHEEP_2, field)
            wolf_position = self.get_player_position(CELL_WOLF_1, field)
            sheep = CELL_SHEEP_2

        distance_x = sheep_position[1] - wolf_position[1]
        abs_distance_x = abs(sheep_position[1] - wolf_position[1])
        distance_y = sheep_position[0] - wolf_position[0]
        abs_distance_y = abs(sheep_position[0] - wolf_position[0])

        # print('player_number %i' %player_number)
        # print('running from wolf')
        # if the wolf is close vertically
        if abs_distance_y == 1 and distance_x == 0:
            # print('wolf is close vertically')
            # if it's above the sheep, move down if possible
            if distance_y > 0:
                if self.valid_move(sheep, sheep_position[0] + 1, sheep_position[1], field):
                    return MOVE_DOWN
            else:  # it's below the sheep, move up if possible
                if self.valid_move(sheep, sheep_position[0] - 1, sheep_position[1], field):
                    return MOVE_UP
                    # if this is not possible, flee to the right or left
            if self.valid_move(sheep, sheep_position[0], sheep_position[1] + 1, field):
                return MOVE_RIGHT
            elif self.valid_move(sheep, sheep_position[0], sheep_position[1] - 1, field):
                return MOVE_LEFT
            else:  # nowhere to go
                return MOVE_NONE

        # else if the wolf is close horizontally
        elif abs_distance_x == 1 and distance_y == 0:
            # print('wolf is close horizontally')
            # if it's to the left, move to the right if possible
            if distance_x > 0:
                if self.valid_move(sheep, sheep_position[0], sheep_position[1] - 1, field):
                    return MOVE_RIGHT
            else:  # it's to the right, move left if possible
                if self.valid_move(sheep, sheep_position[0], sheep_position[1] + 1, field):
                    return MOVE_LEFT
            # if this is not possible, flee up or down
            if self.valid_move(sheep, sheep_position[0] - 1, sheep_position[1], field):
                return MOVE_UP
            elif self.valid_move(sheep, sheep_position[0] + 1, sheep_position[1], field):
                return MOVE_DOWN
            else:  # nowhere to go
                return MOVE_NONE

        elif abs_distance_x == 1 and abs_distance_y == 1:
            # print('wolf is in my surroundings')
            # wolf is left and up
            if distance_x > 0 and distance_y > 0:
                # move right or down
                if self.valid_move(sheep, sheep_position[0], sheep_position[1] + 1, field):
                    return MOVE_RIGHT
                else:
                    return MOVE_DOWN
            # wolf is left and down
            if distance_x > 0 and distance_y < 0:
                # move right or up
                if self.valid_move(sheep, sheep_position[0], sheep_position[1] + 1, field):
                    return MOVE_RIGHT
                else:
                    return MOVE_UP
            # wolf is right and up
            if distance_x < 0 and distance_y > 0:
                # move left or down
                if self.valid_move(sheep, sheep_position[0], sheep_position[1] - 1, field):
                    return MOVE_LEFT
                else:
                    return MOVE_DOWN
            # wolf is right and down
            if distance_x < 0 and distance_y < 0:
                # move left and up
                if self.valid_move(sheep, sheep_position[0], sheep_position[1] - 1, field):
                    return MOVE_LEFT
                else:
                    return MOVE_UP

        else:  # this method was wrongly called
            return MOVE_NONE

    def move_sheep(self, p_num, p_state, p_time_remaining, field):
        
        if p_num == 1:
            figure = CELL_SHEEP_1
        else:
            figure = CELL_SHEEP_2
        #We prioritize running away from the wolf:
        if self.wolf_close(p_num, field):
            move = self.run_from_wolf(p_num, field)

        elif self.food_present(field) and (p_time_remaining> 0) :
            data_tree = GameTree() #we create the tree in wich we are gonna look for the best possition to reach
            l = self.possible_goals(p_num, field) # list with len 5 to parse the tree
            print(l)
            data_tree.build_tree(l)
            x=0
            for elem in l: 
                print(l[x])
                x+=1 
            
            data_tree.build_tree(l)
            busqueda = AlphaBeta(data_tree)  
            root =busqueda.getRoot()
            move = self.gather_closest_goalS(busqueda.alpha_beta_search(root), field, figure) # return the most efficient node
            

        else:
            move = MOVE_NONE

        return move, p_state

    def move_wolf(self, p_num, p_state, p_time_remaining, field):
        if p_num == 1:
            sheep_position = self.get_player_position(CELL_SHEEP_2, field)
            move = self.gather_closest_goal(sheep_position, field, CELL_WOLF_1)
        else:
            sheep_position = self.get_player_position(CELL_SHEEP_1, field)
            move = self.gather_closest_goal(sheep_position, field, CELL_WOLF_2)

        return move, p_state