import arcade

a = arcade


class MyGameWindow(arcade.Window):

    def __init__(self, width, hight, title):
        super().__init__(width, hight, title)
        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

    def on_update(self, delta_time):
        pass


MyGameWindow(1280, 720, "Tutorial Window")
arcade.run()