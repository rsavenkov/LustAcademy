



label haley_events_label:

    call hide_all_main_interfaces from _call_hide_all_main_interfaces_1
    $ set_now = haley_events_set

    menu:

        "0 Talk to Haley" if Q_Haley == 0:


            call Haley_1_label from _call_Haley_1_label
            $ p_up('Haley', 2)

            $ log_message.update({"QLOG_Haley":2 })
            $ Q_Haley=1
            $ haley_view_3 = True
            $ haley_events_set.append("1 Talk to Haley")
            $ wakeup_sets.append([

            
            haley_events_set, "1 Talk to Haley"
            
            
                ])
        "1 Talk to Haley" if Q_Haley == 1:

            call Haley_1_1_label from _call_Haley_1_1_label
            $ haley_events_set.append("1 Talk to Haley")
            $ wakeup_sets.append([

            
            haley_events_set, "1 Talk to Haley"
            
            
                ])

        "3 Talk to Haley" if Q_Haley == 3:

            call Haley_4_label from _call_Haley_4_label
            show expression '#000' with Dissolve(.5)
            call Haley_5_label from _call_Haley_5_label
            show expression '#000' with Dissolve(.5)
            call Haley_6_label from _call_Haley_6_label
            $ p_up('Haley', 4)
            $ log_message.update({"QLOG_Haley":5 })
            $ Q_Haley=6
        "10 Talk to Haley" if Q_Haley == 10:
            call Haley_11_label from _call_Haley_11_label
            $ log_message.update({"QLOG_Haley":8})
            $ Q_Haley=11
            $ p_up('Haley', 7)
            $ change_location('cord_garden_l')
        
        "Not now" if True:

            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label



label haley_events_2_label:
    call hide_all_main_interfaces from _call_hide_all_main_interfaces_2

    $ set_now = haley_events_set_2
    menu:

        "0 Talk to Haley" if Q_Haley == 0:

            call Haley_2_1_label from _call_Haley_2_1_label

            $ log_message.update({"QLOG_Haley":1 })

        "1 Talk to Haley" if Q_Haley == 1:


            call Haley_2_2_label from _call_Haley_2_2_label

            $ haley_events_set_2.append("1 Talk to Haley")
            $ wakeup_sets.append([

            
            haley_events_set_2, "1 Talk to Haley"
            
            
                ])
        "3 Talk to Haley" if Q_Haley == 3:

            call Haley_2_3_label from _call_Haley_2_3_label

            $ haley_events_set_2.append("3 Talk to Haley")
            $ wakeup_sets.append([
            haley_events_set_2, "3 Talk to Haley"])
            $ log_message.update({"QLOG_Haley":4})



        "6 Talk to Haley" if Q_Haley == 6:

            call Haley_2_4_label from _call_Haley_2_4_label

            $ haley_events_set_2.append("6 Talk to Haleyy")
        "Not now" if True:




            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label

label haley_events_3_label:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.5)

    $ set_now = haley_events_set_3
    menu:
        "Talk to Haley" if Q_Haley==1:

            call Haley_2_label from _call_Haley_2_label
            scene expression '#000' with Dissolve(.5)
            $ renpy.pause(.5)
            call Haley_3_label from _call_Haley_3_label

            $ Q_Haley=3
            $ p_up('Haley', 3)

            $ log_message.update({"QLOG_Haley":3 })

            $ time_now = 4
            $ change_location('cord_caffe')
            $ haley_view_3 = False
            jump main_interface_label
        "7 Talk to Haley" if Q_Haley == 7:
            call haley_8_label from _call_haley_8_label
            scene image '#000' with Dissolve(.5)
            $ renpy.pause(.5)
            call haley_9_label from _call_haley_9_label
            scene image '#000' with Dissolve(.5)
            $ renpy.pause(.5)
            call haley_10_label from _call_haley_10_label

            $ Q_Haley = 10
            $ p_up('Haley', 7)
            $ log_message.update({"QLOG_Haley":7})
            if hasattr(store, 'ltssttttt'):
                $ del ltssttttt
                $ change_location_2('leon_room_hl', time_now+1)
            else:
                $ change_location_2('cord_garden_l', time_now+1)

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














label Haley_1_label:

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

    show sc i_Haley_1_1 with Dissolve(.5)










    "[Name]" "Haley, hi!"
    "Haley" "[Name], good to see you!"
    "[Name]" "How's it going? {w} Getting ready for class?"
    show sc i_Haley_1_12 with my_dissolve
    "Haley" "Yeah. Have you opened your magic book yet?"
    "Haley" "I'm really excited."
    "[Name]" "I haven't had the chance yet."
    "[Name]" "What's the big deal?"
    "Haley" "What do you mean?!"
    show sc i_Haley_1_17 with my_dissolve
    "Haley" "Everything! It's got everything!"
    "Haley" "All the answers, the history of magic, practical advice."
    "Haley" "It's objectively the best textbook I've ever seen."
    show sc i_Haley_1_18 with my_dissolve
    "Haley" "And I know textbooks, believe me."
    "[Name]" "I believe you."
    "[Name]" "{i}(Although I've never met such a fiery crammer before...){/i}"
    show sc i_Haley_1_15 with my_dissolve
    "Haley" "I also spoke to Ms. Lapis!"
    "Haley" "She agreed to discuss a thesis about the nature of magic."
    "Haley" "After class."
    "[Name]" "An after-class class?{w} Wow!"
    show sc i_Haley_1_17 with my_dissolve
    "Haley" "I'm looking forward to it!"
    "Haley" "This place is just a treasure trove of knowledge."
    "Haley" "I'm so happy!"
    "[Name]" "I'm happy for you."
    "[Name]" "But are you only interested in knowledge?"
    show sc i_Haley_1_13 with my_dissolve
    "Haley" "What do you mean?"
    "Haley" "We're in the academy."
    "[Name]" "So what?"
    "[Name]" "We still have a few more years studying and living within these walls."
    show sc i_Haley_1_12 with my_dissolve
    "Haley" "What's your point?"
    "[Name]" "I'm saying it's worth exploring more than just the library and the classrooms."
    "[Name]" "Have you been to the local cafe yet?"
    show sc i_Haley_1_16 with my_dissolve
    "Haley" "Um... I don't remember."
    "[Name]" "There!"
    "[Name]" "Let's start there."
    show sc i_Haley_1_17 with my_dissolve
    "Haley" "I don't know...{w} I have so much to learn..."
    "Haley" "I'll check my diary."
    "[Name]" "I didn't say today."
    show sc i_Haley_1_15 with my_dissolve
    "Haley" "Then when?"
    "[Name]" "I won't tell you."
    "Haley" "Why not?"
    "[Name]" "You sorely lack spontaneity in your life."
    "[Name]" "So I'm in charge now."
    show sc i_Haley_1_17 with my_dissolve
    "Haley" "But..."
    "[Name]" "Objections will only be accepted via e-mail."
    "[Name]" "I'll pick you up."
    show sc i_Haley_1_4 with my_dissolve
    "Haley" "Wait, wait, wait, wait, wait, wait."
    "Haley" "Let's just make it tonight, okay?"
    "[Name]" "Okay, no problem."
    "[Name]" "Dates are usually at night, right?"
    show sc i_Haley_1_19 with my_dissolve
    "Haley" "Dates?"
    "[Name]" "All right, it's a deal."
    return

label Haley_2_label:


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

    show sc i_Haley_2_1 with Dissolve(.5)
    "[Name]" "{i}(Wow! I can't take my eyes off her...){/i}"
    "[Name]" "Haley!"
    "[Name]" "You look great!"
    show sc i_Haley_2_2 with my_dissolve
    "Haley" "Hi, [Name]. Thank you."
    "Haley" "Shall we go?"
    "[Name]" "What eagerness!"
    "[Name]" "You're in a hurry to get back to your books, aren't you?"
    show sc i_Haley_2_3 with my_dissolve
    "Haley" "Why are you like that?"
    "[Name]" "I didn't mean to offend you. I was just kidding."
    "[Name]" "Your speech about the magic textbook was so passionate..."
    show sc i_Haley_2_4 with my_dissolve
    "Haley" "Stupid!"
    "[Name]" "Heh."
    "[Name]" "Let's hurry up, I'm starving."
    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    scene sc i_Haley_2_5 with Dissolve(.5)
    "Haley" "It's beautiful here!"
    show sc i_Haley_2_6 with my_dissolve
    "[Name]" "It really is.{w} There's something magical about nature."
    "Haley" "Do you think the world will ever be the same for us?"
    show sc i_Haley_2_7 with my_dissolve
    "[Name]" "What do you mean?"
    "Haley" "Well, there's magic all around..."
    "Haley" "Is everything here so saturated with magic?"
    "Haley" "Or have we just learned to feel it around us?"
    show sc i_Haley_2_8 with my_dissolve
    "[Name]" "Hmm. Wait, what's the difference?"
    "Haley" "If it's the latter, then we'll be able to feel the magic around us when we get home."
    "[Name]" "I never really thought about it."
    show sc i_Haley_2_9 with my_dissolve
    "Haley" "Can you imagine how depressing it would be in the summer?"
    "Haley" "To feel all that magic around and not be able to use it..."
    show sc i_Haley_2_10 with my_dissolve
    "[Name]" "Don't worry about it."
    "[Name]" "Summer is still a long way off."
    "[Name]" "You'll get tired of magic and miss the benefits of civilization."
    show sc i_Haley_2_11 with my_dissolve
    "Haley" "You think so?"
    "[Name]" "Of course."
    "[Name]" "Let's get inside. "
    return


