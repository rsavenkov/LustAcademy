



label lily_events_label:

    call hide_all_main_interfaces from _call_hide_all_main_interfaces_5
    $ set_now = lily_events_set
    menu:

        "0 Talk to Lily" if Q_Lily==0:

            call Lily_1_label from _call_Lily_1_label
            $ p_up('Lily', 2)

            $ log_message.update({"QLOG_Lily":2 })
            $ Q_Lily=1
            $ lily_events_set.append("1 Talk to Lily")
            $ wakeup_sets.append([

            
            lily_events_set, "1 Talk to Lily"
            
            
                ])

        "1 Talk to Lily" if Q_Lily==1:
            if Q_Victoria<1:
                call Lily_1_1_label from _call_Lily_1_1_label
                $ lily_events_set.append("1 Talk to Lily")
                $ wakeup_sets.append([

                
                lily_events_set, "1 Talk to Lily"
                
                
                    ])

                $ log_message.update({"QLOG_Lily":2})
            elif True:
                call Lily_2_label from _call_Lily_2_label
                $ p_up('Lily', 3)
                $ Q_Lily=2

                $ log_message.update({"QLOG_Lily":3})


        "2 Talk to Lily" if Q_Lily==2:
            if books_send<3:

                call Lily_1_2_label from _call_Lily_1_2_label

                $ log_message.update({"QLOG_Lily":3 })
                $ lily_events_set.append("2 Talk to Lily")
                $ wakeup_sets.append([

                
                lily_events_set, "2 Talk to Lily"
                
                
                    ])
                $ log_message.update({"QLOG_Lily":2})
            elif True:

                call Lily_3_label from _call_Lily_3_label
                $ p_up('Lily', 4)
                $ Q_Lily=3

                $ log_message.update({"QLOG_Lily":4})

        "3 Talk to Lily" if Q_Lily==3:
            if hasattr(store, 'Win_Adderin') and Win_Adderin:

                call Lily_1_3_label from _call_Lily_1_3_label

                $ log_message.update({"QLOG_Lily":4})
                $ lily_events_set.append("3 Talk to Lily")
                $ wakeup_sets.append([

                
                lily_events_set, "3 Talk to Lily"
                
                
                    ])
            elif True:

                call Lily_1_4_label from _call_Lily_1_4_label

                $ log_message.update({"QLOG_Lily":5 })
                $ lily_events_set.append("3 Talk to Lily")
                $ wakeup_sets.append([

                
                lily_events_set, "3 Talk to Lily"
                
                
                    ])
        "Not now" if True:

            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label



label lily_events_2_label:
    call hide_all_main_interfaces from _call_hide_all_main_interfaces_6

    $ set_now = lily_events_set_2
    menu:



        "0 Talk to Lily" if Q_Lily==0:

            call Lily_2_1_label from _call_Lily_2_1_label

            $ log_message.update({"QLOG_Lily":1 })
            $ lily_events_set_2.append("0 Talk to Lily")
            $ wakeup_sets.append([

                
                lily_events_set_2, "0 Talk to Lily"
                
                
                    ])
        "1 Talk to Lily" if Q_Lily==1:
            if Q_Victoria == 0:

                call Lily_2_2_label from _call_Lily_2_2_label

                $ log_message.update({"QLOG_Lily":2})
                $ lily_events_set_2.append("1 Talk to Lily")
                $ wakeup_sets.append([

                
                lily_events_set_2, "1 Talk to Lily"
                
                
                    ])
            elif True:
                call Lily_2_3_label from _call_Lily_2_3_label

                $ log_message.update({"QLOG_Lily":1})
                $ lily_events_set_2.append("1 Talk to Lily")
                $ wakeup_sets.append([

                
                lily_events_set_2, "1 Talk to Lily"
                
                
                    ])

        "2 Talk to Lily" if Q_Lily==2:
            if books_send<3:

                call Lily_2_4_label from _call_Lily_2_4_label

                $ log_message.update({"QLOG_Lily":3 })
                $ lily_events_set_2.append("2 Talk to Lily")
                $ lily_events_set_2.append([

                
                lily_events_set_2, "2 Talk to Lily"
                
                
                    ])
                $ log_message.update({"QLOG_Lily":2})
            elif True:

                call Lily_2_5_label from _call_Lily_2_5_label


                $ log_message.update({"QLOG_Lily":1})
                $ lily_events_set_2.append("2 Talk to Lily")
                $ lily_events_set_2.append([

                
                lily_events_set_2, "2 Talk to Lily"
                
                
                    ])

        "3 Talk to Lily" if Q_Lily==3:
            if hasattr(store, 'Win_Adderin') and Win_Adderin:
                call Lily_2_6_label from _call_Lily_2_6_label

                $ log_message.update({"QLOG_Lily":4})
                $ lily_events_set_2.append("3 Talk to Lily")
                $ wakeup_sets.append([

                
                lily_events_set_2, "3 Talk to Lily"
                
                
                    ])
            elif True:
                call Lily_2_7_label from _call_Lily_2_7_label

                $ log_message.update({"QLOG_Lily":5 })
                $ lily_events_set_2.append("3 Talk to Lily")
                $ wakeup_sets.append([

                
                lily_events_set_2, "3 Talk to Lily"
                
                
                    ])
        "5 Talk to Lily" if Q_Lily == 5:

            hide screen show_hide_locations
            hide screen show_hide_locations_2
            hide screen text_animation_up_screen_3
            hide screen main_interface
            scene image '#000' 
            with Dissolve(.5)
            call Lily_6_label from _call_Lily_6_label
            scene image '#000' with Dissolve(.5)
            $ Q_Lily = 6
            $ p_up('Lily', 7)
            $ change_location_2('leon_room_mc', 4)
        "Not now" if True:
            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label

    hide screen black_tmp_screen_menu


    jump main_interface_label

label lily_events_3_label:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.5)

    $ set_now = lily_events_set_3
    menu:


        "0 Talk to Lily" if Q_Lily==0:

            call Lily_3_1_label from _call_Lily_3_1_label

            $ log_message.update({"QLOG_Lily":1})
            $ lily_events_set_3.append("0 Talk to Lily")
            $ wakeup_sets.append([

            
            lily_events_set_3, "0 Talk to Lily"
            
            
                ])
        "1 Talk to Lily" if Q_Lily==1:

            if Q_Victoria==0:
                call Lily_3_2_label from _call_Lily_3_2_label
                $ lily_events_set_3.append("1 Talk to Lily")
                $ wakeup_sets.append([

                
                lily_events_set_3, "1 Talk to Lily"
                
                
                    ])

                $ log_message.update({"QLOG_Lily":2})
            elif True:
                call Lily_3_3_label from _call_Lily_3_3_label

                $ log_message.update({"QLOG_Lily":1})
                $ lily_events_set_3.append("1 Talk to Lily")
                $ wakeup_sets.append([

                
                lily_events_set_3, "1 Talk to Lily"
                
                
                    ])
        "2 Talk to Lily" if Q_Lily==2:

            if books_send<3:

                call Lily_3_4_label from _call_Lily_3_4_label

                $ log_message.update({"QLOG_Lily":3 })
                $ lily_events_set_3.append("2 Talk to Lily")
                $ wakeup_sets.append([

                
                lily_events_set_3, "2 Talk to Lily"
                
                
                    ])
                $ log_message.update({"QLOG_Lily":3})
            elif True:

                call Lily_3_5_label from _call_Lily_3_5_label



                $ log_message.update({"QLOG_Lily":1})

        "3 Talk to Lily" if Q_Lily==3:

            if hasattr(store, 'Win_Adderin') and Win_Adderin:

                call Lily_3_6_label from _call_Lily_3_6_label

                $ log_message.update({"QLOG_Lily":4})
                $ lily_events_set.append("3 Talk to Lily")
                $ wakeup_sets.append([

                
                lily_events_set, "3 Talk to Lily"
                
                
                    ])
            elif True:

                call Lily_4_label from _call_Lily_4_label
                $ p_up('Lily', 5)
                $ Q_Lily=4

                $ log_message.update({"QLOG_Lily":6 })

                $ change_location_2(location_now, time_now+1)
                $ lily_view_5 = False
                $ lily_view_4 = True
        "Not now" if True:

            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label



label lily_events_4_label:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.5)

    $ set_now = lily_events_set_4
    menu:
        "4 Talk to Lily" if True:

            $ unlock_gallery('images/ero/Lily.png')

            call Lily_5_label from _call_Lily_5_label
            $ p_up('Lily', 6)
            $ Q_Lily=5
            if persistent.from_gallery:

                scene expression '#000' with Dissolve(1)
                $ renpy.full_restart()
            $ log_message.update({"QLOG_Lily":7})

            $ change_location_2(location_now, time_now+1)
            $ lily_view_5 = True
            $ lily_view_4 = False
        "Not now" if True:

            if persistent.from_gallery:
                hide screen main_interface 
                scene expression '#000'
                with Dissolve(1)
                $ renpy.full_restart()
            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label
































label Lily_1_label:

    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2


    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)

    show sc i_Lily_1_1 with Dissolve(.5)
    "[Name]" "{i}(Oh, that cute Asian girl who's obsessed with Leonheart.){/i}"
    "[Name]" "{i}(I think her name is Lily.){/i}"
    "[Name]" "Hi, Lily!{w} How are you?"
    show sc i_Lily_1_2 with my_dissolve
    "Lily" "Oh, hello there!"
    show sc i_Lily_1_3 with my_dissolve
    "Lily" "You...{w} Wait, I remember..."
    "Lily" "[Name], right?"
    show sc i_Lily_1_3 with my_dissolve
    "[Name]" "{i}(It's always nice when a cutie remembers your name.){/i}"
    show sc i_Lily_1_9 with my_dissolve
    "[Name]" "Yeah."
    "[Name]" "Congratulations on getting into Leonheart like you wanted."
    show sc i_Lily_1_5 with my_dissolve
    "Lily" "Thank you!"
    "Lily" "It couldn't have gone any other way."
    "Lily" "But I was so happy in that moment!"
    show sc i_Lily_1_11 with my_dissolve
    "Lily" "You got in, too, right?"
    "[Name]" "That's right."
    show sc i_Lily_1_15 with my_dissolve
    "Lily" "That's great! I'm so happy!"
    "[Name]" "You are?"
    "[Name]" "Why is that?"
    show sc i_Lily_1_19 with my_dissolve
    "Lily" "I knew right away there was something special about you."
    "Lily" "And I'm rarely wrong about people."
    "Lily" "The house needs mages like you!"
    "[Name]" "{i}(She's new here, and she's already talking like a prefect.){/i}"
    "[Name]" "{i}(Elijah should be worried about his position.){/i}"
    show sc i_Lily_1_17 with my_dissolve
    "[Name]" "Oh, don't make me blush."
    "[Name]" "I'm glad to be on the team with you too, Lily."
    "[Name]" "Though I really don't know how freshmen can help the house..."
    show sc i_Lily_1_12 with my_dissolve
    "Lily" "Are you kidding me? It's all in our hands!"
    "[Name]" "Really?"
    "Lily" "Every point counts!"
    "Lily" "It's every student's job to fight for their house."
    show sc i_Lily_1_9 with my_dissolve
    "[Name]" "So that's how it is."
    "[Name]" "Still, isn't it more important that we study now?"
    "[Name]" "I just don't get it, if the house wins the competition, so what?"
    show sc i_Lily_1_3 with my_dissolve
    "Lily" "So what?"
    "Lily" "It's prestige and influence."
    "Lily" "The whole magical world watches the results of house battles."
    show sc i_Lily_1_11 with my_dissolve
    "Lily" "It's a great line on a résumé."
    "Lily" "At the very least!"
    "[Name]" "If you say so."
    "[Name]" "{i}(So you're just an adorable little careerist?){/i}"
    "[Name]" "Sounds really useful."
    "[Name]" "Then I'm in."
    show sc i_Lily_1_15 with my_dissolve
    "Lily" "Really?!"
    "[Name]" "{i}(Why is she so surprised?){/i}"
    "[Name]" "{i}(How many people has she already tried to impose her housebattles on?!){/i}"
    "[Name]" "Well, yeah. I'm going to try at least."
    show sc i_Lily_1_17 with my_dissolve
    "Lily" "Oh, great!"
    "Lily" "The two of us together will be much able to stand up to Naomi and her stupid Adderin..."
    "[Name]" "{i}(Oh, so that's the real reason.){/i}"
    "[Name]" "{i}(You have a fundamental disagreement with your girlfriend.){/i}"
    "[Name]" "{i}(I bet you'd do anything you could rub her nose in.){/i}"
    show sc i_Lily_1_19 with my_dissolve
    "Lily" "It's decided!"
    "[Name]" "What's decided?!"
    show sc i_Lily_1_10 with my_dissolve
    "Lily" "We are definitely not going to lose the faculty race to Naomi!"
    "[Name]" "Ah-ha-ha-ha-ha-ha-ha-ha-ha-ha-ha-ha!"
    show sc i_Lily_1_6 with my_dissolve
    "Lily" "What is it?!"
    "[Name]" "No, no, I'm sorry."
    "[Name]" "You're just so cute when you're motivated."
    show sc i_Lily_1_5 with my_dissolve
    "Lily" "Stop it! I'm blushing."
    "[Name]" "And that just makes you prettier!"
    show sc i_Lily_1_3 with my_dissolve
    "Lily" "Aah! You're insufferable."
    "Lily" "Let's just focus on our goal!"
    "[Name]" "Sure, no problem."
    "[Name]" "Our main goal is house points, right?"
    show sc i_Lily_1_4 with my_dissolve
    "Lily" "That's right."
    "[Name]" "Then we should start with studying."
    "[Name]" "Let's go to class, look around, and make a plan."
    show sc i_Lily_1_1 with my_dissolve
    "Lily" "[Name]... You're so meticulate about this!"
    "Lily" "I didn't expect..."
    "[Name]" "Is it bad?"
    "Lily" "Are you kidding?"
    show sc i_Lily_1_17 with my_dissolve
    "Lily" "If it wasn't so crowded, I'd kiss you!"
    "[Name]" "Ah-ha-ha. I'll keep that in mind."
    "Lily" "So we go to class now, and then..."
    "[Name]" "We meet and discuss the plan."
    show sc i_Lily_1_21 with my_dissolve
    "Lily" "Great! It's a deal."
    "[Name]" "Then see you later!"
    return


