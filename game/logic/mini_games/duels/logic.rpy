
transform choose_your_stance_transform(x_start, shift_x, yp):
    on show:
        xpos x_start
        ypos yp
        easein_quart .5 xpos shift_x
    on hide:
        xpos shift_x
        ypos yp

        easeout_quart .5 xpos x_start-200

init 9 python:
    import pygame, datetime, subprocess 
    def spells_up_tmp_up(spell, up):
        global spells_up_tmp 
        spells_up_tmp[spell] += up
    class DuelMiniGame(renpy.Displayable):
        def __init__(self, **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
        
        def render(self, width, height, st, at):
            rend = renpy.Render(1920, 1080)
            renpy.redraw(self, 0)
            return rend
        
        def event(self, event, x, y, st):
            pass


    enemy_mag        = 'd'
    gg_mag           = 'd'
    duel_damage      = 0
    duel_damage_name = 'Combat Bolt'

    def set_potion(potion = 'Lesser Heal'):
        global potions, gg_stamina, gg_stoneskin, gg_inspiration, magic_reflection
        potions[potion]     -= 1
        if potion == 'Lesser Heal':
            gg_stamina = min(500, gg_stamina+50)
            Hide('text_animation')()
            
            Show(
            'text_animation', 
                text_now = str(+50),
                x_now = 1610, 
                y_now = 30)()
        if potion == 'Stoneskin':
            gg_stoneskin     = 1
        if potion == 'Inspiration':
            gg_inspiration   = 1
        if potion == 'Magic Reflection':
            magic_reflection = 1



    def test_duel_choice_mag_def(imn, xp, yp):
        global enemy_mag, gg_mag, enemy_stan, stance, gg_stan
        
        if gg_stan:
            gg_mag     = 'p'
            gg_stan    = False
        if enemy_stan:
            enemy_mag  = 'p' 
            enemy_stan = False
        else:
            enemy_mag = renpy.random.choice(['d', 'a', 's'])
        
        
        Show('test_duel_choice_mag', imn = imn, xp = xp, yp = yp)()
        stance = False
        Hide('choose_your_stance_screen')()
        gg_mag    = imn[3:]

    def check_winner():
        global enemy_mag, gg_mag, gg_stan
        if gg_stan or gg_mag == 'p':
            return 'lose'
        if enemy_mag == 'p':
            return 'win'
        if gg_mag == 'd':
            if   enemy_mag == 'a':
                return 'win'
            elif enemy_mag == 's':
                return 'lose'
            else:
                return 'draw'
        
        elif gg_mag == 'a':
            if   enemy_mag == 's':
                return 'win'
            elif enemy_mag == 'd':
                return 'lose'
            else:
                return 'draw'
        
        elif gg_mag == 's':
            if   enemy_mag == 'd':
                return 'win'
            elif enemy_mag == 'a':
                return 'lose'
            else:
                return 'draw'

    def set_los(trans, st, at):
        xxx = check_winner()
        if xxx == 'win':
            trans.xpos = 800 + renpy.random.randint(0, 150)
        else:
            trans.xpos = 800 + renpy.random.randint(0, 150)
        
        
        return None









    def throw_vial():
        global enemy_stamina, gg_inspiration, combat_ball
        Hide('text_animation')()
        Hide('text_animation_2')()
        combat_ball = True

    def incendio():
        global enemy_stamina, enemy_burn, enemy_burn_need, gg_inspiration
        Hide('text_animation')()
        Hide('text_animation_2')()
        if gg_inspiration:
            gg_inspiration -= 1
            enemy_stamina  -= 125
            Show(
               'text_animation', 
               text_now = str(-125),
               x_now = 250, 
               y_now = 30)()
        else:
            enemy_stamina  -= 100
            Show(
               'text_animation', 
               text_now = str(-100),
               x_now = 250, 
               y_now = 30)()
        if renpy.random.randint(1, 2) == 2:
            enemy_burn_need = True






    def episkey():
        global gg_stamina, gg_heal_need
        gg_stamina = min(500, gg_stamina+100)
        Hide('text_animation')()
        Hide('text_animation_2')()
        Show(
               'text_animation', 
               text_now = str(+100),
               x_now = 1610, 
               y_now = 30)()
        if renpy.random.randint(1, 2) == 2:
            gg_heal_need = True     


    def rictusempra():
        global enemy_stamina, enemy_stan, gg_inspiration
        Hide('text_animation')()
        Hide('text_animation_2')()
        if gg_inspiration:
            gg_inspiration -= 1
            enemy_stamina  -= 125
            Show(
               'text_animation', 
               text_now = str(-125),
               x_now = 250, 
               y_now = 30)()
        
        else:
            enemy_stamina -= 100
            Show(
               'text_animation', 
               text_now = str(-100),
               x_now = 250, 
               y_now = 30)()
        if renpy.random.randint(1, 2) == 2:
            enemy_stan = True



    class MagickDuel():
        def __ini__(self, name, description, action):
            self.name        = name
            self.description = description
            self.action      = action
transform text_animation_up(x_start, y_start, shift_y):
    xpos x_start
    ypos y_start
    on show:
        linear 1.5 xpos x_start ypos shift_y alpha 0.0
screen text_animation(text_now, x_now, y_now):

    key "rollback" action NullAction()
    zorder 300
    if '-' in text_now:
        text str(text_now):
            color '#f00'

            italic True
            outlines [(6, "#000", 0, 0)]
            size 25
            at text_animation_up(x_now, y_now, y_now-100)

    else:

        text '+' + str(text_now):
            color '#00b300'

            italic True
            outlines [(6, "#000", 0, 0)]
            size 25
            at text_animation_up(x_now, y_now, y_now-100)


screen text_animation_2(text_now, x_now, y_now):

    key "rollback" action NullAction()
    zorder 300
    if '-' in text_now:
        text str(text_now):
            color '#f00'

            italic True
            outlines [(6, "#000", 0, 0)]
            size 25
            at text_animation_up(x_now, y_now, y_now-100)

    else:

        text '+' + str(text_now):
            color '#00b300'

            italic True
            outlines [(6, "#000", 0, 0)]
            size 25
            at text_animation_up(x_now, y_now, y_now-100)


screen test_duel_game_win_screen:

    key "rollback" action NullAction()

    default potion_use = False
    viewport:
        at choose_your_stance_transform(x_start = 2200, shift_x = 1350, yp = 300)
        xmaximum 570
        ymaximum 570
        add 'spells_bg'

        vbox:
            spacing 15
            hbox:

                viewport:
                    ypos 30
                    xpos 60
                    xmaximum 513
                    ymaximum 105
                    imagebutton:
                        idle 'spell_bg'
                        hover im.MatrixColor("mini_games/duels/spell_bg.png", im.matrix.brightness(.3))
                        action Function(throw_vial), Return()
                    text 'Combat Bolt' ypos 10 xpos 100 size 25 color '#96D9FF' font 'fonts/h_font.ttf'
                    text 'Medium Reduction in opponent Stamina.' xpos 100 yalign .53 size 17 color '#C4C4C4' font 'fonts/h_font.ttf'
                add 'combat_ball_icon' xpos -505

            if gg_mag == 'a':
                hbox:

                    viewport:
                        ypos 30
                        xpos 60
                        xmaximum 513
                        ymaximum 105
                        imagebutton:
                            idle 'spell_bg'
                            hover im.MatrixColor("mini_games/duels/spell_bg.png", im.matrix.brightness(.3))
                            action NullAction()
                        text 'Incendio' ypos 7 xpos 100 size 25 color '#FFAC89' font 'fonts/h_font.ttf'


                        text 'This spell is not learned yet.' xpos 100 yalign .53 size 17 color '#C4C4C4' font 'fonts/h_font.ttf'

                        viewport:
                            xmaximum 500
                            add '#000a'

                    add 'mini_games/duels/Incendio_icon.png' xpos -505


            elif gg_mag == 'd':
                hbox:

                    viewport:
                        ypos 30
                        xpos 60
                        xmaximum 513
                        ymaximum 105
                        imagebutton:
                            idle 'spell_bg'
                            hover im.MatrixColor("mini_games/duels/spell_bg.png", im.matrix.brightness(.3))
                            action NullAction()
                        text 'Episkey' ypos 7 xpos 100 size 25 color '#FFF48E' font 'fonts/h_font.ttf'

                        text 'This spell is not learned yet.' xpos 100 yalign .52 size 17 color '#C4C4C4' font 'fonts/h_font.ttf'

                        viewport:
                            xmaximum 500
                            add '#000a'

                    add 'mini_games/duels/Episkey_icon.png' xpos -505


            else:

                hbox:

                    viewport:
                        ypos 30
                        xpos 60
                        xmaximum 513
                        ymaximum 105
                        imagebutton:
                            idle 'spell_bg'
                            hover im.MatrixColor("mini_games/duels/spell_bg.png", im.matrix.brightness(.3))
                            action NullAction()
                        text 'Rictusempra' ypos 7 xpos 100 size 25 color '#A0FF88' font 'fonts/h_font.ttf'

                        text 'This spell is not learned yet.' xpos 100 yalign .53 size 17 color '#C4C4C4' font 'fonts/h_font.ttf'

                        viewport:
                            xmaximum 500
                            add '#000a'

                    add 'mini_games/duels/rictusempra_icon.png' xpos -505

        hbox:
            xpos 25
            ypos 420
            viewport:
                xmaximum 130
                ymaximum 130
                add '#fff0'
                $ ptmps = potions['Lesser Heal']
                if ptmps:
                    imagebutton:
                        idle 'mini_games/duels/Lesser Heal.png'
                        hover im.MatrixColor('mini_games/duels/Lesser Heal.png', im.matrix.brightness(.3))
                        focus_mask None
                        if potion_use:
                            action NullAction()
                        else:
                            action SetScreenVariable('potion_use', True), SetVariable('potion_now', True), Function(set_potion, potion = 'Lesser Heal')
                        xalign .5 yalign .5
                    text str(ptmps) size 25 font 'fonts/h_font.ttf'
                if potion_use and ptmps:



                    add im.Grayscale('mini_games/duels/Lesser Heal.png') xalign .5 yalign .5


            viewport:
                xmaximum 130
                ymaximum 130
                add '#fff0'
            viewport:
                xmaximum 130
                ymaximum 130
                add '#fff0'
            viewport:
                xmaximum 130
                ymaximum 130
                add '#fff0'























screen enemy_choose_magick():

    key "rollback" action NullAction()
    default enemy_mag_tmp = 0

    if 's' in enemy_mag:

        if renpy.random.randint(1, 5) in [1, 2, 3]:
            if renpy.random.randint(1, 5) in [1, 2, 3]:
                if hasattr(store, 'magic_reflection') and magic_reflection:
                    timer .5 action SetScreenVariable('enemy_mag_tmp', 'Rictusempra'), SetVariable('enemy_stan', True)
                else:
                    timer .5 action SetScreenVariable('enemy_mag_tmp', 'Rictusempra'), SetVariable('gg_stan_need', True)
            else:
                timer .5 action SetScreenVariable('enemy_mag_tmp', 'Rictusempra')
        else:
            timer .5 action SetScreenVariable('enemy_mag_tmp', 'Combat Bolt')

    elif 'a' in enemy_mag:
        if renpy.random.randint(1, 5) in [1, 2, 3]:
            if renpy.random.randint(1, 5) in [1, 2, 3]:
                if hasattr(store, 'magic_reflection') and magic_reflection:
                    timer .5 action SetScreenVariable('enemy_mag_tmp', 'Incendio'), SetVariable('gg_burn_need', True)
                else:
                    timer .5 action SetScreenVariable('enemy_mag_tmp', 'Incendio'), SetVariable('gg_burn_need', True)
            else:
                timer .5 action SetScreenVariable('enemy_mag_tmp', 'Incendio')

    else:
        timer .5 action SetScreenVariable('enemy_mag_tmp', 'Combat Bolt')
    if enemy_mag:
        timer 1 action Return(enemy_mag_tmp)

init 200:
    image mn_a = LiveComposite(
    (190, 200),
    (0, 0),    'mini_games/duels/mn_a.png',
    (37, 170), Text('Aggressive', size = 20, font = 'fonts/h_font.ttf'),
    )


    image mn_a_m = LiveComposite(
    (190, 200),
    (0, 0),    im.MatrixColor('mini_games/duels/mn_a.png', im.matrix.brightness(.3)),
    (37, 170), Text('Aggressive', size = 20, font = 'fonts/h_font.ttf'),
    )

    image mn_d = LiveComposite(
    (190, 200),
    (0, 0),    'mini_games/duels/mn_d.png',
    (40, 170), Text('Defensive', size = 20, font = 'fonts/h_font.ttf'),
    )


    image mn_d_m = LiveComposite(
    (190, 200),
    (0, 0),    im.MatrixColor('mini_games/duels/mn_d.png', im.matrix.brightness(.3)),
    (40, 170), Text('Defensive', size = 20, font = 'fonts/h_font.ttf'),
    )


    image mn_s = LiveComposite(
    (190, 200),
    (0, 0),    'mini_games/duels/mn_s.png',
    (55, 170), Text('Sneaky', size = 20, font = 'fonts/h_font.ttf'),
    )

    image mn_s_m = LiveComposite(
    (190, 200),
    (0, 0),    im.MatrixColor('mini_games/duels/mn_s.png', im.matrix.brightness(.3)),
    (55, 170), Text('Sneaky', size = 20, font = 'fonts/h_font.ttf'),
    )



screen choose_your_stance_screen():
    default attack_now       = False


    default attack_now_up    = False
    default can_hide         = False    
    default potion_use       = False
    key "rollback" action NullAction()
    default c_colors = {
    'win' : '#FFE2B6',
    'lose': '#FF8F77',
    'draw': '#96D9FF',
    }
    default spell_now = 'incendio'#'combat_bolt'
    if   spell_now == 'combat_bolt':
        default attack_now_timer = 118
    elif spell_now == 'incendio':
        default attack_now_timer = 422
    viewport:
        ymaximum 765
        xmaximum 1150
        image '#0000'
        if attack_now:
            image 'mini_games/duels/new/signs/duel_bg_'+spell_now+'_0.png' xalign .5 yalign .5
        # hbox:
        #     text str(attack_now_timer) size 40
        #     text str(can_hide)         size 40
        #     text str(attack_now)       size 40
        #     xalign .5 
        xalign .5 yalign .4
        if attack_now:
            
            if spell_now == 'combat_bolt':
                viewport:
                    xmaximum 1150
                    ymaximum 765
                    image '#0000'
                    image Crop((0, 0, 1147, attack_now_timer), Transform('mini_games/duels/new/signs/duel_bg_'+spell_now+'_1.png',yzoom =-1))yzoom -1 yalign 1.0
            
            
            elif spell_now == 'incendio':
                viewport:
                    xmaximum 1150
                    ymaximum 765
                    image '#0000'
                    #if attack_now_timer   < 560:
                    image Crop((0,   0, attack_now_timer, 765), 'mini_games/duels/new/signs/duel_bg_'+spell_now+'_1_0.png')  yalign 1.0
                    #elif attack_now_timer < 720:
                    image Crop((560, 0,       attack_now_timer-560, 765), 'mini_games/duels/new/signs/duel_bg_'+spell_now+'_1_1.png')  yalign 1.0 xpos 560
                    #else:
                    viewport:
                        xmaximum 700
                        ymaximum 765
                        image '#0000'
                        image Crop((444, 0,       attack_now_timer-720, 765), Transform('mini_games/duels/new/signs/duel_bg_'+spell_now+'_1_2.png',xzoom = -1)) xzoom -1 yalign 1.0 xalign 1.0 # xzoom -1
                        
            elif spell_now == 'episkey':
                viewport:
                    xmaximum 1150
                    ymaximum 765
                    image '#0000'
                    #if attack_now_timer   < 560:
                    image Crop((0,   0, 1150, attack_now_timer), 'mini_games/duels/new/signs/duel_bg_'+spell_now+'_1_0.png')  ypos 0
                    #image 'duel_bg_episkey_1_1_tmp'
                    viewport:
                        ypos -4
                        xmaximum 1150
                        ymaximum 765
                        image '#0000'
                        image Crop((0,   0, 1150, attack_now_timer-320), Transform('mini_games/duels/new/signs/duel_bg_'+spell_now+'_1_1.png', yzoom = -1)) yzoom -1 yalign 1.0 
                    viewport:
                        xpos -4
                        xmaximum 1150
                        ymaximum 765
                        image '#0000'
                        #attack_now-385
                        image Crop((0,   0, attack_now_timer-400, 765), Transform('mini_games/duels/new/signs/duel_bg_'+spell_now+'_1_2.png', xzoom = -1)) xzoom -1 xalign 1.0 
                    
                    #elif attack_now_timer < 720:
                   # image Crop((560, 0,       attack_now_timer-560, 765), 'mini_games/duels/new/signs/duel_bg_'+spell_now+'_1_1.png')  yalign 1.0 xpos 560
                    #else:
                    #viewport:
                       # xmaximum 700
                     #   ymaximum 765
                      #  image '#0000'
                       # image Crop((444, 0,       attack_now_timer-720, 765), Transform('mini_games/duels/new/signs/duel_bg_'+spell_now+'_1_2.png',xzoom = -1)) xzoom -1 yalign 1.0 xalign 1.0 # xzoom -1
                        

            elif spell_now == 'rictusempra':
                viewport:
                    xmaximum 1150
                    ymaximum 765
                    image '#0000'
                    ypos  -3
                    #if attack_now_timer   < 560:
                    image Crop((0,   0, attack_now_timer, 765), Transform('mini_games/duels/new/signs/duel_bg_'+spell_now+'_1_0.png',yzoom =-1))yzoom -1 yalign 1.0
                    #elif attack_now_timer < 720:
                    viewport:
                        xpos     70
                        ypos     3
                        xmaximum 860
                        ymaximum 765
                        image '#0000'
                        image Crop(
                        
                        (220, 0, attack_now_timer-780, 765), 

                        Transform('mini_games/duels/new/signs/duel_bg_'+spell_now+'_1_1.png', xzoom =-1)) xzoom -1 xalign 1.0 yalign 1.0 #xpos 730


                    viewport:
                        xpos     443
                        ypos     362
                        
                        xmaximum 96

                        ymaximum 113
                        
                        image '#0000'
                        #image 'mini_games/duels/new/signs/duel_bg_'+spell_now+'_1_2.png'
                        image Crop(
                        
                        (
                        0, 
                        0,
                        96,  
                        attack_now_timer-1280,
                        ), 

                        Transform('mini_games/duels/new/signs/duel_bg_'+spell_now+'_1_2.png', yzoom =-1)) yzoom -1 xpos 0 ypos 0 yalign 1.0  #xpos 730


                    #else:
                        

            

            if not can_hide:
                imagebutton:
                    idle  'mini_games/duels/new/duels_stop_button.png'
                    hover im.MatrixColor('mini_games/duels/new/duels_stop_button.png', im.matrix.brightness(.3))
                    focus_mask None
                    xalign .5
                    yalign .9
                    if spell_now == 'episkey':
                        action [
                        SetVariable('duel_damage', int(spells_up['Episkey']+((float(attack_now_timer)/1100.0)*100.0))),
                        SetVariable('duel_damage_name', 'Episkey'),
                        Function(spells_up_tmp_up, 'Episkey', .1),
                        Jump('test_duel_win')
                    ]
                    
                    #attack_now_timer < 1470
                    
                    elif spell_now == 'rictusempra':
                        action [
                        SetVariable('duel_damage', int(spells_up['Rictusempra']+((float(attack_now_timer)/1470.0)*100.0))),
                        SetVariable('duel_damage_name', 'Rictusempra'),
                        Function(spells_up_tmp_up, 'Rictusempra', .1),
                        Jump('test_duel_win')
                    ]

                    #attack_now_timer < 970
                    elif spell_now == 'incendio':
                        action [
                        SetVariable('duel_damage', int(spells_up['Incendio']+((float(attack_now_timer)/970.0)*100.0))),
                        SetVariable('duel_damage_name', 'Incendio'),
                        Function(spells_up_tmp_up, 'Incendio', .1),
                        Jump('test_duel_win')
                    ]

                    elif spell_now == 'combat_bolt':
                        action [
                        SetVariable('duel_damage', int(spells_up['Combat Bolt']+((float(attack_now_timer)/650.0)*100.0))),
                        SetVariable('duel_damage_name', 'Combat Bolt'),
                        Function(spells_up_tmp_up, 'Combat Bolt', .1),
                        Jump('test_duel_win')
                    ]

                    #Function(show_up_donw_text_duel),
                #     if True:# spell_now == 'combat_bolt':
                #         if   attack_now_timer > 500:
                #             action [
                # Function(show_up_donw_text_duel, 
                #     text_now = 'win'.upper(), 
                #     c_color = c_colors['win'], x_now = 810, y_now = 100, curs = False),
                # SetScreenVariable('can_hide','test_duel_win')
                
                # ]
                #         elif attack_now_timer > 300:
                #             action [
                # Function(show_up_donw_text_duel, 
                #     text_now = 'draw'.upper(), 
                #     c_color = c_colors['draw'], x_now = 810, y_now = 100, curs = False),
                # SetScreenVariable('can_hide','test_duel_draw')
                # ]        
                #         else:
                #             action [
                # Function(show_up_donw_text_duel, 
                #     text_now = 'lose'.upper(), 
                #     c_color = c_colors['lose'], x_now = 810, y_now = 100, curs = False),
                # SetScreenVariable('can_hide','test_duel_lose')
                # ]   
                #     elif spell_now == 'incendio':








                #         if   attack_now_timer > 500:
                #             action [
                # Function(show_up_donw_text_duel, 
                #     text_now = 'win'.upper(), 
                #     c_color = c_colors['win'], x_now = 810, y_now = 100, curs = False),
                # SetScreenVariable('can_hide','test_duel_win')
                
                # ]
                #         elif attack_now_timer > 300:
                #             action [
                # Function(show_up_donw_text_duel, 
                #     text_now = 'draw'.upper(), 
                #     c_color = c_colors['draw'], x_now = 810, y_now = 100, curs = False),
                # SetScreenVariable('can_hide','test_duel_draw')
                # ]        
                #         else:
                #             action [
                # Function(show_up_donw_text_duel, 
                #     text_now = 'lose'.upper(), 
                #     c_color = c_colors['lose'], x_now = 810, y_now = 100, curs = False),
                # SetScreenVariable('can_hide','test_duel_lose')
                # ]   













        # if can_hide:
        #     timer 1.5 action Hide('choose_your_stance_screen', transition = Dissolve(.5)), Jump(can_hide)


        #text str(attack_now_timer) xalign .5
        #text str(attack_now_up)    xalign .5 ypos 20
        #761
        
        if attack_now and can_hide is False:
            if   spell_now == 'combat_bolt':
                # if attack_now_up:
                #     if attack_now_timer > 120:
                #         timer .01 repeat True action [SetScreenVariable('attack_now_timer', attack_now_timer-10)]
                #     #else:
                #     #    timer .01 repeat True action [SetScreenVariable('attack_now_up', False)]




                if attack_now_timer < 650:
                    timer .01 repeat True action [SetScreenVariable('attack_now_timer', attack_now_timer+10)]

                else:
                    timer .01 repeat True action [SetScreenVariable('attack_now_timer', 120)]












            elif spell_now == 'incendio':
                #text str('!!!!!!!!!!!!!')
                # if attack_now_up:
                #     if attack_now_timer > 415:
                #         timer .01 repeat True action [SetScreenVariable('attack_now_timer', attack_now_timer-10)]
                #     else:
                #         timer .25 repeat True action [SetScreenVariable('attack_now_up', False)]




               # else:
                if attack_now_timer < 970:
                    timer .01 repeat True action [SetScreenVariable('attack_now_timer', attack_now_timer+10)]

                else:
                    timer .25 repeat True action [SetScreenVariable('attack_now_timer', 415)]





            elif spell_now == 'rictusempra':
                #text str('!!!!!!!!!!!!!')
                # if attack_now_up:
                #     if attack_now_timer > 245:
                #         timer .01 repeat True action [SetScreenVariable('attack_now_timer', attack_now_timer-10)]
                #     else:
                #         timer .25 repeat True action [SetScreenVariable('attack_now_up', False)]




                #else:
                if attack_now_timer < 1470:#1353
                    timer .01 repeat True action [SetScreenVariable('attack_now_timer', attack_now_timer+20)]

                else:
                    timer .25 repeat True action [SetScreenVariable('attack_now_timer', 245)]


            elif spell_now == 'episkey':
                #text str('!!!!!!!!!!!!!')
                # if attack_now_up:
                #     if attack_now_timer > 180:
                #         #pass
                #         timer .01 repeat True action [SetScreenVariable('attack_now_timer', attack_now_timer-10)]
                #     else:
                #         timer .25 repeat True action [SetScreenVariable('attack_now_up', False)]




               # else:
                if attack_now_timer < 1100:#1353
                    timer .01 repeat True action [SetScreenVariable('attack_now_timer', attack_now_timer+10)]

                else:
                    timer .25 repeat True action [SetScreenVariable('attack_now_timer', 180)]






    if not attack_now:
        viewport:
            xalign .5
            yalign .95
            xmaximum 1230
            ymaximum 115
            image "#fff0"
            image 'duels_spells_and_poitons'
            imagebutton: 
                idle      'mini_games/duels/new/combat_ball_icon.png'
                hover     im.MatrixColor('mini_games/duels/new/combat_ball_icon.png', im.matrix.brightness(.3))
                
                hovered   Function(show_up_donw_text, text_now = "Combat Bolt", x_now = 550, y_now = 920)
                unhovered Hide('text_animation_up_screen')
                action    [
                Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_game_click.mp3'), 
                SetVariable('duel_cooldown', False),
                Hide('text_animation_up_screen'), 
                SetScreenVariable('attack_now', True),
                SetScreenVariable('spell_now', 'combat_bolt'),
                SetScreenVariable('attack_now_timer', 118),
                

                ]
                xalign .2   
                ypos    3

            imagebutton: 
                unhovered Hide('text_animation_up_screen')
                if not hasattr(store, 'has_incendio'):
                    idle      Transform('mini_games/duels/new/duels_locked_0.png', alpha = .5)
                    hover     Transform(im.MatrixColor('mini_games/duels/new/duels_locked_0.png', im.matrix.brightness(.3)), alpha = .5)
                    hovered   Function(show_up_donw_text, text_now = 'Locked', x_now = 640, y_now = 920)
                    #ypos 5 xpos -5
                    action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_game_click.mp3')
                
                
                elif duel_cooldown:
                    idle      Transform('mini_games/duels/new/incendio_icon.png', alpha = .5)
                    hover     Transform(im.MatrixColor('mini_games/duels/new/incendio_icon.png', im.matrix.brightness(.3)), alpha = .5)
                    hovered   Function(show_up_donw_text, text_now = 'Cooldown: 1 Round', x_now = 640, y_now = 920)
                    action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_game_click.mp3')
                
                else:
                    idle      'mini_games/duels/new/incendio_icon.png'
                    hover     im.MatrixColor('mini_games/duels/new/incendio_icon.png', im.matrix.brightness(.3))
                    hovered   Function(show_up_donw_text, text_now = 'Incendio', x_now = 640, y_now = 920)
                    action    [
                Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_game_click.mp3'), 
                SetVariable('duel_cooldown', True),
                Hide('text_animation_up_screen'), 
                SetScreenVariable('attack_now', True),
                SetScreenVariable('spell_now', 'incendio'),
                SetScreenVariable('attack_now_timer', 415),
                
                ]
                xalign .285   
                ypos    3

            imagebutton: 
                unhovered Hide('text_animation_up_screen')
                if not hasattr(store, 'has_rictusempra'):
                    idle      Transform('mini_games/duels/new/duels_locked_0.png', alpha = .5)
                    hover     Transform(im.MatrixColor('mini_games/duels/new/duels_locked_0.png', im.matrix.brightness(.3)), alpha = .5)
                    hovered   Function(show_up_donw_text, text_now = 'Locked', x_now = 640, y_now = 920)
                    #ypos 5 xpos -5
                    action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_game_click.mp3')
                
                elif duel_cooldown:
                    idle      Transform('mini_games/duels/new/rictusempra_icon.png', alpha = .5)
                    hover     Transform(im.MatrixColor('mini_games/duels/new/rictusempra_icon.png', im.matrix.brightness(.3)), alpha = .5)
                    hovered   Function(show_up_donw_text, text_now = "Cooldown: 1 Round", x_now = 730, y_now = 920)
                    action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_game_click.mp3')
                
                else:
                    idle      'mini_games/duels/new/rictusempra_icon.png'
                    hover     im.MatrixColor('mini_games/duels/new/rictusempra_icon.png', im.matrix.brightness(.3))
                    hovered   Function(show_up_donw_text, text_now = "Rictusempra", x_now = 730, y_now = 920)
                    action    [
                Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_game_click.mp3'),
                SetVariable('duel_cooldown', True),
                Hide('text_animation_up_screen'), 
                SetScreenVariable('attack_now', True),
                SetScreenVariable('spell_now', 'rictusempra'),
                SetScreenVariable('attack_now_timer', 250),
                
                ]
                xalign .365   
                ypos    3

            #image 'duels_locked' xalign .445 ypos 7
            imagebutton: 
                unhovered Hide('text_animation_up_screen')
                if not hasattr(store, 'has_episkey'):
                    idle      Transform('mini_games/duels/new/duels_locked_0.png', alpha = .5)
                    hover     Transform(im.MatrixColor('mini_games/duels/new/duels_locked_0.png', im.matrix.brightness(.3)), alpha = .5)
                    hovered   Function(show_up_donw_text, text_now = 'Locked', x_now = 640, y_now = 920)
                    #ypos 5 xpos -5
                    action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_game_click.mp3')
                
                elif duel_cooldown:
                    idle      Transform('mini_games/duels/new/episkey_icon.png', alpha = .5)
                    hover     Transform(im.MatrixColor('mini_games/duels/new/episkey_icon.png', im.matrix.brightness(.3)), alpha = .5)
                    hovered   Function(show_up_donw_text, text_now = "Cooldown: 1 Round", x_now = 820, y_now = 920)
                    action Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_game_click.mp3')
                else:
                    idle      'mini_games/duels/new/episkey_icon.png'
                    hover     im.MatrixColor('mini_games/duels/new/episkey_icon.png', im.matrix.brightness(.3))
                    hovered   Function(show_up_donw_text, text_now = "Episkey", x_now = 820, y_now = 920)
                    action    [
                Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_game_click.mp3'),
                SetVariable('duel_cooldown', True),
                Hide('text_animation_up_screen'), 
                SetScreenVariable('attack_now', True),
                SetScreenVariable('spell_now', 'episkey'),
                SetScreenVariable('attack_now_timer', 180),
                
                ]
                xalign .445   
                ypos    3







            #image 'duels_locked'     xalign .285 ypos 12
            #image 'duels_locked'     xalign .365 ypos 12



            



            $ ptmps = potions['Lesser Heal']
            viewport:
                xmaximum 132
                ymaximum 115
                xalign .55 yalign .5
                if ptmps:
                    imagebutton:
                        idle 'mini_games/duels/new/potion_button_duels.png'
                        hover im.MatrixColor('mini_games/duels/new/potion_button_duels.png', im.matrix.brightness(.3))
                        focus_mask None
                        hovered   Function(show_up_donw_text, text_now = "Lesser Heal", x_now = 930, y_now = 920)
                        unhovered Hide('text_animation_up_screen')
                        if potion_use:
                            action NullAction()
                        else:
                            action  Hide('text_animation_up_screen'), SetScreenVariable('potion_use', True), SetVariable('potion_now', True), Function(set_potion, potion = 'Lesser Heal')
                        xalign .5 yalign .5
                    image 'lesser_heal_duels' xalign .5 yalign .5
                    text str(ptmps) size 25 font 'fonts/h_font.ttf' xalign .7 yalign .9 outlines [(1, "#000", 0, 0)]
                if potion_use:
                    image im.Grayscale('mini_games/duels/new/potion_button_duels.png') xalign .5 yalign .5
                    add im.Grayscale('mini_games/duels/new/lesser_heal_duels.png') xalign .5 yalign .5

    # viewport:
    #     xmaximum 266
    #     ymaximum 120
    #     imagebutton:
    #         idle "mini_games/caffe/button_for_left_cafe.png"
    #         hover im.MatrixColor("mini_games/caffe/button_for_left_cafe.png", im.matrix.brightness(.3))
    #         action [

    #         Hide('text_animation_up_screen'),
    # Hide('text_animation_up_screen_duel'),
    # Hide('test_duel_choice_mag'),
    # Hide('main_interface'),
    
    # Hide('test_duel_game_win_screen'),
    # SetVariable('enemy_stamina', -5),
    #         Jump('end_duel'),]
    #         xalign .5 yalign .5
    #     text 'Skip' size 19 color '#fff' font 'fonts/h_font.ttf' xalign .55 yalign .5
    #     xpos 1400
    #     ypos 750

    # viewport:

    #     xmaximum 600
    #     ymaximum 450
    #     add '#fff0'
    #     add 'arrows' xpos 147 ypos 175

    #     at choose_your_stance_transform(x_start = 2200, shift_x = 1250, yp = 300)
    #     imagebutton:
    #         xpos 50
    #         ypos 240
    #         idle 'mn_a'
    #         hover 'mn_a_m'
    #         if gg_stan:
    #             action Function(test_duel_choice_mag_def, imn = 'mn_p', xp = 1450+50, yp = 300+240)
    #         else:
    #             action Function(test_duel_choice_mag_def, imn = 'mn_a', xp = 1450+50, yp = 300+240)
    #         at AlphaEffect

    #     imagebutton:
    #         xpos 300
    #         ypos 240
    #         idle 'mn_d'
    #         hover 'mn_d_m'
    #         if gg_stan:
    #             action Function(test_duel_choice_mag_def, imn = 'mn_p', xp = 1450+325, yp = 300+240)
    #         else:
    #             action Function(test_duel_choice_mag_def, imn = 'mn_d', xp = 1450+325, yp = 300+240)
    #         at AlphaEffect

    #     imagebutton:
    #         xpos 175
    #         ypos 35
    #         idle 'mn_s'
    #         hover 'mn_s_m'
    #         if gg_stan:
    #             action Function(test_duel_choice_mag_def, imn = 'mn_p', xp = 1450+175, yp = 300+35)
    #         else:
    #             action Function(test_duel_choice_mag_def, imn = 'mn_s', xp = 1450+175, yp = 300+35)
    #         at AlphaEffect
screen test_duel_game_start_screen():

    key "rollback" action NullAction()
    viewport:
        add '#0000'

        xmaximum 1920
        ymaximum 1080
        add 'tmp_avatar_1'
        add 'tmp_avatar_2' xalign 1.0
        viewport:
            xmaximum 212
            ymaximum 33
            xpos 1567-3
            ypos 79
            image '#fff0'
            image Crop((0, 0, int(210*float(100.0/(500.0/float(gg_stamina+1)))/100), 32), 'mini_games/duels/new/duels_hp_bar_enemy.png') xalign 1.0
        vbox:
            xpos 1565-3
            ypos 79

            image Crop((0, 0, int(210*float(100.0/(500.0/float(gg_stamina+1)))/100), 32), '#0000')
            hbox ypos 5 xpos 10:
                if gg_burn:

                    add 'mini_games/duels/fire.png' ypos 5 zoom .6



                if gg_stoneskin:

                    add 'mini_games/duels/stoneskin.png' ypos 5 zoom .6



                if gg_inspiration:

                    add 'images/emoji/gg_inspiration.png' ypos 5 zoom .6



                if gg_stan:

                    add 'mini_games/duels/stan.png' ypos 5 zoom .6
 
                if magic_reflection:

                    add 'images/emoji/mirror.png' ypos 5 zoom .6


                if gg_heal:

                    add 'mini_games/duels/heal.png' ypos 5 zoom .6


        if stance:
            $ pass

        text  '[f_now]': 
            xpos 150 ypos 40 size 28 
            if   f_now == 'Martenden':
                color '#FFC978' 
            elif f_now == 'Adderin':
                color '#71A465'
            elif f_now == 'Crowhive':
                color '#366783'

            font 'fonts/h_font.ttf'
        image 'ch_duel_'+str(f_now).lower() ypos 40 xpos 3 zoom .5
        vbox:
            image Crop((0, 0, int(210*float(100.0/(500.0/float(enemy_stamina+1)))/100), 32), 'mini_games/duels/new/duels_hp_bar_enemy.png') 
            xpos 144 ypos 79
            hbox ypos 5:
                if enemy_burn:

                    add 'mini_games/duels/fire.png' ypos 5 zoom .6
                if enemy_stan:

                    add 'mini_games/duels/stan.png' ypos 5 zoom .6


                if enemy_heal:

                    add 'mini_games/duels/heal.png' ypos 5 zoom .6


        # vbox:
        #     xpos 155
        #     ypos 50
        #     viewport:
        #         xmaximum 405
        #         ymaximum 65
        #         add 'mini_games/duels/heal_bar_bg.png'
        #         hbox:
        #             if enemy_stamina>0:
        #                 add 'heal_bar_l'
        #                 add Crop((0, 0, int(312*float(100.0/(500.0/float(enemy_stamina)))/100), 33), 'mini_games/duels/heal_bar.png')
        #                 add Transform('mini_games/duels/heal_bar_l.png', xzoom = -1)
        #             else:
        #                 add Crop((0, 0, int(312*float(100.0/(500.0/1.0))/100), 33), 'mini_games/duels/heal_bar.png')

        #             xpos 16 ypos 15




        #text 'Leonheart' xpos 1550 ypos 5 size 39 font 'fonts/h_font.ttf'
        # vbox:
        #     xpos 1362
        #     ypos 50
        #     viewport:
        #         xmaximum 405
        #         ymaximum 65
        #         add 'mini_games/duels/heal_bar_bg.png' xzoom -1
        #         hbox:
        #             if gg_stamina>0:
        #                 add 'heal_bar_l'
        #                 add Crop((0, 0, int(312*float(100.0/(500.0/float(gg_stamina)))/100), 33), 'mini_games/duels/heal_bar.png')
        #                 add Transform('mini_games/duels/heal_bar_l.png', xzoom = -1)
        #             else:
        #                 add Crop((0, 0, int(312*float(100.0/(500.0/1.0))/100), 33), 'mini_games/duels/heal_bar.png')

        #             xpos 386 ypos 15
        #             xalign 1.0








        #     hbox ypos 5 xpos 50:
        #         if gg_burn:

        #             add 'mini_games/duels/fire.png' ypos 5



        #         if gg_stoneskin:

        #             add 'mini_games/duels/stoneskin.png' ypos 5



        #         if gg_inspiration:

        #             add 'images/emoji/gg_inspiration.png' ypos 5



        #         if gg_stan:

        #             add 'mini_games/duels/stan.png' ypos 5

        #         if magic_reflection:

        #             add 'images/emoji/mirror.png' ypos 5


        #         if gg_heal:

        #             add 'mini_games/duels/heal.png' ypos 5


        # if stance:
        #     $ pass








    if stance:
        timer .1 action Show('choose_your_stance_screen')
    else:
        timer .1 action Hide('choose_your_stance_screen')




transform test_duel_choice_mag_transform(xp, yp, xp_2=1000, yp_2=600, xp_3=1000, yp_3=600, xp_4=890, yp_4=550, pp=.2):

    xpos xp
    ypos yp

    linear .5 xpos xp_2 ypos yp_2

    pause .2

    linear .5 xpos xp_3 ypos yp_3

    pause pp

    linear .2 xpos xp_4 ypos yp_4

transform duels_light:

    alpha 0.0
    pause 1.5
    linear 0.5 alpha 1.0

screen test_duel_choice_mag(imn, xp, yp):

    key "rollback" action NullAction()
    $ check_win      = check_winner()
    default can_hide = False







































    if check_win == 'win':



        add imn at test_duel_choice_mag_transform(xp, yp, yp_3 = 500)
        add 'mn_'+ enemy_mag at test_duel_choice_mag_transform(335, 500, xp_2 = 800, yp_2 = 600, xp_3 = 800, yp_3 = 600, xp_4 = -2000, yp_4 = 2000, pp = .3)

    elif check_win == 'lose':
        add imn at test_duel_choice_mag_transform(xp, yp, xp_4 = 2000, yp_4 = 2000, pp = .3)
        add 'mn_'+ enemy_mag at test_duel_choice_mag_transform(335, 500, xp_2 = 800, yp_2 = 600, xp_3 = 800, yp_3 = 500)

    else:

        add imn at test_duel_choice_mag_transform(xp, yp, xp_3 = 1050+30, yp_3 = 600, xp_4 = 1050+30, yp_4 = 600,)
        add 'mn_'+ enemy_mag at test_duel_choice_mag_transform(335, 500, xp_2 = 800, yp_2 = 600, xp_3 = 650+50, yp_3 = 600, xp_4 = 650+50, yp_4 = 600)

    imagebutton:
        idle '#0000'
        hover '#0000'
        action NullAction()
    default c_colors = {
    'WIN' : '#FFE2B6',
    'LOSE': '#FF8F77',
    'DRAW': '#96D9FF',
    }
    timer 1.5 action SetScreenVariable('can_hide', True), Function(show_up_donw_text_duel, text_now = check_win.upper(), c_color = c_colors[check_win.upper()], x_now = 810, y_now = 450, curs = False)
    if can_hide:
        imagebutton:
            idle '#0000'
            hover '#0000'

            action Jump('test_duel_'+check_win)


screen duel_pass_screen:

    key "rollback" action NullAction()
    $ pass


screen lose_win_duel_screen(ttxt='1'):

    key "rollback" action NullAction()

    add 'caffe_menu_bg' xalign .5 yalign .5



    viewport:
        at hide_my_choice
        xmaximum 1920
        ymaximum 1080

        add '#0000'
        xalign .5 yalign .5
        viewport:
            xmaximum 685
            ymaximum 420
            xalign .5
            yalign .51
            add '#fff0'
            viewport:
                xalign .5 yalign .5
                xmaximum 400
                ymaximum 300
                add '#0000'
                text unicode(ttxt) xalign .5 yalign .5

            textbutton 'Ok' action Return() xalign .5 yalign .985

screen ch_duels_screen:
    imagebutton:
        idle  '#000a'
        hover '#000a'
        action Return('Not now')
    image 'choice_home_duels_bg_0' xalign .5 yalign .5
    viewport:
        ymaximum 762
        xmaximum 1020
        image 'choice_home_duels_bg'
        xalign .5 yalign .5
        viewport:
            xmaximum 100
            ymaximum 60
            image '#0000'
            xpos  710 
            ypos  122
            vbox:

                text   str(homes['Leonheart']['now']) font 'fonts/h_font.ttf' size 30 color '#E04615' xalign .5 
                #image  Text('points', color = '#658DA4', font = 'fonts/h_font.ttf', size = 17) alpha .9 xalign .5 ypos -10
                xalign .5 yalign .5
        $ ptmps = potions['Lesser Heal']
        if ptmps:
            viewport:
                xmaximum 100
                ymaximum 80
                image    '#0000'
                xpos     635 
                ypos     650
                image 'mini_games/duels/new/lesser_heal_duels.png'
            
        viewport:
            xmaximum 555
            ymaximum 213
            imagebutton: 
                idle   '#0000'
                hover  '#fff7'
                action Return('Martenden')
            xpos 80
            ypos 90
            viewport:
                xmaximum 100
                ymaximum 60
                image '#0000'
                xpos  360 
                ypos  45
                vbox:

                    text   str(homes['Martenden']['now']) font 'fonts/h_font.ttf' size 30 color '#835636' xalign .5 
                    image  Text('points', color = '#A47B65', font = 'fonts/h_font.ttf', size = 17) alpha .9 xalign .5 ypos -10
                    xalign .5 yalign .5

        viewport:
            xmaximum 555
            ymaximum 215
            imagebutton: 
                idle   '#0000'
                hover  '#fff7'
                action Return('Adderin')
            xpos 80
            ypos 90+220
            viewport:
                xmaximum 100
                ymaximum 60
                image '#0000'
                xpos  360 
                ypos  48
                vbox:

                    text   str(homes['Adderin']['now']) font 'fonts/h_font.ttf' size 30 color '#368343' xalign .5 
                    image  Text('points', color = '#71A465', font = 'fonts/h_font.ttf', size = 17) alpha .9 xalign .5 ypos -10
                    xalign .5 yalign .5



        viewport:
            xmaximum 555
            ymaximum 215
            imagebutton: 
                idle   '#0000'
                hover  '#fff7'
                action Return('Crowhive')
            viewport:
                xmaximum 100
                ymaximum 60
                image '#0000'
                xpos  360 
                ypos  48
                vbox:

                    text   str(homes['Crowhive']['now']) font 'fonts/h_font.ttf' size 30 color '#366783' xalign .5 
                    image  Text('points', color = '#658DA4', font = 'fonts/h_font.ttf', size = 17) alpha .9 xalign .5 ypos -10
                    xalign .5 yalign .5

            xpos 80
            ypos 90+220+220



    # viewport:
    #     xalign .5
    #     yalign .5
    #     xmaximum 1225
    #     ymaximum 425
    #     add 'ch_duel_bg_0' xalign .5 yalign .5
    #     add 'ch_duel_bg_0' xalign .5 yalign .5
    #     add 'ch_duel_bg_1' xalign .5 yalign .52
    #     hbox xalign .5 yalign .5:
    #         for i in ['adderin', 'crowhive', 'martenden']:
    #             viewport:
    #                 xmaximum 266
    #                 ymaximum 120
    #                 imagebutton:
    #                     idle 'mini_games/duels/ch_duel_' + i + '.png'
    #                     hover im.MatrixColor('mini_games/duels/ch_duel_' + i + '.png', im.matrix.brightness(.3))
    #                     action Return(i.title())
    #                     xalign .5 yalign .5
    #                 text i.title() size 19 color '#fff' font 'fonts/h_font.ttf' xalign .65 yalign .56



    # text 'Chose your apponent’s house.' size 23 color '#fff' font 'fonts/h_font.ttf' xalign .5 yalign .4
    # viewport:
    #     xmaximum 140
    #     ymaximum 60
    #     add '#0000'
    #     imagebutton:
    #         idle "mini_games/caffe/button_for_left_cafe.png"
    #         hover im.MatrixColor("mini_games/caffe/button_for_left_cafe.png", im.matrix.brightness(.3))
    #         action Return('Not now')
    #     text 'Leave' font 'fonts/h_font.ttf' xalign .65 yalign .5 size 17
    #     xalign .5 yalign .6
label test_duel_draw:
    hide screen test_duel_choice_mag
    hide screen text_animation_up_screen
    hide screen text_animation_up_screen_duel
    show screen test_duel_game_start_screen

    with Dissolve(.5)
    $ enemy_stamina = min(500, enemy_stamina+25)
    $ gg_stamina    = min(500, gg_stamina+25)
    $ Hide('text_animation')()
    $ Hide('text_animation_2')()
    $ Show(
           'text_animation', 
           text_now = str(+25),
           x_now = 250, 
           y_now = 30)()
    $ Show(
           'text_animation_2', 
           text_now = str(+25),
            x_now = 1610, 
            y_now = 30)()



    $ renpy.pause(1, hard = True)
    jump duel_next_raund

label test_duel_game_menu:




    hide screen text_animation_up_screen_duel
    hide screen text_animation_up_screen
    hide screen test_duel_choice_mag
    hide screen show_hide_locations_2
    hide screen show_hide_locations


    with Dissolve(.5)
    $ addr  = 'Adderin '   + str(homes['Adderin']['now'])
    $ crwh  = 'Crowhive '  + str(homes['Crowhive']['now'])
    $ mrtn  = 'Martenden ' + str(homes['Martenden']['now'])
    $ f_now = ''
    $ duel_cooldown = True
    $ spells_up_tmp = {
    'Combat Bolt' : 0,
    'Incendio'    : 0,
    'Rictusempra' : 0,
    'Episkey'     : 0,
    }
    $ f_now = renpy.call_screen('ch_duels_screen')
    if f_now == 'Not now':
        hide expression '#0000'
        hide screen tmp_tmp_tmp_pass_screen
        with Dissolve(.5)

        jump main_interface_label
    $ del addr
    $ del crwh
    $ del mrtn
    hide screen text_animation_up_screen_3
    hide screen main_interface
    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/3. Mystery.mp3' fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/3. Mystery.mp3' fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/3. Mystery.mp3' fadein 2



    hide screen tmp_tmp_tmp_pass_screen
    hide screen show_hide_locations_2
    hide screen show_hide_locations
    scene expression '#000'

    with Dissolve(.5)
    jump test_duel_game_start


label test_duel_game_start:
    $ gg_stamina       = 500
    $ enemy_stamina    = 500

    $ potion_now       = False

    $ combat_ball    = False


    $ enemy_burn       = False
    $ gg_burn          = False
    $ gg_stoneskin     = False
    $ gg_inspiration   = False
    $ magic_reflection = False
    $ enemy_stan       = False
    $ gg_stan          = False
    $ gg_heal          = False
    $ enemy_heal       = False
    $ stance           = True

    $ gg_stan_need     = False
    $ enemy_burn_need  = False
    $ gg_burn_need     = False
    $ gg_heal_need     = False
    $ enemy_heal_need  = False

    scene sc i_dueling_anim_1_a with Dissolve(.5)
    "Jacob" "I'm glad to welcome the participants of the magic duel!"

    "Jacob" "Welcome to the Cordale arena!"
    "Jacob" "Today two of our students will perform in a practice battle."
    scene sc i_dueling_anim_1 with Dissolve(.5)
    $ renpy.pause(3, hard = True)
    "Jacob" "Student to my right represents the house [f_now]!"

    "Jacob" "Student to my left represents the house Leonheart!"

    "Jacob" "Duelists, I expect a fair fight from both of you. Good luck!"
    "Jacob" "And may the strongest win!"
    scene sc i_dueling_anim_2 with Dissolve(.2)
    $ renpy.pause(5.96, hard = True)
    "[Name]" "{i}(She looks serious. I bet she won't hold back.){/i}"

    "[Name]" "{i}(Neither should I!){/i}"

    "Unknown Girl" "I'm ready."
    $ unknown_girl_say = renpy.random.choice([
    "Get ready to lose your house points, loser!",
    "You're in a lot of trouble!",
    "I can't guarantee you'll survive our battle.",
    "Are you challenging me? Unwise!",
    "Let's get this over with, I'm bored already!",
    "Hey, try to go easy on me, okay?",
    ])
    show sc i_dueling_1_15 with my_dissolve
    "Unknown Girl" "[unknown_girl_say]"
    scene sc i_dueling_1_2

    show expression '#0004'
    with Dissolve(.5)

label test_duel_game:
    $ battle_tutorial = True
    if not mp.tutorial['DUELING ARENA']:
        $ tutorial_bb = 0
        call screen tutorial_screen(what_tutor = 'DUELING ARENA')
        #show image '#000' with Dissolve(.5)
    if not renpy.get_screen('test_duel_game_start_screen'):
        call screen test_duel_game_start_screen
    elif True:
        call screen duel_pass_screen

label test_duel_lose:






    hide screen text_animation_up_screen
    hide screen text_animation_up_screen_duel
    hide screen test_duel_choice_mag
    hide screen main_interface
    
    show screen test_duel_game_start_screen
    $ stance = False
    $ Hide('text_animation')()
    $ Hide('text_animation_2')()
    #with Dissolve(.5)
    $ enemy_attack_magick = 0 #renpy.call_screen('enemy_choose_magick')
    $ xlttsts = renpy.random.randint(1, 3)
    if xlttsts == 1:
        if renpy.random.randint(1, 5) in [1, 2, 3]:
            if renpy.random.randint(1, 5) in [1, 2, 3]:
                if hasattr(store, 'magic_reflection') and magic_reflection:
                    $ SetVariable('enemy_attack_magick', 'Rictusempra')() 
                    $ SetVariable('enemy_stan', True)()
                else:
                    $ SetVariable('enemy_attack_magick', 'Rictusempra')() 
                    $ SetVariable('gg_stan_need', True)()
            else:
                $ SetVariable('enemy_attack_magick', 'Rictusempra')()
        else:
            $ SetVariable('enemy_attack_magick', 'Combat Bolt')()

    elif xlttsts == 2:
        if renpy.random.randint(1, 5) in [1, 2, 3]:
            if renpy.random.randint(1, 5) in [1, 2, 3]:
                if hasattr(store, 'magic_reflection') and magic_reflection:
                    $ SetVariable('enemy_attack_magick', 'Incendio')() 
                    $ SetVariable('gg_burn_need', True)()
                else:
                    $ SetVariable('enemy_attack_magick', 'Incendio')() 
                    $ SetVariable('gg_burn_need', True)()
            else:
                $ SetVariable('enemy_attack_magick', 'Incendio')()

    else:
        $ SetVariable('enemy_attack_magick', 'Combat Bolt')()











    if enemy_attack_magick == 'Incendio':




        scene sc i_dueling_1_11 with Dissolve(.5)
    elif enemy_attack_magick == 'Rictusempra':
        scene sc i_dueling_1_10R with Dissolve(.5)
    elif enemy_attack_magick == 'Episkey':
        scene sc i_dueling_1_12 with Dissolve(.5)
    elif True:
        scene sc i_dueling_1_10 with Dissolve(.5)
    if enemy_attack_magick != 0:
        "Unknown Girl" "{b}[enemy_attack_magick]!{/b}"
    elif True:


        "Unknown Girl" "{b}Combat bolt!{/b}"


    scene expression '#fff' with Dissolve(.25)
    $ renpy.pause(.25)
    if enemy_burn_need:
        $ enemy_burn_need = False
        $ enemy_burn      = 2
    if gg_burn_need:
        $ gg_burn_need    = False
        $ gg_burn         = 2
    $ unknown_girl_say = renpy.random.choice([
    
    "You realize now that you're no match for me, right?",
    "What's the matter, was that too much?",
    "If you can't take a punch like a man, go running back to mommy!",
    "Are you still on your feet? Not for long.",

    ])

    $ rnd_attack = renpy.random.randint(30, 100)

    if magic_reflection:
        $ magic_reflection -= 1
        $ enemy_stamina    -= rnd_attack
        $ Show(
                   'text_animation', 
                   text_now = str(-rnd_attack),
                   x_now = 250, 
                   y_now = 30)()
    elif True:
        if gg_stoneskin:
            $ gg_stamina   -= int(rnd_attack*.75)
            $ gg_stoneskin -= 1
            $ Show(
                'text_animation', 
                    text_now = str(-int(rnd_attack*.75)),
                    x_now = 1610, 
                    y_now = 30)()
        elif True:
            $ gg_stamina   -= rnd_attack

            $ Show(
                'text_animation', 
                    text_now = str(-rnd_attack),
                    x_now = 1610, 
                    y_now = 30)()


    if gg_burn:
        $ renpy.pause(.5, hard = True)
        $ Hide('text_animation')()
        $ Hide('text_animation_2')()

        if gg_stoneskin:
            $ gg_stoneskin  -= 1
            $ gg_stamina -= 37
            $ Show(
                    'text_animation', 
                    text_now = str(-37),
                    x_now = 1610, 
                    y_now = 30)()
        elif True:
            $ gg_stamina -= 50
            $ Show(
                    'text_animation', 
                    text_now = str(-50),
                    x_now = 1610, 
                    y_now = 30)()
        $ gg_burn -= 1


    if enemy_burn:
        $ renpy.pause(.5, hard = True)
        $ enemy_burn -= 1
        $ Hide('text_animation')()
        $ Hide('text_animation_2')()
        if gg_inspiration:
            $ gg_inspiration -= 1
            $ enemy_stamina  -= 75
            $ Show(
                   'text_animation', 
                   text_now = str(-75),
                   x_now = 250, 
                   y_now = 30)()
        elif True:

            $ enemy_stamina -= 50

            $ Show(
                   'text_animation', 
                   text_now = str(-50),
                   x_now = 250, 
                   y_now = 30)()

    if gg_stan_need:
        $ gg_stan_need = False
        $ gg_stan      = True
    scene sc i_dueling_1_9 with Dissolve(.1)
    "Unknown Girl" "[unknown_girl_say]"


    if enemy_stamina > 0 and gg_stamina > 0:
        scene sc i_dueling_1_2 with Dissolve(.5)
    jump duel_next_raund
label test_duel_win:

    hide screen text_animation_up_screen
    hide screen text_animation_up_screen_duel
    hide screen test_duel_choice_mag
    hide screen main_interface
    show screen test_duel_game_start_screen
    $ go_lose = True
    $ stance = False
    with Dissolve(.5)
    #call screen test_duel_game_win_screen
    $ throw_vial()
    if not gg_stan:
        show sc i_dueling_1_3 with Dissolve(.25)
        "[Name]" "{b}[duel_damage_name]!{/b}"
        if duel_damage_name == 'Incendio':
            if renpy.random.randint(1, 2) == 2:
                $ enemy_burn_need = True
        if duel_damage_name == 'Rictusempra':
            #'!!!!!!!!!!'
            if renpy.random.randint(1, 2) == 2:
             #   '@@@@'
                $ enemy_stan = True
            #else:
            #    '~~~'


        scene expression '#fff' with Dissolve(.25)
        $ renpy.pause(.25)
        if duel_damage_name != 'Episkey':
            $ combat_ball = False

            if gg_inspiration:
                $ gg_inspiration -= 1
                $ enemy_stamina  -= int(duel_damage)+25
                $ Show(
                   'text_animation', 
                   text_now = str(-int(duel_damage)+25),
                   x_now = 250, 
                   y_now = 30)()
            else:

                $ enemy_stamina  -= int(duel_damage)
                $ Show(
                   'text_animation', 
                   text_now = str(-int(duel_damage)),
                   x_now = 250, 
                   y_now = 30)()
        else:
            $ gg_stamina = min(500, gg_stamina+duel_damage)
            $ Show(
                   'text_animation', 
                   text_now = str(+min(500, gg_stamina+duel_damage)),
                   x_now = 1610, 
                   y_now = 30)()
            if renpy.random.randint(1, 2) == 2:
                $ gg_heal_need = True
        if enemy_stamina <= 0:
            $ gg_burn = False
        if gg_burn:
            $ renpy.pause(.5, hard = True)
            $ Hide('text_animation')()
            $ Hide('text_animation_2')()

            if gg_stoneskin:
                $ gg_stoneskin  -= 1
                $ gg_stamina -= int(duel_damage/3.0)
                $ Show(
                        'text_animation', 
                        text_now = str(int(duel_damage/3.0)),
                        x_now = 1610, 
                        y_now = 30)()
            else:
                $ gg_stamina -= int(duel_damage/2.0)
                $ Show(
                        'text_animation', 
                        text_now = str(int(duel_damage/2.0)),
                        x_now = 1610, 
                        y_now = 30)()
            $ gg_burn -= 1


        if enemy_burn:
            $ renpy.pause(.5, hard = True)
            $ enemy_burn -= 1
            $ Hide('text_animation')()
            $ Hide('text_animation_2')()
            if gg_inspiration:
                $ gg_inspiration -= 1
                $ enemy_stamina  -= int(duel_damage*3.0/4.0)
                $ Show(
                       'text_animation', 
                       text_now = str(-duel_damage*3.0/4.0),
                       x_now = 250, 
                       y_now = 30)()
            elif True:

                $ enemy_stamina -= duel_damage*3.0/4.0

                $ Show(
                       'text_animation', 
                       text_now = str(-duel_damage*3.0/4.0),
                       x_now = 250, 
                       y_now = 30)()

        if duel_damage_name == 'Episkey':
            scene sc i_dueling_1_3 with Dissolve(.1)
        

        else:
            scene sc i_dueling_1_4 with Dissolve(.1)
        
        $ renpy.pause(9999999)
    else:
        $ gg_stan = False
    if enemy_stamina > 0 and gg_stamina > 0:
        scene sc i_dueling_1_2 with Dissolve(.5)
label duel_next_raund:
    hide screen text_animation_up_screen
    hide screen text_animation_up_screen_duel
    hide screen test_duel_choice_mag
    hide screen main_interface

    hide screen test_duel_game_win_screen
    $ stance     = True
    $ potion_now = False

    if gg_heal:
        $ renpy.pause(.5, hard = True)
        $ gg_heal = False
        $ gg_stamina = min(500, gg_stamina+50)
        $ Hide('text_animation')()
        $ Hide('text_animation_2')()
        $ Show(
               'text_animation', 
               text_now = str(+50),
               x_now = 1610, 
               y_now = 30)()

label end_duel:
    if enemy_stamina <= 0:

        show expression '#0000'

        hide screen lose_win_duel_screen
        hide screen duel_pass_screen
        hide screen test_duel_choice_mag
        hide screen test_duel_game_start_screen
        hide screen choose_your_stance_screen
        hide screen enemy_choose_magick
        hide screen test_duel_game_win_screen
        hide screen text_animation_2
        hide screen text_animation
        scene expression '#000'
        with Dissolve(.7)
        $ renpy.pause(.7)
        scene sc i_dueling_1_13 with Dissolve(1)


        $ unknown_girl_say = renpy.random.choice([
     "Those were easy points for Lenoheart.",
        "I like you better when you're quiet.",
        "So appetizing. I wonder who's hiding beneath that mask?",
        "A worthy fight! I wish I knew who you were...",
        "And so shall it be with anyone I challenge!",

    ])
        '[Name]' "[unknown_girl_say]"
        scene expression '#000'
        with Dissolve(.7)
        $ renpy.pause(.7)
        scene sc i_dueling_1_14 with Dissolve(.5)
        "Jacob" "[f_now]'s duelist cannot continue the battle."
        show sc i_dueling_1_24 with my_dissolve
        "Jacob" "Victory to the House of Leonheart!"
        "Jacob" "Great job! That's all for today."
        show sc i_dueling_1_25 with my_dissolve
        "Jacob" "Go rest while I..."
        "Jacob" "...see to the loser."
        python:
            for xtrststsad in spells_up_tmp:
                spl_up = spells_up_tmp[xtrststsad]
                if spl_up:
                    spells_up[xtrststsad] += spl_up
                    ShowMessage('[xtrststsad] {color=#0F0}{b}+'+str(spl_up)+'{/color}{/b}')
                
        scene expression '#000' with Dissolve(1)


        $ renpy.pause(1, hard = True)





        $ win  = 'Leonheart'
        $ battle_tutorial = False
        $ lose = f_now
        $ change_location_2(location_now, time_now+1, plus = True)
        return


    if gg_stamina <= 0:


        show expression '#0000'

        hide screen lose_win_duel_screen
        hide screen duel_pass_screen
        hide screen test_duel_choice_mag
        hide screen test_duel_game_start_screen
        hide screen choose_your_stance_screen
        hide screen enemy_choose_magick
        hide screen test_duel_game_win_screen
        hide screen text_animation_2
        hide screen text_animation
        with Dissolve(.5)















        scene expression '#000' with Dissolve(1.5)

        $ win  = f_now
        $ lose = 'Leonheart'

        python:


            if homes.get(win):
                homes[win]['now']  += 3
                rtmps = 3
            ShowMessage(['images/'+win.lower()+'_mini.png', win.title()+' points {color=#0F0}{b}+'+str(rtmps)+'{/color}{/b}'])
            if homes.get(lose):
                homes[lose]['now'] -= 3
                rtmps = 3
                ShowMessage(['images/'+lose.lower()+'_mini.png', lose.title()+' points {color=#F00}{b}-'+str(rtmps)+'{/color}{/b}'])

            if hasattr(store, 'rtmps'):
                del rtmps










        $ set_points_home(13, 20, 15, 25)
        $ time_now = 4
        $ battle_tutorial = False
        $ change_location_2('leon_room_mc', time_now+1, sleep = True)

        return











    if enemy_burn_need:
        $ enemy_burn_need = False
        $ enemy_burn      = 2
    if gg_burn_need:
        $ gg_burn_need    = False
        $ gg_burn         = 2
    if gg_heal_need:
        $ gg_heal_need    = False
        $ gg_heal         = True


    if gg_stan:
        $ gg_del_stan = True
    if enemy_stan:
        $ enemy_del_stan = True
    #show expression '#0004' 
    hide screen test_duel_game_start_screen
    #with Dissolve(.5)
    if hasattr(store, 'go_lose') and go_lose:

        $ go_lose = False
        if not enemy_stan:
            jump test_duel_lose
        else:
            $ enemy_stan = False

    jump test_duel_game
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
