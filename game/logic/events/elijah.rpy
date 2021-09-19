label elijah_events_label:


    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.1)

    $ set_now = elijah_events_set
    menu:

        "0 Talk to Elijah" if Q_Elijah == 0:

            call Elijah_1_label from _call_Elijah_1_label
            $ p_up('Elijah', 2)
            $ Q_Elijah = 1
            $ log_message.update({"QLOG_Elijah":2})


        "2 Talk to Elijah" if Q_Elijah == 2:

            if Q_Sabrina==0:

                call Elijah_1_1_label from _call_Elijah_1_1_label
            elif True:



                call Elijah_1_2_label from _call_Elijah_1_2_label

            $ log_message.update({"QLOG_Elijah":3})
            $ elijah_events_set.append("2 Talk to Elijah")
            $ wakeup_sets.append([

            
            elijah_events_set, "2 Talk to Elijah"
            
            
                ])

        "Not now" if True:

            show screen main_interface 
            show screen show_hide_locations_2
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label


label elijah_events_caffe_label:


    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.5)

    $ set_now = elijah_events_set_2
    menu:

        "Talk to Elijah" if Q_Elijah == 2:
            if Q_Sabrina==0:
                call Elijah_2_1_label from _call_Elijah_2_1_label

                $ log_message.update({"QLOG_Elijah":3})


                $ elijah_events_set_2.append("Talk to Elijah")
                $ wakeup_sets.append([

                
                elijah_events_set_2, "Talk to Elijah"
                
                
                    ])
            else:

                call Elijah_3_label from _call_Elijah_3_label
                $ Q_Elijah = 3
                $ log_message.update({"QLOG_Elijah":4})
                $ p_up('Elijah', 4)

                $ elijah_view_3 = False
                $ change_location_2(location_now, time_now+1)
        "4 About the job" if Q_Elijah == 3:
            call Elijah_4_label from _call_Elijah_4_label
            $ Q_Elijah = 4
            $ log_message.update({"QLOG_Elijah":4})
            

            hide screen black_tmp_screen_menu


            $ log_message.update({"QLOG_Elijah":4})
        "Not now" if True:
            show screen main_interface 
            show screen show_hide_locations_2
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label