label Lily_2_label:

    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2

    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)

    show sc i_Lily_1_21 with Dissolve(.5)
    "[Name]" "Hi!"
    "[Name]" "What are you doing?"
    show sc i_Lily_1_14 with my_dissolve
    "Lily" "Hi there!"
    "Lily" "Nothing exciting."
    "Lily" "Just getting ready for class."
    "[Name]" "I thought you got house points for attending."
    "[Name]" "Or are you here for something else?"
    show sc i_Lily_1_12 with my_dissolve
    "Lily" "I'm here for points."
    "Lily" "But knowledge never hurts."
    "[Name]" "Well said."
    "[Name]" "I'm trying to mix business with pleasure too."
    show sc i_Lily_1_11 with my_dissolve
    "Lily" "Really?"
    "Lily" "And how's the point collection going?"
    "[Name]" "Well..."
    show sc i_Lily_1_8 with my_dissolve
    "[Name]" "I'm in the preparatory phase."
    "[Name]" "I'm trying not to miss any classes."
    "Lily" "That's a good start."
    show sc i_Lily_1_11 with my_dissolve
    "Lily" "I have a few more ideas on how to score points!"
    "[Name]" "{i}(Your enthusiasm scares me...{/i}"
    "[Name]" "Tell me about it!"
    show sc i_Lily_1_5 with my_dissolve
    "Lily" "I had a talk with our librarian Amelie."
    "Lily" "Did you know that the {b}local magical creatures steal textbooks{/b}?"
    "[Name]" "Yeah."
    "Lily" "And that they leave them all over the academy?"
    "[Name]" "She told me."
    show sc i_Lily_1_3 with my_dissolve
    "Lily" "And you didn't say anything?!"
    "[Name]" "Well... why does it matter?"
    "Lily" "Because Amelie gives faculty points for books!"
    "Lily" "It's our chance to rub everyone's nose in it."
    show sc i_Lily_1_19 with my_dissolve
    "Lily" "And it's something to do in our spare time! Awesome!"
    "[Name]" "{i}(Do you really want to wander around the Academy looking for books?){/i}"
    "Lily" "If we do this together, then..."
    "[Name]" "{i}(Ah, you want us to do it together...){/i}"
    show sc i_Lily_1_14 with my_dissolve
    "Lily" "...we can definitely win the house competition!"
    "[Name]" "Sounds like a plan."
    show sc i_Lily_1_1 with my_dissolve
    "Lily" "Let's make a deal: we'll each return three books."
    "Lily" "And then we'll discuss our future plans."
    show sc i_Lily_1_11 with my_dissolve
    "Lily" "Deal?"
    "[Name]" "Sure.{w} Consider the books on Amelie's desk."
    "[Name]" "And the house points already on Leonheart's scoreboard."
    show sc i_Lily_1_17 with my_dissolve
    "Lily" "Yes!"
    "Lily" "That's the spirit!"
    "Lily" "Good luck, champ!"
    show sc i_Lily_1_18 with my_dissolve
    "[Name]" "{i}(That's right.){/i}"
    "[Name]" "{i}(She's a Leonheart fanatic, what did I expect?){/i}"
    "[Name]" "Thanks."
    return


label Lily_3_label:

    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2


    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)
    show sc i_Lily_1_1 with Dissolve(.5)
    "[Name]" "Lily, hey!"
    "Lily" "Hey, [Name]!"
    "Lily" "How's it going?"
    "[Name]" "I'm doing the best."
    show sc i_Lily_1_4 with my_dissolve
    "Lily" "You are?"
label Lily_3_label_8:
    show sc i_Lily_1_4 with my_dissolve
    "[Name]" "Sure."
    show sc i_Lily_1_15 with my_dissolve
    "[Name]" "I found the books and earned house points for us."
    "Lily" "Nice! You've done it!"
    "Lily" "I never doubted you!"
    show sc i_Lily_1_16 with my_dissolve
    "[Name]" "Really?{w} You look surprised."
    show sc i_Lily_1_17 with my_dissolve
    "Lily" "I'm just really happy!"
    "[Name]" "Are you?"
    "[Name]" "And how are you doing?"
    show sc i_Lily_1_12 with my_dissolve
    "Lily" "I couldn't find the third textbook until the very end."
    "Lily" "Damn pixies threw it behind an ancient tapestry."
    show sc i_Lily_1_4 with my_dissolve
    "Lily" "I swallowed a lot of dust..."
    "[Name]" "Poor thing."
    "[Name]" "Mine weren't easy either."
    "[Name]" "But Sherlock [Surname] will find it all!"
    show sc i_Lily_1_15 with my_dissolve
    "Lily" "Ah-ha-ha!"
    "[Name]" "I can't help it, that's me."
    "[Name]" "Well, I'm off to get us some more points!"
    "Lily" "Ah-ha-ha!"
    "Lily" "Stop it, I'll get tired of laughing at this rate."
    "[Name]" "That wasn't a joke."
    show sc i_Lily_1_13 with my_dissolve
    "Lily" "Oh."
    "[Name]" "What?"
    show sc i_Lily_1_12 with my_dissolve
    "Lily" "Wait, was that really your plan?"
    "Lily" "Just walk around and score points."
    show sc i_Lily_1_13 with my_dissolve
    "[Name]" "I deduce that you're having doubts about my plan."
    "Lily" "Well, yeah, a little bit."
    show sc i_Lily_1_14 with my_dissolve
    "Lily" "Everyone takes classes, it's not a revelation."
    "Lily" "And turning in books is child's play."
    "Lily" "I know a way to not only earn points for us, but also..."
    show sc i_Lily_1_11 with my_dissolve
    "Lily" "Take them away from the other houses!"
    "[Name]" "{i}(Is that even legal?){/i}"
    "[Name]" "I'm listening."
    show sc i_Lily_1_19 with my_dissolve
    "Lily" "{b}We have to win at the dueling club!{/b}"
    "[Name]" "Ah, that's what you mean..."
    "Lily" "That's what I'm talking about!"
    "Lily" "And right now it's especially important that we beat Adderin."
    show sc i_Lily_1_6 with my_dissolve
    "[Name]" "Because Naomi's there?"
    show sc i_Lily_1_3 with my_dissolve
    "Lily" "No.{w} That's not the only reason."
    "Lily" "They score too many points."
    "Lily" "If we fall behind now, we'll never catch up."
    show sc i_Lily_1_10 with my_dissolve
    "[Name]" "Let me handle this."
    "Lily" "I'm not sure you can..."
    show sc i_Lily_1_12 with my_dissolve
    "[Name]" "Let's make a bet."
    show sc i_Lily_1_14 with my_dissolve
    "Lily" "A bet?"
    "[Name]" "Yeah, a friendly bet."
    "[Name]" "If Leonheart takes Adderin's points in a duel, I win..."
    "[Name]" "And if it loses, you win."
    show sc i_Lily_1_17 with my_dissolve
    "Lily" "All right, it's a deal."
    "Lily" "But if I win, you'll obey my orders for a month."
    "[Name]" "{i}(Hmm... To be enslaved for a month by a hot Asian girl?){/i}"
    "[Name]" "{i}(Though what good would it do if it isn't sexual...){/i}"
    show sc i_Lily_1_9 with my_dissolve
    "[Name]" "Okay. And if I win, I want one kiss."
    show sc i_Lily_1_15 with my_dissolve
    "Lily" "A what-what?"
    "Lily" "Have you lost your mind, [Name]?"
    show sc i_Lily_1_13 with my_dissolve
    "[Name]" "No, I'm as serious as can be."
    "[Name]" "You win either way."
    "[Name]" "And I get extra motivation to tear Adderin up."
    "Lily" "...."
    show sc i_Lily_1_19 with my_dissolve
    "Lily" "All right."
    "Lily" "If you win, you'll get a kiss. But you'll lose."
    show sc i_Lily_1_3 with my_dissolve
    "[Name]" "We'll see."
    show sc i_Lily_1_19 with my_dissolve
    "Lily" "We'll see."
    "[Name]" "Good luck."
    return


label Lily_4_label:

    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2

    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)

    show sc i_Lily_2_1 with Dissolve(.5)
    "[Name]" "Hey, guys!"
    "[Name]" "Lily, can I talk to you for a minute?"
    show sc i_Lily_2_2 with my_dissolve
    "Lily" "Hi!"
    "Lily" "Uh, yeah, sure."
    "Lily" "Naomi, do you mind?"
    show sc i_Lily_2_8 with my_dissolve
    "Naomi" "What's it to me?"
    "Lily" "We won't be long."
    show sc i_Lily_2_9 with my_dissolve
    "Lily" "What do you want, [Name]?"
    "[Name]" "I think you'll be happy to know that our house won the duel."
    show sc i_Lily_2_20 with my_dissolve
    "Lily" "Cool! Why are you telling me this?"
    show sc i_Lily_2_21 with my_dissolve
    "[Name]" "We had a bet."
    show sc i_Lily_2_20 with my_dissolve
    "Lily" "Wait...{w} Are you saying...?{w} No!"
    "[Name]" "Yes!"
    "Lily" "Was it you?"
    "[Name]" "I told you it would be easy."
    show sc i_Lily_2_25 with my_dissolve
    "Lily" "But how did you do it?"
    "[Name]" "A professional never reveals his methods."
    "Lily" "Spit it out!"
    show sc i_Lily_2_24 with my_dissolve
    "[Name]" "All right, all right."
    "[Name]" "I'll tell you this story somewhere private."
    show sc i_Lily_2_19 with my_dissolve
    "Lily" "Private?"
    "[Name]" "Of course."
    "[Name]" "Remember that bet we made?"
    show sc i_Lily_2_17 with my_dissolve
    "Lily" "Yeah. What does that have to do with..."
    "[Name]" "No, well, you wanted to give me my prize here?"
    show sc i_Lily_2_21 with my_dissolve
    "[Name]" "In front of everybody?"
    show sc i_Lily_2_20 with my_dissolve
    "Lily" "Oh... Yeah, you're right."
    "Lily" "I'm just a little busy right now."
    show sc i_Lily_2_21 with my_dissolve
    "[Name]" "Of course.{w} I'm not rushing you at all."
    "Lily" "Thanks."
    "Lily" "I have an idea!"
    show sc i_Lily_2_22 with my_dissolve
    "Lily" "Why don't we {b}meet in your room when it gets dark? {/b}"
    "[Name]" "Whoa, just like that, at my place?"
    show sc i_Lily_2_23 with my_dissolve
    "Lily" "Haley and I share a room."
    "Lily" "I think it would be easier at your place."
    "[Name]" "Easier to do what?"
    show sc i_Lily_2_25 with my_dissolve
    "Lily" "Talk, discuss our next move."
    "[Name]" "Oh, I thought you meant our bet..."
    show sc i_Lily_2_19 with my_dissolve
    "Lily" "Damn it, [Name]! You want me to say it?"
    "Lily" "Yeah, and it's easier to make out there, too."
    show sc i_Lily_2_18 with my_dissolve
    "[Name]" "Heh.{w} Did I insist that much?"
    "[Name]" "Just clarifying."
    "[Name]" "You're the one talking loudly about our future makeout..."
    show sc i_Lily_2_27 with my_dissolve
    "Lily" "I can't stand you sometimes!"
    "[Name]" "You'll get over it."
    "[Name]" "See you later."
    return

