init python:
    class PhysicsCircle(renpy.Displayable):
        
        
        
        def __init__(self, circles = [], **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            
            self.tick_now       = None
            
            self.f_time         = None 
            self.x_0 = 500
            self.y_0 = 500
            
            self.x_1 = 500
            self.y_1 = 500
            
            self.r   = 100
            
            self.x_d = False
            self.y_d = False
            
            self.xx             = 0
            self.yy             = 0
        
        
        
        
        def render(self, width, height, st, at):
            rend = renpy.Render(1920, 1080)
            if not self.tick_now:
                
                self.tick_now = pygame.time.get_ticks()
            
            self.f_time       = pygame.time.get_ticks() - self.tick_now
            
            self.tick_now     = pygame.time.get_ticks()
            
            
            
            self.xx = renpy.get_mouse_pos()[0]
            self.yy = renpy.get_mouse_pos()[1]
            
            
            
            
            
            
            
            rend.blit(
                renpy.render(

                    AlphaMask(
                    Crop(
                        (self.x_1, self.y_0, 500, self.r*2), 'glyph_3_and_bg'), 'mini_games/magic/circle_white_5.png')
                    , 1920, 1080, 0.3, at), (self.x_1, self.y_0,))
            
            
            rend.blit(renpy.render(




                AlphaMask(
                    Crop(
                        (self.xx-75, self.yy-75, 500, 140), 'glyph_3_and_bg'), Transform('mini_games/magic/circle_white_4.png'
                        )), 1920, 1080, 0.3, at), (self.xx-75, self.yy-75,))  
            
            
            
            
            
            
            
            
            inside0 = (self.yy < self.y_0+self.r*2 and self.yy > self.y_0)
            inside1 = (self.xx < self.x_1+self.r*2 and self.xx > self.x_1)
            insidem = not ((self.r**2 - ((self.x_1+self.r-self.xx)**2 + (self.y_0+self.r-self.yy)**2)<0))
            
            rend.blit(renpy.render(Text(str(inside0), color = '#FFF'), 1920, 1080, 0.3, at), (0, 0,))
            rend.blit(renpy.render(Text(str(inside1), color = '#FFF'), 1920, 1080, 0.3, at), (0, 100,))
            rend.blit(renpy.render(Text(str(insidem), color = '#FFF'), 1920, 1080, 0.3, at), (0, 200,))
            
            if not inside0:
                
                self.y_d = False
                self.x_d = False
                if self.yy <= self.y_0:
                    self.y_0 = self.yy-1
                
                elif self.yy > self.y_0:
                    self.y_0 = self.yy-self.r*2
            
            if not inside1:
                
                self.y_d = False
                self.x_d = False
                if self.xx <= self.x_1:
                    self.x_1 = self.xx-1
                
                elif self.xx > self.x_1:
                    self.x_1 = self.xx-self.r*2
            
            
            
            renpy.redraw(self, 0)
            return rend
        
        
        def get_pixels(self, x, y):
            
            xv0 = 0
            xv1 = 0
            
            yv0 = 0
            yv1 = 0
            
            for i in xrange(x, 1920):
                s    = renpy.load_surface('mini_games/magic/glyph_3_line.png').get_at([x, y])
                xv0 += 0
                if s != 0:
                    break
            for i in xrange(x, 1920):
                s    = renpy.load_surface('mini_games/magic/glyph_3_line.png').get_at([x+xv0, y])
                xv0 += 0
                if s != 0:
                    break
            for i in range(0, x)[::-1]:
                s    = renpy.load_surface('mini_games/magic/glyph_3_line.png').get_at([x-xv1, y])
                xv1 += 0
                if s != 0:
                    break
            
            
            for i in xrange(y, 1080):
                s    = renpy.load_surface('mini_games/magic/glyph_3_line.png').get_at([x, y+yv0])
                yv0 += 0
                if s != 0:
                    break
            for i in range(0, y)[::-1]:
                s    = renpy.load_surface('mini_games/magic/glyph_3_line.png').get_at([x, y-yv1])
                yv1 += 0
                if s != 0:
                    break
            
            
            
            return 



screen PhysicsCircleScreen:
    add 'glyph_3_and_bg' alpha .5
    add PhysicsCircle()

label TestPhysicsCircle:
    call screen PhysicsCircleScreen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
