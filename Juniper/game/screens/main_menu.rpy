
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like
# image main_menu_background = HBox(
#     Solid("#292835", xsize=350),
#     Solid("#21212d")
# )

image main_menu_animated:
    "gui/mm/menu3.png"
    pause 0.1
    "gui/mm/menu2.png"
    pause 0.1
    "gui/mm/menu1.png"
    pause 0.1
    "gui/mm/menu2.png"
    pause 0.1
    "gui/mm/menu3.png"
    pause 0.1
    "gui/mm/menu4.png"
    choice:
        2.5
    choice:
        4.1
    choice:
        1.1
    choice:
        3.2
    choice:
        0.2
    repeat

image main_menu_background="gui/main_menu_background.png"

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main_menu_animated"

    # vbox:
    #     xpos 60
    #     yalign 0.5
    #     spacing 6

    #     textbutton _("Start") action Start()

    #     textbutton _("Load") action ShowMenu("load")

    #     textbutton _("Preferences") action ShowMenu("preferences")

    #     #textbutton _("About") action ShowMenu("about")

    #     # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

    #     #     ## Help isn't necessary or relevant to mobile devices.
    #     #     textbutton _("Help") action ShowMenu("help")

    #     if renpy.variant("pc"):

    #         ## The quit button is banned on iOS and unnecessary on Android and
    #         ## Web.
    #         textbutton _("Quit") action Quit(confirm=not main_menu)

    fixed:
        #yalign 0.0
        #spacing 6

        #textbutton _("Start") action Start()
        imagebutton auto "gui/mm/mm_newgame_%s.png" xpos 1432 ypos 110 focus_mask True action Start() hovered [ Play ("sound", "audio/effect2.mp3")]

        #textbutton _("Load") action ShowMenu("load")
        imagebutton auto "gui/mm/mm_loadgame_%s.png" xpos 1416 ypos 238 focus_mask True action ShowMenu("load") hovered [ Play ("sound", "audio/effect2.mp3")]

        #textbutton _("Preferences") action ShowMenu("preferences")
        imagebutton auto "gui/mm/mm_options_%s.png" xpos 1528 ypos 372 focus_mask True action ShowMenu("preferences") hovered [ Play ("sound", "audio/effect2.mp3")]

        #textbutton _("About") action ShowMenu("about")

        # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        #     ## Help isn't necessary or relevant to mobile devices.
        #     textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            imagebutton auto "gui/mm/mm_quit_%s.png" xpos 1601 ypos 494 focus_mask True action Quit(confirm=not main_menu) hovered [ Play ("sound", "audio/effect2.mp3")]
            #textbutton _("Quit") action Quit(confirm=not main_menu)