label Lily_5_label:

    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/17. Dreams.mp3' fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/17. Dreams.mp3' fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/17. Dreams.mp3' fadein 2

    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)

    show sc i_Lily_5_1 with Dissolve(.5)
    "[Name]" "Hey, Lily!"
    "[Name]" "I didn't think you'd be here so soon."
    show sc i_Lily_5_2 with my_dissolve
    "Lily" "[Name], h-hi!"
    "Lily" "Why wait? I have to get up early tomorrow."
    "Lily" "I'm going for a morning run."
    "[Name]" "That's cool. I'd go with you if it wasn't for my leg injury."
    "Lily" "Then let's go running together."
    show sc i_Lily_5_3 with my_dissolve
    "Lily" "When you heal your leg."
    "[Name]" "Sure."
    "Lily" "You got a cool room."
    "Lily" "Isn't Leonheart's dorm awesome?"
    "Lily" "This room is even cooler than ours."
    "[Name]" "You think so?"
    "Lily" "At least you don't have to share it with anyone."
    "[Name]" "Probably. But that's not always a plus."
    show sc i_Lily_5_4 with my_dissolve
    "Lily" "What do you mean?"
    "[Name]" "Well...{w} I have a double bed."
    "[Name]" "It's kind of lonely on my own..."
    show sc i_Lily_5_5 with my_dissolve
    "Lily" "[Name]!"
    "[Name]" "I was just kidding."
    show sc i_Lily_5_6 with my_dissolve
    "[Name]" "Do you really like everything here?"
    "[Name]" "I think you'll change a lot when you're a prefect."
    show sc i_Lily_5_7 with my_dissolve
    "Lily" "Do you really think I can be the prefect?"
    show sc i_Lily_5_8 with my_dissolve
    "[Name]" "Somehow I don't doubt it."
    "Lily" "In fact, I did have a couple of ideas for improving our campus."
    "[Name]" "{i}(Who would have doubted it?){/i}"
    "Lily" "But it's pretty cool as it is."
    "Lily" "Elijah's a great guy, even though he's pretty irresponsible."
    "[Name]" "I got that impression, too."
    "[Name]" "That he's cool, not that he's irresponsible..."
    "[Name]" "Although if you think about it, you're probably right."
    show sc i_Lily_5_9 with my_dissolve
    "[Name]" "{i}(Lily looks a little stiff, she seems nervous.){/i}"
    "[Name]" "Lily..."
    show sc i_Lily_5_10 with my_dissolve
    "Lily" "What?"
    "[Name]" "About our bet."
    "Lily" "I was hoping you'd forget while we were chatting."
    "Lily" "Uh..."
    "[Name]" "You really don't like me?"
    show sc i_Lily_5_11 with my_dissolve
    "Lily" "No, that's not it!"
    "[Name]" "What is it?"
    show sc i_Lily_5_12 with my_dissolve
    "Lily" "It's just that I've never kissed anyone before..."
    "Lily" "Okay, let's get it over with."
    show sc i_Lily_5_13 with my_dissolve
    "[Name]" "Lily..."
    "Lily" "What?"
    "[Name]" "I don't know how to say this..."
    show sc i_Lily_5_14 with my_dissolve
    "[Name]" "But I don't want a kiss like that."
    "Lily" "Huh?{w} I don't get it..."
    "Lily" "What do you mean?"
    show sc i_Lily_5_6 with my_dissolve
    "[Name]" "The first kiss should be special."
    "[Name]" "I don't want to be the jerk who steals it because of a stupid bet."
    "[Name]" "I didn't even know..."
    "Lily" "[Name]..."
    show sc i_Lily_5_15 with my_dissolve
    "Lily" "No way!"
    "[Name]" "I'm sorry, I didn't realize..."
    "Lily" "I spent all day getting ready."
    "Lily" "I imagined what it would be like."
    "Lily" "I am prepared!"
    "Lily" "And now you say you don't want to kiss me."
    show sc i_Lily_5_16 with my_dissolve
    "[Name]" "Wait a minute..."
    show sc i_Lily_5_17 with my_dissolve
    "Lily" "Do you have any idea how I feel?"
    show sc i_Lily_5_16 with my_dissolve
    "[Name]" "I thought you'd be happy."
    show sc i_Lily_5_17 with my_dissolve
    "Lily" "About what?"
    "Lily" "That a cute guy doesn't want to kiss me?"
    "[Name]" "{i}(Cute?){/i}"
    show sc i_Lily_5_6 with my_dissolve
    "[Name]" "What makes you think I don't want to?"
    show sc i_Lily_5_7 with my_dissolve
    "Lily" "Do you want to?"
    show sc i_Lily_5_6 with my_dissolve
    "[Name]" "Yes!"
    show sc i_Lily_5_18 with my_dissolve
    "Lily" "Yes?"
    "[Name]" "Yes!"
    show sc i_Lily_5_19 with my_dissolve
    "[Name]" "{i}(Whoa!){/i}"
    "[Name]" "{i}(Lily, for a first time - that was good.){/i}"
    scene sc i_Lily_5_anim_1 with Dissolve(.5)
    "[Name]" "{i}(Did she really want it that badly?){/i}"
    scene sc i_Lily_5_anim_2 with Dissolve(.5)
    "[Name]" "{i}(She attacked me like a lioness going after her prey.){/i}"
    scene sc i_Lily_5_anim_3 with Dissolve(.5)
    "[Name]" "{i}(And she looked so shy...){/i}"

    menu:
        "Ask about her feelings" if True:
            $ pass
        "Keep kissing Lily" if True:
            jump Lily_5_label_101
    scene sc i_Lily_5_20 with Dissolve(.5)
    "[Name]" "Lily..."
    "Lily" "Yes?"
    "[Name]" "How do you feel?"
    "Lily" "I... I like it..."
    "Lily" "I'm sorry if I'm doing something wrong!"
    "[Name]" "Don't be silly, Lily."
    "[Name]" "You're really something..."
    show sc i_Lily_5_21 with my_dissolve
    "Lily" "Really? I tried."
    "[Name]" "You took me by surprise."
    "[Name]" "{i}(I hope I didn't mess up.){/i}"
    "[Name]" "So, what did you think?"
    show sc i_Lily_5_22 with my_dissolve
    "Lily" "It was nice."
    "[Name]" "{i}(Is that all? I didn't impress you very much...){/i}"
    "[Name]" "{i}(I thought you got a taste for it...){/i}"
    "Lily" "But why did you stop?"
    "[Name]" "Why?"
    show sc i_Lily_5_23 with my_dissolve
    "[Name]" "It could have lasted much longer than a friendly kiss."
    "Lily" "I didn't know there were levels of kissing."
    "[Name]" "Well...{w} How to put it? Kinda."
    show sc i_Lily_5_24 with my_dissolve
    "Lily" "I don't mind exploring that distinction in more detail."
    "[Name]" "{i}(I think I was right after all!){/i}"
    "[Name]" "{i}(She clearly doesn't mind if we keep going...){/i}"
    "[Name]" "In that case..."
label Lily_5_label_101:

    scene sc i_Lily_5_25 with vpunch
    "Lily" "Mhm..."
    "[Name]" "{i}(You obviously don't mind continuing.){/i}"
    scene sc i_Lily_5_anim_4
    "[Name]" "{i}(How can I say no?){/i}"
    scene sc i_Lily_5_anim_5 with Dissolve(.5)
    "[Name]" "{i}(You seem so shy...){/i}"
    scene sc i_Lily_5_anim_6 with Dissolve(.5)
    "[Name]" "{i}(But your tongue isn't shy at all.){/i}"
    scene sc i_Lily_5_anim_4 with Dissolve(.5)
    "[Name]" "{i}(You're obviously a natural at kissing.){/i}"
    scene sc i_Lily_5_anim_5 with Dissolve(.5)
    "Lily" "{i}(What is this... I can't control myself at all...){/i}"

    "Lily" "{i}(What's that strange feeling below the belly when we kiss...){/i}"
    scene sc i_Lily_5_anim_6 with Dissolve(.5)
    "[Name]" "{i}(I don't think Lily has ever been this close to a guy before.){/i}"

    "[Name]" "{i}(Maybe help her catch up on what she missed in high school.){/i}"

    menu:
        "Stop kissing" if True:
            $ pass
        "Touch Lily" if True:
            jump Lily_5_label_130
    show sc i_Lily_5_27 with my_dissolve
    "[Name]" "{i}(Okay, she's done for the day.){/i}"
    "Lily" "Ah..."
    "Lily" "[Name], I..."
    "[Name]" "Shh!"
    "[Name]" "Don't say anything."
    "[Name]" "I think I've had enough for today."
    "[Name]" "Let's discuss the faculty points plan some other time."
    show sc i_Lily_5_28 with my_dissolve
    "Lily" "L-l-okay..."
    "Lily" "Did I do something wrong?"
    "[Name]" "No, no, no, you didn't."
    "[Name]" "You couldn't have done it better."
    show sc i_Lily_5_29 with my_dissolve
    "Lily" "Then what happened?"
    "[Name]" "I just... I'm not ready."
    "Lily" "I understand."
    "[Name]" "Thank you. (chuckles)"
    show sc i_Lily_5_66 with my_dissolve
    "Lily" "Thank you for tonight..."
    "[Name]" "Good night."
    "Lily" "You, too."
    return
label Lily_5_label_130:


    show sc i_Lily_5_30 with my_dissolve
    "[Name]" "{i}(I bet no one's ever stroked your smooth skin like that before.){/i}"
    "[Name]" "Are you ready, Lily?"
    show sc i_Lily_5_31 with my_dissolve
    "[Name]" "I'm starting!"
    scene sc i_Lily_5_anim_7 with Dissolve(.5)
    "Lily" "Ah..."
    "Lily" "Ah... Mhm..."
    "Lily" "[Name], what are you doing?"
    "[Name]" "Should I stop?"
    "Lily" "Oh... Uh...{w} No."
    scene sc i_Lily_5_anim_8 with Dissolve(.5)
    "[Name]" "I can't hear you..."
    "Lily" "Don't stop!"
    "[Name]" "Good girl."
    scene sc i_Lily_5_anim_9 with Dissolve(.5)
    "Lily" "{i}(What sorcery in his touch...){/i}"
    "Lily" "{i}(I can't control myself...){/i}"
    "Lily" "Ah... Mhm..."
    show sc i_Lily_5_38 with my_dissolve
    "[Name]" "{i}(But I can...){/i}"
    "[Name]" "{i}(...control you...){/i}"
    "[Name]" "{i}(...with every move I make.){/i}"
    show sc i_Lily_5_36 with my_dissolve
    "[Name]" "{i}(I can feel you melting with every kiss.){/i}"
    "[Name]" "{i}(And every touch.){/i}"
    "[Name]" "{i}(And now...){/i}"
    show sc i_Lily_5_40 with my_dissolve
    "Lily" "Ah!"
    "Lily" "[Name]...{w} I'm not sure..."
    show sc i_Lily_5_34 with my_dissolve
    "Lily" "Maybe it's too far."
    "[Name]" "Trust me, Lily."
    "[Name]" "I'll stop as soon as you say so."
    "Lily" "Okay."
    show sc i_Lily_5_35 with my_dissolve
    "[Name]" "{i}(Let's see if my fingers remember.){/i}"
    scene sc i_Lily_5_anim_10 with Dissolve(.5)
    "Lily" "Oh... That tickles... Hee-hee..."
    "Lily" "Ah...{w} Oh...."
    "Lily" "Yes...{w} ah..."
    scene sc i_Lily_5_anim_11 with Dissolve(.5)
    "Lily" "{i}(Am I so...){/i}"
    "Lily" "{i}(But it feels so good...){/i}"
    "Lily" "Ah....{w} Yes...{w} Yes, that's it!"
    scene sc i_Lily_5_anim_12 with Dissolve(.5)
    "[Name]" "Do you like everything?"
    "Lily" "Yes! Yes! Yes! Yes! Oh yes..."
    "[Name]" "Good girl..."
    scene sc i_Lily_5_anim_11 with Dissolve(.5)
    "Lily" "More! More!"
    "Lily" "Yes...{w} Ah..."
    "Lily" "Yes...{w} Yes!"
    show sc i_Lily_5_37 with my_dissolve
    "[Name]" "{i}(I think we're getting to the main thing...){/i}"
    "[Name]" "{i}(You're trembling with excitement.){/i}"
    show sc i_Lily_5_64 with my_dissolve
    "[Name]" "{i}(It's time to give you real pleasure!){/i}"
    "[Name]" "I'm going to go deeper..."
    show sc i_Lily_5_65 with my_dissolve
    "Lily" "Wait!"
    "Lily" "I... I'm not ready."
    "[Name]" "Come on, you're almost at the finish line..."
    show sc i_Lily_5_39 with my_dissolve
    "Lily" "You promised we'd stop when I asked."
    "[Name]" "You're right."
    show sc i_Lily_5_40 with my_dissolve
    "Lily" "I can't stop shaking..."
    "Lily" "[Name], what have you done to me?"
    show sc i_Lily_5_41 with my_dissolve
    "[Name]" "Nothing that dishonors you."
    "Lily" "I thought..."
    "[Name]" "It's nothing."
    "[Name]" "Although if you've never kissed before, it must be the first time you've been fingered."
    show sc i_Lily_5_42 with my_dissolve
    "Lily" "Well..."
    "Lily" "I've touched myself... there."
    "Lily" "But not how you do it..."
    show sc i_Lily_5_43 with my_dissolve
    "Lily" "You're better."
    "[Name]" "{i}(I'm flattered!){/i}"
    "[Name]" "{i}(Do you have any idea how highly you rated me?){/i}"
    show sc i_Lily_5_41 with my_dissolve
    "[Name]" "You too."
    "[Name]" "That's our combined score."
    "Lily" "Aha-ha."
    "Lily" "Let's discuss what's next, shall we?"
    show sc i_Lily_5_38 with my_dissolve
    "[Name]" "I think that's enough excitement for today."
    "[Name]" "Let's discuss everything, including the faculty point plan, some other time."
    "Lily" "You're probably right."
    "Lily" "Let's do that."
    "Lily" "I have a lot on my mind, so..."
    "[Name]" "I think you'll sleep like a baby."
    show sc i_Lily_5_43 with my_dissolve
    "Lily" "I could fall asleep here..."
    "[Name]" "I don't know if Elijah would be thrilled if he came by in the morning."
    "Lily" "I'm kidding."
    show sc i_Lily_5_66 with my_dissolve
    "Lily" "I'm gonna run."
    "[Name]" "I'll see you in a bit."
    return


label Lily_1_1_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)

    show sc i_Lily_1_1 with Dissolve(.5)
    "[Name]" "Hi, how are you?"
    "Lily" "Hi, [Name]."
    "Lily" "Tell me that at least you've already {b}found the three books{/b}, as we agreed."
    show sc i_Lily_1_3 with my_dissolve
    "Lily" "{b}Have you even been to Victoria's class yet?{/b}"
    "[Name]" "Uh... No, but I've been meaning to go."
    show sc i_Lily_1_11 with my_dissolve
    "Lily" "Okay. Don't take too long."
    "Lily" "We've got a lot of work to do."
    show sc i_Lily_1_14 with my_dissolve
    "Lily" "Leonheart's fate depends on us!"
    "[Name]" "I understand."
    "Lily" "Let's not waste time talking. Let's go!"
    return