label Haley_3_label:


    scene sc i_Haley_3_1 with Dissolve(1)
    "[Name]" "Everything looks so yummy!"
    show sc i_Haley_3_2 with my_dissolve
    "Haley" "Bon appetit!"
    "[Name]" "You, too."
    show sc i_Haley_3_3 with my_dissolve
    "[Name]" "{i}(Hmm, she chews so neatly.){/i}"
    "[Name]" "{i}(Strange... I've never paid attention to the way my companions eat.){/i}"
    "[Name]" "{i}(Maybe I'm staring too hard.){/i}"
    show sc i_Haley_3_4 with my_dissolve
    "Haley" "What?"
    "Haley" "Would you like to try some?"
    "[Name]" "А? What?{w} No, no, thank you."
    show sc i_Haley_3_5 with my_dissolve
    "Haley" "It's just that you were looking so closely..."
    "[Name]" "{i}(She did notice, though!){/i}"
    "[Name]" "I was just thinking.{w} Nevermind."
    show sc i_Haley_3_6 with my_dissolve
    "Haley" "Whatever you say, I don't mind."
    "[Name]" "{i}(Whew... got through that.){/i}"
    show sc i_Haley_3_7 with my_dissolve
    "Haley" "What were you thinking about?"
    "[Name]" "{i}(Dammit!){/i}"
    "[Name]" "About your..."
    menu:
        "About what you've said..." if True:

            "[Name]" "About how you said we'll never be the same again."
            show sc i_Haley_3_8 with my_dissolve
            "Haley" "Ah-ha-ha-ha."
            "[Name]" "What's the big deal?"
            show sc i_Haley_3_9 with my_dissolve
            "Haley" "Shit..."
            "Haley" "I was sure that was one of your jokes!"
            "[Name]" "Why would it be?"
            show sc i_Haley_3_10 with my_dissolve
            "Haley" "Well, it's just that you..."
            "Haley" "I'm sorry, I'll be blunt..."
            "Haley" "You don't strike me as a romantic."
            "[Name]" "What do you mean?"
            "Haley" "We haven't known each other very long, but..."
            "Haley" "You seem like a simpler, more straightforward kind of guy."
            show sc i_Haley_3_11 with my_dissolve
            "Haley" "Not the kind of guy who would sit with a girl in a cafe and think about eternal things."
            "Haley" "I'd be less surprised if you were staring at my chest."
            "[Name]" "You're hurting my feelings."
            "[Name]" "I've been looking at your boobs for a long time!"
            show sc i_Haley_3_12 with my_dissolve
            "Haley" "There! That's what I'm talking about!"
            "[Name]" "I'm a multifaceted person."
            "Haley" "Forget it."
            jump Haley_3_label_mtp_1
        "About your eyes" if True:
            $ pass



    "[Name]" "About your eyes."
    show sc i_Haley_3_13 with my_dissolve
    "Haley" "W-what, excuse me?"
    "[Name]" "I didn't mean to sound creepy..."
    show sc i_Haley_3_14 with my_dissolve
    "[Name]" "It's just, I don't know if it's the magic in the air..."
    "[Name]" "...or if you have really expressive eyes..."
    "[Name]" "I got a little lost in them."
    show sc i_Haley_3_15 with my_dissolve
    "Haley" "[Name]... Are you serious?"
    "Haley" "I'd sooner believe that you're dreaming about my sushi."
    "[Name]" "What?"
    show sc i_Haley_3_16 with my_dissolve
    "Haley" "Well, it's just that you..."
    "Haley" "I'm sorry, I'll be blunt..."
    show sc i_Haley_3_17 with my_dissolve
    "Molly" "Your order."
    menu:
        "Look at Molly's butt" if True:

            $ pass
        "Don't look at Molly's butt" if True:
            jump Haley_3_label_ingore_mollys_ass

    show sc i_Haley_3_17 with my_dissolve
    "[Name]" "Thank you very much."
    "Haley" "Thank you."
    show sc i_Haley_3_33 with my_dissolve
    "[Name]" "{i}(Check this out!){/i}"
    show sc i_Haley_3_30 with my_dissolve
    "[Name]" "{i}(That's the kind of service I like.){/i}"
    "[Name]" "{i}(No wonder Molly gets so many tips.){/i}"
    show sc i_Haley_3_31 with my_dissolve
    "Haley" "Hey, buddy."
    "[Name]" "Oh... I was just..."
    show sc i_Haley_3_32 with my_dissolve
    "Haley" "Proving to me that you weren't joking about being a perv?"
    "[Name]" "Sorry, let's pretend that didn't happen."
label Haley_3_label_ingore_mollys_ass:

    show sc i_Haley_3_18 with my_dissolve
    "[Name]" "You wanted to tell me something..."
    "Haley" "Forget it."
    "[Name]" "No, come on. I'm curious!"
    show sc i_Haley_3_19 with my_dissolve
    "[Name]" "Why don't you believe my compliment is sincere?"
    "Haley" "Well..."
    show sc i_Haley_3_20 with my_dissolve
    "Haley" "You don't strike me as a romantic!"
    "[Name]" "What do you mean?"
    "Haley" "We haven't known each other very long, but..."
    "Haley" "You seem like a simpler, more straightforward kind of guy."
    show sc i_Haley_3_20 with my_dissolve
    "Haley" "Not the kind of guy who would sit with a girl in a café and think about eternal things."
    "Haley" "I'd be less surprised if you were staring at my chest."
    "[Name]" "You're hurting my feelings."
    show sc i_Haley_3_21 with my_dissolve
    "[Name]" "I've been looking at your boobs for a long time!"
    "Haley" "There! That's what I'm talking about!"
    "[Name]" "I'm a multifaceted person."
    "Haley" "Never mind."
label Haley_3_label_mtp_1:

    show sc i_Haley_3_22 with my_dissolve
    "Haley" "Anyway, spit it out!"
    "[Name]" "What do you mean?"
    "Haley" "Tell me why you called me here."
    "[Name]" "What do you mean..."
    show sc i_Haley_3_23 with my_dissolve
    "Haley" "You wanted to talk about something?"
    "Haley" "To talk about the basics of magic?"
    "Haley" "Maybe practice some magic together?"
    show sc i_Haley_3_24 with my_dissolve
    "Haley" "Or were you trying to trick me?"
    "[Name]" "Is it working?"
    "Haley" "I knew it!"
    "[Name]" "I was just kidding!"
    "[Name]" "You're desperately lacking in simple impulses in your life."
    show sc i_Haley_3_25 with my_dissolve
    "[Name]" "I asked you out because I wanted to ask you out."
    "[Name]" "I hardly know anybody here but you."
    "[Name]" "And I thought we had a great time on the train..."
    "Haley" "Yeah, you were a lot of fun."
    show sc i_Haley_3_26 with my_dissolve
    "Haley" "I'm sorry for jumping to the punch line."
    "Haley" "In high school, guys often pretended to be interested in me."
    "Haley" "And in reality, they needed help in school."
    "[Name]" "{i}(And what, no one wanted to get into your pants?){/i}"
    "[Name]" "I'm sorry that you went to school with scumbags."
    "[Name]" "But don't lump everyone together."
    show sc i_Haley_3_27 with my_dissolve
    "[Name]" "Give me a chance and eventually you'll see what I'm really like."
    "[Name]" "There's no other way."
    "Haley" "Hmm. Okay."
    "Haley" "Friends?"
    "[Name]" "Friends. For now."
    "Haley" "For now?!"
    "[Name]" "Who knows what you'll do..."
    "Haley" "Heh, okay."
    show sc i_Haley_3_28 with my_dissolve
    "Haley" "Look, [Name], it was really nice to make a friend, but..."
    "[Name]" "Have we already had a fight?!"
    "Haley" "No, no! I have to finish my individual assignment from Victoria."
    "Haley" "Gotta run!"
    "[Name]" "I get it. It's hard to let go and just stop being a straight-A student."
    "[Name]" "Just do what you think is right."
    show sc i_Haley_3_29 with my_dissolve
    "Haley" "Thank you for a lovely evening."
    "[Name]" "You, too."
    return

