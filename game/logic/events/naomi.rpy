



label naomi_events_label:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.5)

    $ set_now =  naomi_events_set
    menu:
        "0 Talk to Naomi" if Q_Naomi == 0:



            call Naomi_1_label from _call_Naomi_1_label
            $ p_up('Naomi', 2)
            $ Q_Naomi=1
            
    

            $ log_message.update({"QLOG_Naomi":1 })
            $ naomi_events_set.append("1 Talk to Naomi")
            $ wakeup_sets.append([

            
            naomi_events_set, "1 Talk to Naomi"
            
            
                ])
        "1 Talk to Naomi" if Q_Naomi == 1:

            call Naomi_1_1_label from _call_Naomi_1_1_label

            $ log_message.update({"QLOG_Naomi":2})
            $ naomi_events_set.append("1 Talk to Naomi")
            $ wakeup_sets.append([

            
            naomi_events_set, "1 Talk to Naomi"
            
            
                ])

        "2 Talk to Naomi" if Q_Naomi == 2:

            call Naomi_1_2_label from _call_Naomi_1_2_label

            $ log_message.update({"QLOG_Naomi":4})
            $ naomi_events_set.append("2 Talk to Naomi")
            $ wakeup_sets.append([

            
            naomi_events_set, "2 Talk to Naomi"
            
            
                ])

        "3 Talk to Naomi" if Q_Naomi == 3:

            call Naomi_1_3_label from _call_Naomi_1_3_label

            $ log_message.update({"QLOG_Naomi":5})
            $ naomi_events_set.append("3 Talk to Naomi")
            $ wakeup_sets.append([

            
            naomi_events_set, "3 Talk to Naomi"
            
            
                ])


        "5 Talk to Naomi" if Q_Naomi == 5:

            call Naomi_6_label from _call_Naomi_6_label
            $ p_up('Naomi', 6)
            $ log_message.update({"QLOG_Naomi":7})
            $ Q_Naomi = 6
        "Not now" if True:


            show screen main_interface 
            show screen show_hide_locations_2
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label

label naomi_events_2_label:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.5)

    $ set_now =  naomi_events_set_2
    menu:

        "0 Talk to Naomi" if Q_Naomi == 0:
            call Naomi_2_1_label from _call_Naomi_2_1_label

            $ log_message.update({"QLOG_Naomi":1})
            $ naomi_events_set_2.append("0 Talk to Naomi")
            $ wakeup_sets.append([

            
            naomi_events_set_2, "0 Talk to Naomi"
            
            
                ])
        "1 Talk to Naomi" if Q_Naomi == 1:
            call Naomi_2_2_label from _call_Naomi_2_2_label

            $ log_message.update({"QLOG_Naomi":2})
            $ naomi_events_set_2.append("1 Talk to Naomi")
            $ wakeup_sets.append([

            
            naomi_events_set_2, "1 Talk to Naomi"
            
            
                ])

        "2 Talk to Naomi" if Q_Naomi == 2:
            call Naomi_3_label from _call_Naomi_3_label
            $ p_up('Naomi', 4)
            $ log_message.update({"QLOG_Naomi":5})
            $ Q_Naomi = 3
            $ naomi_events_set_2.append("3 Talk to Naomi")
            $ wakeup_sets.append([

            
            naomi_events_set_2, "3 Talk to Naomi"
            
            
                ])

        "3 Talk to Naomi" if Q_Naomi == 3:
            call Naomi_2_3_label from _call_Naomi_2_3_label

            $ log_message.update({"QLOG_Naomi":5})

            $ naomi_events_set_2.append("3 Talk to Naomi")
            $ wakeup_sets.append([

            
            naomi_events_set_2, "3 Talk to Naomi"
            
            
                ])
        "5 Talk to Naomi" if Q_Naomi == 5:
            call Naomi_2_4_label from _call_Naomi_2_4_label
            $ naomi_events_set_2.append("5 Talk to Naomi")
            $ wakeup_sets.append([

            
            naomi_events_set_2, "3 Talk to Naomi"
            
            
                ])
        "Not now" if True:
            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label
label naomi_events_3_label:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.5)

    $ set_now =  naomi_events_set_3
    menu:



        "0 Talk to Naomi" if Q_Naomi == 0:
            call Naomi_3_1_label from _call_Naomi_3_1_label

            $ log_message.update({"QLOG_Naomi":5})
            $ set_stubs(naomi_events_set_3, "0 Talk to Naomi")


        "1 Talk to Naomi" if Q_Naomi == 1:
            call Naomi_2_label from _call_Naomi_2_label
            $ p_up('Naomi', 3)
            $ log_message.update({"QLOG_Naomi":3})
            $ Q_Naomi = 2

            $ time_up()

        "2 Talk to Naomi" if Q_Naomi == 2:
            call Naomi_3_2_label from _call_Naomi_3_2_label

            $ log_message.update({"QLOG_Naomi":4})
            $ set_stubs(naomi_events_set_3, "2 Talk to Naomi")

        "3 Talk to Naomi" if Q_Naomi == 3:
            call Naomi_4_label from _call_Naomi_4_label
            call Naomi_5_label from _call_Naomi_5_label
            $ Q_Naomi=5
            $ p_up('Naomi', 5)
            $ log_message.update({"QLOG_Haley":6})
            $ time_up()

        "5 Talk to Naomi" if Q_Naomi == 5:
            call Naomi_3_3_label from _call_Naomi_3_3_label
            $ set_stubs(naomi_events_set_3, "5 Talk to Naomi")
        "6 Talk to Naomi" if Q_Naomi == 6:
            call Naomi_7_label from _call_Naomi_7_label

            scene image '#000' with Dissolve(.5)

            call Naomi_8_label from _call_Naomi_8_label
            $ p_up('Naomi', 7)
            $ Q_Naomi = 8
            $ change_location_2(location_now, time_now+1)

        "Not now" if True:


            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label

    show screen main_interface 
    hide screen black_tmp_screen_menu

    with Dissolve(.5)
    jump main_interface_label


label Naomi_1_label:

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

    show sc i_Naomi_1_7 with Dissolve(.5)
    "[Name]" "Hi!"
    show sc i_Naomi_1_2 with my_dissolve
    "Naomi" "Hey! [Name], right?"
    show sc i_Naomi_1_7 with my_dissolve
    "[Name]" "That's right."
    "[Name]" "It's good to see you, Naomi."
    show sc i_Naomi_1_2 with my_dissolve
    "Naomi" "You got into the same house as Lily, right?"
    "[Name]" "Yeah, Leonheart."
    show sc i_Naomi_1_19 with my_dissolve
    "Naomi" "So how's Leonheart treating you, do you regret it yet?"
    "Naomi" "Sorry you had to end up there."
    show sc i_Naomi_1_18 with my_dissolve
    "Naomi" "Well, what can you do, Adderin only picks the best..."
    "[Name]" "{i}(Naive girl.){/i}"
    "[Name]" "{i}(If you only knew how hard Katrina tried to make me choose her.){/i}"
    show sc i_Naomi_1_9 with my_dissolve
    "[Name]" "I'm happy with the way things turned out."
    "[Name]" "Especially since I could have easily been in Adderin."
    show sc i_Naomi_1_14 with my_dissolve
    "Naomi" "Pfft.{w} Keep telling yourself that and someday you'll believe it."
    "[Name]" "{i}(She's so stubborn.){/i}"
    "[Name]" "Let's change the subject."
    show sc i_Naomi_1_22 with my_dissolve
    "Naomi" "Is it hard to face the truth?"
    "[Name]" "Not at all, but I didn't come to argue."

    "Naomi" "For what then?"
    show sc i_Naomi_1_10 with my_dissolve
    "[Name]" "No reason."
    "[Name]" "I wanted to get to know you better."
    "[Name]" "{i}(Let's see how prickly the cactus is, so to speak...){/i}"
    "[Name]" "Maybe we're kindred spirits."
    show sc i_Naomi_1_11 with my_dissolve
    "Naomi" "You and me?"
    show sc i_Naomi_1_15 with my_dissolve
    "Naomi" "Ha-ha-ha-ha."
    "Naomi" "That's funny."
    "[Name]" "What's so funny about that?"
    show sc i_Naomi_1_19 with my_dissolve
    "Naomi" "Have you heard the saying about the eagle and the hen?"
    "[Name]" "Why fly like a hen when you can soar like an eagle?"



    menu:
        "Tease Naomi" if True:
            $ pass
        "Reply romantically" if True:
            jump Naomi_1_label_45

    show sc i_Naomi_1_19 with my_dissolve
    "[Name]" "Hey little chick, don't get it twisted."
    "[Name]" "Let the eagle decide whether to fly with you or not."
    show sc i_Naomi_1_21 with my_dissolve
    "Naomi" "Jackass!"
    "Naomi" "Where do you get the right to talk to me like that?"
    "[Name]" "You have double standards."
    show sc i_Naomi_1_4 with my_dissolve
    "Naomi" "Why is that?"
    "[Name]" "I was just using your words."
    show sc i_Naomi_1_3 with my_dissolve
    "Naomi" "You called me a chicken!"
    show sc i_Naomi_1_24 with my_dissolve
    "[Name]" "Chick."
    "[Name]" "You drew your own conclusions."

    "Naomi" "Argh! Fuck you!"
    "Naomi" "What are you picking on me for?"
    jump Naomi_1_label_55
