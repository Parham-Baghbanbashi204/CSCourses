import arcade
import math
a = arcade


class MyGameWindow(arcade.Window):

    def __init__(self, width, hight, title):
        super().__init__(width, hight, title)
        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.BLACK)

        self.green_x = 100
        self.green_y = 100

        self.blue_x = 300
        self.blue_y = 300

        self.yellow_x = 500
        self.yellow_y = 500

        self.vel_y = 0
        self.vel_x = 0

    def on_draw(self):
        arcade.start_render()
        a.draw_circle_filled(self.green_x, self.green_y, 50, a.color.GREEN)
        a.draw_circle_filled(self.blue_x, self.blue_y, 50, a.color.BLUE)
        a.draw_circle_outline(self.yellow_x, self.yellow_y, 50, a.color.YELLOW, 2)

    def on_update(self, delta_time):
        self.move_yellow_circle()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.green_x = x
            self.green_y = y
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.blue_x = x
            self.blue_y = y

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.vel_y = y
        self.vel_x = x

    def move_yellow_circle(self):
        x_dist = self.vel_x - self.yellow_x
        y_dist = self.vel_y - self.yellow_y

        # distance = math.sqrt(x_dist * x_dist + y_dist * y_dist)

        distance = math.pow(x_dist * x_dist + y_dist * y_dist, 0.5)
        if distance > 1:
            self.yellow_y += y_dist * 0.1

            self.yellow_x += x_dist * 0.1


MyGameWindow(1280, 720, "Tutorial Window")
arcade.run()
