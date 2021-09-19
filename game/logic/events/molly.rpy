label molly_events_label:


    #hide screen show_hide_locations
    #hide screen show_hide_locations_2
    hide screen text_animation_up_screen
    hide screen text_animation_up_screen_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.5)

    $ set_now =  molly_events_set
    menu:

        "Work" if Q_Molly==1:
            hide screen main_interface 
            hide screen show_hide_locations
            hide screen show_hide_locations_2
            hide screen text_animation_up_screen_3
            hide screen black_tmp_screen_menu
            with Dissolve(.5)

            show expression '#000' with Dissolve(.5)
            show sc i_Molly_1_1 with Dissolve(.5)
            "[Name]" "Molly!"
            "[Name]" "I've decided I'm ready to work."
            "[Name]" "Tell me what to do."
            show sc i_Molly_1_2 with my_dissolve
            "Molly" "That's cool! I could really use the help."
            "Molly" "I'll serve the guests."
            "Molly" "Be attentive, be on time."
            "Molly" "Maybe they'll even tip you."
            scene expression '#000' with Dissolve(.5)
            $ renpy.pause(.5)
            scene sc i_Activity_Work_1 with Dissolve(.5)
            "Molly" "Are you ready?"
            "[Name]" "Yeah, I'm ready. Let's go!"

            $ log_message.update({"QLOG_Molly":2})
            $ Q_Molly = 2

            
            jump test_coffe_game

        "Work" if Q_Molly==2:

            $ log_message.update({"QLOG_Molly":3})
            hide screen main_interface 
            hide screen show_hide_locations
            hide screen show_hide_locations_2
            hide screen text_animation_up_screen_3
            hide screen black_tmp_screen_menu

            scene sc i_Activity_Work_1
            with Dissolve(.5)
            $ p_up('Molly', 2)
            jump test_coffe_game
            $ change_location_2(location_now, time_now+1)
        "Not now" if True:

            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label
#molly_1_label
label cofe_event_1:
label coffe_event_1:

    
    show screen main_interface 
    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    scene cord_garden_1_door
    show screen black_tmp_screen_menu
    with Dissolve(.5)

    $ Event('coffe_event_1', 'cord_caffe', 'coffe_event_1', time = [1,])

    $ Event('coffe_event_1', 'cord_caffe_door', 'coffe_event_1', time = [1,])
    if hasattr(store, 'q_molly_block'):
        if day_now > q_molly_block:
            $ del q_molly_block
    menu:
        "Sneak a peek" if Q_Molly and not hasattr(store, 'q_molly_block'):
            $ pass

        "Closed" if not Q_Molly:
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            $ change_location(location = 'cord_garden_r')
        "Closed" if Q_Molly and hasattr(store, 'q_molly_block'):
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            $ change_location(location = 'cord_garden_r')
        "Walk away" if Q_Molly and not hasattr(store, 'q_molly_block'):
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            $ change_location(location = 'cord_garden_r')
    hide screen main_interface 


    $ q_molly_block = day_now






    if day_now%7 == 1:
        show sc i_Molly_0_13 with Dissolve(.5)
        "[Name]" "{i}(OMG, what's she doing?){/i}"
        "[Name]" "{i}(If someone's out there behind those windows...){/i}"
        show sc i_Molly_0_14 with my_dissolve
        "[Name]" "{i}(They'll see her body...){/i}"
        "[Name]" "{i}(Oh, wow...){/i}"
        show sc i_Molly_0_15 with my_dissolve
        "[Name]" "{i}(What a gorgeous body indeed...){/i}"
        "[Name]" "{i}(If only I could take a closer look...){/i}"
        show sc i_Molly_0_16 with my_dissolve
        "[Name]" "{i}(I knew Molly is hot, but...){/i}"
        "[Name]" "{i}(I'm impressed.){/i}"
        "[Name]" "{i}(Alarm! She's going to see me!){/i}"
        show sc i_Molly_0_17 with my_dissolve
        "[Name]" "{i}(Phew! That was close...){/i}"
    if day_now%7 == 2:
        show sc i_Molly_0_1 with Dissolve(.5)
        "[Name]" "{i}(Never thought I'd find window cleaning sexy.){/i}"
        "[Name]" "{i}(But Molly may be the one to change my mind.){/i}"
        show sc i_Molly_0_2 with my_dissolve
        "[Name]" "{i}(I've never had a boss that's so hot.){/i}"
        "[Name]" "{i}(It'd be hard to stick to a proper working relationship with this babe.){/i}"
        show sc i_Molly_0_3 with my_dissolve
        "[Name]" "{i}(Oh, shit, she's turning around! I'd better hide.){/i}"
        "[Name]" "{i}(Phew! That was close...){/i}"
    if day_now%7 == 3:

        show sc i_Molly_0_4 with Dissolve(.5)
        "[Name]" "{i}(Molly's cleaning again? She's so hardworking.){/i}"
        "[Name]" "{i}(Gosh, her skirt indeed does bad job at hiding something.){/i}"
        show sc i_Molly_0_5 with my_dissolve
        "[Name]" "{i}(It's like she wants me to take a look... Is this horrible to think so?){/i}"
        "[Name]" "{i}( I mean if that's not a view worth a risk...){/i}"
        "[Name]" "{i}(Than what is?){/i}"
        show sc i_Molly_0_6 with my_dissolve
        "[Name]" "{i}(Oh no, she's looking this way! I have to hide!){/i}"
        "[Name]" "{i}(Phew! That was close...){/i}"
    if day_now%7 == 4:

        show sc i_Molly_0_7 with Dissolve(.5)
        "[Name]" "{i}(Oh my, Molly... What are you doing to me?){/i}"
        "[Name]" "{i}(How can someone resist this view?){/i}"
        show sc i_Molly_0_8 with my_dissolve
        "[Name]" "{i}(This wakes up some wild animal instincts inside of me...){/i}"
        "[Name]" "{i}(I hope I can handle myself.){/i}"
        show sc i_Molly_0_9 with my_dissolve
        "[Name]" "{i}(Alarm! She's going to see me! I have to go!){/i}"
        "[Name]" "{i}(Phew! That was close...){/i}"
    if day_now%7 == 5:
        show sc i_Molly_0_10 with Dissolve(.5)
        "[Name]" "{i}(Is there something wrong with her shoes?){/i}"
        "[Name]" "{i}(It must be hard to work all days on those heels...){/i}"
        show sc i_Molly_0_11 with my_dissolve
        "[Name]" "{i}(But she looks fantastic, that's for sure...){/i}"
        "[Name]" "{i}(I would love to draw a picture of this if I were an artist...){/i}"
        show sc i_Molly_0_12 with my_dissolve
        "[Name]" "{i}(Oh. wait. she's going to my location, I have to run...){/i}"
        "[Name]" "{i}(Phew! That was close...){/i}"
    scene expression '#000' 

    hide screen black_tmp_screen_menu

    with Dissolve(.5)
    $ change_location(location = 'cord_garden_r')
    jump main_interface_label

