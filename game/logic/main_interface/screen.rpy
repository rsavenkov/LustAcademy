












screen black_tmp_screen_menu:
    zorder 205
    imagebutton:
        idle '#0000'
        hover '#0000'
        action NullAction()
    #timer .5 action Hide('show_hide_locations'), Hide('show_hide_locations_2')





screen pass_screen():
    $ pass
image inventory_button:

    on idle:
        "images/main_interface/inventory_button_circle.png" with Dissolve(.2)
    on hover:
        im.MatrixColor("images/main_interface/inventory_button_circle.png", im.matrix.brightness(.3)) with Dissolve(.2)



image head_button:

    on idle:
        "images/main_interface/heads_button_circle.png" with Dissolve(.2)
    on hover:
        im.MatrixColor("images/main_interface/heads_button_circle.png", im.matrix.brightness(.3)) with Dissolve(.2)




image skip_button:

    on idle:
        "images/main_interface/skip_button.png" with Dissolve(.2)
    on hover:
        im.MatrixColor("images/main_interface/skip_button.png", im.matrix.brightness(.3)) with Dissolve(.2)



image hide_button:

    on idle:
        'locations_main/location_buttons/hide_button.png' with Dissolve(.2)
    on hover:
        im.MatrixColor('locations_main/location_buttons/hide_button.png', im.matrix.brightness(.3)) with Dissolve(.2)



image show_button:

    on idle:
        'locations_main/location_buttons/show_button.png' with Dissolve(.2)
    on hover:
        im.MatrixColor('locations_main/location_buttons/show_button.png', im.matrix.brightness(.3)) with Dissolve(.2)

image map_button:

    on idle:
        "images/main_interface/map_button_circle.png" with Dissolve(.2)
    on hover:
        im.MatrixColor("images/main_interface/map_button_circle.png", im.matrix.brightness(.3)) with Dissolve(.2)


image notebook_button:

    on idle:
        "images/main_interface/notebook_button_circle.png" with Dissolve(.2)
    on hover:
        im.MatrixColor("images/main_interface/notebook_button_circle.png", im.matrix.brightness(.3)) with Dissolve(.2)


screen olivia_bag(money=False):
    imagebutton:
        idle '#0000'
        hover '#0000'
        action Return('exit')
    if not hasattr(store, 'olivia_bag_n_bag'):
        imagebutton:
            idle 'images/main_interface/locations/IMG_3107_0.png'
            hover 'images/main_interface/locations/IMG_3107.png'
            focus_mask True
            hovered Function(show_up_donw_text, text_now = "Makeup bag", x_now = 850, y_now = 400+100)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            action Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Return('bag')
    if money:
        imagebutton:
            idle 'images/main_interface/locations/IMG_3106_0.png'
            hover 'images/main_interface/locations/IMG_3106.png'
            focus_mask True
            hovered Function(show_up_donw_text, text_now = "Money", x_now = 850, y_now = 500+100)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            action Return('money')

screen don_cupboard(money=False):
    imagebutton:
        idle '#0000'
        hover '#0000'
        action Return('exit')
    if not hasattr(store, 'don_cupboard_1'):
        imagebutton:
            idle 'images/main_interface/locations/DON_CUPBOARD/1_0.png'
            hover 'images/main_interface/locations/DON_CUPBOARD/1_0.png'
            focus_mask True
            hovered Function(show_up_donw_text, text_now = "Documents", x_now = 920, y_now = 650)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            action Return('1')

    imagebutton:
        idle 'images/main_interface/locations/DON_CUPBOARD/2_0.png'
        hover 'images/main_interface/locations/DON_CUPBOARD/2_0.png'
        focus_mask True
        if not hasattr(store, 'don_cupboard_2'):
            hovered Function(show_up_donw_text, text_now = "Condoms", x_now = 940, y_now = 650)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            action Return('2')
        else:
            action NullAction()

    if not hasattr(store, 'don_cupboard_3'):
        imagebutton:
            idle 'images/main_interface/locations/DON_CUPBOARD/3_0.png'
            hover 'images/main_interface/locations/DON_CUPBOARD/3_0.png'
            focus_mask True
            hovered Function(show_up_donw_text, text_now = "Book", x_now = 720, y_now = 650)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            action Return('3')
screen add_book():
    zorder 300
    imagebutton:
        idle '#000a'
        hover '#000a'
        action NullAction()
    viewport:
        at hide_my_choice
        xmaximum 700
        ymaximum 426
        yalign .5
        xalign .5

        add 'caffe_menu_bg'
        viewport:
            xalign .5 yalign .5
            xmaximum 400
            ymaximum 300
            add '#0000'
            #text '??????, ???? ?????????? ??????????! ???????? ?? ???????????????????? ?? ???????????? ???????? ????????????????????' xalign .5 yalign .5

        textbutton 'Ok' action Hide('add_book', transition = Dissolve(.5)) xalign .5 yalign .99


init python:
    def books_pop(i):
        global books_now
        books_now.pop(i, 0)
    lightning = False