label Elijah_1_label:

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

    show sc i_Elijah_1_2 with Dissolve(.5)
    "[Name]" "{i}(I recall Elijah wanted to meet me!){/i}"
    "[Name]" "{i}(Let's find out what he wants.){/i}"
    "[Name]" "Hi, prefect!"
    "Elijah" "[Name]!{w} You're the one I've been waiting for! I have your instructions here!"
    "[Name]" "Sorry, had to change."
    "[Name]" "What instructions?"
    show sc i_Elijah_1_3 with my_dissolve
    "Elijah" "Safety instructions."
    "Elijah" "The local poltergeist is quite vicious..."
    "[Name]" "Great..."
    show sc i_Elijah_1_4 with my_dissolve
    "Elijah" "Relax.{w} I was kidding."
    "Elijah" "Our poltergeist is pretty peaceful."
    "Elijah" "I'm talking about learning and stuff."
    show sc i_Elijah_1_5 with my_dissolve
    "Elijah" "Oh, yeah! You're a freshman, I need to brief you."
    "Elijah" "I'm personally responsible for making sure you're fully prepared to study!"
    "Elijah" "So I need you to get your textbooks."
    show sc i_Elijah_1_6 with my_dissolve
    "Elijah" "Here, take your {b}student card{/b}... Show it to the library."
    "Elijah" "They don't give out textbooks without it."
    "Elijah" "After you get it, you can go to class."
    "Elijah" "Questions, objections, requests?"
    "[Name]" "Why do I even need a card? Who can be here except students and teachers?"
    show sc i_Elijah_1_5 with my_dissolve
    "Elijah" "Shapeshifters, evil entities, and spirits from another realm."
    "Elijah" "Strange question, dude. Don't forget what place you are studying in!"
    "Elijah" "In Cordale you can meet unexpected things anywhere, even in the library."
    show sc i_Elijah_1_7 with my_dissolve
    "Elijah" "By the way, about the temple of knowledge."
    "Elijah" "The library is open in the morning and afternoon."
    "Elijah" "Stop by during that time and pick up some textbooks from Amelie."
    "[Name]" "Amelie is..."
    "Elijah" "Our librarian."
    show sc i_Elijah_1_8 with my_dissolve
    "Elijah" "She' s super hot, if you ask my opinion."
    "[Name]" "Got it, got it."
    "[Name]" "And the library is..."
    "Elijah" "It's a big room with lots of books."
    "Elijah" "You go to the academy, and there..."
    "Elijah" "...in the courtyard, first door on the left."
    show sc i_Elijah_1_9 with my_dissolve
    "Elijah" "Any questions?"

    menu:
        "Learn about classes" if True:
            $ pass
        "Nothing" if True:
            jump Elijah_1_label_64


    show sc i_Elijah_1_9 with my_dissolve
    "[Name]" "Yes, I wanted to know more about the classes."
    show sc i_Elijah_1_5 with my_dissolve
    "Elijah" "First semester you'll have two core courses."
    "Elijah" "Keep your student card with you."
    "Elijah" "With it, you can attend Fundamentals of Magic and Potions."
    "Elijah" "Fundamentals of Magic has been taught by Miss Lapis for the past few years."
    "Elijah" "You probably already know her."
    show sc i_Elijah_1_10 with my_dissolve
    "Elijah" "The class is in the classroom where you had your exam."
    "Elijah" "I think Victoria, as usual, will focus on battle magic."
    "Elijah" "I wouldn't say that's a bad thing."
    "Elijah" "Combat magic is rough, but it's very impressive."
    "Elijah" "It's great for beginners!"
    show sc i_Elijah_1_5 with my_dissolve
    "Elijah" "Watch out for your eyebrows, though. Very easy to burn."
    "[Name]" "Good."
    "Elijah" "Potions is taught by Miss Sabrina Spellman."
    "Elijah" "You don't know her, so make sure you go to class."
    "[Name]" "Is there anything I should know about her?"
    show sc i_Elijah_1_10 with my_dissolve
    "Elijah" "She's a sweetheart."
    "Elijah" "I kind of feel sorry for her."
    "[Name]" "Why?"
    "Elijah" "Most of the time it's more fun for newcomers to do magic than it is to brew potions."
    "Elijah" "And she really resents that."
    "Elijah" "Try to show a bit of interest during her classes."
    "Elijah" "And you'll already be in good standing."
    "[Name]" "Sounds simple enough."
    "Elijah" "It is."

    jump Elijah_1_label_69
label Elijah_1_label_64:
    hide screen main_interface

    show sc i_Elijah_1_9 with my_dissolve
    "[Name]" "No, I'll figure it out on the spot."
    show sc i_Elijah_1_10 with my_dissolve
    "Elijah" "Suit yourself, it's up to you."
    "Elijah" "I almost forgot! Here's your security clearance."
    "Elijah" "With it, you can take Fundamentals of Magic and Potions."
    "[Name]" "Thank you."

label Elijah_1_label_69:

    show sc i_Elijah_1_5 with my_dissolve
    "Elijah" "Anyway, I've got a lot to do."
    "Elijah" "When you've done both Fundamentals of Magic and Potions..."
    "Elijah" "Find me at the cafe."
    show sc i_Elijah_1_10 with my_dissolve
    "Elijah" "I almost always hang out there in the evening."
    "[Name]" "You got it."

    return




label Elijah_3_label:

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


    show sc i_Elijah_3_1 with Dissolve(.5)
    "Elijah" "Yo! [Name]!{w} This way!"
    "Elijah" "Have a seat."
    "[Name]" "Hi."
    show sc i_Elijah_3_2 with my_dissolve
    "Elijah" "So, did you meet the teachers?"
    "[Name]" "Sure did."
    "Elijah" "That's great!"
    "Elijah" "I'm sure you'll soon be 100%% integrated into university life."
    "[Name]" "What do you mean?"
    "Elijah" "Well, studying, clubs, parties, romance."
    show sc i_Elijah_3_3 with my_dissolve
    "Elijah" "Let me ask you a question, [Name]."
    "[Name]" "Shoot."
    "Elijah" "What did you come to Cordale for?"
    "[Name]" "Oh, uh..."
    "[Name]" "It's a weird question..."




    menu:
        "I've been given a chance" if True:
            $ pass
        "To be the best" if True:
            jump Elijah_3_label_26
        "New acquaintances" if True:
            jump Elijah_3_label_39


    show sc i_Elijah_3_3 with my_dissolve
    "[Name]" "The invitation came to me and I jumped at the chance."
    show sc i_Elijah_3_4 with my_dissolve
    "[Name]" "How do you know what you're in it for when you've only just learned about magic?"
    "Elijah" "Well, you have a point."
    show sc i_Elijah_3_7 with my_dissolve
    "Elijah" "So, anyway, what I'm asking is..."
    "Elijah" "I got some business on the side."
    "Elijah" "I could use someone like you."
    "[Name]" "Like me?"
    show sc i_Elijah_3_8 with my_dissolve
    "Elijah" "Yes.{w} A man who takes a chance when he sees one."



    jump Elijah_3_label_51
