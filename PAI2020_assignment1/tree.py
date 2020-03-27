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
possible_goals = ['A','B','C','D']

class GameNode:
    def __init__(self, parent,value):
        #self.Name = name      # a char, puede que no necesitemos nombre.
        self.value = value    # an int
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
            
    def toArray(self):
    	print("root")
    	if len(self.children) == 0:
    		return 0
    	else:
    		aux = []
    		for child in self.children:
    			aux.append(child)
    		return aux
    def isEmpty(self): 
        return len(self.root)==0 
    
   
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


                         
##########################
#### MAIN ENTRY POINT ####
##########################

def main():
    data_tree = GameTree()
    data_tree.build_tree(possible_goals)
    #print(data_tree.toArray())
    data_tree.searchtree()
   
if __name__ == "__main__":
    main()