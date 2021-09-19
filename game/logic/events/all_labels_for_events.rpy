init -100 python:
    hotspots = {
    'cord_class_1':{
    'haley_cord_class_1_':[1350, 485, 250, 400], 
    'lily_cord_class_1_':[460, 500, 200, 300], 
    'naomi_cord_class_1_':[1100, 430, 220, 400], 
    'victoria_cord_class_1_':[650, 300, 180, 350],
    'door': [1665, 150, 200, 430]
    },

    'cord_class_2':{
    'sabrina':[1550,540,330,400],
    'door'   :[1230,290,130,230],
    'haley'  : [940, 420, 150, 330],
    'lily'   : [480, 500, 130, 170],
    'naomi'  : [140, 420, 150, 440],
    },

    'leon_living':{
    'door_1'   :[1170, 150, 100, 300],
    'door_2'   :[1105, 150, 60, 300],
    'door_3'   :[50, 0, 150, 510],
    'stairs'   :[460, 0, 640, 420],
    'samantha_3':[540, 420, 160, 300],
    'audrey_3'  :[700, 420, 160, 300],
    'samantha_1':[500, 400, 260, 390],
    'audrey_1'  :[880, 200, 120, 260],
    'elijah_1'  :[1580, 200, 200, 450],

    },


    'leon_corridor':{

    'door_1'     :[100, 15, 420, 770],
    'door_2'     :[785, 80, 150, 500],
    'door_3'     :[1170, 95, 250, 450],
    'stairs'     :[1100, 800, 700, 280],

    },

    'leon_room_mc':{

    'door_1'     :[67, 250, 300, 555],
    'door_2'     :[1534, 235, 365, 715],
    'picture'    :[600, 170, 400, 260],
    'rune'       :[1575, 0, 310, 235],
    'bed'        :[655, 525, 620, 275],
    },


    'dale_mainstreet' : {


'door_hotel':[168, 350, 180, 350],
'door_shop' :[1025, 435, 100, 240],
'door_spa'  :[1550, 462, 250, 170],
'sign_shop' :[885, 350, 135, 100],
'sign_spa'  :[1560, 350, 250, 100],
'sign_hotel':[340, 365, 150, 100],


    },


    'dale_hotel' : {


'door':[1600, 200, 320, 880],
'mina':[390, 310, 215, 315],


    },


    

    'dale_shop' : {


'door'  :[0, 230, 155, 850],
'gordon':[770, 470, 160, 125],


    },


'dale_spa' : {


'door'  :[1680, 0, 240, 1080],
'faith' :[640, 170, 175, 230],


    },


    
    
    

    }

    def get_size(displayable, x = 0, y = 0):
        return renpy.render(renpy.easy.displayable(displayable), x, y, 0, 0).get_size()
    class CorsOnMouse(renpy.Displayable):
        
        
        
        
        def __init__(self, shift_x = 0, shift_y = 0, **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            
            
            self.shift_x  = shift_x
            self.shift_y  = shift_y 
            self.next_time_for_TextOnScreen = 0
            self.f_time   = None 
            self.tick_now = None
        
        def render(self, width, height, st, at):
            
            
            rend = renpy.Render(1920, 1080)
            if renpy.get_mouse_pos()[0]+self.shift_x+220 > 1920:
                self.shift_x = self.shift_x - (1920 - renpy.get_mouse_pos()[0]+self.shift_x+220) 
            
            
            rend.blit(
                    renpy.render(
                        Text(unicode(renpy.get_mouse_pos()[0]) + ',' + unicode(renpy.get_mouse_pos()[1]), outlines = [(3, "#000", 0, 0)]),
                        500, 140, st, at),
                        (renpy.get_mouse_pos()[0]+self.shift_x+30, renpy.get_mouse_pos()[1]+self.shift_y))
            
            
            renpy.redraw(self, 0)
            
            return rend

init python:
    def set_stubs(s_list, event):
        global wakeup_sets
        s_list.append(event)
        wakeup_sets.append([s_list, event])
    def time_up():
        change_location_2(location_now, time_now+1)


label all_events_up_variables:
    $ setattr(store, 
        tmp_variable_up_now, 
            getattr(store, 'tmp_variable_up_now')+1)

    $ log_message.update({tmp_QLOG_all[0]:tmp_QLOG_all[1]})

    return
label exit_from_event:
    $ lose = None
    $ win  = 'Leonheart'
    $ change_location_2(location_now, time_now+1, plus = True)


    hide screen black_tmp_screen_menu


    jump main_interface_label


label hide_all_main_interfaces:


    #hide screen show_hide_locations
    #hide screen show_hide_locations_2
    
    hide screen text_animation_up_screen
    hide screen text_animation_up_screen_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu


    hide expression '#000'


    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