screen main_interface():
    key "rollback" action NullAction()
    



    if not persistent.from_gallery:
        if not renpy.get_screen('inventory_interface_screen'):

            key "i" action Show('inventory_interface_screen', transition = Dissolve(.3)), Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_open.mp3')
            key "I" action Show('inventory_interface_screen', transition = Dissolve(.3)), Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_open.mp3')
        else:
            key "i" action Hide('inventory_interface_screen', transition = Dissolve(.3)), Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_open.mp3')
            key "I" action Hide('inventory_interface_screen', transition = Dissolve(.3)), Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_open.mp3')

        if not renpy.get_screen('lustagram_screen'):
            key "p" action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Phone_take.mp3'), Show('lustagram_screen', transition = Dissolve(.3)), Function(renpy.play, channel = 'sound', filename = 'audio/Iphone.mp3')
            key "P" action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Phone_take.mp3'), Show('lustagram_screen', transition = Dissolve(.3)), Function(renpy.play, channel = 'sound', filename = 'audio/Iphone.mp3')
        else:
            key "p" action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Phone_take.mp3'), Hide('lustagram_screen', transition = Dissolve(.3)), Function(renpy.play, channel = 'sound', filename = 'audio/Iphone.mp3')
            key "P" action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Phone_take.mp3'),     Hide('lustagram_screen', transition = Dissolve(.3)), Function(renpy.play, channel = 'sound', filename = 'audio/Iphone.mp3')

        if not renpy.get_screen('map_screen'):
            key "m" action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Open_latter.mp3'), Show('map_screen', transition = Dissolve(.5))
            key "M" action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Open_latter.mp3'), Show('map_screen', transition = Dissolve(.5))

        else:
            key "m" action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Open_latter.mp3'), Hide('map_screen', transition = Dissolve(.5))
            key "M" action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Open_latter.mp3'), Hide('map_screen', transition = Dissolve(.5))

        if not renpy.get_screen('quest_log_screen'):
            key "Q" action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_open.mp3'), Show('quest_log_screen', transition = Dissolve(.5))

            key "q" action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_open.mp3'), Show('quest_log_screen', transition = Dissolve(.5))

        else:
            key "Q" action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_open.mp3'), Hide('quest_log_screen', transition = Dissolve(.5))

            key "q" action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_open.mp3'), Hide('quest_log_screen', transition = Dissolve(.5))




        if lightning:
            key "L" action SetVariable('lightning', False)
            key "l" action SetVariable('lightning', False)
        else:
            key "L" action SetVariable('lightning', True)
            key "l" action SetVariable('lightning', True)





    $ time_now_texts = {
    1:'MORNING',
    2:'DAY',
    3:'EVENING',
    4:'NIGHT',
    



    }


    $ check_dow = (dow == 'SAT' and time_now != 1) or (dow == 'SUN')










    if location_now == 'gg_room':
        imagebutton:
            if lightning:
                idle 'images/main_interface/locations/gg_room_door.png'
            
            else:
                idle Transform('images/main_interface/locations/gg_room_door.png', alpha = .1)
            hover 'images/main_interface/locations/gg_room_door.png'
            hovered Function(show_up_donw_text, text_now = 'Corridor', x_now = 920, y_now = 200)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            focus_mask True

            action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'corridor')





















    if location_now == 'leon_bathroom':
        imagebutton:
            if lightning:
                idle im.MatrixColor('locations_main/items/bathroom/leon_bathroom_1.Door.png', im.matrix.brightness(.2))
            else:
                idle 'locations_main/items/bathroom/leon_bathroom_1.Door.png'
            hover im.MatrixColor('locations_main/items/bathroom/leon_bathroom_1.Door.png', im.matrix.brightness(.2))
            hovered Function(show_up_donw_text, text_now = 'Living Room', x_now = 1600, y_now = 250)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            focus_mask True
            action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'leon_living')
        imagebutton:
            if lightning:
                idle im.MatrixColor('locations_main/items/bathroom/leon_bathroom_1.Duks.png', im.matrix.brightness(.2))
            else:
                idle 'locations_main/items/bathroom/leon_bathroom_1.Duks.png'
            hover im.MatrixColor('locations_main/items/bathroom/leon_bathroom_1.Duks.png', im.matrix.brightness(.2))
            focus_mask True
            action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Duck_click.mp3')

    if location_now == 'leon_corridor':

        imagemap:
            if lightning:
                ground 'locations_main/items/corridor/leon_corridor_'+str(time_now)+'_2.png'

            else:
                ground '#0000'
            hover 'locations_main/items/corridor/leon_corridor_'+str(time_now)+'_2.png'

            hotspot hotspots['leon_corridor']['door_1']:
                hovered Function(show_up_donw_text, text_now = 'Girls Room 1', x_now = 200, y_now = 250)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                focus_mask None
                clicked Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'leon_room_hl')




            hotspot hotspots['leon_corridor']['door_2']:

                hovered Function(show_up_donw_text, text_now = 'Girls Room 2', x_now = 780, y_now = 250)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                focus_mask None
                clicked Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'leon_room_sa')

            hotspot hotspots['leon_corridor']['door_3']:

                hovered Function(show_up_donw_text, text_now = 'My Room', x_now = 1180, y_now = 250)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                focus_mask None
                clicked Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'leon_room_mc')


            hotspot hotspots['leon_corridor']['stairs']:

                hovered Function(show_up_donw_text, text_now = "Living Room", x_now = 1400, y_now = 900)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                focus_mask None
                clicked Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'leon_living')




    if location_now == 'leon_room_mc':
        imagemap:
            if lightning:
                ground 'locations_main/items/leon_room_mc/leon_room_mc_'+str(time_now)+'_2.png'

            else:
                ground '#0000'
            hover 'locations_main/items/leon_room_mc/leon_room_mc_'+str(time_now)+'_2.png'

            hotspot hotspots['leon_room_mc']['door_1']:
                focus_mask None
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                hovered Function(show_up_donw_text, text_now = 'Corridor', x_now = 110, y_now = 300)
                clicked Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, 'leon_corridor')





            if not hasattr(store, 'picture_in_mc_room_variable'):
                hotspot hotspots['leon_room_mc']['picture']:
                    focus_mask None

                    clicked Jump('picture_in_mc_room')


            if not hasattr(store, 'rune_in_mc_room_variable'):

                hotspot hotspots['leon_room_mc']['rune']:
                    focus_mask None

                    clicked Jump('rune_in_mc_room')





            hotspot hotspots['leon_room_mc']['door_2']:
                focus_mask None

                clicked Jump('close_room_label'), Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'),


            if time_now == 4:
                if Q_Lily != 4:
                    hotspot hotspots['leon_room_mc']['bed']:
                        focus_mask None

                        hovered Function(show_up_donw_text, text_now = 'Sleep', x_now = 800, y_now = 600)
                        unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                        clicked Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location_2, location_now, time_now+1, sleep = True)






        if time_now == 4:


            if Q_Lily == 4:

                add 'locations_main/items/leon_room_mc/lily_leon_room_mc_4.1.png'

                imagebutton:
                    focus_mask True
                    idle 'locations_main/items/leon_room_mc/lily_leon_room_mc_4.1.png'
                    if getattr(store, 'lily_events_4', None) is not None:
                        hover im.MatrixColor('locations_main/items/leon_room_mc/lily_leon_room_mc_4.1.png', im.matrix.brightness(.2))
                        action Jump('lily_events_4_label')

                    else:
                        hover 'locations_main/items/leon_room_mc/lily_leon_room_mc_4.1.png'
                        action NullAction()






    if location_now == 'leon_room_hl':
        if time_now == 3:

            if Q_Haley in [1, 7, 11]:

                add 'locations_main/items/leon_room_hl/haley_leon_room_hl_3.1.png'
                imagebutton:
                    if lightning:
                        idle im.MatrixColor('locations_main/items/leon_room_hl/haley_leon_room_hl_3.2.png', im.matrix.brightness(.2))
                    else:
                        idle 'locations_main/items/leon_room_hl/haley_leon_room_hl_3.2.png'
                    hover im.MatrixColor('locations_main/items/leon_room_hl/haley_leon_room_hl_3.2.png', im.matrix.brightness(.2))

                    focus_mask True

                    action Jump('haley_events_3_label')



            imagebutton:
                if lightning:
                    idle im.MatrixColor('locations_main/items/leon_room_hl/haley_leon_room_hl_4.Door.png', im.matrix.brightness(.2))

                else:
                    idle Transform('locations_main/items/leon_room_hl/haley_leon_room_hl_4.Door.png', alpha = .1)

                hover im.MatrixColor('locations_main/items/leon_room_hl/haley_leon_room_hl_4.Door.png', im.matrix.brightness(.2))
                hovered Function(show_up_donw_text, text_now = 'Corridor', x_now = 1700, y_now = 250)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                focus_mask True
                action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'leon_corridor')

        else:
            imagebutton:
                if lightning:
                    idle im.MatrixColor('locations_main/items/leon_room_hl/haley_leon_room_hl_4.Door.png', im.matrix.brightness(.2))

                else:
                    idle Transform('locations_main/items/leon_room_hl/haley_leon_room_hl_4.Door.png', alpha = .1)

                hover im.MatrixColor('locations_main/items/leon_room_hl/haley_leon_room_hl_4.Door.png', im.matrix.brightness(.2))
                hovered Function(show_up_donw_text, text_now = 'Corridor', x_now = 1700, y_now = 250)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                focus_mask True
                action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'leon_corridor')

        if time_now == 4:




            if Q_Lily != 4:
                imagebutton:
                    focus_mask True
                    if lightning:
                        idle im.MatrixColor('locations_main/items/leon_room_hl/lily_leon_room_hl_4.2.png', im.matrix.brightness(.2))
                    else:
                        idle 'locations_main/items/leon_room_hl/lily_leon_room_hl_4.2.png'
                    if getattr(store, 'lily_events_5', None) is not None:

                        hover im.MatrixColor('locations_main/items/leon_room_hl/lily_leon_room_hl_4.2.png', im.matrix.brightness(.2))
                        action Jump('lily_events_5_label')

                    else:
                        hover 'locations_main/items/leon_room_hl/lily_leon_room_hl_4.2.png'
                        action NullAction()

            add 'locations_main/items/leon_room_hl/haley_leon_room_hl_4.1.png'

            imagebutton:
                focus_mask True
                if lightning:
                    idle im.MatrixColor('locations_main/items/leon_room_hl/haley_leon_room_hl_4.2.png', im.matrix.brightness(.2))
                
                else:
                    idle 'locations_main/items/leon_room_hl/haley_leon_room_hl_4.2.png'

                hover im.MatrixColor('locations_main/items/leon_room_hl/haley_leon_room_hl_4.2.png', im.matrix.brightness(.2))
                
                action Jump('haley_events_4_label')

    if location_now == 'leon_room_sa':

        imagebutton:
            if lightning:
                idle im.MatrixColor('locations_main/items/leon_room_sa/leon_room_sa_'+str(time_now)+'.Door.png', im.matrix.brightness(.2))

            else:
                idle 'locations_main/items/leon_room_sa/leon_room_sa_'+str(time_now)+'.Door.png'
            hover im.MatrixColor('locations_main/items/leon_room_sa/leon_room_sa_'+str(time_now)+'.Door.png', im.matrix.brightness(.2))

            focus_mask True

            hovered Function(show_up_donw_text, text_now = "Corridor", x_now = 1000, y_now = 200)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            action [
        Hide('text_animation_up_screen'), 
        Function(set_mouse_to_default), 
        Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
        Function(change_location, location = 'leon_corridor')
        ]
        if time_now == 4 and dow not in ['SAT', 'SUN']:
            for i in ['audrey_leon_room_sa_4', 'samantha_leon_room_sa_4']:
                add 'locations_main/items/leon_room_sa/'+str(i)+'.1.png'

                imagebutton:
                    focus_mask True
                    if lightning:
                        idle im.MatrixColor('locations_main/items/leon_room_sa/'+str(i)+'.2.png', im.matrix.brightness(.2))

                    else:
                        idle 'locations_main/items/leon_room_sa/'+str(i)+'.2.png'
                    hover im.MatrixColor('locations_main/items/leon_room_sa/'+str(i)+'.2.png', im.matrix.brightness(.2))
                    if 'samantha' in i:
                        action Jump('samantha_events_4_label')
                    else:
                        action Jump('audrey_events_4_label')


    if location_now == 'cord_class_1':
        if time_now == 1 and dow not in ['SAT', 'SUN']:
            imagemap:
                if lightning:

                    ground 'locations_main/items/cord_class_1/cord_class_buttons_2.png'

                else:
                    ground 'locations_main/items/cord_class_1/cord_class_buttons_1.png'
                hover 'locations_main/items/cord_class_1/cord_class_buttons_2.png'
                for i in ['haley_cord_class_1_', 'lily_cord_class_1_', 'naomi_cord_class_1_', 'victoria_cord_class_1_']:
                    $ xtmp = i.split('_cord_class')[0]

                    if getattr(store, xtmp +'_events', None) is not None:

                        hotspot hotspots['cord_class_1'][i] clicked Jump(xtmp+'_events_label')
                hotspot hotspots['cord_class_1']['door']:
                    hovered Function(show_up_donw_text, text_now = 'Inner Garden', x_now = 1650, y_now = 250)
                    unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),

                    clicked Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_door1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'cord_garden_l')

        elif time_now == 2 and dow not in ['SAT', 'SUN']:
            imagemap:
                if lightning:
                    ground 'locations_main/items/cord_class_1/cord_class_buttons_2_2.png'

                else:
                    ground 'locations_main/items/cord_class_1/cord_class_buttons_1_2.png'

                hover 'locations_main/items/cord_class_1/cord_class_buttons_2_2.png'



                if getattr(store, 'victoria_events', None) is not None:

                    hotspot hotspots['cord_class_1']['victoria_cord_class_1_'] clicked Jump('victoria_events_label')

                hotspot hotspots['cord_class_1']['door']:
                    hovered Function(show_up_donw_text, text_now = 'Inner Garden', x_now = 1650, y_now = 250)
                    unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),

                    clicked Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_door1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'cord_garden_l')

        else:
            imagemap:
                if lightning:
                    ground 'locations_main/items/cord_class_1/cord_class_buttons_3_2.png'

                else:
                    ground 'locations_main/items/cord_class_1/cord_class_buttons_3.png'
                hover 'locations_main/items/cord_class_1/cord_class_buttons_3_2.png'





                hotspot hotspots['cord_class_1']['door']:
                    hovered Function(show_up_donw_text, text_now = 'Inner Garden', x_now = 1650, y_now = 250)
                    unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),

                    clicked Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_door1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'cord_garden_l')




    if location_now == 'cord_class_2':
        imagemap:





            hotspot hotspots['cord_class_2']['door']:
                hovered Function(show_up_donw_text, text_now = 'Inner Garden', x_now = 1200, y_now = 250)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),

                focus_mask None
                clicked Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_door1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'cord_garden_r')



            if dow not in ['SAT', 'SUN']:

                if time_now == 1:
                    ground 'locations_main/items/cord_class/cord_class_2_buttons_1.png'
                    hover 'locations_main/items/cord_class/cord_class_2_buttons_1_2.png'
                    hotspot hotspots['cord_class_2']['sabrina']:
                        focus_mask None

                        clicked Jump('sabrina_events_label')

                elif time_now == 2:
                    ground 'locations_main/items/cord_class/cord_class_2_buttons_2.png'
                    hover 'locations_main/items/cord_class/cord_class_2_buttons_2_2.png'
                    for i in ['haley', 'lily', 'naomi']:
                        hotspot hotspots['cord_class_2'][i]:

                            focus_mask None
                            clicked Jump(i+'_events_2_label')

                    hotspot hotspots['cord_class_2']['sabrina']:
                        focus_mask None

                        clicked Jump('sabrina_events_label')




                else:
                    if lightning:
                        ground 'locations_main/items/cord_class/cord_class_2_buttons_door_'+str(time_now)+'_2.png'

                    else:
                        ground 'locations_main/items/cord_class/cord_class_2_buttons_door_'+str(time_now)+'.png'
                    hover 'locations_main/items/cord_class/cord_class_2_buttons_door_'+str(time_now)+'_2.png'
            else:
                if lightning:
                    ground 'locations_main/items/cord_class/cord_class_2_buttons_door_'+str(time_now)+'_2.png'

                else:
                    ground 'locations_main/items/cord_class/cord_class_2_buttons_door_'+str(time_now)+'.png'

                hover 'locations_main/items/cord_class/cord_class_2_buttons_door_'+str(time_now)+'_2.png'




    if location_now in ['cord_caffe', 'cord_cafe']:
        if time_now == 4:
            imagebutton:
                if lightning:
                    idle im.MatrixColor('images/locations_main/items/caffe/cord_cafe_4.Door.png', im.matrix.brightness(.2))

                else:
                    idle 'images/locations_main/items/caffe/cord_cafe_4.Door.png'

                hover im.MatrixColor('images/locations_main/items/caffe/cord_cafe_4.Door.png', im.matrix.brightness(.2))

                focus_mask True

                hovered Function(show_up_donw_text, text_now = "Inner Garden", x_now = 1200, y_now = 350)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),

                action [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3'), 
            Function(change_location, location = 'cord_garden_r')
            ]
        else:
            imagebutton:
                if lightning:
                    idle im.MatrixColor('images/locations_main/items/caffe/cord_cafe_1.Door.png', im.matrix.brightness(.2))

                else:
                    idle 'images/locations_main/items/caffe/cord_cafe_1.Door.png'
                hover im.MatrixColor('images/locations_main/items/caffe/cord_cafe_1.Door.png', im.matrix.brightness(.2))

                focus_mask True

                hovered Function(show_up_donw_text, text_now = "Inner Garden", x_now = 1200, y_now = 350)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),

                action [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3'), 
            Function(change_location, location = 'cord_garden_r')
            ]

        if time_now not in [1, 4] and dow not in ['SAT', 'SUN']:


            add 'images/locations_main/items/caffe/cord_cafe_2.1.png'


            if time_now == 3:
                if getattr(store, 'elijah_view_3', None) is not None:
                    add 'images/locations_main/items/caffe/elijah_cord_cafe_3.1.png'
                    imagebutton:
                        if lightning:
                            idle im.MatrixColor('images/locations_main/items/caffe/elijah_cord_cafe_3.2.png', im.matrix.brightness(.2))

                        else:
                            idle 'images/locations_main/items/caffe/elijah_cord_cafe_3.2.png'
                        hover im.MatrixColor('images/locations_main/items/caffe/elijah_cord_cafe_3.2.png', im.matrix.brightness(.2))

                        focus_mask True
                        action Jump('elijah_events_caffe_label')

        if time_now in [2,3] and dow not in ['SAT', 'SUN']:

            add 'images/locations_main/items/caffe/'+'molly_cord_cafe_'+str(time_now)+'.1.png'


            imagebutton:
                focus_mask True
                if lightning:
                    idle im.MatrixColor('images/locations_main/items/caffe/'+'molly_cord_cafe_'+str(time_now)+'.2.png', im.matrix.brightness(.2))

                else:
                    idle 'images/locations_main/items/caffe/'+'molly_cord_cafe_'+str(time_now)+'.2.png'
                hover im.MatrixColor('images/locations_main/items/caffe/'+'molly_cord_cafe_'+str(time_now)+'.2.png', im.matrix.brightness(.2))
                action Jump('molly_events_label')

    if location_now == 'cord_garden_c':
        if not hide_interface:
            imagebutton:
                yalign .9
                xalign .5

                if lightning:
                    idle Transform(im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2)), rotate = -90)

                else:
                    idle Transform('images/main_interface/arrow_location.png', rotate = -90)
                hover Transform(im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2)), rotate = -90)
                action [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3'), 
            Function(change_location, location = 'cord_entrance')
            ]
            imagebutton:
                yalign .7
                xalign .05
                hovered Function(show_up_donw_text, text_now = "Left Wing", x_now = 50, y_now = 700)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                if lightning:
                    idle im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2))
                else:
                    idle 'images/main_interface/arrow_location.png'

                hover im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2))
                action [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3'), 
            Function(change_location, location = 'cord_garden_l')
            ]

            imagebutton:
                yalign .7
                xalign .95
                hovered Function(show_up_donw_text, text_now = "Right Wing", x_now = 1670, y_now = 700)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),


                if lightning:
                    idle Transform(im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2)), xzoom = -1)

                else:
                    idle Transform('images/main_interface/arrow_location.png', xzoom = -1)

                hover Transform(im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2)), xzoom = -1)





                action [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3'), 
            Function(change_location, location = 'cord_garden_r')
            ]

        if time_now == 3 and dow not in ['SAT', 'SUN']:


            for i in ['naomi', 'lily']:
                if getattr(store, i +'_view', None) is not None:
                    imagebutton:
                        focus_mask True
                        if lightning:
                            idle im.MatrixColor('locations_main/items/cord/'+i+'_cord_garden_c_3_1.3.png', im.matrix.brightness(.2))

                        else:
                            idle 'locations_main/items/cord/'+i+'_cord_garden_c_3_1.3.png'

                        if getattr(store, i +'_events', None) is not None:
                            hover im.MatrixColor('locations_main/items/cord/'+i+'_cord_garden_c_3_1.3.png', im.matrix.brightness(.2))
                            action Jump(i+'_events_3_label')

                        else:
                            hover 'locations_main/items/cord/'+i+'_cord_garden_c_3_1.3.png'

                            action NullAction()



        imagebutton:
            if lightning:
                idle im.MatrixColor('locations_main/items/cord/cord_garden_c_'+str(time_now)+'.Door.png', im.matrix.brightness(.2))
            else:
                idle 'locations_main/items/cord/cord_garden_c_'+str(time_now)+'.Door.png'
            hover im.MatrixColor('locations_main/items/cord/cord_garden_c_'+str(time_now)+'.Door.png', im.matrix.brightness(.2))

            hovered Function(show_up_donw_text, text_now = "Main Hall", x_now = 1670, y_now = 400)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),

            focus_mask True

            action [
        Hide('text_animation_up_screen'), 
        Function(set_mouse_to_default), 
        Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_door1.mp3'), 
        Function(change_location, location = 'cord_mainhall')
        ]





    for cord in ['cord_garden_l', 'cord_garden_r']:
        if location_now == cord:
            for i in [1, 2]:
                imagebutton:
                    if lightning:
                        idle im.MatrixColor('locations_main/items/'+cord[:5]+cord[12:]+'/'+cord+'_'+str(time_now)+'.Door'+str(i)+'.png', im.matrix.brightness(.2))

                    else:
                        idle 'locations_main/items/'+cord[:5]+cord[12:]+'/'+cord+'_'+str(time_now)+'.Door'+str(i)+'.png'

                    hover im.MatrixColor('locations_main/items/'+cord[:5]+cord[12:]+'/'+cord+'_'+str(time_now)+'.Door'+str(i)+'.png', im.matrix.brightness(.2))

                    if cord == 'cord_garden_l':
                        if i == 1:
                            hovered Function(show_up_donw_text, text_now = "Library", x_now = 200+(i-1)*1060, y_now = 400)

                        else:
                            hovered Function(show_up_donw_text, text_now = "Classroom 1", x_now = 200+(i-1)*1060, y_now = 400)

                    else:
                        if i == 1:
                            hovered Function(show_up_donw_text, text_now = "Cafe", x_now = 1500-(i-1)*1050, y_now = 400)

                        else:
                            hovered Function(show_up_donw_text, text_now = "Classroom 2", x_now = 1500-(i-1)*1050, y_now = 400)


                    unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),

                    focus_mask True
                    if cord == 'cord_garden_l':
                        if i == 1:


                            action [
                            Hide('text_animation_up_screen'), 
                            Function(set_mouse_to_default), 
                            Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_door1.mp3'), 
                            Function(change_location, location = 'cord_library')
                            ]
                        else:
                            action [
                            Hide('text_animation_up_screen'), 
                            Function(set_mouse_to_default), 
                            Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_door1.mp3'), 
                            Function(change_location, location = 'cord_class_1')
                            ]

                    else:
                        if i == 1:

                            if time_now != 1:
                                action [
                            Hide('text_animation_up_screen'), 
                            Function(set_mouse_to_default), 
                            
                            Function(change_location, location = 'cord_caffe')
                            ]
                            else:
                                action [
                            Hide('text_animation_up_screen'), 
                            Function(set_mouse_to_default), 
                            
                            Function(change_location, location = 'cord_caffe_door')
                            ]
                        else:
                            action [
                            Hide('text_animation_up_screen'), 
                            Function(set_mouse_to_default), 
                            Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_door1.mp3'), 
                            Function(change_location, location = 'cord_class_2')
                            ]













    if location_now == 'leon_living':


        imagemap:
            if lightning:
                ground 'locations_main/items/living_room/leon_living_1_buttons_doors_stairs_'+str(time_now)+'_2.png'

            else:
                ground '#0000'
            hover 'locations_main/items/living_room/leon_living_1_buttons_doors_stairs_'+str(time_now)+'_2.png'
            hotspot hotspots['leon_living']['door_1']:
                focus_mask None

                hovered Function(show_up_donw_text, text_now = "Bathroom", x_now = 1100, y_now = 400)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                clicked [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
            Function(change_location, location = 'leon_bathroom')
            ]

            hotspot hotspots['leon_living']['door_2']:
                focus_mask None

                hovered Function(show_up_donw_text, text_now = "Elijah's Room", x_now = 1000, y_now = 400)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                action [
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'),
            Jump('close_room_label')
            ]

            hotspot hotspots['leon_living']['door_3']:

                focus_mask None

                hovered Function(show_up_donw_text, text_now = "Outside", x_now = 50, y_now = 400)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                clicked [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'),
            Show('map_screen', transition = Dissolve(.5))
            ]

            hotspot hotspots['leon_living']['stairs']:
                focus_mask None

                hovered Function(show_up_donw_text, text_now = "Upstairs", x_now = 700, y_now = 200)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                clicked [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3'), 
            Function(change_location, location = 'leon_corridor')
            ]




        if time_now   == 1 and dow not in ['SAT', 'SUN']:
            imagemap:
                if lightning:
                    ground 'locations_main/items/living_room/leon_living_morning_1_2.png'

                else:
                    ground 'locations_main/items/living_room/leon_living_morning_1.png'
                hover 'locations_main/items/living_room/leon_living_morning_1_2.png'

                for i in ['samantha', 'elijah', 'audrey']:
                    hotspot hotspots['leon_living'][i+'_1']:
                        focus_mask None
                        clicked Jump(i+'_events_label')
        if time_now   == 3 and dow not in ['SAT', 'SUN']:
            imagemap:
                if lightning:
                    ground 'locations_main/items/living_room/leon_living_1_buttons_doors_stairs_1_3_girls_2.png'

                else:
                    ground 'locations_main/items/living_room/leon_living_1_buttons_doors_stairs_1_3_girls.png'
                hover 'locations_main/items/living_room/leon_living_1_buttons_doors_stairs_1_3_girls_2.png'

                for i in ['audrey', 'samantha']:
                    hotspot hotspots['leon_living'][i+'_3']:
                        focus_mask None
                        clicked Jump(i+'_events_3_label')



    elif location_now == 'cord_mainhall':
        if not hide_interface:
            imagebutton:
                yalign .9
                xalign .5

                if lightning:
                    idle Transform(im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2)), rotate = -90)

                else:
                    idle Transform('images/main_interface/arrow_location.png', rotate = -90)
                hover Transform(im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2)), rotate = -90)
                action [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3'), 
            Function(change_location, location = 'cord_garden_c')
            ]

    elif location_now == 'cord_library':
        if time_now in [1, 2] and dow not in ['SAT', 'SUN']:
            add 'locations_main/items/library/amelie_cord_library_'+str(time_now)+'.1.png'
            if getattr(store, 'amelie_view', None) is not None:
                imagebutton:
                    if lightning:
                        idle im.MatrixColor('locations_main/items/library/amelie_cord_library_'+str(time_now)+'.2.png', im.matrix.brightness(.2))

                    else:
                        idle 'locations_main/items/library/amelie_cord_library_'+str(time_now)+'.2.png'

                    if getattr(store, 'amelie_events', None) is not None:
                        hover im.MatrixColor('locations_main/items/library/amelie_cord_library_'+str(time_now)+'.2.png', im.matrix.brightness(.2))
                        focus_mask True
                        action Jump('amelie_events_label')

                    else:
                        hover 'locations_main/items/library/amelie_cord_library_'+str(time_now)+'.2.png'
                        focus_mask True
                        action NullAction()

        imagebutton:


            if lightning:

                idle im.MatrixColor('locations_main/items/library/cord_library_'+str(time_now)+'.Door.png', im.matrix.brightness(.2))

            else:
                idle 'locations_main/items/library/cord_library_'+str(time_now)+'.Door.png'

            hover im.MatrixColor('locations_main/items/library/cord_library_'+str(time_now)+'.Door.png', im.matrix.brightness(.2))

            hovered Function(show_up_donw_text, text_now = "Inner Garden", x_now = 1250, y_now = 400)
            focus_mask True
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            action [
        Hide('text_animation_up_screen'), 
        Function(set_mouse_to_default), 
        Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_door1.mp3'), 
        Function(change_location, location = 'cord_garden_l')
        ]


    elif location_now == 'cord_entrance':
        for i in (1, 2):

            imagebutton:
                if lightning:
                    idle im.MatrixColor('locations_main/items/entrance/cord_entrance_'+str(time_now)+'.Door'+str(i)+'.png', im.matrix.brightness(.2))

                else:
                    idle 'locations_main/items/entrance/cord_entrance_'+str(time_now)+'.Door'+str(i)+'.png'
                hover im.MatrixColor('locations_main/items/entrance/cord_entrance_'+str(time_now)+'.Door'+str(i)+'.png', im.matrix.brightness(.2))

                hovered Function(show_up_donw_text, text_now = "Inner Garden", x_now = 410+(i-1)*880, y_now = 600)
                focus_mask True
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                action [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_door1.mp3'), 
            Function(change_location, location = 'cord_garden_c')
            ]
        if time_now == 3 and dow not in ['SAT', 'SUN']:
            add 'locations_main/items/entrance/jacob_cord_entrance_3.1.png'
            if getattr(store, 'jacob_events', None) is not None:

                imagebutton:
                    if lightning:
                        idle im.MatrixColor('locations_main/items/entrance/jacob_cord_entrance_3.2.png', im.matrix.brightness(.2))

                    else:
                        idle 'locations_main/items/entrance/jacob_cord_entrance_3.2.png'

                    hover im.MatrixColor('locations_main/items/entrance/jacob_cord_entrance_3.2.png', im.matrix.brightness(.2))
                    focus_mask True
                    action Jump('jacob_events_label')
    elif location_now == 'corridor':
        imagebutton:
            if lightning:
                idle 'images/main_interface/locations/corridor_ashlie_door.png'
            else:
                idle Transform('images/main_interface/locations/corridor_ashlie_door.png', alpha = .1)
            hover 'images/main_interface/locations/corridor_ashlie_door.png'
            hovered Function(show_up_donw_text, text_now = "Ashley's Bedroom", x_now = 1220, y_now = 200)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            focus_mask True

            action Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'ashlie_room')
        imagebutton:
            if lightning:
                idle 'images/main_interface/locations/corridor_bath_door.png'
            else:
                idle Transform('images/main_interface/locations/corridor_bath_door.png', alpha = .1)
            hover 'images/main_interface/locations/corridor_bath_door.png'
            hovered Function(show_up_donw_text, text_now = "Bathroom", x_now = 850, y_now = 200)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            focus_mask True

            action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'bath')

        imagebutton:
            if lightning:
                idle 'images/main_interface/locations/corridor_samanta_door.png'
            else:
                idle Transform('images/main_interface/locations/corridor_samanta_door.png', alpha = .1)
            hover 'images/main_interface/locations/corridor_samanta_door.png'
            hovered Function(show_up_donw_text, text_now = "Samantha's Bedroom", x_now = 1000, y_now = 200)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            focus_mask True

            action Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'samanta_room')

        imagebutton:
            if lightning:
                idle 'images/main_interface/locations/corridor_restroom_door.png'
            else:
                idle Transform('images/main_interface/locations/corridor_restroom_door.png', alpha = .1)
            hover 'images/main_interface/locations/corridor_restroom_door.png'
            focus_mask True

            hovered Function(show_up_donw_text, text_now = "Downstairs", x_now = 600, y_now = 800)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),

            action Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'restroom')

        imagebutton:
            if lightning:
                idle 'images/main_interface/locations/corridor_gg_room.png'
            else:
                idle Transform('images/main_interface/locations/corridor_gg_room.png', alpha = .1)
            hover 'images/main_interface/locations/corridor_gg_room.png'
            focus_mask True
            hovered Function(show_up_donw_text, text_now = "My Bedroom", x_now = 1600, y_now = 400)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'gg_room')


        imagebutton:
            if lightning:
                idle 'images/main_interface/locations/corridor_parents_room.png'
            else:
                idle Transform('images/main_interface/locations/corridor_parents_room.png', alpha = .1)
            hover 'images/main_interface/locations/corridor_parents_room.png'
            focus_mask True

            hovered Function(show_up_donw_text, text_now = "Olivia's Bedroom", x_now = 600, y_now = 200)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),

            action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'parents_room')


    elif location_now == 'parents_room':
        imagebutton:
            idle Transform('images/main_interface/locations/parents_room_cupboard_1.png', alpha = .1)
            hover 'images/main_interface/locations/parents_room_cupboard_1.png'
            hovered Function(show_up_donw_text, text_now = "Cupboard", x_now = 120, y_now = 600)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            focus_mask True

            action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Wood_open_chest.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Jump('parents_room_cupboard_1_label')


        imagebutton:
            idle Transform('images/main_interface/locations/parents_room_cupboard_2.png', alpha = .1)
            hover 'images/main_interface/locations/parents_room_cupboard_2.png'
            focus_mask True

            hovered Function(show_up_donw_text, text_now = "Olivia???s Purse", x_now = 1250, y_now = 600)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),

            action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/woman_bag.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Jump('parents_room_cupboard_2_label')

        if not hasattr(store, 'parents_room_photo'):
            imagebutton:
                idle Transform('images/main_interface/locations/IMG_3142.png', alpha = .1)
                hover 'images/main_interface/locations/IMG_3142.png'
                focus_mask True

                hovered Function(show_up_donw_text, text_now = "Photo", x_now = 110, y_now = 400)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),

                action Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Jump('parents_room_photo_label')

        if not hasattr(store, 'parents_room_painting'):
            imagebutton:
                idle Transform('images/main_interface/locations/IMG_3156.png', alpha = .1)
                hover 'images/main_interface/locations/IMG_3156.png'


                hovered Function(show_up_donw_text, text_now = "Painting", x_now = 400, y_now = 200)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),


                focus_mask True

                action Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Jump('parents_room_painting_label')



        imagebutton:
            idle Transform('images/main_interface/locations/parents_room_corridor_door.png', alpha = .1)
            hover 'images/main_interface/locations/parents_room_corridor_door.png'
            focus_mask True

            hovered Function(show_up_donw_text, text_now = "Corridor", x_now = 1170, y_now = 200)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),

            action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'corridor')

    elif location_now == 'bath':
        imagebutton:
            idle 'images/main_interface/locations/bath_room_door_corridor.png'
            hover im.MatrixColor('images/main_interface/locations/bath_room_door_corridor.png', im.matrix.brightness(.3))
            hovered Function(show_up_donw_text, text_now = "Corridor", x_now = 0, y_now = 600)
            unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            focus_mask True

            action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(change_location, location = 'corridor')
        if not hasattr(store, 'bath_duck'):
            imagebutton:
                idle 'images/main_interface/locations/IMG_3114.png'
                hover im.MatrixColor('images/main_interface/locations/IMG_3114.png', im.matrix.brightness(.3))
                hovered Function(show_up_donw_text, text_now = "Bath Ducks", x_now = 1680, y_now = 300)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                focus_mask True

                action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Duck_click.mp3'), Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Jump('bath_duck_label')
        else:
            imagebutton:
                idle 'images/main_interface/locations/IMG_3114.png'
                hover im.MatrixColor('images/main_interface/locations/IMG_3114.png', im.matrix.brightness(.3))
                hovered Function(show_up_donw_text, text_now = "Bath Ducks", x_now = 1680, y_now = 300)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                focus_mask True

                action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Duck_click.mp3')

        if not hasattr(store, 'bath_breth'):
            imagebutton:
                idle 'images/main_interface/locations/IMG_3113.png'
                hover im.MatrixColor('images/main_interface/locations/IMG_3113.png', im.matrix.brightness(.3))
                hovered Function(show_up_donw_text, text_now = "Toothbrush", x_now = 420, y_now = 570)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                focus_mask True

                action Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Jump('bath_breth_label')

    imagebutton:
        ymaximum 120
        xmaximum 900
        idle '#0000'
        hover '#0000'
        action NullAction()
        yalign 1.0
    add 'hide_button' yalign .5


    #if show_hide_locations_pos:
        
    # timer .1 action [
    #     Hide('show_hide_locations'), 
    #     Show('show_hide_locations_2'),
    #     Hide('text_animation_up_screen_3')
    #     ]
    #else:
    # if show_hide_locations_pos:
    #     timer .1 action [
    #    Hide('show_hide_locations_2'), 
    #    Hide('text_animation_up_screen_3'), 
    #    Show('show_hide_locations')
    #    ]  
    # else:
    #     timer .1 action [
    #     Hide('show_hide_locations'), 
    #     Show('show_hide_locations_2'),
    #     Hide('text_animation_up_screen_3')
    #     ]
    for i in books_now:
        if location_now == i:
            imagebutton:

                if lightning:
                    idle im.MatrixColor('images/locations_main/items/' + location_now + '/books/' + str(books_now[i])+ '.png', im.matrix.brightness(.2))
                else:
                    idle 'images/locations_main/items/' + location_now + '/books/' + str(books_now[i])+ '.png'

                hover im.MatrixColor('images/locations_main/items/' + location_now + '/books/' + str(books_now[i])+ '.png', im.matrix.brightness(.2))
                hovered Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_highlighting_menu.mp3')
                focus_mask True

                action Function(ShowMessage, ['images/main_interface/books_mini.png', 'You found the book']), Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_game_click.mp3'), SetVariable('books_gg', books_gg+1), Function(books_pop, i)
    for i in books_now_debug:
        if location_now == i[0]:
            imagebutton:
                idle 'images/locations_main/items/' + location_now + '/books/' + str(i[1])+ '.png'
                hover im.MatrixColor('images/locations_main/items/' + location_now + '/books/' + str(i[1])+ '.png', im.matrix.brightness(.2))
                focus_mask True
                action SetVariable('books_gg', books_gg+1)


    if location_now == 'cord_garden_l':
        if not hide_interface:
            imagebutton:
                yalign .7
                xalign .95
                hovered Function(show_up_donw_text, text_now = "Inner Garden", x_now = 1670, y_now = 700)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                if lightning:
                    idle Transform(im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2)), xzoom = -1)

                else:
                    idle Transform('images/main_interface/arrow_location.png', xzoom = -1)
                hover Transform(im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2)), xzoom = -1)
                action [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3'), 
            Function(change_location, location = 'cord_garden_c')
            ]
    elif location_now == 'cord_garden_r':
        if not hide_interface:
            imagebutton:
                yalign .7
                xalign .05
                hovered Function(show_up_donw_text, text_now = "Inner Garden", x_now = 50, y_now = 700)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                if lightning:
                    idle im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2))

                else:
                    idle 'images/main_interface/arrow_location.png'
                hover im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2))
                action [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3'), 
            Function(change_location, location = 'cord_garden_c')
            ]


    hbox:
        xalign .5

        spacing 15


    default text_dow = {
'MON' : 'Monday', 
'TUE' : 'Tuesday',
'WED' : 'Wednesday',
'THUR': 'Thursday',
'FRI' : 'Friday',
'SAT' : 'Saturday', 
'SUN' : 'Sunday',
    }

    default color_dow = {
1 : '#C5FFDF', 
2 : '#DCFFC0',
3 : '#FFD8B4',
4 : '#BFD9FF',
    }

    if hasattr(store, 'ep2start') and not persistent.from_gallery and not hide_interface:
        add 'main_interface/time_panel_'+str(time_now)+'.png' xpos -34 ypos -30



        viewport xpos 90:
            add '#fff0'
            ypos -7
            xmaximum 160
            ymaximum 90
            text str(text_dow[dow]) size 21 color color_dow[time_now] font 'fonts/h_font.ttf' xalign .5 ypos 10

            #text time_now_texts[time_now].title() xpos 25 size 18 font 'fonts/h_font.ttf'
            #text _(str(dow).title()) color '#FFFb' xpos 25 ypos 20 size 18 font 'fonts/h_font.ttf'
            if hasattr(store, 'ep2start') and not persistent.from_gallery:

                if 'dale' in location_now and time_now == 4:
                    button:
                        xpos 15
                        ypos 40
                        add 'skip_button'
                        action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_time_skip.mp3'), Function(change_location_2, 'dale_hotel', time_now+1, sleep = True)
                
                elif location_now == 'dale_spa' and time_now == 3:
                    button:
                        xpos 15
                        ypos 40
                        add 'skip_button'
                        action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_time_skip.mp3'),Function(change_location_2, 'dale_mainstreet', time_now+1)
                
                elif location_now == 'dale_shop' and time_now == 3:
                    button:
                        xpos 15
                        ypos 40
                        add 'skip_button'
                        action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_time_skip.mp3'),Function(change_location_2, 'dale_mainstreet', time_now+1)
                
                elif location_now == 'club' and time_now == 4:
                    button:
                        xpos 15
                        ypos 40
                        add 'skip_button'
                        action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_time_skip.mp3'),Function(change_location_2, 'dale_clubenter', time_now+1)
                
                elif time_now != 4:
                    button:
                        xpos 15
                        ypos 40
                        add 'skip_button'
                        action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_time_skip.mp3'),Function(change_location_2, location_now, time_now+1)
                
                else:
                    button:
                        xpos 15
                        ypos 40
                        add 'skip_button'
                        action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_time_skip.mp3'), Function(change_location_2, 'leon_room_mc', time_now+1, sleep = True)
                
                #text 'Skip time' xpos 35 ypos 52 size 12 font 'fonts/h_font.ttf'






















    #text str(show_hide_locations_pos) xalign .5 size 40
    # if hasattr(store, 'ep2start') and not hide_interface:
    #     if not renpy.get_screen('show_hide_locations_2') and not renpy.get_screen('show_hide_locations'): 
    #         # if show_hide_locations_pos:
    #         #     timer .1 action [
    #         #    Hide('show_hide_locations_2'), 
    #         #    Hide('text_animation_up_screen_3'), 
    #         #    Show('show_hide_locations')
    #         #    ]  
    #         # else:
            
    #         timer .1 action [
    #        Hide('show_hide_locations'), 
    #        Hide('text_animation_up_screen_3'), 
    #        Show('show_hide_locations_2')
    #        ]  






    if location_now == 'dale_mainstreet':
        if not hide_interface:
            imagebutton:
                yalign .35
                xalign .35
                hovered Function(show_up_donw_text, text_now = "Alley", x_now = 600, y_now = 270)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                if lightning:
                    idle Transform(im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2)))

                else:
                    idle Transform('images/main_interface/arrow_location.png')
                hover Transform(im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2)))
                action [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3'), 
            Function(change_location, location = 'dale_clubenter')
            ]
        if time_now == 4:
            if (not hasattr(store, 'Q_Giant')) or (hasattr(store, 'Q_Giant') and not Q_Giant):
                image 'locations_main/items/dale_mainstreet/giant2_dale_mainstreet_4.png'
            
                imagebutton:
                    if lightning:
                        idle  'locations_main/items/dale_mainstreet/giant_dale_mainstreet_4_2.png'
                    
                    else:
                        idle  'locations_main/items/dale_mainstreet/giant_dale_mainstreet_4.png'
                    hover 'locations_main/items/dale_mainstreet/giant_dale_mainstreet_4_2.png'
                    focus_mask True

                    action Jump('giant_dale_mainstreet_label')


        imagemap:
            if lightning:
                ground 'locations_main/items/dale_mainstreet/dale_mainstreet_'+str(time_now)+'_2.png'

            else:
                ground '#0000'
            hover 'locations_main/items/dale_mainstreet/dale_mainstreet_'+str(time_now)+'_2.png'
            hotspot hotspots['dale_mainstreet']['door_hotel']:
                focus_mask None

                hovered Function(show_up_donw_text, text_now = "Hotel", x_now = 140, y_now = 350)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                clicked [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
            Function(change_location, location = 'dale_hotel')
            
            ]


       




            hotspot hotspots['dale_mainstreet']['door_shop']:
                focus_mask None

                hovered Function(show_up_donw_text, text_now = "Shop", x_now = 950, y_now = 350)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                if time_now == 4:
                    clicked [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
            Jump('close_room_label')
            ]
                else:
                    clicked [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
            Function(change_location, location = 'dale_shop')
            
            ]


            hotspot hotspots['dale_mainstreet']['door_spa']:
                focus_mask None

                hovered Function(show_up_donw_text, text_now = "Spa", x_now = 1560, y_now = 462)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                if time_now in (1, 4) or dow == 'SUN':
                    clicked [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
            Jump('close_room_label')
            ]
                else:
                    clicked [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
            Function(change_location, location = 'dale_spa')
            
            ]
    if location_now == 'dale_clubenter':
        if time_now in (1, 2):
            imagebutton:
                idle  'images/locations_main/items/clubenter/door_dale_clubenter_'+str(time_now)+'.png'
                hover Transform(im.MatrixColor('images/locations_main/items/clubenter/door_dale_clubenter_'+str(time_now)+'.png', im.matrix.brightness(.2)))
                
                focus_mask True
                action [
                Hide('text_animation_up_screen'), 
                Function(set_mouse_to_default), 
                Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
                Jump('close_room_label')
                ]
        else:
            imagebutton:
                idle  'images/locations_main/items/clubenter/romul_dale_clubenter_'+str(time_now)+'.png'
                hover Transform(im.MatrixColor('images/locations_main/items/clubenter/romul_dale_clubenter_'+str(time_now)+'.png', im.matrix.brightness(.2)))
                
                focus_mask True
                action [
                Hide('text_animation_up_screen'), 
                Function(set_mouse_to_default), 
                Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
                Jump('romul_dale_clubenter_label')
                ]
        if not hide_interface:
            imagebutton:
                yalign .9
                xalign .5

                if lightning:
                    idle Transform(im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2)), rotate = -90)

                else:
                    idle Transform('images/main_interface/arrow_location.png', rotate = -90)
                hover Transform(im.MatrixColor('images/main_interface/arrow_location.png', im.matrix.brightness(.2)), rotate = -90)
                action [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3'), 
            Function(change_location, location = 'dale_mainstreet')
            ]
        
    if location_now == 'dale_spa':

        imagemap:
            if lightning:
                ground 'locations_main/items/dale_spa/dale_spa_1_2.png'

            else:
                ground '#0000'
            hover 'locations_main/items/dale_spa/dale_spa_1_2.png'
            hotspot hotspots['dale_spa']['door']:
                focus_mask None

                hovered Function(show_up_donw_text, text_now = "Exit", x_now = 1680, y_now = 200)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                clicked [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
            Function(change_location, location = 'dale_mainstreet')
            
            ]


            hotspot hotspots['dale_spa']['faith']:
                focus_mask None

                hovered Function(show_up_donw_text, text_now = "Faith", x_now = 650, y_now = 170)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                clicked [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
            Jump('faith_dale_spa_1_label')
            ]

    if location_now == 'dale_hotel':

        imagemap:
            if lightning:
                ground 'locations_main/items/dale_hotel/dale_hotel_1_2.png'

            else:
                ground '#0000'
            hover 'locations_main/items/dale_hotel/dale_hotel_1_2.png'
            hotspot hotspots['dale_hotel']['door']:
                focus_mask None

                hovered Function(show_up_donw_text, text_now = "Exit", x_now = 1700, y_now = 200)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                clicked [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
            Function(change_location, location = 'dale_mainstreet')
            
            ]


            # hotspot hotspots['dale_hotel']['mina']:
            #     focus_mask None

            #     hovered Function(show_up_donw_text, text_now = "Mina", x_now = 370, y_now = 310)
            #     unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
            #     clicked [
            # Hide('text_animation_up_screen'), 
            # Function(set_mouse_to_default), 
            # Function(renpy.play, channel = 'sound', fileslename = 'audio/new/gameplay/Door_open1.mp3'), 
            # Jump('mina_dale_hotel_1_label')
            # ]
    

    if location_now == 'dale_shop':

        imagemap:
            if lightning:
                ground 'locations_main/items/dale_shop/dale_shop_1_2.png'

            else:
                ground '#0000'
            hover 'locations_main/items/dale_shop/dale_shop_1_2.png'
            hotspot hotspots['dale_shop']['door']:
                focus_mask None

                hovered Function(show_up_donw_text, text_now = "Exit", x_now = 20, y_now = 200)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                clicked [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
            Function(change_location, location = 'dale_mainstreet')
            
            ]


            hotspot hotspots['dale_shop']['gordon']:
                focus_mask None

                hovered Function(show_up_donw_text, text_now = "Gordon", x_now = 750, y_now = 470)
                unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
                clicked [
            Hide('text_animation_up_screen'), 
            Function(set_mouse_to_default), 
            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Door_open1.mp3'), 
            Jump('gordon_dale_shop_1_label')
            ]
    if location_now == 'dale_club':
        imagebutton:
            focus_mask True
            if lightning:
                idle im.MatrixColor('locations_main/items/dale_mainstreet/door_dale_club_1.png', im.matrix.brightness(.3)) 
            
            else:
                idle 'locations_main/items/dale_mainstreet/door_dale_club_1.png'
            hover im.MatrixColor('locations_main/items/dale_mainstreet/door_dale_club_1.png', im.matrix.brightness(.3)) 
            action Function(change_location_2, 'dale_clubenter', time_now)

        imagebutton:
            focus_mask True
            if lightning:
                idle im.MatrixColor('locations_main/items/dale_mainstreet/adele_dale_club_1.png', im.matrix.brightness(.3)) 
            
            else:
                idle 'locations_main/items/dale_mainstreet/adele_dale_club_1.png'
            hover im.MatrixColor('locations_main/items/dale_mainstreet/adele_dale_club_1.png', im.matrix.brightness(.3)) 
            action Jump('talk_to_adele')
        
        imagebutton:
            focus_mask True
            if lightning:
                idle im.MatrixColor('locations_main/dale_club_sprite1.png', im.matrix.brightness(.3)) 
            
            else:
                idle 'locations_main/dale_club_sprite1.png'
            hover im.MatrixColor('locations_main/dale_club_sprite1.png', im.matrix.brightness(.3)) 
            action Jump('Lucy_2_label')
        imagebutton:
            focus_mask True
            if lightning:
                idle im.MatrixColor('locations_main/dale_club_sprite2.png', im.matrix.brightness(.3)) 
            
            else:
                idle 'locations_main/dale_club_sprite2.png'
            hover im.MatrixColor('locations_main/dale_club_sprite2.png', im.matrix.brightness(.3)) 
            action Jump('Sadira_2_label')
    

        



    

    key "hide_windows" action SetVariable('hide_interface', not hide_interface)
    viewport:
        xmaximum 300
        ymaximum 50
        image '#000'
        hbox:
            textbutton 'Dale'     action Jump('set_auto_events_dale') #Function(change_location, location = 'dale_mainstreet') 
            xalign .5 yalign .5
        xalign .5
   # ????????    


    if hasattr(store, 'ep2start') and not persistent.from_gallery and not hide_interface:
        
        add 'bg_for_buttons' xalign 1.0 ypos -5
        viewport ypos -5:
            xmaximum 403
            ymaximum 86
            image '#0000'
            xalign  1.0
            hbox:
                spacing 22
                yalign .5
                viewport:
                    xmaximum 60
                    ymaximum 55
                    image '#fff0'
                    button yalign .5 xalign .5:
                       add 'notebook_button'
                       focus_mask None
                       action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_open.mp3'), Show('quest_log_screen', transition = Dissolve(.5))
                    

                viewport:
                    xmaximum 60
                    ymaximum 55
                    image '#fff0'
                    button yalign .5 xalign .5:
                       add 'head_button'
                       focus_mask None
                       action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_open.mp3'), Show('quest_log_screen', open_menu = 'CHARACTER INFO',  transition = Dissolve(.5))
                    
                viewport:
                    xmaximum 60
                    ymaximum 55
                    image '#fff0'
                    button yalign .5 xalign .5:
                       add 'inventory_button'
                       focus_mask None
                       action Show('inventory_interface_screen', transition = Dissolve(.3)), Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_open.mp3')

                viewport:
                    xmaximum 55
                    ymaximum 55
                    image '#fff0'
                    button yalign .5 xalign .5:
                        add 'phone_button'
                        focus_mask None
                        if hasattr(store, 'new_cnq') and new_cnq:
                            action [
                
                                Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Phone_take.mp3'), 
                                Show('lustagram_screen', transition = Dissolve(.3)), 
                                Function(renpy.play, channel = 'sound', filename = 'audio/Iphone.mp3'),
                                SetVariable('new_cnq', False)
                                
                                ]

                        else:
                            action [
                            Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Phone_take.mp3'), 
                            Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3'), 
                            Show('lustagram_screen', transition = Dissolve(.3))
                            ]

                viewport:
                    xmaximum 60
                    ymaximum 55
                
                    image '#fff0'
                    if 'dale' not in location_now:
                        button yalign .5 xalign .5:
                            add 'map_button'
                            focus_mask True
                            action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Open_latter.mp3'), Show('map_screen', transition = Dissolve(.5))
                
                    else:
                        button yalign .5 xalign .5:
                            add im.Grayscale("images/main_interface/map_button_circle.png")
                            focus_mask True
                            action NullAction()



        # button xalign .85:

        #     add 'phone_button'
        #     focus_mask None
        #     if hasattr(store, 'new_cnq') and new_cnq:
        #         action [
            
        #     Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Phone_take.mp3'), 
        #     Show('lustagram_screen', transition = Dissolve(.3)), 
        #     Function(renpy.play, channel = 'sound', filename = 'audio/Iphone.mp3'),
        #     SetVariable('new_cnq', False)
            
        #     ]

        #     else:
        #         action [
        #     Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Phone_take.mp3'), 
        #     Function(renpy.play,channel = 'sound', filename = 'audio/new/gameplay/smartphone_button.mp3'), 
        #     Show('lustagram_screen', transition = Dissolve(.3))
        #     ]

            
        # button xalign .9:
        #     add 'inventory_button'
        #     focus_mask None
        #     action Show('inventory_interface_screen', transition = Dissolve(.3)), Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_open.mp3')


        # if hasattr(store, 'new_cnq') and new_cnq:
        #     add 'new_quest_icon' xalign .853 ypos 10


        # if 'dale' not in location_now:
        #     button xalign .99 ypos 3:
        #         add 'map_button'
        #         focus_mask True
        #         action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/Open_latter.mp3'), Show('map_screen', transition = Dissolve(.5))
        
        # else:
        #     button xalign .99 ypos 3:
        #         add im.Grayscale("images/main_interface/map_button_circle.png")
        #         focus_mask True
        #         action NullAction()



