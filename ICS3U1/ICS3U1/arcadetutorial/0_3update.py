import arcade

a = arcade


class MyGameWindow(arcade.Window):

    def __init__(self, width, hight, title):
        super().__init__(width, hight, title)
        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.BLACK)

        self.c_x = 100
        self.c_y = 100

        self.x_speed = 300
        self.y_speed = 100

    def on_draw(self):
        arcade.start_render()
        a.draw_circle_filled(self.c_x, self.c_y, 30, a.color.RED)

    def on_update(self, delta_time):
        self.c_x += self.x_speed*delta_time
        self.c_y += self.y_speed*delta_time

        if self.c_x > 1280 - 30 or self.c_x < 0 + 30:
            self.x_speed *= -1
        if self.c_y > 720 - 30 or self.c_y < 0 + 30:
            self.y_speed *= -1


MyGameWindow(1280, 720, "Tutorial Window")
arcade.run()
