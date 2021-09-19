














screen test_glyph_episode_2_2(spell_now):
    default attack_now       = True


    default attack_now_up    = False
    default can_hide         = False    
    default potion_use       = False
    key "rollback" action NullAction()
    default c_colors = {
    'win' : '#FFE2B6',
    'lose': '#FF8F77',
    'draw': '#96D9FF',
    }
    #default spell_now = 'incendio'#'combat_bolt'
    if   spell_now == 'combat_bolt':
        default attack_now_timer = 118
    elif spell_now == 'incendio':
        default attack_now_timer = 415
    elif spell_now == 'episkey':
        default attack_now_timer = 180
    elif spell_now == 'rictusempra':
        default attack_now_timer = 250
        
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
                        Return(int((float(attack_now_timer)/1100.0)*100.0))
                        ]
                    
                    #attack_now_timer < 1470
                    
                    elif spell_now == 'rictusempra':
                        action [
                        Return(int((float(attack_now_timer)/1470.0)*100.0))
                        

                    ]

                    #attack_now_timer < 970
                    elif spell_now == 'incendio':
                        action [
                        Return(int((float(attack_now_timer)/970.0)*100.0))
                        

                    ]

                    elif spell_now == 'combat_bolt':
                        action [
                        Return(int((float(attack_now_timer)/650.0)*100.0))
                        

                    ]

        
        if attack_now and can_hide is False:
            if   spell_now == 'combat_bolt':
           



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
                    timer .01 repeat True action [SetScreenVariable('attack_now_timer', attack_now_timer+10)]

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
                if duel_cooldown:
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
                if duel_cooldown:
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
                if duel_cooldown:
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



            



            # $ ptmps = potions['Lesser Heal']
            # viewport:
            #     xmaximum 132
            #     ymaximum 115
            #     xalign .55 yalign .5
            #     if ptmps:
            #         imagebutton:
            #             idle 'mini_games/duels/new/potion_button_duels.png'
            #             hover im.MatrixColor('mini_games/duels/new/potion_button_duels.png', im.matrix.brightness(.3))
            #             focus_mask None
            #             hovered   Function(show_up_donw_text, text_now = "Lesser Heal", x_now = 930, y_now = 920)
            #             unhovered Hide('text_animation_up_screen')
            #             if potion_use:
            #                 action NullAction()
            #             else:
            #                 action  Hide('text_animation_up_screen'), SetScreenVariable('potion_use', True), SetVariable('potion_now', True), Function(set_potion, potion = 'Lesser Heal')
            #             xalign .5 yalign .5
            #         image 'lesser_heal_duels' xalign .5 yalign .5
            #         text str(ptmps) size 25 font 'fonts/h_font.ttf' xalign .7 yalign .9 outlines [(1, "#000", 0, 0)]
            #     if potion_use:
            #         image im.Grayscale('mini_games/duels/new/potion_button_duels.png') xalign .5 yalign .5
            #         add im.Grayscale('mini_games/duels/new/lesser_heal_duels.png') xalign .5 yalign .5








image warning_icon:



    'images/mini_games/magic/mouse_star.png' with Dissolve(.5)

    pause .5

    Transform('images/mini_games/magic/mouse_star.png', alpha = .5) with Dissolve(.5)

    pause .5

    repeat

image glyph_and_bg = LiveComposite(
    (1920, 1080),
    (0, 0), 'prologue/19-32/magery_1_2.webp',
    (700, 200), 'mini_games/magic/glyph_2_bg.png',
    
    (700, 200), 'mini_games/magic/glyph_2.png',
    )