init python:
    hide_interface = False


screen variables_screen:
    imagebutton:
        idle '#000'
        hover '#000'
        action Hide('variables_screen', transition = Dissolve(.5))
    vbox:
        xalign .5 yalign .5
        hbox:
            text 'Q_Victoria: ' + str(Q_Victoria) size 20 color "#FFF"
            textbutton '-' action SetVariable('Q_Victoria', Q_Victoria-1)

            textbutton '+' action SetVariable('Q_Victoria', Q_Victoria+1)

        hbox:

            text 'Q_Elijah: ' + str(Q_Elijah) size 20 color "#FFF"
            textbutton '-' action SetVariable('Q_Elijah', Q_Elijah-1)

            textbutton '+' action SetVariable('Q_Elijah', Q_Elijah+1)

        hbox:
            text 'Q_Leona: ' + str(Q_Leona) size 20 color "#FFF"
            textbutton '-' action SetVariable('Q_Leona', Q_Leona-1)

            textbutton '+' action SetVariable('Q_Leona', Q_Leona+1)

        hbox:
            text 'Q_Lily: ' + str(Q_Lily) size 20 color "#FFF"
            textbutton '-' action SetVariable('Q_Lily', Q_Lily-1)

            textbutton '+' action SetVariable('Q_Lily', Q_Lily+1)

        hbox:
            text 'Q_Haley: ' + str(Q_Haley) size 20 color "#FFF"
            textbutton '-' action SetVariable('Q_Haley', Q_Haley-1)

            textbutton '+' action SetVariable('Q_Haley', Q_Haley+1)


        hbox:
            text 'Q_Amelie: ' + str(Q_Amelie) size 20 color "#FFF"
            textbutton '-' action SetVariable('Q_Amelie', Q_Amelie-1)

            textbutton '+' action SetVariable('Q_Amelie', Q_Amelie+1)

        hbox:
            text 'Q_Samantha: ' + str(Q_Samantha) size 20 color "#FFF"
            textbutton '-' action SetVariable('Q_Samantha', Q_Samantha-1)

            textbutton '+' action SetVariable('Q_Samantha', Q_Samantha+1)


        hbox:
            text 'Q_Jacob: ' + str(Q_Jacob) size 20 color "#FFF"
            textbutton '-' action SetVariable('Q_Jacob', Q_Jacob-1)

            textbutton '+' action SetVariable('Q_Jacob', Q_Jacob+1)



        hbox:
            text 'Q_Molly: ' + str(Q_Molly) size 20 color "#FFF"
            textbutton '-' action SetVariable('Q_Molly', Q_Molly-1)

            textbutton '+' action SetVariable('Q_Molly', Q_Molly+1)


        hbox:
            text 'Q_Naomi: ' + str(Q_Molly) size 20 color "#FFF"
            textbutton '-' action SetVariable('Q_Naomi', Q_Naomi-1)

            textbutton '+' action SetVariable('Q_Naomi', Q_Naomi+1)



        hbox:
            text 'Q_Sabrina: ' + str(Q_Sabrina) size 20 color "#FFF"
            textbutton '-' action SetVariable('Q_Sabrina', Q_Sabrina-1)

            textbutton '+' action SetVariable('Q_Sabrina', Q_Sabrina+1)


        hbox:
            text 'Q_Audrey: ' + str(Q_Audrey) size 20 color "#FFF"
            textbutton '-' action SetVariable('Q_Audrey', Q_Audrey-1)

            textbutton '+' action SetVariable('Q_Audrey', Q_Audrey+1)







