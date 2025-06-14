import arcade
import math

# set screen dimensions (constants)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Satellite Orbit Simulator"
#Earth(Constant)
EARTH_RADIUS = 100
EARTH_MASS = 5.972e24 #Will be used later
GRAVITY_CONSTANT = 1.0
#Satellite(Constant)
SATELLITE_RADIUS = 5
INITIAL_DISTANCE = 200 #From Earth center
INITIAL_SPEED = 2.3 #user-defined

class OrbitView(arcade.View):
    def __init__(self):
        super().__init__()
        #Earth Center
        self.earth_x = SCREEN_WIDTH // 2
        self.earth_y = SCREEN_HEIGHT // 2

        #Satellite State
        self.satellite_x = self.earth_x + INITIAL_DISTANCE
        self.satellite_y = self.earth_y

        self.vx = 0
        self.vy = 0
        self.launched = False

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        #Placeholder Earth
        arcade.draw_circle_filled(self.earth_x, self.earth_y, EARTH_RADIUS, arcade.color.DARK_GREEN)
        
        #Placeholder Satellite
        arcade.draw_circle_filled(self.satellite_x, self.satellite_y, SATELLITE_RADIUS, arcade.color.LIGHT_GRAY)

        #Draw velocity vector
        if self.launched:
            arcade.draw_line(self.satellite_x, self.satellite_y,
                             self.satellite_x + self.vx * 10,
                             self.satellite_y + self.vy * 10,
                             arcade.color.YELLOW, 2)

    def on_update(self, delta_time):
        if not self.launched:
            return
        print("update position")

        #Vector from Satellite to Earth center
        dx = self.earth_x - self.satellite_x
        dy = self.earth_y - self.satellite_y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < EARTH_RADIUS:
            print("Impact Detected")
            self.launched = False
            return

        #Gravitational Force (simplified)
        force = GRAVITY_CONSTANT / (distance ** 2)
        angle = math.atan2(dy, dx)
        ax = force * math.cos(angle)
        ay = force * math.sin(angle)

        #Update velocity
        self.vx += ax * delta_time * 69000
        self.vy += ay * delta_time * 69000

        #Update Position
        self.satellite_x += self.vx
        self.satellite_y += self.vy

        
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            if self.launched:
                return
            self.launched = True
# Vector from Earth to satellite
        dx = self.satellite_x - self.earth_x
        dy = self.satellite_y - self.earth_y
        distance = math.sqrt(dx**2 + dy**2)
        print(f"dx={dx}, dy={dy}, distance={distance}")

        if distance == 0:
            print("Satellite is at Earth's center! Cannot launch.")
            self.launched = False
            return

        # Normalize to get radial direction
        nx = dx / distance
        ny = dy / distance

        # Rotate 90 degrees to get tangential direction
        tx = -ny
        ty = nx
        print(f"Tangent vector: tx={tx}, ty={ty}")

        # Apply tangential initial velocity
        self.vx = INITIAL_SPEED * tx
        self.vy = INITIAL_SPEED * ty
        

#Main Exe
def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = OrbitView()
    window.show_view(view)
    arcade.run()

if __name__ == "__main__":
    main()