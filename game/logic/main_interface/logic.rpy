transform text_animation_up_down(x_start, y_start, shift_y):
    xpos x_start
    ypos y_start
    on show:
        linear .2 xpos x_start ypos shift_y alpha 1.0
    on hide:
        linear .2 xpos x_start ypos y_start alpha 0.0


screen text_animation_up_screen_duel(text_now, x_now, y_now, c_color='#FFE2B6'):
    $ btns = 'mini_games/duels/'
    zorder 220
    viewport:
        xmaximum 390
        ymaximum 100


        add btns+'inform_bg.png'
        text unicode(text_now):



            color c_color
            font 'fonts/h_font.ttf'
            size 67

            xalign .5 yalign .5

        at text_animation_up_down(x_now-20, y_now, y_now-50)

screen text_animation_up_screen(text_now, x_now, y_now):
    $ btns = 'images/main_menu/buttons/'
    zorder 220
    viewport:
        xmaximum 300
        ymaximum 30


        add btns+'hover_3.png' zoom 1
        text unicode(text_now):



            color "#FFEEDE"
            font 'fonts/h_font.ttf'
            size 18

            xalign .5 yalign .35

        at text_animation_up_down(x_now-20-40, y_now, y_now-30)


screen text_animation_up_screen_3(text_now, x_now, y_now):
    zorder 220
    $ btns = 'images/main_menu/buttons/'
    viewport:
        xmaximum 125
        ymaximum 30


        add btns+'hover_4.png'
        text unicode(text_now):



            color "#fff"
            font 'fonts/h_font.ttf'
            size 15

            xalign .5 yalign .5
        xpos x_now-20
        ypos y_now-50


screen text_animation_up_screen_2(text_now, x_now, y_now):
    zorder 200
    $ btns = 'images/main_menu/buttons/'
    viewport:
        xmaximum 125
        ymaximum 30


        add btns+'hover_4.png'
        text unicode(text_now):



            color "#fff"
            font 'fonts/h_font.ttf'
            size 15

            xalign .5 yalign .5

        at text_animation_up_down(x_now-20, y_now, y_now-50)

