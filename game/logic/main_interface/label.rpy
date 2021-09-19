








init python:
    def need_play_now():
        
        
        
        if location_now in [
            'cord_class_1',  'cord_class_2', 
            'cord_class_1',  'cord_entrance',
            'cord_library',  'cord_caffe',
            'cord_mainhall'
            ]:
            
            return 'audio_ep2/Ambience/amb_classroom1_people.mp3'
        if location_now in ['cord_garden_r', 'cord_garden_l', 'cord_garden_c']:
            if time_now != 4:
                return 'audio_ep2/Ambience/amb_castle_fountain.mp3'
            else:
                return 'audio_ep2/Ambience/amb_castle_fountain_night.mp3'
        return 'audio_ep2/SC/33. Romantic.mp3'

    new_lustogram_profile = None
    def check_new_quest():
        
        
        global Q_Victoria_old
        global Q_Elijah_old
        global Q_Leona_old
        global Q_Lily_old
        global Q_Haley_old
        global Q_Amelie_old
        global Q_Samantha_old
        global Q_Jacob_old
        global Q_Molly_old
        global Q_Naomi_old
        global Q_Sabrina_old
        global Q_Audrey_old  
        global Q_Victoria
        global Q_Elijah
        global Q_Leona
        global Q_Lily
        global Q_Haley
        global Q_Amelie
        global Q_Samantha
        global Q_Jacob
        global Q_Molly
        global Q_Naomi
        global Q_Sabrina
        global Q_Audrey
        global new_lustogram_profile
        
        
        
        
        
        
        
        if Q_Victoria_old != Q_Victoria:
            if not Q_Victoria_old:
                new_lustogram_profile = True
            Q_Victoria_old = Q_Victoria
            
            
            if log_message.get('QLOG_Victoria', 0) == 4:
                return None
            
            
            return 'Victoria'
        
        if Q_Elijah_old != Q_Elijah:
            if not Q_Elijah_old:
                new_lustogram_profile = True
            Q_Elijah_old = Q_Elijah
            
            if Q_Elijah == 5:
                return None
            if log_message.get('QLOG_Elijah', 0) == 4:
                return None
            return 'Elijah'
        
        
        
        if Q_Lily_old != Q_Lily:
            if not Q_Lily_old:
                new_lustogram_profile = True
            Q_Lily_old = Q_Lily
            
            if log_message.get('QLOG_Lily', 0) == 7:
                return None
            
            return 'Lily'
        
        if Q_Haley_old != Q_Haley:
            if not Q_Haley_old:
                new_lustogram_profile = True
            Q_Haley_old = Q_Haley
            
            
            if log_message.get('QLOG_Haley', 0) == 7:
                return None
            return 'Haley'
        
        if Q_Amelie_old != Q_Amelie:
            if not Q_Amelie_old:
                new_lustogram_profile = True
            Q_Amelie_old = Q_Amelie
            
            if log_message.get('QLOG_Amelie', 0) == 2:
                return None
            return 'Amelie'
        
        if Q_Samantha_old != Q_Samantha:
            if not Q_Samantha_old:
                new_lustogram_profile = True
            Q_Samantha_old = Q_Samantha
            
            
            if log_message.get('QLOG_Samantha', 0) == 5:
                return None
            return 'Samantha'
        
        if Q_Jacob_old != Q_Jacob:
            if not Q_Jacob_old:
                new_lustogram_profile = True
            Q_Jacob_old = Q_Jacob
            
            
            if log_message.get('QLOG_Jacob', 0) in [2, 4]:
                return None
            return 'Jacob'
        
        if Q_Molly_old != Q_Molly:
            if not Q_Molly_old:
                new_lustogram_profile = True
            Q_Molly_old = Q_Molly
            
            if log_message.get('QLOG_Molly', 0) == 3:
                return None
            return 'Molly'
        
        if Q_Naomi_old != Q_Naomi:
            if not Q_Naomi_old:
                new_lustogram_profile = True
            Q_Naomi_old = Q_Naomi
            
            if log_message.get('QLOG_Naomi', 0) == 7:
                return None
            return 'Naomi'
        
        if Q_Sabrina_old != Q_Sabrina:
            if not Q_Sabrina_old:
                new_lustogram_profile = True
            Q_Sabrina_old = Q_Sabrina
            
            
            
            if log_message.get('QLOG_Sabrina', 0) == 3:
                return None
            return 'Sabrina'
        
        if Q_Audrey_old != Q_Audrey:
            if not Q_Audrey_old:
                new_lustogram_profile = True
            Q_Audrey_old = Q_Audrey
            
            
            
            if log_message.get('QLOG_Audrey', 0) in [5, 6]:
                return None
            return 'Audrey'


    p_variables = {
 'Victoria': {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 7: 7, 8: 8, 9: 9, 10: 10},
 'Sabrina':  {1: 2, 2: 3, 3: 4, 4: 5, 5: 6},
 'Haley':    {2: 1, 1: 2, 3: 3, 6: 4, 7: 5, 10: 6, 11: 7, 12: 8},
 'Samantha': {1: 2, 2: 3, 3: 4, 4: 5, 6: 5},
 'Audrey':   {1: 1, 3: 2, 4: 3},
 'Lily':     {2: 3, 1: 2, 3: 4, 4: 5, 5: 6, 6: 7},
 'Naomi':    {2: 3, 1: 2, 3: 4, 5: 5, 6: 6, 8: 7},
 'Amelie':   {1: 1, 2: 2},
 'Molly':    {1: 1, 2: 2},
 'Elijah':   {1: 2, 2: 3, 3: 4, 4: 5, 5: 6},
 'Jacob':    {1: 1, 2: 2}}



