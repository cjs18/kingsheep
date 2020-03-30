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
possible_goals = [(13,19),(4,3),(2,5),(2,4),(5,6),(7,9)]

class GameNode:
    def __init__(self, parent):
        #self.Name = name      # a char, puede que no necesitemos nombre.
        self.value = None    # an int
        self.parent = parent  # a node reference
        self.children = []    # a list of nodes
        #self.tupla = tupla

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
       	self.root = GameNode(data_list[0],data_list[0]) #the first possition of the list will be the root
        data_list.remove(data_list[0]) #remove the first element 
        self.sub_tree(data_list, self.root)
    
    def sub_tree(self, data_list,parent):
        if len(data_list)==0:
            return
        if len(data_list)==1:
            tree_node = GameNode(parent,data_list[0])
            print('El nodo hoja:', tree_node.getValue(), 'ha sido añadido al padre:', parent.getValue())
            parent.addChild(tree_node) # We add a leaf in the tree
            return
        #if the list contain more than one node: 
        x=0
        for elem in data_list:
            auxlist= data_list.copy()
            tree_node = GameNode(parent,data_list[x])
            parent.addChild(tree_node)
            print('El nodo:', tree_node.getValue(), 'ha sido añadido al padre:', parent.getValue())
            x+=1
            #if len(auxlist)>=2:
            auxlist.remove(tree_node.getValue())
            print(auxlist)
            print('Esta es la nueva lista que estoy pasando: ', auxlist)
            print('--- FIN LOOP ---')
            self.sub_tree(auxlist,tree_node)
       

    

    def toArray(self):
    	return self.root.toArray()
    
    def searchtree(self):
        
        queue = SimpleQueue()

        if not(self.root==None): 
            rot= self.getRoot()
            print(rot.getValue())
            aux= rot.getChildren()
            for i in aux:
                print(i.getValue())
            print('Hasta aqui los hijos del root')
            for elem in aux: 
                queue.put(elem)
            while(not queue.empty()): 
                x = queue.get()
                print('child')
                print(x.getValue(),x.getParent().getValue())

                for elem in x.getChildren():
                    queue.put(elem)

    def imprimir(self):
        for elem in self.root:
            print(elem.value())

class AlphaBeta:
    # print utility value of root node (assuming it is max)
    # print names of all nodes visited during search
    def __init__(self, game_tree):
        self.game_tree = game_tree  # GameTree
        self.root = game_tree.getRoot()  # GameNode
        
    def getRoota(self): 
        return self.root.getValue()
    def getRoot(self): 
        return self.root

    def is_leaf(self,node): 
        return len(node.getChildren())==0 

    def alpha_beta_search(self, node):
        infinity = float('inf') #unbounded upper value for comparison
        best_val = -infinity  #alpha 
        beta = infinity       #beta 

        successors = node.getChildren()
        best_state = None
        for state in successors:
            value = self.min_value(state, best_val, beta)
            if value > best_val:
                best_val = value
                best_state = state
        print('AlphaBeta:  Utility Value of Root Node: = ' , str(best_val))
        print('AlphaBeta:  Best State is: ' , best_state.getValue())
        return best_state

    def max_value(self, node, alpha, beta):
        print("AlphaBeta-->MAX: Visited Node :: " , node.getValue()) 
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
        print('AlphaBeta-->MIN: Visited Node :: ' , node.getValue()) 
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
#### MAIN ENTRY POINT ####
##########################

def main():
    data_tree = GameTree()
    data_tree.build_tree(possible_goals)
    #print(data_tree.toArray())
    data_tree.searchtree()
    busqueda = AlphaBeta(data_tree)
    print(busqueda.getRoota())
    root =busqueda.getRoot()
    print(root)
    busqueda.alpha_beta_search(root)
    #alpha_beta_search(busqueda.getRoota())
   
if __name__ == "__main__":
    main()

    # llamar getsuccesors al metodo get children.

