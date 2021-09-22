
init python:
    predict_locations_final = False
    def update_p_variable(name, var):
        if getattr(store, name, None) is not None:
            #if getattr(store, name, None) == 0:
            #    ShowMessage(['images/lustogram_mini.png', '   New Profile: '+str(new_lustogram_profile)])
            if getattr(store, name, var) != var:
                setattr(store, name, var)
                ShowMessage(['images/notes_mini.png', '  New Quest: '+str(cnq)])
    def get_showing_images(): 
        img_list = [] 
        tags = renpy.get_showing_tags() 
        lst = list(tags)[0]
        if 'sc' in lst:
            
            return 'sc ' + renpy.get_attributes(lst)[0] 
        try:
            img_list = [] 
            tags = renpy.get_showing_tags() 
            lst = list(tags)[0]
            if 'image_now_preload' in lst:
                if hasattr(store, 'image_now_preload'):
                    return image_now_preload
            elif 'images/main_interface/locations/'+ str(location_now)+'.png' in list_files:
                return 'images/main_interface/locations/'+ str(location_now)+'.png'
            elif 'location_now' in lst:
                if location_now == 'cord_class_1' and  dow in ['SAT', 'SUN'] and time_now in [1, 2]:
                    
                    if 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '_s.png' in list_files:
                        
                        return 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '_s.png'
                else:
                    if 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png' in list_files:
                        return 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png'
                return list(tags)[0]
            elif 'sc' in lst:
                
                return 'sc ' + renpy.get_attributes(lst)[0] 
            else:
                if 'images/main_interface/locations/'+ str(location_now)+'.png' in list_files:
                    return 'images/main_interface/locations/'+ str(location_now)+'.png'
                if location_now == 'cord_class_1' and  dow in ['SAT', 'SUN'] and time_now in [1, 2]:
                    
                    if 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '_s.png' in list_files:
                        
                        return 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '_s.png'
                else:
                    if 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png' in list_files:
                        return 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png'
        
        
        except:
            
            if 'images/main_interface/locations/'+ str(location_now)+'.png' in list_files:
                return 'images/main_interface/locations/'+ str(location_now)+'.png'
            if location_now == 'cord_class_1' and  dow in ['SAT', 'SUN'] and time_now in [1, 2]:
                
                if 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '_s.png' in list_files:
                    
                    return 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '_s.png'
            else:
                if 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png' in list_files:
                    return 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png'
        
        
        return 'black.png'


transform sand_rotate:
    rotate 0
    linear 5 rotate 360

    repeat

screen predict_load_screen_web(show_loading = True):
    key "rollback" action NullAction()
    zorder 1100
    viewport:
        xmaximum 1920
        ymaximum 1080
        imagebutton:
            idle '#000'
            hover '#000'
            action NullAction()
        if show_loading:
            vbox:
                xalign .5
                yalign .5
                text 'Loading, please wait...' xalign .5







            #text str(var_predict_load_screen_web) size 50

            add 'images/mini_games/magic/time_line.png' xpos 500 yalign .6
            
            add Crop((0, 0, int(int((float(var_predict_load_screen_web)/float(var_predict_load_screen_web_max))*922)), 142), 'images/mini_games/magic/time_line_2.png') xpos 500 yalign .6



screen predict_load_screen:
    zorder 1000
    viewport:
        xmaximum 1920
        ymaximum 1080
        imagebutton:
            idle '#000'
            hover '#000'
            action NullAction()
        vbox:
            xalign .5
            yalign .5
            text 'Loading, please wait...' xalign .5









        add 'images/mini_games/magic/time_line.png' xpos 500 yalign .6
        if preload_time:
            add Crop((0, 0, int(int((float(140-int(len(predict_locations)*10) + (preload_time+1)*3)/140.0)*922)), 142), 'images/mini_games/magic/time_line_2.png') xpos 500 yalign .6

        else:
            add Crop((0, 0, int(int((float(140-int(len(predict_locations)*10) + 12)/140.0)*922)), 142), 'images/mini_games/magic/time_line_2.png') xpos 500 yalign .6