#molly_2_label
label cofe_event_2:


    stop music_2 fadeout 1
    play music 'audio_ep2/SC/9. Hot coffee.mp3' fadein 2



    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface 
    scene expression 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png'
    show expression 'locations_main/items/caffe/cord_cafe_2.1.png'
    show expression 'locations_main/items/caffe/molly_cord_cafe_2.1.png'
    with Dissolve(.5)

    "[Name]" "{i}(Hmm, so this is the local cafe?){/i}"
    "[Name]" "{i}(It's not bad!){/i}"


    stop music 
    play music_2 'audio_ep2/SC/9. Hot coffee.mp3' fadein 2
    play sound_2 'audio/new/Music/intro1.mp3' fadein 1.0

    scene sc i_Molly_1_anim_1 with Dissolve(.5)
    $ renpy.pause(8.96, hard = True)
    "[Name]" "{i}(Oh! What do we have here?){/i}"
    "[Name]" "{i}(Is she a waitress or the best dish in the menu?){/i}"
    "[Name]" "{i}(Anyway, she looks pretty cute.){/i}"
    scene sc i_Molly_1_1 with Dissolve(.5)

    "[Name]" "{i}(A-and she's looking at me.){/i}"
    "[Name]" "{i}(I have to say something...{/i}"
    show sc i_Molly_1_1 with my_dissolve
    "[Name]" "Hi, I'm [Name] [Surname]."
    show sc i_Molly_1_2 with my_dissolve
    "Molly " "Oh, hi! My name is Molly."
    "Molly " "Haven't seen you here before. Are you new here?"
    show sc i_Molly_1_1 with my_dissolve
    "[Name]" "Yeah, freshman. Just looking around."
    show sc i_Molly_1_2 with my_dissolve
    "Molly " "That's cool! Congratulations."
    show sc i_Molly_1_1 with my_dissolve
    "[Name]" "This place looks very cozy."
    show sc i_Molly_1_2 with my_dissolve
    "Molly " "Thanks, that's nice to hear."
    "Molly " "Cup of something hot?"
    show sc i_Molly_1_1 with my_dissolve
    "[Name]" "No, thanks, I don't have any money right now..."
    show sc i_Molly_1_2 with my_dissolve
    "Molly " "Don't worry, it's my treat."
    show sc i_Molly_1_1 with my_dissolve
    "[Name]" "In that case..."

    menu:
        "A cup of tea" if True:
            $ pass
            show sc i_Molly_1_1 with my_dissolve
            "[Name]" "A cup of tea."
            "[Name]" "Black, no sugar."
        "A cup of coffee" if True:

            show sc i_Molly_1_1 with my_dissolve
            "[Name]" "I think I'll have a cup of coffee."
            "[Name]" "Black, no sugar."



    show sc i_Molly_1_12 with my_dissolve
    "Molly " "Just a minute!"
    show sc i_Molly_1_13 with my_dissolve
    "Molly " "Here you go!"
    "[Name]" "Thank you."
    show sc i_Molly_1_1 with my_dissolve
    "[Name]" "Are you a magician too?"
    show sc i_Molly_1_2 with my_dissolve
    "Molly " "No, an aspiring entrepreneur."
    show sc i_Molly_1_1 with my_dissolve
    "[Name]" "That's interesting."
    "[Name]" "So you got a job here as a waitress?"
    show sc i_Molly_1_2 with my_dissolve
    "Molly " "Not exactly."
    "Molly " "This is my cafe."
    show sc i_Molly_1_1 with my_dissolve
    "[Name]" "Really?"
    "[Name]" "Sorry, I thought you worked here as a waitress."
    show sc i_Molly_1_4 with my_dissolve
    "Molly " "I am."
    "Molly " "It's a small business. For now."
    "Molly " "So I work by myself."
    show sc i_Molly_1_1 with my_dissolve
    "[Name]" "That must be very hard!"
    show sc i_Molly_1_2 with my_dissolve
    "Molly " "It can be hard, but that's okay.{w} I can do it."
    show sc i_Molly_1_1 with my_dissolve
    "[Name]" "I know what I'm talking about."
    "[Name]" "I worked as a waiter for a while, I can imagine the workload."
    "[Name]" "I've been a bartender too."
    show sc i_Molly_1_6 with my_dissolve
    "Molly " "Really?"
    "[Name]" "Yes... I needed something to do after I broke my leg."
    "[Name]" "Long story."
    "Molly " "Hmm... What if?"
    show sc i_Molly_1_7 with my_dissolve
    "Molly " "[Name], I had a crazy idea!"
    "Molly " "You said you were broke..."
    "Molly " "How would you like to get a {b}part-time job?{/b}"
    show sc i_Molly_1_6 with my_dissolve
    "[Name]" "Wow. That's an unexpected offer."
    "[Name]" "You're inviting all strangers to work?"
    show sc i_Molly_1_10 with my_dissolve
    "Molly " "Ah-ha-ha."
    "Molly " "No. But I got a hunch about you!"
    "Molly " "And my instincts never fail me."
    show sc i_Molly_1_12 with my_dissolve
    "Molly " "Especially since you already gave me your full name."
    "Molly " "If anything goes wrong, I'll find you..."
    show sc i_Molly_1_1 with my_dissolve
    "[Name]" "Heh heh..."
    "[Name]" "{i}(Creepy...){/i}"
    menu:
        "Agree" if True:


            show sc i_Molly_1_1 with my_dissolve
            "[Name]" "Sounds too good to refuse!"
            show sc i_Molly_1_12 with my_dissolve
            "Molly " "Does it? That's great!"
            "Molly " "Then come back in the afternoon or evening when you have some free time."
            "Molly " "It never hurts to have extra hands."
            show sc i_Molly_1_11 with my_dissolve
            "[Name]" "It's a deal."
        "Refuse" if True:


            show sc i_Molly_1_1 with my_dissolve
            "[Name]" "I don't know. I'll have to think about it..."
            show sc i_Molly_1_4 with my_dissolve
            "Molly " "All right, then."
            "Molly " "If you decide to do it, come back when you have some free time."
            "Molly " "I could use an extra pair of hands."
            show sc i_Molly_1_3 with my_dissolve
            "[Name]" "All right."







    $ log_message.update({"QLOG_Molly":1 })
    $ Q_Molly = 1
    $ p_up('Molly', 1)
    
    scene expression '#000' with Dissolve(.5)
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