label Elijah_3_label_26:
    hide screen main_interface

    show sc i_Elijah_3_3 with my_dissolve
    "[Name]" "I'm an athlete.{w} If I take something on, it's to be the best."
    show sc i_Elijah_3_5 with my_dissolve
    "Elijah" "That's the spirit."
    "Elijah" "You remind me of someone."
    "Elijah" "Is that Samantha's influence, by any chance?"
    "[Name]" "Heh heh."
    "[Name]" "Not really.{w} But we were raised the same way."
    "Elijah" "I see."
    show sc i_Elijah_3_7 with my_dissolve
    "Elijah" "So, anyway, what I'm asking is..."
    "Elijah" "I got some business on the side."
    "Elijah" "I could use someone like you."
    "[Name]" "Like me?"
    show sc i_Elijah_3_8 with my_dissolve
    "Elijah" "Yes. Most people don't care about themselves."
    "Elijah" "You want to be the best. I respect that."
    jump Elijah_3_label_51
label Elijah_3_label_39:
    hide screen main_interface

    show sc i_Elijah_3_3 with my_dissolve
    "[Name]" "I'm hoping to make some new and interesting acquaintances here."
    "[Name]" "If you know what I mean."
    show sc i_Elijah_3_6 with my_dissolve
    "Elijah" "Ah-ha-ha...{w} Are you serious?"
    "Elijah" "A community college would be enough for that, man."
    "[Name]" "It's more fun to get to know someone with magic."
    "Elijah" "Yeah, well, you got a point there."
    show sc i_Elijah_3_7 with my_dissolve
    "Elijah" "So, anyway, what I'm asking is..."
    "Elijah" "I got some business on the side."
    "Elijah" "I could use someone like you."
    "[Name]" "Like me?"
    show sc i_Elijah_3_8 with my_dissolve
    "Elijah" "Yes. {w} A man who's open to new acquaintances."
    "Elijah" "A guy like that always comes in handy."
