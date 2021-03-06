label amelie_events_label:


    #hide screen show_hide_locations
    #hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.1)

    $ set_now = amelie_events_set
    menu:

        "Ask about textbooks" if Q_Elijah == 0 and Q_Victoria==0.5:


            hide screen black_tmp_screen_menu
            with Dissolve(.5)
            call Amelie_1_1_label from _call_Amelie_1_1_label
        "1 Spying on Amelie" if Q_Haley == 11:
            call Haley_12_label from _call_Haley_12_label
            $ Q_Haley=12
            $ p_up('Haley', 8)
            $ change_location_2(location_now, time_now+1)
        "Ask about textbooks" if Q_Elijah == 1:

            hide screen black_tmp_screen_menu
            with Dissolve(.5)
            call Elijah_2_label from _call_Elijah_2_label
            $ p_up('Elijah', 3)
            $ Q_Elijah = 2




        "Lost foliants" if Q_Amelie<2 and books_gg:

            hide screen black_tmp_screen_menu
            with Dissolve(.5)
            call Amelie_2_label from _call_Amelie_2_label
            $ p_up('Amelie', 2)
            $ log_message.update({"QLOG_Amelie":2})




        "Talk to Amelie" if Q_Amelie<2 and not books_gg:

            hide screen black_tmp_screen_menu
            with Dissolve(.5)
            call Amelie_1_2_label from _call_Amelie_1_2_label



        "Lost foliants" if Q_Amelie>=2 and books_gg:
            hide screen main_interface
            hide screen black_tmp_screen_menu
            show expression 'images/prologue/19-32/Amelie_2_1.webp'
            $ pass
            with Dissolve(.5)
            $ rtmps = renpy.call_screen('give_book_screen')
            if rtmps:
                $ books_send += rtmps
                $ books_gg   -= rtmps
                $ homes['Leonheart']['now'] += rtmps
                $ ShowMessage(['images/leonheart_mini.png', 'Leonheart points {color=#0F0}{b}+'+str(rtmps)+'{/color}{/b}'])
            $ del rtmps
            hide expression 'main_interface/give_book/give_book_bg.png'
            with Dissolve(.5)
        "Not now" if True:



            #show screen main_interface 
            #show screen show_hide_locations_2
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            hide screen main_interface 
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label
screen my_tmp_skip_screen():
    zorder 200
    imagebutton:
        idle  '#0000'
        hover '#0000'
        action Return('')