label Haley_4_label:

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
    show sc i_Haley_1_7 with Dissolve(.5)
    "[Name]" "Haley!"
    "[Name]" "I knew I'd find you here!"
    show sc i_Haley_1_2 with my_dissolve
    "Haley" "[Name], good to see you!"
    "Haley" "What's up?"
    show sc i_Haley_1_19 with my_dissolve
    "[Name]" "Nothing. I just missed you."
    "[Name]" "What are you doing?"
    show sc i_Haley_1_17 with my_dissolve
    "Haley" "Studying."
    "Haley" "I have an individual test with Miss Victoria after class."
    show sc i_Haley_1_16 with my_dissolve
    "[Name]" "Individual test?!"
    "[Name]" "What the fuck is that?"
    "[Name]" "We're supposed to be studying?"
    show sc i_Haley_1_15 with my_dissolve
    "Haley" "Aha-ha. No, no!"
    show sc i_Haley_1_23 with my_dissolve
    "Haley" "I just wanted to pick up some tutorials on how to do advanced martial arts spells."
    "Haley" "Mostly for the theory, of course."
    "Haley" "But you can't get books like that for a freshman, it's too dangerous."
    show sc i_Haley_1_24 with my_dissolve
    "Haley" "Miss Lapis is willing to make an exception for me."
    "Haley" " If I get full marks on the spell course from the basic textbook."
    show sc i_Haley_1_21 with my_dissolve
    "[Name]" "Oh... Sounds hard."
    show sc i_Haley_1_22 with my_dissolve
    "Haley" "Hard doesn't mean impossible!"
    "[Name]" "Heh. I'll keep that in mind."
    "[Name]" "Okay, I'll get out of your way."
    show sc i_Haley_1_23 with my_dissolve
    "[Name]" "Wait a minute!"
    "Haley" "I have a favor to ask you..."
    show sc i_Haley_1_17 with my_dissolve
    "[Name]" "I'm all ears."
    "Haley" "{b}My potion book was dipped in ink last night{/b} by pixies."
    show sc i_Haley_1_11 with my_dissolve
    "Haley" "I went to the library and left a request for a replacement."
    "Haley" "But Miss Amelie couldn't find the textbook right away."
    "Haley" "So she told me to come in between classes."
    "Haley" "And then Miss Lapis said my practical was after class."
    show sc i_Haley_1_10 with my_dissolve
    "[Name]" "What a busy day you've had this morning."
    "[Name]" "I don't envy you."
    "[Name]" "So what's your request?"
    show sc i_Haley_1_3 with my_dissolve
    "Haley" "I don't have time to pick up my textbook myself before Potions."
    "Haley" "And the library closes after class."
    "Haley" "I didn't know what to do, but then you showed up..."
    show sc i_Haley_1_19 with my_dissolve
    "Haley" "Like a knight on a white horse! Just like in the fairy tales!"
    "[Name]" "Hey, wait a minute!"
    "[Name]" "I haven't agreed to anything yet."
    show sc i_Haley_1_14 with my_dissolve
    "Haley" "Yeah, I know."
    "Haley" "Just daydreaming."
    "Haley" "So, can you pick up the textbook?"
    show sc i_Haley_1_15 with my_dissolve
    "[Name]" "No problem."
    "[Name]" "But you'll owe me one."
    show sc i_Haley_1_12 with my_dissolve
    "Haley" "The knights in fairy tales do good deeds in the name of honor!"
    "[Name]" "I'm just a product of my times and upbringing."
    "Haley" "All right. I'm in your debt."
    show sc i_Haley_1_19 with my_dissolve
    "Haley" "Something tells me I can trust you."
    "[Name]" "{i}(Oh, Hayley... I'll be sure to collect my debt.){/i}"
    "[Name]" "Consider the new textbook already in your bag."

    return


label Haley_5_label:

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
    scene expression '#000'
    with Dissolve(.5)
    $ renpy.pause(.5)
    scene sc i_Haley_5_1 with Dissolve(.5)
    "Amelie" "Hello, Mr... [Surname], am I right?"
    "[Name]" "Yeah, you have a perfect memory!"
    "Amelie" "What can I do for you during school hours? Let me guess..."
    show sc i_Haley_5_2 with my_dissolve
    "[Name]" "I need a textbook..."
    "Amelie" "You need a textbook!"
    "Amelie" "That was too easy."
    show sc i_Haley_5_3 with my_dissolve
    "[Name]" "I'm impressed. What's your secret? Magic?"
    "Amelie" "Experience. There are many spirits and magical beings at the academy."
    show sc i_Haley_5_4 with my_dissolve
    "Amelie" "And many of them don't mind messing around with naive freshmen."
    "[Name]" "{i}(You don't seem to mind fooling around with a naive freshman yourself...){/i}"
    "[Name]" "Hats off to you."
    show sc i_Haley_5_5 with my_dissolve
    "Amelie" "What kind of textbook do you need?"
    "[Name]" "I just came by to pick up Haley Ranger's potions books."
    "[Name]" "She said you knew about it."
    "Amelie" "Yeah, yeah, of course."
    "Amelie" "Helping out your friend?"
    show sc i_Haley_5_6 with my_dissolve
    "Amelie" "That's very nice of you."
    "[Name]" "How could I not?"
    "Amelie" "Just a moment..."
    scene expression '#000' with Dissolve(.5)

    $ renpy.pause(.5)

    scene sc i_Haley_5_7 with Dissolve(.5)

    "[Name]" "{i}(Well, where is she?){/i}"
    "[Name]" "{i}(How long do I hacew to wait?){/i}"
    scene expression '#000' with Dissolve(.5)

    $ renpy.pause(.5)

    scene sc i_Haley_5_8 with Dissolve(.5)
    "[Name]" "Ahem. Ahem."
    "Amelie" "Yes? What can I do for you?"
    show sc i_Haley_5_9 with my_dissolve
    "[Name]" "You went to get me a potions textbook..."
    "Amelie" "Yes? It completely slipped my mind."
    "[Name]" "!!!"
    show sc i_Haley_5_10 with my_dissolve
    "Amelie" "I'm kidding!"
    "Amelie" "You should have seen your face!"
    show sc i_Haley_5_11 with my_dissolve
    "[Name]" "Well, what can I say, you got me."
    show sc i_Haley_5_12 with my_dissolve
    "Amelie" "Here's your textbook. The last one in the warehouse! A rarity."
    "Amelie" "The new batch has been given and the old one was thrown out."
    "Amelie" "Only this one survived, lost on the shelves. Lucky guy!"
    show sc i_Haley_5_13 with my_dissolve
    "[Name]" "Maybe Haley will get lucky, too."
    "Amelie" "You'll tell me about it later."
    "[Name]" "I will. A thousand thanks!"
    "[Name]" "I gotta run before class starts!"
    return


label Haley_6_label:

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
    scene expression '#000'
    with Dissolve(.5)
    $ renpy.pause(.5)
    scene sc i_Haley_6_1 with Dissolve(.5)
    "Haley" "[Name]! You're here!"
    scene sc i_Haley_1_10 with Dissolve(.5)
    "Haley" "Did you get the book?"
    "[Name]" "Of course it did!"
    show sc i_Haley_6_2 with my_dissolve
    "[Name]" "One ancient textbook."
    "[Name]" "Sign for it here, please."
    "Haley" "Whee!"
    show sc i_Haley_6_3 with my_dissolve
    "Haley" "I don't believe it!"
    "[Name]" "Believe it."
    show sc i_Haley_1_17 with my_dissolve
    "Haley" "[Name]! Thank you!"
    "Haley" "Now I'm gonna make it!"
    "Haley" "You don't know how much it means to me!"
    show sc i_Haley_6_4 with my_dissolve
    "[Name]" "I can imagine.{w} You told me right away."
    "[Name]" "Be careful with him."
    "[Name]" "Amelia said all the new textbooks are gone."
    "[Name]" "This one's a rarity!"
    show sc i_Haley_6_5 with my_dissolve
    "Haley" "Ooh... Nice!"
    show sc i_Haley_6_6 with my_dissolve
    "Haley" "Ancient folios turn me on!"
    "[Name]" "Wait....."
    "[Name]" "You're kidding, right?"
    "Haley" "Who knows..."
    show sc i_Haley_6_7 with my_dissolve
    "Haley" "Of course I'm kidding!"
    "Haley" "Thank you so much."
    "Haley" "I owe you one!"
    "[Name]" "Yes, I remember."
    show sc i_Haley_6_8 with my_dissolve
    "Haley" "But now I have to finish learning my spells."
    "Haley" "Otherwise, I won't get them to Victoria after class and it was all for nothing!"
    "[Name]" "Exactly."
    "[Name]" "Well, I won't get in the way!"

    return


label Haley_1_1_label:
    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)

    scene sc i_Haley_1_7 with Dissolve(.5)
    "[Name]" "Yo, what's up?"
    show sc i_Haley_1_2 with my_dissolve
    "Haley" "Hey, [Name]."
    "Haley" "Sorry, I'm busy right now, I'm getting ready for a tutorial."
    show sc i_Haley_1_8 with my_dissolve
    "[Name]" "You're always talking about studying..."
    "[Name]" "When can we talk?"
    "Haley" "I don't know, I'm too busy studying."
    "Haley" "Let's do it tonight when you pick me up."
    show sc i_Haley_1_5 with my_dissolve
    "Haley" "The cafe is on, right?"
    "[Name]" "Sure."
    "[Name]" "It's a deal."
    return


label Haley_2_1_label:

    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)

    scene sc i_Haley_4_1 with Dissolve(.5)
    "[Name]" "Haley, hi!"
    "[Name]" "You got a minute?"
    show sc i_Haley_4_2 with my_dissolve
    "Haley" "[Name]! I'd love to, but..."
    "Haley" "Potions are hard for me, and I can't afford to screw it up."
    "Haley" "So I'm repeating a paragraph right now."
    "Haley" "Let's talk about it some other time."
    show sc i_Haley_4_3 with my_dissolve
    "[Name]" "{i}(She looks pretty nervous before potions.){/i}"
    "[Name]" "{i}(It's better to talk to Haley prior to the basics of magic.){/i}"
    "[Name]" "No problem."

    return