screen map_screen:
    zorder 205
    imagebutton:
        idle '#0000'
        hover '#0000'
        action NullAction()
    add 'bg_map_' + str(time_now)
    textbutton 'X' xalign .95 yalign .05 action Hide('map_screen', transition = Dissolve(.5)) text_size 50 text_color '#F00' text_bold True

    imagebutton:
        idle Transform('campus.png', alpha = .1)
        hover Transform('campus.png', alpha = .5)
        focus_mask True
        hovered Function(show_up_donw_text, text_now = "Campus", x_now = 1120, y_now = 400+100)
        unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
        action Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(set_locations, loc = 'campus')

    imagebutton:
        idle Transform('academy.png', alpha = .1)
        hover Transform('academy.png', alpha = .5)
        focus_mask True
        hovered Function(show_up_donw_text, text_now = "Academy", x_now = 1400, y_now = 280)
        unhovered Hide('text_animation_up_screen'), SetField(config, 'mouse', None),
        action Hide('text_animation_up_screen'), SetField(config, 'mouse', None), Function(set_locations)

transform show_hide_locations_trans(xp):
    on show:
        xpos xp yalign 1.0
        easein_quart .5 xpos 0 yalign 1.0
    on hide:
        xpos 0 yalign 1.0
        easeout_quart .5 xpos xp yalign 1.0