label Lily_1_2_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)
    show sc i_Lily_1_2 with my_dissolve
    "[Name]" "Lily, it's good to see you!"
    "Lily" "Hi, [Name]."
    show sc i_Lily_1_4 with my_dissolve
    "Lily" "Tell me that at least you've already {b}found the three books{/b}, as we agreed."
    menu:
        "Lie about books":
            $ pass
            show sc i_Lily_1_4 with my_dissolve
            "[Name]" "...Yup. I'm done."
            show sc i_Lily_1_5 with my_dissolve
            "Lily" "Yay! Really?"
            call Lily_3_label_8 from _call_Lily_3_label_8
            $ p_up('Lily', 4)
            $ Q_Lily=3

            $ log_message.update({"QLOG_Lily":4})
            return
        "Tell the truth":
            $ pass
    show sc i_Lily_1_4 with my_dissolve
    "[Name]" "Not quite yet."
    show sc i_Lily_1_5 with my_dissolve
    "Lily" "Yeah, it's harder than I thought."
    "Lily" "But we'll get through it."
    "[Name]" "I'm sure we will. You wanna go for a walk?"
    show sc i_Lily_1_3 with my_dissolve
    "Lily" "Business before pleasure. First we have to find the books!"
    "Lily" "And don't you dawdle!"
    "Lily" "It's for the house!"
    

    return


label Lily_1_3_label:
    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)


    show sc i_Lily_1_1 with Dissolve(.5)
    "[Name]" "How's it going, Lily? As always, with your head in house issues?"
    "Lily" "Well, someone has to think about it."
    "Lily" "I wouldn't rely on Elijah."
    "[Name]" "Heh."
    show sc i_Lily_1_15 with my_dissolve
    "Lily" "You didn't happen to come here to talk about the duels, did you?"
    "[Name]" "What about them?"
    "Lily" "I thought you realized you couldn't win our wager."
    show sc i_Lily_1_19 with my_dissolve
    "Lily" "So you' ve come to admit your defeat."
    "[Name]" "No, I' m not."
    show sc i_Lily_1_6 with my_dissolve
    "[Name]" "I always see things through to the end."
    "[Name]" "I've told you Leonheart will win the duel with Adderin."
    "[Name]" "So that' s how it's going to be."
    show sc i_Lily_1_3 with my_dissolve
    "Lily" "We'll see."

    return


label Lily_1_4_label:
    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)

    show sc i_Lily_1_2 with Dissolve(.5)
    "[Name]" "Hi Lily, I have great news!"
    "Lily" "Hi [Name]!"
    show sc i_Lily_1_12 with my_dissolve
    "Lily" "Sorry, I can't right now, I'm getting ready for Victoria's practice."
    "Lily" "If you distract me now, I'll totally fail..."
    "[Name]" "Uh..."
    "[Name]" "Let's get together tonight then."
    show sc i_Lily_1_8 with my_dissolve
    "[Name]" "Good luck in practice!"
    "Lily" "Thank you"
    return


label Lily_2_1_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)


    show sc i_Lily_3_1 with Dissolve(.5)
    "[Name]" "Hi! I think we've met..."
    "Lily" "Yes, I remember you."
    "Lily" "We saw each other before the exam, didn't we?"
    show sc i_Lily_3_2 with my_dissolve
    "[Name]" "That's right."
    "[Name]" "Are you interested in potions?"
    "Lily" "I'm not sure..."
    "Lily" "But attendance gives you house points."
    show sc i_Lily_3_3 with my_dissolve
    "Lily" "Sorry, I have to get ready for class..."
    "[Name]" "Can we do this another time?"
    "Lily" "Sure."
    return


label Lily_2_2_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)



    show sc i_Lily_3_1 with Dissolve(.5)
    "[Name]" "Lily, hi!"
    "Lily" "[Name]! I was hoping we'd see each other."
    "[Name]" "You were?"
    "Lily" "Yeah, I wanted to see how the house points hunt was going."
    "[Name]" "Oh, you mean..."
    "[Name]" "I was just about to go to Victoria's class."
    show sc i_Lily_3_3 with my_dissolve
    "Lily" "You haven't even been there yet? Uh..."
    "[Name]" "Don't be sad, gorgeous."
    "[Name]" "I told you I'd help you with house points."
    "[Name]" "So I will."
    show sc i_Lily_3_4 with my_dissolve
    "[Name]" "Trust me."
    "Lily" "I will. I trust you."
    "Lily" "Go do it!"
    return

label Lily_2_3_label:
    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)

    show sc i_Lily_3_1 with Dissolve(.5)
    "[Name]" "Hey!"
    "[Name]" "I think you'll be pleased to know that I attended class, as promised."
    "[Name]" "The house points are already in Leonheart's pocket."
    show sc i_Lily_3_2 with my_dissolve
    "Lily" "That's wonderful news, [Name]!"
    "Lily" "Let's discuss it tomorrow before magic class."
    "[Name]" "I was hoping to chat with you now..."
    show sc i_Lily_3_3 with my_dissolve
    "Lily" "I'd love to, but I already promised to help Sabrina with the inventory."
    "[Name]" "Maybe you could use my help, too?"
    show sc i_Lily_3_2 with my_dissolve
    "Lily" "No, thank you. I want to get in touch with her."
    "[Name]" "Oh, I see."
    "[Name]" "Then I'll leave you to it."
    return


label Lily_2_4_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)
    show sc i_Lily_3_3 with Dissolve(.5)


    "[Name]" "Hi, Lily! Have you seen any old folios lying around?"
    "Lily" "Look how sneaky you are! I'm doing my own looking here."
    "[Name]" "Yes? I thought you already found them all."
    show sc i_Lily_3_3 with my_dissolve
    "Lily" "Alas, only two so far."
    "Lily" "I was hoping you'd already done that."
    "[Name]" "Almost."
    show sc i_Lily_3_2 with my_dissolve
    "Lily" "Let's see which one of us does it first!"
    "Lily" "Let's not waste any time!"
    return




label Lily_2_5_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)


    show sc i_Lily_3_1 with Dissolve(.5)

    show sc i_Lily_3_1 with my_dissolve
    "[Name]" "Oh, Lily, I was just looking for you!"
    "Lily" "Hello, [Name]."
    show sc i_Lily_3_2 with my_dissolve
    "Lily" "Why?"
    "[Name]" "I just have some good news to share..."
    show sc i_Lily_3_5 with my_dissolve
    "Lily" "Oh, sorry, it's about my secret project."
    "[Name]" "{i}(Is it so secret if you talk about it freely?){/i}"
    "Lily" "I have to take this."
    "[Name]" "I'll wait."
    show sc i_Lily_3_6 with my_dissolve
    "Lily" "It may be a long time."
    "Lily" "Especially since it is a secret conversation."
    "Lily" "Let's meet in the morning before magic class and talk quietly."
    "[Name]" "It's a deal."

    return


label Lily_2_6_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)




    show sc i_Lily_3_1 with Dissolve(.5)
    "[Name]" "Hi, Lily!"
    "Lily" "[Name]? What are you doing here?"
    "[Name]" "What do you mean?"
    show sc i_Lily_3_7 with my_dissolve
    "Lily" "I thought you were getting ready for a duel."
    "Lily" "Or did you realize it was a stupid idea and come to give up?"
    "[Name]" "Well, no."
    "[Name]" "I don't plan on losing an argument to you."
    "Lily" "We'll see about that."

    return


label Lily_2_7_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)




    show sc i_Lily_3_1 with Dissolve(.5)
    "[Name]" "Hi, Lily!"
    "[Name]" "I have great news..."
    show sc i_Lily_3_3 with my_dissolve
    "Lily" "Hold on, [Name]. I'll stop you right there."
    "Lily" "I can't talk right now."
    "Lily" "I'm waiting for a call."
    "[Name]" "Huh?"
    "[Name]" "Your secret project?"
    show sc i_Lily_3_8 with my_dissolve
    "Lily" "Shh! It's a secret, duh!"
    "[Name]" "Sorry, I wasn't thinking."
    show sc i_Lily_3_2 with my_dissolve
    "Lily" "Let's meet tomorrow morning before class and talk about it. Okay?"
    "[Name]" "Sure."
    return


label Lily_3_1_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)



    show sc i_Lily_2_2 with Dissolve(.5)
    "[Name]" "Oh, girls, hello!"
    show sc i_Lily_2_6 with my_dissolve
    "Lily" "Hi."
    "Naomi" "Hi."
    "[Name]" "Am I interrupting?"
    show sc i_Lily_2_7 with my_dissolve
    "Lily" "Actually, um..."
    "Naomi" "Sorry, dude. You're interrupting. This is a private conversation."
    "[Name]" "I get it, I'm no fool."
    show sc i_Lily_2_1 with my_dissolve
    "[Name]" "{i}(I guess I should get to know them better when they're not together.){/i}"

    return


label Lily_3_2_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)
    show sc i_Lily_2_1 with Dissolve(.5)
    "[Name]" "Lily, Naomi! Hi!"
    show sc i_Lily_2_7 with my_dissolve
    "Lily" "Hi, [Name]!"
    "Naomi" "Hi."
    "[Name]" "What are you guys doing?"
    show sc i_Lily_2_6 with my_dissolve
    "Lily" "Discussing Victoria's commencement lecture."
    "Lily" "Have you been? What do you think?"
    "[Name]" "No, I haven't had a chance to..."
    show sc i_Lily_2_4 with my_dissolve
    "Lily" "Too bad! I thought you were planning on..."
    "[Name]" "Yes, I'm still planning."
    show sc i_Lily_2_5 with my_dissolve
    "Lily" "I'm glad to hear it. You won't regret it!"
    "[Name]" "Thank you."
    return
label Lily_3_3_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)


    show sc i_Lily_2_2 with Dissolve(.5)
    "[Name]" "Hey, guys!"
    "[Name]" "Lily, will you be free soon?"
    "[Name]" "I wanted to discuss our plans for Leonheart."
    show sc i_Lily_2_7 with my_dissolve
    "Lily" "Look, [Name], this is a serious matter."
    "Lily" "Let's meet in the morning before magic class."
    show sc i_Lily_2_6 with my_dissolve
    "Lily" "so we can talk about it with a clear head."
    "[Name]" "Okay."
    return

label Lily_3_4_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)

    show sc i_Lily_2_1 with Dissolve(.5)
    "[Name]" "Girls, hello!"
    show sc i_Naomi_2_2 with my_dissolve
    "Naomi" "Hi."
    show sc i_Lily_2_6 with my_dissolve
    "Lily" "Hi there, [Name]."
    "Lily" "How's the book search going?"
    "[Name]" "I wanted to ask you the same thing!"
    "[Name]" "I'm still in the middle of it..."
    show sc i_Lily_2_7 with my_dissolve
    "Lily" "Yeah and I haven't found everything yet."
    "Lily" "It's harder than I thought it would be."
    "[Name]" "We'll get through it!"
    "Lily" "Yes! Let's go find the books!"
    return
label Lily_3_5_label:
    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)

    show sc i_Lily_2_4 with Dissolve(.5)
    "[Name]" "Hi, Lily!"
    "[Name]" "So, how's the book search going?"
    show sc i_Lily_2_7 with my_dissolve
    "Lily" "Sorry, [Name]. We're kind of busy right now."
    "Lily" "Can we meet in the morning and talk about it?"
    "[Name]" "Uh, sure. Before magic class?"
    "Lily" "Great."
    return

label Lily_3_6_label:
    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)

    show sc i_Lily_2_2 with Dissolve(.5)
    "[Name]" "Yo, Lily, Naomi!"
    "Lily" "Hi!"
    show sc i_Naomi_2_2 with my_dissolve
    "Naomi" "Hi."
    "[Name]" "Lily, can I kidnap you?"
    show sc i_Lily_2_4 with my_dissolve
    "Lily" "Not now, [Name]."
    "Lily" "Naomi and I just met."
    "Lily" "I have a lot of catching up to do in a day."
    show sc i_Lily_2_1 with my_dissolve
    "Lily" "So, then I'm telling him..."
    "[Name]" "{i}(I can imagine.){/i}"
    "[Name]" "Allright, see you later."
    return


label lily_events_5_label:
    







    if not hasattr(store, 'Q_NV_Lily'):
        $ Q_NV_Lily = 0
    if persistent.nv is None:
        call hide_all_main_interfaces from _call_hide_all_main_interfaces_10 
        $ nv = renpy.call_screen('confirm', 
        '{size=15}Note that night visits are entirely optional.{/size} \n{size=15}This additional content is not required to complete the game{/size} \n{size=15}and won’t influence your relationship with other characters.{/size}', 
        Return('Continue'), Return('Not now'), yes_text = _('Continue'), no_text = _('Not now'),)
        $ persistent.nv = True
    else:
       $ nv = 'Continue' 
    if True:
        if nv == 'Continue':

            if renpy.music.get_playing():
                stop music fadeout .5
                play music_2 'audio_ep2/Music/mus_for_visites.mp3' fadein 1
            elif renpy.music.get_playing('music_2'):
                stop music_2 fadeout .5
                play music 'audio_ep2/Music/mus_for_visites.mp3' fadein 1
            elif True:
                stop music_2 fadeout .5
                play music 'audio_ep2/Music/mus_for_visites.mp3' fadein 1
            if persistent.from_gallery:
                hide screen main_interface 
                show expression '#000a'
                with Dissolve(.5)
                menu:
                    "Scene 1" if True:
                        $ renpy.call('lily_events_5_label_0')
                    "Scene 2" if True:

                        $ renpy.call('lily_events_5_label_1')
                    "Scene 3" if True:

                        $ renpy.call('lily_events_5_label_2')
                    "Scene 4" if True:

                        $ renpy.call('lily_events_5_label_3')

                hide screen black_tmp_screen_menu
                show expression '#000'
                with Dissolve(1.5)
                $ renpy.pause(1.5, hard = True)

                if persistent.from_gallery:
                    scene expression '#000' with Dissolve(1)
                    $ renpy.full_restart()
            if Q_NV_Lily:
                hide screen main_interface with Dissolve(.5)
                $ renpy.call('lily_events_5_label_'+str(Q_NV_Lily))

                hide screen black_tmp_screen_menu
                show expression '#000'
                with Dissolve(1.5)
                $ renpy.pause(1.5, hard = True)


                if renpy.music.get_playing():
                    stop music fadeout .5
                    play music_2 'audio_ep2/SC/33. Romantic.mp3' fadein 1


                elif renpy.music.get_playing('music_2'):
                    stop music_2 fadeout .5
                    play music 'audio_ep2/SC/33. Romantic.mp3' fadein 1
                $ change_location_2('leon_room_mc', time_now+1, sleep = True)
                jump main_interface_label
            $ pass
        else:

            if persistent.from_gallery:
                hide screen main_interface                
                scene expression '#000'
                with Dissolve(1)
                $ renpy.full_restart()


            show screen main_interface 
            show screen show_hide_locations_2
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label