label Naomi_1_label_45:
    show sc i_Naomi_1_10 with my_dissolve
    "[Name]" "Even a hen can soar like an eagle if she sets her mind to it."
    "[Name]" "If I were a wizard with a little more experience, I'd prove it to you."
    show sc i_Naomi_1_19 with my_dissolve
    "Naomi" "What, you'd turn into a chicken?"
    "[Name]" "What? No..."
    show sc i_Naomi_1_11 with my_dissolve
    "Naomi" "That's a shame, I'd watch that."
    show sc i_Naomi_1_10 with my_dissolve
    "[Name]" "Why are you trying so hard to act cold to me?"
    "[Name]" "Have you ever tried to make friends before?"
    "[Name]" "Does your method even work?"
    show sc i_Naomi_1_4 with my_dissolve
    "Naomi" "Why would I want to make friends?"
    "Naomi" "Why are you picking on me anyway?"
label Naomi_1_label_55:
    show sc i_Naomi_1_8 with my_dissolve
    "[Name]" "I want to get to know you better, I told you."
    "[Name]" "{i}(There must be something human underneath all your barbs.){/i}"
    show sc i_Naomi_1_12 with my_dissolve
    "Naomi" "All right!"
    "[Name]" "All right?"
    show sc i_Naomi_1_3 with my_dissolve
    "Naomi" "All right! But not right now."
    "Naomi" "I'm getting ready for class."
    show sc i_Naomi_1_6 with my_dissolve
    "[Name]" "Sure, I understand."
    "[Name]" "Let's meet later."
    "[Name]" "I'll find you."
    show sc i_Naomi_1_23 with my_dissolve
    "Naomi" "Whatever you say."


    "Naomi" "Now leave me alone!"

    return

label Naomi_2_label:

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
    show sc i_Naomi_2_3 with Dissolve(.5)
    "[Name]" "Hi, girls!"
    "Lily" "Hey there!"
    "Naomi" "Yo."
    "[Name]" "Naomi, mind if I kidnap you?"
    "[Name]" "We were supposed to meet."
    "Naomi" "I don't know, um..."
    "Naomi" "You know, I'm hanging out with my friend..."
    "[Name]" "{i}(Are you trying to stand me up?){/i}"
    show sc i_Naomi_2_4 with my_dissolve
    "Lily" "Oh, I was just leaving."
    "[Name]" "{i}(Good girl.){/i}"
    "Lily" "I still have to go..."
    "Naomi" "No, wait..."
    "Lily" "Oh, there's so much to do!"
    "Lily" "Bye Naomi, it was good seeing you."
    show sc i_Naomi_2_5 with my_dissolve
    "Naomi" "Bye-bye."
    "[Name]" "Well, here we are alone!"
    show sc i_Naomi_2_8 with my_dissolve
    "Naomi" "I'm thrilled."
    "[Name]" "Why do you have to be so sarcastic?"
    "[Name]" "You didn't even give me a chance."
    show sc i_Naomi_2_6 with my_dissolve
    "Naomi" "Why should I waste my time with you?"
    "Naomi" "I'm not here to hang out with just anybody."
    "[Name]" "I'm not just anybody."
    "Naomi" "You're not?"
    show sc i_Naomi_2_24 with my_dissolve
    "Naomi" "You're just a Leonheart."
    "[Name]" "Just like your friend Lily."
    show sc i_Naomi_2_16 with my_dissolve
    "Naomi" "Pfft. That's different."
    "[Name]" "Even if you're right about your house superiority, and you're not."
    "[Name]" "You still don't have the right to lump everyone together."
    show sc i_Naomi_2_17 with my_dissolve
    "Naomi" "Oh, really?"
    "Naomi" "What's so special about you?"
    menu:
        "A charming smile." if True:
            $ pass
        "Find out for yourself." if True:
            jump Naomi_2_label_43
    show sc i_Naomi_2_9 with my_dissolve
    "[Name]" "Isn't my charming smile enough for you?"
    "Naomi" "A smile is a smile."
    "Naomi" "Obviously, it's not enough."
    "[Name]" "Ouch."
    "[Name]" "Do you always respond to jokes like that?"
    show sc i_Naomi_2_10 with my_dissolve
    "Naomi" "No."
    "Naomi" "Just the bad ones."
    "[Name]" "{i}(Now that really hurts.){/i}"
    "[Name]" "{i}(Shouldn't provoke her...){/i}"
    jump Naomi_2_label_55
label Naomi_2_label_43:

    show sc i_Naomi_2_17 with my_dissolve
    "[Name]" "Try me out and you'll find out."
    "[Name]" "You'll be pleasantly surprised."
    show sc i_Naomi_2_20 with my_dissolve
    "Naomi" "Ah-ha-ha."
    "Naomi" "What's that supposed to mean?"
    "Naomi" "Or do you think all girls get wet from a confident voice?"
    "[Name]" "{i}(She's trying to put me off with her taunts.){/i}"
    "[Name]" "{i}(But I'll get her.){/i}"
    show sc i_Naomi_2_10 with my_dissolve
    "[Name]" "{i}I'm not interested in ″all girls.″{/i}"
    "[Name]" "I'm talking to you."
    show sc i_Naomi_2_16 with my_dissolve
    "Naomi" "Against my wishes."
    "[Name]" "For now."
    "Naomi" "I don't plan to spend the whole evening here."
label Naomi_2_label_55:

    show sc i_Naomi_2_19 with my_dissolve
    "Naomi" "Is that all you wanted to surprise me with?"
    "[Name]" "I haven't even started yet."
    show sc i_Naomi_2_8 with my_dissolve
    "Naomi" "Then start."
    "[Name]" "{i}(Whatever I do now, she won't admit she's wrong.){/i}"
    "[Name]" "{i}(I need to make it so she can't doubt the outcome.){/i}"
    "[Name]" "{i}(I have an idea!){/i}"
    show sc i_Naomi_2_9 with my_dissolve
    "[Name]" "No."
    show sc i_Naomi_2_6 with my_dissolve
    "Naomi" "{i}What do you mean ″no″? Then I'm off!{/i}"
    "[Name]" "Wait."
    "[Name]" "I'm not taking my words back."
    "[Name]" "But think about it: my job is to surprise you, right?"
    show sc i_Naomi_2_19 with my_dissolve
    "Naomi" "And?"
    "[Name]" "You think that because I am in Leonheart, I am not worthy to be with you from Adderin."
    "[Name]" "And I need to prove that I could succeed as an Adderin."
    "Naomi" "That's right."
    show sc i_Naomi_2_17 with my_dissolve
    "Naomi" "And you don't stand a chance. Sorry about the spoiler."
    show sc i_Naomi_2_20 with my_dissolve
    "[Name]" "It's okay, I'll try."
    "[Name]" "I propose this: A problem that only an Adderin could solve..."
    "[Name]" "Only an Adderin could come up with."
    show sc i_Naomi_2_22 with my_dissolve
    "Naomi" "Hmm, I hadn't thought of that..."
    "[Name]" "So the most logical thing would be for you to come up with a challenge for me!"
    "Naomi" "You're right."
    "Naomi" "But what could I come up with that even you would understand you couldn't handle?"
    "[Name]" "Anything."
    show sc i_Naomi_2_16 with my_dissolve
    "Naomi" "Anything, you say?"
    "[Name]" "{i}(That's it! There you go, Naomi...){/i}"
    "[Name]" "{i}(I knew you pass up this opportunity.){/i}"
    "[Name]" "{i}(Let's see what your imagination can do.){/i}"
    "[Name]" "{i}(Though how am I supposed to deal with this...){/i}"
    "[Name]" "Within reason."
    show sc i_Naomi_2_24 with my_dissolve
    "Naomi" "That's a flexible concept."
    "[Name]" "{i}(You're starting to scare me...){/i}"
    "Naomi" "Okay, I agree."
    "Naomi" "But I need to think about your assignment."
    "[Name]" "Nothing comes to mind?"
    show sc i_Naomi_2_17 with my_dissolve
    "Naomi" "Oh, a lot..."
    "Naomi" "But why waste such fun on the first thing that comes to mind?"
    "Naomi" "It's not every day a hen tries to become an eagle."
    "Naomi" "Well, all right, that's enough of that."
    "Naomi" "I had other things to do."
    "[Name]" "Good luck."
    return