label Haley_2_2_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)

    scene sc i_Haley_4_1 with Dissolve(.5)
    "[Name]" "Hi."
    "Haley" "Oh, [Name]. What are you doing here?"
    "Haley" "We were supposed to go to a cafe tonight."
    "[Name]" "I know, I just wanted to see you."
    show sc i_Haley_4_4 with my_dissolve
    "Haley" "That's really sweet, but we have potions class coming up."
    "Haley" "I have to get ready."
    "Haley" "Pick me up tonight. I'll be waiting."
    "[Name]" "All right, then."

    return



label Haley_2_3_label:

    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)

    scene sc i_Haley_4_5 with Dissolve(.5)
    "[Name]" "Haley, hi, I just noticed..."
    show sc i_Haley_4_6 with my_dissolve
    "Haley" "Sorry, [Name], I can't talk right now."
    "Haley" "Is it an emergency?"
    "[Name]" "No, it's just..."
    show sc i_Haley_4_5 with my_dissolve
    "Haley" "Then we can do it another time, right?"
    "[Name]" "All right."
    "Haley" "I've got a private class until late, so it' better in the morning."
    "[Name]" "Okay."
    return


label Haley_2_4_label:

    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)

    scene sc i_Haley_4_7 with Dissolve(.5)
    "[Name]" "Haley, would you like to go for a walk?"
    "Haley" "Are you out of your mind?"
    "Haley" "The bell's about to ring."
    "[Name]" "So what? We'll take a walk."
    "[Name]" "We don't have to go to class."
    show sc i_Haley_4_6 with my_dissolve
    "Haley" "I don't agree with that thesis. We're here to study."
    "[Name]" "It's amazing how she can be so cute whenever she's nerdy."
    "[Name]" "If you say so."
    return


label haley_events_4_label:
    







    if not hasattr(store, 'Q_NV_Haley'):
        $ Q_NV_Haley = 0
    if persistent.nv is None:
        call hide_all_main_interfaces from _call_hide_all_main_interfaces_9 
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
                        $ renpy.call('haley_events_4_label_0')
                    "Scene 2" if True:

                        $ renpy.call('haley_events_4_label_1')
                    "Scene 3" if True:

                        $ renpy.call('haley_events_4_label_2')
                    "Scene 4" if True:

                        $ renpy.call('haley_events_4_label_3')

                hide screen black_tmp_screen_menu
                show expression '#000'
                with Dissolve(1.5)
                $ renpy.pause(1.5, hard = True)

                if persistent.from_gallery:
                    scene expression '#000' with Dissolve(1)
                    $ renpy.full_restart()


            if Q_NV_Haley:
                hide screen main_interface with Dissolve(.5)
                $ renpy.call('haley_events_4_label_'+str(Q_NV_Haley))

                hide screen black_tmp_screen_menu
                show expression '#000'
                with Dissolve(1.5)
                $ renpy.pause(1.5, hard = True)

                if persistent.from_gallery:
                    scene expression '#000' with Dissolve(1)
                    $ renpy.full_restart()

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
label haley_events_4_label_0:
    $ Q_NV_Haley += 1
    hide screen main_interface 
    scene sc i_Haley_NV_1
    with Dissolve(.5)
    "[Name]" "{i}(Haley looks so peaceful in her sleep.){/i}"
    "[Name]" "{i}(Let's take a closer look at you.){/i}"
    show sc i_Haley_NV_2 with my_dissolve
    "[Name]" "{i}(Sleeping beauty...){/i}"
    "[Name]" "{i}(It's not that cold here, though. Do we really need that blanket?){/i}"
    show sc i_Haley_NV_2 with my_dissolve
    "[Name]" "{i}(So what are you hiding here, Haley...){/i}"
    "[Name]" "{i}(Let's see...){/i}"
    show sc i_Haley_NV_3 with my_dissolve
    "[Name]" "{i}(Oh wow...){/i}"
    "[Name]" "{i}(What a beauty...){/i}"
    "[Name]" "{i}(I'm sure I'm not dreaming?){/i}"
    show sc i_Haley_NV_4 with my_dissolve
    "[Name]" "{i}(Sometimes you're even too gorgeus, Haley...){/i}"
    "[Name]" "{i}(How can I resist you...){/i}"
    "[Name]" "{i}(I wonder what you're wearing underneath...){/i}"
    show sc i_Haley_NV_10 with my_dissolve
    "Haley" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I think she's gonna wake up any minute.){/i}"
    "[Name]" "{i}(Better get out of here.){/i}"

    hide screen black_tmp_screen_menu
    show expression '#000'
    with Dissolve(1.5)

    if persistent.from_gallery:
        scene expression '#000' with Dissolve(1)
        $ renpy.full_restart()

    $ renpy.pause(1.5, hard = True)
    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/33. Romantic.mp3' fadein 2


    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/33. Romantic.mp3' fadein 2
    $ change_location_2('leon_room_mc', time_now+1, sleep = True)
    jump main_interface_label

label haley_events_4_label_1:
    $ Q_NV_Haley += 1
    scene sc i_Haley_NV_1 with Dissolve(.5)
    "[Name]" "{i}(Haley always looks so peaceful in her sleep.){/i}"
    "[Name]" "{i}(Let's take a closer look at you.){/i}"
    show sc i_Haley_NV_2 with my_dissolve
    "[Name]" "{i}(Sleeping beauty...){/i}"
    "[Name]" "{i}(It's not that cold here, though. Do we really need that blanket?){/i}"
    show sc i_Haley_NV_2 with my_dissolve
    "[Name]" "{i}(Still hiding from me under the blanket, Haley?){/i}"
    "[Name]" "{i}(Let's take that off...){/i}"
    show sc i_Haley_NV_3 with my_dissolve
    "[Name]" "{i}(Oh wow...){/i}"
    "[Name]" "{i}(What a beauty...){/i}"
    "[Name]" "{i}(Every time I'm amazed at your beauty.){/i}"
    show sc i_Haley_NV_4 with my_dissolve
    "[Name]" "{i}(Sometimes you're even too gorgeus, Haley...){/i}"
    "[Name]" "{i}(How can I resist you...){/i}"
    "[Name]" "{i}(I wonder what you're wearing underneath today...){/i}"
    show sc i_Haley_NV_3 with my_dissolve
    "[Name]" "{i}(Haley, show me all of yourself...){/i}"
    "[Name]" "{i}(I bet you're not just beautiful on top...){/i}"
    show sc i_Haley_NV_5 with my_dissolve
    "[Name]" "{i}(It exceeds all my expectations.){/i}"
    "[Name]" "{i}(I could look at you forever.){/i}"
    "[Name]" "{i}(But the clock is ticking.){/i}"
    show sc i_Haley_NV_6 with my_dissolve
    "[Name]" "{i}(Is it just me, or are you bored?){/i}"
    "[Name]" "{i}(Let's get to the fun part...){/i}"
    show sc i_Haley_NV_7 with my_dissolve
    "[Name]" "{i}(What do we have here?){/i}"
    "[Name]" "{i}(It's so hard to take your eyes off of them.){/i}"
    "[Name]" "{i}(Especially when you're dressed like that...){/i}"
    "[Name]" "{i}(I wonder what this fabric feels like?){/i}"
    "[Name]" "{i}(Let's take a look at another piece of art...){/i}"
    show sc i_Haley_NV_11 with my_dissolve
    "[Name]" "{i}(Oh, Haley... Let me see your temple.){/i}"
    "[Name]" "{i}(What could be more beautiful?){/i}"
    show sc i_Haley_NV_12 with my_dissolve
    "[Name]" "{i}(And your legs...){/i}"
    "[Name]" "{i}(Your soft skin makes me crazy.){/i}"
    "[Name]" "{i}(What's so playful through your transparent panties?){/i}"
    "[Name]" "{i}(It's tempting to touch...){/i}"
    show sc i_Haley_NV_10 with my_dissolve
    "Haley" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I think she could wake up any minute.){/i}"
    "[Name]" "{i}(Better get out of here.){/i}"
    return