label Elijah_3_label_51:
    hide screen main_interface

    show sc i_Elijah_3_8 with my_dissolve
    "[Name]" "Drop your riddles!"
    "[Name]" "What's the deal?"
    show sc i_Elijah_3_9 with my_dissolve
    "Elijah" "You see, everything in Cordale is fine..."
    "Elijah" "Except a couple of overly strict rules."
    "Elijah" "Many of the things forbidden in the academy..."
    "Elijah" "...can be very useful and pleasant."
    "[Name]" "What are you talking about?"
    show sc i_Elijah_3_10 with my_dissolve
    "Elijah" "Well, you know... A little doping to get things done."
    "Elijah" "Or the opposite, to relax and take your time."
    "[Name]" "Are you talking about something illegal?"
    show sc i_Elijah_3_11 with my_dissolve
    "Elijah" "Come on! Of course not."
    "Elijah" "In some states and countries it's legal, in others not so much."
    "Elijah" "If people's average IQ wasn't around 70..."
    "Elijah" "No one would be banning these things."
    "[Name]" "You think?"
    show sc i_Elijah_3_12 with my_dissolve
    "Elijah" "Sure. There's a limit to everything."
    "Elijah" "You can die from too much coffee."
    "Elijah" "And if you start the Hungarian dragon fireworks without reading the instructions..."
    "Elijah" "It's a lot easier to die."
    show sc i_Elijah_3_13 with my_dissolve
    "[Name]" "Well, we're not talking about fireworks..."
    "Elijah" "Why not? It's one of my offers."
    "Elijah" "I got all kinds of stuff, depending on who it's for and what it's for."
    "Elijah" "That's why I need help."
    "Elijah" "Some orders I can't handle on my own."
    "Elijah" "Especially now that I have the responsibilities of a house advisor."
    show sc i_Elijah_3_14 with my_dissolve
    "Elijah" "Are you with me?"
    "[Name]" "I don't know, um..."
    "[Name]" "I need to think about it."
    "Elijah" "Okay, I understand."
    show sc i_Elijah_3_12 with my_dissolve
    "Elijah" "{i}It's not an emergency, usually everyone brings ″stuff″ with them after the summer.{/i}"
    "Elijah" "They come to me afterwards."
    "Elijah" "Or when they're planning a party."
    "Elijah" "I'm telling you, there are perks to this business."
    "[Name]" "Like the risk of being expelled?"
    show sc i_Elijah_3_15 with my_dissolve
    "Elijah" "Nonsense! Arthur's too kind-hearted."
    "Elijah" "I got caught with a live dragon egg once!"
    "Elijah" "The boys at Crowhive wanted to breed it and tame it so that..."
    "Elijah" "It doesn't matter. The point is I've never been expelled."
    "Elijah" "As you can see, it didn't even stop me from becoming prefect."
    show sc i_Elijah_3_7 with my_dissolve
    "[Name]" "All right, all right.{w} You sound convincing."
    "[Name]" "But I still have to think about it."
    "Elijah" "When you decide, you know where to find me."
    "Elijah" "Just don't talk about it on campus."
    "Elijah" "I don't want anyone to accidentally overhear us."
    "[Name]" "All right. I'll see you later."
    "Elijah" "All right."
    return
label Elijah_1_1_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)

    show sc i_Elijah_1_3 with Dissolve(.5)
    "[Name]" "Yo, headman!"
    "Elijah" "[Name]! How's it going - {b}have you been to any lectures{/b}?"
    "[Name]" "Still in progress."
    show sc i_Elijah_1_7 with my_dissolve
    "Elijah" "Don't wait too long, bro."
    "Elijah" "Otherwise you risk falling hopelessly behind your classmates."
    "Elijah" "You don't want to be the only one who can't make a fireball, do you?"
    "[Name]" "I guess not."
    "Elijah" "All right, then. Off you go!"
    return
label Elijah_1_2_label:
    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)

    show sc i_Elijah_1_10 with Dissolve(.5)
    "[Name]" "El, I was just looking for you!"
    "Elijah" "Why?"
    "[Name]" "You wanted to discuss something after I attended both classes."
    show sc i_Elijah_1_8 with my_dissolve
    "Elijah" "I seem to recall something..."
    "Elijah" "Anyway, why are you bothering yourself with this in the morning?"
    "Elijah" "You should get to classes."
    show sc i_Elijah_1_9 with my_dissolve
    "Elijah" "{b}We can meet at the cafe in the evening{/b} and talk quietly."
    "[Name]" "Okay."
    return
label Elijah_2_1_label:
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


    show sc i_Elijah_3_2 with Dissolve(.5)
    "[Name]" "Yo, Elijah!"
    "Elijah" "Hey, [Name]!"
    show sc i_Elijah_3_3 with my_dissolve
    "Elijah" "What brings you by?"
    "[Name]" "Just passing by and thought I'd say hello."
    "Elijah" "I see."
    show sc i_Elijah_3_5 with my_dissolve
    "Elijah" "How are you, {b}have you been to any lectures yet{/b}?"
    "[Name]" "I'm still in the process."
    show sc i_Elijah_3_8 with my_dissolve
    "Elijah" "A word of advice!"
    "Elijah" "Don't take too long, bro."
    "[Name]" "All right, man."
    show sc i_Elijah_3_1 with my_dissolve
    "Elijah" "Good luck with it."
    "[Name]" "You too."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
label pre_Elijah_4_label:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    call Elijah_4_label from _call_Elijah_4_label_1
    $ Q_Elijah = 4
    $ log_message.update({"QLOG_Elijah":4})
    

    hide screen black_tmp_screen_menu


    jump main_interface_label
