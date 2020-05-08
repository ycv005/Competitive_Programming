class Solution:
    def checkStraightLine(self, coordinates):
        # two points always makes a straight line
        if len(coordinates) == 2: return True
        x0, y0 = coordinates.pop(0)
        x1, y1 = coordinates.pop(0)
        for x2, y2 in coordinates:
            if (y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0): return False
        return True