label lily_events_5_label_0:
    $ Q_NV_Lily += 1
    hide screen main_interface 
    scene sc i_Lily_NV_1
    with Dissolve(.5)
    "[Name]" "{i}(Hey there, sleeping beauty.){/i}"
    "[Name]" "{i}(I hope you're seeing a peaceful dream.){/i}"
    show sc i_Lily_NV_2 with my_dissolve
    "[Name]" "{i}(Don't mind me, I'm here just to admire your beauty.){/i}"
    "[Name]" "{i}(If only this blanket was not covering all the best parts.){/i}"
    show sc i_Lily_NV_2 with my_dissolve
    "[Name]" "{i}(Let's take a closer look at you.){/i}"
    "[Name]" "{i}(I'm sure you won't mind.){/i}"
    show sc i_Lily_NV_3 with my_dissolve
    "[Name]" "{i}(Oh, my...){/i}"
    "[Name]" "{i}(What a cute little lingerie you've got.){/i}"
    "[Name]" "{i}(I bet it look's even better down there...){/i}"
    show sc i_Lily_NV_3 with my_dissolve
    "[Name]" "{i}(How can I resist you...){/i}"
    "[Name]" "{i}(Let me get rid of that...){/i}"
    show sc i_Lily_NV_8 with my_dissolve
    "Lily" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I think she's gonna wake up any minute.){/i}"
    "[Name]" "{i}(Better get out of here.){/i}"

    hide screen black_tmp_screen_menu
    show expression '#000'
    with Dissolve(1.5)
    $ renpy.pause(1.5, hard = True)
    if renpy.music.get_playing():
        stop music fadeout .5
        play music_2 'audio_ep2/SC/33. Romantic.mp3' fadein 1


    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout .5
        play music 'audio_ep2/SC/33. Romantic.mp3' fadein 1
    $ change_location_2('leon_room_mc', time_now+1, sleep = True)
    if persistent.from_gallery:
        scene expression '#000' with Dissolve(1)
        $ renpy.full_restart()
    jump main_interface_label

label lily_events_5_label_1:
    $ Q_NV_Lily += 1
    scene sc i_Lily_NV_1 with Dissolve(.5)
    "[Name]" "{i}(Hey there, sleeping beauty.){/i}"
    "[Name]" "{i}(I hope you're seeing a peaceful dream.){/i}"
    show sc i_Lily_NV_2 with my_dissolve
    "[Name]" "{i}(Don't mind me, I'm here just to admire your beauty.){/i}"
    "[Name]" "{i}(If only this blanket was not covering all the best parts.){/i}"
    show sc i_Lily_NV_2 with my_dissolve
    "[Name]" "{i}(Let's take a closer look at you.){/i}"
    "[Name]" "{i}(I'm sure you won't mind.){/i}"
    show sc i_Lily_NV_3 with my_dissolve
    "[Name]" "{i}(Oh, my...){/i}"
    "[Name]" "{i}(What a cute little lingerie you've got.){/i}"
    show sc i_Lily_NV_3 with my_dissolve
    "[Name]" "{i}(How can I resist you...){/i}"
    "[Name]" "{i}(Let me get rid of that...){/i}"
    show sc i_Lily_NV_4 with my_dissolve
    "[Name]" "{i}(Here we go.){/i}"
    "[Name]" "{i}(Let me just enjoy this magnificent view.){/i}"
    "[Name]" "{i}(I don't know where to start...){/i}"
    show sc i_Lily_NV_4 with my_dissolve
    "[Name]" "{i}(Your whole body is so incredibly hot...){/i}"
    show sc i_Lily_NV_5 with my_dissolve
    "[Name]" "{i}(But the hardest thing is to take my eyes off those breasts.){/i}"
    "[Name]" "{i}(I bet it feels incredibly nice to touch them...){/i}"
    "[Name]" "{i}(Let's not rush things up. Let me take a look at another angle.){/i}"
    show sc i_Lily_NV_4 with my_dissolve
    "[Name]" "{i}(This lingerie enhances your beauty.){/i}"
    show sc i_Lily_NV_9 with my_dissolve
    "[Name]" "{i}(Especially between your legs...){/i}"
    "[Name]" "{i}(I bet you'll like my caresses.){/i}"
    "[Name]" "{i}(I just know where to touch...){/i}"
    show sc i_Lily_NV_8 with my_dissolve
    "Lily" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I think she's gonna wake up any minute.){/i}"
    "[Name]" "{i}(Better get out of here.){/i}"
    return
label lily_events_5_label_2:
    $ Q_NV_Lily += 1
    scene sc i_Lily_NV_1 with Dissolve(.5)


    "[Name]" "{i}(Hey there, sleeping beauty.){/i}"
    "[Name]" "{i}(I hope you're seeing a peaceful dream.){/i}"
    show sc i_Lily_NV_2 with my_dissolve
    "[Name]" "{i}(Don't mind me, I'm here just to admire your beauty.){/i}"
    "[Name]" "{i}(If only this blanket was not covering all the best parts.){/i}"
    show sc i_Lily_NV_2 with my_dissolve
    "[Name]" "{i}(Let's take a closer look at you.){/i}"
    "[Name]" "{i}(I'm sure you won't mind.){/i}"
    show sc i_Lily_NV_3 with my_dissolve
    "[Name]" "{i}(Oh, my...){/i}"
    "[Name]" "{i}(What a cute little lingerie you've got.){/i}"
    "[Name]" "{i}(I bet it look's even better down there...){/i}"
    show sc i_Lily_NV_3 with my_dissolve
    "[Name]" "{i}(Why do you even need blanket, anyway?){/i}"
    "[Name]" "{i}(Let me get rid of that...){/i}"
    show sc i_Lily_NV_4 with my_dissolve
    "[Name]" "{i}(Here we go.){/i}"
    "[Name]" "{i}(Let me just enjoy this magnificent view.){/i}"
    "[Name]" "{i}(I don't know where to start...){/i}"
    show sc i_Lily_NV_4 with my_dissolve
    "[Name]" "{i}(Your whole body is so damn hot...){/i}"
    show sc i_Lily_NV_5 with my_dissolve
    "[Name]" "{i}(It's so hard to take your eyes off of those breasts.){/i}"
    "[Name]" "{i}(I bet it feels incredibly nice to the touch them...){/i}"
    "[Name]" "{i}(Maybe this time I can actually try it...){/i}"
    show sc i_Lily_NV_5 with my_dissolve
    "[Name]" "{i}(I'll try not to disturb your sleep, Lily.){/i}"
    "[Name]" "{i}(Just relax and watch the naughty dreams...){/i}"
    show sc i_Lily_NV_6 with my_dissolve
    "[Name]" "{i}(Oh, yeah... That feels good.){/i}"
    "[Name]" "{i}(I can feel your heart beating, Lily.){/i}"
    "[Name]" "{i}(I can feel every breath you take.){/i}"
    "[Name]" "{i}(This really brings us clother, my dear.){/i}"
    "[Name]" "{i}(Let's take a look at othey honey spots...){/i}"
    show sc i_Lily_NV_4 with my_dissolve
    "[Name]" "{i}(This underwear emphasizes your beauty.){/i}"
    show sc i_Lily_NV_9 with my_dissolve
    "[Name]" "{i}(Especially between your legs...){/i}"
    "[Name]" "{i}(I bet you like my caresses.){/i}"
    "[Name]" "{i}(I just know where to touch...){/i}"
    show sc i_Lily_NV_9 with my_dissolve
    "[Name]" "{i}(I will be gentle with you, dear Lily.){/i}"
    show sc i_Lily_NV_10 with my_dissolve
    "[Name]" "{i}(I feel the heat of your loins.){/i}"
    "[Name]" "{i}(You obviously don't mind feeling someone's tender hands...){/i}"
    "[Name]" "{i}(Maybe next time...){/i}"
    show sc i_Lily_NV_14 with my_dissolve
    "[Name]" "{i}(The blanket is moved and I have a beautiful view of your legs...){/i}"
    "[Name]" "{i}(They drive me crazy...){/i}"
    show sc i_Lily_NV_15 with my_dissolve
    "[Name]" "{i}(And your toes... I wish I could...){/i}"
    show sc i_Lily_NV_8 with my_dissolve
    "Lily" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I think she's gonna wake up any minute.){/i}"
    "[Name]" "{i}(Better get out of here.){/i}"
    return
label lily_events_5_label_4:
label lily_events_5_label_3:

    $ unlock_gallery('images/ero/NV_Lily.png')
    scene sc i_Lily_NV_1 with Dissolve(.5)


    "[Name]" "{i}(Hey there, sleeping beauty.){/i}"
    "[Name]" "{i}(I hope you're seeing a peaceful dream.){/i}"
    show sc i_Lily_NV_2 with my_dissolve
    "[Name]" "{i}(Don't mind me, I'm here just to admire your beauty.){/i}"
    "[Name]" "{i}(If only this blanket was not covering all the best parts.){/i}"
    show sc i_Lily_NV_2 with my_dissolve
    "[Name]" "{i}(Let's take a closer look at you.){/i}"
    "[Name]" "{i}(I'm sure you won't mind.){/i}"
    show sc i_Lily_NV_3 with my_dissolve
    "[Name]" "{i}(Oh, my...){/i}"
    "[Name]" "{i}(What a cute little lingerie you've got.){/i}"
    "[Name]" "{i}(I bet it look's even better down there...){/i}"
    "[Name]" "{i}(Let me get rid of that...){/i}"
    show sc i_Lily_NV_4 with my_dissolve
    "[Name]" "{i}(Here we go.){/i}"
    "[Name]" "{i}(Let me just enjoy this magnificent view.){/i}"
    "[Name]" "{i}(I don't know where to start...){/i}"
    show sc i_Lily_NV_4 with my_dissolve
    "[Name]" "{i}(Your whole body is so damn hot...){/i}"
    show sc i_Lily_NV_5 with my_dissolve
    "[Name]" "{i}(But I always tend to start with your breasts.){/i}"
    "[Name]" "{i}(I know for sure it feels incredibly nice to the touch them...){/i}"
    "[Name]" "{i}(I'll try not to disturb your sleep, Lily.){/i}"
    "[Name]" "{i}(Just relax and watch the naughty dreams...){/i}"
    show sc i_Lily_NV_6 with my_dissolve
    "[Name]" "{i}(Oh, yeah... That feels good.){/i}"
    "[Name]" "{i}(I can feel your heart beating, Lily.){/i}"
    "[Name]" "{i}(I can feel every breath you take.){/i}"
    "[Name]" "{i}(I need to squeeze it and feel it in my hand...){/i}"
    "[Name]" "{i}(Maybe if I do it gently, she won't notice...){/i}"
    show sc i_Lily_NV_6 with my_dissolve
    "[Name]" "{i}(Gently...){/i}"
    show sc i_Lily_NV_7 with my_dissolve
    "[Name]" "{i}(Oh yes...){/i}"
    "[Name]" "{i}(Her breasts feel like they were meant to be in my hand.){/i}"
    "[Name]" "{i}(Imagine what they feel like without a bra...){/i}"
    "[Name]" "{i}(I have to find out how to take it off...){/i}"
    "[Name]" "{i}(Meanwhile, I can take a look at your temple.){/i}"
    show sc i_Lily_NV_4 with my_dissolve
    "[Name]" "{i}(This underwear emphasizes your beauty.){/i}"
    show sc i_Lily_NV_9 with my_dissolve
    "[Name]" "{i}(Especially between your legs...){/i}"
    "[Name]" "{i}(I know you like my caresses.){/i}"
    "[Name]" "{i}(I just know where to touch...){/i}"
    show sc i_Lily_NV_9 with my_dissolve
    "[Name]" "{i}(I will be gentle with you, dear Lily.){/i}"
    show sc i_Lily_NV_10 with my_dissolve
    "[Name]" "{i}(I feel the heat of your loins.){/i}"
    "[Name]" "{i}(You obviously don't mind feeling someone's tender hands...){/i}"
    "[Name]" "{i}(But if you want to continue, I need to spread your legs.){/i}"
    show sc i_Lily_NV_11 with my_dissolve
    "[Name]" "{i}(Gently moving your beautiful leg...){/i}"
    "[Name]" "{i}(And look at what a beautiful view opens up to us.){/i}"
    "[Name]" "{i}(Just move your panties...){/i}"
    show sc i_Lily_NV_12 with my_dissolve
    "[Name]" "{i}(I could admire your blossom forever, Lily.){/i}"
    "[Name]" "{i}(You're so tense... Did you feel my touch?){/i}"
    "[Name]" "{i}(Shall we continue?){/i}"
    show sc i_Lily_NV_14 with my_dissolve
    "[Name]" "{i}(The blanket is pulled and I have a beautiful view of your legs...){/i}"
    "[Name]" "{i}(They drive me crazy...){/i}"
    show sc i_Lily_NV_15 with my_dissolve
    "[Name]" "{i}(And your toes... I wish I could...){/i}"

    menu:
        "Lick her toes" if True:
            $ pass
        "Stop and go to sleep" if True:
            jump lily_events_5_label_3_162

    "[Name]" "{i}(I can't help it...){/i}"

    "[Name]" "{i}(Your skin is so soft...){/i}"
    show sc i_Lily_NV_anim_1 with my_dissolve
    "[Name]" "{i}(I want to caress every part of your body.){/i}"
    show sc i_Lily_NV_anim_1 with my_dissolve
    "[Name]" "{i}(And especially those fingers...){/i}"
    show sc i_Lily_NV_anim_1 with my_dissolve
    "[Name]" "{i}(Your scent gives me an animal passion.){/i}"
    show sc i_Lily_NV_anim_1 with my_dissolve
    "Lily" "He-he... mmm..."
    show sc i_Lily_NV_anim_2 with my_dissolve
    "[Name]" "{i}(Does tha tickles, Lily?){/i}"
    show sc i_Lily_NV_anim_2 with my_dissolve
    "[Name]" "{i}(I'm sorry.){/i}"
    show sc i_Lily_NV_anim_2 with my_dissolve
    "[Name]" "{i}(Got too playful with my tongue...){/i}"
