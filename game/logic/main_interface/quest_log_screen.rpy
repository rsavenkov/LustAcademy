label quest_log_label:
    $ renpy.call(qstt)
    show screen main_interface 
    show screen show_hide_locations_2
    hide screen black_tmp_screen_menu
    with Dissolve(.5)
    $ change_location(qstt_location)
    $ qstt_location = 0
    jump main_interface_label
init python:
    place_holder_text  = 'placeholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholderplaceholder placeholder placeholder placeholder placeholder placeholder'
    surnames           = {'Adele': 'Cuill', 
'Amelie': 'Earhart', 
'Arthur': 'Doorman Iv', 
'Ashley': 'Rose', 
'Audrey': 'Burns', 
'Carter': 'Brown', 
'Diego': 'Faradenza', 
'Don': 'Rose', 
'Elijah': 'Bloom', 
'Faith': 'Whistley', 
'Frida': 'Crowhive', 
'Gabriella': 'Leal', 
'Giant': '', 
'Gordon': 'Chompski', 
'Grace': ' Sherman', 
'Haley': 'Ranger', 
'Jacob': 'Frollo', 
'Jaina': 'Martenden', 
'Jill': 'Whistley', 
'Joshi': 'Backs', 
'Katrina': 'Adderin', 
'Leona': 'Leonheart', 
'Lily': 'Hebi', 
'Lucy': 'Altidore', 
'Mina': 'Harper', 
'Molly': 'Maeve', 
'Naomi': 'Kimba', 
'Olivia': 'Wild-Rose', 
'Romul': 'Mobs', 
'Sabrina': 'Spellman', 
'Sadira': 'Adala', 
'Samantha': 'Rose', 
'Vanessa': 'Le Court', 
'Victoria': 'Lapis', 
'Willow': 'Chompski', 
'Mushroom Girl': '', 
'Evelin': 'Caretop', 
'Marta': 'Scott'}

    quest_log_menu_now = 'CALENDAR'