label Elijah_4_label:


    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3

    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)
    show sc i_Elijah_3_2 with my_dissolve
    "[Name]" "Listen, what about that job you were talking about?"
    "[Name]" "Is it still available?"
    "Elijah" "Sure, bro."
    show sc i_Elijah_3_5 with my_dissolve
    "Elijah" "Glad you asked. I could really use some help!"
    "[Name]" "What's up?"
    "Elijah" "There's an order that needs to be picked up in town this weekend."
    "Elijah" "But I can't do it personally."
    show sc i_Elijah_3_6 with my_dissolve
    "[Name]" "Why not?"
    "Elijah" "I asked a fairy to get something for me."
    "Elijah" "She got in trouble with the law because of it."
    show sc i_Elijah_3_10 with my_dissolve
    "Elijah" "And her father said he'd rip my head off next time he sees me."
    "[Name]" "So that's why you can't go there... I see."
    "Elijah" "So, will you pick up the nectar of the dryads for me?"
    "[Name]" "Nectar of the dryads?"
    scene sc i_Elijah_3_6 with Dissolve(.5)
    menu:
        "What's that?":
            $ pass
        "Alright":
            jump Elijah_4_label_28
    show sc i_Elijah_3_13 with my_dissolve
    "[Name]" "What is that?"
    "Elijah" "Haven't you ever heard of the nectar of the dryads?"
    "Elijah" "Believe me, there are no words to describe it."
    show sc i_Elijah_3_12 with my_dissolve
    "[Name]" "Well, you try it..."
    "Elijah" "You're going back to your roots, brother."
    "Elijah" "No shyness, no doubts. Euphoria."
    show sc i_Elijah_3_15 with my_dissolve
    "[Name]" "What is that, a drug?"
    "Elijah" "Hey, take it easy. No, of course it's not!"
    "Elijah" "It's just a powerful magical aphrodisiac."
    "[Name]" "Oh, wow..."
label Elijah_4_label_28:
    show sc i_Elijah_3_5 with my_dissolve
    "[Name]" "All right, I'm on it."
    "Elijah" "That's great."
    "Elijah" "I knew you wouldn't let me down."
    show sc i_Elijah_3_2 with my_dissolve
    "Elijah" "You have to go to Chompsky's on the main square."
    "Elijah" "And tell the owner to get Willow."
    "[Name]" "Got it."
    show sc i_Elijah_3_5 with my_dissolve
    "Elijah" "Tell her you're from Mr. Bloom."
    "Elijah" "It's already paid for."
    "[Name]" "It's that simple?"
    "Elijah" "Of course it is, handsome. I told you it was a great job."
    show sc i_Elijah_3_11 with my_dissolve
    "Elijah" "I'll see you back here when you pick up the nectar."
    "Elijah" "Good luck."
    "[Name]" "{i}(Did he just call me handsome?){/i}"
    "[Name]" "{i}(And what's with the weird look?){/i}"
    "[Name]" "Alright. I'll see you later."
    scene image '#000' with Dissolve(.5)
    # QLOG_Elijah=5
    # Q_Elijah=4
    # TS +1
    return

