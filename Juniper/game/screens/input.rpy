
## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    frame:
        background Frame("gui/inputbox.png")
        xalign 0.5
        yalign 0.5
        padding (200, 100)
        vbox:
            spacing 15
            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    properties gui.text_properties("input_prompt")
    font gui.interface_text_font
    xalign 0.0

style input:
    color '#83d894'
    xalign 0.5
    yalign 0.5
    xmaximum 1116


