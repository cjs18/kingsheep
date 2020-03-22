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

from ast import literal_eval
import sys

##########################
###### PARSE DATA ########
##########################
possible_goals = [(15,19),(6,7),(7,7),(8,8),(9,9)]
value = 5

class GameNode:
    def __init__(self, name, value=0, parent=None):
        #self.Name = name      # a char, puede que no necesitemos nombre.
        self.value = value    # an int
        self.parent = parent  # a node reference
        self.children = []    # a list of nodes

    def addChild(self, childNode):
        self.children.append(childNode)

class GameTree:
    def __init__(self):
        self.root = None

    def build_tree(self, data_list,): #here we are gonna introduce the list
        """
        :param data_list: Take data in list format
        :return: Parse a tree from it
        """
       	self.root = GameNode(data_list[0]) # la raiz sera posicion de la primera oveja.
        for elem in data_list:
            self.parse_subtree(data_list.remove(data_list[0]), self.root)

    def parse_subtree(self, data_list, parent):
        # base case
        if len(data_list)==1: #if it is the last element of the list we have a leaf
	        if type(data_list) is tuple:
	            # make connections
	            leaf_node = GameNode(data_list[0]) #we create the node 
	            leaf_node.parent = parent
	            leaf_node.value= value  #establish the node 
	            parent.addChild(leaf_node) # we add the node to the tree
	            # if we're at a leaf, set the value
	            #if len(data_list) == 2:
	            #leaf_node.value = data_list[1]
	            return

        # recursive case
        tree_node = GameNode(data_list.pop())
        # make connections
        tree_node.parent = parent
        parent.addChild(tree_node)
        for elem in data_list:
            self.parse_subtree(elem, tree_node)

        # return from entire method if base case and recursive case both done running
        return

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret


##########################
#### MAIN ENTRY POINT ####
##########################

def main():
    data_tree = GameTree()
    data_tree.build_tree(possible_goals)
    str(data_tree)
    print(data_tree)

if __name__ == "__main__":
    main()