label Naomi_3_label:

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


    show sc i_Naomi_3_1 with Dissolve(.5)
    "[Name]" "Naomi! {w} Hi!"
    show sc i_Naomi_3_2 with my_dissolve
    "Naomi" "[Name], good to see you!"
    "[Name]" "Is it really you Naomi, or am I talking to a doppelganger?"
    show sc i_Naomi_3_3 with my_dissolve
    "Naomi" "What are you talking about?"
    "[Name]" "{i}Where did all your ″Back off, don't waste my time″ go?{/i}"
    "[Name]" "{i}And where did you get that ″It's good to see you″?{/i}"
    show sc i_Naomi_3_4 with my_dissolve
    "Naomi" "Oh, that's what you're talking about."
    "Naomi" "You're not offended, are you?"
    "Naomi" "I just wasn't in the mood."
    "[Name]" "{i}(There's something wrong here...){/i}"
    "[Name]" "{i}(She's too nice.){/i}"
    show sc i_Naomi_3_5 with my_dissolve
    "[Name]" "Really?"
    "Naomi" "Of course."
    "Naomi" "Especially since you're about to prove to me that you're worthy."
    "Naomi" "Isn't that great?"
    show sc i_Naomi_3_6 with my_dissolve
    "[Name]" "{i}(So that's what this is about...){/i}"
    "[Name]" "{i}(Have you thought of something that I would just say no to?){/i}"
    "[Name]" "And more specifically?"
    show sc i_Naomi_3_7 with my_dissolve
    "Naomi" "I've suddenly run into a problem."
    "Naomi" "One that might jeopardize my plans for Adderin."
    "Naomi" "You could help me and help a noble cause."
    show sc i_Naomi_3_8 with my_dissolve
    "[Name]" "So what's the problem, Naomi?"
    show sc i_Naomi_3_9 with my_dissolve
    "Naomi" "Well, you see. It's a delicate matter and I..."
    "Naomi" "I really want to trust you..."
    show sc i_Naomi_3_10 with my_dissolve
    "[Name]" "{i}(What the...){/i}"
    "[Name]" "{i}(Is she teasing me so I can be more easily manipulated?){/i}"
    "[Name]" "{i}(Girl, you got the wrong guy.){/i}"
    "[Name]" "{i}(Should I play along and see what happens next, or get it over with?){/i}"


    menu:
        "Stop her" if True:


            $ pass
        "Play along" if True:
            jump Naomi_3_label_39

    show sc i_Naomi_3_11 with my_dissolve
    "[Name]" "I'm sorry, I have other things to do."
    "Naomi" "But I..."
    "[Name]" "I don't have time for these games."
    show sc i_Naomi_3_12 with my_dissolve
    "[Name]" "Bye, Naomi."
    "Naomi" "Wait, um... I..."
    "Naomi" "You didn't like it at all?"
    "[Name]" "Get to the point, Naomi."
    jump Naomi_3_label_54
label Naomi_3_label_39:

    show sc i_Naomi_3_10 with my_dissolve
    "[Name]" "You can trust me."
    show sc i_Naomi_3_13 with my_dissolve
    "[Name]" "W-what are you doing?"
    show sc i_Naomi_3_14 with my_dissolve
    "Naomi" "Who doesn't like to be treated like a hero?"
    scene sc i_Naomi_3_anim_1 with Dissolve(.5)
    "[Name]" "Someone could see us!"
    "Naomi" "They might..."
    "Naomi" "I guess I'm just trying to say..."

    "Naomi" "...that I value loyalty..."
    scene sc i_Naomi_3_anim_2 with Dissolve(.5)
    "Naomi" "Very highly..."
    "[Name]" "{i}(Damn... She's good...){/i}"
    "[Name]" "{i}(Just a little bit more and...){/i}"
    show sc i_Naomi_3_15 with my_dissolve

    "Naomi" "And that's just a taste of what my hero will get."
    show sc i_Naomi_3_16 with my_dissolve
    "Naomi" "After he helps me."
    "[Name]" "{i}(You're adorably conniving...){/i}"
    show sc i_Naomi_3_17 with my_dissolve
    "[Name]" "I wish I knew what it takes to become your hero."
    "Naomi" "Oh, the task is pretty simple."
label Naomi_3_label_54:

    "Naomi" "I just need one picture."
    show sc i_Naomi_3_18 with my_dissolve
    "[Name]" "{i}(What a coincidence....){/i}"
    "[Name]" "{i}It's funny: before this ″magic″ thing happened in my life...{/i}"
    "[Name]" "I was a photographer."
    show sc i_Naomi_3_19 with my_dissolve
    "Naomi" "Screw you!"
    "Naomi" "So, taking a {b}picture of the answers to a potions test{/b}... "
    "Naomi" "...wouldn't be a problem for you?"
    show sc i_Naomi_3_20 with my_dissolve
    "[Name]" "Wait... What?"
    "[Name]" "Are you crazy?"
    show sc i_Naomi_3_21 with my_dissolve
    "Naomi" "Relax. It's easier than you think."
    "Naomi" "I've got it all planned."
    "[Name]" "{i}(You bet you have.){/i}"
    "[Name]" "I have to think."

    "Naomi" "Then think faster."
    "Naomi" "When you make up your mind, meet me in the yard tonight."
    "[Name]" "Okay. "
    return


label Naomi_4_label:

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

    show sc i_Naomi_2_1 with Dissolve(.5)
    "[Name]" "Hi, girls!"
    show sc i_Naomi_2_2 with my_dissolve
    "[Name]" "Naomi. Are you free?"
    "Naomi" "Yeah, we just finished discussing class."
    show sc i_Naomi_2_5 with my_dissolve
    "Lily" "It was nice to see you, I'm gonna run."
    "Naomi" "Good luck, Lily!"
    show sc i_Naomi_2_7 with my_dissolve
    "Naomi" "You came after all!"
    "[Name]" "Yep. "
    "Naomi" "So are you in?"
    show sc i_Naomi_2_15 with my_dissolve
    "[Name]" "First, tell me what your plan is."
    show sc i_Naomi_2_16 with my_dissolve
    "Naomi" "I'm gonna knock on the door and distract Ms. Spellman..."
    "Naomi" "You sneak in and take a picture of the test."
    "Naomi" "It's a piece of cake."
    show sc i_Naomi_2_19 with my_dissolve
    "[Name]" "You really think so?"
    "[Name]" "Your plan is a disaster."
    "[Name]" "You haven't thought through the details."
    "[Name]" "There's a few dozen things that might not go according to plan!"
    show sc i_Naomi_2_17 with my_dissolve
    "Naomi" "Yeah."
    "Naomi" "Well you wanted a test!"
    "Naomi" "So you're in?"
    show sc i_Naomi_2_10 with my_dissolve
    "[Name]" "You only live once."
    "[Name]" "I'm in."
    show sc i_Naomi_2_24 with my_dissolve
    "Naomi" "You are?"
    "[Name]" "Absolutely."
    show sc i_Naomi_2_7 with my_dissolve
    "Naomi" "Oh, my God. I wasn't sure you'd say yes!"
    "[Name]" "{i}(Wow... Maybe this is really important to her.){/i}"
    "[Name]" "{i}(Was I too harsh in my judgment?){/i}"
    "Naomi" "Thank you!"
    show sc i_Naomi_2_6 with my_dissolve
    "Naomi" "Well, let's not waste any time then!"
    show sc i_Naomi_2_14 with Dissolve(.5)



    menu:
        "Agreed!" if True:
            jump Naomi_4_label_44
        "Not today" if True:
            $ pass

    "[Name]" "Not today!"
    show sc i_Naomi_2_9 with my_dissolve
    "[Name]" "I need to get ready."
    "[Name]" "And find a camera."
    "[Name]" "How about another night?"
    show sc i_Naomi_2_8 with my_dissolve
    "Naomi" "We don't have another night, [Name]!"
    "Naomi" "You don't need a camera. You can have mine."
    "[Name]" "{i}(Damn, she's right...){/i}"
    show sc i_Naomi_2_19 with my_dissolve
    "Naomi" "Hurry up before Sabrina leaves."
    "[Name]" "Ugh... Well, okay."
    "Naomi" "You're the best."
    return