label library_event_amelie_1:



    stop music_2 fadeout 1
    play music 'audio_ep2/SC/8. Beautiful people.mp3' fadein 1.0


    hide screen text_animation_up_screen
    hide screen text_animation_up_screen_2
    hide screen text_animation_up_screen_3
    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen main_interface 
    hide screen black_tmp_screen_menu

    $ load_image_now = 'Amelie_1'
    call pre_load_web_image from _call_pre_load_web_image

    scene image 'images/locations_main/'+ str(location_now) + '_' + str(time_now) + '.png'
    with Dissolve(.5)
    show screen my_tmp_skip_screen
    "[Name]" "{i}(Wow! What an impressive library they have!){/i}"

    "[Name]" "{i}(Holy crap!){/i}"
    "[Name]" "{i}(I'm not sure if I've seen that many books in my entire life!){/i}"
    "[Name]" "{i}(And they're all about magic?){/i}"
    "[Name]" "{i}(Unbelievable.){/i}"
    "[Name]" "{i}(Hmm. Weird.){/i}"
    "[Name]" "{i}(There doesn't seem to be a soul here...){/i}"
    show sc i_Amelie_1_2 with my_dissolve
    "[Name]" "Hello?"
    "[Name]" "Hello?!"



    stop music 
    play music_2 'audio_ep2/SC/8. Beautiful people.mp3' fadein 3.0




    play sound_2 'audio/new/Music/intro1.mp3' fadein 1.0

    hide screen my_tmp_skip_screen
    scene sc i_Amelie_1_anim_1 with Dissolve(.5)
    $ renpy.pause(9.96, hard = True)
    show screen my_tmp_skip_screen
    $ renpy.pause(0.96, hard = True)
    "Amelie" "Young man!"


    "[Name]" "{i}(Her legs are really something...){/i}"

    "[Name]" "{i}(Is this the library or faschion show runaway?){/i}"



    "Amelie" "Where are your manners?"


    "Amelie" "Weren't you taught that books like silence?"


    show sc i_Amelie_1_3 with my_dissolve
    "[Name]" "Is that true?"
    "Amelie" "Some fantasy creature books take a nap at this time of day."

    show sc i_Amelie_1_4 with my_dissolve
    "Amelie" "They'll fiercely bite those that disturb their sleep."
    "Amelie" "And that's nothing compared to..."
    "Amelie" "...what I will do to you for violating the rules in the library."
    show sc i_Amelie_1_5 with my_dissolve
    "[Name]" "I'll try to remember that."
    "Amelie" "Good boy."
    "Amelie" "My name is Amelie Earhart."
    "Amelie" "I'm in charge of the Cordale Library."
    show sc i_Amelie_1_6 with my_dissolve
    "Amelie" "And you are...?"
    "[Name]" "[Name] [Surname], Leonheart."
    "[Name]" "What services do you have here?"
    show sc i_Amelie_1_7 with my_dissolve
    "Amelie" "What do you mean?"
    "Amelie" "It's a library."
    show sc i_Amelie_1_8 with my_dissolve
    "Amelie" "Cordale has the largest collection of books on magic and the history of magic."
    "Amelie" "Of course, not all books are available to first year students."
    "Amelie" "Some may be too dangerous."
    show sc i_Amelie_1_9 with my_dissolve
    "Amelie" "And, alas, some {b}folios{/b} are temporarily {b}lost{/b}..."
    "[Name]" "How could that be?"
    show sc i_Amelie_1_12 with my_dissolve
    "Amelie" "Many of our students never return their books."
    "[Name]" "That's very rude."
    show sc i_Amelie_1_13 with my_dissolve
    "Amelie" "But it's not always their fault."
    "Amelie" "These pixies are nothing but trouble!"
    "[Name]" "Pixies?"
    "Amelie" "Students swear that pixies steal their books and other things from their bags."
    show sc i_Amelie_1_14 with my_dissolve
    "Amelie" "And then they scatter our books all over the academy grounds."
    "Amelie" "And the library suffers!"
    "Amelie" "So many interesting works are lost!"
    "[Name]" "Can't they be found?"
    show sc i_Amelie_1_15 with my_dissolve
    "Amelie" "You can. But who's going to do it?"
    "Amelie" "I'm running the library all by myself."
    "[Name]" "Perhaps I could help you, Miss...?"
    "Amelie" "Miss Amelie Erhart."
    "[Name]" "Amelie! Is there any way I can help?"
    "[Name]" "It saddens me to think of good books being lost like that."
    show sc i_Amelie_1_16 with my_dissolve
    "Amelie" "I don't know..."
    "Amelie" "Well, why not?"
    "Amelie" "Bring me all the books you find lying around the Academy grounds."
    show sc i_Amelie_1_17 with my_dissolve
    "Amelie" "I'll gladly {b}reward you with housepoints{/b} for them."
    "[Name]" "Sounds like fun!"
    "[Name]" "It's a deal."
    "[Name]" "I will be more than happy to help you."
    "Amelie" "That's very generous of you, Mr. [Surname]."



    hide screen my_tmp_skip_screen
    $ log_message.update({"QLOG_Amelie":1 })
    $ Q_Amelie=1

            
    #amelie_1_label
    $ p_up('Amelie', 1)
    jump main_interface_label


label Elijah_2_label:
    $ load_image_now = 'Amelie_2'
    call pre_load_web_image from _call_pre_load_web_image_1
    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2


    hide screen main_interface with Dissolve(.5)
    show expression '#000' with Dissolve(.5)

    show sc i_Amelie_2_1 with Dissolve(.5)
    "[Name]" "I would like to get my textbooks."
    "Amelie" "Remind me your name and course."
    "[Name]" "[Name] [Surname], first year. Leonheart."
    show sc i_Amelie_2_2 with my_dissolve
    "..."
    "Amelie" "Yep. There you are."
    show sc i_Amelie_2_3 with my_dissolve
    "Amelie" "Do you have a student card?"
    "[Name]" "This one?"
    "Amelie" "Yeah. Great."
    show sc i_Amelie_2_4 with my_dissolve
    "Amelie" "Let me get your textbooks."
    "[Name]" "..."
    show sc i_Amelie_2_5 with my_dissolve
    "[Name]" "{i}(Oh Cordale, you're so full of surprises.){/i}"
    "[Name]" "{i}(I've never seen a librarian like THAT.){/i}"
    show sc i_Amelie_2_6 with my_dissolve
    "[Name]" "{i}(I wonder how all those ancient folio books don't catch fire from her heat...){/i}"
    "[Name]" "{i}(Maybe she cools them down with her stern gaze.){/i}"
    "[Name]" "{i}(I should visit library more often...){/i}"
    show sc i_Amelie_2_7 with my_dissolve
    "Amelie" "What are you dreaming about?"
    "[Name]" "Me?"
    "[Name]" "Oh, uh..."
    "[Name]" "I'm thinking about my battle-magic lessons."
    "[Name]" "I can't wait!"
    "Amelie" "That's it."
    "Amelie" "I'd recommend a ???From Spark to Fire??? by Ignius of Wales."
    show sc i_Amelie_2_8 with my_dissolve
    "Amelie" "But the last student hasn't brought it back yet."
    "[Name]" "I'll be sure to ask next time."
    "[Name]" "Thank you for the textbooks."
    show sc i_Amelie_2_9 with my_dissolve
    "Amelie" "It's my job."
    "Amelie" "Good luck with learning Cordale, [Surname]."
    "Amelie" "I hope you'll stop by more often."
    "[Name]" "I will!"

    $ log_message.update({"QLOG_Elijah":3})
    $ Q_Elijah=2

    
    $ elijah_view_3 = True
    return


