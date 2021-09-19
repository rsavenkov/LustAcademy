

init 9 python:
    import pygame, datetime, subprocess 

    class CaffeMiniGame(renpy.Displayable):
        def __init__(self, **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
        
        def render(self, width, height, st, at):
            rend = renpy.Render(1920, 1080)
            renpy.redraw(self, 0)
            return rend
        
        def event(self, event, x, y, st):
            pass
    coffe_game_log   = None
    coffe_game_log_2 = None
    def set_order(order):
        
        global coffe_game_start, coffe_game_log
        if order != order_list[coffe_game_start-1]:
            coffe_lose(order_list[coffe_game_start-1], order)
        
        else:
            if coffe_game_start < 3:
                coffe_game_start += 1
            else:
                coffe_game_log = 'Win!'
                renpy.end_interaction('Win!')
    def coffe_lose(tm1, tm2, timer = False):
        global coffe_game_log, coffe_game_log_2
        if timer:
            coffe_game_log_2 = 'Ты не успел обслужить гостей вовремя.'
        
        else:
            coffe_game_log_2 = 'Ты перепутал заказ: вместо числа '+str(tm1)+ ' указал число '+ str(tm2)
        
        coffe_game_log   = 'Lose'
        renpy.end_interaction('Lose')
transform hide_my_choice():
    on show:
        alpha 0.0
        linear .5 alpha 1.0
    on hide:
        alpha 1.0
        linear .5 alpha 0.0
screen coffe_game_start_screen:
    key "game_menu" action NullAction()
    key "rollback" action NullAction()
    viewport:
        at hide_my_choice

        add '#fff0'
        hbox xalign .5 ypos 910:
            for i in xrange(10):
                viewport:
                    xmaximum 93
                    ymaximum 95
                    add '#0000'
                    imagebutton:
                        idle Transform('mini_games/caffe/foods/food_' + str(i) + '.png', zoom = .7)
                        hover Transform(im.MatrixColor('mini_games/caffe/foods/food_' + str(i) + '.png', im.matrix.brightness(.3)), zoom = .7)
                        xalign .5 yalign .5
                        action Function(set_order, i)
    viewport:
        xmaximum 535
        ymaximum 275
        add '#0000'
        vpgrid cols 3 rows 1:
            yspacing 45
            xspacing 25
            xalign .52 yalign .4
            for i in xrange(10):
                viewport:


                    xmaximum 120
                    ymaximum 120
                    add '#0000'

                    if i < len(order_list) and i < coffe_game_start-1:
                        add 'mini_games/caffe/foods/food_' + str(order_list[i]) + '.png' xalign .5 yalign .5 zoom .8






        xalign .5 yalign .2





























screen lose_win_caffe_screen():
    key "game_menu" action NullAction()
    key "rollback" action NullAction()
    if 'Ты закончил работу' not in coffe_game_log_2:
        viewport:
            xmaximum 390
            ymaximum 105
            xalign .5 yalign .2
            if 'Всё сделал правильно и получил чаевые $5' in coffe_game_log_2:
                add 'cafe_win_bg'
                text 'SUCCESS!' xalign .5 yalign .5 font 'fonts/h_font.ttf' size 67 color '#AEFF88'

            else:
                add 'cafe_lose_bg'
                text 'FAIL' xalign .5 yalign .5 font 'fonts/h_font.ttf' size 67 color '#FF855F'
    else:
        viewport:
            xmaximum 628
            ymaximum 100
            xalign .5 yalign .2

            text 'The work is done.' xalign .5 yalign .5 font 'fonts/h_font.ttf' size 67 color '#79BFFF'
        hbox:
            xalign .5 yalign .35
            text "You've earned " font 'fonts/h_font.ttf' size 30
            text ' +' + str(plus_money)+ '$' font 'fonts/h_font.ttf' size 30 color '#5EAB42'
        viewport:
            xmaximum 285
            ymaximum 60
            xalign .5 yalign .5
            imagebutton:
                idle 'order_start_button'
                hover im.MatrixColor('mini_games/caffe/order_start_button.png', im.matrix.brightness(.3))
                action Return()
            text 'Take money' font 'fonts/h_font.ttf' size 30 color '#FFFFFF' xalign .5 yalign .45




    if 'Ты закончил работу' not in coffe_game_log_2:
        if 'Всё сделал правильно и получил чаевые $5' in coffe_game_log_2:
            hbox:
                xalign .5 yalign .35
                text 'Satisfied guests left a tip!' font 'fonts/h_font.ttf' size 30
                text ' +5$' font 'fonts/h_font.ttf' size 30 color '#5EAB42'
        else:
            if 'Ты не успел обслужить гостей' in coffe_game_log_2:
                text 'The guests got tired of waiting and left...' font 'fonts/h_font.ttf' size 30 color '#FFFFFF' xalign .5 yalign .35
            else:
                text 'You messed up the order...' font 'fonts/h_font.ttf' size 30 color '#FFFFFF' xalign .5 yalign .35
        viewport:
            xmaximum 285
            ymaximum 60
            xalign .5 yalign .5
            imagebutton:
                idle 'order_start_button'
                hover im.MatrixColor('mini_games/caffe/order_start_button.png', im.matrix.brightness(.3))
                action Return()
            text 'Next' font 'fonts/h_font.ttf' size 30 color '#FFFFFF' xalign .5 yalign .45
            hbox:
                text '>' font 'fonts/h_font.ttf' size 27 color '#9E9E9E'
                text '>' font 'fonts/h_font.ttf' size 27 color '#9E9E9E'
                xalign .9 yalign .5




































































































screen CaffeMiniGameScreen():
    key "game_menu" action NullAction()
    key "rollback" action NullAction()
    # viewport:
    #     at hide_my_choice

    #     add '#fff0'
    #     add 'cafe_bg_for_text' xalign .5 ypos 917
    #     add 'cafe_bg_for_text_menu' ypos 830+30 xalign .5
    #     text 'Menu' font 'fonts/h_font.ttf' xalign .5 ypos 835+30
    #     hbox xalign .5 ypos 923:
    #         spacing 12
    #         for i in xrange(10):
    #             add 'cafe_polygon'

    image 'caffe_down' yalign .95 xalign .5

    viewport:
        xmaximum 535
        ymaximum 275
        add 'order_bg'
        xalign .5 yalign .2






screen CaffeMiniGameScreenButtons:
    key "game_menu" action NullAction()
    key "rollback" action NullAction()
   # text 'Order ' + str(raund_now) + '/5' xalign .5 yalign .15 font 'fonts/h_font.ttf' size 33
   










    viewport:
        at hide_my_choice

        add '#fff0'
        hbox xalign .5 ypos 910:
            for i in xrange(10):
                viewport:
                    xmaximum 93
                    ymaximum 95
                    add '#0000'
                    imagebutton:
                        idle Transform('mini_games/caffe/foods/food_' + str(i) + '.png', zoom = .7)
                        hover Transform(im.MatrixColor('mini_games/caffe/foods/food_' + str(i) + '.png', im.matrix.brightness(.3)), zoom = .7)
                        xalign .5 yalign .5
                        action NullAction()




    viewport:
        xmaximum 535
        ymaximum 275
        add '#0000'
        viewport:
            xmaximum 35
            ymaximum 40
            image '#0000'
            xalign .63
            text str(raund_now) + '/5' color '#FFEEDE' size 20 font 'fonts/h_font.ttf' yalign .5
        vpgrid cols 3 rows 1:
            yspacing 45
            xspacing 25
            xalign .52 yalign .4
            for i in xrange(10):
                viewport:


                    xmaximum 120
                    ymaximum 120
                    add '#0000'

                    if i < len(order_list):
                        add 'mini_games/caffe/foods/food_' + str(order_list[i]) + '.png' xalign .5 yalign .5 zoom .8


        imagebutton:
            idle  'mini_games/caffe/caffe_start_button.png'
            hover im.MatrixColor('mini_games/caffe/caffe_start_button.png', im.matrix.brightness(.3))
            action Hide('CaffeMiniGameScreenButtons'), Show('CaffeMiniGameScreenButtons2'), Show('coffe_game_start_screen')
            xalign .5 
            yalign .9




        xalign .5 yalign .2



























    imagebutton:
        idle "mini_games/caffe/button_for_left_cafe.png"
        hover im.MatrixColor("mini_games/caffe/button_for_left_cafe.png", im.matrix.brightness(.3))
        action Jump('end_caffe')
        xpos 1200
        ypos 845
transform block_transform:




    linear .5 alpha 1.0

    .5

    linear .5 alpha 0

    repeat
screen CaffeMiniGameScreenButtons2:
    key "game_menu" action NullAction()
    key "rollback" action NullAction()
    default tm = 6
    if tm > 1:
        timer 1 repeat True action SetScreenVariable('tm', tm-1)
    else:
        timer 1 repeat True action Function(coffe_lose, tm1 = 0, tm2 = 0, timer = True)































    viewport:
        xmaximum 448
        ymaximum 440
        add '#0000'
        xalign .5 yalign .1
        text str(tm) xalign .5 yalign 0 font 'fonts/h_font.ttf' size 33

label lose_win_caffe_screen_label:
    if 'Ты закончил работу' not in coffe_game_log_2:
        if 'Всё сделал правильно и получил чаевые $5' in coffe_game_log_2:
            $ tmpp_text       = 'Satisfied guests left a tip! {color=#5EAB42}+5{/color}'
            $ tmppbutton_text = '{size=15}Take money{/size}'
        else:
            if 'Ты не успел обслужить гостей' in coffe_game_log_2:
                $ tmpp_text = 'The guests got tired of waiting and left...' 
            else:
                $ tmpp_text = 'You messed up the order...' 

            $ tmppbutton_text = '{size=15}New order{/size}'
    else:
        $ tmpp_text       = "The work is done.\nYou've earned {color=#5EAB42}+[plus_money]{/color}"
        $ tmppbutton_text = '{size=15}Take money{/size}'
    $ nv = renpy.call_screen('confirm', 
        tmpp_text, 
        Return(), None, yes_text = _(tmppbutton_text), no_text = _('Ok'),)
    if hasattr(store, 'tmppbutton_text'):
        $ del tmppbutton_text
    if hasattr(store, 'tmpp_text'):
        $ del tmpp_text
    return
screen empty_screen_2:
    key "game_menu" action NullAction()
    key "rollback" action NullAction()
    $ pass

label test_coffe_game:
    show expression '#0003'
    hide screen main_interface 
    with Dissolve(.3)
    $ caffe_tutorial = True
    if not mp.tutorial['CAFE']:
        $ tutorial_bb = 0
        call screen tutorial_screen(what_tutor = 'CAFE')
    $ cause_lose       = "None"
    $ plus_money       = 10
    $ raund_now        = 1
    $ lose_quant       = 0
    $ win_quant        = 0
    $ renpy.choice_for_skipping()

label test_coffe_game_raund:
    $ coffe_game_start = 1
    $ coffe_item_now   = 0
    $ menu_list        = [
    ]

    $ order_list       = [
    renpy.random.randint(0, 2), renpy.random.randint(3, 6), renpy.random.randint(7, 9),
    ]
    show screen CaffeMiniGameScreen
    show screen CaffeMiniGameScreenButtons
    call screen empty_screen_2
label end_caffe_2:
    hide screen CaffeMiniGameScreen
    hide screen CaffeMiniGameScreenButtons
    hide screen CaffeMiniGameScreenButtons2
    hide screen coffe_game_start_screen

    if coffe_game_log != 'Lose':
        $ coffe_game_log_2 = 'Молодец! Всё сделал правильно и получил чаевые $5'

        $ plus_money      += 5
        call lose_win_caffe_screen_label from _call_lose_win_caffe_screen_label
        scene sc i_work_1_4 with Dissolve(.5)
        if not win_quant:
            'Molly' "You're doing just fine! Keep up the good work!"
            scene sc i_work_1_5 with Dissolve(.5)
            $ renpy.pause(99999)
        elif win_quant == 1:

            'Molly' "You're a treasure! What would I do without you?"
            scene sc i_work_1_6 with Dissolve(.5)
            $ renpy.pause(99999)
        elif win_quant == 2:

            'Molly' "Just magical! [Name], you're on fire!"
            scene sc i_work_1_7 with Dissolve(.5)
            $ renpy.pause(99999)
        elif win_quant == 3:

            'Molly' "The clients are crazy about you! What's your secret?"
            scene sc i_work_1_8 with Dissolve(.5)
            $ renpy.pause(99999)
        elif True:

            'Molly' "Great job, [Name]! Looks like all the tips are yours today."
            scene sc i_work_1_9 with Dissolve(.5)
            $ renpy.pause(99999)
        $ win_quant += 1
    elif True:
        call lose_win_caffe_screen_label from _call_lose_win_caffe_screen_label_1

        scene sc i_work_1_3 with Dissolve(.5)
        if not lose_quant:
            'Molly' "Hey! If you keep this up, we'll lose all our customers."
        elif lose_quant == 1:
            'Molly' "What's the matter with you today? Pull yourself together, please!"
        elif lose_quant == 2:

            'Molly' "Quit your daydreaming and focus on work, [Name]! "
        elif lose_quant == 3:

            'Molly' "Are you sure you weren't lying that you used to work in the service industry?"
        elif True:

            'Molly' "What's wrong with you today? I don't need that kind of help!"
        $ lose_quant += 1



    if raund_now == 5:
        jump end_caffe


    if raund_now    != 5:
        scene sc i_Activity_Work_1 with Dissolve(.5)
        $ raund_now += 1
        jump test_coffe_game_raund


    jump test_coffe_game


label end_caffe:





    $ money  += plus_money
    $ tmps_raund_now   = win_quant
    $ raund_now        = 5
    $ coffe_game_log_2 = 'Отлично! Ты закончил работу и заработал $[plus_money]!\n +3 балла факультету!'

    $ win  = 'Leonheart'
    $ lose = None
    hide screen CaffeMiniGameScreen
    hide screen CaffeMiniGameScreenButtons
    hide screen CaffeMiniGameScreenButtons2
    hide screen coffe_game_start_screen


    jump hide_all_caffe_screens





label hide_all_caffe_screens:

    hide screen CaffeMiniGameScreen
    hide screen CaffeMiniGameScreenButtons
    hide screen CaffeMiniGameScreenButtons2
    hide screen coffe_game_start_screen
    hide expression '#000a' with Dissolve(.5)

    if plus_money == 10 and not tmps_raund_now:

        scene sc i_work_1_12 with Dissolve(.5)
        "Molly" "Thank you for your help, [Name]."
        "Molly" "I'm very glad I found someone I can count on."
        "[Name]" "Thank you, too, Molly. I'm glad we're working together, too."

    elif tmps_raund_now == 5:

        scene sc i_work_1_10 with Dissolve(.5)
        "Molly" "[Name]! I never thought I'd find the perfect employee..."
        "Molly" "But you and I are taking over! Be sure to come again!"
        "[Name]" "Of course, always happy to spend time with you and make some extra money."

    elif tmps_raund_now == 4:

        scene sc i_work_1_11 with Dissolve(.5)
        "Molly" "Good work today!"
        "Molly" "Come back more often and we'll get rich!"
        "[Name]" "You got it."

    elif tmps_raund_now == 3:

        scene sc i_work_1_12 with Dissolve(.5)
        "Molly" "Good work today. But we can do better!"
        "Molly" "Come again."
        "[Name]" "Always happy to help."

    elif tmps_raund_now == 2:

        scene sc i_work_1_12 with Dissolve(.5)
        "Molly" "Yeah, well...{w} It could have been better."
        "Molly" "I hope you'll learn in time."
        "[Name]" "I guarantee it!{w} Until next time!"

    elif tmps_raund_now == 1:

        scene sc i_work_1_13 with Dissolve(.5)
        "Molly" "There were a lot of complaints about you today. What's the matter?"
        "Molly" "Are you sick?"
        "[Name]" "No, I don't know what came over me. Next time will be better."

    elif tmps_raund_now == 0:

        scene sc i_work_1_14 with Dissolve(.5)
        "Molly" "Goblin socks, [Name]! Thanks for volunteering, of course..."
        "Molly" "But you're no help at all."
        "[Name]" "Yes, something went wrong, sorry. But next time it'll be fine."


    show expression '#000a' with Dissolve(.5)
    $ caffe_tutorial = False
    call lose_win_caffe_screen_label from _call_lose_win_caffe_screen_label_2

    $ change_location_2(location_now, time_now+1, plus = True, caffe = True)

    jump main_interface_label






screen tmp_tmp_tmp_pass_screen():
    zorder 300
    imagebutton:
        idle '#0000'
        hover '#0000'
        action NullAction()



label test_coffe_game_menu:


    show screen tmp_tmp_tmp_pass_screen

    hide screen text_animation_up_screen
    hide screen test_duel_choice_mag
    hide screen show_hide_locations_2
    hide screen show_hide_locations


    with Dissolve(.5)
    menu:
        "Work" if True:

            hide screen tmp_tmp_tmp_pass_screen
            jump test_coffe_game
        "Not now" if True:

            hide expression '#000a'
            hide screen tmp_tmp_tmp_pass_screen
            with Dissolve(.5)

            jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