label after_load:
    hide screen text_animation
    hide screen text_animation_2
    hide screen text_animation_3
    $ MessageEXMP = []
    if not hasattr(store, 'p_variables'):
        $ p_variables = {
'Samantha': 1,
'Elijah':   1,
'Arthur':   1,
'Victoria': 0,
'Sabrina':  0,
'Haley':    0,
'Audrey':   0,
'Lily':     0,
'Naomi':    0,
'Amelie':   0,
'Molly':    0,
'Jacob':    0,
}
    if not hasattr(store, 'wins_house'):
        $ wins_house = 'None'


    if not hasattr(store, 'Q_Victoria'):
        $ Q_Victoria = 0
    if not hasattr(store, 'Q_Elijah'):
        $ Q_Elijah   = 0
    if not hasattr(store, 'Q_Leona'):
        $ Q_Leona    = 0
    if not hasattr(store, 'Q_Lily'):
        $ Q_Lily     = 0
    if not hasattr(store, 'Q_Haley'):
        $ Q_Haley    = 0
    if not hasattr(store, 'Q_Amelie'):
        $ Q_Amelie   = 0
    if not hasattr(store, 'Q_Samantha'):
        $ Q_Samantha = 0
    if not hasattr(store, 'Q_Jacob'):
        $ Q_Jacob    = 0
    if not hasattr(store, 'Q_Molly'):
        $ Q_Molly    = 0
    if not hasattr(store, 'Q_Naomi'):
        $ Q_Naomi    = 0
    if not hasattr(store, 'Q_Sabrina'):
        $ Q_Sabrina  = 0
    if not hasattr(store, 'Q_Audrey'):
        $ Q_Audrey   = 0















##############################
#P_ переменные
##############################
    if not hasattr(store, 'set_prst_p_variable_5'):
        python:
            set_prst_p_variable_5 = True

            for i in q_to_p:
                if hasattr(store, 'Q_'+i):
                    if getattr(store, 'Q_'+i) in q_to_p[i]:
                        p_up(i, q_to_p[i][getattr(store, 'Q_'+i)]) 