screen quest_log_screen(open_menu = 'CALENDAR'):
    zorder 220


    default menu_now = open_menu

    imagebutton:
        idle '#000a'
        hover '#000a'
        action SetVariable('quest_log_menu_now', 'CALENDAR'), Hide('quest_log_screen', transition = Dissolve(.5)), Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_close.mp3')

    vbox:
        xalign .5 
        yalign .5
        hbox:
            for i in ('CHARACTER INFO', 'CALENDAR', 'CHARACTERISTICS' ):
                viewport:
                    xmaximum 409
                    ymaximum 51
                    imagebutton:
                        if menu_now == i:
                            idle  'other_menu_quest_log_1'
                        else:
                            idle  'other_menu_quest_log_0'
                        hover 'other_menu_quest_log_1'
                        action SetVariable('quest_log_menu_now', i), SetScreenVariable('menu_now', i)
                    text i font 'fonts/h_font.ttf' size 20 xalign .5 yalign .5 color '#FFEEDE'
            viewport:
                xmaximum 50
                ymaximum 50
                image 'quest_log_exit_0'
                imagebutton:
                    idle  'main_interface/quest_log/quest_log_exit.png'
                    hover im.MatrixColor('main_interface/quest_log/quest_log_exit.png', im.matrix.brightness(.2)) 
                    action Hide('quest_log_screen', transition = Dissolve(.5)), Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_close.mp3')

            xpos 3
            ypos 4
        viewport:
                
            xmaximum 1278
            ymaximum 670
            xpos 2
            image '#0000'

            
            imagebutton:
                idle   '#0000'
                hover  '#0000'
                action NullAction()

        



            if menu_now == 'CHARACTERISTICS':
                #if hasattr(store, 'Q_Victoria') and Q_Victoria >= 5:
                #    image 'characteristics_bg'
                #else:
                image 'characteristics_bg_0'
                default stats = None
                default get_homes_great = get_homes_great()
                default get_homes_great_number = {
                1 : 'st',
                2 : 'nd',
                3 : 'rd',
                4 : 'th',


                }
                vbox:
                    xpos 22
                    ypos 275
                    viewport:
                        image '#0000'
                        xmaximum 390+20
                        ymaximum 95
                        if hasattr(store, 'Q_Victoria') and Q_Victoria >= 5:
                            image 'combat_ball_icon'
                        else:
                            image 'duels_locked'
                        viewport:
                            xpos 120
                            xmaximum 280+20
                            ymaximum 95
                            image '#fff0'
                            if hasattr(store, 'Q_Victoria') and Q_Victoria >= 5:
                                text 'Medium Reduction in opponent Stamina. Spellpower: ' + str(100+spells_up['Combat Bolt']) size 18 color "#fdd4b8" font 'fonts/h_font.ttf' yalign .5
                            else:
                                text 'This spell is not learned yet.' size 18 color "#afa5b6" font 'fonts/h_font.ttf' yalign .5



                    viewport:
                        image '#0000'
                        xmaximum 390+20
                        ymaximum 95
                        if hasattr(store, 'has_rictusempra'):
                            image 'rictusempra_icon'
                        else:
                            image 'duels_locked'
                        viewport:
                            xpos 120
                            xmaximum 280+20
                            ymaximum 95
                            image '#fff0'
                            if hasattr(store, 'has_rictusempra'):
                                text 'Medium Reduction in opponent Stamina. Chance of Small Stun. Spellpower: ' + str(100+spells_up['Rictusempra']) size 18 color "#fdd4b8" font 'fonts/h_font.ttf' yalign .5
                            else:
                                text 'This spell is not learned yet.' size 18 color "#afa5b6" font 'fonts/h_font.ttf' yalign .5
                    viewport:
                        image '#0000'
                        xmaximum 390+20
                        ymaximum 95
                        if hasattr(store, 'has_incendio'):
                            image 'mini_games/duels/new/incendio_icon.png' 
                        else:
                            image 'duels_locked'
                        viewport:
                            xpos 120
                            xmaximum 280+20
                            ymaximum 95
                            image '#fff0'
                            if hasattr(store, 'has_incendio'):
                                text 'Medium Reduction in opponent Stamina. Chance of Medium Burn. Spellpower: ' + str(100+spells_up['Incendio']) size 18 color "#fdd4b8" font 'fonts/h_font.ttf' yalign .5
                            else:
                                text 'This spell is not learned yet.' size 18 color "#afa5b6" font 'fonts/h_font.ttf' yalign .5
                    viewport:
                        image '#0000'
                        xmaximum 390+20
                        ymaximum 95
                        if hasattr(store, 'has_episkey'):
                        
                            image 'mini_games/duels/new/episkey_icon.png'
                        else:
                            image 'duels_locked'
                        viewport:
                            xpos 120
                            xmaximum 280+20
                            ymaximum 95
                            image '#fff0'
                            if hasattr(store, 'has_episkey'):
                                text 'Medium Heal. Chance of Small Heal over time. Spellpower: ' + str(100+spells_up['Episkey']) size 18 color "#fdd4b8" font 'fonts/h_font.ttf' yalign .5
                            else:
                                text 'This spell is not learned yet.' size 18 color "#afa5b6" font 'fonts/h_font.ttf' yalign .5
                default ghg_adderin = get_homes_great.index('Adderin')+1
                default ghg_leonheart = get_homes_great.index('Leonheart')+1
                default ghg_martenden = get_homes_great.index('Martenden')+1
                default ghg_crowhive = get_homes_great.index('Crowhive')+1
                viewport:
                    xpos 30
                    ypos 165
                    xmaximum 300
                    ymaximum 50
                    image '#0000'
                    text '[Name] [Surname]' size 36 color '#FFD4AD' font 'fonts/h_font.ttf'
              
                # viewport:
                #     xpos 165
                #     ypos 80
                #     xmaximum 300
                #     ymaximum 80
                #     image '#fff0'
                #     text place_holder_text[:40] size 18 color '#FFEEDE' font 'fonts/h_font.ttf'

                # viewport:
                #     xpos 15
                #     ypos 170
                #     xmaximum 445
                #     ymaximum 80
                #     image '#fff0'
                #     image Text(place_holder_text[:40], size = 18, color = '#D6DEFF', font = 'fonts/h_font.ttf') alpha .6
                viewport:
                    image '#0000'
                    image 'house_points_bg'
                    xmaximum 350
                    ymaximum 632
                    ypos 20
                    xpos 480
                    viewport:
                        xpos 25
                        ypos 526
                        xmaximum 65
                        ymaximum 20
                        add '#0000'
                        text str(homes['Adderin']['now']) xalign .5 yalign .5 size 16 font 'fonts/h_font.ttf' color '#654D6D'
                    viewport:
                        xpos 25+79
                        ypos 526
                        xmaximum 65
                        ymaximum 20
                        add '#0000'
                        text str(homes['Leonheart']['now']) xalign .5 yalign .5 size 16 font 'fonts/h_font.ttf' color '#654D6D'
                    viewport:
                        xpos 180
                        ypos 526
                        xmaximum 65
                        ymaximum 20
                        add '#0000'
                        text str(homes['Crowhive']['now']) xalign .5 yalign .5 size 16 font 'fonts/h_font.ttf' color '#654D6D'
                    viewport:
                        xpos 180+78
                        ypos 526
                        xmaximum 65
                        ymaximum 20
                        add '#0000'
                        text str(homes['Martenden']['now']) xalign .5 yalign .5 size 16 font 'fonts/h_font.ttf' color '#654D6D'
                    viewport:
                        xpos 28
                        ypos 30
                        xmaximum 65
                        ymaximum 20
                        add '#0000'
                        if ghg_adderin == 1:
                            add Text(
                                str(ghg_adderin) + get_homes_great_number[ghg_adderin], 
                                font  = 'fonts/h_font.ttf', 
                                size  = 24,
                                color = '#FFEEDE'
                                ) xalign .5 yalign .5
                        else:
                            add Text(
                                str(ghg_adderin) + get_homes_great_number[ghg_adderin], 
                                font  = 'fonts/h_font.ttf', 
                                size  = 18,
                                color = '#DAE0FF'
                                ) alpha .5 xalign .5 yalign .5
                    viewport:
                        xpos 103
                        ypos 30
                        xmaximum 65
                        ymaximum 20
                        add '#0000'
                        if ghg_leonheart == 1:
                            add Text(
                                str(ghg_leonheart) + get_homes_great_number[ghg_leonheart], 
                                font  = 'fonts/h_font.ttf', 
                                size  = 24,
                                color = '#FFEEDE'
                                ) xalign .5 yalign .5
                        else:
                            add Text(
                                str(ghg_leonheart) + get_homes_great_number[ghg_leonheart], 
                                font  = 'fonts/h_font.ttf', 
                                size  = 18,
                                color = '#DAE0FF'
                                ) alpha .5 xalign .5 yalign .5


                    viewport:
                        xpos 178
                        ypos 30
                        xmaximum 65
                        ymaximum 20
                        add '#0000'
                        if ghg_crowhive == 1:
                            add Text(
                                str(ghg_crowhive) + get_homes_great_number[ghg_crowhive], 
                                font  = 'fonts/h_font.ttf', 
                                size  = 24,
                                color = '#FFEEDE'
                                ) xalign .5 yalign .5
                        else:
                            add Text(
                                str(ghg_crowhive) + get_homes_great_number[ghg_crowhive], 
                                font  = 'fonts/h_font.ttf', 
                                size  = 18,
                                color = '#DAE0FF'
                                ) alpha .5 xalign .5 yalign .5
                    viewport:
                        xpos 253
                        ypos 30
                        xmaximum 65
                        ymaximum 20
                        add '#0000'
                        if ghg_martenden == 1:
                            add Text(
                                str(ghg_martenden) + get_homes_great_number[ghg_martenden], 
                                font  = 'fonts/h_font.ttf', 
                                size  = 24,
                                color = '#FFEEDE'
                                ) xalign .5 yalign .5
                        else:
                            add Text(
                                str(ghg_martenden) + get_homes_great_number[ghg_martenden], 
                                font  = 'fonts/h_font.ttf', 
                                size  = 18,
                                color = '#DAE0FF'
                                ) alpha .5 xalign .5 yalign .5

                    viewport:
                        xmaximum 50
                        ymaximum int(int((float(homes['Adderin']['now'])/350.0)*353))
                        add '#349b4d' alpha .8
                        xpos 110-77
                        ypos 525
                        yalign 1.0
                    image 'ch_duel_adderin' xpos 110-77 ypos 490-int(int((float(homes['Adderin']['now'])/350.0)*353)) zoom .5
                    viewport:
                        xmaximum 50
                        ymaximum int(int((float(homes['Leonheart']['now'])/350.0)*353))
                        add '#b64067' alpha .8
                        xpos 110
                        ypos 525
                        yalign 1.0
                    image 'ch_duel_leonheart' xpos 111 ypos 490-int(int((float(homes['Leonheart']['now'])/350.0)*353)) zoom .5
                    viewport:
                        xmaximum 50
                        ymaximum int(int((float(homes['Crowhive']['now'])/350.0)*353))
                        add '#c48f4c' alpha .8
                        xpos 188
                        ypos 525
                        yalign 1.0
                    image 'ch_duel_martenden' xpos 189 ypos 490-int(int((float(homes['Crowhive']['now'])/350.0)*353)) zoom .5
                    viewport:
                        xmaximum 50
                        ymaximum int(int((float(homes['Martenden']['now'])/350.0)*353))
                        add '#5f61d3' alpha .8
                        xpos 188+77
                        ypos 525
                        yalign 1.0
                    image 'ch_duel_crowhive' xpos 188+79 ypos 490-int(int((float(homes['Martenden']['now'])/350.0)*353)) zoom .5
                    
                viewport:
                    xpos 870
                    ypos 47
                    xmaximum 400
                    ymaximum 615
                    image '#0000'
                    vbox:
                        xalign .5
                        spacing 5
                        for i in ('Placeholder 0', 'Placeholder 1', 'Placeholder 2'):
                            viewport:
                                xmaximum 381
                                ymaximum 30
                                imagebutton:
                                    if stats != i:
                                        idle  'characteristics_statistic_button_0'
                                        hover im.MatrixColor('main_interface/quest_log/characteristics_statistic_button_0.png', im.matrix.brightness(.2)) 

                                        action SetScreenVariable('stats', i)
                                    else:
                                        idle  'characteristics_statistic_button_1'
                                        hover im.MatrixColor('main_interface/quest_log/characteristics_statistic_button_1.png', im.matrix.brightness(.2)) 

                                        action SetScreenVariable('stats', None)
                                text 'Placeholder' size 18 color '#4D4E65' font 'fonts/h_font.ttf' yalign .5 xpos 5
                            if stats == i:
                                vbox:
                                    for i in xrange(7):
                                        hbox:
                                            spacing 7
                                            image 'characteristics_statistic_point'
                                            image Text('placeholder placehol', size = 14, font='fonts/h_font.ttf', color = '#FFFFFF') alpha .7
                                            image 'characteristics_statistic_line' yalign .5
                                            image Text('12', size = 14, font='fonts/h_font.ttf', color = '#FFFFFF') alpha .7


            if menu_now == 'CHARACTER INFO':
                if not mp.tutorial['CHARACTER INFO']:
                    timer .01 action SetVariable('tutorial_bb', 0), Show('tutorial_screen', what_tutor = 'CHARACTER INFO')
                image 'character_info_bg' xpos 1

                default char_now         = log_message.items()[0][0][5:]

                default ch_in_circle_now = 0




               # if char_now.title() in quest_log_big_avatars:
               #     image 'main_interface/quest_log/quest_log_avatars/'+char_now.title()+'_big.png' xalign .22 alpha .95
                
                #else:
                image 'main_interface/quest_log/quest_log_avatars/'+char_now.title()+'_big.png' xalign .17 alpha .95
                viewport:
                    xpos 540
                    xmaximum 380
                    ymaximum 80 
                    image '#0000'
                    text char_now + ' ' + surnames.get(char_now.title(), ''): 
                        xalign .5 yalign .5
                        if colors_names.get(char_now.title()):
                            color colors_names[char_now.title()]
                        else:
                            color '#FFBA7B'
                        size  40
                        font  'fonts/h_font.ttf' 
                viewport:
                    xpos 570
                    ypos 100
                    xmaximum 620
                    ymaximum 200
                    image '#0000'
                    if chars_gender_table.get(char_now.title()):
                        
                        image Text(chars_gender_table[char_now.title()]['description'], outlines = [(1, "#000", 0, 0)], color = '#FFEEDE', size = 22, font = 'fonts/h_font.ttf')
                    
                    else:
                        text place_holder_text:
                            color '#FFEEDE'
                            size  20
                            font  'fonts/h_font.ttf'

                # viewport:
                #     xpos 1085
                #     ypos 8
                #     xmaximum 185
                #     ymaximum 155
                #     image '#0000'
                #     vbox xpos 5:
                #         hbox:
                #             image Text('Gender: ', color = '#0F1621', size = 20, font = 'fonts/h_font.ttf') alpha .38
                            
                #             if chars_gender_table.get(char_now.title()):
                                

                #                 image Text(chars_gender_table[char_now.title()]['gender'], color = '#FFEEDE', size = 20, font = 'fonts/h_font.ttf'):
                #                     if 'shemale' in chars_gender_table[char_now.title()]['gender'].lower():
                #                         ypos 6
                #         hbox:
                #             image Text('Age: ', color = '#0F1621', size = 20, font = 'fonts/h_font.ttf')    alpha .38
                #             if chars_gender_table.get(char_now.title()):
                #                 image Text(str(int(chars_gender_table[char_now.title()]['age'])), color = '#FFEEDE', size = 20, font = 'fonts/h_font.ttf')
                        
                #         image Text('Height:', color = '#0F1621', size = 20, font = 'fonts/h_font.ttf') alpha .38
                #         image Text('Hair:', color = '#0F1621', size = 20, font = 'fonts/h_font.ttf')   alpha .38
                #         image Text('Eyes:', color = '#0F1621', size = 20, font = 'fonts/h_font.ttf')   alpha .38
                #         image Text('P-rs:', color = '#0F1621', size = 20, font = 'fonts/h_font.ttf')   alpha .38
                
                viewport: 
                    xpos 560 ypos 400
                    xmaximum 710
                    ymaximum 40
                    image '#fff0'
                    if (log_message_p.get(str(char_now).title())
                        ) is not None and (
                        p_variables.get(str(char_now).title()) is not None) and (
                        p_variables[str(char_now).title()] < len(log_message_p[str(char_now).title()])
                        ):      
                        #hbox:

                        #default ch_in_circle_now = p_variables[str(char_now).title()]
                        $ mxrange = len(log_message_p[char_now.title()])-1
                        for i in xrange(mxrange):
                            viewport:
                                xmaximum 55
                                ymaximum 52
                                image '#0000'
                                imagebutton:
                                    xalign .5 yalign .5
                                    if ch_in_circle_now == i:
                                        idle im.MatrixColor('main_interface/quest_log/character_info_circle.png', im.matrix.brightness(.3)) 
                                    
                                    else:
                                        idle  'character_info_circle'
                                    hover im.MatrixColor('main_interface/quest_log/character_info_circle.png', im.matrix.brightness(.3)) 
                                    if p_variables[str(char_now).title()] >= i:
                                
                                        action SetScreenVariable('ch_in_circle_now', i)
                                    
                                    else:
                                        action NullAction()
                                text   str(i+1): 
                                    xalign .5 yalign .5 
                                    if p_variables[str(char_now).title()] == i:
                                        size 17
                                        #color '#000'

                                    else:
                                        size 15

                                    font 'fonts/h_font.ttf'
                                xalign float(str(1.0/mxrange)[:4])*(i)
                                if p_variables[str(char_now).title()] == i:
                                    
                                    image 'character_info_elipse' xalign .5 yalign .5
                        
                        viewport:
                            xmaximum 55
                            ymaximum 52
                            image '#0000'
                            imagebutton:
                                xalign .5 yalign .5
                                if ch_in_circle_now == i+1:
                                    idle im.MatrixColor('main_interface/quest_log/character_info_circle.png', im.matrix.brightness(.3)) 
                                
                                else:
                                    idle  'character_info_circle'
                                hover im.MatrixColor('main_interface/quest_log/character_info_circle.png', im.matrix.brightness(.3)) 
                                if p_variables[str(char_now).title()] >= i+1:
                                
                                    action SetScreenVariable('ch_in_circle_now', i+1)
                                else:
                                    action NullAction()
                            #image 'character_info_circle' xalign .5 yalign .5
                            
                            text   str(i+2): 
                                xalign .5 yalign .5 
                                if p_variables[str(char_now).title()] == i+1:
                                    size 17
                                    #color '#000'

                                else:
                                    size 15

                                font 'fonts/h_font.ttf'
                            xalign float(str(1.0/mxrange)[:4])*(i+1)
                            if p_variables[str(char_now).title()] == i+1:
                                
                                image 'character_info_elipse' xalign .5 yalign .5
                viewport:
                    xpos 570
                    ypos 450
                    ymaximum 210
                    xmaximum 690
                    image '#0000'
                    if (log_message_p.get(str(char_now).title())
                        ) is not None and (
                        p_variables.get(str(char_now).title()) is not None) and (
                        p_variables[str(char_now).title()] < len(log_message_p[str(char_now).title()])
                        ):                        
                        text log_message_p[str(char_now).title()][ch_in_circle_now] font 'fonts/h_font.ttf' size 17 color '#FFEEDE' outlines [(1, "#000", 0, 0)]
                
                    else:
                        text place_holder_text font 'fonts/h_font.ttf' size 17 color '#FFEEDE'
                
                viewport:
                    xpos 2
                    xmaximum 226
                    ymaximum 630
                    #image '#000a'
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    vbox xalign .5 ypos 10:
                        spacing 5
                        for i in log_message:
                            $ log_name = i[5:]
                            viewport:
                                xmaximum 200
                                ymaximum 80
                                imagebutton: 
                                    idle  'char_card' 

                                    hover im.MatrixColor('main_interface/quest_log/char_card.png', im.matrix.brightness(.2)) 
                                    action SetScreenVariable('char_now', log_name), SetScreenVariable('ch_in_circle_now', p_variables[str(log_name).title()])
                                    xalign .5 yalign .5
                                image 'main_interface/quest_log/quest_log_avatars/' + log_name + '.png' zoom .55 yalign .5 xpos 5
                                text log_name: 
                                    size 18 
                                    if colors_names.get(log_name):
                                        color colors_names[log_name] #'#B2D09A'
                                    else:
                                        color '#FFD6AF' 
                                    xpos 75 ypos 15 
                                    font 'fonts/h_font.ttf'
                                viewport:
                                    xmaximum 100
                                    ymaximum 4
                                    image '#260B30' alpha .5
                                    xpos 75
                                    ypos 65
                                    viewport:
                                        xmaximum int(float(p_variables[str(log_name).title()])/(len(log_message_p[log_name.title()])-1)*100.0)
                                        ymaximum 4
                                        image '#E5D7FF'
                                hbox:
                                    xpos 75
                                    ypos 45
                                    image Text('Progress: ', font='fonts/h_font.ttf', size = 10, color ='#E5D7FF', alpha = .5)

                                    image Text( 


                                    str(int(float(p_variables[str(log_name).title()])/(len(log_message_p[log_name.title()])-1)*100.0)) + '%', 


                                      font='fonts/h_font.ttf', size = 10, color ='#E5D7FF', alpha = .8)
                                    
                                    
            if menu_now == 'CALENDAR':
                if not mp.tutorial['CALENDAR']:

                    timer .01 action  [Function(set_tutorial, 'CALENDAR'),  SetVariable('tutorial_bb', 0), SetVariable('tmp_time_now', copy.copy(time_now)), SetVariable('time_now', 2), Hide('quest_log_screen'), Show('quest_log_screen'), Show('tutorial_screen', what_tutor= 'CALENDAR', rtrn=False)]
                    
                
                image 'quest_log_bg' xalign .5# yalign .5
                viewport:
                    image '#0000'
                    ymaximum 62
                    xmaximum 1200
                    xalign .5 
                    vbox:
                        xalign .5
                        yalign .5
                        text 'Here you can keep track of all the routes, activities, etc. that are available to you. and quickly navigate to the desired one, without wasting' :
                            color '#91A1CB'
                            font 'fonts/h_font.ttf'
                            size 16
                            xalign .5 
                        text 'time walking around the locations and searching. Next to the avatars of the characters are icons, the decoding of which is next.':
                            color '#91A1CB'
                            font 'fonts/h_font.ttf'
                            size 16
                            xalign .5 
                imagebutton:
                    idle '#0000'
                    hover '#0000'
                    action NullAction()


                for i in [1, 2, 3, 4]:
                    $ q_t_n = get_quest_log_time(i)
                    viewport:
                        xpos 150
                        ypos 85+147*(i-1)
                        ymaximum 95
                        xmaximum 50
                        if array_quest_log[i]:
                            imagebutton:
                                idle Transform('main_interface/quest_log/arrow_right_quest_log.png', xzoom = -1)
                                hover Transform(im.MatrixColor('main_interface/quest_log/arrow_right_quest_log.png', im.matrix.brightness(.2)), xzoom = -1)
                                action Function(def_array_quest_log, i = i, j =-7 )
                    viewport:
                        xpos 1195
                        ypos 85+147*(i-1)
                        ymaximum 95
                        xmaximum 60
                        if len(check_copies_quest_log(i)[array_quest_log[i]+7:7+7+array_quest_log[i]]):
                            imagebutton:
                                idle 'main_interface/quest_log/arrow_right_quest_log.png'
                                hover im.MatrixColor('main_interface/quest_log/arrow_right_quest_log.png', im.matrix.brightness(.2))
                                action Function(def_array_quest_log, i = i, j =+7)
                vbox:

                    for i in [1, 2, 3, 4]:
                        $ q_t_n = get_quest_log_time(i)
                        viewport:
                            xpos 155
                            ypos 60
                            ymaximum 147
                            xmaximum 1130





                            add '#fff0'
                            hbox:
                                spacing 10

                                yalign .5
                                $ tmp_q_t_n = []
                                for x in check_copies_quest_log(i)[array_quest_log[i]:7+array_quest_log[i]]:

                                    if x[1] not in tmp_q_t_n:
                                        viewport:
                                            xmaximum 125
                                            ymaximum 130
                                            viewport:
                                                xalign .5

                                                xmaximum 125
                                                ymaximum 130
                                                image '#0000'

                                                image 'main_interface/quest_log/quest_log_avatars/'+x[1]+'.png':
                                                    if i < time_now:
                                                        alpha .2 
                                                    xalign .5 yalign .5
                                            
                                            if i >= time_now:
                                                viewport:
                                                    xalign 1.0
                                                    yalign 1.0

                                                    xmaximum 50
                                                    ymaximum 50
                                                    add '#0000'

                                                    if 'dale' not in location_now:
                                                        imagebutton:
                                                            idle 'main_interface/quest_log/quest_log_skip_0.png'
                                                            hover 'main_interface/quest_log/quest_log_skip_1.png'
                                                            if time_now != i and not persistent.quest_log_screen_warning:
                                                                action Show('quest_log_screen_warning', x=x,i=i)
                                                            else:
                                                                if x[3][0] == '!':
                                                                    action [

                                                                SetVariable('time_now', i), 
                                                                Hide('quest_log_screen'),
                                                                Function(change_location, get_location_for_quest_log(x[3][1:]), up_points_0 = time_now, up_points = i),
                                                                Function(jump_to_event, x[3][1:], False, False),
                                                                ]
                                                                else:
                                                                    action [

                                                                SetVariable('time_now', i), 
                                                                Hide('quest_log_screen'),
                                                                Function(change_location, x[3], up_points_0 = time_now, up_points = i),
                                                                ]

                                                    else:
                                                        image im.Grayscale('main_interface/quest_log/quest_log_skip_0.png')








                                    $ tmp_q_t_n.append(x[1])
            # imagebutton:
            #     idle  'inventory_interface/close_inventory.png'
            #     hover im.MatrixColor('inventory_interface/close_inventory.png', im.matrix.brightness(.3))
            #     action Hide('quest_log_screen', transition = Dissolve(.5)), Function(renpy.play, channel = 'sound', filename = 'audio_ep2/Gameplay/snd_invenoty_close.mp3')

            #     xalign .985
            #     ypos 4
