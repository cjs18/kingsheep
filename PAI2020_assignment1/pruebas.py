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
sheep_position = (19,15,0)
possible_goals = [(15,19,1),(6,7,2),(7,7,3),(8,8,4),(9,9,5)]
value = 5

class GameNode:
    def __init__(self, value, parent, tupla):
        #self.Name = name      # a char, puede que no necesitemos nombre.
        self.value = value    # an int
        self.parent = parent  # a node reference
        self.children = []    # a list of nodes
        self.tupla = tupla

    def addChild(self, childNode):
        self.children.append(childNode)

    def toArray(self):
    	print("a")
    	if len(self.children) == 0:
    		return tupla
    	else:
    		aux = []
    		for child in self.children:
    			aux.append(child)
    		return aux



class GameTree:
    def __init__(self):
    	self.root = None

    def build_tree(self, data_list, sheep_position): #here we are gonna introduce the list
        """
        :param data_list: Take data in list format
        :return: Parse a tree from it
        """
       	self.root = GameNode(2, None, sheep_position) # la raiz sera posicion de la primera oveja.
        for elem in data_list:
        	auxlist = data_list
        	auxlist.remove(elem)
        	#print(elem)
        	#print(auxlist)
        	self.parse_subtree(auxlist, self.root)

    def parse_subtree(self, data_list, parent):
        # base case
        #print(data_list)
        if len(data_list)==1: #if it is the last element of the list we have a leaf
	        if type(data_list[0]) is tuple:
	            # make connections
	            leaf_node = GameNode(data_list[0][2], parent, data_list[0]) #we create the node 
	            parent.addChild(leaf_node) # we add the node to the tree
	            # if we're at a leaf, set the value
	            #if len(data_list) == 2:
	            #leaf_node.value = data_list[1]
	            return

        # recursive case
        
        for elem in data_list:
        	auxlist = data_list
        	auxlist.remove(elem)
        	print(data_list[0])
        	tree_node = GameNode(0, parent, data_list[0])
	        parent.addChild(tree_node)
        	self.parse_subtree(auxlist, tree_node)

        # return from entire method if base case and recursive case both done running
        return


    def toArray(self):
    	return self.root.toArray()


##########################
#### MAIN ENTRY POINT ####
##########################

def main():
    data_tree = GameTree()
    data_tree.build_tree(possible_goals, sheep_position)
    print(data_tree.toArray())

if __name__ == "__main__":
    main()