##############################
#P_ переменные
##############################






    if not hasattr(store, 'Q_Victoria_old'):
        $ Q_Victoria_old = 0
    if not hasattr(store, 'Q_Elijah_old'):
        $ Q_Elijah_old   = 0
    if not hasattr(store, 'Q_Leona_old'):
        $ Q_Leona_old    = 0
    if not hasattr(store, 'Q_Lily_old'):
        $ Q_Lily_old     = 0
    if not hasattr(store, 'Q_Haley_old'):
        $ Q_Haley_old    = 0
    if not hasattr(store, 'Q_Amelie_old'):
        $ Q_Amelie_old   = 0
    if not hasattr(store, 'Q_Samantha_old'):
        $ Q_Samantha_old = 0
    if not hasattr(store, 'Q_Jacob_old'):
        $ Q_Jacob_old    = 0
    if not hasattr(store, 'Q_Molly_old'):
        $ Q_Molly_old    = 0
    if not hasattr(store, 'Q_Naomi_old'):
        $ Q_Naomi_old    = 0
    if not hasattr(store, 'Q_Sabrina_old'):
        $ Q_Sabrina_old  = 0
    if not hasattr(store, 'Q_Audrey_old'):
        $ Q_Audrey_old   = 0


    if not hasattr(store, 'audrey_events'):
        $ audrey_events   = True
    if not hasattr(store, 'audrey_events_3'):
        $ audrey_events_3 = True
    if not hasattr(store, 'victoria_events'):
        $ victoria_events = True
    if not hasattr(store, 'elijah_events'):
        $ elijah_events   = True
    if not hasattr(store, 'victoria_events'):
        $ victoria_events = True
    if not hasattr(store, 'leona_events'):
        $ leona_events    = True
    if not hasattr(store, 'haley_events'):
        $ haley_events    = True
    if not hasattr(store, 'haley_events_2'):
        $ haley_events_2  = True
    if not hasattr(store, 'haley_events_3'):
        $ haley_events_3  = True
    if not hasattr(store, 'elijah_events_2'):
        $ elijah_events_2 = True
    if not hasattr(store, 'amelie_events'):
        $ amelie_events   = True
    if not hasattr(store, 'samantha_events'):
        $ samantha_events = True
    if not hasattr(store, 'samantha_events_3'):
        $ samantha_events_3 = True
    if not hasattr(store, 'jacob_events'):
        $ jacob_events     = True
    if not hasattr(store, 'molly_events'):
        $ molly_events     = True



    if not hasattr(store, 'naomi_events'):
        $ naomi_events     = True
    if not hasattr(store, 'naomi_event_2'):
        $ naomi_event_2    = True
    if not hasattr(store, 'naomi_events_2'):
        $ naomi_events_2   = True
    if not hasattr(store, 'naomi_events_3'):
        $ naomi_events_3   = True
    if not hasattr(store, 'sabrina_events'):
        $ sabrina_events   = True


    if not hasattr(store, 'lily_events'):
        $ lily_events      = True
    if not hasattr(store, 'lily_events_2'):
        $ lily_events_2    = True
    if not hasattr(store, 'lily_events_3'):
        $ lily_events_3    = True
    if not hasattr(store, 'lily_events_4'):
        $ lily_events_4    = True
    if not hasattr(store, 'lily_events_5'):
        $ lily_events_5    = True


    if not hasattr(store, 'audrey_events_set'):
        $ audrey_events_set       = []
    if not hasattr(store, 'lily_events_set'):
        $ lily_events_set         = []
    if not hasattr(store, 'lily_events_set_2'):
        $ lily_events_set_2       = []
    if not hasattr(store, 'lily_events_set_3'):
        $ lily_events_set_3       = []
    if not hasattr(store, 'lily_events_set_4'):
        $ lily_events_set_4       = []
    if not hasattr(store, 'lily_events_set_5'):
        $ lily_events_set_5       = []

    if not hasattr(store, 'audrey_events_set_3'):
        $ audrey_events_set_3     = []
    if not hasattr(store, 'victoria_events_set'):
        $ victoria_events_set     = []
    if not hasattr(store, 'elijah_events_set'):
        $ elijah_events_set       = []
    if not hasattr(store, 'victoria_events_set'):
        $ victoria_events_set     = []
    if not hasattr(store, 'leona_events_set'):
        $ leona_events_set        = []
    if not hasattr(store, 'haley_events_set'):
        $ haley_events_set        = []
    if not hasattr(store, 'haley_events_set_2'):
        $ haley_events_set_2      = []
    if not hasattr(store, 'haley_events_set_3'):
        $ haley_events_set_3      = []
    if not hasattr(store, 'elijah_events_set_2'):
        $ elijah_events_set_2     = []
    if not hasattr(store, 'amelie_events_set'):
        $ amelie_events_set       = []
    if not hasattr(store, 'samantha_events_set'):
        $ samantha_events_set     = []
    if not hasattr(store, 'samantha_events_set_3'):
        $ samantha_events_set_3   = []
    if not hasattr(store, 'jacob_events_set'):
        $ jacob_events_set        = []
    if not hasattr(store, 'molly_events_set'):
        $ molly_events_set        = []
    if not hasattr(store, 'naomi_events_set'):
        $ naomi_events_set        = []
    if not hasattr(store, 'naomi_events_set_2'):
        $ naomi_events_set_2      = []
    if not hasattr(store, 'naomi_events_set_3'):
        $ naomi_events_set_3      = []
    if not hasattr(store, 'sabrina_events_set'):
        $ sabrina_events_set      = []


    if not hasattr(store, 'wakeup_sets'):
        $ wakeup_sets             = []
    if not hasattr(store, 'lily_view'):
        $ lily_view     = True
    if not hasattr(store, 'lily_view_2'):
        $ lily_view_2   = True
    if not hasattr(store, 'lily_view_3'):
        $ lily_view_3   = True
    if not hasattr(store, 'lily_view_4'):
        $ lily_view_4   = None
    if not hasattr(store, 'lily_view_5'):
        $ lily_view_5   = True
    if not hasattr(store, 'audrey_view'):
        $ audrey_view   = True
    if not hasattr(store, 'audrey_view_3'):
        $ audrey_view_3 = True
    if not hasattr(store, 'victoria_view'):
        $ victoria_view = True
    if not hasattr(store, 'elijah_view'):
        $ elijah_view   = True
    if not hasattr(store, 'victoria_view'):
        $ victoria_view = True
    if not hasattr(store, 'leona_view'):
        $ leona_view    = True
    if not hasattr(store, 'haley_view_2'):
        $ haley_view_2  = True
    if not hasattr(store, 'haley_view_3'):
        $ haley_view_3  = None
    if not hasattr(store, 'elijah_view_3'):
        $ elijah_view_3 = True
    if not hasattr(store, 'amelie_view'):
        $ amelie_view   = True
    if not hasattr(store, 'samantha_view'):
        $ samantha_view = True
    if not hasattr(store, 'jacob_view'):
        $ jacob_view    = True
    if not hasattr(store, 'molly_view'):
        $ molly_view    = True
    if not hasattr(store, 'naomi_view'):
        $ naomi_view    = True
    if not hasattr(store, 'naomi_view_2'):
        $ naomi_view_2  = True
    if not hasattr(store, 'sabrina_view'):
        $ sabrina_view  = True
    if not hasattr(store, 'log_message'):
        $ log_message   = {}
    if not hasattr(store, 'show_hide_locations_pos'):

        $ show_hide_locations_pos = True

    if not hasattr(store, 'spells_up'):
        $ spells_up = {
    'Combat Bolt' : 0,
    'Incendio'    : 0,
    'Rictusempra' : 0,
    'Episkey'     : 0,
    }

    if hasattr(store, 'debug_now') and debug_now:
        return

    if not hasattr(store, 'potions'):
        $ potions               = {

    'Lesser Heal'      : 0,

    'Stoneskin'        : 0,

    'Inspiration'      : 0,

    'Magic Reflection' : 0,


    }


    if not hasattr(store, 'events'):
        $ events = {}

    if not events.get('coffe_event_1'):


        $ Event('coffe_event_1', 'cord_caffe', 'coffe_event_1', time = [1,])

        $ Event('coffe_event_1', 'cord_caffe_door', 'coffe_event_1', time = [1,])
        $ Event('cofe_event_2',  'cord_caffe', 'cofe_event_2', time = [2, 3])


    if not hasattr(store, 'books_now'):
        $ books_now             = {}
    if not hasattr(store, 'books_gg'):
        $ books_gg              = 0
    if not hasattr(store, 'books_send'):
        $ books_send            = 0
    if not hasattr(store, 'generate_books'):
        $ generate_books()

    if not hasattr(store, 'pos_track_now'):
        $ pos_track_now         = 0
    if not hasattr(store, 'persistent'):
        $ persistent.first_game = True
    if not hasattr(store, 'button_menu_now'):
        $ button_menu_now       = None
    if not hasattr(store, 'button_menu_now_2'):
        $ button_menu_now_2     = None

    if not hasattr(store, 'homes'):
        $ homes = {

    'Leonheart' :{'now':0, 'new':0, 'add':0},
    'Adderin'   :{'now':0, 'new':0, 'add':0},
    'Crowhive'  :{'now':0, 'new':0, 'add':0},
    'Martenden' :{'now':0, 'new':0, 'add':0},

    }
    $ predict_locations = ['leon_room_sa', 'leon_room_hl', 'leon_corridor', 'leon_living', 'leon_bathroom', 'cord_entrance',
    'cord_garden_c','cord_garden_l','cord_garden_r','cord_class_1','cord_class_2','cord_mainhall','cord_caffe','leon_room_mc', ]





    if not hasattr(store, 'events'):
        $ events       = {}

    if not hasattr(store, 'locations_now'):
        $ locations_now = copy.copy(locations_campus)
    if not hasattr(store, 'time_now'):
        $ time_now     = 1
    if not hasattr(store, 'day_now'):
        $ day_now      = 1
    if not hasattr(store, 'dow'):
        $ dow          = 'MON'
    if not hasattr(store, 'location_now'):
        $ location_now = 'leon_room_mc'
    if not hasattr(store, 'old_location'):
        $ old_location = None
    $ say_stop = True
    $ old_location_now  = location_now
    $ old_time_now      = time_now
    if get_showing_images():
        $ image_now_preload = get_showing_images()


    if renpy.get_screen('main_interface'):
        $ main_interface_preload = True

    "" "..."




    $ predict_locations_final_2 = True
    call change_location_optimisation_books_label from _call_change_location_optimisation_books_label
    return