transform show_hide_locations_trans_2(xp):
    on show:
        xpos xp yalign 1.0
        easein_quart .5 xpos 0 yalign 1.0


screen show_hide_locations_2:
    zorder 200
    # else:
    #     timer .1 action [
    #     Hide('show_hide_locations'), 
    #     Show('show_hide_locations_2'),
    #     Hide('text_animation_up_screen_3')
    #     ]
    if hasattr(store, 'ep2start') and not hide_interface and renpy.get_screen('main_interface'):
        if show_hide_locations_pos:
            timer .1 action [
           Hide('show_hide_locations_2'), 
           Hide('text_animation_up_screen_3'), 
           Show('show_hide_locations')
           ]  
        button:
            add 'show_button'
            yalign 1.0
            action [
            Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_game_click.mp3'), 
            Hide('show_hide_locations_2'),
            Function(lambda:Show('show_hide_locations')()),
            Function(lambda:SetVariable('show_hide_locations_pos', True)()),

            
            ]
            at show_hide_locations_trans_2(-125)
init python:
    def tmp_change_location(i, text_now = '', x_now = 0, y_now = 0):
        Hide('text_animation_up_screen')()
        Hide('text_animation_up_screen_2')()
        Hide('text_animation_up_screen_3')()
        #Show('text_animation_up_screen_3', text_now = text_now, x_now = x_now, y_now = y_now)()
        
        Function(set_mouse_to_default)()
        Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3')()
        Function(change_location, location = i.image_name)()


