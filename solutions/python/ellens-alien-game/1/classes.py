"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    health=3
    total_aliens_created=0
    def __init__(self,a,b):
        self.x_coordinate=a
        self.y_coordinate=b
        Alien.total_aliens_created+=1
    def hit(self): 
        self.health-=1
        return self.health
    def is_alive(self):
        return self.health>0
    def teleport(self,a,b):
        self.x_coordinate=a
        self.y_coordinate=b 
    def collision_detection(self,other_object):
        pass
    

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(positions):
    aliens=[]
    for a,b in positions:
        alien=Alien(a,b)
        aliens.append(alien)
    return aliens
    
