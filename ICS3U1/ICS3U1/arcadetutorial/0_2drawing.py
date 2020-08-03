import arcade

a = arcade


class MyGameWindow(arcade.Window):

    def __init__(self, width, hight, title):
        super().__init__(width, hight, title)
        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        a.start_render()
        a.draw_lines([(0, 0), (100, 100)], a.color.RED, 4)
        a.draw_point(150, 150, a.color.WHITE, 20)
        a.draw_circle_filled(250, 150, 50, a.color.GREEN, 50)
        a.draw_circle_outline(450, 200, 50, a.color.BLUE, 2, 50)
        a.draw_lrtb_rectangle_filled(500, 600, 600, 500, arcade.color.BLUE)


MyGameWindow(1280, 720, "Tutorial Window")
arcade.run()