label change_location_optimisation_books_label:
    $ books_now_debug = []
    $ predict_locations = [
    'leon_room_sa', 'leon_room_hl', 
    'cord_garden_l','cord_garden_r', 'leon_bathroom', 'cord_entrance','leon_room_mc', 'leon_corridor', 'leon_living', 'cord_garden_c', 'cord_class_1','cord_class_2','cord_mainhall', 'leon_room_mc', 'leon_room_mc'
    ]


    $ load_all_images_books()
    $ start_load   = datetime.datetime.today()
    $ preload_time = 0
    show screen predict_load_screen
label change_location_optimisation_label:
    if len(predict_locations) == 1 and preload_time == 2:
        call end_optimisation from _call_end_optimisation
        return

    if len(predict_locations):
        if preload_time   == 4:
            $ preload_time = 0


        if location_now == 'cord_class_1' and  dow in ['SAT', 'SUN'] and time_now in [1, 2]:

            if 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '_s.png' in list_files:

                show expression 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '_s.png'
        elif True:
            if 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png' in list_files:
                show expression 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png'
        if not renpy.get_screen('main_interface') and not hasattr(store, 'show_main_interface_preload'):
            $ show_main_interface_preload = True
            show screen main_interface
        with Fade(0.0, 0.0, 0.0)
        if not preload_time:
            $ preload_loc   = predict_locations.pop(0)

            $ preload_time  = 1
        elif True:
            $ preload_time += 1

        $ change_location_optimisation(preload_loc, preload_time)
    elif True:
        call end_optimisation from _call_end_optimisation_1
        return