label lily_events_5_label_3_162:
    scene sc i_Lily_NV_8 with Dissolve(.5)
    "Lily" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I think she's gonna wake up any minute.){/i}"
    "[Name]" "{i}(Better get out of here.){/i}"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc




label Lily_6_label:

    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2


    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)
    show sc i_Lily_3_1  with my_dissolve
    "[Name]" "Hi there, beautiful!"
    "Lily" "Hello!"
    show sc i_Lily_3_2 with my_dissolve
    "[Name]" "What are you doing, getting ready for class?"
    "Lily" "Yeah, kind of."
    show sc i_Lily_6_1 with my_dissolve
    "Lily" "Miss Spellman asked me to help harvest herbs for potions."
    "Lily" "We're going to the Forbidden magical forest!"
    "Lily" "I'm so excited!"
    "[Name]" "{i}(She'll have to spend all day in the woods feeding mosquitoes...){/i}"
    show sc i_Lily_6_2 with my_dissolve
    "[Name]" "I don't know what you're so excited about. Isn't it dangerous?"
    show sc i_Lily_6_3 with my_dissolve
    "Lily" "With Miss Spellman? Of course not."
    "Lily" "I'm sure it would help enhance Leonheart's reputation."
    show sc i_Lily_6_2 with my_dissolve
    "[Name]" "{i}(There she goes again...){/i}"
    "[Name]" "So that's your motive. I see."
    show sc i_Lily_6_4 with my_dissolve
    "Lily" "Oh, I'm so rude... Do you want to join us?"
    "[Name]" "{i}(I don't think I have anything else planned for today.){/i}"
    show sc i_Lily_6_5 with my_dissolve
    "[Name]" "Yes. Why not?"
    "Lily" "Really? That's great! I'm so excited!"
    "Lily" "I just have to ask Miss Spellman."
    show sc i_Lily_6_6 with my_dissolve
    "Sabrina" "Ask me what?"
    "Lily" "Can [Name] come pick up the ingredients with us?"
    show sc i_Lily_6_7 with my_dissolve
    "Sabrina" "So that's what!"
    "Sabrina" "I didn't know you were interested in herbalism [Name]."
    "[Name]" "He-he. I'm still searching for my calling."
    show sc i_Lily_6_8 with my_dissolve
    "Sabrina" "Well, I don't mind."
    "Sabrina" "The more hands, the more ingredients."
    "Lily" "Hooray!"
    show sc i_Lily_6_9 with my_dissolve
    "Sabrina" "Let's not waste any time! Follow me, guys."
    "Lily" "Come on, [Name]!"
    scene image '#000' with Dissolve(.5)
    scene sc i_Lily_6_10 with Dissolve(.5)
    "[Name]" "{i}(I thought the woods are closer to the academy...){/i}"
    "[Name]" "{i}(I'm already a little tired even in sneakers.){/i}"
    "[Name]" "(I wonder if Sabrina and Lily are comfortable walking in those high-heels shoes.)"
    show sc i_Lily_6_11 with my_dissolve
    "Sabrina" "Hmmm, you know what?"
    "Lily" "What?"
    "[Name]" "What?"
    "Sabrina" "I have an idea!"
    show sc i_Lily_6_12 with my_dissolve
    "Sabrina" "Since we have extra hands, we can do something more efficient with you."
    "Sabrina" "If we split up now, I'll go gather the bloodblossom."
    "Sabrina" "And the two of you will gather the dragon berries."
    "Lily" "Sounds simple."
    show sc i_Lily_6_13 with my_dissolve
    "Sabrina" "Here, [Name], take this."
    "[Name]" "What's this?"
    show sc i_Lily_6_14 with my_dissolve
    "Sabrina" "It's a magic compass."
    "Sabrina" "It's very easy to get lost in a magical forest."
    "Sabrina" "And this compass will always show you a safe way."
    "Sabrina" "Follow its pointers and pick berries."
    show sc i_Lily_6_15 with my_dissolve
    "[Name]" "It vibrates slightly... {w} Is that supposed to be like that?"
    "Sabrina" "Yes, it's living magic."
    show sc i_Lily_6_16 with my_dissolve
    "Lily" "Don't worry, Miss Spellman."
    "Lily" "Everything's gonna be just fine."
    show sc i_Lily_6_17 with my_dissolve
    "Sabrina" "Good luck, guys!"
    "[Name]" "{i}(Let's see where this thing takes us...){/i}"
    scene image '#000' with Dissolve(.5)
    scene sc i_Lily_6_18 with Dissolve(.5)
    "[Name]" "{i}(The terrain seems to be starting to change a bit.){/i}"
    "[Name]" "Oh, Lily, look, there are the berries!"
    "Lily" "I'll get them now."
    show sc i_Lily_6_19 with my_dissolve
    "[Name]" "{i}(Lily is picking berries so diligently, one might envy her dedication.){/i}"
    "Lily" "There don't seem to be any more here. Let's look for more."
    show sc i_Lily_6_18 with my_dissolve
    "[Name]" "The compass is pointing that way, let's go."
    "Lily" "Okay."
    show sc i_Lily_6_20 with my_dissolve
    "Lily" "Oh, look at those flowers!"
    "[Name]" "{i}(I thought we were only picking berries.){/i}"
    "[Name]" "{i}(Oh, well, I think she knows better.){/i}"
    "Lily" "Let's keep going!"
    show sc i_Lily_6_18 with my_dissolve
    "[Name]" "Alright, baby."
    show sc i_Lily_6_21 with my_dissolve
    "[Name]" "Let's see where the compass is pointing."
    "[Name]" "I think we need to go further..."
    show sc i_Lily_6_22 with my_dissolve
    "[Name]" "Oh, shit!"
    "Lily" "[Name]!"
    show sc i_Lily_6_23 with my_dissolve
    "Lily" "Are you all right?"
    "[Name]" "I am. {w} But look at the compass..."
    "Lily" "Ah...."
    show sc i_Lily_6_24 with my_dissolve
    "Lily" "[Name], what are we going to do?"
    "Lily" "Without the compass, we don't know where to go...."
    show sc i_Lily_6_25 with my_dissolve
    "[Name]" "Wait a minute."
    "[Name]" "I need to think."
    "[Name]" "There's got to be a way out of these woods, right?"
    "Lily" "I guess..."
    show sc i_Lily_6_26 with my_dissolve
    "[Name]" "I know!"
    "[Name]" "Let's trace our footsteps back!"
    "Lily" "I don't know...."
    "Lily" "Are you sure we're gonna remember how we got here?"
    show sc i_Lily_6_27 with my_dissolve
    "[Name]" "Totally."
    "[Name]" "(Not really.)"
    show sc i_Lily_6_28 with my_dissolve
    "[Name]" "(What's she so worried about?)"
    "[Name]" "(What can happen in the woods?)"
    scene image '#000' with Dissolve(.5)
    scene sc i_Lily_6_29 with Dissolve(.5)
    "Lily" "Whoa..."
    "[Name]" "Wow!"
    "Lily" "What is this wonderful place?"
    show sc i_Lily_6_29_2 with my_dissolve
    "[Name]" "I have no idea..."
    "Lily" "It's so beautiful..."
    "[Name]" "It's beautiful, it's true."
    "[Name]" "{i}(But this place makes me feel uncomfortable.){/i}"
    show sc i_Lily_6_30 with my_dissolve
    "Lily" "Have you ever seen something so beautiful?"
    "Lily" "Shall we go closer?"
    show sc i_Lily_6_31 with my_dissolve
    "[Name]" "Lily, wait!"
    "[Name]" "I don't think it's a good idea to go there..."
    "[Name]" "It's definitely not that way."
    show sc i_Lily_6_32 with my_dissolve
    "Lily" "Come on! Look how beautiful it is."
    "Lily" "Why would you want to go back to the boring woods?"
    "Lily" "I don't think we'll remember the way back."
    show sc i_Lily_6_33 with my_dissolve
    "Lily" "It's best to wait for help."
    "Lily" "So why not in a nice place like this?"
    show sc i_Lily_6_34 with my_dissolve
    "[Name]" "All right. Maybe you're right."
    "Lily" "You'll see I'm right!"
    show sc i_Lily_6_35 with my_dissolve
    "[Name]" "This is so unusual. Where did the light come from?"
    "Lily" "It's like some kind of magic."
    "Lily" "Do you think someone lives here?"
    show sc i_Lily_6_36 with my_dissolve
    "[Name]" "If so, it doesn't look like he's home."
    "[Name]" "{i}(I'm just now realizing how tired I am.){/i}"
    show sc i_Lily_6_37 with my_dissolve
    "[Name]" "{i}(Is Lily tired too?){/i}"
    "Lily" "Sorry..."
    show sc i_Lily_6_38 with my_dissolve
    "[Name]" "Nevermind..."
    "[Name]" "I think your yawn made me yawn too."
    show sc i_Lily_6_39 with my_dissolve
    "Lily" "Hee-hee-hee."
    "Lily" "{i}You're cute.{/i}"
    show sc i_Lily_6_40 with my_dissolve
    "[Name]" "{i}(...){/i}"
    "[Name]" "{i}(Strange. Are we both tired by the road?){/i}"
    show sc i_Lily_6_41 with my_dissolve
    "Lily" "Alright, stop it!"
    "Lily" "Stop mocking me."
    show sc i_Lily_6_42 with my_dissolve
    "[Name]" "I was not moc..."
    "[Name]" "..king you. I swear."
    show sc i_Lily_6_43 with my_dissolve
    "Lily" "[Name], I think something is wrong."
    "Lily" "We yawn too much."
    show sc i_Lily_6_44 with my_dissolve
    "[Name]" "Look!"
    "Lily" "What the fuck!"
    "Lily" "Do you think they all suddenly got sleepy too?"
    show sc i_Lily_6_45 with my_dissolve
    "[Name]" "We should get out of here anyway."
    "[Name]" "What do you think, Lily?{w} Lily?"
    show sc i_Lily_6_46 with my_dissolve
    "[Name]" "Lily! What are you doing?"
    "[Name]" "Are you crazy?!"
    show sc i_Lily_6_47 with my_dissolve
    "Lily" "I was just... I just sat down for a second to rest."
    "Lily" "Try it, it's so soft..."
    show sc i_Lily_6_48 with my_dissolve
    "[Name]" "It' is soft, you're right!"
    "[Name]" "I could fall asleep here..."
    show sc i_Lily_6_49 with my_dissolve
    "Lily" "No, wait!"
    "Lily" "What am I talking about?"
    "Lily" "Get up! Do you hear me?!"
    show sc i_Lily_6_50 with my_dissolve
    "Lily" "[Name], we can't sleep!"
    "Lily" "We have to think of something!"
    show sc i_Lily_6_51 with my_dissolve
    "[Name]" "Huh, what? Yes... Right..."
    "[Name]" "Lily, what is it that keeps you up all night? Any ideas?"
    show sc i_Lily_6_52 with my_dissolve
    "Lily" "Well...."
    "Lily" "Actually, there is one..."
    "Lily" "But...."
    show sc i_Lily_6_53 with my_dissolve
    "[Name]" "Our lives depend on it!"
    show sc i_Lily_6_54 with my_dissolve
    "Lily" "After that time in your room..."
    "Lily" "I couldn't sleep all night."
    "Lily" "My heart was beating like crazy."
    show sc i_Lily_6_55 with my_dissolve
    "Lily" "But what about you...."
    show sc i_Lily_6_56 with my_dissolve
    "Lily" "I know! We could have...."
    "[Name]" "Lily..."
    show sc i_Lily_6_57 with my_dissolve
    "Lily" "That way we would both have to stay awake!"
    "[Name]" "{i}(The important thing is not to fall asleep after sex...){/i}"
    show sc i_Lily_6_58 with my_dissolve
    "Lily" "So... What do you say?"
    menu:

        "Yes":
            $ l6_yes = True
        "No":
            jump Lily_6_label_434
    "[Name]" "Lily, I like you."
    show sc i_Lily_6_59 with my_dissolve
    "Lily" "I like you too, [Name]..."
    "Lily" "I dreamed we were doing this..."
    show sc i_Lily_6_60 with my_dissolve
    "[Name]" "How was I in your dream?"
    "Lily" "Passionate... tender... mine..."
    show sc i_Lily_6_61 with my_dissolve
    "[Name]" "Lily..."
    "[Name]" "{i}(Her lips. Soft as two pillows...){/i}"
    show sc i_Lily_6_60 with my_dissolve
    "Lily" "Let's pick a spot away from the pile of corpses, if you don't mind."
    "[Name]" "Yes, of course."
    "[Name]" "Anything you want."
    scene image '#000' with Dissolve(.5)
    scene sc i_Lily_6_61 with Dissolve(.5)
    "Lily" "Mhm..."
    "[Name]" "(I think she's not so sleepy anymore.)"
    show sc i_Lily_6_62 with my_dissolve
    "[Name]" "(I know what will wake her up even more.)"
    "Lily" "M-m-m-m..."
    show sc i_Lily_6_63 with my_dissolve
    "[Name]" "(The fabric prevents me from feeling the magnificence of your tits...)"
    "[Name]" "Do you like it when I squeeze your breasts?"
    "Lily" "Oh yes..."
    show sc i_Lily_6_64 with my_dissolve
    "[Name]" "Then let's get rid of your top."
    "Lily" "Okay..."
    "Lily" "Do everything you've dreamed of doing with me."
    show sc i_Lily_6_65 with my_dissolve
    "[Name]" "That's a whole other thing..."
    "[Name]" "what a view!"
    show sc i_Lily_6_66 with my_dissolve
    "Lily" "[Name].... Mhm..."
    "[Name]" "M-m-m..."
    show sc i_Lily_6_66_2 with my_dissolve
    "[Name]" "(Her breasts are so firm and neat...)"
    "Lily" "Ah...oh...."
    show sc i_Lily_6_67 with my_dissolve
    "Lily" "Look, [Name], that's not good..."
    "[Name]" "What happened, did I do something wrong?"
    "Lily" "No, it's not that."
    show sc i_Lily_6_68 with my_dissolve
    "Lily" "It's just that you should take your clothes off too."
    "Lily" "If you want to play like a grown-up."
    show sc i_Lily_6_69 with my_dissolve
    "[Name]" "You don't have to ask me twice, beautiful."
    "Lily" "Well, then I'll get rid of the extra stuff, too."
    "[Name]" "(And she's serious.)"
    show sc i_Lily_6_70 with my_dissolve
    "[Name]" "(Hmm, what a figure!)"
    "[Name]" "Lily, you're incredibly beautiful..."
    "[Name]" "But why did you leave your panties on?"
    show sc i_Lily_6_71 with my_dissolve
    "Lily" "What are you here for?"
    "Lily" "Or do I have to do everything myself?"
    "[Name]" "Well. Fair enough. You'll have to do better than that."
    show sc i_Lily_6_72 with my_dissolve
    "Lily" "Just... {w} Be gentle."
    "[Name]" "I promise."
    show sc i_Lily_6_73 with my_dissolve
    "[Name]" "(What a cute little butt!)"
    "[Name]" "(I want to touch it...)"
    show sc i_Lily_6_74 with my_dissolve
    "[Name]" "(Oh yes...)"
    "[Name]" "(What soft skin.)"
    "[Name]" "(And so firm!)"
    show sc i_Lily_6_75 with my_dissolve
    "[Name]" "(This is what I call a real stress relief toy.)"
    "[Name]" "(I already forgot about our misfortunes.)"
    show sc i_Lily_6_76 with my_dissolve
    "Lily" "Honey, I'm going to sleep..."
    "Lily" "Do something!"
    show sc i_Lily_6_77 with my_dissolve
    "[Name]" "Oh, sure. Sorry."
    "[Name]" "Let's get rid of the cloth..."
    show sc i_Lily_6_78 with my_dissolve
    "[Name]" "(That's better.)"
    "[Name]" "(Though much is still hidden from me.)"
    "[Name]" "Lily..."
    show sc i_Lily_6_79 with my_dissolve
    "Lily" "Y-yes?"
    "[Name]" "Could you arch your back a little bit, baby?"
    "Lily" "Sure! Let me get comfy."
    show sc i_Lily_6_80 with my_dissolve
    "Lily" "So, what then? How?"
    "[Name]" "How?"
    show sc i_Lily_6_81 with my_dissolve
    "Lily" "Yes... H-how do you want to do it?"
    "[Name]" "(Let's see...)"
    $ l6_sex_1 = False
    $ l6_sex_2 = False
    $ l6_sex_3 = False
