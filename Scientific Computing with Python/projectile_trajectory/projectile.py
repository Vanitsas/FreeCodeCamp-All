import math

# --------------------------
# Sabitler
# --------------------------
GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

# --------------------------
# Projectile sınıfı
# --------------------------
class Projectile:
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)  # içsel olarak radyan

    def __str__(self):
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    # Displacement hesaplama
    def __calculate_displacement(self):
        v = self.__speed
        theta = self.__angle
        h = self.__height
        horizontal_component = v * math.cos(theta)
        vertical_component = v * math.sin(theta)
        sqrt_component = math.sqrt(vertical_component**2 + 2 * GRAVITATIONAL_ACCELERATION * h)
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION

    # Belirli bir x için y koordinatı
    def __calculate_y_coordinate(self, x):
        v = self.__speed
        theta = self.__angle
        h = self.__height
        return h + x * math.tan(theta) - (GRAVITATIONAL_ACCELERATION * x**2) / (2 * v**2 * math.cos(theta)**2)

    # Tüm koordinatları hesapla
    def calculate_all_coordinates(self):
        return [(x, self.__calculate_y_coordinate(x)) for x in range(math.ceil(self.__calculate_displacement()))]

    # Getters ve setters
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, s):
        self.__speed = s

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, h):
        self.__height = h

    @property
    def angle(self):
        return round(math.degrees(self.__angle))
    @angle.setter
    def angle(self, a):
        self.__angle = math.radians(a)

    def __repr__(self):
        return f'Projectile({self.speed}, {self.height}, {self.angle})'


# --------------------------
# Graph sınıfı
# --------------------------
class Graph:
    __slots__ = ('__coordinates',)

    def __init__(self, coordinates):
        self.__coordinates = coordinates

    def __repr__(self):
        return f"Graph({self.__coordinates})"

    # Koordinat tablosu
    def create_coordinates_table(self):
        table = '\n  x      y\n'
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'
        return table

    # Trajektori grafiği
    def create_trajectory(self):
        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        x_max = max(x for x, y in rounded_coords)
        y_max = max(y for x, y in rounded_coords)

        # Boş matrisi oluştur
        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        # PROJECTILE sembolünü yerleştir
        for x, y in rounded_coords:
            matrix_list[y_max - y][x] = PROJECTILE  # alt-sol köşe 0,0

        # Y ekseni ekle
        for row in matrix_list:
            row.insert(0, y_axis_tick)

        # X ekseni ekle
        x_axis_row = [x_axis_tick] * (x_max + 1)
        x_axis_row.insert(0, " ")  # sol üst köşe boş
        matrix_list.append(x_axis_row)

        # Tek multiline string hâline getir
        final_output = "\n" + "\n".join("".join(row) for row in matrix_list) + "\n"
        return final_output


# --------------------------
# Yardımcı fonksiyon
# --------------------------
def projectile_helper(speed, height, angle):
    # Projectile nesnesi
    ball = Projectile(speed, height, angle)
    print(ball)  # Detaylar

    # Koordinatları hesapla
    coordinates = ball.calculate_all_coordinates()

    # Graph nesnesi
    graph = Graph(coordinates)

    # Koordinat tablosunu yazdır
    print(graph.create_coordinates_table())

    # Grafiği yazdır
    print(graph.create_trajectory())


# --------------------------
# Örnek çağrı
# --------------------------
projectile_helper(10, 3, 45)
