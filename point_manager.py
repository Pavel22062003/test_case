from shapely.geometry import Point


class PointManager:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def find_distance(self, x, y):
        distance = Point(self.x_coord, self.y_coord).distance(Point(x, y))
        return round(distance, 2)

#Example
# manager = PointManager(x=1, y=2)
# print(manager.find_distance(2, 3))
# manager.x_coord = 10
# print(manager.find_distance(2, 3))