label Lily_6_label_224:
    if all(('l6_sex_1', 'l6_sex_2', 'l6_sex_3')):
        $ pass
    menu:
        "Cunnilingus" if not l6_sex_1:
            $ l6_sex_1 = True
            
            $ l6_sex = "Cunnilingus"
            show sc i_Lily_6_anim_1 with my_dissolve
            "[Name]" "(That pie looks too yummy)."
            show sc i_Lily_6_anim_1_z with my_dissolve
            "[Name]" "(I just have to try it.)"
            "[Name]" "I want to kiss you there..."
            show sc i_Lily_6_82 with my_dissolve
            "Lily" "Ah...AH!"
            "Lily" "[Name]..."
            show sc i_Lily_6_83 with my_dissolve
            "[Name]" "(I can feel her trembling with pleasure.)"
            "Lily" "This is incredible!"
            show sc i_Lily_6_anim_2 with my_dissolve
            "Lily" "M-m-m..."
            "Lily" "I've never felt like this!"
            show sc i_Lily_6_anim_3 with my_dissolve
            "[Name]" "(How her moans turn me on!)"
            "Lily" "Yes... Oh..."
            show sc i_Lily_6_anim_2 with my_dissolve
            "Lily" "Ah... Ah..."
            "Lily" "M-m-m-m..."
            call Lily_6_label_change_r from _call_Lily_6_label_change_r
            "[Name]" "Lily, I want to see you."
            show sc i_Lily_6_84 with my_dissolve
            "[Name]" "Lily, I want to see you."
            "[Name]" "To see you enjoying yourself."
            "[Name]" "Let me see your face."
            show sc i_Lily_6_85 with my_dissolve
            "Lily" "[Name]..."
            "Lily" "I want to see your face too."
            show sc i_Lily_6_86 with my_dissolve
            "Lily" "Like this?"
            "[Name]" "It's perfect."
            show sc i_Lily_6_87 with my_dissolve
            "Lily" "M-m-m..."
            "Lily" "Yes... Oh..."
            show sc i_Lily_6_88 with my_dissolve
            "Lily" "Ah...AH!"
            "[Name]" "{i}(This is definitely a pleasure she hasn't experienced before!){/i}"
            show sc i_Lily_6_89 with my_dissolve
            "Lily" "[Name].... Mhm..."
            show sc i_Lily_6_anim_4 with my_dissolve
            "Lily" "Yes...Oh..."
            "[Name]" "Mhm-mm..."
            show sc i_Lily_6_anim_5 with my_dissolve
            "Lily" "Yeah, there you go..."
            "Lily" "Go on...."
            show sc i_Lily_6_anim_6 with my_dissolve
            "[Name]" "Oh, Lily..."
            "Lily" "[Name]...."
            "[Name]" "Yes?"
            show sc i_Lily_6_90 with my_dissolve
            "Lily" "[Name]... Hold on a second..."
            "[Name]" "Yes, baby?"
            show sc i_Lily_6_79 with my_dissolve
            "Lily" "I can't do this anymore."
            "Lily" "I'm tired of wanting you."
            show sc i_Lily_6_80 with my_dissolve
            "Lily" "Fuck me right here and now."
            "Lily" "Fuck me so hard I can't stand!"
            "[Name]" "You don't have to ask for this twice."
            jump Lily_6_label_224
        "Classic" if not l6_sex_2:
            $ l6_sex_2 = True
            $ l6_sex = "Classic"
            show sc i_Lily_6_anim_7 with my_dissolve
            "[Name]" "{i}(All right, Lily, you asked for it.){/i}"
            show sc i_Lily_6_anim_7_z with my_dissolve
            "[Name]" "(You're about to find out what I'm really good at.)"
            "Lily" "[Name], start gently..."
            show sc i_Lily_6_91 with my_dissolve
            "[Name]" "Sure, baby."
            "[Name]" "{i}(I know how to handle the ladies, Lily. Don't worry.){/i}"
            show sc i_Lily_6_92 with my_dissolve
            "Lily" "Ah... there you go..."
            "Lily" "Go on..."
            show sc i_Lily_6_94 with my_dissolve
            "Lily" "Ah..."
            "Lily" "Ah, yes, oh, yes!"
            show sc i_Lily_6_84 with my_dissolve
            "[Name]" "Lily, baby, arch your back."
            "Lily" "Okay, sure....."
            show sc i_Lily_6_anim_8_a with my_dissolve
            "[Name]" "There you go!"
            show sc i_Lily_6_anim_8 with my_dissolve
            "Lily" "M-m-m..."
            "Lily" "Yeah... Oh..."
            show sc i_Lily_6_anim_9 with my_dissolve
            "Lily" "Ah...AH!"
            show sc i_Lily_6_anim_10 with my_dissolve
            "[Name]" "Do you like the way I enter inside you?"
            "Lily" "Yes..."
            show sc i_Lily_6_anim_11 with my_dissolve
            "Lily" "Oh yes..."
            "Lily" "More...."
            show sc i_Lily_6_96 with my_dissolve
            "[Name]" "I got something, baby!"
            "Lily" "Yeah... Oh..."
            show sc i_Lily_6_97 with my_dissolve
            "Lily" "What? Oh..."
            "[Name]" "I want to change positions."
            show sc i_Lily_6_98 with my_dissolve
            "Lily" "Change positions?"
            "Lily" "I had no idea you were such a naughty boy, [Name]."
            show sc i_Lily_6_99 with my_dissolve
            "[Name]" "What's wrong with that?"
            "[Name]" "I want to look into your eyes."
            show sc i_Lily_6_100 with my_dissolve
            "Lily" "You're right, [Name]..."
            "Lily" "I want to see your face as you enter me."
            show sc i_Lily_6_101 with my_dissolve
            "[Name]" "Come here, baby."
            "[Name]" "Let's melt into ecstasy."
            "[Name]" "Come to me..."
            show sc i_Lily_6_102 with my_dissolve
            "[Name]" "What the?!"
            "[Name]" "Did you hear that?"
            show sc i_Lily_6_103 with my_dissolve
            "[Name]" "Some kind of weird glowing mushroom. It doesn't seem to have been here before."
            "[Name]" "{i}(Was it just me, or was it moving?){/i}"
            show sc i_Lily_6_104 with my_dissolve
            "Lily" "What kind of mushroom? Ah... [Name], come here!"
            "[Name]" "But... You're right..."
            show sc i_Lily_6_105 with my_dissolve
            "[Name]" "I'm sorry, baby."
            "[Name]" "I got distracted."
            show sc i_Lily_6_106 with my_dissolve
            "Lily" "Ahh..."
            "[Name]" "But now I'm all yours!"
            show sc i_Lily_6_107 with my_dissolve
            "Lily" "Yeah... Oh..."
            "Lily" "Ah...AH!"
            show sc i_Lily_6_anim_12_a with my_dissolve
            "Lily" "Oh yes..."
            show sc i_Lily_6_anim_12 with my_dissolve
            "Lily" "More...."
            "Lily" "Ah...AH!"
            show sc i_Lily_6_anim_13 with my_dissolve
            "[Name]" "{i}(She keeps getting the shivers. I wonder how many times she cum?){/i}"
            "Lily" "Yeah...Oh..."
            show sc i_Lily_6_anim_14 with my_dissolve
            "[Name]" "{i}(She's so tight inside. It's hard for me to get a full on.){/i}"
            "Lily" "Ah..."
            show sc i_Lily_6_anim_15 with my_dissolve
            "Lily" "Ah...AH!"
            "[Name]" "{i}(But that seems to be enough for her...){/i}"
            "Lily" "Ah... More...."
            show sc i_Lily_6_107 with my_dissolve
            "[Name]" "Do you like everything, baby?"
            "Lily" "Oh yes... Oh yes!"
            show sc i_Lily_6_108 with my_dissolve
            "Lily" "But I'm ready to try something else."
            "[Name]" "Get on your knees!"
            show sc i_Lily_6_109 with my_dissolve
            "Lily" "The grass is so soft... Join me."
            "[Name]" "One second."
            show sc i_Lily_6_110 with my_dissolve
            "[Name]" "{i}(Let me enjoy the view.){/i}"
            "Lily" "Where are you..."
            show sc i_Lily_6_111 with my_dissolve
            "[Name]" "I'm here!"
            "Lily" "Ah...Fuck me already!"
            show sc i_Lily_6_112 with my_dissolve
            "[Name]" "Like that?"
            show sc i_Lily_6_113 with my_dissolve
            "Lily" "Yes... Oh..."
            "[Name]" "Let's change something!"
            show sc i_Lily_6_114 with my_dissolve
            "Lily" "Oh, what the..."
            "[Name]" "That's better!"
            show sc i_Lily_6_anim_16_a with my_dissolve
            "Lily" "Oh... Wow!"
            "Lily" "Ah..."
            show sc i_Lily_6_anim_16 with my_dissolve
            "[Name]" "Just like you asked for, beautiful."
            "Lily" "Oh, yeah... Ah..."
            show sc i_Lily_6_anim_17 with my_dissolve
            "[Name]" "So you can't walk!"
            "Lily" "Oh, yes... Oh, yes!"
            show sc i_Lily_6_anim_18 with my_dissolve
            "Lily" "Ahh..."
            "Lily" "Ah... AH!"
            show sc i_Lily_6_anim_19 with my_dissolve
            "Lily" "Ah... AH! Ah... AH!"
            "Lily" "Oh, yeah..."
            "[Name]" "Lily! I think..."
            show sc i_Lily_6_anim_18 with my_dissolve
            "[Name]" "I'm... Going to cum!"
            "Lily" "Hey! You're not going to come inside me, are you?"
            "Lily" "Don't you dare!"
            menu:
                "Cum inside":
    
        
                    show sc i_Lily_6_anim_18 with my_dissolve
                    "Lily" "Ah..."
                    "Lily" "Ah...Oh..."
                    show sc i_Lily_6_115 with my_dissolve
                    "Lily" "Ah... AH!"
                    "[Name]" "Oh..."
                    "[Name]" "Oh... Oh yes..."
                    show sc i_Lily_6_116 with my_dissolve
                    "Lily" "Ah..."
                    "Lily" "What was that...."
                    show sc i_Lily_6_117 with my_dissolve
                    "Lily" "YOU CAME IN ME?"
                    "Lily" "Are you completely retarded?"
                    show sc i_Lily_6_118 with my_dissolve
                    "[Name]" "It's gonna be okay, Lily. Don't worry about it."
                    "Lily" "I can't believe it!"
                    show sc i_Lily_6_119 with my_dissolve
                    "Lily" "Just let me go already."
                    "Lily" "How could you be so irresponsible? What a bastard!"
                    show sc i_Lily_6_120 with my_dissolve
                    "Lily" "Fucking..."
                    "[Name]" "Why do you care so much?"
                    show sc i_Lily_6_121 with my_dissolve
                    "Lily" "I'll have to take some crapy medicine to take care of it now."
                    "Lily" "That kind of magic affects your health, you know."
                    show sc i_Lily_6_122 with my_dissolve
                    "Lily" "Okay, I'll take care of this problem on my own..."
                    "Lily" "You better help me figure out how to get out of here."
                    show sc i_Lily_6_121 with my_dissolve
                    "Lily" "YOU IDIOT!!!"
                    "[Name]" "{i}(She seems a little upset.){/i}"
                    show sc i_Lily_6_131 with my_dissolve
                    menu:
                        "We have to go":
                            show sc i_Lily_6_132 with my_dissolve
                            "[Name]" "We have to go!"
                            "Lily" "Yeah, you're right."
                        "Hug her":
                            show sc i_Lily_6_133 with my_dissolve
                            "[Name]" "Baby..."
                            "[Name]" "Come here."
                            show sc i_Lily_6_134 with my_dissolve
                            "Lily" "M-m-m-m..."
                            "Lily" "[Name]..."
                            show sc i_Lily_6_131 with my_dissolve
                            "Lily" "We should go before we fall asleep..."
                            "[Name]" "You're right."
                    show sc i_Lily_6_135 with my_dissolve
                    "[Name]" "Come on, Lily. We should get out of here."
                    "Lily" "I know, I know. You think it's easy to put on a bra that fast?"
                    show sc i_Lily_6_136 with my_dissolve
                    "[Name]" "Hmm... I don't know."
                    "[Name]" "You took it off pretty fast."
                    show sc i_Lily_6_137 with my_dissolve
                    "Lily" "[Name]..."
                    "Lily" "I'm sleepy."
                    "[Name]" "I know. Hang in there."
                    jump Lily_6_label_442
                "Cum on her back":
                    scene image '#000' with Dissolve(.5)
                    show sc i_Lily_6_anim_18 with my_dissolve
                    "[Name]" "Oh... Oh yeah..."
                    "Lily" "Oh..."
                    show sc i_Lily_6_123 with my_dissolve
                    "[Name]" "Oh..."
                    "[Name]" "Oh... Oh yes..."
                    show sc i_Lily_6_124 with my_dissolve
                    "[Name]" "Ah..."
                    "Lily" "I can't believe how much of her there is!"
                    show sc i_Lily_6_125 with my_dissolve
                    "[Name]" "There's more!"
                    "[Name]" "Oh..."
                    show sc i_Lily_6_126 with my_dissolve
                    "[Name]" "...Oh yes..."
                    "Lily" "Hee hee hee!"
                    show sc i_Lily_6_127 with my_dissolve
                    "Lily" "And more?"
                    "Lily" "Unbelievable..."
                    show sc i_Lily_6_128 with my_dissolve
                    "[Name]" "Lily, you were incredible!"
                    "Lily" "[Name]..."
                    show sc i_Lily_6_129 with my_dissolve
                    "Lily" "That was something..."
                    "Lily" "I've never felt like that before."
                    show sc i_Lily_6_130 with my_dissolve
                    "Lily" "Thank you, [Name]."
                    "Lily" "I didn't expect THIS from you...."
                    show sc i_Lily_6_131 with my_dissolve
                    "[Name]" "I didn't expect it from myself."
                    "[Name]" "But you brought out the beast in me."
                    "Lily" "Hee hee hee!"
            show sc i_Lily_6_131 with my_dissolve
            menu:
                "We have to go":
                    show sc i_Lily_6_132 with my_dissolve
                    "[Name]" "We have to go!"
                    "Lily" "Yeah, you're right."
                "Hug her":

                    "[Name]" "Baby..."
                    "[Name]" "Come here."
                    show sc i_Lily_6_134 with my_dissolve
                    "Lily" "M-m-m-m..."
                    "Lily" "[Name]..."
                    show sc i_Lily_6_131 with my_dissolve
                    "Lily" "We should go before we fall asleep..."
                    "[Name]" "You're right."
            show sc i_Lily_6_135 with my_dissolve
            "[Name]" "Come on, Lily. We should get out of here."
            "Lily" "I know, I know. You think it's easy to put on a bra that fast?"
            show sc i_Lily_6_136 with my_dissolve
            "[Name]" "Hmm... I don't know."
            "[Name]" "You took it off pretty fast."
            show sc i_Lily_6_137 with my_dissolve
            "Lily" "[Name]..."
            "Lily" "I'm sleepy."
            "[Name]" "I know. Hang in there."
            jump Lily_6_label_442
        'Anal' if not l6_sex_3:
            $ l6_sex_3 = True
            $ l6_sex = "Anal"
            show sc i_Lily_6_anim_7 with my_dissolve
            "[Name]" "{i}(Hmm, what if?){/i}"
            show sc i_Lily_6_anim_7_z with my_dissolve
            "[Name]" "Lily, I want to try something."
            "[Name]" "Will you be patient for me?"
            show sc i_Lily_6_91 with my_dissolve
            "Lily" "Um... Well..."
            "Lily" "L-okay."
            show sc i_Lily_6_93 with my_dissolve
            "Lily" "Ouch..."
            "Lily" "Ouch... Careful there..."
            show sc i_Lily_6_95 with my_dissolve
            "[Name]" "{i}(It's so bouncy...){/i}"
            "[Name]" "{i}(The sensation is unspeakable...){/i}"
            show sc i_Lily_6_138 with my_dissolve
            "Lily" "Ouch! No... Wait, [Name]."
            "Lily" "I'm sorry. But no."
            show sc i_Lily_6_93 with my_dissolve
            "Lily" "Maybe another time..."
            "[Name]" "{i}(She said maybe another time?){/i}"
            "[Name]" "Okay, okay."
            jump Lily_6_label_224
    "[Name]" "We'll try it next time."
