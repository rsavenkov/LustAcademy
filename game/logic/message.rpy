init python:

    MessageEXMP = []
    def check_MessageEXMP_none():
        global MessageEXMP
        for i in MessageEXMP:
            if i.time <= 0:
                i.block = True
            if not i.block:
                return None
        MessageEXMP = []

    def ShowMessage(text, show_screen = True):
        renpy.play(channel = 'sound_message', filename = 'audio_ep2/Gameplay/snd_quest_completed2.mp3')
        global MessageEXMP
        check_MessageEXMP_none()
        if text not in ('0.0', '0', '-0' '+0', '-0.0' '+0.0'): 
            
            
            
            
            
            
            
            
            if '\n' in text:
                mes                   = Message(text) 
                mes_MessageText_split = mes.MessageText.split('\n')
                time_factor = float(get_max_size(mes_MessageText_split))/16
            else:
                time_factor = 1
            MessageEXMP.append(Message(text, time_factor = time_factor))
        
        
        
        if show_screen:
            renpy.show_screen('show_message_info_screen')

    def get_size(displayable, x = 0, y = 0):
        return renpy.render(renpy.easy.displayable(displayable), x, y, 0, 0).get_size()


    class Message(renpy.Displayable):
        
        def __init__(self, text, speed = 100, time = 500, line = True, time_factor = 2, **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            self.oldst = None 
            
            self.MessageText = text
            if not time_factor:
                time_factor  = 1
            self.time        = int(8*time_factor)
            self.time_max    = int(8*time_factor)
            self.time_next   = None
            self.block       = False
        
        
        
        def render(self, width, height, st, at):
            
            global MessageEXMP
            rend = renpy.Render(45, 45)
            if self.time_next == None:
                
                self.time_next  = datetime.datetime.today() + datetime.timedelta(seconds=1)
            
            if datetime.datetime.today() >= self.time_next: 
                
                self.time -= 1
                
                self.time_next = None
                
                renpy.restart_interaction()
            if self.time <= 0:
                if self in MessageEXMP:
                    self.block = True
            
            
            
            
            
            renpy.redraw(self, 0)
            
            return rend
    def tmp_transform_func(trans, st, at):
        return None




    def get_max_size(array):
        max_size = 0
        for i in array:
            if len(i) > max_size:
                max_size = len(i)
        return max_size
transform informer_transform(yp=70):

    xalign 1.5 ypos yp
    linear 1.0 xalign 1.0
    pause 5
    linear 1.0 xalign 1.5



screen show_message_info_screen:

    zorder 300
    if not persistent.from_gallery:
        for i in xrange(len(MessageEXMP)):
            if i < len(MessageEXMP):
                $ mes = MessageEXMP[i]
                add mes
                if mes.time<= 0:
                    $ check_MessageEXMP_none()
                if not mes.block and mes.time > 2:


                    if type(mes.MessageText) == type('!'):
                        if '\n' in mes.MessageText:
                            $ mes_MessageText_split = mes.MessageText.split('\n')
                            vbox:
                                at informer_transform(yp=(i+2)*60)

                                for x in mes_MessageText_split:
                                    if len(x):
                                        viewport:
                                            ymaximum 30
                                            xmaximum int(get_max_size(mes_MessageText_split)*15.7)
                                            #add '#000a'
                                            image 'message_bg'
                                            text x size 14 font 'fonts/h_font.ttf' xalign .5 yalign .5

                        else:
                            viewport:
                                at informer_transform(yp=(i+2)*60)
                                ymaximum 30
                                if len(mes.MessageText) < 22:
                                    xmaximum 150

                                else:
                                    if '{image=' in mes.MessageText:
                                        xmaximum 250
                                    else:
                                        xmaximum 200
                                image 'message_bg'
                                #add '#000a'





                                text mes.MessageText size 14 font 'fonts/h_font.ttf' xalign .5 yalign .5
                    else:
                        viewport:
                            at informer_transform(yp=(i+2)*60)
                            ymaximum 30

                            xmaximum 250

                            image 'message_bg'
                            #add '#000a'





                            add mes.MessageText[0] yalign .5 xpos 15
                            text mes.MessageText[1] size 14 font 'fonts/h_font.ttf' xalign .5 yalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
