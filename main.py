import arcade
import math

# set screen dimensions (constants)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Satellite Orbit Simulator"
#Radius(Constant)
EARTH_RADIUS = 100
ELLIPSE_RADIUS_X = 180 #Major axis
ELLIPSE_RADIUS_Y = 115 #Minor axis
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

    def on_draw(self):
        self.clear()
        #Placeholder Earth
        arcade.draw_circle_filled(self.earth_x, self.earth_y,EARTH_RADIUS, arcade.color.DARK_GREEN)
        
        #Compute satellite position on an ellipse
        sat_x = self.earth_x + ELLIPSE_RADIUS_X * math.cos(self.angle)
        sat_y = self.earth_y + ELLIPSE_RADIUS_Y * math.sin(self.angle)

        #Placeholder Satellite
        arcade.draw_circle_filled(sat_x, sat_y, SATELLITE_RADIUS, arcade.color.LIGHT_GRAY)

    def on_update(self, delta_time):
        #Variable based on distance
        a = ELLIPSE_RADIUS_X
        b = ELLIPSE_RADIUS_Y

        #Compute satellite position
        x = a * math.cos(self.angle)
        y = b * math.sin(self.angle)

        #Distance to center (Earth)
        r = math.sqrt(x**2 + y**2)

        #Speed is inversely proportional to distanse 
        angular_velocity = 2 / r

        self.angle += angular_velocity + delta_time

#Main Exe
def main():
    window = SatelliteSim()
    arcade.run()

if __name__ == "__main__":
    main()