label end_optimisation:
    hide screen main_interface
    if hasattr(store, 'say_stop'):
        $ del say_stop

    $ predict_locations_final = True
    $ books_now_debug = []
    $ end_load  = datetime.datetime.today()
    $ load_time = str(end_load - start_load)
    hide expression '#000'

    $ time_now     = old_time_now
    $ location_now = old_location_now
    scene expression '#000'
    if hasattr(store, 'image_now_preload'):

        scene expression '[image_now_preload]'




    if hasattr(store, 'main_interface_preload'):
        $ del main_interface_preload
        show screen main_interface







    hide screen predict_load_screen
    return
init -100 python:
    books_now_debug = []
    predict_locations = ['leon_room_sa', 'leon_room_hl', 'leon_corridor', 'leon_living', 'leon_bathroom', 'cord_entrance',
    'cord_garden_c','cord_garden_l','cord_garden_r','cord_class_1','cord_class_2','cord_mainhall','cord_caffe','leon_room_mc', ]





    def load_all_images_books():
        
        x = books_list_1.keys()
        while len(x):
            print(len(x))
            v = x.pop(0)
            
            for i in xrange(0, books_list_1[v]):
                books_now_debug.append([v, i])
        x = books_list_2.keys()
        
        while len(x):
            print(len(x))
            v = x.pop(0)
            
            for i in xrange(0, books_list_2[v]):
                books_now_debug.append([v, i])

    def change_location_optimisation(location, time = None, plus = False, jump = True):
        global location_now, old_location, time_now, day_now, dow, homes, class_plus, win, lose, tmp_events
        global locations_now, locations_academy, locations_campus
        if time is None:
            time = time_now
        old_location = copy.copy(location_now)
        location_now = location
        
        stt = 0
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
        #for event in events:
        #    if events[event].check():
        #        events[event].complete = True
        #        Jump(events[event].label)()
        
        
        if time != 5:
            time_now     = time
        else:
            time_now     = 1
            day_now     += 1
            if day_now%7 == 1:
                dow = 'MON'
            
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
                #if not hasattr(store, 'check_arthur_2'): 
                #    Jump('arthur_2')()
                #    return
            
            if day_now%7 == 0:
                dow = 'SUN'
        if jump:
            Jump('change_location_optimisation_label')()





















