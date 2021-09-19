init python:
    def get_all_locations_academy_campus_names():
        rtn = []
        for i in locations_academy+locations_campus:
            rtn.append(i.image[39:-4])
        return rtn


transform inventory_interface_transform:

    on show:
        xpos 2000
        ypos 130
        easein_quart .5 xpos 1300
    on hide:

        xpos 1300
        ypos 130
        easeout_quart .5 xpos 2000


screen inventory_interface_screen:








    zorder 220
    imagebutton:
        idle '#000a'
        hover '#000a'
        action Hide('inventory_interface_screen', transition = Dissolve(.5)), Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_close.mp3')
    viewport:
        at inventory_interface_transform

        xmaximum 430
        ymaximum 507
        image '#fff0'
        imagebutton:
            idle 'main_inventory_bg'
            hover 'main_inventory_bg'
            action NullAction()
        imagebutton:
            idle  'inventory_interface/close_inventory.png'
            hover im.MatrixColor('inventory_interface/close_inventory.png', im.matrix.brightness(.3))
            action Hide('inventory_interface_screen', transition = Dissolve(.5)), Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_close.mp3')
            xalign .985
            ypos 4
        viewport:
            xmaximum 100
            ymaximum 50
            xpos 90
            ypos 32
            add '#FFF0'
            text '{color=#5eab42}${/color}'+ str(money) font 'fonts/h_font.ttf' size 25 xalign .5 yalign .5 color '#FFF'
        hbox:
            xpos 8
            ypos 80
            if books_gg:
                viewport:
                    xmaximum 83
                    ymaximum 85

                    add '#FFF0'

                    add 'books_for_inventory' zoom .7 xalign .5 yalign .7

                    viewport:
                        xmaximum 37
                        ymaximum 37
                        image 'inventory_ellipse' 
                        text str(books_gg) color '#535067' size 14 font 'fonts/h_font.ttf' xalign .5 yalign .5
                        yalign 1.0


            viewport:
                xmaximum 83
                ymaximum 85


                add '#FFF0'
                if hasattr(store, 'potions') and potions['Lesser Heal']:
                    add 'mini_games/duels/Lesser Heal.png' zoom .5 xalign .5 yalign .5

                    viewport:
                        xmaximum 37
                        ymaximum 37
                        image 'inventory_ellipse' 
                        text str(potions['Lesser Heal']) color '#535067' size 14 font 'fonts/h_font.ttf' xalign .5 yalign .5
                        yalign 1.0
































        key "rollback" action NullAction()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