#This route is not available at this time of the day. 
#Chosing this option will lead to a time skip. Continue?

screen quest_log_screen_warning(x, i):
    zorder 1000
    imagebutton:
        idle  '#0000'
        hover '#0000'
        action SetField(persistent, 'quest_log_screen_warning', None), Hide('quest_log_screen_warning')
    if x[3][0] == '!':
        $ yes_action = [

        SetVariable('time_now', i), 
        Hide('quest_log_screen'),
        Hide('quest_log_screen_warning'),
        Function(change_location, get_location_for_quest_log(x[3][1:]), up_points_0 = time_now, up_points = i),
        Function(jump_to_event, x[3][1:], False, False),
        ]
    else:
        $ yes_action = [

        SetVariable('time_now', i), 
        Hide('quest_log_screen'),
        Hide('quest_log_screen_warning'),
        Function(change_location, x[3], up_points_0 = time_now, up_points = i),
        ]
    $ message = _('{size=20}This route is not available at this time of the day.{/size}\n{size=20}Chosing this option will lead to a time skip.{/size}\n{size=20}Continue?{/size}')
    $ dont_ask_again = [
    SetField(persistent, 'quest_log_screen_warning', True),
    SetField(persistent, 'quest_log_screen_warning', None),
    persistent.quest_log_screen_warning
    ]
    use confirm(message, yes_action, Hide('quest_log_screen_warning', transition = Dissolve(.5)), yes_text = _("Accept"), no_text = _("Decline"), dont_ask_again = dont_ask_again)

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

       # at inventory_interface_transform

    #Transform(i.image, xalign = .5, yalign = .5, zoom = .5)
    #image 'main_interface/quest_log/quest_log_avatars/Audrey.png'
    #image AlphaMask(Transform('main_interface/quest_log/quest_log_avatars/Audrey.png',zoom=.2, xpos = -100, ypos = -50), 'main_interface/quest_log/quest_log_avatars/mask.png') xalign .5 yalign .5