label Naomi_4_label_44:

    show sc i_Naomi_2_10 with my_dissolve
    "[Name]" "What's the holdup?"
    "[Name]" "Let's do it."
    return


label Naomi_5_label:

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

    show sc i_Naomi_5_1 with Dissolve(.5)
    "Naomi" "Oh, Miss Spellman!"
    "Naomi" "I'm so glad you're still here!"
    show sc i_Naomi_5_2 with my_dissolve
    "Sabrina" "Naomi? Honey, what's wrong?"
    "Sabrina" "Why are you crying?"
    show sc i_Naomi_5_3 with my_dissolve
    "Naomi" "I.. I.. I don't know what to say!"
    "Naomi" "It's so scary and painful..."
    "Sabrina" "Come on, honey. You can be honest with me..."
    show sc i_Naomi_5_4 with my_dissolve
    "Sabrina" "Let's go to the ladies' room."
    "Sabrina" "We'll wash those tears away. Okay?"
    "[Name]" "{i}(This is my chance!){/i}"
    "[Name]" "{i}(Better not waste time here.){/i}"
    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.5)

    scene sc i_Naomi_5_11 with Dissolve(.5)
    "[Name]" "{i}(There's something special about this place.){/i}"
    "[Name]" "{i}(Being here alone, this time of day. It's peaceful.){/i}"
    "[Name]" "{i}(Alas, I don't have time for this meditative nonsense.){/i}"
    show sc i_Naomi_5_5 with my_dissolve
    "[Name]" "{i}(I bet the test answers are on her desk.){/i}"
    show sc i_Naomi_5_6 with my_dissolve
    "[Name]" "{i}(So, what do we have here?){/i}"
    show sc i_Naomi_5_7 with my_dissolve
    "[Name]" "{i}(Freshman list.){/i}"
    "[Name]" "{i}(Nothing of interest.){/i}"
    show sc i_Naomi_5_8 with my_dissolve
    "[Name]" "{i}(Looks like Sabrina's notebook.){/i}"
    "[Name]" "{i}(Mostly ideas for new potions, a few notes about students.){/i}"
    "[Name]" "{i}(Zero information about the test.){/i}"
label Naomi_5_label_24:
    show sc i_Naomi_5_9 with my_dissolve
    "[Name]" "{i}(What do we have here?){/i}"
    "[Name]" "{i}(Test answers! Bingo!){/i}"
    show sc i_Naomi_5_10 with my_dissolve
    "[Name]" "{i}(Let's take some pictures!){/i}"
    scene expression '#fff' with Dissolve(.5)
    play sound 'audio/new/sounds/Phone_Photo.mp3'
    scene sc i_Naomi_5_10 with Dissolve(.75)
    $ renpy.pause(999999)

    scene sc i_Naomi_5_11 with Dissolve(1)
    "[Name]" "{i}(My work here is done.){/i}"
    "[Name]" "{i}(Let's not overstay our welcome.){/i}"
    show sc i_Naomi_5_13 with my_dissolve
    "[Name]" "{i}(... Did I hear something?){/i}"
    "[Name]" "{i}(...){/i}"
    show sc i_Naomi_5_12 with my_dissolve
    "[Name]" "{i}(... Shit!){/i}"
    "[Name]" "{i}(Naomi, what the fuck!){/i}"
    show sc i_Naomi_5_14 with my_dissolve
    "[Name]" "{i}(Think, [Name]!..Think!){/i}"
    "[Name]" "{i}(What do I do?){/i}"
    show sc i_Naomi_5_15 with my_dissolve
    "[Name]" "{i}(I need to hide.){/i}"
    "[Name]" "{i}(This will do.){/i}"
    show sc i_Naomi_5_17 with my_dissolve
    "[Name]" "{i}(If she doesn't focus her attention on me.){/i}"
    "[Name]" "{i}(Please just take what you need and go away.){/i}"
    show sc i_Naomi_5_18 with my_dissolve
    "Sabrina" "Okay, everything seems to be in order..."
    "Sabrina" "And ready for test."
    show sc i_Naomi_5_16 with my_dissolve
    "Sabrina" "Now I can finally get to relaxing..."
    "[Name]" "{i}(I hope you're not planning on doing it here...){/i}"
    "[Name]" "{i}(Things are bad, Sabrina's too close.){/i}"
    "[Name]" "{i}(If I move or make a sound, she'll notice right away.){/i}"
    show sc i_Naomi_5_19 with my_dissolve
    "Jacob" "Oh, I'm so lucky to meet you here at this time of day!"
    show sc i_Naomi_5_20 with my_dissolve
    "Sabrina" "Jacob?"
    "Sabrina" "What do you want?"
    "Jacob" "Oh, that's a very important question, my dear."
    show sc i_Naomi_5_21 with my_dissolve
    "Sabrina" "Can it wait until tomorrow? I just got off work."
    "Jacob" "I've waited long enough, Sabrina."
    "Jacob" "And my patience is melting like ice in the middle of July."
    "Sabrina" "Please, spare me all of that. What do you want?"
    show sc i_Naomi_5_22 with my_dissolve
    "Jacob" "It's time to choose your side, Sabrina."
    "Jacob" "With your testimony, I can prove that old fool..."
    "Jacob" "...is incapable of running our prestigious academy."
    "[Name]" "{i}(Holy crap! He's plotting against the headmaster?){/i}"
    "[Name]" "{i}(Why do I always get myself into these situations?){/i}"
    "Jacob" "You know I'm right!"
    show sc i_Naomi_5_23 with my_dissolve
    "Sabrina" "No, I don't!"
    "Sabrina" "Stop this revolutionary madness!"
    show sc i_Naomi_5_24 with my_dissolve
    "Sabrina" "I don't know what Arthur did to piss you off!"
    "Sabrina" "But stop trying to drag me into this."
    "Jacob" "Your emotions are understandable."
    show sc i_Naomi_5_25 with my_dissolve
    "Jacob" "I want you to know that I'm not holding a grudge."
    "Jacob" "I know you want what's best for the academy."
    "Jacob" "And I'll keep that in mind when I become a headmaster."
    show sc i_Naomi_5_26 with my_dissolve
    "Sabrina" "Since when is an elegantly concealed threat better than a plain one?"
    "Sabrina" "Be a man and tell me directly what you're hinting at."
    "[Name]" "{i}(Ouch... That's got to hurt.){/i}"
    show sc i_Naomi_5_27 with my_dissolve
    "Jacob" "All I said was that your passion for this place..."
    "Jacob" "...really touches my heart."
    show sc i_Naomi_5_28 with my_dissolve
    "Jacob" "And nothing more."
    "Jacob" "Good night, Miss Spellman."
    show sc i_Naomi_5_29 with my_dissolve
    "Sabrina" "Yeah, it's time for you to go."
    "Sabrina" "Asshole!"
    show sc i_Naomi_5_30 with my_dissolve
    "Sabrina" "Why does he act like this is some kind of game..."
    "Sabrina" "And why do I feel so weak around him?"
    show sc i_Naomi_5_32 with my_dissolve
    "Sabrina" "Fuck."
    "Sabrina" "Don't let him hurt you like that, Sabrina. Come on. Pull yourself together."
    "Sabrina" "Well... That was awkward. Thank God no one saw me."
    show sc i_Naomi_5_31 with my_dissolve
    "[Name]" "{i}(Your secret dies with me, Miss Spellman){/i}"
    "[Name]" "{i}(I'm stuck here forever...){/i}"
    scene expression '#000' with Dissolve(1)

    $ renpy.pause(1)



    scene sc i_Naomi_5_39 with Dissolve(.5)
    "[Name]" "{i}(My whole body is stiff. It's been hours.){/i}"
    "[Name]" "{i}(It never ends...){/i}"
    show sc i_Naomi_5_37 with my_dissolve
    "[Name]" "{i}(Is she leaving?){/i}"
    "[Name]" "{i}(At last.){/i}"
    "[Name]" "{i}(I can't believe I went unnoticed!){/i}"
    show sc i_Naomi_5_38 with my_dissolve
    "[Name]" "{i}(Good night, Miss Spellman.){/i}"
    "[Name]" "{i}(Well... Now...){/i}"
    show sc i_Naomi_5_36 with my_dissolve
    "[Name]" "{i}(To freedom!){/i}"
    "[Name]" "{i}(Agent [Surname] is coming out.){/i}"
    return
