"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Name:  arcade_assignment.py
Purpose: Part 2 to the cs assignment

Author: Baghbanbashi.P
Date Created: 04/05/2019

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
import arcade
import time
arcade.open_window(800,800,"Effects Of Tecnolagy On Human Health")
arcade.set_background_color(arcade.color.WHITE)

poppy = arcade.load_texture("images/poppy.jpg")
workspace = arcade.load_texture("images/compter.jpg")


def draw_textures():
    """
        draws the required textures
    """

    arcade.draw_texture_rectangle(750, 50, 100, 100, poppy)
    arcade.draw_texture_rectangle(400,400, 400, 400, workspace)


def draw_circle(x, y, size):
    """draws circles

    Arguments:
        x {int} -- x location
        y {int} -- y location
        size {int} -- radius of circle

    """

    arcade.draw_circle_filled(x, y, size, arcade.color.RED)


def draw_text(text, x, y, color, size):
    arcade.draw_text(text, x, y, color, size)
    """draws text

    Arguments:
        text {string} -- determines string text
        x {int} -- x location
        y {int} -- y location
        size {int} -- font size of text 
        color {arcade.color} -- color of text

    """

def draw_all():
    draw_text("Long times at a computer will cause pain in the following areas", 100, 700, arcade.color.BLACK, 16)
    draw_textures()
    """draws all items on the screen 

    """


def on_draw(delta_time):
    """draws animation
    """

    global pain
    global timer
    draw_all()
    timer += 1

    if timer > 100:

        draw_circle(300, 530, pain)
        draw_circle(300, 450, pain)
        draw_circle(270, 400, pain)

    if timer > 150:
        pain += 5

    if pain > 650:
        draw_text("To Prevent Pain", 100, 700, arcade.color.BLACK, 50)
        draw_text("Take A Break Every ", 100, 600, arcade.color.BLACK, 50)
        draw_text("20 Minutes", 100, 500, arcade.color.BLACK, 50)


pain = 10
timer = 0


def main():
    """runs program
    """
    arcade.start_render()
    arcade.schedule(on_draw, 1/60)

    arcade.run()


main()