label haley_events_4_label_2:
    $ Q_NV_Haley += 1
    scene sc i_Haley_NV_1 with Dissolve(.5)


    "[Name]" "{i}(Haley always looks so peaceful in her sleep.){/i}"
    "[Name]" "{i}(Let's take a closer look at you.){/i}"
    show sc i_Haley_NV_2 with my_dissolve
    "[Name]" "{i}(Sleeping beauty...){/i}"
    "[Name]" "{i}(It's not that cold here, though.){/i}"
    show sc i_Haley_NV_2 with my_dissolve
    "[Name]" "{i}(Still hiding from me under the blanket, Haley?){/i}"
    "[Name]" "{i}(Let's take that off...){/i}"
    show sc i_Haley_NV_3 with my_dissolve
    "[Name]" "{i}(Oh wow...){/i}"
    "[Name]" "{i}(What a beauty...){/i}"
    "[Name]" "{i}(Every time I'm amazed by you...){/i}"
    show sc i_Haley_NV_4 with my_dissolve
    "[Name]" "{i}(Sometimes you're even too gorgeus, Haley...){/i}"
    "[Name]" "{i}(How can I resist you...){/i}"
    "[Name]" "{i}(I wonder what you're wearing underneath today...){/i}"
    show sc i_Haley_NV_3 with my_dissolve
    "[Name]" "{i}(Haley, show me all of yourself...){/i}"
    "[Name]" "{i}(I know you're not just beautiful on top...){/i}"
    show sc i_Haley_NV_5 with my_dissolve
    "[Name]" "{i}(And every time I see it.){/i}"
    "[Name]" "{i}(I could look at you forever.){/i}"
    "[Name]" "{i}(But the clock is ticking.){/i}"
    show sc i_Haley_NV_6 with my_dissolve
    "[Name]" "{i}(Is it just me, or are you bored?){/i}"
    "[Name]" "{i}(Let's get to the fun part...){/i}"
    "[Name]" "{i}(Where do I start?){/i}"
    show sc i_Haley_NV_7 with my_dissolve
    "[Name]" "{i}(It's so hard to take your eyes off of them.){/i}"
    "[Name]" "{i}(Especially when you're dressed like that...){/i}"
    "[Name]" "{i}(I wonder if the fabric still feels the same?){/i}"
    "[Name]" "{i}(I just have to try it...){/i}"
    show sc i_Haley_NV_8 with my_dissolve
    "[Name]" "{i}(Oh yes...){/i}"
    "[Name]" "{i}(That's a nice fabric!){/i}"
    "[Name]" "{i}(It's so flattering and pleasing to the skin...){/i}"
    "[Name]" "{i}(And underneath, it's... It's magic.){/i}"
    "[Name]" "{i}(Haley, how do you keep such a perfect balance...){/i}"
    "[Name]" "{i}(Between the softness and firmness of your breasts.){/i}"
    "[Name]" "{i}(I have to switch my attention to something else...){/i}"
    "[Name]" "{i}(While I can still control myself.){/i}"
    show sc i_Haley_NV_11 with my_dissolve
    "[Name]" "{i}(Oh, Haley... Let me look at your temple.){/i}"
    "[Name]" "{i}(What could be more beautiful?){/i}"
    show sc i_Haley_NV_12 with my_dissolve
    "[Name]" "{i}(Let me touch your legs...){/i}"
    "[Name]" "{i}(Your soft skin makes me crazy.){/i}"
    "[Name]" "{i}(What's so playful through your transparent panties?){/i}"
    "[Name]" "{i}(It beckons to pull them down...){/i}"
    show sc i_Haley_NV_12 with my_dissolve
    "[Name]" "{i}(Open Sesame!){/i}"
    show sc i_Haley_NV_13 with my_dissolve
    "[Name]" "{i}(Haley... I'm speechless...){/i}"
    "[Name]" "{i}(Your neat little pussy is driving me crazy.){/i}"
    "[Name]" "{i}(Maybe I should make your dream a little spicier.){/i}"
    "[Name]" "{i}(Just one little touch...){/i}"
    show sc i_Haley_NV_10 with my_dissolve
    "Haley" "Mhm... mmm..."
    "[Name]" "{i}(Shit, I think she could wake up any minute.){/i}"
    "[Name]" "{i}(Better get out of here.){/i}"
    return
label haley_events_4_label_4:

label haley_events_4_label_3:

    $ unlock_gallery('images/ero/NV_Haley.png')

    scene sc i_Haley_NV_1 with Dissolve(.5)
    "[Name]" "{i}(Haley always looks so peaceful in her sleep.){/i}"
    "[Name]" "{i}(Let's take a closer look at you.){/i}"
    show sc i_Haley_NV_2 with my_dissolve
    "[Name]" "{i}(Sleeping beauty...){/i}"
    "[Name]" "{i}(It's not that cold here, though. Do we really need that blanket?){/i}"
    show sc i_Haley_NV_2 with my_dissolve
    "[Name]" "{i}(Still hiding from me under the blanket, Haley?){/i}"
    "[Name]" "{i}(Let's take that off...){/i}"
    show sc i_Haley_NV_3 with my_dissolve
    "[Name]" "{i}(Oh wow...){/i}"
    "[Name]" "{i}(What a beauty...){/i}"
    "[Name]" "{i}(Every time I'm amazed by you.){/i}"
    show sc i_Haley_NV_4 with my_dissolve
    "[Name]" "{i}(Sometimes you're even too gorgeus, Haley...){/i}"
    "[Name]" "{i}(How can I resist you...){/i}"
    "[Name]" "{i}(I wonder what you're wearing underneath today...){/i}"
    show sc i_Haley_NV_3 with my_dissolve
    "[Name]" "{i}(Show me all of yourself, Haley...){/i}"
    "[Name]" "{i}(I know you're not just beautiful on top...){/i}"
    show sc i_Haley_NV_5 with my_dissolve
    "[Name]" "{i}(And every time I see it.){/i}"
    "[Name]" "{i}(I could look at you forever.){/i}"
    "[Name]" "{i}(But the clock is ticking.){/i}"
    show sc i_Haley_NV_6 with my_dissolve
    "[Name]" "{i}(Let's get to the fun part...){/i}"
    "[Name]" "{i}(Where do I start?){/i}"
    show sc i_Haley_NV_7 with my_dissolve
    "[Name]" "{i}(It's so hard to take your eyes off of them.){/i}"
    "[Name]" "{i}(Especially when you're dressed like that...){/i}"
    "[Name]" "{i}(I wonder if the fabric still feels the same?){/i}"
    "[Name]" "{i}(I just have to try it...){/i}"
    show sc i_Haley_NV_8 with my_dissolve
    "[Name]" "{i}(Oh yes...){/i}"
    "[Name]" "{i}(That's a nice fabric!){/i}"
    "[Name]" "{i}(It's so flattering and pleasing to the skin...){/i}"
    "[Name]" "{i}(And underneath, it's... It's magic.){/i}"
    "[Name]" "{i}(Haley, how do you keep such a perfect balance...){/i}"
    "[Name]" "{i}(Between the softness and firmness of your breasts.){/i}"
    "[Name]" "{i}(I want to have a better look...){/i}"
    show sc i_Haley_NV_9 with my_dissolve
    "[Name]" "{i}(Did you miss me?){/i}"
    "[Name]" "{i}(Well hello...){/i}"
    "[Name]" "{i}(I wonder if your nipples are sensitive?){/i}"
    "[Name]" "{i}(We'll find out...){/i}"
    "[Name]" "{i}(And now, let's free your breasts of excess tissue...){/i}"
    show sc i_Haley_NV_9 with my_dissolve
    "[Name]" "{i}(Let's pull some strings...){/i}"
    "[Name]" "{i}(Hmm, that's not so easy...){/i}"
    show sc i_Haley_NV_16 with my_dissolve
    "[Name]" "{i}(How gorgeous Haley looks in that lingerie...){/i}"
    "[Name]" "{i}(Too bad it's so hard to get it off without being caught.){/i}"
    "[Name]" "{i}(Maybe I'll have more luck underneath?){/i}"
    show sc i_Haley_NV_11 with my_dissolve
    "[Name]" "{i}(Oh, Haley... Let me see your temple.){/i}"
    "[Name]" "{i}(What could be more beautiful?){/i}"
    show sc i_Haley_NV_12 with my_dissolve
    "[Name]" "{i}(Let me touch your foot...){/i}"
    "[Name]" "{i}(Your soft skin makes me crazy.){/i}"
    "[Name]" "{i}(What's so playful through your transparent panties?){/i}"
    "[Name]" "{i}(It beckons to pull them down...){/i}"
    show sc i_Haley_NV_12 with my_dissolve
    "[Name]" "{i}(Open Sesame!){/i}"
    show sc i_Haley_NV_13 with my_dissolve
    "[Name]" "{i}(Oh yeah...){/i}"
    "[Name]" "{i}(Your neat little pussy always drives me crazy.){/i}"
    "[Name]" "{i}(Maybe I should make your sleep a little spicier.){/i}"
    "[Name]" "{i}(Just one little touch...){/i}"
    show sc i_Haley_NV_14 with my_dissolve
    "[Name]" "{i}(I have contact.){/i}"
    "[Name]" "{i}(I can feel her whole body tense...){/i}"
    "[Name]" "{i}(But it doesn't feel like she's waking up.){/i}"
    show sc i_Haley_NV_anim_1 with my_dissolve
    "[Name]" "{i}(I'll press gently...){/i}"
    "Haley" "Ah..."
    "[Name]" "{i}(She clearly likes it...){/i}"
    show sc i_Haley_NV_anim_2 with my_dissolve
    "[Name]" "{i}(I wonder how far this can go...){/i}"
    "Haley" "Ah... ah..."
    "[Name]" "{i}(This must be your sweetest dream in a long time...){/i}"
    show sc i_Haley_NV_15 with my_dissolve
    "[Name]" "{i}(Push a little harder...){/i}"
    show sc i_Haley_NV_10 with my_dissolve
    "Haley" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I think she might wake up...){/i}"
    "[Name]" "{i}(Better get out of here.){/i}"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
label pre_haley_8_label:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    call haley_8_label from _call_haley_8_label_1
    scene image '#000' with Dissolve(.5)
    $ renpy.pause(.5)
    call haley_9_label from _call_haley_9_label_1
    scene image '#000' with Dissolve(.5)
    $ renpy.pause(.5)
    call haley_10_label from _call_haley_10_label_1
    $ Q_Haley = 10
    $ log_message.update({"QLOG_Haley":7})
    if hasattr(store, 'ltssttttt'):
        $ del ltssttttt
        $ change_location_2('leon_room_hl', time_now+1)
    else:
        $ change_location_2('cord_garden_l', time_now+1)
    show screen main_interface 
    hide screen black_tmp_screen_menu

    with Dissolve(.5)
    jump main_interface_label