init -100 python:
    class MagicMiniGame_2(renpy.Displayable):
        
        
        
        def __init__(self, circles = [], timer = 7, **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            
            self.tick_now       = None
            
            self.f_time         = None 
            self.crop_y         = 70
            self.circles        = []
            self.click          = False
            
            self.time           = 7
            self.time_next      = None
            self.particles   = []
            self.path        = 'images/mini_games/magic/'
            for i in xrange(500):
                self.particles.append(0)
            
            
            self.particles_next = 0
        
        def check_circles(self, x, y):
            def circle_def(x0, y0, x, y):
                r = 10
                if (x - x0)**2 + (y - y0)**2 <= r**2:
                    return True
            
            for i in self.circles:
                if circle_def(i[0], i[1], x, y):
                    return True
        
        def get_line(self, x1, y1, x2, y2):
            points = []
            issteep = abs(y2-y1) > abs(x2-x1)
            if issteep:
                x1, y1 = y1, x1
                x2, y2 = y2, x2
            rev = False
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
                rev = True
            deltax = x2 - x1
            deltay = abs(y2-y1)
            error = int(deltax / 2)
            y = y1
            ystep = None
            if y1 < y2:
                ystep = 1
            else:
                ystep = -1
            for x in range(x1, x2 + 1):
                if issteep:
                    points.append((y, x))
                else:
                    points.append((x, y))
                error -= deltay
                if error < 0:
                    y += ystep
                    error += deltax
            
            if rev:
                points.reverse()
            return points
        
        def draw_circle(self):
            x = renpy.get_mouse_pos()[0]
            y = renpy.get_mouse_pos()[1]
            new_x = None
            new_y = None
            
            self.particles[self.particles_next] = ((x-100+renpy.random.randint(-30, 30), y-100+renpy.random.randint(-20, 20), 0, 0, renpy.random.randint(1, 6)))
            self.particles_next += 1
            if not self.check_circles(x, y):
                self.circles.append([x, y])
                if len(self.circles) >= 2:
                    x_0 = self.circles[len(self.circles)-1][0]
                    y_0 = self.circles[len(self.circles)-1][1]
                    
                    x_1 = self.circles[len(self.circles)-2][0]
                    y_1 = self.circles[len(self.circles)-2][1]
                    
                    self.debug = self.get_line(x_0, y_0, x_1, y_1)
                    
                    for i in self.debug[1::15]:
                        if not self.check_circles(i[0], i[1]):
                            self.circles.insert(len(self.circles)-1, i)
            
            renpy.restart_interaction()
        
        
        
        
        def render(self, width, height, st, at):
            rend = renpy.Render(1920, 1080)
            if not self.tick_now:
                
                self.tick_now = pygame.time.get_ticks()
            
            self.f_time       = pygame.time.get_ticks() - self.tick_now
            
            self.tick_now     = pygame.time.get_ticks()
            if self.click:
                if self.time_next == None:
                    
                    self.time_next  = datetime.datetime.today() + datetime.timedelta(seconds=1)
                
                if datetime.datetime.today() >= self.time_next: 
                    
                    self.time -= 1
                    
                    self.time_next = None
                    
                    renpy.restart_interaction()
                
                
                if self.time <= 0:
                    
                    self.end_interaction()
            
            
            
            
            
            
            
            xx = renpy.get_mouse_pos()[0]
            yy = renpy.get_mouse_pos()[1]
            
            
            rend.blit(renpy.render(Image('images/mini_games/magic/time_line.png'), 1920, 1080, 0.3, at), (500, 50,))
            rend.blit(renpy.render(Crop((0, 0, int(((float(self.time)/7.0) )*922), 142), 'images/mini_games/magic/time_line_2.png'), 1920, 1080, 0.3, at), (500, 50,))
            
            
            
            
            
            
            
            
            if return_lose and self.click:
                self.end_interaction()
            
            
            
            
            
            
            
            
            if self.click:
                
                
                
                
                
                
                
                
                
                
                
                if 1000 - yy > self.crop_y:
                    self.crop_y = (1000 - yy)
            
            
            for i in self.circles:
                rend.blit(renpy.render(Image(self.path+'red_star.png'), 38, 475, 0.3, at), (i[0]-37, i[1]-37))
            
            
            
            
            
            renpy.redraw(self, 0)
            return rend
        def event(self, event, x, y, st):
            
            
            if True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 1:
                        if not self.click:
                            if renpy.get_mouse_pos()[0] > 945 and  renpy.get_mouse_pos()[1] > 880 and renpy.get_mouse_pos()[1] < 950 and renpy.get_mouse_pos()[0] < 1020:
                                self.click = True
                                renpy.restart_interaction()
                
                
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.click:
                            self.end_interaction()
                if event.type == pygame.MOUSEMOTION:
                    
                    if self.click:
                        self.draw_circle()
        def end_interaction(self):
            r = int((self.crop_y/700.0)*100)
            if r > 100:
                r = 100
            renpy.end_interaction(r)
transform hide_show_screen():
    on show:
        alpha 0.0
        linear .5 alpha 1.0
    on hide:
        alpha 1.0
        linear .5 alpha 0.0



screen test_glyph_2:
    key "rollback" action NullAction()
    viewport:
        xmaximum 1920
        ymaximum 1080
        at hide_show_screen
        add 'prologue/19-32/magery_1_2.webp'

        imagebutton:
            idle '#0000'
            hover '#0000'
            hovered SetVariable('return_lose', True)
            action NullAction()

        imagebutton:
            xpos 700
            ypos 200
            idle 'glyph_2_bg'
            hover 'glyph_2_bg'
            hovered SetVariable('return_lose', False)
            focus_mask True
            action NullAction()
    add mmt

    if mmt.particles is not None:

        for i in mmt.particles[::4]:
            if i is not 0:
                add "images/mini_games/magic/square.png" at raintransform1(i[0], i[1], i[4])


    if not mmt.click:
        add 'warning_icon' xpos 935 ypos 860
        viewport:
            xmaximum 285
            ymaximum 55

            imagebutton:
                idle 'order_start_button'
                hover im.MatrixColor('mini_games/caffe/order_start_button.png', im.matrix.brightness(.3))
                action Jump('end_MagicMiniGame_2_label')


            text _('Skip') font 'fonts/h_font.ttf' size 23 color '#FFFFFF' xalign .5 yalign .45
            xpos 645 ypos 155
        window:
            at my_say_transform
            style_prefix "say"
            id "window"

            window:
                id "namebox"
                style "namebox"

                text unicode('\n\nAttempt №') + str(game_now) id "who" bold True color '#fff'


            text _('\n\nClick and drag your mouse to draw the glyph on your screen. You have ') + str(timer) + _(' seconds.') id "what" color persistent.dialogue_color xpos 300


    text 'Time left' size 25 font 'fonts/h_font.ttf' xalign .53 ypos 52




screen test_glyph_2_result:
    viewport:
        xmaximum 1920
        ymaximum 1080
        imagebutton idle '#000a' hover '#000a' action Return('1')
        if test == 'lose':
            text str(test) xalign .5 yalign .5 size 50

        else:
            text str(test) + '%' xalign .5 yalign .5 size 50
        at hide_show_screen
label MagicMiniGameLabel_2:
    scene sc i_Victoria_0_1 with Dissolve(.5)
    "[Name]" "Miss Lapis, I'd like to practice my spell."
    show sc i_magery_1_1 with my_dissolve
    "Victoria" "Commendable zeal, [Name]. What spell are you interested in?"
    $ result_magic = 3+3
    $ score_1      = 0
    $ score_2      = 0
    $ score_3      = 0
    $ result_score = 3
    menu:
        "Combat Bolt" if True:
            $ spellname = 'Combat Bolt'
        "Episkey" if hasattr(store, 'has_episkey'):
            $ spellname = 'Episkey'
        "Incendio" if hasattr(store, 'has_incendio'):
            $ spellname = 'Incendio'
        "Rictusempra" if hasattr(store, 'has_rictusempra'):
            $ spellname = 'Rictusempra'
        


    "[Name]" "I wish to improve my mastery of [spellname], ma'am."

    "Victoria" "Excellent! Stand at the board and begin."

    scene sc i_magery_1_2 with Dissolve(.5)
    $ return_lose = False
    $ mmt  = MagicMiniGame_2(7)
    $ game_now = 1
    $ timer    = 7
    if spellname == 'Combat Bolt':
        $ test = renpy.call_screen('test_glyph_episode_2_2', 'combat_bolt')
        #default attack_now_timer = 118
    elif spellname == 'Incendio':
        $ test = renpy.call_screen('test_glyph_episode_2_2', 'incendio')
        
    elif spellname == 'Episkey':
        $ test = renpy.call_screen('test_glyph_episode_2_2', 'episkey')
        
    elif spellname == 'Rictusempra':
        $ test = renpy.call_screen('test_glyph_episode_2_2', 'rictusempra')
        
    $ score_1 = test
    "Score: [score_1]%%"
    $ result_score += 1
    if int(score_1) >= 100:
        $ result_score += 1
    if int(test) < 50:
        show sc i_magery_1_3 with Dissolve(.5)
        "Victoria" "Concentrate, [Surname]! I know you can do better than that."
    elif int(test) < 100:
        show sc i_magery_1_4 with Dissolve(.5)
        "Victoria" "Not a bad result, but there's room for improvement."
    elif True:
        $ result_magic += 1
        show sc i_magery_1_5 with Dissolve(.5)
        "Victoria" "Amazing, [Name]! Excellent concentration! Can you do it again?"


    scene sc i_magery_1_2 with Dissolve(.5)
    $ return_lose = False
    $ mmt  = MagicMiniGame_2(6)
    if spellname == 'Combat Bolt':
        $ test = renpy.call_screen('test_glyph_episode_2_2', 'combat_bolt')
        #default attack_now_timer = 118
    elif spellname == 'Incendio':
        $ test = renpy.call_screen('test_glyph_episode_2_2', 'incendio')
        
    elif spellname == 'Episkey':
        $ test = renpy.call_screen('test_glyph_episode_2_2', 'episkey')
        
    elif spellname == 'Rictusempra':
        $ test = renpy.call_screen('test_glyph_episode_2_2', 'rictusempra')
    $ game_now = 2
    $ timer    = 6

    $ score_2 = test
    "Score: [score_2]%%"
    $ result_score += 1
    if int(score_2) >= 100:
        $ result_score += 1
    if int(test) < 50:
        show sc i_magery_1_3 with Dissolve(.5)
        "Victoria" "Come on, [Name]. I'm sure you can do better."
    elif int(test) < 100:
        show sc i_magery_1_4 with Dissolve(.5)
        "Victoria" "Not bad, but I've seen that you can do better."
    elif True:
        $ result_magic += 1
        show sc i_magery_1_5 with Dissolve(.5)
        "Victoria" "Well done, [Name]! You're getting better and better! Will you do it again?"



    scene sc i_magery_1_2 with Dissolve(.5)
    $ return_lose = False
    $ mmt  = MagicMiniGame_2(5)
    $ game_now = 3
    $ timer    = 5
    if spellname == 'Combat Bolt':
        $ test = renpy.call_screen('test_glyph_episode_2_2', 'combat_bolt')
        #default attack_now_timer = 118
    elif spellname == 'Incendio':
        $ test = renpy.call_screen('test_glyph_episode_2_2', 'incendio')
        
    elif spellname == 'Episkey':
        $ test = renpy.call_screen('test_glyph_episode_2_2', 'episkey')
        
    elif spellname == 'Rictusempra':
        $ test = renpy.call_screen('test_glyph_episode_2_2', 'rictusempra')

    $ score_3 = test
    "Score: [score_3]%%"
    $ result_score += 2
    if int(score_3) >= 100:
        $ result_score += 2
    if int(test) < 50:
        show sc i_magery_1_3 with Dissolve(.5)
        "Victoria" "No, no. This is clearly not your day, [Name]!"
    elif int(test) < 100:
        show sc i_magery_1_4 with Dissolve(.5)
        "Victoria" "It's a fairly stable spell, but it could be better."
    elif True:
        $ result_magic += 1
        show sc i_magery_1_5 with Dissolve(.5)
        "Victoria" "That's great! That's a phenomenal result!"
label end_MagicMiniGame_2_label:
    hide screen test_glyph_2
    show sc i_magery_1_4 with my_dissolve
    "Victoria" "That's enough, [Name]. The class has come to an end, so we'll continue next time."

    show sc i_magery_1_6 with my_dissolve
    "[Name]" "Thank you, Miss Lapis. You are my favorite teacher!"












    return





    $ game_now  = 1
    $ difficulty = 'Easy'
    $ timer_now = TimerClass(3)
    $ s = 2
    $ timer      = 0
    $ timer_hide = False
    $ timer     = 10
    $ timer_now = TimerClass(10)
label MagicMiniGameLabel_start_2:
    scene bg_magic_test with Dissolve(.5)
    $ unhovered_variable = 0
    $ unhovered_variable_2 = 1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