label change_location_label:
    hide screen main_interface 

    with Dissolve(.3)
    if not len(predict_locations):
        $ check_events()
label main_interface_label:
    #$ renpy.start_predict('images/locations_main/**')
    hide screen black_tmp_screen_menu
    if not hasattr(store, 'ep2start'):
        call change_location_label_without_events from _call_change_location_label_without_events_1
    elif True:
        python:
            
            cnq = check_new_quest()
            
            if cnq:
                #if cnq in p_variables:
                    #ttttxstttt = getattr(store, 'Q_'+cnq, None) 
                    #if ttttxstttt in p_variables[cnq]:
                   #     setattr(store, 'P_'+cnq, p_variables[cnq][ttttxstttt]) 
                    

                if new_lustogram_profile:
                    new_lustogram_profile = copy.copy(cnq)  
                new_cnq   = True
                new_cnq_2 = cnq
                
                if not persistent.from_gallery:
                    ShowMessage(['images/notes_mini.png', '  New Quest: '+str(cnq)])
                    #if new_lustogram_profile:
                    #    ShowMessage(['images/lustogram_mini.png', '   New Profile: '+str(new_lustogram_profile)])
            npn    = need_play_now()
            rmgp   = renpy.music.get_playing() 
            rmgp_2 = renpy.music.get_playing('music_2') 

            if rmgp is not None and rmgp != npn:
                renpy.music.stop('music', fadeout = 3.0)
                renpy.music.play(npn, 'music_2', loop = True, fadein=5.0)
            elif rmgp_2 is not None and rmgp_2 != npn:
                renpy.music.stop('music_2', fadeout = 3.0)
                renpy.music.play(npn, 'music', loop = True, fadein=5.0)

        if location_now == 'cord_class_1' and  dow in ['SAT', 'SUN'] and time_now in [1, 2]:

            scene expression 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '_s.png'
        elif True:

            scene expression 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png'
    if not renpy.get_screen('show_hide_locations_2') and not renpy.get_screen('show_hide_locations'): 
        show screen show_hide_locations_2
    show screen main_interface 
    with Dissolve(.3)
    $ renpy.choice_for_skipping()

    call screen pass_screen


label change_location_label_without_events:


    scene expression '#000'
    if 'images/main_interface/locations/'+ str(location_now)+'.png' in list_files:
        scene expression 'images/main_interface/locations/'+ str(location_now)+'.png'
    elif True:
        $ ep2start = True
        jump main_interface_label
    with Dissolve(.3)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