label Elijah_5_label:

    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3

    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)

    show sc i_Chompski_1_28 with my_dissolve
    "[Name]" "Gordon, hello."
    "Gordon" "Come on in, boy, pick out what you like!"
    "Gordon" "Come closer."
    show sc i_Chompski_1_29 with my_dissolve
    "Gordon" "So, why are you here?"
    "[Name]" "Actually, I'm not here to see you this time."
    "[Name]" "Can you get Willow?"
    "Gordon" "Heh! Sure."
    show sc i_Chompski_1_30 with my_dissolve
    "Gordon" "Willow, baby!"
    "Gordon" "You have visitors!"
    "Gordon" "Just a second, she's probably busy with something important."
    "[Name]" "That's okay, I'll wait as long as it takes. ...."
    show sc i_Elijah_5_1 with my_dissolve
    "Willow" "Hi there!"
    "[Name]" "What the..."
    show sc i_Elijah_5_2 with my_dissolve
    "[Name]" "But I was just..."
    "[Name]" "How did you get in here?!"
    "Willow" "Silly, have you forgotten that I'm a fairy?"
    show sc i_Elijah_5_3 with my_dissolve
    "[Name]" "I didn't know fairies could sneak up on you like that."
    "Willow" "People just don't know how to pay attention to what's going on around them."
    "[Name]" "Interesting opinion."
    show sc i_Elijah_5_4 with my_dissolve
    "Willow" "Did you call me for something?"
    "Willow" "You want me to find a magical artifact for you?"
    "[Name]" "I want to get the nectar of a dryad for Elijah Bloom."
    "Willow" "So you're Elijah's friend!"
    show sc i_Elijah_5_5 with my_dissolve
    "Willow" "Hold on one second..."
    "Willow" "I'll be right there!"
    show sc i_Elijah_5_6 with my_dissolve
    "Willow" "Or..."
    "[Name]" "What?"
    "Willow" "You want to see something cool?"
    "[Name]" "Sure I do."
    "Willow" "Then follow me."
    show sc i_Elijah_5_7 with my_dissolve
    "Willow" "So, what do you think?"
    "[Name]" "What do I think?.. About  what?"
    "[Name]" "A pile of books? A ladder? A trunk?"
    show sc i_Elijah_5_8 with my_dissolve
    "Willow" "Wow! You really don't see anything?"
    "Willow" "I'm telling you, people can't see anything around them."
    "Willow" "Your ability to sense magic is no match for ours."
    show sc i_Elijah_5_9 with my_dissolve
    "Willow" "Look..."
    "[Name]" "Whoa... Wow..."
    "[Name]" "(It's like I'm looking into the eyes of the cosmos....)"
    show sc i_Elijah_5_10 with my_dissolve
    "[Name]" "What the hell is that?"
    "Willow" "A wormhole."
    "Willow" "A fairy portal that connects my grove to this world."
    "[Name]" "Your... grove?"
    show sc i_Elijah_5_11 with my_dissolve
    "[Name]" "Sorry, I don't know anything about fairies."
    "Willow" "Oh, those people. I'm not surprised."
    "[Name]" "You're obviously prejudiced against us."
    "Willow" "What makes you say that?"
    show sc i_Elijah_5_12 with my_dissolve
    "Willow" "I'll be right back..."
    "[Name]" "Wait, where are you going?"
    show sc i_Elijah_5_13 with my_dissolve
    "[Name]" "Isn't that dangerous?"
    "Willow" "Hee hee hee! You're so silly..."
    show sc i_Elijah_5_21 with my_dissolve
    "[Name]" "Wait a minute!"
    "[Name]" "{i}(Who does that?!){/i}"
    "[Name]" "And what kind of weird magic is this?"
    show sc i_Elijah_5_14 with my_dissolve
    "[Name]" "It really is like distant galaxies..."
    "[Name]" "{i}(One thing's for sure, this chest doesn't seem to have a bottom...){/i}"
    "[Name]" "Well, how long do I have to wait here?"
    show sc i_Elijah_5_15 with my_dissolve
    "Willow" "Done!"
    "Willow" "Hi there!"
    "Willow" "You are so impatient."
    "[Name]" "I just wanted to see what was going on."
    show sc i_Elijah_5_16 with my_dissolve
    "Willow" "Here you go!"
    "[Name]" "What's that?"
    "Willow" "What's what? Dryad nectar for your friend."
    "[Name]" "How did you get it... out of there?"
    show sc i_Elijah_5_17 with my_dissolve
    "Willow" "It's my grove."
    "[Name]" "What is this grove of yours?"
    "Willow" "Every fairy has a grove that is born and grows with her."
    "Willow" "My retreat."
    "[Name]" "Like your own personal dimension? Cool! Can I see it?"
    show sc i_Elijah_5_18 with my_dissolve
    "Willow" "Huh... I'd show you, but it's very personal..."
    "[Name]" "Why?"
    "Willow" "The fairies only invite their chosen ones into the grove."
    "Willow" "The ones they want to trust to pick their flower..."
    "[Name]" "Sorry, I didn't mean...."
    show sc i_Elijah_5_19 with my_dissolve
    "Willow" "It's okay!"
    "Willow" "I'm just fooling around with you, [Name]. You're cute."
    "Willow" "Tell Elijah I said hi!"
    show sc i_Elijah_5_20 with my_dissolve
    "[Name]" "Wait...."
    "[Name]" "{i}(She's so nimble!){/i}"
    return