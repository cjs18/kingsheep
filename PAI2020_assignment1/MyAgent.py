"""
Kingsheep Agent Template

This template is provided for the course 'Practical Artificial Intelligence' of the University of Zürich. 

Please edit the following things before you upload your agent:
	- change the name of your file to '[uzhshortname]_A1.py', where [uzhshortname] needs to be your uzh shortname: done
	- change the name of the class to a name of your choosing : done
	- change the def 'get_class_name()' to return the new name of your class: done
	- change the init of your class:
		- self.name can be an (anonymous) name of your choosing: done
		- self.uzh_shortname needs to be your UZH shortname: done

The results and rankings of the agents will be published on OLAT using your 'name', not 'uzh_shortname', 
so they are anonymous (and your 'name' is expected to be funny, no pressure).

"""

from config import *


def get_class_name():
    return 'MyFAgent'


class MyFAgent:
    """Example class for a Kingsheep player"""

    def __init__(self):
        self.name = "CJ"
        self.uzh_shortname = "clsant"

    def get_player_position(self,figure,field):
        x = [x for x in field if figure in x][0]
        return (field.index(x), x.index(figure))

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

    def food_present(self,field):
        food_present = False

        for line in field: 
            for item in line:
                if item == CELL_RHUBARB or item == CELL_GRASS:
                    food_present = True
                    break
        return food_present

    def closest_goal(self,player_number,field):
        possible_goals = []
        
        if player_number == 1:
            sheep_position = self.get_player_position(CELL_SHEEP_1,field)
        else:
            sheep_position = self.get_player_position(CELL_SHEEP_2,field)

        #make list of possible goals
        #inicia las variables x e y to 0

        y_position = 0
        for line in field:
            x_position = 0
            for item in line:
                if item == CELL_RHUBARB or item == CELL_GRASS:
                    possible_goals.append((y_position,x_position))
                x_position += 1
            y_position += 1
        #si encuentra comida añade la posicion a la lista de posible goals si no aumenta posicion y continua buscando
        #determine closest item and return
        distance = 1000
        for possible_goal in possible_goals:
            if (abs(possible_goal[0]-sheep_position[0])+abs(possible_goal[1]-sheep_position[1])) < distance:
                distance = abs(possible_goal[0]-sheep_position[0])+abs(possible_goal[1]-sheep_position[1])
                final_goal = (possible_goal)
                
        return final_goal

    def move_sheep(self, p_num, p_state, p_time_remaining, field):
        # edit here incl. the return statement
        return MOVE_NONE, p_state

    def move_wolf(self, p_num, p_state, p_time_remaining, field):
        # edit here incl. the return statement
        return MOVE_NONE, p_state