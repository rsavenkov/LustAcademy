label set_variables_at_start:
    $ events      = {}
    $ p_variables = {
'Victoria': 0,
'Sabrina':  0,
'Haley':    0,
'Samantha': 0,
'Audrey':   0,
'Lily':     0,
'Naomi':    0,
'Amelie':   0,
'Molly':    0,
'Elijah':   0,
'Jacob':    0,
}

    $ spells_up = {
    'Combat Bolt' : 0,
    'Incendio'    : 0,
    'Rictusempra' : 0,
    'Episkey'     : 0,
    }
    


    $ set_prst_p_variables = True
    $ Event('SamantaRoomStnd', 'samanta_room', 'samanta_room_label', True)
    $ Event('BathStnd',        'bath',         'bath_label', True)

    $ Event('AshlieRoomStnd',        'ashlie_room',  'ashlie_room_label', True)

    $ Event('RestroomStump',     'restroom',  'restroom_stump_label', True)
    $ Event('KitchenStump',      'kitchen',   'kitchen_stump_label', True)
    $ Event('library_event_amelie_1', 'cord_library', 'library_event_amelie_1', time = [1,2])



    $ Event('coffe_event_1', 'cord_caffe', 'coffe_event_1', time = [1,])

    $ Event('coffe_event_1', 'cord_caffe_door', 'coffe_event_1', time = [1,])
    $ Event('cofe_event_2',  'cord_caffe', 'cofe_event_2', time = [2, 3])

    $ show_hide_locations_pos = False
    #$ hide_interface          = True


    $ like    = [False, False, False]

    $ money   = 0

    $ comment = ['', '', '']

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