label Amelie_2_label:
    $ load_image_now = 'Amelie_2'
    call pre_load_web_image from _call_pre_load_web_image_2
    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2


    hide screen main_interface with Dissolve(.5)
    show expression '#000' with Dissolve(.5)
    show sc i_Amelie_2_1 with Dissolve(.5)

    "[Name]" "Remember you were talking about the lost folios?"
    "Amelie" "Yes. Textbooks are scattered all over the academy. It's a tragedy."
    show sc i_Amelie_2_3 with my_dissolve
    "[Name]" "I think I found something like that."
    "[Name]" "Here, take a look."
    show sc i_Amelie_2_12 with my_dissolve
    "Amelie" "Let me see that."
    "Amelie" "This is definitely a book from our library."
    show sc i_Amelie_2_10 with my_dissolve
    "Amelie" "Excellent work, [Name]!"

    "Amelie" "I'll give you points."
    show sc i_Amelie_2_13 with my_dissolve
    "Amelie" "As promised, I will reward you for all the books you find."
    "[Name]" "The main reward is hearing your satisfied voice!"
    "[Name]" "{i}(But I won't refuse points either.){/i}"
    show sc i_Amelie_2_9 with my_dissolve
    "[Name]" "And to know that priceless books are in safe hands."

    "Amelie" "It's nice to see a like-minded man."
    "Amelie" "There are few lovers of literature among the young these days."
    show sc i_Amelie_2_8 with my_dissolve
    "[Name]" "{i}(What else to do while confined to bed with a fracture?){/i}"
    "[Name]" "I'm very concerned about the fate of the academy textbooks."
    "[Name]" "So I'll try to find some more!"
    show sc i_Amelie_2_9 with my_dissolve
    "Amelie" "Great!"
    "Amelie" "By the way, [Name], you don't have to carry textbooks one at a time."
    "Amelie" "You can collect several and bring them at once."
    show sc i_Amelie_2_7 with my_dissolve
    "Amelie" "If it's more convenient for you."
    "[Name]" "That's fine."
    "[Name]" "I'll be sure to stop by if I find another textbook."
    "Amelie" "I'll look forward to it."
    if books_gg:
        $ books_gg   -= 1
        $ books_send += 1
    $ Q_Amelie  = 2
    
    
    $ homes['Leonheart']['now'] += 1
    $ ShowMessage(['images/leonheart_mini.png', 'Leonheart points {color=#0F0}{b}+1{/color}{/b}'])




    $ log_message.update({"QLOG_Amelie":1 })
    return


label Amelie_1_1_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)
    show sc i_Amelie_2_1 with Dissolve(.5)

    "[Name]" "I wanted to know about the textbooks."
    "[Name]" "Miss Lapis said she couldn't let me go to class without them."
    show sc i_Amelie_1_15 with my_dissolve
    "Amelie" "That's right. It's academy policy."
    "[Name]" "So I'm here to see you."
    "[Name]" "Give me the first-year textbooks."
    show sc i_Amelie_1_7 with my_dissolve
    "Amelie" "Not so fast."
    "Amelie" "Do you already have a {b}student card?{/b} "
    "[Name]" "No... What is that anyway?"
    show sc i_Amelie_1_8 with my_dissolve
    "Amelie" "It's a student card from our academy."
    "Amelie" "You'll have to {b}go to Elijah{/b}. He's responsible for that."
    "Amelie" "I can't give out textbooks without a student card."
    "[Name]" "{i}(I hate bureaucracy...){/i}"
    "[Name]" "Thank you for the information."

    $ log_message.update({"QLOG_Elijah":1})
    return


label Amelie_1_2_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)
    show sc i_Amelie_1_7 with Dissolve(.5)
    "[Name]" "So, as for the {b}lost folios{/b}..."
    "Amelie" "Have you found anything yet?"
    "[Name]" "Not yet, but I feel I'm on the right track..."
    show sc i_Amelie_1_17 with my_dissolve
    "Amelie" "Keep trying and you will be rewarded as you deserve!"
    "[Name]" "Thanks for the motivation."
    "[Name]" "I won't let you down!"

    $ log_message.update({"QLOG_Amelie":1 })
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