#     viewport:
#         add 'quest_log_bg'
#         xmaximum 721
#         ymaximum 492
#         add '#fff0'
#         imagebutton:
#             idle '#0000'
#             hover '#0000'
#             action NullAction()
#         at inventory_interface_transform


#         for i in [1, 2, 3, 4]:
#             $ q_t_n = get_quest_log_time(i)
#             viewport:
#                 xpos 100
#                 ypos 75+95*(i-1)
#                 ymaximum 95
#                 xmaximum 50
#                 if array_quest_log[i]:
#                     imagebutton:
#                         idle Transform('main_interface/quest_log/arrow_right_quest_log.png', xzoom = -1)
#                         hover Transform(im.MatrixColor('main_interface/quest_log/arrow_right_quest_log.png', im.matrix.brightness(.2)), xzoom = -1)
#                         action Function(def_array_quest_log, i = i, j =-5 )
#             viewport:
#                 xpos 610
#                 ypos 75+95*(i-1)
#                 ymaximum 95
#                 xmaximum 60
#                 if len(check_copies_quest_log(i)[array_quest_log[i]+5:5+5+array_quest_log[i]]):
#                     imagebutton:
#                         idle 'main_interface/quest_log/arrow_right_quest_log.png'
#                         hover im.MatrixColor('main_interface/quest_log/arrow_right_quest_log.png', im.matrix.brightness(.2))
#                         action Function(def_array_quest_log, i = i, j =+5)
#         vbox:

#             for i in [1, 2, 3, 4]:
#                 $ q_t_n = get_quest_log_time(i)
#                 viewport:
#                     xpos 140
#                     ypos 70
#                     ymaximum 95
#                     xmaximum 490





#                     add '#fff0'
#                     hbox:
#                         spacing 10

#                         yalign .5
#                         $ tmp_q_t_n = []
#                         for x in check_copies_quest_log(i)[array_quest_log[i]:5+array_quest_log[i]]:

#                             if x[1] not in tmp_q_t_n:
#                                 vbox:
#                                     ypos 10
#                                     viewport:
#                                         xalign .5

#                                         xmaximum 75
#                                         ymaximum 75

#                                         if i < time_now:
#                                             add 'phone_interface/avatars/'+x[1]+'.png' alpha .2 xalign .5 yalign .5
#                                             add 'quest_log_circle' xalign .5 yalign .5
#                                         else:
#                                             imagebutton:
#                                                 idle 'phone_interface/avatars/'+x[1]+'.png'
#                                                 hover im.MatrixColor('phone_interface/avatars/'+x[1]+'.png', im.matrix.brightness(.2))

#                                                 xalign .5 yalign .5
#                                                 if x[3][0] == '!':
#                                                     action [

#                                                 SetVariable('time_now', i), 
#                                                 Hide('quest_log_screen'),
#                                                 Function(change_location, get_location_for_quest_log(x[3][1:]), up_points_0 = time_now, up_points = i),
#                                                 Function(jump_to_event, x[3][1:], False, False),
                                                
                                                
                                                
