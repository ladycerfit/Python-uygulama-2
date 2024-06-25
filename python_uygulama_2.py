##Noktaların Tanımlanması (points list):

points = [(1, 2), (4, 6), (5, 7), (8, 10)]

##Öklid Mesafesi İçin Bir Fonksiyon Yazma (eucledianDistance):
##euclidean_distance = ((x2 – x1)^2 + (y2 – y1)^2)^1/2

def euclideanDistance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

##Mesafelerin Hesaplanması (distances list):

distances = []
for x in range(len(points)):
    for y in range(x + 1, len(points)):
        distance = euclideanDistance(points[x], points[y])
        distances.append(distance)

##Minimum Mesafenin Bulunması (min ve print):  
      
min_dis = min(distances)
print(f"Minimum Mesafe: {min_dis:}")