screen show_hide_locations:
    if 'dale' in location_now:

        $ locations_now_tmp = locations_dale
    elif locations_now[len(locations_now)-1].name == 'Cafe' and time_now == 1:
        $ locations_now_tmp = locations_now[:len(locations_now)-1]

    else:
        $ locations_now_tmp = locations_now
    zorder 200
    default scr_location_now = None
    if not hide_interface and renpy.get_screen('main_interface'):
        viewport:
            xmaximum 1920
            ymaximum 1080
            at show_hide_locations_trans(-(len(locations_now_tmp)*115+90))
                
                #for i in locations_now_tmp:
            viewport:
                xmaximum 80*len(locations_now_tmp)+83
                ymaximum 95
                image Frame('locations_main/location_buttons/location_buttons_bg.png')
                yalign 1.0
                #        add '#000'
                #viewport:
                #    xmaximum 25
                #    ymaximum 95
                #    add '#000'
            hbox yalign .99 xpos 25:
                spacing 3
                for i in locations_now_tmp:
                    viewport ypos 25:
                        xmaximum 80
                        ymaximum 80

                        viewport:
                            xmaximum 80
                            ymaximum 80
        
                            imagebutton xalign .5 yalign i.yalign:

                                idle  AlphaMask(Transform(i.image, xalign = .5, yalign = .5, zoom = .5), 'images/locations_main/location_buttons/locations_polygon.png')
                                
                                hover AlphaMask(Transform(i.image, xalign = .5, yalign = .5, zoom = .5), 'images/locations_main/location_buttons/locations_polygon.png')
                                hovered   [
                                Function(show_up_donw_text, text_now = i.name, x_now = i.cor_x-30, y_now = 980), 
                                SetScreenVariable('scr_location_now', i.image_name)]
                                unhovered [
                                SetScreenVariable('scr_location_now', None),
                                Hide('text_animation_up_screen')
                                ]
                                if 'dale' in location_now:
                                    
                                    if 'spa' in i.image_name:
                                        if time_now in (1, 4):
                                            action NullAction(), Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3')

                                        else:
                                            action Function(tmp_change_location, i = i, text_now = i.name, x_now = i.cor_x, y_now = 1100,)
                                    
                                    elif 'shop' in i.image_name:
                                        if time_now == 4:
                                            action NullAction(), Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3')

                                        else:
                                            action Function(tmp_change_location, i = i, text_now = i.name, x_now = i.cor_x, y_now = 1100,)
                                    else:
                                        action Function(tmp_change_location, i = i, text_now = i.name, x_now = i.cor_x, y_now = 1100,)


                                elif location_now != i.image_name:
                                    action Function(tmp_change_location, i = i, text_now = i.name, x_now = i.cor_x, y_now = 1100,)
                                else:
                                    action Function(renpy.play, channel = 'sound', filename = 'audio/new/gameplay/click_button2.mp3')






                                #hovered Function(show_up_donw_text, text_now = i.name, x_now = i.cor_x, y_now = 1100, screen_2 = True)
                                #unhovered Hide('text_animation_up_screen_2'), SetField(config, 'mouse', None),
                        if not ((location_now == i.image_name) or (scr_location_now == i.image_name)):
                            add 'locations_polygon_0' xalign .5 yalign i.yalign #alpha .5# zoom .702

                        else:
                            add 'locations_polygon_gold' xalign .5 yalign i.yalign #alpha .5 zoom .702
                viewport:
                    xmaximum 115
                    ymaximum 102
                    ypos 10
                    has button xpos 0:
                        add 'hide_button' 
                        action [
                        Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_game_click.mp3'),
                        Hide('show_hide_locations'),
                        Function(lambda:SetVariable('show_hide_locations_pos', False)()),
                        Show('show_hide_locations_2'),
                        Hide('text_animation_up_screen_3')
        
                ]