label Naomi_6_label:

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

    show sc i_Naomi_1_1 with Dissolve(.5)
    "Naomi" "Did you get it?"
    "[Name]" "Yeah, I got the picture."
    "Naomi" "Did it go well?"
    show sc i_Naomi_1_3 with my_dissolve
    "[Name]" "Smooth sailing?!"
    "[Name]" "It would've gone smoothly if someone had followed the plan."
    "Naomi" "What happened?"
    show sc i_Naomi_1_26 with my_dissolve
    "[Name]" "Wasn't it your idea to distract Sabrina."
    "Naomi" "Yeah, so? I did."
    "[Name]" "For how long?"
    show sc i_Naomi_1_24 with my_dissolve
    "Naomi" "I don't know, a few minutes? Why?"
    "[Name]" "Because she came back earlier than you said she would!"
    "[Name]" "I was stuck in class for hours because of it!"
    "[Name]" "I almost got caught."
    show sc i_Naomi_1_5 with my_dissolve
    "Naomi" "You poor thing."
    show sc i_Naomi_1_17 with my_dissolve
    "Naomi" "Maybe you're a Leonheartian after all, since a little thing like that held you up?"
    "Naomi" "A thing like that would be nothing for an Adderinian."
    show sc i_Naomi_1_22 with my_dissolve

    "[Name]" "{i}(Naomi, were you trying to set me up on purpose?){/i}"
    "[Name]" "{i}(Or do you just not know how to apologize?){/i}"
    "[Name]" "{i}(Either way, you obviously think you've put me in my place...){/i}"
    show sc i_Naomi_1_19 with my_dissolve
    "[Name]" "That's it."
    "[Name]" "Ah-ha-ha-ha."
    show sc i_Naomi_1_14 with my_dissolve
    "Naomi" "What's so funny?"
    "[Name]" "It's funny what you were willing to go through for those pictures."
    "[Name]" "And the way you're talking now."
    show sc i_Naomi_1_12 with my_dissolve
    "Naomi" "Just a little friendly lesson."
    "Naomi" "Adderins always get their way."
    "[Name]" "Yeah, maybe."
    "[Name]" "One question:"
    "[Name]" "I'm not from Crowhive myself, but..."
    show sc i_Naomi_1_9 with my_dissolve
    "[Name]" "Shouldn't you have gotten the photo before you sassed me?"
    "Naomi" "..."
    show sc i_Naomi_1_5 with my_dissolve
    "Naomi" "Shit!{w} I didn't think of that!"
    "Naomi" "A-ha-ha-ha"
    "Naomi" "What a shame."
    show sc i_Naomi_1_20 with my_dissolve
    "Naomi" "What a fool I am, gosh."
    "Naomi" "Go ahead, laugh at me."
    "Naomi" "I deserve it."
    "[Name]" "I don't feel like it."
    show sc i_Naomi_1_4 with my_dissolve
    "Naomi" "I don't need your pity."
    "Naomi" "I deserve to be mocked..."
    "[Name]" "{i}(No way. It's bad sportsmanship to kick someone when they're down.){/i}"
    show sc i_Naomi_1_3 with my_dissolve
    "[Name]" "Oh, come on."
    "[Name]" "Besides, I have other plans for you."

    "Naomi" "You sound like some kind of psycho..."
    "[Name]" "You're not the first person to say that."
    "[Name]" "I'll give you the answers to the test tonight."
    "[Name]" "After a date with me."
    show sc i_Naomi_1_25 with my_dissolve
    "Naomi" "Definitely a psycho..."
    "[Name]" "Do we have a deal?"
    "Naomi" "One date and we're even?"
    "[Name]" "You have my word."
    show sc i_Naomi_1_2 with my_dissolve
    "Naomi" "Okay. I'll meet you at the fountain."
    return


label Naomi_1_1_label:
    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)
    show sc i_Naomi_1_6 with Dissolve(.5)
    "[Name]" "Hi there, Naomi!"
    show sc i_Naomi_1_14 with my_dissolve
    "Naomi" "You again?"
    "[Name]" "Sounds like you don't like my company."
    "Naomi" "Well, you're smart."
    show sc i_Naomi_1_12 with my_dissolve
    "Naomi" "Besides, I told you not to bother me before class."
    "[Name]" "So you're in the mood to socialize tonight?"
    show sc i_Naomi_1_4 with my_dissolve
    "Naomi" "I suppose so."
    "[Name]" "Then I' ll see you tonight, baby."
    return


label Naomi_1_2_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)

    show sc i_Naomi_1_9 with Dissolve(.5)
    "[Name]" "Hello, gorgeous!"
    "Naomi" "Hello there."
    "[Name]" "How are you today? Are you in the mood?"
    show sc i_Naomi_1_15 with my_dissolve
    "Naomi" "That depends."
    "[Name]" "Well... To give me an assignment!"
    "[Name]" "To make you stop doubting my worthiness."
    show sc i_Naomi_1_5 with my_dissolve
    "Naomi" "That's it..."
    "Naomi" "I hadn't thought of that yet. Good of you to remind me."
    show sc i_Naomi_1_12 with my_dissolve
    "Naomi" "Let's meet this afternoon. I can't think of anything right now."
    "[Name]" "Okay."
    return
label Naomi_1_3_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)

    show sc i_Naomi_1_5 with Dissolve(.5)
    "[Name]" "Naomi, hi."
    "Naomi" "Hey, handsome."
    "[Name]" "{i}(I could get used to flattery if I didn't know what you were getting at.){/i}"
    "[Name]" "Listen, about your plan..."
    show sc i_Naomi_1_1 with my_dissolve
    "Naomi" "Not here!"
    "Naomi" "What, do you want us to get caught?"
    "Naomi" "Let's discuss it tonight, like we planned."
    "[Name]" "All right."
    return


label Naomi_2_1_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)
    show sc i_Naomi_3_3 with Dissolve(.5)
    "[Name]" "Oh, hello! We know each other, don't we?"
    "Naomi" "Maybe."
    show sc i_Naomi_3_5 with my_dissolve
    "[Name]" "We definitely saw each other before the exam!"
    "[Name]" "You also told me how much you wanted to go to Adderin."
    "Naomi" "I recall."
    show sc i_Naomi_3_7 with my_dissolve
    "Naomi" "Look, I don't have time for any Leonhearts."
    "Naomi" "Go your own way."
    "[Name]" "{i}(And she's pretty sharp...){/i}"
    "[Name]" "{i}(But there's something in it!){i}"
    "[Name]" "{i}(Let's see if I can melt this ice.){/i}"
    return
label Naomi_2_2_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)

    show sc i_Naomi_3_2 with Dissolve(.5)
    "[Name]" "Hi there, Naomi!"
    "[Name]" "So, ready to get to know each other better?"
    show sc i_Naomi_3_7 with my_dissolve
    "Naomi" "I hope not all Leonhearts are such imbeciles..."
    "Naomi" "I told you not to distract me during class."
    "[Name]" "Sorry, I thought that until the lecture started..."
    show sc i_Naomi_3_5 with my_dissolve
    "Naomi" "Never mind. I'll say it again:"
    "Naomi" "I'm getting ready for class, don't interrupt."
    "[Name]" "Done."
    return
label Naomi_2_3_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)

    show sc i_Naomi_3_5 with Dissolve(.5)
    "[Name]" "Yo, beautiful!"
    "Naomi" "[Name], hi!"
    "[Name]" "Listen, about our plan for tonight..."
    show sc i_Naomi_3_7 with my_dissolve
    "Naomi" "Shh! What are you doing?!"
    "Naomi" "They might hear us."
    "Naomi" "Let's talk about it tonight."
    "[Name]" "Okay."
    return