label Lily_6_label_434:
    show sc i_Lily_6_148 with my_dissolve
    "[Name]" "I'm sorry, Lily."
    "[Name]" "I can't even think about sex right now..."
    show sc i_Lily_6_149 with my_dissolve
    "[Name]" "Look how creepy it is!"
    "[Name]" "We can't stay here or we'll die for sure."
    "[Name]" "Let's run while we can!"
    show sc i_Lily_6_150 with my_dissolve
    "Lily" "I understand."
    "Lily" "Don't waste time!"
    "Lily" "Let's run!"
label Lily_6_label_442:
    scene image '#000' with Dissolve(.5)
    show sc i_Lily_6_151 with my_dissolve
    "[Name]" "{i}(Damn, my eyelids are getting heavier.){/i}"
    "[Name]" "{i}(I don't know if I can make it.){/i}"
    show sc i_Lily_6_152 with my_dissolve
    "[Name]" "{i}(We have to stay strong.){/i}"
    "[Name]" "Lily! I think I found a way out!"
    show sc i_Lily_6_153 with my_dissolve
    "[Name]" "Lily, where are you?"
    "[Name]" "{i}(Not again.){/i}"
    "[Name]" "What the hell?!"
    show sc i_Lily_6_154 with my_dissolve
    "[Name]" "Lily, get away from the mushroom! IT'S DANGEROUS!"
    "Lily" "Mmm, [Name].... It's so cozy in here."
    "Lily" "Come here."
    show sc i_Lily_6_155 with my_dissolve
    "[Name]" "(What? What the hell?)"
    "[Name]" "{i}(Am I dreaming? Or am I hallucinating?){/i}"
    show sc i_Lily_6_156 with my_dissolve
    "[Name]" "{i}(What does she want from me?){/i}"
    "Mushroom Girl" "Don't be afraid..."
    show sc i_Lily_6_157 with my_dissolve
    "Mushroom Girl" "I am a friend."
    "Mushroom Girl" "Come to me!"
    show sc i_Lily_6_158 with my_dissolve
    "[Name]" "{i}(Where am I...){/i}"
    "[Name]" "{i}(Sabrina?){/i}"
    show sc i_Lily_6_159 with my_dissolve
    "[Name]" "{i}(What's happening...){/i}"
    "[Name]" "{i}(I can't see...){/i}"
    "[Name]" "{i}(I can't... Lift my eyelids.){/i}"
    scene image '#000' with Dissolve(.5)
    scene sc i_Lily_6_200 with Dissolve(.5)
    "[Name]" "{i}(Where am I?){/i}"
    "[Name]" "{i}(How beautiful...){/i}"
    "[Name]" "{i}(I think I survived.){/i}"
    show sc i_Lily_6_201 with my_dissolve
    "[Name]" "{i}(What's that over there. Lily?){/i}"
    "[Name]" "{i}(I'm so glad she's all right.){/i}"
    "[Name]" "{i}(Well, I'll go find out what happened.){/i}"
    "[Name]" "{i}(And how she's doing.){/i}"
    show sc i_Lily_6_202 with my_dissolve
    "[Name]" "Hi..."
    "Lily" "[Name], you're awake!"
    "Lily" "I was worried..."
    "Lily" "The forest sucked a lot of energy out of you..."
    "[Name]" "Hmm, well..."
    show sc i_Lily_6_203 with my_dissolve
    "[Name]" "At least I got a good night's sleep!"
    "Lily" "Fool."
    show sc i_Lily_6_203_2 with my_dissolve
    "Lily" "Miss Spellman was worried, too."
    "Lily" "She went to pick night flowers."
    show sc i_Lily_6_204 with my_dissolve
    "[Name]" "Did she swear a lot?"
    "Lily" "I wouldn't say..."
    "Lily" "She was more worried than angry."
    "[Name]" "You said the forest sucked the energy out of me? How's that?"
    show sc i_Lily_6_205 with my_dissolve
    "Lily" "The mushroom forest we're in is a predator."
    "[Name]" "How so?"
    show sc i_Lily_6_206 with my_dissolve
    "Lily" "It's like one big trap..."
    "[Name]" "The whole forest?"
    "Lily" "Mushrooms release dormant spores."
    show sc i_Lily_6_207 with my_dissolve
    "Lily" "And then slowly devour the sleeping victims with their mycelium."
    "[Name]" "What an abomination..."
    "[Name]" "{i}(I wonder if she's seen those mushroom girls.){/i}"
    "[Name]" "Listen, did you see..."
    show sc i_Lily_6_208 with my_dissolve
    "Sabrina" "It seems you've already told our sleeping beauty all the interesting stuff, Lily."
    "Sabrina" "How are you feeling, [Name]?"
    "[Name]" "I'm fine... I guess."
    show sc i_Lily_6_209 with my_dissolve
    "[Name]" "Miss Spellman, I'm so sorry about what happened."
    "[Name]" "I broke your compass and we..."
    "[Name]" "We let you down."
    show sc i_Lily_6_210 with my_dissolve
    "Sabrina" "I'm glad you understand the gravity of your transgression."
    "Sabrina" "But the important thing is that you are both safe and sound."
    "[Name]" "{i}(She is too kind to us...){/i}"
    "[Name]" "{i}(I never knew such caring people.){/i}"
    show sc i_Lily_6_211 with my_dissolve
    "Sabrina" "Well, I see you've had your rest!"
    "Lily" "I'm ready."
    "[Name]" "Me too."
    "Sabrina" "That's great! Because I wasn't planning on spending the night in the woods."
    show sc i_Lily_6_212 with my_dissolve
    "Sabrina" "Let's go home!"
    scene image '#000' with Dissolve(.5)
    scene sc i_Lily_6_213 with Dissolve(.5)
    "[Name]" "Home, sweet home!"
    "Lily" "At last I can go to bed and not be afraid of being sucked dry by a mushroom."
    show sc i_Lily_6_214 with my_dissolve
    "[Name]" "Don't remind me..."
    "[Name]" "Listen, Lily."
    "[Name]" "About what happened in the woods..."
    "Lily" "I don't want to talk about it..."
    show sc i_Lily_6_215 with my_dissolve
    "[Name]" "Wait, Lily!"
    "[Name]" "I don't want to talk!"
    "Lily" "Then what is it?"
    if hasattr(store, 'l6_yes'):
        show sc i_Lily_6_215 with my_dissolve
        "[Name]" "Just this."
        show sc i_Lily_6_216 with my_dissolve
        "Lily" "Oh, [Name]..."
        "Lily" "Mm-hmm..."
    else:
        show sc i_Lily_6_217 with my_dissolve
        "[Name]" "..."
        "Lily" "..."
    show sc i_Lily_6_218 with my_dissolve
    "Lily" "I have to go...."
    "[Name]" "Good night, Lily."
    return

















label Lily_6_label_change_r:
    menu:
        "Pose 1":
            scene sc i_Lily_6_anim_2 with Dissolve(.5)
            $ renpy.pause(9999)
            call Lily_6_label_change_r from _call_Lily_6_label_change_r_1
        "Pose 2":
            scene Lily_6_anim_1 with Dissolve(.5)
            $ renpy.pause(9999)
            call Lily_6_label_change_r from _call_Lily_6_label_change_r_2
        "Continue":
            return