label parents_room_cupboard_1_label:
    hide screen main_interface 
    scene expression 'images/prologue/0_011.webp'




    with Dissolve(.3)

    $ don_cupboard_n = renpy.call_screen('don_cupboard', money = not hasattr(store, 'get_money'))
    $ Hide('text_animation_up_screen')()
    $ SetField(config, 'mouse', None)()



    if don_cupboard_n == '2':
        $ don_cupboard_2 = 1
        "[Name]" "{i}(At least I know they're not trying to kick me out to make room for a new baby...){/i}"

    elif don_cupboard_n == '1':
        $ don_cupboard_1 = 1
        "[Name]" "{i}(These files are probably older than me. Nothing intresting.){/i}"

    elif don_cupboard_n == '3':
        $ don_cupboard_3 = 1
        "[Name]" "{i}(Never saw any of them read a single book, so It's probably an organizer...){/i}"
    elif True:

        $ change_location(location = 'parents_room')


    jump parents_room_cupboard_1_label
label parents_room_cupboard_2_label:
    hide screen main_interface 
    scene expression 'images/prologue/0_012.webp'
    show expression 'images/main_interface/locations/IMG_3107_0.png'
    if not hasattr(store, 'get_money'):
        show expression 'images/main_interface/locations/IMG_3106_0.png'
    with Dissolve(.3)

    $ olivia_bag_n = renpy.call_screen('olivia_bag', money = not hasattr(store, 'get_money'))



    if olivia_bag_n == 'money':


        $ Hide('text_animation_up_screen')()
        $ SetField(config, 'mouse', None)()

        "[Name]" "{i}(To take or not to take, that is the question...){/i}"

        menu:
            "Take" if True:
                "[Name]" "{i}(Bingo! There goes the initial rent for the room.){/i}"
                $ get_money = True
                $ money    += 5
                play sound 'audio/new/gameplay/take_money2.mp3'
            "Don't take" if True:
                $ pass


    elif olivia_bag_n == 'bag':
        $ olivia_bag_n_bag = True
        "[Name]" "{i}(Never undestood why Olivia needs to keep so much in her purse...){/i}"
        "[Name]" "{i}(Considering the fact, that she barely leaves the house...){/i}"
    elif True:
        $ change_location(location = 'parents_room')


    jump parents_room_cupboard_2_label

label parents_room_photo_label:
    hide screen main_interface 
    $ parents_room_photo = True
    scene sc i_0_011_2 with Dissolve(.5)
    "[Name]" "{i}(Photo of Ashley from her last competition...){/i}"
    show sc i_0_011_2 with my_dissolve
    "[Name]" "{i}(She's so flexible!){/i}"
    show sc i_0_011_2 with my_dissolve
    "[Name]" "{i}(I wonder where else she can put this agility in use...){/i}"
    $ change_location(location = 'parents_room')
label parents_room_painting_label:
    hide screen main_interface 
    $ parents_room_painting = True
    show sc i_0_009 with my_dissolve
    "[Name]" "{i}(Don's favourite painting.){/i}"
    show sc i_0_009 with my_dissolve
    "[Name]" "{i}(He is very proud that his ancestors were among the first colonists.){/i}"
    show sc i_0_009 with my_dissolve
    "[Name]" "{i}(I remember him boasting that the man on the white horse was his great-great-great grandfather.){/i}"
    show sc i_0_009 with my_dissolve
    "[Name]" "{i}(Scumbag never heard of googling by the picture.){/i}"
    show sc i_0_009 with my_dissolve
    "[Name]" "{i}(The painting was sold on Craigslist for $15 few years ago.){/i}"
    show sc i_0_009 with my_dissolve
    "[Name]" "{i}(I wonder what else he lied about?){/i}"
    $ change_location(location = 'parents_room')

label bath_breth_label:
    hide screen main_interface 
    $ bath_breth = True

    "[Name]" "{i}(Ashley seems to have forgotten to hide her toothbrush.){/i}"

    "[Name]" "{i}(She got the whole sink dirty... Olivia will get mad.){/i}"
    $ change_location(location = 'bath')

label bath_duck_label:
    hide screen main_interface 
    if not hasattr(store, 'bath_duck'):
        $ bath_duck = True

        "[Name]" "{i}(Samantha and Ashley's ducks.){/i}"

        "[Name]" "{i}(No one's bathed with them in 100 years, but I hate to throw them away.){/i}"

        "[Name]" "{i}(And it's kind of cozy with them here...){/i}"
    $ change_location(location = 'bath')



label close_room_label:


    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.1)

    menu:
        "Closed" if True:
            $ pass
    show screen main_interface 
    show screen show_hide_locations_2
    hide screen black_tmp_screen_menu

    with Dissolve(.5)

    jump main_interface_label

label picture_in_mc_room:


    $ picture_in_mc_room_variable = True
    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface

    with Dissolve(.1)
    if time_now == 1:
        '[Name]' "{i}(Is it just me, or was that picture moving?){/i}"
        '[Name]' "{i}(Hmm, i'll have to take a closer look...){/i}"
        '[Name]' "{i}(It moved! Did you see it?){/i}"
        '[Name]' "{i}(Who am I talking to anyway, i'm here alone...){/i}"
    elif time_now == 2:
        '[Name]' "{i}(I feel strange vibrations coming from this painting.){/i}"
        '[Name]' "{i}(I wonder who could know anything about it?){/i}"
        '[Name]' "{i}(I could have sworn I heard quiet laughter...){/i}"
        '[Name]' "{i}(This painting is driving me crazy!){/i}"
    elif time_now == 3:
        '[Name]' "{i}(Sometimes I feel as if dim light is coming from that painting...){/i}"
        '[Name]' "{i}(Am I going crazy?){/i}"
        '[Name]' "{i}(Is it just me, or was that picture moving?){/i}"
        '[Name]' "{i}(Hmm, I'll have to take a closer look...){/i}"
    elif time_now == 4:
        '[Name]' "{i}(I feel strange vibrations coming from this painting.){/i}"
        '[Name]' "{i}(I wonder who could know anything about it?){/i}"
        '[Name]' "{i}(It moved! Did you see it?){/i}"
        '[Name]' "{i}(Who am I talking to anyway, I'm here alone...){/i}"


    show screen main_interface 
    show screen show_hide_locations_2
    hide screen black_tmp_screen_menu

    with Dissolve(.5)

    jump main_interface_label

label rune_in_mc_room:
    $ rune_in_mc_room_variable = True
    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface

    with Dissolve(.1)
    if time_now == 1:
        '[Name]' "{i}(What strange symbols...){/i}"
        '[Name]' "{i}(I'm sure they're there for a reason...){/i}"
        '[Name]' "{i}(But how do you know what secrets they hold?){/i}"
        '[Name]' "{i}(Mystery...){/i}"


    elif time_now == 2:
        '[Name]' "{i}(Those symbols, I can't stop thinking about them...){/i}"
        '[Name]' "{i}(It's some kind of runes, I quess.){/i}"
        '[Name]' "{i}(But what are they for?){/i}"
        '[Name]' "{i}(Mystery...){/i}"
    elif time_now == 3:

        '[Name]' "{i}(How stupid would it be, if it's just a decoration.){/i}"
        '[Name]' "{i}(No, It can't be...){/i}"
        '[Name]' "{i}(But what is this){/i}"
        '[Name]' "{i}(Mystery...){/i}"
    elif time_now == 4:
        '[Name]' "{i}(These strange runes...){/i}"
        '[Name]' "{i}(If only I could find out what do they do...){/i}"
    show screen main_interface 
    show screen show_hide_locations_2
    hide screen black_tmp_screen_menu

    with Dissolve(.5)

    jump main_interface_label
label mina_dale_hotel_1_label:


    stop music_2 fadeout 1
    play music 'audio_ep2/SC/8. Beautiful people.mp3' fadein 1.0



    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface 
    scene sc i_dale_hotel_1_1 with Dissolve(.5)

    #"???????? ?????? ?????????? ????????????????: ???????? ?????????? ???? ??????????????, ???? ???????? ???????????????????????? ???? ???????????????? ?????????? ?????? ??????????????????????????, ???????????????????????????? ?? ?????????????????? ????,

    # #???? ?????????????????????? ?? ???????????????????? ?????? ??????????????, ???????? ???????????????? ???? ???????????? ?????? ????????, ???? ?????????????? ?????? ?????????????????????? ???????????? ???????????? ?????????????? ???? ????????????, ???? ???????? ?????????? ?????????????? ?? ?????????????????? ???????????????? ???? ???????????????? ??????????. ???? ?????????????? ?????????????? ?????????????? ?? ?????????? ???????? ?????? ?????????? ?????????? ??????????."
    # show sc i_Mina_anim_1 with my_dissolve
    # "[Name]" "(?????????????? ?????? ?????????????? ??????????.)"
    # show sc i_Mina_anim_1_z with my_dissolve
    # "[Name]" "(??????????????????, ?? ?????? ???????? ???????????? ?????? ???????????????????)"
    # "[Name]" "(????, ?????????????? ?????????? ?????? ?????????? ???????????????? ??????????.)"
    # "Unknown Girl" "????????????????????????! ?????????? ???????????????????? ?? ??????????-???? ????????????????????!"
    # show sc i_Mina_1_1 with my_dissolve
    # "Mina" "???????? ?????????? ????????. ?????? ?? ???????? ?? ?????? ?????????????????????"
    # "[Name]" "?????????????? ????????????????????????. ???????? ?????????? [Name]."
    # "Mina" "[Name], ???? ?????????? ?????????????? ???? ?????????"
    # show sc i_Mina_1_2 with my_dissolve
    # "[Name]" "???? ???????????????? ???? ?????????????????????"
    # "Mina" "??????, ?????????????"
    # "[Name]" "???????????? ???? ?????? ???????????????? ?????????????????? ?????? ??????????!"
    # show sc i_Mina_1_3 with my_dissolve
    # "Mina" "????-????."
    # "[Name]" "(?????????? ?????? ??????????????.)"
    # show sc i_Mina_1_2 with my_dissolve
    # "Mina" "???????????? ?????????????????????? ?????????? ???????????? ?? ??????????????."
    # "Mina" "?????????????????? ?????????? ?????????? ?????????????????????? ???????????????????????????? ?????????? ???? ?????? ????????????????."
    # "[Name]" "??????????????."
    # "Mina" "??????????????????. ?????????????????????? ?????????????? ?? ??????????."
    # show sc i_Mina_1_4 with my_dissolve
    # "Mina" "?????? ?????? ???????????? ?? ?????? ???????????????? ???????????? ?????????????? ?????????????? ?? ?????????????????????????? ????????????????."
    # "[Name]" "??????????????. ?? ?????????? ?? ?????? ?????????????????"
    # "Mina" "$5 ???? ????????."
    # "[Name]" "??????????. ??????????????."
    # show sc i_Mina_1_5 with my_dissolve
    # "Mina" "?? ???????? ?????? ??????-???? ?????? ?????????????"
    # menu:
    #     "?????? ???? ??????????????":
    #         show sc i_Mina_1_5 with my_dissolve
    #         "[Name]" "???? ?????? ?????????????????? ????????????, ?????? ?????? ???????????? ????????????????????."
    #         "[Name]" "???? ????????????????????, ?????? ???? ???????????"
    #         show sc i_Mina_1_6 with my_dissolve
    #         "Mina" "????, ??????...???? ??????, ??????????????..."
    #         "[Name]" "(???????? ?????? ???? ?????? ?????????????????????)"
    #         "[Name]" "(?? ???? ?????? ?????????? ???????? ?????????? ?????????? ???????????????? ??????????...)"
    #         "[Name]" "(Delta of Venus? ?????????? ?????? ???? ?????????????? ??????????-?????????????)"
    #         "[Name]" "(?? ???? ???? ?????????? ????????????????, ?????????? ???????????????? ???? ???????????? ????????????.)"
    #         show sc i_Mina_1_7 with my_dissolve
    #         "[Name]" "????????. ?????? ?????? ?????????? ?????? ???????????????? ????????????, ?????????? ?????????? ??????????????."
    #         "Mina" "..."
    #         "Mina" "????????????????, ???????????? ???? ???????????????? ?????????????????????? ???? ????."
    #     "???????????? ??????????????????":
    #         show sc i_Mina_1_5 with my_dissolve
    #         "[Name]" "?????????? ???????????? ???????? ???? ?? ?????? ???????????? ?????? ?????????????????? ????????????????."
    #         show sc i_Mina_1_8 with my_dissolve
    #         "Mina" "??, ?????? ???? ???????????????"
    #         "Mina" "?? ?????? ?? ???? ??????????????, ?? ???????????? ???? ???????????????? ??????????????????????..."
    #         "[Name]" "(????? ?? ???????? ???? ???????)"
    #         show sc i_Mina_1_2 with my_dissolve
    #         "[Name]" "???????? ?????????????? ???? ????????????."
    #         "Mina" "??????????????."
    #         "Mina" "???? ?????????? ???????? ?? ?????? ?? ?????????????????? ?????????????????????? ????????????????????????????."
    #         "Mina" "?????????????????????????? ?????????? ???????????????????? ?? ?????????????? ???????????????? ??????????????????."
    #         "[Name]" "????, ???????????????? ??????????????!"
    #         show sc i_Mina_1_2 with my_dissolve
    #         "Mina" "?? ???????? ?????? ??????-???? ?????? ?????????????"
    #         "[Name]" "???????????????? ??????. "
    #         "[Name]" "??????????????, ????????."
    #         "Mina" "??????????????????????."
    scene image '#000' with Dissolve(.5)

    jump main_interface_label


    