label change_location_optimisation_books_label_2:
    $ books_now_debug = []
    $ predict_locations = [
    'leon_room_sa', 'leon_room_hl', 'cord_garden_l','cord_garden_r', 'leon_bathroom', 
    'cord_entrance', 

    ]


    $ load_all_images_books()
    $ start_load   = datetime.datetime.today()
    $ preload_time = 0
    $ old_time_now     =  time_now
    $ old_location_now = location_now
    show screen predict_load_screen



    if preload_time   == 4:
        $ preload_time = 0


    if location_now == 'cord_class_1' and  dow in ['SAT', 'SUN'] and time_now in [1, 2]:

        if 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '_s.png' in list_files:

            show expression 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '_s.png'
    elif True:
        if 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png' in list_files:
            show expression 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png'
    if not renpy.get_screen('main_interface') and not hasattr(store, 'show_main_interface_preload'):
        $ show_main_interface_preload = True
        show screen main_interface
    with Fade(0.0, 0.0, 0.0)
    if not preload_time:
        $ preload_loc   = predict_locations.pop(0)

        $ preload_time  = 1
    elif True:
        $ preload_time += 1

    $ change_location_optimisation(preload_loc, preload_time)











label change_location_optimisation_books_label_3:
    $ books_now_debug = []
    $ predict_locations = ['leon_room_sa', 'leon_room_hl', 'leon_corridor', 'leon_living', 'leon_bathroom', 'cord_entrance',
    'cord_garden_c','cord_garden_l','cord_garden_r','cord_class_1','cord_class_2','cord_mainhall','cord_caffe','leon_room_mc', ]


    $ load_all_images_books()
    $ start_load   = datetime.datetime.today()
    $ preload_time = 0
    $ old_time_now     = time_now
    $ old_location_now = location_now
    show screen predict_load_screen

    if preload_time   == 4:
        $ preload_time = 0


    if location_now == 'cord_class_1' and  dow in ['SAT', 'SUN'] and time_now in [1, 2]:

        if 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '_s.png' in list_files:

            show expression 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '_s.png'
    elif True:
        if 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png' in list_files:
            show expression 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png'
    if not renpy.get_screen('main_interface') and not hasattr(store, 'show_main_interface_preload'):
        $ show_main_interface_preload = True
        show screen main_interface
    with Fade(0.0, 0.0, 0.0)
    if not preload_time:
        $ preload_loc   = predict_locations.pop(0)

        $ preload_time  = 1
    elif True:
        $ preload_time += 1

    $ change_location_optimisation(preload_loc, preload_time)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