label Naomi_2_4_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)
    show sc i_Naomi_3_5 with Dissolve(.5)
    "[Name]" "Naomi, there you are!"
    "Naomi" "[Name]!"
    "[Name]" "I need to talk to you about something."
    "[Name]" "I think you know what I mean."
    show sc i_Naomi_3_7 with my_dissolve
    "Naomi" "Of course I do... But definitely not here!"
    "Naomi" "Not in front of Sabrina."
    "Naomi" "Meet you in the morning before class?"
    "[Name]" "{i}(sighs){/i} Okay."
    return
label Naomi_3_1_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)
    show sc i_Naomi_2_1 with Dissolve(.5)
    "[Name]" "Hey, girls!"
    "Naomi" "Yo."
    "Lily " "Hi."
    show sc i_Naomi_2_3 with my_dissolve
    "[Name]" "You're Naomi, right? I wanted to talk to you."
    "Naomi" "Can't you see I'm already talking?"
    "[Name]" "Well, I was just..."
    show sc i_Naomi_2_2 with my_dissolve
    "Naomi" "Walking by."
    "Naomi" "So walk on by."
    "[Name]" "{i}(Hmm. Why is she so rude?){/i}"
    "[Name]" "{i}(She's gonna need a little pick-me-up.){/i}"
    "[Name]" "{i}(And it' s better to do it in private...){/i}"
    return
label Naomi_3_2_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)

    show sc i_Lily_2_7 with Dissolve(.5)
    "[Name]" "Hello, girls!"
    "Lily" "Hi!"
    "Naomi" "Yo."
    "[Name]" "So, Naomi, did you come up with a worthy assignment for me?"
    show sc i_Naomi_2_2 with my_dissolve
    "Naomi" "What do you mean?"
    "[Name]" "Well, that thing we talked about last time..."
    "Naomi" "Oh, that."
    "Naomi" "I haven't thought about it yet."
    show sc i_Naomi_2_3 with my_dissolve
    "Naomi" "Why don't we talk about it this afternoon?"
    "Naomi" "It's late and I'm busy."
    "[Name]" "All right."
    return
label Naomi_3_3_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)
    show sc i_Naomi_2_1 with Dissolve(.5)
    "[Name]" "Naomi, there you are!"
    "[Name]" "I got what we talked about."
    "[Name]" "But we need to have a serious talk..."
    show sc i_Naomi_2_3 with my_dissolve
    "[Name]" "I think you know what I mean."
    "Naomi" "Of course I do... But not now."
    "Naomi" "I'm busy right now."
    show sc i_Naomi_2_2 with my_dissolve
    "Naomi" "Let's talk tomorrow morning. In private."
    "[Name]" "Of course. I understand."
    "[Name]" "Okay."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label Naomi_7_label:


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
    show sc i_Naomi_2_1 with my_dissolve
    "[Name]" "Hi, girls!"
    show sc i_Naomi_2_2 with my_dissolve
    "[Name]" "Naomi. I thought we'll be alone."
    "Naomi" "Yeah, right. We were just chatting."
    show sc i_Naomi_2_5 with my_dissolve
    "Lily" "It was nice to see you, I'll go do my homework."
    "Naomi" "Good luck, Lily!"
    show sc i_Naomi_2_6 with my_dissolve
    "Naomi" "So, where are test asnwers? "
    "[Name]" "I have them."
    show sc i_Naomi_2_9 with my_dissolve
    "Naomi" "Then what are you waiting for?"
    "[Name]" "Having a memory loss, Naomi?"
    "[Name]" "Have you forgotten how you treated me?"
    show sc i_Naomi_7_1 with my_dissolve
    "Naomi" "[Name], come on, what are you talking about..."
    "Naomi" "I was just having some fun."
    "Naomi" "Can't you take a joke?"
    show sc i_Naomi_7_2 with my_dissolve
    "[Name]" "I don't know. "
    "[Name]" "Maybe house Leonheart is too pathetic to know how to take jokes."
    "Naomi" "Come on, baby...{w} I really need those results..."
    show sc i_Naomi_7_3 with my_dissolve
    "[Name]" "Well, than you'll have to make it up to me."
    "Naomi" "How do I do that?"
    "[Name]" "{i}(Maybe we should go somewhere more quiet... ){/i}"
    show sc i_Naomi_7_4 with my_dissolve
    "[Name]" "I'll tell you. But first... Let's go to the library?"
    "Naomi" "Wha's fun about that?"
    show sc i_Naomi_7_5 with my_dissolve
    "[Name]" "Do you want your answers, or do you not?!"
    "Naomi" "Argh...{w} Alright! Let's go to your stupid library."
    show sc i_Naomi_7_6 with my_dissolve
    "Naomi" "I hope your not going to read some stupid poems to impress me."
    "[Name]" "{i}(I can't believe how she still tries to play cool.){/i}"
    "[Name]" "{i}(Even when we both know I have what she needs.){/i}"
    "[Name]" "{i}(The question is - how far is she willing to go in her begging...){/i}"
    show sc i_Naomi_7_7 with my_dissolve
    "[Name]" "Don't worry, I have something else in mind."
    "[Name]" "Let's go."

    return