# label giant_dale_mainstreet_label:
#     stop music_2 fadeout 1
#     play music 'audio_ep2/SC/8. Beautiful people.mp3' fadein 1.0



#     hide screen show_hide_locations
#     hide screen show_hide_locations_2
#     hide screen text_animation_up_screen_3
#     hide screen main_interface 
#     scene image '#000' with Dissolve(.5)
#     menu:
#         "??????????????????????":
#             $ pass
#         "????????????":
#             jump main_interface_label

    
#     "#?????? ???????????? ?????? ???????? ??????????"

#     jump main_interface_label        


# label romul_dale_clubenter_label:



#     hide screen show_hide_locations
#     hide screen show_hide_locations_2
#     hide screen text_animation_up_screen_3
#     hide screen main_interface 
#     scene image '#000' with Dissolve(.5)
#     stop music_2 fadeout 1
#     play music 'audio_ep2/SC/8. Beautiful people.mp3' fadein 1.0
#     "#?????? ?????????????????????? ?????? ???????? ??????????"
#     show sc i_dale_street_2_3  with my_dissolve
# #     "???????????????? ?????????????? ?????? ???? ???? ?????????????????????????? ?????? ????????????????????, ???? ???? ?????????? ?????????????? ?????????? ?????? ?????? ???? 50 ???????????? (???????? ???????????? ??????????????). ???? ?????? ?????????? ?? ????????????????, ?????????? ?? ?????????????????? ?????? ?????????? ???? ??????????. 

# # ?????? ?????????????????????? ?? ?????????? ?????????????????????? ??????. ??????????: ???? ?????????????? ???? ?????????????????? ?? ?????????? ?????? ?????????? ?????????????????????? ?????????????????? ??????????????. ?????? ???????? ?????????????????????? ?? ?????????????? ?? ????????. ?????????? ?????????????? ??????????????????: ???? ?????????????? ???????? ?????????? ???????????? ???? ??????????????. 

# # ???? ?????????? ??????-???? ?????????????????????? ?? ?????????????????????????? ???? ?????????? ?? ????????????????????. ?????? ?????????? ???????????????? ?? ?????????????? ?? ?????????????? ?????? ???? ???????????????? ???????????????????????? ??????????, ?????????????? ?????????? ????????????????. ???? ?????????? ???????????????? ???? ?? ?? ?????????????????????????? ???????????????? ??????????. ?????????? ?????????? ?????? ?????????????????? ????????????, ?????????? ?????????????? ?????? ?????????? ???? ???????????? ???????? ???? ???????????? ?????????? ???? ???????????? ?? ??????????.

# # ?????? ?????????? ???????????????????? ?????? ???? ???????????????? ?? ?????????????????? ?????????? ???????????????? ???? ?????????????? ???????? ?????? ??????????."
#     show sc i_Romul_1_1 with my_dissolve
#     "Romul" "???????? ????????????, ?????????????? ???????????????"
#     "[Name]" "???????????? ???????????? ????????????????????. "
#     "[Name]" "?????? ?????????? ?? ???????? ??????????????????."
#     show sc i_Romul_1_2 with my_dissolve
#     "Romul" "?????????? ???? ?????????????? ?????????????? ????????????, ??????????."
#     "Romul" "???? ???? ??????????????????."
#     "[Name]" "?????? ???????????? ???????!"
#     show sc i_Romul_1_3 with my_dissolve
#     "Romul" "???? ???? ???????????????????????????? ????????????????????."
#     "[Name]" "?????????? ?????????????????????!"
#     "Romul" "???????? ???????????? ????????????????????."
#     "Romul" "???????? ???????? ?????? ???? ????????????????."
#     show sc i_Romul_1_4 with my_dissolve
#     "[Name]" "(???????????? ???????????!)"
#     "[Name]" "(?????????? ?????????????? ???????? ?? ??????????.)"
#     "[Name]" "(???????? ???? ??????-???? ?? ???????????????? ?????????????? ?????????????????? ?????????????????? ??????????.)"
#     show sc i_Romul_1_5 with my_dissolve
#     "Romul" "????... ?????????? ???????? ?? ???????????????????????"
#     "Romul" "?????????? ???????? ???? ???? ?????????? ?? ???????? ?????????? ???????????? ?? ?????????"
#     "[Name]" "(?? ??????????, ?? ???????? ???? ????????????...)"
#     show sc i_Romul_1_6 with my_dissolve
#     "Romul" "?????????? ???? ???????? ????????????..."
#     "Romul" "?? ?????????? ??????????????, ???? ???? ?????????????????? ?????? ??????????????????."
#     show sc i_Romul_1_7 with my_dissolve
#     "Romul" "?? ????????????,  ?? ???????? ?? ???????????????????? ?? ???????????? ??????????!"
#     show sc i_Romul_1_19 with my_dissolve
#     "Romul" "?????????? ???????? ??????-???? ?????????? ???????????? ???????? ?????????? ?????????????????????"
#     "[Name]" "??????????????? "
#     "Romul" "$50"
#     "[Name]" "(?????????? ????????... ?? ???????? ???? ?????????? ????????????, ?????? ????????????.)"
#     scene sc i_Romul_1_7 with Dissolve(.5)
#     menu:
#         "???????? ????????????":
#             $ pass 
#         "????????":
#             jump romul_dale_clubenter_label_42
#     show sc i_Romul_1_8 with my_dissolve
#     "[Name]" "???????? ?? ??????????, ????????????????."
#     "Romul" "?????????"
#     "[Name]" "???? ????????????, ???????? ????????????."
#     "[Name]" "?? ???????? ?????????????"
#     show sc i_Romul_1_9 with my_dissolve
#     "Romul" "??????, ???????? ?? ???? ??????????????????."
#     "Romul" "???? ????????????..."
#     show sc i_Romul_1_20 with my_dissolve
#     "Romul" "?? ??????????????????."
#     "[Name]" "???????????? ??????????, ???????????"
#     "Romul" "?? ?????????????? ???? ?? ???????????????????? ?????????????? ?????????????? ??????????-???? ????????????????."
#     "[Name]" "?? ???????? ????????????????!"
#     show sc i_Romul_1_21 with my_dissolve
#     "Romul" "???? ??????????!"
#     "Romul" "???????????? ?????????????? ????????????? ???????? ???????? ??????????????, ?????????? ?????????? ?? ????????????????."
#     "Romul" "?? ???????? ??????????????, ?????????????? ??????????????????????!"
#     "Romul" "??????, ????????."
#     show sc i_Romul_1_22 with my_dissolve
#     "Romul" "?????? ???????????? ???????????? ?????? ???? ???????????????!"
# label romul_dale_clubenter_label_42:
#     show sc i_Romul_1_10 with my_dissolve
#     "[Name]" "?????? ???????? ???? ??????????."
#     "[Name]" "??????."
#     "Romul" "???????? ????????????, ??????????."
#     show sc i_Romul_1_11 with my_dissolve
#     "[Name]" "(?????? ???? ?????????????? ???????????????????? combta bolt ???? ??????...)"
#     "[Name]" "(????????, ?????????????? ?????????? ?????? ?????????????? ???? ????????????.)"
#     show sc i_Romul_1_12 with my_dissolve
#     "[Name]" "(????, ?????????? ???????????????? ??????.)"
#     "[Name]" "(??????????????????, ?????? ?????? ???????????? ?????????? ???? ??????????.)"
#     "[Name]" "(???? ???????? ???????????????? ??????????????????????..)"
#     "[Name]" "(?????????? ????????????????????!)"
#     show sc i_Romul_1_13 with my_dissolve
#     "Romul" "????????????, ??????????, ???????? VIP ?????? ???? ??????????????."
#     "Romul" "?????????????? ????????????????????, ?????? ?????? ???????? ???????? ???????????? ????????????????."
#     show sc i_Romul_1_14 with my_dissolve
#     "Man" "?????? ?? ???? ?????????? ????????????. ?????????? ????.."
#     show sc i_Romul_1_15 with my_dissolve
#     "Romul" "??????! ??????...?????? ????..."
#     "Man" "??-??-??! ?????? ?????? ????????."
#     show sc i_Romul_1_16 with my_dissolve
#     "Man" "???????????? ???????????? ?????? ??????????????, ?????? ???????????? ???? ??????????????."
#     show sc i_Romul_1_17 with my_dissolve
#     "[Name]" "(??????-???? ?????? ???? ????????????.)"
#     "[Name]" "(?????? ???????? ?????????? ?????? ?????????????????????? ???? ???????????)"
#     "[Name]" "(????????????????-????, ?????? ?????????? ???????? ???? ?????????????????? ?? ????????...)"
#     show sc i_Romul_1_18 with my_dissolve
#     "[Name]" "(?????? ?????????? ??????????????... ?? ???????????? ???? ?????? ????????????????????.)"
#     show sc i_Romul_1_18 with my_dissolve
#     "[Name]" "(?????????? ?? ???????????????????? ???? ???????????? ??????????????????...)"
#     "[Name]" "(???? ???? ???????? ???? ???????????? ?????? ?????? ?????????????????)"


#     hide screen show_hide_locations
#     hide screen show_hide_locations_2
#     hide screen text_animation_up_screen_3
#     hide screen main_interface 
#     scene image '#000' with Dissolve(.5)
    
#     jump main_interface_label

# # Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

