image warning_icon:



    'images/mini_games/magic/mouse_star.png' with Dissolve(.5)

    pause .5

    Transform('images/mini_games/magic/mouse_star.png', alpha = .5) with Dissolve(.5)

    pause .5

    repeat


image warning_m_line_max:



    'images/mini_games/magic/m_line_max.png' with Dissolve(1.5)

    pause 1.5

    Transform('images/mini_games/magic/m_line_max.png', alpha = .6) with Dissolve(1.5)

    pause 1.5

    repeat


image square = "images/mini_games/magic/square.png"
image m_line_0_true = LiveComposite(
    (1920, 1080),
    (0, 0), 'mini_games/magic/bg_magic_test.png',
    (0, 0), 'mini_games/magic/m_line_0.png',
    )


transform my_say_transform:


    alpha 0.0


    linear .5 alpha 1.0


transform star_transform:




    alpha 0


    linear .5 alpha .5

    .5
    linear .5 alpha 1.0

    .5


    linear .5 alpha 0
init 10 python:
    import pygame, datetime, subprocess 
    cursor_dop = {"default":[ ("images/cursors/click.png", 1, 1) ] }
    class TimerClass(renpy.Displayable):
        
        
        
        def __init__(self, time, **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            
            
            
            
            self.time_next = None
            self.time_max  = time
            self.time      = time
            
            
            
            
            
            
            self.time_wait  = 0
        
        def render(self, width, height, st, at):
            
            rend = renpy.Render(45, 45)
            
            
            
            
            
            
            rend.blit(renpy.render(Image('images/mini_games/magic/time_line.png'), 1920, 1080, 0.3, at), (500, 50,))
            rend.blit(renpy.render(Crop((0, 0, int(((float(self.time)/self.time_max) )*922), 142), 'images/mini_games/magic/time_line_2.png'), 1920, 1080, 0.3, at), (500, 50,))
            
            if mmg.mouse_down:
                if self.time_next == None:
                    
                    self.time_next  = datetime.datetime.today() + datetime.timedelta(seconds=1)
                
                if datetime.datetime.today() >= self.time_next: 
                    
                    self.time -= 1
                    
                    self.time_next = None
                    
                    renpy.restart_interaction()
                
                
                if self.time <= 0:
                    
                    renpy.end_interaction(mmg.check_win(click = True))
            
            
            
            
            
            
            
            
            
            renpy.redraw(self, 0)
            
            return rend
        
        
        def event(self, event, x, y, st):
            
            
            if mmg.click and not mmg.only_watch:
                
                
                if event.type == pygame.MOUSEBUTTONUP:
                    
                    if event.button == 1:
                        if mmg.mouse_down:
                            if len(mmg.win_circles):
                                
                                renpy.end_interaction(mmg.check_win())
                            else:
                                
                                renpy.end_interaction(mmg.circles)


    class ExplodeParticle:
        
        def __init__(self, theDisplayable, timeDelay):
            self.displayable = theDisplayable
            self.delay = timeDelay
            self.xSpeed = (renpy.random.random() - 0.5) * 0.02
            self.ySpeed = (renpy.random.random() - 0.5) * 0.02
            self.xPos = 0.5
            self.yPos = 0.5
        
        def update(self, theTime):
            
            if (theTime > self.delay):
                self.xPos += self.xSpeed
                self.yPos += self.ySpeed
                
                if self.xPos > 1.05 or self.xPos < -1.05 or self.yPos > 1.05 or self.yPos < -1.05:
                    return None
            
            return (self.xPos, self.yPos, theTime, self.displayable)


    class ExplodeFactory: 
        
        def __init__(self, theDisplayable, explodeTime=0, numParticles=20):
            self.displayable = theDisplayable
            self.time = explodeTime
            self.particleMax = numParticles
        
        def create(self, partList, timePassed):
            newParticles = None
            if partList == None or len(partList) < self.particleMax:
                if timePassed < self.time or self.time == 0:
                    newParticles = self.createParticles()
            return newParticles
        
        
        def createParticles(self):
            timeDelay = renpy.random.random() * 0.6
            return [ExplodeParticle(self.displayable, timeDelay)]
        
        def predict(self):
            return [self.displayable]

    class MagicMiniGame(renpy.Displayable):
        
        
        
        def __init__(self, circles = [], click = True, win_circles = [], timer = False, **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            self.circle_x    = -100
            self.circle_y    = -100 
            self.path        = 'images/mini_games/magic/'
            self.time_wait   = 0
            self.start       = False
            self.win_circles = win_circles
            self.only_watch  = False
            for i in self.win_circles:
                i.append(False)
            
            print(self.win_circles)
            
            
            self.circles     = circles
            self.circles_2   = []
            self.mask_circles =  []
            self.mouse_down  = False
            self.mouse_up    = False
            self.click       = click
            self.particles   = []
            for i in xrange(500):
                self.particles.append(0)
            
            
            self.particles_next = 0
            self.win_image   = [0, 0, 0, 0, 0, 0]
            self.win_image_now = 0
            
            
            self.timer       = timer
            
            self.win_stars   = []
            self.win         = 0
            
            self.add_star    = 1
            
            
            self.all         = len(self.win_circles)
            self.exit        = None
            self.exit_2      = [-100, -100]
            self.exit_3      = False
            
            self.debug       = []
            self.xxxxxxx     = -100
            self.yyyyyyy     = -100
            
            self.xxxxx = 0
            self.yyyyy = 0
            
            self.only_watch_win_image_now = 0
            
            
            self.only_watch_win_image_now_time_next = datetime.datetime.today()
            
            self.y_next = 0
            self.x_next = 0
            
            
            self.tick_now       = None
            
            self.f_time         = None 
            
            self.only_watch_win_image = None
            self.show_max_line_screen_var = 0
        
        def show_max_line_screen(self):
            Hide('m_line_max_screen')()
            
            Show('m_line_max_screen')()
        def render(self, width, height, st, at):
            rend = renpy.Render(1920, 1080)
            if not self.tick_now:
                
                self.tick_now = pygame.time.get_ticks()
            
            self.f_time       = pygame.time.get_ticks() - self.tick_now
            
            self.tick_now     = pygame.time.get_ticks()
            if self.only_watch_win_image is None:
                
                xxxxx = renpy.get_mouse_pos()[0]
                yyyyy = renpy.get_mouse_pos()[1]
            
            
            
            if self.only_watch_win_image is not None and b >= 95:
                if self.win_image[0] < 300:
                    self.win_image[0] += int(1000*(float(self.f_time)/1000))
                if self.win_image[1] > -360:
                    if self.win_image[0] > 180:
                        self.win_image[1] -= int(800*(float(self.f_time)/1000))
                        rend.blit(renpy.render(




            AlphaMask(
                Crop(
                    (
            894+240+self.win_image[1]-80, 387+295, 100, 100), 'm_line_0_true'), 
                Transform(self.path+'circle_white.png', zoom = 1.0)), 1920, 1080, 0.3, at), (894+240+self.win_image[1]-80, 387+295,))
                
                
                
         
                
                
                
                
                
                
                
                
                if self.win_image[2] > -350:
                    
                    if self.win_image[1] <= -350:
                        self.win_image[2] -= int(800*(float(self.f_time)/1000))
                        rend.blit(renpy.render(




            AlphaMask(
                Crop(
                    (
            894+240-350-80, 387+295-self.win_image[2]-30, 100, 100), 'm_line_0_true'), 
                Transform(self.path+'circle_white.png', zoom = 1.0)), 1920, 1080, 0.3, at), (894+240-350-80, 387+295-self.win_image[2]-30,))
                
                
                
                
                
                
                
                
                
                elif self.win_image[3] < 520:
                    self.win_image[3] += int(800*(float(self.f_time)/1000))
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                elif self.win_image[4] < 440:
                    self.win_image[3] += int(800*(float(self.f_time)/1000))
                    self.win_image[4] += int(800*(float(self.f_time)/1000))
                
                
                
                
                
                
                
                
                
                
                
                
                
                elif self.win_image[5] > -440:
                    self.win_image[4] += int(800*(float(self.f_time)/1000))
                    self.win_image[5] -= int(800*(float(self.f_time)/1000))
                else:
                    if b >= 95:
                        if not self.show_max_line_screen_var:
                            self.show_max_line_screen_var = 1
                            
                            renpy.end_interaction(0)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            rend.blit(renpy.render(Transform(self.path+'m_line_1.png', alpha = .5), 38, 475, 0.3, at), (0, 0))
            
            
            rend.blit(renpy.render(Transform(Crop((894, 387, 220, self.win_image[0]), 'm_line_0_true')), 38, 475, 0.3, at), (894, 387))
            rend.blit(renpy.render(Transform(Crop((894+220, 387+300, self.win_image[1], 100), 'm_line_0_true')), 38, 475, 0.3, at), (894+220, 387+300))
            rend.blit(renpy.render(Transform(Crop((805, 730, -200, self.win_image[2]), 'm_line_0_true')), 38, 475, 0.3, at), (805, 730))
            rend.blit(renpy.render(Transform(Crop((660, 380, self.win_image[3], -200), 'm_line_0_true')), 38, 475, 0.3, at), (660, 380))
            
            rend.blit(renpy.render(Transform(Crop((1130, 300, 300, self.win_image[4]), 'm_line_0_true')), 38, 475, 0.3, at), (1130, 300))
            
            rend.blit(renpy.render(Transform(Crop((1180, 730, self.win_image[5], 200), 'm_line_0_true')), 38, 475, 0.3, at), (1180, 730))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            if self.mouse_down:
                
                
                
                rend.blit(renpy.render(




            AlphaMask(
                Crop(
                    (self.xxxxxxx-50, self.yyyyyyy-50, 100, 100), 'm_line_0_true'), Transform(self.path+'circle_white.png', zoom = 1.0)), 1920, 1080, 0.3, at), (self.xxxxxxx-50, self.yyyyyyy-50,))
            
            
            
            
            
            
            
            
            for i in self.circles:
                rend.blit(renpy.render(Image(self.path+'red_star.png'), 38, 475, 0.3, at), (i[0]-37, i[1]-37))
            
            
            
            
            
            
            renpy.redraw(self, 0)
            
            return rend
        
        
        def get_last_win_circle(self):
            len_tmp = len(self.win_circles)
            for i in xrange(len_tmp):
                try:
                    if not self.win_circles[i+1][2]:
                        return i
                except:
                    pass
            
            return 0
        
        
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
            
            def circle_in_circle_def(x):
                def circle_def(x0, y0, x, y, r = 35):
                    
                    if (x - x0)**2 + (y - y0)**2 <= r**2:
                        return True
                    
                    if (x-15 - x0)**2 + (y - y0)**2 <= r**2:
                        return True
                    
                    if (x+15 - x0)**2 + (y - y0)**2 <= r**2:
                        return True
                    
                    
                    
                    if (x - x0)**2 + (y - y0-15)**2 <= r**2:
                        return True
                    
                    if (x-15 - x0)**2 + (y - y0-15)**2 <= r**2:
                        return True
                    
                    if (x+15 - x0)**2 + (y - y0-15)**2 <= r**2:
                        return True
                    
                    
                    
                    if (x - x0)**2 + (y - y0+15)**2 <= r**2:
                        return True
                    
                    if (x-15 - x0)**2 + (y - y0+15)**2 <= r**2:
                        return True
                    
                    if (x+15 - x0)**2 + (y - y0+15)**2 <= r**2:
                        return True
                
                for i in self.win_circles:
                    if self.win_circles[len(self.win_circles)-1][2]:
                        renpy.end_interaction(self.check_win(click = True))
                    if circle_def(i[0], i[1], x[0], x[1]):
                        if not i[2]:
                            i[2] = True
                            
                            
                            
                            
                            
                            
                            
                            
                            return True
                        else:
                            return False
            
            
            
            
            
            
            def circle_def(x0, y0, x, y):
                r = 15
                if (x - x0)**2 + (y - y0)**2 <= r**2:
                    return True
                
                if (x-15 - x0)**2 + (y - y0)**2 <= r**2:
                    return True
                
                if (x+15 - x0)**2 + (y - y0)**2 <= r**2:
                    return True
                
                
                
                if (x - x0)**2 + (y - y0-15)**2 <= r**2:
                    return True
                
                if (x-15 - x0)**2 + (y - y0-15)**2 <= r**2:
                    return True
                
                if (x+15 - x0)**2 + (y - y0-15)**2 <= r**2:
                    return True
                
                
                
                if (x - x0)**2 + (y - y0+15)**2 <= r**2:
                    return True
                
                if (x-15 - x0)**2 + (y - y0+15)**2 <= r**2:
                    return True
                
                if (x+15 - x0)**2 + (y - y0+15)**2 <= r**2:
                    return True
            
            
            
            
            x = renpy.get_mouse_pos()[0]
            y = renpy.get_mouse_pos()[1]
            new_x = None
            new_y = None
            if self.particles_next < len(self.particles)-1:
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
            
            
            
            
            
            v = circle_in_circle_def([x, y])
            global unhovered_variable_2
            if v:
                if unhovered_variable_2 == 1:
                    self.win += 1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            renpy.restart_interaction()
        
        
        
        def check_win(self, click = False):
            self.exit = [self.xxxxxxx-125, self.yyyyyyy-125]
            
            
            
            win = int((float(self.win)/self.all)*100)
            if win >= 95:
                win = 100
            if click:
                if win == 100:
                    return   [win, self.circles, 1, 1]
                
                else:
                    return   [win, self.circles, 1]
            
            else:
                if win == 100:
                    return   [win, self.circles, 0, 1]
                else:
                    return   [win, self.circles]
        
        def event(self, event, x, y, st):
            
            
            if self.click and not mmg.only_watch:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 1:
                        
                        tmp_xxx = renpy.get_mouse_pos()[0]
                        tmp_yyy = renpy.get_mouse_pos()[1]
                        if tmp_xxx >= 950+80 and tmp_xxx <= 950+80+80 and tmp_yyy >= 440 and tmp_yyy <= 440+70:
                            self.mouse_down = True
                            config.mouse = None
                            renpy.restart_interaction()
                
                
                
                
                
                
                
                
                
                
                
                if event.type == pygame.MOUSEMOTION:
                    
                    if unhovered_variable == 2 and not self.only_watch:
                        
                        renpy.end_interaction(self.check_win(click = True))
                    if self.mouse_down:
                        self.draw_circle()
                    elif not self.only_watch:
                        tmp_xxx = renpy.get_mouse_pos()[0]
                        tmp_yyy = renpy.get_mouse_pos()[1]
                        if tmp_xxx >= 950 and tmp_xxx <= 950+80 and tmp_yyy >= 460 and tmp_yyy <= 460+70:
                            if config.mouse is None:
                                config.mouse = cursor_dop
                        else:
                            if config.mouse is not None:
                                config.mouse = None   
                
                
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.draw_circle()                    

image boom = Particles(ExplodeFactory("images/mini_games/magic/circle_red.png", numParticles=80, explodeTime = 1.0))
transform raintransform1(x, y, t):

    xpos x ypos y

    linear t xpos x ypos 2000









init python:
    import math
    def Trampoline(x):
        if x < 0.5:
            return (0.5, 4 * x * x * x, 4 * x * x * x, 0)
        else:
            return (0.5, 1 - pow(-2 * x + 2, 3) / 2, 1 - pow(-2 * x + 2, 3) / 2, 0)
screen m_line_max_screen():

    add 'warning_m_line_max'

screen MagicMiniGameScreen(circles=[], click=True, win_circles=[], timer=3, click_warning=True):


    key "rollback" action NullAction()

    viewport:







        xpos 950 ypos 460
        xmaximum 80
        ymaximum 70
    add mmg
    if click and mmg.mouse_down and not mmg.only_watch:
        imagebutton:
            idle '#0000'
            hover '#0000'
            hovered SetVariable('unhovered_variable', 2)
            action NullAction()





        $ mimg = Transform('mini_games/magic/m_line_2.png', alpha = .02)
        imagebutton:
            idle mimg
            hover mimg
            focus_mask True
            hovered SetVariable('unhovered_variable', 1)

            unhovered SetVariable('unhovered_variable', 2)
            action NullAction()
        $ mimg = Transform('mini_games/magic/m_line_05.png', alpha = .02)
        imagebutton:
            idle mimg
            hover mimg
            focus_mask True
            hovered SetVariable('unhovered_variable_2', 1), SetVariable('unhovered_variable', 1)

            unhovered SetVariable('unhovered_variable_2', 2)
            action NullAction()



    if mmg.particles is not None:
        if mmg.only_watch:
            for i in mmg.particles[::2]:
                if i is not 0:
                    add "images/mini_games/magic/square.png" at raintransform1(i[0], i[1], i[4])
        else:
            for i in mmg.particles[::5]:
                if i is not 0:
                    add "images/mini_games/magic/square.png" at raintransform1(i[0], i[1], i[4])
    for i in mmg.win_stars:


        add i[2] xpos i[0] ypos i[1] at star_transform
    viewport:

        xpos 950+80
        xmaximum 80
        ypos 440
        ymaximum 70
        add '#0000'
    if not mmg.mouse_down and click_warning and not mmg.only_watch:
        add 'warning_icon' xpos 465+465+80 ypos 270+170
        window:
            at my_say_transform
            style_prefix "say"
            id "window"

            window:
                id "namebox"
                style "namebox"

                text unicode('Attempt №') + str(game_now) + ', Difficulty: ' +  str(difficulty) id "who" bold True color '#fff'
            text _('Click and drag your mouse to draw the glyph on your screen. You have ') + str(timer) + _(' seconds.') id "what" color persistent.dialogue_color xpos 300







    add timer_now
    text 'Time left' size 25 font 'fonts/h_font.ttf' xalign .53 ypos 52
    if not mmg.mouse_down and not mmg.only_watch:

        viewport:
            xmaximum 285
            ymaximum 55

            imagebutton:
                idle 'order_start_button'
                hover im.MatrixColor('mini_games/caffe/order_start_button.png', im.matrix.brightness(.3))
                action Jump('sheet_24_end_game')


            text _('Skip') font 'fonts/h_font.ttf' size 23 color '#FFFFFF' xalign .5 yalign .45
            xpos 645 ypos 155




















transform spark(my_x, my_y):
    xpos my_x
    ypos my_y

    linear 5.0 xpos my_x-100 ypos my_y-100
image ms = Crop((100, 0, -30, 387), 'm_line_0_true')
label MagicMiniGameLabel:
    $ game_now  = 1
    $ difficulty = 'Easy'
    $ timer_now = TimerClass(3)
    $ s = 2
    $ timer      = 0
    $ timer_hide = False
    $ timer     = 10
    $ timer_now = TimerClass(10)
label MagicMiniGameLabel_start:
    scene bg_magic_test with Dissolve(.5)
    $ unhovered_variable = 0
    $ unhovered_variable_2 = 1
    $ circles_animation  = [[8, 'down']]




















    python:
        if s == 0:
            a = [] 
        elif s == 1:
            a = [[1047, 407], [1055, 416], [1059, 426], [1063, 437], [1067, 447], [1071, 459], [1076, 468], [1079, 478], [1083, 489], [1087, 499], [1088, 510], [1091, 520], [1092, 533], [1093, 544], [1093, 557], [1093, 568], [1097, 579], [1099, 590], [1096, 604], [1093, 615], [1091, 626], [1091, 637], [1088, 647], [1085, 657], [1078, 665], [1072, 676], [1065, 686], [1056, 691], [1047, 697], [1038, 702], [1027, 705], [1017, 709], [1005, 713], [996, 720], [987, 725], [977, 733], [966, 740], [956, 743], [944, 748], [934, 751], [923, 754], [911, 756], [898, 757], [886, 759], [875, 759], [863, 760], [853, 761], [842, 761], [830, 761], [819, 756], [810, 751], [801, 746], [792, 741], [783, 733], [774, 728], [766, 720], [757, 713], [746, 707], [737, 701], [731, 692], [725, 682], [719, 671], [714, 661], [708, 652], [703, 642], [696, 634], [691, 624], [688, 614], [687, 604], [685, 594], [680, 583], [676, 572], [675, 561], [673, 549], [671, 537], [670, 527], [667, 511], [665, 501], [664, 491], [665, 481], [671, 469], [676, 455], [683, 444], [687, 428], [692, 418], [697, 408], [701, 398], [707, 381], [712, 372], [716, 361], [722, 352], [732, 339], [743, 330], [755, 323], [765, 316], [774, 307], [784, 297], [795, 288], [806, 284], [822, 279], [837, 277], [853, 274], [863, 273], [879, 265], [893, 260], [906, 255], [916, 250], [929, 248], [940, 248], [951, 248], [968, 248], [982, 250], [1005, 250], [1016, 252], [1027, 255], [1040, 256], [1052, 261], [1063, 264], [1078, 267], [1090, 272], [1099, 277], [1108, 284], [1121, 291], [1132, 297], [1141, 305], [1151, 314], [1158, 323], [1167, 333], [1175, 341], [1184, 349], [1191, 359], [1195, 369], [1201, 379], [1206, 393], [1210, 403], [1214, 414], [1218, 426], [1222, 437], [1225, 448], [1227, 460], [1231, 472], [1233, 482], [1236, 495], [1237, 507], [1237, 521], [1239, 532], [1240, 544], [1243, 555], [1243, 568], [1244, 580], [1244, 593], [1240, 604], [1237, 615], [1234, 627], [1232, 639], [1227, 652], [1213, 675], [1206, 683], [1200, 693], [1194, 707], [1187, 719], [1182, 730], [1174, 741], [1166, 753], [1148, 762], [1141, 773], [1134, 786], [1131, 796], [1124, 804], [1113, 817], [1106, 825], [1098, 832], [1088, 839], [1076, 846], [1067, 852], [1058, 858], [1048, 865], [1039, 870], [1029, 877], [1015, 881], [1004, 888]]
            a = a[::5]
        elif s == 2:
            a = [ [1003, 469], [1043, 520], [1051, 579], [1024, 640], [1010, 686], [933, 709], 
            [864, 712], [805, 702], [751, 680], [700, 638], [679, 575], [669, 515], [669, 454], 
            [688, 398], [713, 347], [749, 305], [802, 276], [856, 253], [914, 240], [974, 242], 
            [1032, 260], [1086, 290], [1137, 331], [1173, 382], [1204, 448], [1222, 511], [1228, 575], 
            [1227, 636], [1200, 713], [1180, 757], [1115, 798], [1060, 840], [1010, 860]]


        else:
            a = [
        [480, 300], [480, 325], [480, 350], [480, 375], [480, 400], [480, 250],


        [1500-975, 250],  [1550-975,  250],  [1600-975,  250],  [1650-975,  250], 
        [1700-975,  250],  [1750-975,  250], 

        [1800-975,  250], [1850-975,  250],  

        [1900-975,  250],  [1950-975,  250],  [2000-975,  250], [2050-975,  250],


        [1075, 300], [1075, 325], [1075, 350], [1075, 375], [1075, 400], [1075, 425],
        ] 
        mmg = MagicMiniGame([], True, a, timer = timer_hide)
    show screen MagicMiniGameScreen(win_circles = a, timer = timer, click_warning = False) with Dissolve(.75)

    $ renpy.pause(.5)
    $ b = renpy.call_screen('MagicMiniGameScreen', win_circles = a, timer = timer)

    python:
        d = 0
        if len(b) == 3 and b[2]:
            d = 1
        if len(b) == 4:
            d = 2
        c = b[1]
        b = b[0]
    $ stss = mmg.check_win()
    $ mmg.mouse_down = False
    $ mmg.timer      = False
    $ mmg.only_watch = True

    $ mmg.only_watch_win_image = [



    [987, 469, False, False], [1021, 519, False, False], [1038, 571, False, False], [1036, 631, False, False], [996, 679, False, False], [936, 708, False, False], [874, 714, False, False], [816, 700, False, False], [763, 669, False, False], [717, 633, False, False], [685, 585, False, False], [670, 526, False, False], [669, 463, False, False], [691, 402, False, False], [721, 348, False, False], [777, 306, False, False], [831, 273, False, False], [906, 258, False, False], [975, 256, False, False], [1030, 276, False, False], [1086, 303, False, False], [1138, 337, False, False], [1171, 387, False, False], [1203, 436, False, False], [1234, 496, False, False], [1222, 555, False, False], [1209, 612, False, False], [1192, 673, False, False], [1167, 732, False, False], [1125, 774, False, False], [1080, 816, False, False], [1029, 846]]


    hide screen MagicMiniGameScreen
    hide screen m_line_max_screen 

    if d == 1:
        show screen MagicMiniGameScreen(circles = c, win_circles = a, click = False) 
        $ renpy.pause(999999999)
        "Score: [b]%%"
    elif d == 2:
        scene bg_magic_test
        call screen MagicMiniGameScreen(circles = c, win_circles = a, click = False)
        show screen MagicMiniGameScreen(circles = c, win_circles = a, click = False) 

        hide screen m_line_max_screen

        show screen m_line_max_screen with Dissolve(.5)


        "Score: [b]%%"
    elif True:

        show screen MagicMiniGameScreen(circles = c, win_circles = a, click = False)
        "Score: [b]%%"

    if game_now == 1:
        $ game_now = 2
        if b >= 75:
            scene sc i_1_196_5 with Dissolve(.5)
            "Victoria" "Pleasant surprise, Mr. [Surname]. "
            show sc i_1_196_5 with my_dissolve
            "Victoria" "I can see you have good potential. "
            show sc i_1_196_5 with my_dissolve
            "[Name]" "(Hell yes I do! That was too easy!)"
            show sc i_1_196_5 with my_dissolve
            "Victoria" "Let's see if you can do even better."
            show sc i_1_196_5 with my_dissolve
            "[Name]" "(Bring it on!)"

            $ difficulty = 'Medium'
            $ timer     = 7
            $ timer_now = TimerClass(7)
            scene sc i_1_196_5
            hide screen MagicMiniGameScreen
            hide screen m_line_max_screen 
            with Dissolve(.5)

        elif b >= 50:
            scene sc i_1_196_4 with Dissolve(.5)
            "Victoria" "Not bad for the first time!"
            show sc i_1_196_4 with my_dissolve
            "Victoria" "But I've had more capable students."
            show sc i_1_196_4 with my_dissolve
            "[Name]" "{i}(Not bad? I can do better than \"not bad\"! Come on, [Name]!){/i}"
            show sc i_1_196_4 with my_dissolve
            "Victoria" "Let's try to make it more difficult..."
            $ difficulty = 'Medium'
            $ timer     = 7
            $ timer_now = TimerClass(7)
            scene sc i_1_196_4
            hide screen MagicMiniGameScreen
            hide screen m_line_max_screen 
            with Dissolve(.5)
        elif True:

            scene sc i_1_196_3 with Dissolve(.5)
            "Victoria" "[Surname], you're on the verge of failure."
            show sc i_1_196_3 with my_dissolve
            "Victoria" "That kind of concentration is no good!"
            show sc i_1_196_3 with my_dissolve
            "[Name]" "{i}(Crap... I need to focus! I won't lose this!){/i}"
            show sc i_1_196_3 with my_dissolve
            "Victoria" "Try again."
            $ difficulty = 'Easy'
            $ timer     = 10
            $ timer_now = TimerClass(10)
            scene sc i_1_196_3
            hide screen MagicMiniGameScreen
            hide screen m_line_max_screen 
            with Dissolve(.5)





    elif game_now == 2:
        $ game_now = 3
        if b >= 75:

            if timer == 7:
                scene sc i_1_196_5 with Dissolve(.5)
                "Victoria" "Very good, Mr. [Surname]! "
                show sc i_1_196_5 with my_dissolve
                "Victoria" "It is clear that you have potential."
                show sc i_1_196_5 with my_dissolve
                "[Name]" "(Hell yes I do! That was too easy!)"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "Let's see how good can you use it right now."
                show sc i_1_196_5 with my_dissolve
                "Victoria" "Your last try! Go!"
                $ difficulty = 'Hard'
                $ timer     = 5
                $ timer_now = TimerClass(5)
                scene sc i_1_196_5
                hide screen MagicMiniGameScreen
                hide screen m_line_max_screen 
                with Dissolve(.5)
            elif True:

                scene sc i_1_196_5 with Dissolve(.5)
                "Victoria" "Not bad, [Surname]!"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "I'm really interested to see what else you can do!"
                show sc i_1_196_5 with my_dissolve
                "[Name]" "(Is this a dream, or am I really that good?!)"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "Last one will be even more difficult. Get ready!"
                show sc i_1_196_5 with my_dissolve
                "[Name]" "(I am ready!)"
                $ difficulty = 'Medium'
                $ timer     = 7
                $ timer_now = TimerClass(7)
                scene sc i_1_196_5
                hide screen MagicMiniGameScreen
                hide screen m_line_max_screen 
                with Dissolve(.5)

        elif b >= 50:

            if timer == 7:
                scene sc i_1_196_4 with Dissolve(.5)
                "Victoria" "Mr. [Surname]! "
                show sc i_1_196_4 with my_dissolve
                "Victoria" "I recommend that you take this task more seriously."
                show sc i_1_196_4 with my_dissolve
                "[Name]" "(I can do better, I know it!)"
                show sc i_1_196_4 with my_dissolve
                "Victoria" "I'll give you one more try."
                scene sc i_1_196_4
                hide screen MagicMiniGameScreen
                hide screen m_line_max_screen 
                with Dissolve(.5)
                $ difficulty = 'Hard'
                $ timer     = 5
                $ timer_now = TimerClass(5)
            elif True:
                scene sc i_1_196_4 with Dissolve(.5)
                "Victoria" "Better. "
                show sc i_1_196_4 with my_dissolve
                "Victoria" "Bot not perfect."
                show sc i_1_196_4 with my_dissolve
                "[Name]" "(I can nail this. Just need a little bit more focus.)"
                show sc i_1_196_4 with my_dissolve
                "Victoria" "Let's make the task more difficult this time..."
                scene sc i_1_196_4
                hide screen MagicMiniGameScreen
                hide screen m_line_max_screen 
                with Dissolve(.5)
                $ difficulty = 'Medium'
                $ timer     = 7
                $ timer_now = TimerClass(7)
        elif True:


            scene sc i_1_196_3 with Dissolve(.5)
            "Victoria" "No, no, no... "
            show sc i_1_196_3 with my_dissolve
            "Victoria" "This is not the level I expect from my future students. "
            show sc i_1_196_3 with my_dissolve
            "[Name]" "Sorry, I've probably got disctracted. "
            show sc i_1_196_3 with my_dissolve
            "Victoria" "You still have one more try to impress me."
            show sc i_1_196_3 with my_dissolve
            "[Name]" "(it's now or never!)"
            scene sc i_1_196_3
            hide screen MagicMiniGameScreen
            hide screen m_line_max_screen 
            with Dissolve(.5)
            if timer == 7:
                $ difficulty = 'Medium'
                $ timer     = 7
                $ timer_now = TimerClass(7)
            elif True:
                $ difficulty = 'Easy'
                $ timer     = 10
                $ timer_now = TimerClass(10)
    elif game_now == 3:
        $ game_now = 3
        if timer == 10:
            if b < 50:
                scene sc i_1_196_3 with Dissolve(.5)
                "Victoria" "You're a little bit bellow our standart level, mister [Surname]. "
                show sc i_1_196_3 with my_dissolve
                "[Name]" "(....Shit.)"
                show sc i_1_196_3 with my_dissolve
                "[Name]" "(I was so close. Is this... the end?)"
                show sc i_1_196_6 with my_dissolve
                "Victoria" "But you've still managed to form a solid glyph for an entrant."
                show sc i_1_196_7 with my_dissolve
                "#нет 1_196_7"
                "[Name]" "Does this mean...?"
                show sc i_1_196_7 with my_dissolve
                "Victoria" "Yes, but if you want to stay at this school, you'll have to show a special zeal for your studies."
                show sc i_1_196_7 with my_dissolve
                "Victoria" "You're enrolled."
                show sc i_1_196_7 with my_dissolve
                "Victoria" "For now."
                show sc i_1_196_7 with my_dissolve
                "Victoria" "But you'll have to show a special zeal for your studies."
                show sc i_1_196_7 with my_dissolve
                "Victoria" "If you want to stay at this academy."
                show sc i_1_196_7 with my_dissolve
                "[Name]" "I do."
                show sc i_1_196_7 with my_dissolve
                "[Name]" "I mean... I will. A special zeal from now on!"
                show sc i_1_196_7 with my_dissolve
                "[Name]" "Thank you!"
                scene sc i_1_196_7
                hide screen MagicMiniGameScreen
                hide screen m_line_max_screen 
                with Dissolve(.5)
            elif True:
                scene sc i_1_196_4 with Dissolve(.5)
                "Victoria" "Well..."
                show sc i_1_196_4 with my_dissolve
                "Victoria" "At least you achieved some result."
                show sc i_1_196_4 with my_dissolve
                "[Name]" "(Does this mean...?)"
                show sc i_1_196_6 with my_dissolve
                "Victoria" "You're enrolled."
                show sc i_1_196_6 with my_dissolve
                "Victoria" "For now."
                show sc i_1_196_6 with my_dissolve
                "Victoria" "But you'll have to show a special zeal for your studies."
                show sc i_1_196_6 with my_dissolve
                "Victoria" "If you want to stay at this academy."
                show sc i_1_196_6 with my_dissolve
                "[Name]" "I do."
                show sc i_1_196_6 with my_dissolve
                "[Name]" "I mean... I will. A special zeal from now on!"
                show sc i_1_196_6 with my_dissolve
                "[Name]" "Thank you!"
                scene sc i_1_196_6
                hide screen MagicMiniGameScreen
                hide screen m_line_max_screen 
                with Dissolve(.5)
        elif timer == 7:
            if b < 75:
                scene sc i_1_196_4 with Dissolve(.5)
                "Victoria" "Well..."
                show sc i_1_196_4 with my_dissolve
                "Victoria" "At least you achieved some result."
                show sc i_1_196_4 with my_dissolve
                "[Name]" "(Does this mean...?)"
                show sc i_1_196_6 with my_dissolve
                "Victoria" "You're enrolled."
                show sc i_1_196_6 with my_dissolve
                "Victoria" "For now."
                show sc i_1_196_6 with my_dissolve
                "Victoria" "But you'll have to show a special zeal for your studies."
                show sc i_1_196_6 with my_dissolve
                "Victoria" "If you want to stay at this academy."
                show sc i_1_196_6 with my_dissolve
                "[Name]" "I do."
                show sc i_1_196_6 with my_dissolve
                "[Name]" "I mean... I will. A special zeal from now on!"
                show sc i_1_196_6 with my_dissolve
                "[Name]" "Thank you!"
            elif True:

                scene sc i_1_196_5 with Dissolve(.5)
                "Victoria" "Congratulations, Mr. [Surname]! "
                show sc i_1_196_5 with my_dissolve
                "Victoria" "You have passed this exam. "
                show sc i_1_196_5 with my_dissolve
                "Victoria" "You have good potential! "
                show sc i_1_196_5 with my_dissolve
                "Victoria" "Someday you may even become a worthy wizard!"
                show sc i_1_196_5 with my_dissolve
                "[Name]" "Thank you, miss Lapis!"
                show sc i_1_196_5 with my_dissolve
                "[Name]" "I won't dissapoint you!"
        elif True:




            if b < 90:

                scene sc i_1_196_5 with Dissolve(.5)
                "Victoria" "Don't feel bad, Mr. [Surname]. "
                show sc i_1_196_5 with my_dissolve
                "Victoria" "I see such results on this test very rarely."
                show sc i_1_196_5 with my_dissolve
                "[Name]" "Was it that bad?"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "On the contrary!"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "A very decent result. But I think you can do better!"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "You're accepted. "
                show sc i_1_196_5 with my_dissolve
                "Victoria" "You'll need a lot of practice to get even better."
                show sc i_1_196_5 with my_dissolve
                "[Name]" "I'm looking forward to it!"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "Nice zeal, don't lose it!"
            elif True:

                scene sc i_1_196_6 with Dissolve(.5)
                "Victoria" "Great result, [Name]! "
                show sc i_1_196_6 with my_dissolve
                "Victoria" "You are definitely accepted!"
                show sc i_1_196_6 with my_dissolve
                "Victoria" "You have a great future ahead of you. "
                show sc i_1_196_6 with my_dissolve
                "Victoria" "And I will do my best to help you reach your potential!"
                show sc i_1_196_6 with my_dissolve
                "[Name]" "Thank you, miss Lapis!"
                show sc i_1_196_6 with my_dissolve
                "[Name]" "That's an honor to hear this!"
        "end demo"
        $ renpy.full_restart()
    jump MagicMiniGameLabel_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