label Naomi_8_label:


    show sc i_Naomi_8_1 with my_dissolve
    "[Name]" "{i}(Just as I thought, there's not a soul here.){/i}"
    "[Name]" "{i}(Let's see how much she needs those test answers...){/i}"
    show sc i_Naomi_8_2 with my_dissolve
    "Naomi" "I can't believe I went to the library tonight."
    "Naomi" "I hope no one saw us come in here."
    "[Name]" "Come on! It's pretty atmospheric, isn't it?"
    show sc i_Naomi_8_3 with my_dissolve
    "Naomi" "You're kidding, right?"
    "Naomi" "Or are you talking about an atmosphere of boredom and gloom?"
    "Naomi" "Why did you bring me here in the first place?"
    show sc i_Naomi_8_4 with my_dissolve
    "Naomi" "Couldn't we talk there?"
    "[Name]" "{i}(That's okay, I'll cheer you up...){/i}"
    "[Name]" "Trust me, being stuck in Sabrina's class under a desk isn't much fun either."
    "Naomi" "I get it. Honey, I'm really sorry for that."
    show sc i_Naomi_8_5 with my_dissolve
    "Naomi" "Let's just leave it at that, okay?"
    "Naomi" "Just give me the answers to the test..."
    "Naomi" "And I'll figure out a way to make it up to you..."
    show sc i_Naomi_8_6 with my_dissolve
    "[Name]" "Don't worry about it, baby."
    "[Name]" "I already figured it out."
    show sc i_Naomi_8_7 with my_dissolve
    "Naomi" "Why don't you give me the results first..."
    "Naomi" "You know, so I don't forget later, in a fit of passion..."
    "[Name]" "Nice try!"
    show sc i_Naomi_8_8 with my_dissolve
    "[Name]" "But you underestimate me."
    "[Name]" "Honestly, this demeaning attitude is even getting annoying."
    "Naomi" "[Name]..."
    "[Name]" "You are so sure of Aderin's superiority over the others."
    show sc i_Naomi_8_9 with my_dissolve
    "[Name]" "That even when you fail, you try to manipulate me."
    "Naomi" "You're taking this too seriously..."
    show sc i_Naomi_8_10 with my_dissolve
    "Naomi" "I was just messing with you."
    "Naomi" "It's a healthy relationship between our houses."
    "Naomi" "If you came from a magical society, you'd understand that..."
    show sc i_Naomi_8_11 with my_dissolve
    "[Name]" "Too bad I'm not your kind."
    "[Name]" "But there are some things I understand perfectly."
    "[Name]" "Like the fact that you need the answers to this test."
    show sc i_Naomi_8_12 with my_dissolve
    "Naomi" "And what do I have to do to get them?"
    menu:
        "Answer gently":
            "[Name]" "Well, you know..."
            "[Name]" "I was looking for a hiding place for a reason."
            show sc i_Naomi_8_13 with my_dissolve
            "Naomi" "What are you implying?"
            "[Name]" "You wanted to make amends, didn't you?"
            "[Name]" "I suggest we continue what you started back in Potions class."
            show sc i_Naomi_8_14 with my_dissolve
            "Naomi" "[Name], I..."
            "[Name]" "You can leave whenever you want..."
            "[Name]" "But we both know that you want what I want..."
            show sc i_Naomi_8_15 with my_dissolve
            "Naomi" "Don't think you know me, [Name]."
            show sc i_Naomi_8_16 with my_dissolve
            "[Name]" "You shouldn't waste time talking, Ameliе could be back any minute."
            "[Name]" "Better hurry if you want the answers to the test."
            show sc i_Naomi_8_15 with my_dissolve
            "Naomi" "What do I do?"
            "[Name]" "Get on your knees..."
        "Answer stricktly":
            show sc i_Naomi_8_17 with my_dissolve
            "[Name]" "Whatever I tell you to do."
            "Naomi" "What's on your mind?"
            show sc i_Naomi_8_18 with my_dissolve
            "[Name]" "You know what's on my mind..."
            "Naomi" "Come on, [Name], I..."
            show sc i_Naomi_8_19 with my_dissolve
            "[Name]" "You're the one who started it when you teased me in Potions class."
            show sc i_Naomi_8_20 with my_dissolve
            "[Name]" "Ready to thank your hero?"
            "Naomi" "Oh... Ah..."
            show sc i_Naomi_8_21 with my_dissolve
            "Naomi" "I didn't expect you to be so determined."
            "[Name]" "You always look down at me, Naomi."
            show sc i_Naomi_8_22 with my_dissolve
            "[Name]" "I think it's time for a change of perspective."
            "[Name]" "Get down on your knees!"

    scene image '#000' with Dissolve(.5)
    scene sc i_Naomi_8_23 with Dissolve(.5)
    "[Name]" "I like that look a lot better."
    "[Name]" "You have such a pretty face."
    "Naomi" "Thank you, uh..."
    show sc i_Naomi_8_24 with my_dissolve
    "[Name]" "Go ahead, baby."
    "Naomi" "O-okay..."
    show sc i_Naomi_8_25 with my_dissolve
    "Naomi" "I can't believe..."
    show sc i_Naomi_8_26 with my_dissolve
    "Naomi" "He's so tense even through his pants."
    "[Name]" "Get ready for more surprises!"
    "Naomi" "Let's see, [Name]..."
    show sc i_Naomi_8_27 with my_dissolve
    "Naomi" "..."
    "[Name]" "Oops!"
    "[Name]" "My cock looks good with you, Naomi."
    show sc i_Naomi_8_28 with my_dissolve
    "Naomi" "Impressive size..."
    "[Name]" "It's perfect for your sexy lips. Try it."
    show sc i_Naomi_8_29 with my_dissolve
    "Naomi" "You mean..."
    show sc i_Naomi_8_30 with my_dissolve
    "Naomi" "Like this?"
    "[Name]" "Oh, yeah..."
    "[Name]" "Go on..."
    show sc i_Naomi_8_anim_1_a with my_dissolve
    "[Name]" "I want to see you try it."
    show sc i_Naomi_8_anim_1 with my_dissolve
    "[Name]" "Oh yes..."
    "[Name]" "Do you like it?"
    show sc i_Naomi_8_anim_2 with my_dissolve
    "Naomi" "Mhmh...."
    "[Name]" "Don't get distracted."
    show sc i_Naomi_8_anim_3 with my_dissolve
    "[Name]" "Work with your tongue too, honey."
    "[Name]" "Oh,yeah... That's it!"
    show sc i_Naomi_8_31 with my_dissolve
    "[Name]" "Wait..."
    "[Name]" "Before we continue, let's free your magnificent breasts."
    "[Name]" "From the extra rags..."
    scene image '#000' with Dissolve(.5)
    scene sc i_Naomi_8_32_2 with Dissolve(.5)
    "Naomi" "Whatever you say."
    "Naomi" "If it comforts you and makes it up to me."
    show sc i_Naomi_8_32_3 with my_dissolve
    "Naomi" "Look."
    "Naomi" "You'll never see tits like that again in your life."
    "[Name]" "{i}(Still thinks she's the queen of the world.){/i}"
    show sc i_Naomi_8_32 with my_dissolve
    "[Name]" "{i}(That doesn't stop her from sucking me.){/i}"
    "[Name]" "Fine. Get back to work."
    show sc i_Naomi_8_anim_4_a with my_dissolve
    "Naomi" "Mhmh...."
    show sc i_Naomi_8_anim_4 with my_dissolve
    "[Name]" "Oh yeah..."
    "[Name]" "Keep going..."
    show sc i_Naomi_8_anim_5 with my_dissolve
    "[Name]" "There you go."
    "[Name]" "{i}(She seems to be getting a taste for it.){/i}"
    show sc i_Naomi_8_anim_6 with my_dissolve
    "[Name]" "{i}(I'll bet she's getting wet right now!){/i}"
    "[Name]" "Oh yeah..."
    show sc i_Naomi_8_33 with my_dissolve
    "[Name]" "I want you..."
    "Naomi" "That's... That wasn't the deal..."
    #show sc i_Naomi_8_34 with my_dissolve
    show sc i_Naomi_8_35 with my_dissolve
    "[Name]" "Forget the deal."
    "[Name]" "What do you really want, Naomi?"
    "Naomi" "I..."
    "[Name]" "Come on..."
    show sc i_Naomi_8_36 with my_dissolve
    "Naomi" "I want you,too..."
    "Naomi" "But first,I want you to lick me..."
    menu:
        "Agree for cunnilingus":
            "[Name]" "{i}(After that you won't be able to hold back any longer...){/i}"
            show sc i_Naomi_8_37 with my_dissolve
            "[Name]" "With pleasure..."
            "[Name]" "{i}(Oh, she seems very happy about this decision.){/i}"
            show sc i_Naomi_8_38 with my_dissolve
            "Naomi" "Wait a second..."
            "Naomi" "Not many people get a chance to see my body."
            show sc i_Naomi_8_39 with my_dissolve
            "[Name]" "That makes me special."
            "Naomi" "That's right, baby"
            show sc i_Naomi_8_40 with my_dissolve
            "Naomi" "You know I could have said no."
            "Naomi" "I came here of my own free will."
            show sc i_Naomi_8_41 with my_dissolve
            "[Name]" "You did?"
            "Naomi" "Of course you did."
            show sc i_Naomi_8_42 with my_dissolve
            "Naomi" "Look who's in front of you."
            "Naomi" "You hit the jackpot, [Name]."
            show sc i_Naomi_8_43_2 with my_dissolve
            "Naomi" "But don't get cocky, thinking you've earned it."
            "[Name]" "{i}(Strong move, Naomi.){/i}"
            "[Name]" "{i}(But you're where I want you now. Naked and ready for anything.){/i}"
            show sc i_Naomi_8_43 with my_dissolve
            "[Name]" "{i}(And I can see all your virtues.){/i}"
            "[Name]" "{i}(What an incredible beauty...){/i}"
            show sc i_Naomi_8_43_3 with my_dissolve
            "Naomi" "Admit it, you want to touch that sexy body..."
            "[Name]" "Oh yes..."
            show sc i_Naomi_8_44 with my_dissolve
            "Naomi" "Taste what winning women are made of..."
            "Naomi" "Come to me..."
            show sc i_Naomi_8_45 with my_dissolve
            "[Name]" "{i}(How passionately she looks at me.){/i}"
            "[Name]" "{i}(As if I were her prey.){/i}"
            show sc i_Naomi_8_46 with my_dissolve
            "[Name]" "{i}(It's time to taste you, Naomi.){/i}"
            "[Name]" "Get ready to feel yourself in heaven of pleasure, baby."
            "Naomi" "Oh..."
            show sc i_Naomi_8_47 with my_dissolve
            "Naomi" "Oh yes..."
            "Naomi" "Caress me."
            show sc i_Naomi_8_48 with my_dissolve
            "[Name]" "{i}(She's so eager and trembling with passion.){/i}"
            "[Name]" "{i}(She barely restrains herself from cumming at the first touch.){/i}"
            show sc i_Naomi_8_49 with my_dissolve
            "[Name]" "{i}(It's okay, baby, I'll caress you all over.){/i}"
            "Naomi" "Oh, yes..."
            show sc i_Naomi_8_50 with my_dissolve
            "Naomi" "Oh, God..."
            "[Name]" "{i}(And there's no trace of your power...){/i}"
            show sc i_Naomi_8_51 with my_dissolve
            "[Name]" "{i}(How fortunate that the library is empty at night.){/i}"
            "[Name]" "{i}(Where else could we have such privacy?){/i}"
            show sc i_Naomi_8_52 with my_dissolve
            "Naomi" "I'm trembling all over..."
            "[Name]" "{i}(Okay, I won't tease her any further.){/i}"
            "[Name]" "Are you ready?"
            show sc i_Naomi_8_53 with my_dissolve
            "Naomi" "Yes..."
            "Naomi" "Yes... Yes... Yes..."
            show sc i_Naomi_8_54 with my_dissolve
            "Naomi" "It's unbelievable."
            "Naomi" "This is so good!"
            show sc i_Naomi_8_55 with my_dissolve
            "[Name]" "{i}(I think I'm good at everything sexually.){/i}"
            "Naomi" "Oh yeah..."
            "Naomi" "Oh..."
            show sc i_Naomi_8_56 with my_dissolve
            "Naomi" "Ah... Oh yeah..."
            "Naomi" "Yes... That's it."
            show sc i_Naomi_8_56_2 with my_dissolve
            "[Name]" "You like that?"
            "Naomi" "Don't stop..."
            show sc i_Naomi_8_57 with my_dissolve
            "Naomi" "You have a magic tongue..."
            "Naomi" "Ah... Oh yes..."
            show sc i_Naomi_8_58 with my_dissolve
            "Naomi" "OH YES!"
            "Naomi" "Oh my god...."
            show sc i_Naomi_8_59 with my_dissolve
            "[Name]" "{i}(There you go!){/i}"
            scene sc i_Naomi_8_anim_7 with Dissolve(.5)
            "Naomi" "Unbelievable..."
            scene sc i_Naomi_8_anim_8 with Dissolve(.5)
            
            "Naomi" "[Name], I didn't expect..."
            scene sc i_Naomi_8_anim_9 with Dissolve(.5)
            "[Name]" "So, are you ready now?"
        "Go straight to sex":
            show sc i_Naomi_8_60 with my_dissolve
            "[Name]" "{i}(Who does she think I am?){/i}"
            "[Name]" "Have you forgotten who's paying your debts here?"
            "[Name]" "Take off your clothes and get up to the table!"
            show sc i_Naomi_8_38 with my_dissolve
            "Naomi" "All right, all right, cowboy! Take it easy."
            "Naomi" "I'm just teasing you."
            show sc i_Naomi_8_39 with my_dissolve
            "[Name]" "What are you trying to do, bring out the beast in me?"
            "Naomi" "What beast in you? A kitten?"
            show sc i_Naomi_8_40 with my_dissolve
            "[Name]" "I think you're asking for tough."
            "Naomi" "You think you can be tough?"
            "Naomi" "Surprise me!"
            show sc i_Naomi_8_41 with my_dissolve
            "[Name]" "{i}(Is she challenging me?){/i}"
            "Naomi" "Or are you scared?"
            "[Name]" "Who, me?"
            show sc i_Naomi_8_42 with my_dissolve
            "[Name]" "Turn around and get comfortable, baby."

    scene image '#000' with Dissolve(.5)
    scene sc i_Naomi_8_47 with Dissolve(.5)
    "[Name]" "I want to see your back."
    "Naomi" "Now..."
    show sc i_Naomi_8_61 with my_dissolve
    "[Name]" "Your hair is so gorgeous."
    "[Name]" "I want to see it when I enter you."
    show sc i_Naomi_8_62 with my_dissolve
    "Naomi" "I'm ready to take you in."
    "[Name]" "I know you can't take it anymore."
    "Naomi" "Yes... Take me!"
    show sc i_Naomi_8_52 with my_dissolve
    "[Name]" "{i}(I have nowhere to hurry, you're all mine.){/i}"
    "[Name]" "{i}(I can feel how much you want cock.){/i}"
    show sc i_Naomi_8_63 with my_dissolve
    "Naomi" "Please, come inside me..."
    "[Name]" "{i}(I can feel how badly you want it.) {/i}"
    "Naomi" "Come on, what are you waiting for?"
    show sc i_Naomi_8_56 with my_dissolve
    "[Name]" "I want to enjoy this moment, baby."
    "[Name]" "{i}(And make you long for me to come in.){/i}"
    "Naomi" "I'm all yours..."
    show sc i_Naomi_8_56_2 with my_dissolve
    "[Name]" "You are? What am I supposed to do with you?"
    "Naomi" "Take me!"
    "[Name]" "Do you like it?"
    "[Name]" "Do you like feeling the throbbing of my cock with your buttocks?"
    show sc i_Naomi_8_64 with my_dissolve
    "[Name]" "{i}(I can feel her wiggle.){/i}"
    "[Name]" "{i}(And she's begging with her whole look.){/i}"
    "Naomi" "I... I can't wait any longer."
    show sc i_Naomi_8_65 with my_dissolve
    "[Name]" "Be patient."
    "[Name]" "The longer you endure, the more enjoyable you'll be."
    show sc i_Naomi_8_59 with my_dissolve
    "Naomi" "I'm already on fire... [Name], please."
    "[Name]" "{i}(I'm already barely holding back myself.){/i}"
    scene sc i_Naomi_8_anim_7 with Dissolve(.5)
    "[Name]" "{i}(It's time to enter her.){/i}"
    scene sc i_Naomi_8_anim_8 with Dissolve(.5)
    "[Name]" "{i}(And fuck her good.){/i}"
    scene sc i_Naomi_8_anim_9 with Dissolve(.5)
    "Amelie" "Mm-hmm. ...."
    "[Name]" "So, are you ready?"
    show sc i_Naomi_8_66 with my_dissolve
    "Naomi" "Oh,yeah..."
    "Naomi" "Ready as I'll ever be."
    show sc i_Naomi_8_67 with my_dissolve
    "Amelie" "Mm-hmm....."
    "Amelie" "oh..."
    show sc i_Naomi_8_68 with my_dissolve
    "[Name]" "What the...?!"
    show sc i_Naomi_8_69 with my_dissolve
    "Naomi" "Did you hear that?"
    "[Name]" "Yeah."
    "Naomi" "Is someone there?"
    show sc i_Naomi_8_69_2 with my_dissolve
    "[Name]" "I don't see anyone."
    "[Name]" "Shit..."
    "Naomi" "Damn, [Name], that was a terrible idea!"
    show sc i_Naomi_8_69_3 with my_dissolve
    "[Name]" "Maybe we were just imagining things."
    "Naomi" "Imagining things?! Are you kidding me?"
    "[Name]" "All right, let's get out of here."
    show sc i_Naomi_8_69_4 with my_dissolve
    "[Name]" "{i}(Damn, I hope we don't get expelled for this.){/i}"
    "[Name]" "{i}(Whoever caught us didn't want to show his face.){/i}"
    "Naomi" "Let's run!"
    scene image '#000' with Dissolve(.5)
    scene sc i_Naomi_8_70 with my_dissolve
    "[Name]" "Oh... Wow."
    "[Name]" "Yeah, that was something."
    "Naomi" "Something? We almost got caught!"
    "Naomi" "I gotta get dressed."
    show sc i_Naomi_8_71 with my_dissolve
    "[Name]" "{i}(Naomi looks even prettier in the moonlight.){/i}"
    "[Name]" "{i}(I wish we could've had sex.){/i}"
    show sc i_Naomi_8_72 with my_dissolve
    "Naomi" "You shouldn't have taken so long, [Name]."
    "[Name]" "Huh... Who knew?"
    "[Name]" "I just wanted to play with you."
    show sc i_Naomi_8_73 with my_dissolve
    "Naomi" "Yeah..."
    "Naomi" "What a game you're playing, [Name]."
    "[Name]" "Huh..."
    scene image '#000' with Dissolve(.5)
    scene sc i_Naomi_8_74 with Dissolve(.5)
    "Naomi" "Aha-ha-ha..."
    "Naomi" "I can't believe we almost got caught naked in the library!"
    "[Name]" "Told you it would be fun..."
    "Naomi" "Yeah..."
    show sc i_Naomi_8_75 with my_dissolve
    "Naomi" "So, can I get my answers?"
    "[Name]" "I don't know."
    "[Name]" "We never got to the end of it, did we?"
    "Naomi" "Come on, [Name], you got more than you should have."
    "[Name]" "All right, well..."
    show sc i_Naomi_8_76 with my_dissolve
    "[Name]" "But I  think we both don't mind continuing this adventure..."
    "[Name]" "What do you say?"
    show sc i_Naomi_8_77 with my_dissolve
    "Naomi" "Maybe another time."
    "[Name]" "Don't I even deserve..."
    show sc i_Naomi_8_78 with my_dissolve
    "[Name]" "{i}(Whoa...){/i}"
    "Naomi" "A goodbye kiss?"
    show sc i_Naomi_8_79 with my_dissolve
    "Naomi" "I guess you do."
    "Naomi" "Good night, [Name]."
    "[Name]" "Good night, Naomi!"
    return