label haley_8_label:

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
    scene sc i_Haley_8_1 
    with Dissolve(.5)

    "[Name]" "Haley, hi there!"
    "[Name]" "Am I interrupting?"
    "Haley" "[Name]! Of course not!"
    "Haley" "I've been waiting for you!"
    "[Name]" "{i}(Yeah? That's nice.){/i}"
    "[Name]" "What's the rush?"
    show sc i_Haley_8_2 with my_dissolve
    "Haley" "I can't wait to show you what I found in this textbook..."
    "[Name]" "I'm all ears."
    show sc i_Haley_8_3 with my_dissolve
    "Haley" "Look! See how many markings there are in the margins?"
label haley_8_label_menu:
    show sc i_Haley_8_3 with my_dissolve
    menu:
        "Caricature of Sabrina" if not hasattr(store, 'haley_8_label_menu_1_var'):
            $ haley_8_label_menu_1_var = 1
        "Potion tips" if not hasattr(store, 'haley_8_label_menu_2_var'):
            $ haley_8_label_menu_2_var = 1
            jump haley_8_16
        "Familiar initials" if not hasattr(store, 'haley_8_label_menu_3_var'):
            $ haley_8_label_menu_3_var = 1
            jump haley_8_20
    show sc i_Haley_8_4 with my_dissolve
    "[Name]" "So? It's just scribbling..."
    "[Name]" "Although, I must admit, they're quite sophisticated."
    "Haley" "No, you dummy!"

    jump haley_8_19
label haley_8_16:

    show sc i_Haley_8_5 with my_dissolve
    "[Name]" "Tips on how to make a potion?"
    "[Name]" "Thanks, I was happy with the usual method. That's it?"
    "Haley" "Don't worry about that!"
label haley_8_19:
    show sc i_Haley_8_6 with my_dissolve
    "Haley" "Here! Look at this..."

label haley_8_20:
    
    show sc i_Haley_8_7 with my_dissolve
    "[Name]" "Initials?"
    "[Name]" "What's the big deal?"
    "Haley" "Don't be stupid! E. Bloom? Elijah Bloom?"
    show sc i_Haley_8_8 with my_dissolve
    "[Name]" "No, it can't be."
    "[Name]" "That textbook must be ten years old."
    "[Name]" "And even if it was, what's the big deal?"
    show sc i_Haley_8_9 with my_dissolve
    "Haley" "That's what I thought at first. But my curiosity got the better of me."
    "Haley" "So I went to the library."
    "[Name]" "For what? The reference book?"
    show sc i_Haley_8_10 with my_dissolve
    "Haley" "Yeah. So what?"
    "Haley" "Just listen!"
    "Haley" "I found out that E. Bloom had already gone to Cordale eight years ago."
    "[Name]" "Something's not right."
    show sc i_Haley_8_11 with my_dissolve
    "Haley" "And H. Gross went to school with him. Gross. What do you think, is it Hans?"
    "[Name]" "Hmm, it's quite possible."
    "[Name]" "{i}(I can't believe she found something...){/i}"
    "[Name]" "{i}(And all this because of a couple of lines on the side of a textbook?){/i}"
    "[Name]" "{i}(I'm afraid to imagine what Haley could do if she was a stalker.){/i}"
    show sc i_Haley_8_12 with my_dissolve
    "[Name]" "And what do you want to do with this information?"
    "Haley" "All students have an enrollment and graduation date."
    "Haley" "All except E. Bloom and H. Gross."
    "Haley" "They are both listed as missing/killed."
    show sc i_Haley_8_13 with my_dissolve
    "Haley" "And all the news columns and articles about academy life back then..."
    "Haley" "It all looks like something got hushed up, [Name]!"
    "Haley" "I've got a nose for that kind of thing. Detective Haley's back in business!"
    "[Name]" "Ha-ha-ha. What are you gonna do? Investigate a case that's eight years old?"
    "Haley" "How else would you do it? I can't just leave it..."
    show sc i_Haley_8_14 with my_dissolve
    "Haley" "But there's no more information in the library."
    "Haley" "It's probably best to ask Elijah directly. What do you think?"
    "[Name]" "What, right now?"
    "Haley" "Don't you want to solve this mystery as soon as possible?"
    "[Name]" "Well, I don't know."
    "Haley" "Then let's hurry up!"
    "[Name]" "Okay, let's... Let's go. He's probably at the cafe."
    #jump main_interface_label
    if not hasattr(store, 'haley_8_label_menu_1_var', ) or not hasattr(store, 'haley_8_label_menu_2_var') or not hasattr(store, 'haley_8_label_menu_3_var'):
        call haley_8_label_menu from _call_haley_8_label_menu
    if hasattr(store, 'haley_8_label_menu_1_var'):
        $ del haley_8_label_menu_1_var
    if hasattr(store, 'haley_8_label_menu_2_var'):
        $ del haley_8_label_menu_2_var
    if hasattr(store, 'haley_8_label_menu_3_var'):
        $ del haley_8_label_menu_3_var

    return

label haley_9_label:


    scene sc i_Haley_9_1 with Dissolve(.5)
    "Haley" "He's sitting over there!"
    "[Name]" "Hold on, Haley. We're not running the hundred yard dash..."
    "Haley" "I was afraid he'd leave before we got here."
    show sc i_Haley_9_2 with my_dissolve
    "[Name]" "At least let me start the talking."
    "[Name]" "I have a feeling you might scare him with your obsession."
    "Haley" "If you say so..."
    show sc i_Haley_9_3 with my_dissolve
    "[Name]" "Yo, El J! Got room for us?"
    "Elijah" "[Name]! When a bro comes to me with a pretty chick like that..."
    "Elijah" "There's always room."
    show sc i_Haley_9_4 with my_dissolve
    "Elijah" "No offense, Haley, it's just a joke."
    "Haley" "Come on, I'm not offended by that."
    show sc i_Haley_9_5 with my_dissolve
    "[Name]" "El, we just stumbled across something strange."
    "[Name]" "Something to do with you."
    "Elijah" "Whatever you've heard about me, it's not true."
    "Elijah" "Unless you're looking to buy something, in which case..."
    show sc i_Haley_9_6 with my_dissolve
    "Haley" "That's not why we're here."
    "Elijah" "Why then?"
    show sc i_Haley_9_7 with my_dissolve
    "[Name]" "Haley got herself a pretty old potions book..."
    "Elijah" "Oh, guys. It's not that easy to trade a book. Fairies steal them all the time!"
    "Haley" "We know. It's not about that."
    "Elijah" "What is it about? Why are you taking so long to tell me?"
    show sc i_Haley_9_8 with my_dissolve
    "[Name]" "Dude, if you hadn't interrupted me, I would have told you already."
    "Elijah" "Okay, okay, easy!"
    show sc i_Haley_9_9 with my_dissolve
    "Haley" "There's a lot of notes in the margins of my textbook."
    "Haley" "Weird notes, Elijah."
    show sc i_Haley_9_10 with my_dissolve
    "[Name]" "It's about a student who went missing years ago."
    "Haley" "Don't you think that's weird?"
    "Elijah" "Dudes, I don't know where you're going with this."
    show sc i_Haley_9_11 with my_dissolve
    "Haley" "Take a closer look, El."
    "[Name]" "You see the signatures underneath the notes?"
    "Elijah" "..."
    "[Name]" "E. Bloom..."
    show sc i_Haley_9_12 with my_dissolve
    "Haley" "We're worried, headman..."
    "[Name]" "Do you have something to do with this?"
    show sc i_Haley_9_13 with my_dissolve
    "Elijah" "Pfft... Don't be ridiculous."
    "Elijah" "This book is ten years old, I was still in high school."
    "Elijah" "Why are you even bothering me with this? Not cool, man."
    "Haley" "We're just worried about you..."
    show sc i_Haley_9_14 with my_dissolve
    "Elijah" "Get this straight: I don't need your concern."
    "Elijah" "Or your long noses."
    "Elijah" "Forget about it. I'll talk to Amelie about replacing your textbook."
    "Haley" "But..."
    show sc i_Haley_9_15 with my_dissolve
    "Elijah" "The subject is closed."
    "Elijah" "Excuse me, I'm expecting guests."
    "Elijah" "You should go."
    return
