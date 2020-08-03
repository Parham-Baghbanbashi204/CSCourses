import arcade

a = arcade


class MyGameWindow(arcade.Window):

    def __init__(self, width, hight, title):
        super().__init__(width, hight, title)
        self.set_location(400, 200)


MyGameWindow(1280, 720, "Tutorial Window")
arcade.run()
