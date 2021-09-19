image warning_icon:



    'images/mini_games/magic/mouse_star.png' with Dissolve(.5)

    pause .5

    Transform('images/mini_games/magic/mouse_star.png', alpha = .5) with Dissolve(.5)

    pause .5

    repeat

image glyph_3_and_bg = LiveComposite(
    (1920, 1080),
    (0, 0), 'prologue/19-32/1_196_8.webp',
    (0, 0), 'mini_games/magic/glyph_3_bg.png',
    
    (0, 0), 'mini_games/magic/glyph_3.png',
    )

init -100 python:
    class MagicMiniGame_3(renpy.Displayable):
        
        
        
        def __init__(self, circles = [], **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            
            self.tick_now       = None
            
            self.f_time         = None 
            self.crop_y         = 0
            self.crop_x         = 0
            self.circles        = []
            self.click          = False
            
            self.time           = 7
            self.minus_x        = 120
            self.minus_y        = 20
            self.time_next      = None
            
            self.xx             = 0
            self.yy             = 0
            
            self.x_zoom         = 1.0
            self.y_zoom         = 1.2
            
            
            self.points         = [
            {'x':970,  'y':740,  'n':('<', '!'), 'x_m':130, 'y_m':20, 'y_zoom' : 1, 'x_zoom':1 }, 
            {'x':680,  'y':600,  'n':('!', '<'), 'x_m':140, 'y_m':30, 'y_zoom' : 1, 'x_zoom':1 }, 
            {'x':930,  'y':260,  'n':('>', '!'), 'x_m':140, 'y_m':20, 'y_zoom' : 1.5, 'x_zoom':1 }, 
            {'x':1120, 'y':320, 'n':('!', '>'), 'x_m':50,  'y_m':20,  'y_zoom' : 1, 'x_zoom':1 }]
            
            self.blocks         = [
            {
            'x0':970, 
            'y0':400, 
            'x1':1122-970, 
            'y1':815-400,
            'crop_x_n' : '!',
            'crop_x'   : 0,
            'crop_y_n' : 'down', 
            'crop_y'   : 0,
            },

            {
            'x0':910, 
            'y0':800, 
            'x1':-350, 
            'y1':-220,
            'crop_x_n' : 'left',
            'crop_x'   : 0,
            'crop_y_n' : '!', 
            'crop_y'   : 0,
            },

            {
            'x0':910, 
            'y0':570, 
            'x1':-300, 
            'y1':230,
            'crop_x_n' : 'left',
            'crop_x'   : 0,
            'crop_y_n' : '!', 
            'crop_y'   : 0,
            },

            {
            'x0':910, 
            'y0':570, 
            'x1':-300, 
            'y1':230,
            'crop_x_n' : 'left',
            'crop_y'   : 0,            
            'crop_y_n' : '!', 
            'crop_y'   : 0,
            }

            ]
            self.point_now      = 0
        
        
        
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
            
            
            
            
            
            
            
            self.xx = renpy.get_mouse_pos()[0]
            self.yy = renpy.get_mouse_pos()[1]
            
            
            rend.blit(renpy.render(Image('images/mini_games/magic/time_line.png'), 1920, 1080, 0.3, at), (500, 50,))
            rend.blit(renpy.render(Crop((0, 0, int(((float(self.time)/7.0) )*922), 142), 'images/mini_games/magic/time_line_2.png'), 1920, 1080, 0.3, at), (500, 50,))
            
            
            
            
            
            
            
            rend.blit(renpy.render(Text(str(self.xx)), 1920, 1080, 0.3, at), (0, 100,))
            rend.blit(renpy.render(Text(str(renpy.get_mouse_pos()[0] > 1000 and  renpy.get_mouse_pos()[1] > 420 and renpy.get_mouse_pos()[1] < 500 and renpy.get_mouse_pos()[0] < 1075)), 1920, 1080, 0.3, at), (0, 200,))
            rend.blit(renpy.render(Text(str(self.yy)), 1920, 1080, 0.3, at), (0, 300,))
            if self.click:
                if self.point_now < len(self.points):
                    rend.blit(renpy.render(Text(str(self.check_points())), 1920, 1080, 0.3, at), (0, 400,))
                rend.blit(renpy.render(Text(str(self.point_now)), 1920, 1080, 0.3, at), (0, 500,))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            for i in self.points:
                
                rend.blit(renpy.render(Text('x'), 1920, 1080, 0.3, at), (i['x'], i['y'],))
            
            
            
            if return_lose and self.click:
                self.end_interaction()
            
            
            
            
            rend.blit(renpy.render(Crop((
                self.blocks[self.point_now]['x0'], 
                self.blocks[self.point_now]['y0'], 
                self.get_crop('x'), 
                self.get_crop('y')
                ), 

                'mini_games/magic/glyph_3.png'), 1920, 1080, 0.3, at), (self.blocks[self.point_now]['x0'], self.blocks[self.point_now]['y0'],))
            
            
            
            
            
            if self.click:
                rend.blit(renpy.render(




                AlphaMask(
                    Crop(
                        (self.xx-75, self.yy-75, 500, 140), 'glyph_3_and_bg'), Transform('mini_games/magic/circle_white_4.png'
                        )), 1920, 1080, 0.3, at), (self.xx-75, self.yy-75,))  
                
                
                
                
                
                if 1000 - self.yy > self.crop_y:
                    self.crop_y = (1000 - self.yy)
            
            
            
            
            
            
            
            renpy.redraw(self, 0)
            return rend
        
        def get_crop(self, w):
            if w == 'x':
                if self.blocks[self.point_now]['crop_x_n'] == '!':
                    return self.blocks[self.point_now]['x1']
                elif self.blocks[self.point_now]['crop_x_n'] == 'left':
                    return self.xx-self.blocks[self.point_now]['x0']
                elif self.blocks[self.point_now]['crop_x_n'] == 'right':
                    return self.blocks[self.point_now]['x0']-self.xx
            else:
                if self.blocks[self.point_now]['crop_y_n'] == '!':
                    return self.blocks[self.point_now]['y1']
                elif self.blocks[self.point_now]['crop_y_n'] == 'up':
                    return self.blocks[self.point_now]['y0']-self.yy
                elif self.blocks[self.point_now]['crop_y_n'] == 'down':
                    return self.yy-self.blocks[self.point_now]['y0']
            return 0
        def check_points(self):
            return_n = [False, False]
            for i in (('x', 0, self.xx), ('y', 1, self.yy)):
                if self.points[self.point_now]['n'][i[1]] != '!':
                    if self.points[self.point_now]['n'][i[1]] == '>':
                        if i[2] >= self.points[self.point_now][i[0]]:
                            return_n[i[1]] = True
                    elif self.points[self.point_now]['n'][i[1]] == '<':
                        if i[2] <= self.points[self.point_now][i[0]]:
                            return_n[i[1]] = True
                
                
                
                
                else:
                    return_n[i[1]] = True
            if all(return_n):
                self.minus_x    = self.points[self.point_now]['x_m']
                self.minus_y    = self.points[self.point_now]['y_m']
                self.x_zoom     = self.points[self.point_now]['x_zoom']
                self.y_zoom     = self.points[self.point_now]['y_zoom']
                
                self.point_now += 1
                return return_n
        def event(self, event, x, y, st):
            
            
            if True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 1:
                        if not self.click:
                            if renpy.get_mouse_pos()[0] > 1000 and  renpy.get_mouse_pos()[1] > 420 and renpy.get_mouse_pos()[1] < 500 and renpy.get_mouse_pos()[0] < 1075:
                                self.click = True
                                renpy.restart_interaction()
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.click:
                            self.end_interaction()
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



screen test_glyph_3:
    key "rollback" action NullAction()
    viewport:
        xmaximum 1920
        ymaximum 1080
        at hide_show_screen
        add '1_196_8'

        imagebutton:
            idle '#0000'
            hover '#0000'
            hovered SetVariable('return_lose', True)
            action NullAction()

        imagebutton:
            xpos 0
            ypos 0
            idle 'glyph_3_bg'
            hover 'glyph_3_bg'
            hovered SetVariable('return_lose', False)
            focus_mask True
            action NullAction()
    add mmt
    if not mmt.click:
        add 'warning_icon' xpos 990 ypos 410

    text 'Time left' size 25 font 'fonts/h_font.ttf' xalign .53 ypos 52





label MagicMiniGameLabel_3:
    scene sc i_1_196_8 with Dissolve(.5)
    $ return_lose = False
    $ mmt  = MagicMiniGame_3()
    $ test = renpy.call_screen('test_glyph_3')
    call screen test_glyph_2_result
    jump MagicMiniGameLabel_3
    $ game_now  = 1
    $ difficulty = 'Easy'
    $ timer_now = TimerClass(3)
    $ s = 2
    $ timer      = 0
    $ timer_hide = False
    $ timer     = 10
    $ timer_now = TimerClass(10)
label MagicMiniGameLabel_start_3:
    scene bg_magic_test with Dissolve(.5)
    $ unhovered_variable = 0
    $ unhovered_variable_2 = 1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
