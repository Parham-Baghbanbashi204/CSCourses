import arcade

a = arcade


class MyGameWindow(arcade.Window):

    def __init__(self, width, hight, title):
        super().__init__(width, hight, title)
        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.BLACK)

        self.player_x = 100
        self.player_y = 200
        self.player_speed = 300

        self.player = arcade.Sprite("sprites/playership.png", 0.1, center_x=100, center_y=100)
        self.astriod1 = arcade.Sprite("sprites/astroid.png", 0.1, center_x=300, center_y=300)
        self.astriod2 = arcade.Sprite("sprites/astroid.png", 0.1, center_x=500, center_y=500)

        self.sprite_list = arcade.SpriteList()
        self.astriod_list = arcade.SpriteList()
        self.astriod_list.append(self.astriod1)
        self.astriod_list.append(self.astriod2)
        self.sprite_list.append(self.player)

        self.right = False
        self.left = False
        self.up = False
        self.down = False

        self.player.turn_left(90)

    def on_draw(self):
        arcade.start_render()
        self.sprite_list.draw()
        self.astriod_list.draw()
        # self.player.draw()

    def on_update(self, delta_time):
        if self.right:
            self.player.turn_right(2)
            # self.player_x += self.player_speed * delta_time

        if self.left:
            self.player.turn_left(2)
            # self.player_x -= self.player_speed * delta_time
        if self.up:
            # self.player.strafe(0.1)
            # self.player_y += self.player_speed * delta_time
            self.player.forward(0.1)
        if self.down:
            # self.player.strafe(-0.1)
            # self.player_y -= self.player_speed * delta_time
            self.player.reverse(0.1)

        if self.player.collides_with_list(self.astriod_list):
            print("hit")

        # self.player.set_position(self.player_x, self.player_y)
        self.player.update()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = True
        if symbol == arcade.key.LEFT:
            self.left = True
        if symbol == arcade.key.UP:
            self.up = True

        if symbol == arcade.key.DOWN:
            self.down = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = False
        if symbol == arcade.key.LEFT:
            self.left = False
        if symbol == arcade.key.UP:
            self.up = False
            self.player.stop()
        if symbol == arcade.key.DOWN:
            self.down = False
            self.player.stop()


MyGameWindow(1280, 720, "Tutorial Window")
arcade.run()