#                                                 ]
#                                                 else:
#                                                     action [
                                                
#                                                 SetVariable('time_now', i), 
#                                                 Hide('quest_log_screen'),
#                                                 Function(change_location, x[3], up_points_0 = time_now, up_points = i),
                                                
                                                
                                                
#                                                 ]
#                                             add 'quest_log_circle' xalign .5 yalign .5 alpha .2
#                                     viewport ypos -15:
#                                         xalign .5

#                                         xmaximum 90
#                                         ymaximum 25
#                                         add '#0000'
#                                         if i >= time_now:

#                                             imagebutton:
#                                                 idle 'main_interface/quest_log/quest_log_skip.png'
#                                                 hover im.MatrixColor('main_interface/quest_log/quest_log_skip.png', im.matrix.brightness(.2))
#                                                 if x[3][0] == '!':
#                                                     action [

#                                                 SetVariable('time_now', i), 
#                                                 Hide('quest_log_screen'),
#                                                 Function(change_location, get_location_for_quest_log(x[3][1:]), up_points_0 = time_now, up_points = i),
#                                                 Function(jump_to_event, x[3][1:], False, False),
                                                
                                                
                                                
#                                                 ]
#                                                 else:
#                                                     action [

#                                                 SetVariable('time_now', i), 
#                                                 Hide('quest_log_screen'),
#                                                 Function(change_location, x[3], up_points_0 = time_now, up_points = i),
                                                
                                                
                                                
#                                                 ]

#                                             text str(x[1]) font 'fonts/h_font.ttf' size 10 xalign .5 yalign .5








#                             $ tmp_q_t_n.append(x[1])