label haley_10_label:

    show sc i_Haley_10_1 with my_dissolve
    "[Name]" "I don't know what got into him..."
    "[Name]" "All I asked was if he knew anything about the initials."
    "Haley" "There's more to it than that, I can feel it in my gut."
    show sc i_Haley_10_2 with my_dissolve
    "Haley" "He wouldn't be so angry if he didn't know whose records those were."
    "Haley" "It seems we have to find out if the other Bloom went to the school."
    "Haley" "And what his connection to Elijah is."
    show sc i_Haley_10_3 with my_dissolve
    "[Name]" "Don't you think he was clear he doesn't want us bringing it up?"
    "Haley" "Don't be so callous, [Name]!"
    "[Name]" "Why am I callous? I'm trying to consider his feelings."
    show sc i_Haley_10_4 with my_dissolve
    "Haley" "Didn't you hear how painful it was for him to talk about that?"
    "Haley" "How hard it is for him to remember this E. Bloom?"
    "Haley" "Something happened and we owe it to him to find out what!"
    show sc i_Haley_10_5 with my_dissolve
    "[Name]" "Why?!"
    "Haley" "Because I believe we will find something."
    "Haley" "Something that will ease Elijah's pain."
    "[Name]" "I can't believe..."
    "[Name]" "That's your excuse to get another thrill of adventure?!"
    show sc i_Haley_10_6 with my_dissolve
    "Haley" "Stop being so boring! We're killing two birds with one stone."
    "[Name]" "The important thing is that we don't end up being the birds."
    "Haley" "Smartass."
    show sc i_Haley_10_7 with my_dissolve
    "Haley" "[Name] I've made up my mind."
    "Haley" "Are you with me or not?"
    show sc i_Haley_10_8 with my_dissolve
    "[Name]" "I got to keep an eye on you."
    "Haley" "Great! "
    "[Name]" "What's the plan?"
    show sc i_Haley_10_9 with my_dissolve
    "Haley" "I'll go to the library and try to find some information about the students."
    "Haley" "I'll meet you before class and tell you what I found out."
    show sc i_Haley_10_10 with my_dissolve
    "Haley" "Then we'll decide what to do."
    "[Name]" "What should I do?"
    show sc i_Haley_10_11 with my_dissolve
    "Haley" "I have to think about it."
    "Haley" "Let's talk about it tomorrow."
    show sc i_Haley_10_12 with my_dissolve
    "[Name]" "Okay. I got it."
    menu:
        "Walk her to dorm":
            $ pass
            show sc i_Haley_10_12 with my_dissolve
            "[Name]" "Are you going in to the dorms now?"
            show sc i_Haley_10_13 with my_dissolve
            "Haley" "Yeah. Why?"
            "[Name]" "Let me keep you company."
            show sc i_Haley_10_14 with my_dissolve
            "Haley" "That's so sweet of you."
            "Haley" "Well, sure."
            show sc i_Haley_10_15 with my_dissolve
            "[Name]" "After you."
            "Haley" "Thank you, sir."
            scene image '#000' with Dissolve(.5)
            $ ltssttttt = 1
            return
            
        "Say goodbye":
            $ pass

    show sc i_Haley_10_12 with my_dissolve
    "[Name]" "I'll see you then. I'm staying here. Still in the middle of something."
    show sc i_Haley_10_13 with my_dissolve
    "Haley" "[Name], thank you for volunteering to help me."
    "[Name]" "It's nothing."
    show sc i_Haley_10_16 with my_dissolve
    "Haley" "Bye-bye!"
    scene image '#000' with Dissolve(.5)

    return
label pre_Haley_11_label:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    call Haley_11_label from _call_Haley_11_label_1
    $ log_message.update({"QLOG_Haley":8})
    $ Q_Haley=11
    $ change_location('cord_garden_l')
    hide screen black_tmp_screen_menu


    jump main_interface_label

label Haley_11_label:
    
    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface
    hide screen black_tmp_screen_menu
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

    show sc i_Haley_1_2 with my_dissolve
    "[Name]" "Hi, Haley!"
    "Haley" "Yo, [Name], good to see you!"
    "[Name]" "So, did you get anything?"
    show sc i_Haley_1_15 with my_dissolve
    "Haley" "Yeah, but I had to bend the school rules a little bit."
    "Haley" "I'm not proud of it..."
    "[Name]" "{i}(Haley was so concerned about her reputation, and now she's risking it...){/i}"
    "[Name]" "{i}(Apparently the spirit of an adventurer is stronger than that of a crammer.){/i}"
    "[Name]" "Haley broke the rules? Sure the world hasn't gone crazy?"
    show sc i_Haley_1_4 with my_dissolve
    "Haley" "Hey! Keep your voice down. I don't want anyone to hear you."
    "Haley" "Besides, you can hear everything in this room..."
    "Haley" "Joshie would probably tell everyone if he found out."
    "[Name]" "You're right."
    show sc i_Haley_11_1 with my_dissolve
    "[Name]" "So maybe we should talk somewhere quieter."
    "Haley" "That's a great idea."
    show sc i_Haley_11_2 with my_dissolve
    "Haley" "Let's go!"
    "[Name]" "{i}(There's probably a secluded spot in the courtyard.){/i}"
    "Haley" "If we hurry, I can even make it back to class in time."
    show sc i_Haley_11_3 with my_dissolve
    "[Name]" "After you, madam."
    "Haley" "Hee hee hee..."
    "Haley" "You're so sophisticated, Monsieur [Name]."
    "Haley" "Let's go to the courtyard."
    scene image '#000' with Dissolve(.5)
    scene sc i_Haley_11_4 with Dissolve(.5)
    
    "Haley" "Where can you and I sit so we can talk more comfortably..."
    "[Name]" "Hmm, let's see..."
    show sc i_Haley_11_5 with my_dissolve
    "Haley" "Look! What a luck..."
    "[Name]" "What?"
    "Haley" "The fountain is empty. Shall we take a seat?"
    "[Name]" "Sure."
    show sc i_Haley_11_6 with my_dissolve
    "Haley" "It's great here. Especially when it's not as crowded as usual."
    "[Name]" "It is."
    "Haley" "This place makes me feel so peaceful..."
    "Haley" "I don't know why, but I feel like I could spend the whole day like this."
    show sc i_Haley_11_7 with my_dissolve
    "Haley" "Would you?"
    "[Name]" "{i}(What got into her? She was in such a hurry to talk about the textbook, and now...){/i}"
    "[Name]" "{i}(Or was it just an excuse to get out here together?){/i}"
    menu:
        "Touch her hand":
            $ touch_haley_1 = True
        "Talk about a book":
            jump haley_11_label_84

    show sc i_Haley_11_8 with my_dissolve
    "[Name]" "{i}(Alright, I'll risk it. I have to make the first move!){/i}"
    show sc i_Haley_11_9 with my_dissolve
    "Haley" "[Name] ..."
    "[Name]" "Should I stop? Sorry, I didn't mean to embarrass you..."
    "Haley" "No, what are you..."
    show sc i_Haley_11_10 with my_dissolve
    "Haley" "No...Don't take it away."
    "Haley" "I didn't say I dont like it..."
    "Haley" "It's just so sudden."
    show sc i_Haley_11_11 with my_dissolve
    "Haley" "I'm sorry, I'm being weird about it, aren't I?"
    "Haley" "I'm not very experienced with these things..."
    menu:
        "Touch her knee":
            $ touch_haley_2 = True
        "Change the subject":
            jump haley_11_label_84
    "[Name]" "Haley, baby."
    "[Name]" "Don't worry about it, you're being great."
    "Haley" "You really think so?"
    show sc i_Haley_11_12 with my_dissolve
    "[Name]" "I wouldn't keep going otherwise."
    "Haley" "..."
    show sc i_Haley_11_13 with my_dissolve
    "Haley" "I... I don't know what to do, [Name]."
    "Haley" "I've never had time to have a relationship."
    "Haley" "Before you, I never flirted with anyone..."
    show sc i_Haley_11_14 with my_dissolve
    "[Name]" "Are you kidding?"
    "Haley" "No..."
    show sc i_Haley_11_15 with my_dissolve
    "[Name]" "I never thought of that! I thought you were really good at flirting."
    "Haley" "I've done my homework by studying the theory."
    "[Name]" "{i}(Nerds know how to ruin the romance of any dialogue...){/i}"
    "[Name]" "I know what you need right now!"
    menu:
        "Kiss her":
            $ kiss_haley = True
        "Change the subject":
            jump haley_11_label_84

    show sc i_Haley_11_16 with my_dissolve
    "Haley" "What?"
    show sc i_Haley_11_17 with my_dissolve
    "[Name]" "{i}(What a reckless thing to do...){/i}"
    "[Name]" "{i}(But her lips are so soft I don't care...){/i}"
    show sc i_Haley_11_18 with my_dissolve
    "Haley" "mhm...."
    "[Name]" "{i}(She's clearly surprised... But she's in no hurry to stop the kiss.){/i}"
    show sc i_Haley_11_19 with my_dissolve
    "Haley" "mhm....ooh..."
    "[Name]" "{i}(She seems to like it.){/i}"
    "[Name]" "{i}(Now I agree. I could spend the whole day here too...){/i}"
    show sc i_Haley_11_20 with my_dissolve
    "[Name]" "{i}(She has such pretty eyes...){/i}"
    "[Name]" "Haley..."
    show sc i_Haley_11_21 with my_dissolve
    "[Name]" "I have to say you're too good a kisser. Was it your first time too?"
    "Haley" "Hee... hee... Yes, it was my first kiss."
    show sc i_Haley_11_22 with my_dissolve
    "Haley" "Not how I imagined it...."
    "[Name]" "How much worse was it than you imagined?"
    show sc i_Haley_11_23 with my_dissolve
    "Haley" "Better."
    "[Name]" "{i}(...Better? Did she really say better? Better than she imagined?){/i}"
    "[Name]" "{i}(I'm still on a roll!){/i}"
    "[Name]" "I'm flattered."
    show sc i_Haley_11_24 with my_dissolve
    "[Name]" "{i}(I think I've already squeezed all the romance resource out of Haley's benda.){/i}"
    "[Name]" "{i}(We need to change the subject before we get to the practice of other theories.){/i}"
