from shapely.geometry import Point, LineString, Polygon

point1 = Point(0,0)
point2 = Point(1,1)
point3 = Point(0,3)

line1 = LineString([point1, point2, point3])
print(line1)

line2 = LineString([(0,0), (3,1), (0,3)])
print(line2)

polygon = Polygon([[p.x, p.y] for p in [point1, point2, point3]])
print(polygon)