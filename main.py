import arcade
import math

# set screen dimensions (constants)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Satellite Orbit Simulator"
#Radius(Constant)
EARTH_RADIUS = 100
ORBIT_RADIUS = 150
SATELLITE_RADIUS = 5

class SatelliteSim(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        #Earth Center
        self.earth_x = SCREEN_WIDTH // 2
        self.earth_y = SCREEN_HEIGHT // 2

        #Orbit angle in radians
        self.angle = 0.0
        self.angular_velocity = 0.01 #Radians per frame

    def on_draw(self):
        self.clear()
        #Placeholder Earth
        arcade.draw_circle_filled(self.earth_x, self.earth_y,EARTH_RADIUS, arcade.color.DARK_GREEN)
        
        #Compute satellite position based on angle
        sat_x = self.earth_x + ORBIT_RADIUS * math.cos(self.angle)
        sat_y = self.earth_y + ORBIT_RADIUS * math.sin(self.angle)

        #Placeholder Satellite
        arcade.draw_circle_filled(sat_x, sat_y, SATELLITE_RADIUS, arcade.color.LIGHT_GRAY)

    def on_update(self, delta_time):
        #increment angle over time
        self.angle += self.angular_velocity

#Main Exe
def main():
    window = SatelliteSim()
    arcade.run()

if __name__ == "__main__":
    main()