label haley_11_label_84:
    show sc i_Haley_11_7 with my_dissolve
    "[Name]" "I think we should discuss the book."
    "[Name]" "Did you discover something?"
    show sc i_Haley_11_25 with my_dissolve
    "Haley" "Right! I was just starting to tell you about it..."
    "Haley" "It wasn't that simple."
    "Haley" "All info on E. Bloom and H. Gross has been blacked out and removed from the record books."
    show sc i_Haley_11_26 with my_dissolve
    "Haley" "There are no photos of them in albums, no documents in the archives..."
    "Haley" "Nothing!"
    "[Name]" "It can't be!"
    "[Name]" "They definitely existed, didn't they?"
    show sc i_Haley_11_27 with my_dissolve
    "Haley" "You saw Elijah's reaction."
    "[Name]" "Yeah, I did."
    "[Name]" "Then what's the plan?"
    "Haley" "I think..."
    show sc i_Haley_11_28 with my_dissolve
    "Haley" "No, I'm pretty sure there's a hidden archive in the library."
    "Haley" "I'm sure we'll find the information we need there."
    show sc i_Haley_11_29 with my_dissolve
    "[Name]" "What makes you think that?"
    show sc i_Haley_11_28 with my_dissolve
    "Haley" "One of the shelves feels a little drafty."
    "Haley" "Amelia came out of nowhere one day behind me."
    "Haley" "Right next to that rack!"
    show sc i_Haley_11_29 with my_dissolve
    "[Name]" "Wow!"
    "[Name]" "Who knew you could learn so much from hanging out in the library!"
    show sc i_Haley_11_30 with my_dissolve
    "Haley" "Anyway, I think Amelia suspects that I know something."
    "Haley" "She's too careful around me."
    "[Name]" "So what do you suggest?"
    show sc i_Haley_11_31 with my_dissolve
    "Haley" "I hope you like to read!"
    "[Name]" "What?"
    "Haley" "You spend the day in the library."
    show sc i_Haley_11_32 with my_dissolve
    "[Name]" "Oh, to keep an eye on her?"
    "Haley" "Exactly."
    "Haley" "We have to figure out how to get into the secret archives."
    "Haley" "Hopefully we'll find something there..."
    show sc i_Haley_11_33 with my_dissolve
    "[Name]" "I'm sure we'll find something."
    "[Name]" "That's a great idea."
    "[Name]" "You're good!"
    show sc i_Haley_11_34 with my_dissolve
    "Haley" "R-really?"
    "[Name]" "Of course it is!"
    show sc i_Haley_11_35 with my_dissolve
    "Haley" "Then find out how to get into the archives and tell me."
    "Haley" "I'll meet you afterwards in my room."
    "[Name]" "Okay."
    show sc i_Haley_11_36 with my_dissolve
    "Haley" "Oh, that's great. I can't wait to..."
    "Haley" "Okay, time to get back to class!"
    scene image '#000' with Dissolve(.5)
    return

label Haley_12_label:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface

    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2

    #call Haley_11_label #from _call_Haley_11_label_1
    #$ log_message.update({"QLOG_Haley":8})
    #$ Q_Haley=11
    #$ change_location('cord_garden_l')
    hide screen black_tmp_screen_menu

    show sc i_Amelie_2_1 with my_dissolve
    "[Name]" "(I need to think of a reason why I'll be sitting here.)"
    "[Name]" "Hello. I need to prepare for a report on the fundamentals of magic."
    "Amelie" "Sounds interesting."
    show sc i_Amelie_2_3 with my_dissolve
    "Amelie" "And how can I help you?"
    "[Name]" "Don't you have any books on... methodology for creating a fireball?"
    "Amelie" "Just a minute."
    show sc i_Amelie_2_12 with my_dissolve
    "Amelie" '{i}Judging by my notes on Pascal Lovegoods "Let the sphere burn!", theres plenty of information.{/i}'
    "Amelie" "I think you're good with it."
    "[Name]" "That's great. Thank you very much,"
    show sc i_Amelie_2_13 with my_dissolve
    "Amelie" "Anything else?"
    "[Name]" "Can I sit here and learn?"
    "Amelie" "Sure. This whole reading room is for students."
    show sc i_Haley_12_1 with my_dissolve
    "[Name]" "(Took another weightier book too look more dedicated.)"
    "[Name]" "(Now it sure looks like I'm serious about studying.)"
    "[Name]" "(Okay. I took my seat.)"
    show sc i_Haley_12_2 with my_dissolve
    "[Name]" "(Haley says she felt something wrong from here.)"
    "[Name]" "(My job is to pretend I'm studying.)"
    "[Name]" "(And figure out where the secret room in the library is hidden.)"
    show sc i_Haley_12_3 with my_dissolve
    "[Name]" "(Hmm, that's quite a view from up there.)"
    "[Name]" "(I hope Amelie can't see me staring at her weirdly.)"
    "[Name]" "(Although if anything, I can always say I was admiring her legs...)"
    scene image '#000' with Dissolve(.5)
    scene sc i_Haley_12_4 with Dissolve(.5)
    "[Name]" "It's been hours. My neck is stiff.)"
    "[Name]" "(My arms are tired of holding a book like this.)"
    "[Name]" "(Wait, is she going to do something?)"
    show sc i_Haley_12_5 with my_dissolve
    "[Name]" "(What are you up to, Amelia?)"
    "[Name]" "(It's like she's looking for something.)"
    "[Name]" "(Maybe something fell down?)"
    "[Name]" "(I would help, but it would give away my observation...)"
    show sc i_Haley_12_6 with my_dissolve
    "[Name]" "(Ah, that's it.)"
    "[Name]" "(Your pen fell off the table!)"
    show sc i_Haley_12_7 with my_dissolve
    "[Name]" "(And that's the most interesting thing that's happened to you all day...)"
    "[Name]" "(Amelie, was our little genius Haley mistaken?)"
    "[Name]" "(And there's no secret room?)"
    show sc i_Haley_12_8 with my_dissolve
    "[Name]" "(Can't say my day is wasted, though.)"
    "[Name]" "(How did Amelia, with her looks, become a librarian?)"
    "[Name]" "(Sometimes you can't take your eyes off her...)"
    scene image '#000' with Dissolve(.5)
    scene sc i_Haley_12_9 with Dissolve(.5)
    "[Name]" "(It's getting harder and harder to stay here every hour.)"
    "[Name]" "(I'm tired, I'm hungry and I have to pee...)"
    "[Name]" "(Wait a minute! Is she looking in my direction?)"
    show sc i_Haley_12_10 with my_dissolve
    "[Name]" "(She's definitely interested in me!)"
    "[Name]" "(Damn, if she finds out I'm watching her...)"
    show sc i_Haley_12_11 with my_dissolve
    "[Name]" "(Reading a book. What an interesting book. Pretending to read a book.)"
    "[Name]" "(Don't look here. Don't look here...)"
    show sc i_Haley_12_12 with my_dissolve
    "[Name]" "(Let's take a glace...)"
    "[Name]" "(!!!)"
    "[Name]" "(WHERE IS SHE?!)"
    show sc i_Haley_12_13 with my_dissolve
    "[Name]" "(WHERE DID SHE GO?!)"
    "[Name]" "(Whoa...)"
    "[Name]" "(It feels like she's vanished...)"
    show sc i_Haley_12_14 with my_dissolve
    "[Name]" "(Hmm... I guess there's no point in continuing to sit here.)"
    "[Name]" "(If she did find a moment to sneak into the room...)"
    "[Name]" "(I don't think she'll come out while I'm sitting here.)"
    show sc i_Haley_12_15 with my_dissolve
    "[Name]" "(I'll pretend to leave.)"
    "[Name]" "(I'll turn in my books like I'm done.)"
    "[Name]" "(And I'll go...)"
    show sc i_Haley_12_16 with my_dissolve
    "[Name]" "(What the?!)"
    "[Name]" "(I think that glow is coming from the second floor...)"
    "[Name]" "(We have to hide somewhere and trace exactly where it's coming from.)"
    show sc i_Haley_12_17 with my_dissolve
    "[Name]" "(The shelf behind her back seems to have turned into a portal...)"
    "[Name]" "(What is stored there?)"
    "[Name]" "(And how to get there?!)"
    show sc i_Haley_12_18 with my_dissolve
    "[Name]" "(Shit, she's coming this way...)"
    "[Name]" "(I hope she won't look under the stairs...)"
    show sc i_Haley_12_19 with my_dissolve
    "[Name]" "(Amelia is holding some suspicious coins...)"
    "[Name]" "(Maybe they have something to do with the secret room?)"
    "[Name]" "(In any case, I won't know now...)"
    show sc i_Haley_12_20 with my_dissolve
    "[Name]" "(I think she keeps them on her desk.)"
    "[Name]" "(All I have to do is get to it while she's not looking.)"
    "[Name]" "(I'm sure Haley will have a better plan.)"
    show sc i_Haley_12_21 with my_dissolve
    "[Name]" "(All that's left is to get out of here...)"
    "[Name]" "(And tell her everything I've learned.)"
    show sc i_Haley_12_22 with my_dissolve
    "[Name]" "(Please don't turn around...)"
    "[Name]" "(I think I can do it!)"   
    scene image '#000' with Dissolve(.5)
    return