init -1000 python:


    def generate_books():
        global books_now
        books_now = {}
        x = books_list_1.keys()
        
        v = renpy.random.choice(x)
        
        x.remove(v)
        books_now.update({v:renpy.random.randint(0, books_list_1[v]-1)})
        
        x = books_list_1.keys()
        v = renpy.random.choice(x)
        x.remove(v)
        books_now.update({v:renpy.random.randint(0, books_list_1[v]-1)})
        
        x = books_list_2.keys()
        v = renpy.random.choice(x)
        x.remove(v)
        books_now.update({v:renpy.random.randint(0, books_list_2[v]-1)})


    books_list_1 = {


    
    'cord_garden_c' : 3,
    'cord_garden_l' : 6,
    'cord_garden_r' : 5,
    'cord_class_1'  : 7,
    'cord_class_2'  : 3,

    'cord_mainhall' : 9,
    'cord_caffe'    : 5,
    }

    books_list_2 = {


    'leon_living'   : 7,

    'leon_bathroom' : 3,





    }

    def show_up_donw_text_duel(text_now, x_now, y_now, curs = True, screen_2=False, c_color = '#FFE2B6'):
        global config
        
        Hide('text_animation_up_screen_duel')()
        
        if curs:
            config.mouse = cursor_dop
        
        Show('text_animation_up_screen_duel', text_now = text_now, x_now = x_now, y_now = y_now, c_color = c_color)()




    def show_up_donw_text(text_now, x_now, y_now, curs = True, screen_2=False):
        global config
        Hide('text_animation_up_screen_2')()
        Hide('text_animation_up_screen_3')()
        
        Hide('text_animation_up_screen')()
        
        if curs:
            config.mouse = cursor_dop
        if screen_2:
            Show('text_animation_up_screen_2', text_now = text_now, x_now = x_now, y_now = y_now)()
        
        else:
            Show('text_animation_up_screen', text_now = text_now, x_now = x_now, y_now = y_now)()

    def set_mouse_to_default():
        config.mouse = None
        config.mouse = None



    def get_images_list(path):
        rtrn_list = list()
        for fn in renpy.list_files():
            if fn.startswith(path) and (fn.endswith((".png")) or fn.endswith((".jpg"))):    
                rtrn_list.append(fn)
        return rtrn_list


    locations_path = 'images/locations_main/location_buttons/'
    class Location():
        def __init__(self, name, path, cor_x, zoom = 1.0, yalign = .5):
            self.name       = name
            self.image      = 'images/locations_main/location_buttons/' + path + '.png'
            self.image_gold = 'images/locations_main/location_buttons/' + path + '_gold.png'
            self.image_name = path
            self.cor_x      = cor_x
            self.zoom       = zoom
            self.yalign     = yalign
            self.path       = path





    locations = []

    locations.append(Location(_('My Bedroom'),       'gg_room',      0))
    locations.append(Location(_('Corridor'),           'corridor',     70, .99, .51))
    locations.append(Location(_("Olivia's Bedroom"), 'parents_room', 170))
    locations.append(Location(_("Ashley's Bedroom"),      'ashlie_room',  280))
    locations.append(Location(_('Bathroom'),    'bath',         370))



    locations_academy = []

    locations_campus  = []

    locations_dale    = []

    locations_dale.append(Location(_('Mainstreet'),    'dale_mainstreet',  20))
    locations_dale.append(Location(_('Spa'),           'dale_spa',         100))
    locations_dale.append(Location(_("Hotel"),         'dale_hotel',       180))
    locations_dale.append(Location(_("Shop"),          'dale_shop',        260))
    locations_dale.append(Location(_('Club Enter'),          'dale_clubenter',        340))



    locations = locations_academy


    locations_academy.append(Location(_("Entrance"),     'cord_entrance',  20))
    locations_academy.append(Location(_("Inner Garden"),  'cord_garden_c', 100))
    locations_academy.append(Location(_("Left Wing"), 'cord_garden_l',  180))
    locations_academy.append(Location(_("Right Wing"), 'cord_garden_r',  260))
    locations_academy.append(Location(_("Classroom 1"),      'cord_class_1',   340))
    locations_academy.append(Location(_("Classroom 2"),      'cord_class_2',   420))
    locations_academy.append(Location(_("Library"),      'cord_library',   500))
    locations_academy.append(Location(_("Main Hall"),    'cord_mainhall',  580))
    locations_academy.append(Location(_("Cafe"),        'cord_caffe',     660))    




    locations_campus.append(Location(_("My Room"),  'leon_room_mc',   20))
    locations_campus.append(Location(_("Corridor"), 'leon_corridor',  100))
    locations_campus.append(Location(_("Living Room"), 'leon_living', 180))
    locations_campus.append(Location(_("Bathroom"), 'leon_bathroom',  260))


    locations_campus.append(Location(_("Girls Room 1"), 'leon_room_hl', 340))

    locations_campus.append(Location(_("Girls Room 2"), 'leon_room_sa', 420))





    class_plus = 0
    win        = None
    lose       = None

    def change_location(location, time = None, plus = False, jump = True, up_points_0 = 0, up_points = 0):
        
        global location_now, old_location, time_now, day_now, dow, homes, class_plus, win, lose, tmp_events
        global locations_now, locations_academy, locations_campus, homes, picture_in_mc_room_variable, rune_in_mc_room_variable
        global wins_house
        if up_points and up_points_0 != up_points:
            
            set_points_times([i for i in xrange(up_points_0, up_points)])
        if time is None:
            time = time_now
        old_location = copy.copy(location_now)
        location_now = location
        
        stt = 0
        if 'cafe' in location and 'dale' not in location_now:
            locations_now = copy.copy(locations_academy)
                
        else:
            for i in locations_academy:
                if i.path == location:
                    locations_now = copy.copy(locations_academy)
                    
                    stt = 1
                    break
            
            if not stt:
                for i in locations_campus:
                    if i.path == location:
                        locations_now = copy.copy(locations_campus)
                        
                        break
            for event in events:
                if events[event].check():
                    events[event].complete = True
                    Jump(events[event].label)()
        
        
        if time != 5:
            if time_now != time:
                if hasattr(store, 'picture_in_mc_room_variable'):
                    del picture_in_mc_room_variable
                if hasattr(store, 'rune_in_mc_room_variable'):
                    del rune_in_mc_room_variable
            time_now     = time
            if 'dale' in location_now and dow == 'SUN':
                if time_now == 3:
                    renpy.jump('escape_from_dale')
        else:
            time_now     = 1
            day_now     += 1
            if 'dale' in location_now and dow == 'SAT':
                dow = 'SUN'
                
                day_now-=day_now%7
            else:
                if day_now%7 == 1:
                    dow = 'MON'
                    
                    homes = {

                    'Leonheart' :{'now':0, 'new':0, 'add':0},
                    'Adderin'   :{'now':0, 'new':0, 'add':0},
                    'Crowhive'  :{'now':0, 'new':0, 'add':0},
                    'Martenden' :{'now':0, 'new':0, 'add':0},

                    }
                    if 'dale' in location_now:
                        renpy.jump('escape_from_dale')
                    
                
                if day_now%7 == 2:
                    dow = 'TUE'
                
                if day_now%7 == 3:
                    dow =  'WED'
                
                if day_now%7 == 4:
                    dow = 'THUR'
                
                if day_now%7 == 5:
                    dow = 'FRI'
                
                if day_now%7 == 6:
                    day_now += 2
                    dow = 'MON'
                    
                    wins_house = get_all_collest_home()
                    homes = {

                    'Leonheart' :{'now':0, 'new':0, 'add':0},
                    'Adderin'   :{'now':0, 'new':0, 'add':0},
                    'Crowhive'  :{'now':0, 'new':0, 'add':0},
                    'Martenden' :{'now':0, 'new':0, 'add':0},

                    }
                    if 'dale' in location_now:
                        renpy.jump('escape_from_dale')

                    #if not hasattr(store, 'check_arthur_2'): 
                    Jump('arthur_2')()
                    return 'add'
                if day_now%7 == 0:
                    dow = 'MON'
                    wins_house = get_all_collest_home()
                    homes = {

                    'Leonheart' :{'now':0, 'new':0, 'add':0},
                    'Adderin'   :{'now':0, 'new':0, 'add':0},
                    'Crowhive'  :{'now':0, 'new':0, 'add':0},
                    'Martenden' :{'now':0, 'new':0, 'add':0},

                    }
            
        if jump:
            Jump('change_location_label')()
    def set_points_times(time):
        for i in time:
            if i in [1, 2]:
                set_points_home(13, 20, 15, 25)
            elif i == 3:
                set_points_home(13, 20, 15, 25)
            elif i == 4:
                set_points_home(3, 7, 4, 10)
    def change_location_2(location, time, plus=False, caffe = False, sleep = False):
        global location_now, old_location, time_now, day_now, dow, homes, class_plus, win, lose, qstt_location
        global picture_in_mc_room_variable, rune_in_mc_room_variable
        if 'dale' in location and time == 5:
            location = 'dale_hotel'
        if sleep:
            
            if hasattr(store, 'picture_in_mc_room_variable'):
                del picture_in_mc_room_variable
            if hasattr(store, 'rune_in_mc_room_variable'):
                del rune_in_mc_room_variable
        change_location(location, time, jump = False)
        for i in homes:
            homes[i]['add'] = 0
        if plus:
            if homes.get(win) and caffe:
                homes[win]['add']  += 3
                rtmps = 3
            
            elif homes.get(win) and not homes.get(lose):
                homes[win]['add']  += 5
                rtmps = 5
            
            elif homes.get(win):
                homes[win]['add']  += 3
                rtmps = 3
            ShowMessage(['images/'+win.lower()+'_mini.png', win.title()+' points {color=#0F0}{b}+'+str(rtmps)+'{/color}{/b}'])
            
            if homes.get(lose):
                homes[lose]['add'] -= 3
                rtmps = 3
                ShowMessage(['images/'+lose.lower()+'_mini.png', lose.title()+' points {color=#F00}{b}-'+str(rtmps)+'{/color}{/b}'])
        
        
        
        
        
        
        if time_now == 1:
            
            
            
            generate_books()
            if sleep:
                Jump('sleep_events')()
        
        
        if day_now%7  == 1 and time_now == 1:
            
            lose  = None
            win   = None
            homes = {

    'Leonheart' :{'now':0, 'new':0, 'add':0},
    'Adderin'   :{'now':0, 'new':0, 'add':0},
    'Crowhive'  :{'now':0, 'new':0, 'add':0},
    'Martenden' :{'now':0, 'new':0, 'add':0},

    }
        if day_now%7 not in [6, 0]:
            if time_now == 1:
                for i in ('Leonheart', 'Adderin', 'Crowhive', 'Martenden'):
                    
                    homes[i]['new']  = 0
            if time_now == 2:
                set_points_home(13, 20, 15, 25)
            if time_now == 3:
                set_points_home(13, 20, 15, 25)
            if time_now == 4:
                set_points_home(3, 7, 4, 10)
        
        
        
        
        if hasattr(store, 'qstt_location') and qstt_location != 0:
            location_now  = qstt_location
            qstt_location = 0
        Jump('change_location_label')()
    def get_all_collest_home():
        
        for i in homes:
            if homes[i]['now'] == get_collest_home():
                return i
        return 'Leonheart'
    def get_collest_home():
        max = 0
        
        for i in homes:
            if homes[i]['now'] >= max:
                max = homes[i]['now']
        
        
        return max
    def set_points_home(l_0, l_1, o_0, o_1):
        
        news = renpy.random.randint(l_0, l_1)
        homes['Leonheart']['now'] += news+homes['Leonheart']['add']
        homes['Leonheart']['new']  = news
        for i in ('Adderin', 'Crowhive', 'Martenden'):
            news = renpy.random.randint(o_0, o_1)
            homes[i]['now'] += news+homes[i]['add']
            homes[i]['new']  = news

    def check_events():
        for event in events:
            ev = events[event]
            if ev.check():
                if not ev.repeat:
                    ev.complete = True
                Jump(ev.label)()
    def jump_to_event(event, check_location = True, check_time = True):
        if events.get(event):
            ev = events[event]
        else:
            return 'Error 1'
        if ev.check(check_location, check_time):
            if not ev.repeat:
                ev.complete = True
            Jump(ev.label)()
        return 'Error 2'

    def get_location_for_quest_log(event):
        if events.get(event):
            if events[event].location is not None:
                return events[event].location
        return location_now


init -100 python:
    def set_locations(loc = 'academy'):
        global location_now, locations_now, locations_academy, locations_campus
        Hide('main_interface')()
        
        if loc == 'academy':
            
            if (locations_now[0] != locations_academy[0]) or ('dale' in location_now):
                locations_now = copy.copy(locations_academy)
                location_now  = 'cord_entrance'
        else:   
            if (locations_now[0] != locations_campus[0]) or ('dale' in location_now):
                
                location_now  = 'leon_living'
                locations_now = copy.copy(locations_campus)
        Hide('map_screen', transition = Dissolve(.5))()
        renpy.jump('main_interface_label')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
