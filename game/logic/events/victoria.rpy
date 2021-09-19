label victoria_events_label:


    call hide_all_main_interfaces from _call_hide_all_main_interfaces_7

    $ set_now = victoria_events_set

    menu:

        "Ask for remedy" if Q_Samantha == 3:

            call Samantha_4_label from _call_Samantha_4_label
            $ p_up('Samantha', 5)
            $ log_message.update({"QLOG_Samantha":4 })
            $ Q_Samantha=4

            hide screen black_tmp_screen_menu


            jump main_interface_label

        "Attend lesson" if Q_Victoria != 5 and Q_Victoria < 10:

            hide screen black_tmp_screen_menu
            with Dissolve(.5)
            if Q_Victoria<1:
                if Q_Elijah<2:

                    call Victoria_1_1_label from _call_Victoria_1_1_label
                    $ Q_Victoria=0.5

                    $ log_message.update({'QLOG_Victoria':1})

                    hide screen black_tmp_screen_menu


                    jump main_interface_label
                elif True:
                    call Victoria_1_label from _call_Victoria_1_label
                    $ Q_Victoria=1
                    $ p_up('Victoria', 2)

                    $ log_message.update({'QLOG_Victoria':2})
            elif Q_Victoria == 1:
                call Victoria_2_label from _call_Victoria_2_label
                $ p_up('Victoria', 3)
                $ Q_Victoria=2

                $ log_message.update({"QLOG_Victoria":3})


            elif Q_Victoria == 2:
                if Q_Leona == 1:
                    call Victoria_3_label from _call_Victoria_3_label
                    $ p_up('Victoria', 4)
                    $ Q_Victoria=3

                    $ log_message.update({"QLOG_Victoria":2 })
                else:

                    call Victoria_1_2_label from _call_Victoria_1_2_label

                    hide screen black_tmp_screen_menu


                    jump main_interface_label
            elif Q_Victoria == 3:

                call Victoria_4_label from _call_Victoria_4_label
                $ p_up('Victoria', 5)
                $ Q_Victoria=4



            elif Q_Victoria == 4:

                call Victoria_5_label from _call_Victoria_5_label
                $ Q_Victoria=5
                $ p_up('Victoria', 6)
            elif Q_Victoria == 7:
                call Victoria_8_label from _call_Victoria_8_label
                $ p_up('Victoria', 8)
                $ Q_Victoria = 8

                #hide screen black_tmp_screen_menu


                #jump main_interface_label
            elif Q_Victoria == 8:
                call Victoria_9_label from _call_Victoria_9_label
                $ p_up('Victoria', 9)
                $ Q_Victoria = 9

                #hide screen black_tmp_screen_menu


                #jump main_interface_label
            elif Q_Victoria == 9:
                call Victoria_10_label from _call_Victoria_10_label
                $ p_up('Victoria', 10)
                $ Q_Victoria = 10

                #hide screen black_tmp_screen_menu


                #jump main_interface_label
            else:



                hide screen main_interface with Dissolve(.5)
                show expression '#000' with Dissolve(.5)
                if renpy.music.get_playing():
                    stop music fadeout 1
                    play music_2 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
                elif renpy.music.get_playing('music_2'):
                    stop music_2 fadeout 1
                    play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
                elif True:
                    stop music_2 fadeout 1
                    play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
                call MagicMiniGameLabel_2 from _call_MagicMiniGameLabel_2
                $ spl_up                = float(score_1+score_2+score_3)/200
                $ spells_up[spellname] += spl_up



                $ ShowMessage(str(spellname)+ '{color=#0F0}{b}+'+str(spl_up)+'{/color}{/b}')
                $ spellname = float(score_1+score_2+score_3)/200
                


                $ ShowMessage(['images/leonheart_mini.png', 'Leonheart points {color=#0F0}{b}+'+str(result_score)+'{/color}{/b}'])
                $ homes['Leonheart']['now'] += int(result_score)
                $ change_location_2(location_now, time_now +1)

                hide screen black_tmp_screen_menu


                jump main_interface_label
        "Practice" if Q_Victoria >= 5:

            hide screen main_interface with Dissolve(.5)
            show expression '#000' with Dissolve(.5)
            if renpy.music.get_playing():
                stop music fadeout 1
                play music_2 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
            elif renpy.music.get_playing('music_2'):
                stop music_2 fadeout 1
                play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
            elif True:
                stop music_2 fadeout 1
                play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
            call MagicMiniGameLabel_2 from _call_MagicMiniGameLabel_2_1 
            $ spl_up                = float(score_1+score_2+score_3)/200
            $ spells_up[spellname] += spl_up

            $ ShowMessage(str(spellname)+ '{color=#0F0}{b}+'+str(spl_up)+'{/color}{/b}')
            $ spellname = float(score_1+score_2+score_3)/200
                



            $ ShowMessage(['images/leonheart_mini.png', 'Leonheart points {color=#0F0}{b}+'+str(result_score)+'{/color}{/b}'])
            $ homes['Leonheart']['now'] += int(result_score)
            $ change_location_2(location_now, time_now +1)

            hide screen black_tmp_screen_menu


            jump main_interface_label

        "Talk to Victoria" if Q_Victoria == 5:

            call Victoria_6_label from _call_Victoria_6_label



            $ Q_Victoria=6
            scene expression '#000' with Dissolve(.5)
            call Victoria_7_label from _call_Victoria_7_label

            $ p_up('Victoria', 7)
            $ Q_Victoria=7

            $ log_message.update({'QLOG_Victoria':4})

            hide screen black_tmp_screen_menu


            $ change_location_2('cord_garden_l', time_now)
            jump main_interface_label
        "Not now" if True:

            hide screen black_tmp_screen_menu
            show screen show_hide_locations_2

            with Dissolve(.5)
            jump main_interface_label


    jump exit_from_event


label Samantha_4_label:

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
    show sc i_Victoria_0_1 with Dissolve(.5)
    "[Name]" "Good afternoon, Miss Lapis. May I have a moment of your time?"
    show sc i_Victoria_0_4 with my_dissolve
    "Victoria " "You seem very modest and polite today. [Surname]."
    "Victoria " "You want something from me, don't you?"
    "[Name]" "{i}(It's amazing, she reads me like an open book...){/i}"
    "Victoria " "So, did I get it right?"
    show sc i_Victoria_0_9 with my_dissolve
    "[Name]" "There's nothing I can hide from you, Miss Lapis."
    "[Name]" "That's why you're Cordale's best teacher."
    show sc i_Victoria_0_5 with my_dissolve
    "Victoria " "I don't care for rude flattery. But I commend you for trying."
    "[Name]" "But it's true! Everyone I've talked to thinks you're the most talented."
    show sc i_Victoria_0_7 with my_dissolve
    "Victoria " "You're certainly better at flattery than witchcraft,[Surname]."
    "Victoria " "Though you have room to grow in both."
    "[Name]" "You are cruel but fair."
    show sc i_Victoria_0_5 with my_dissolve
    "Victoria " "[Name], get to the point. I have plans and I don't want to be late."
    "[Name]" "Miss Lapis. I really need to borrow your {b}night fairy pollen compress{/b}..."
    "Victoria " "That's an interesting request. Why would you need a compress?"
    "Victoria " "And how did a first-year student even hear about them?"
    "[Name]" "Mr. Frollo. He told me about the compress and its properties because..."
    "[Name]" "I really need to help a friend."
    show sc i_Victoria_0_5 with my_dissolve
    "Victoria " "That's a very vague explanation."
    "Victoria " "Would you care to give me one reason to even consider..."
    "Victoria " "...giving you a fairly rare healing drug?"
    "[Name]" "Miss Lapis, I wish I could... But I can't."
    show sc i_Victoria_0_8 with my_dissolve
    "Victoria " "Well, you know where the door is."
    "[Name]" "Victoria, I'm begging you."
    show sc i_Victoria_0_6 with my_dissolve
    "Victoria " "[Name], don't be ridiculous."
    "Victoria " "{i}However you rephrase 'please' it doesn't change the situation.{/i}"
    "Victoria " "You're asking me to give you a rare resource for no reason but cute eyes."
    "[Name]" "So you think my eyes are cute?"
    "Victoria " "Don't waste my time."
    show sc i_Victoria_0_10 with my_dissolve
    "[Name]" "I'm not asking for a compress for myself."
    "[Name]" "One of our faculty students has torn magical ligaments."
    "[Name]" "He can't manage without a compress."
    show sc i_Samantha_4_1 with my_dissolve
    "Victoria " "Why didn't you say so before!"
    "Victoria " "Take me to the injured person, we'll quickly solve his problem and find the cause."
    "[Name]" "No!{w} Wait.{w} I can't take you to him."
    show sc i_Samantha_4_2 with my_dissolve
    "Victoria " "Why not?"
    "[Name]" "I promised I wouldn't betray his secret to the teachers. I won't break my word."
    "Victoria " "Oh, why am I surprised? You're Leonheart's student."
    show sc i_Samantha_4_3 with my_dissolve
    "Victoria " "You know this isn't a joke, don't you?"
    "Victoria " "If you don't find the cause of the ruptured magical ligaments, it could happen again."
    "[Name]" "{i}(What have you gotten yourself into, Sam?){/i}"
    "[Name]" "{i}(I'll have to have a serious talk with her and find out the truth...){/i}"
    "Victoria " "Are you going to run to me every time and waste rare academy resources?"
    show sc i_Samantha_4_4 with my_dissolve
    "[Name]" "No. I will solve this problem. I'll find the reason."
    "Victoria " "You? A first-year student?"
    "Victoria " "Yes. Trust me."
    show sc i_Samantha_4_5 with my_dissolve
    "Victoria " "Yes, you have a lot of confidence. But you have a problem with wisdom..."
    "[Name]" "{i}(This is a failure...){/i}"
    "[Name]" "{i}(We'll have to bring Samantha in.){/i}"
    "[Name]" "{i}(Or find a compress somewhere else.){/i}"
    show sc i_Samantha_4_6 with my_dissolve
    "[Name]" "{i}(At least it looks good.){/i}"
    "[Name]" "{i}(I didn't waste my time.){/i}"
    show sc i_Samantha_4_7 with my_dissolve
    "Victoria " "But wisdom comes with experience."
    "[Name]" "I don't understand. You're giving me the compress?"
    "Victoria " "And experience comes with mistakes. Go help your friend."
    "[Name]" "Thank you!"
    show sc i_Samantha_4_8 with my_dissolve
    "Victoria " "But promise me that if you don't find the cause of his injury soon..."
    "Victoria " "You will come to me."
    "[Name]" "You have my word, Victoria. Thank you."
    "Victoria " "I believe you."
    "Victoria " "Good luck to you."
    return


label Victoria_1_label:
    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2

    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)
    show sc i_Victoria_1_1 with Dissolve(.5)
    "[Name]" "{i}(I wonder what's going to happen in class today.){/i}"
    show sc i_Victoria_1_1 with my_dissolve
    "Victoria" "Students, the class is about to begin."
    "Victoria" "I welcome you all to a class on the fundamentals of martial magic!"
    "Victoria" "I will teach you to understand what magic is."
    "Victoria" "How to find the sources of magical power."
    "Victoria" "And to use your talents..."
    show sc i_Victoria_1_anim_1 with my_dissolve
    "Victoria" "To bend that power to your will!"
    "Joshi" "Did you see that?"
    "Gabriella" "Wow!"
    show sc i_Victoria_1_31 with my_dissolve
    "Victoria" "Magic is as much a part of the world around us as you or me."
    "Victoria" "But not everyone is given the talent to feel and touch it."
    "Victoria" "To learn new spells and develop your talents..."
    "Victoria" "Wizards must be in synergy with {b}sources of power{/b}."
    "Victoria" "To understand and master their essence!"
    show sc i_Victoria_1_7 with my_dissolve
    "Gabriella" "Excuse me!"
    "Gabriella" "What do you mean, master it?"
    "Gabriella" "There are no details in the textbook."
    show sc i_Victoria_1_8 with my_dissolve
    "Victoria" "Good question, Gabriella!"
    "Victoria" "The textbook doesn't describe how the source of power is mastered."
    "Victoria" "This is because it is different for every magician."
    "Victoria" "There are many techniques for categorizing wizards by sources of power."
    "Victoria" "But none of this is officially recognized by the Ministry of Magic."
    "[Name]" "So not even magic can overcome bureaucracy?"
    "Joshi" "Not bad!"
    show sc i_Victoria_1_16 with my_dissolve
    "Victoria" "Settle down, Mr. [Surname] and Becks."
    "Victoria" "This will be your first practical assignment."
    "Victoria" "Find your source of power."
    "Gabriella" "But how? Where do you usually start your search?"
    show sc i_Victoria_1_12 with my_dissolve
    "Victoria" "There are sources of power all around you!"
    "Victoria" "And experienced wizards are capable of mastering any element and any power."
    "Victoria" "As for the newbies..."
    show sc i_Victoria_1_15 with my_dissolve
    "Victoria" "More often than not, a magician's talents lie in one thing."
    "Victoria" "And the easiest place to start is with this thing."
    "Victoria" "Your source of power is closely connected with your personality."
    "Victoria" "Look inside yourself, remember what you were always close to."
    "Victoria" "Often it might be some element of nature."
    show sc i_Victoria_1_4 with my_dissolve
    "Victoria" "For example, I started with fire."
    "Victoria" "I remember from my childhood the bright sparks of the fireplace in my parents' house."
    "Victoria" "The warmth of campfires when we went camping."
    show sc i_Victoria_1_34 with my_dissolve
    "Victoria" "How I laughed when my uncle's dragon spewed flames on command!"
    "Victoria" "And at your age I found my element in remembering that."
    "Gabriella" "What a beautiful story..."
    "[Name]" "Perhaps you can give me a hint?"
    "[Name]" "I want to discover my source soon!"
    show sc i_Victoria_1_26 with my_dissolve
    "Victoria" "Don't rush yourself, Mr. [Surname]."
    "Victoria" "And guys, always remember."
    "Victoria" "There's nothing more dangerous than magic that's out of control."
    "Victoria" "And more often than not, it's harmful to its owner."
    show sc i_Victoria_1_24 with my_dissolve
    "Victoria" "So don't be in any hurry when choosing a source of power."
    "Victoria" "Find it in yourself, and only then look around you."
    "[Name]" "{i}(Either it's been too long since I've been to a lecture.){/i}"
    "[Name]" "{i}(Or Victoria is really very wise...){/i}"
    show sc i_Victoria_1_4 with my_dissolve
    "Victoria" "I think a week is enough for you to find your source."
    "Victoria" "That's enough for today, I don't want you to get distracted from this task."
    "Victoria" "I wish you all the best of luck!"
    return



label Victoria_2_label:
    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)
    show sc i_Victoria_1_5 with Dissolve(.5)
    "Victoria" "Today's lesson is about the nature of magic."
    "Gabriella" "What about sources of power?"
    "[Name]" "{i}(Has anyone found their source of power yet?){/i}"
    "[Name]" "{i}(I'm not the only one who's stumped...){/i}"
    show sc i_Victoria_1_3 with my_dissolve
    "Victoria" "Unfortunately not all students have already found their source of power."
    "Victoria" "But that's okay."
    "Victoria" "Like I said, don't rush yourself. It's dangerous!"
    show sc i_Victoria_1_33 with my_dissolve
    "Victoria" "Open the textbook Fundamentals of Magic, page 16."
    "Victoria" "Lecture topic: The nature of magic."
    "Victoria" "You already know that magic is part of the nature around us."
    show sc i_Victoria_1_31 with my_dissolve
    "Victoria" "But magic has one peculiarity: it is the only matter that..."
    "Victoria" "permeates all worlds, not just ours."
    "Victoria" "It is not subject to the specific laws of one world's physics and chemistry."
    "Victoria" "It makes it possible to change the natural course of events."
    "[Name]" "Sounds too good to be true."
    show sc i_Victoria_1_24 with my_dissolve
    "Victoria" "You're right! You should look for a catch in everything."
    "Victoria" "Magic is a very fluid, changeable and capricious matter."
    "Victoria" "To do real spells, not petty tricks..."
    "Victoria" "You have to have the utmost concentration and dexterity."
    "Victoria" "Otherwise your own power can destroy you."
    menu:
        "Be terrified" if True:
            $ pass
        "Boast" if True:
            jump Victoria_2_label_32

    show sc i_Victoria_1_22 with my_dissolve
    "[Name]" "Destroy you?{w} That's horrible!"
    "[Name]" "{i}(Go to Cordale, they said... Being a wizard is fun, they said...){/i}"
    show sc i_Victoria_1_24 with my_dissolve
    "Victoria" "Mr. [Surname], stop your pussyfooting!"
    "Victoria" "If you really care that much: attend my classes more often."
    "Victoria" "The teachers at Cordale are there to guide your learning."
    "Victoria" "In an effective and safe way."
    "[Name]" "I have plenty of reasons to take your classes as it is, Victoria."
    show sc i_Victoria_1_39 with my_dissolve
    "[Name]" "{i}(At least two of those good reasons!){/i}"
    jump Victoria_2_label_44

label Victoria_2_label_32:
    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)
    show sc i_Victoria_1_25 with my_dissolve
    "[Name]" "Pfft, what do I care?"
    "[Name]" "No spell can break my will."
    "Victoria" "Oh, you're very presumptuous, Mr. [Surname]."
    "Victoria" "Even the greatest wizards can stumble."
    "Victoria" "And your potential has yet to be discovered..."
    "[Name]" "I'm quite sure of myself."
    show sc i_Victoria_1_27 with my_dissolve
    "Victoria" "That's commendable."
    "Victoria" "But confidence is better when it's backed up by knowledge."
    "Victoria" "Attend classes more often and you really won't be in any danger."
    "Victoria" "The teachers at Cordale are here to guide your learning."
    "Victoria" "In an effective and safe way."
    show sc i_Victoria_1_39 with my_dissolve
    "[Name]" "Absolutely! I always look forward to your classes, Victoria."
label Victoria_2_label_44:
    hide screen main_interface

    show sc i_Victoria_1_39 with my_dissolve
    "[Name]" "{i}(I wonder if that's her natural size?){/i}"
    "[Name]" "{i}(Or is there a bit of magic involved?){/i}"
    show sc i_Victoria_1_4 with my_dissolve
    "Victoria" "Well and good, then let's get back to the lesson."
    "Victoria" "Wizards and certain creatures can manipulate magic."
    "Victoria" "And use it to change the matter of the world."
    "Victoria" "This ability is innate."
    show sc i_Victoria_1_5 with my_dissolve
    "Victoria" "People first began to notice their ability to do magic a long time ago."
    "Victoria" "For centuries, magic was not controlled in any way."
    "Victoria" "And quite a bit of it was made public."
    "Victoria" "Which led to the persecution and extermination of magicians."
    show sc i_Victoria_1_35 with my_dissolve
    "Victoria" "Fortunately, this stopped before the first written sources appeared."
    "Victoria" "It is now accepted around the world that magic is kept secret from non-magicians."
    "Victoria" "And it is not used to influence secular society."
    show sc i_Victoria_1_1 with my_dissolve
    "Victoria" "But you will study this in more detail in the history of magic."
    "Victoria" "And that's all for today."
    "Victoria" "Your homework remains the same: Find your source of power."

    return



label Victoria_3_label:
    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2

    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)

    show sc i_Victoria_1_1 with Dissolve(.5)
    "Victoria" "Class, attention!"
    "Victoria" "The lesson is about to begin."
    "Victoria" "Today's topic: Mastering the source of power."
    "Victoria" "Would anyone like to talk about their progress?"
    show sc i_Victoria_1_17 with my_dissolve
    "Victoria" "How about you, Mr. [Surname]?"
    "[Name]" "Who? Me?"
    "Victoria" "Yes. You."
    "Victoria" "So, have you found your source of power?"
    show sc i_Victoria_1_13 with my_dissolve
    "[Name]" "{i}(It's about time I showed the power Leona gave me!){/i}"


    menu:
        "Answer modestly" if True:
            $ pass
        "Answer confidently" if True:
            jump Victoria_3_label_18

    show sc i_Victoria_1_22 with my_dissolve
    "[Name]" "I'm not 100%% sure...{w} But I think I have."
    "Victoria" "More Courage!"
    "[Name]" "...I mean..{w} I have. I have!"
    "[Name]" "I think I can control the source of power."
    show sc i_Victoria_1_18 with my_dissolve
    "Victoria" "Come on! Be brave!"
    jump Victoria_3_label_22
label Victoria_3_label_18:


    show sc i_Victoria_1_18 with my_dissolve
    "[Name]" "Of course. What did you expect?"
    "Victoria" "You sound pretty confident in yourself."
    "Victoria" "That's commendable."
    show sc i_Victoria_1_14 with my_dissolve
    "[Name]" "It's only natural."
label Victoria_3_label_22:



    show sc i_Victoria_1_14 with my_dissolve
    "Victoria" "Tell me, what is the source of your strength?"
    "[Name]" "This may sound rather unusual."
    "[Name]" "But none of the elements of nature fit me."
    show sc i_Victoria_1_35 with my_dissolve
    "Victoria" "Yes?"
    "Victoria" "So what did you do?"
    "Victoria" "You found another solution?"
    show sc i_Victoria_1_23 with my_dissolve
    "[Name]" "Exactly."
    "Victoria" "Tell me."
    "[Name]" "I don't know exactly what it is."
    "[Name]" "But it's a burning feeling inside."
    "[Name]" "The desire to be first."
    show sc i_Victoria_1_35 with my_dissolve
    "Victoria" "I wonder..."
    "Victoria" "You're not an athlete by any chance, are you?"
    "[Name]" "How did you know that?!"
    "Victoria" "Oh, it all makes sense to me then."
    show sc i_Victoria_1_27 with my_dissolve
    "Victoria" "It's the power of motivation."
    "Victoria" "Athletes have been motivated by achievement since childhood."
    "Victoria" "No wonder that's the path closest to you."
    show sc i_Victoria_1_14 with my_dissolve
    "[Name]" "{i}(Whew... Good thing it worked out...){/i}"
    "[Name]" "{i}(If it weren't for my past...){/i}"
    "[Name]" "{i}(It would have been hard for me to explain Leona's ″gift.″){/i}"
    show sc i_Victoria_1_18 with my_dissolve
    "Victoria" "Well done, [Name]."
    "Victoria" "Keep looking for sources of power."
    "Victoria" "It will help you feel your magic better."
    "[Name]" "Thank you for the advice."
    show sc i_Victoria_1_1 with my_dissolve
    "Victoria" "Anyone else wants to tell me about their source?"
    "Joshi" "Yesterday, as I was roasting marshmallows on the fire, it hit me...."
    show sc i_Victoria_1_11 with my_dissolve
    "Victoria" "Wait...Were you roasting marshmallows on academy grounds?"
    "Victoria" "Interesting!"
    "Victoria" "Tell me more about that!"
    show sc i_Victoria_1_1 with my_dissolve
    "After a long and uninteresting story about roasting marshmallows."
    "Victoria" "Oops! I totally lost track of the time."
    "Victoria" "Thank you all for your attention."
    "Victoria" "That's the end of our lesson for today!"
    return



label Victoria_4_label:
    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2

    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)
    show sc i_Victoria_1_1 with Dissolve(.5)
    "Victoria" "Class, attention! Class is about to begin."
    "Victoria" "Today you and I will learn how to use the energy of a power source."
    "Victoria" "To create a simple projectile of magical energy."
    "Victoria" "To form a spell out of magical matter."
    show sc i_Victoria_1_2 with my_dissolve
    "Victoria" "Your task: to clearly visualize the result."
    "Victoria" "The form, the properties and all the characteristics of the spell."
    "Victoria" "The more complex the magic, the harder it is to exactly achieve the desired result."
    show sc i_Victoria_1_3 with my_dissolve
    "Victoria" "To do this, we start with your source of power."
    "Victoria" "Concentrating on it, start imagining how you change it."
    "Victoria" "To begin, imagine something simple: the shape of a ball."
    "Victoria" "A smooth ball of concentrated magical power."
    "Victoria" "Nourished by the nature of your source."
    show sc i_Victoria_1_7 with my_dissolve
    "Gabriella" "Excuse me!"
    "Victoria" "Yes?"
    "Gabriella" "And if my source of power is heavily tangible..."
    "Gabriella" "How do you concentrate it into such a rigorous form?"
    show sc i_Victoria_1_8 with my_dissolve
    "Victoria" "That's a good question."
    "Victoria" "You know what the problem with all Cordale freshmen is?"
    "Victoria" "You guys think in terms of the physics of our world."
    "Victoria" "And that's okay, because you grew up here and studied here."
    "Victoria" "But magic isn't one world."
    "Victoria" "And it's not limited by the rules of our universe."
    "Victoria" "In order to create a true miracle..."
    "Victoria" "You have to make yourself forget those rules."
    show sc i_Victoria_4_anim_1 with my_dissolve
    "Victoria" "Look: right now there is just air in the palm of my hand."
    "Victoria" "Thanks to the source of power in the air, I begin to draw energy."
    "Victoria" "And I hold in my head a perfectly straight ball."
    "Victoria" "While the ball is forming I keep in my mind all the time..."
    "Victoria" "The balloon, the gust of wind, the jolt."
    "Victoria" "It's very simple, isn't it?"
    "Victoria" "I use magic to enclose the gust of wind into a ball."
    "Victoria" "Strengthening the properties of the element, but not changing them."
    "Victoria" "It's simple magic, easy to learn."
    "Victoria" "Even an ogre would be knocked unconscious by such a projectile."
    show sc i_Victoria_1_17 with my_dissolve
    "Victoria" "I hope everyone understands how it works."
    "Victoria" "By the next session, I want all of you to be able to create one!"
    "Victoria" "At least for a few seconds."
    show sc i_Victoria_1_26 with my_dissolve
    "Victoria" "So practice more often."
    "Victoria" "Every time you try, it will get easier and easier!"
    "Victoria" "Trust me."
    "Victoria" "Class dismissed."
    return


label Victoria_5_label:
    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2

    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)
    show sc i_Victoria_1_1 with Dissolve(.5)
    "Victoria" "Class is starting!"
    "Victoria" "Class! Turn to page 42 of the Magic Fundamentals textbook."
    "Victoria" "Topic: Defensive and Attack Spells."
    show sc i_Victoria_1_40 with my_dissolve
    "[Name]" "What's going on there? Is she looking for a book?"
    "[Name]" "{i}(What are you looking at, Joshie?){/i}"
    show sc i_Victoria_1_42 with my_dissolve
    "[Name]" "I can't blame you, though."
    "[Name]" "{i}(She's got a great ass and she's twirling it right in front of your nose...){/i}"
    show sc i_Victoria_1_41 with my_dissolve
    "[Name]" "{i}(I think the hem of her dress is a little bit pulled up.){/i}"
    "[Name]" "{i}(Joshi, you lucky bastard!){/i}"
    show sc i_Victoria_1_43 with my_dissolve
    "[Name]" "{i}(I bet it's a great view.){/i}"
    "[Name]" "{i}(Damn!){/i}"
    "[Name]" "{i}(How can I concentrate on my studies with this?!){/i}"
    show sc i_Victoria_1_4 with my_dissolve
    "Victoria" "As you already know, the nature of magic allows it to change its properties."
    "Victoria" "And the properties of the objects it interacts with."
    "Victoria" "This has many uses."
    "Victoria" "But the more complex and unusual a property is for an object."
    show sc i_Victoria_1_5 with my_dissolve
    "Victoria" "The harder it is to create it with magic."
    "Victoria" "For example: it's easy to create a magic projectile."
    "Victoria" "But it's much harder to make in into real fireball."
    show sc i_Victoria_1_2 with my_dissolve
    "Victoria" "Remember when we studied magic projectiles?"
    "Victoria" "Using a balloon as an example."
    "Victoria" "By adding the right emotion and presenting the right property..."
    "Victoria" "You can change it to suit your needs."
    show sc i_Victoria_1_1 with my_dissolve
    "Victoria" "Next time, we're going to practice..."
    "Victoria" "...in creating the {b}Combat Bolt{/b}!"
    "Victoria" "This simple combat spell is in every wizard's arsenal."
    show sc i_Victoria_1_5 with my_dissolve
    "Victoria" "There will be some practical exercises..."
    "Victoria" "...similar to your entrance exam."
    "[Name]" "{i}(It looks like it's going to be interesting.){/i}"
    show sc i_Victoria_1_4 with my_dissolve
    "Victoria" "Well? Glad you're about to learn your first spell?"
    "Joshi" "You bet!"
    "Victoria" "That's good!"
    show sc i_Victoria_1_17 with my_dissolve
    "Victoria" "By the way, {b}you can join our dueling club with this spell{/b}."
    "Victoria" "That's the end of the lesson."
    show sc i_Victoria_1_23 with my_dissolve
    "Victoria" "If you need any more help learning the spell..."
    show sc i_Victoria_1_24 with my_dissolve
    "Victoria" "...feel free to consult me."
    return



label Victoria_6_label:

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
    show sc i_Victoria_0_1 with Dissolve(.5)
    "[Name]" "Miss Lapis!"
    "[Name]" "Just wanted to thank you for the lessons."
    show sc i_Victoria_0_2 with my_dissolve
    "[Name]" "It was very productive."
    show sc i_Victoria_0_3 with my_dissolve
    "Victoria" "Was it?"
    "[Name]" "Yes, of course it has!"
    "[Name]" "I feel like I'm growing every day."
    "Victoria" "It's nice to hear that."
    show sc i_Victoria_0_9 with my_dissolve
    "[Name]" "I would like to understand exactly how to create a Combat bolt."
    "[Name]" "I can imagine the ball and stretch it out..."
    "[Name]" "But how do I fill it with my source of power?"
    show sc i_Victoria_0_7 with my_dissolve
    "Victoria" "That's an interesting way to look at it, Mr. [Surname]."
    "Victoria" "But you're getting way ahead of yourself."
    "Victoria" "Advanced spells effectively combine different magic."
    "Victoria" "And they can have several natures at once."
    show sc i_Victoria_0_3 with my_dissolve
    "Victoria" "But a Combat Bolt is a pure projectile of kinetic energy."
    "Victoria" "A beginner can't turn it into a fireball just by adding fire."
    "Victoria" "You're just starting out, so take your time mastering everything."
    show sc i_Victoria_0_7 with my_dissolve
    "Victoria" "Focus on the first step."
    "Victoria" "And stretch your ball of energy into projectile form."
    "Victoria" "Believe me, it's not practical for everyone either."
    "Victoria" "But get it right once and you'll remember it forever."
    show sc i_Victoria_0_9 with my_dissolve
    "[Name]" "So that's how it is."
    "[Name]" "Now I get it. Thank you."
    "Victoria" "No problem."
    show sc i_Victoria_0_4 with my_dissolve
    "Victoria" "I'm glad to see I was wrong about you, Mr. [Surname]."
    "[Name]" "А? Huh?"
    "Victoria" "I was pretty prejudiced against you after I met you."
    "Victoria" "But it turns out you're more than just sharp-tongued."
    "Victoria" "Your zeal to study my subject is evident to the naked eye."
    "[Name]" "Wait a minute..."
    "[Name]" "Ms. Lapis, why were you prejudiced against me?"
    "[Name]" "What did I do to you?"
    show sc i_Victoria_0_3 with my_dissolve
    "Victoria" "I don't know. A gut feeling."
    "Victoria" "{i}(Maybe it's the strange nature of his source of power...){/i}"
    "[Name]" "{i}(Wow! I could hear her thoughts!){/i}"
    "[Name]" "{i}(My source of power?){/i}"
    "[Name]" "{i}(So she felt Leona's influence after all, right?){/i}"
    show sc i_Victoria_0_7 with my_dissolve
    "Victoria" "Anyway, what I meant to say was that it's in the past."
    "Victoria" "That's all. You can go now."
label Victoria_6_label_42:
    menu:
        "Thank you" if True:
            scene sc i_Victoria_0_9 with Dissolve(.5)
            "[Name]" "Miss Lapis, thank you!"
            "[Name]" "I really love your subject matter."
            "[Name]" "And with your advice, it's not hard at all to get good results!"
            jump Victoria_6_label_62
        "Flirt" if True:
            scene sc i_Victoria_0_9 with Dissolve(.5)

            "[Name]" "Miss Lapis, thank you for your kind words!"
            "[Name]" "When I'm in your classes I feel such a rush of energy..."
            "[Name]" "I can do any kind of magic."
            scene sc i_Victoria_0_4 with Dissolve(.5)

            "[Name]" "And not only magic."
            "[Name]" "That must be your great talent as a teacher."
            "[Name]" "{i}(Or even two talents.){/i}"
            jump Victoria_6_label_62
        "Check out her legs" if not hasattr(store, 'tmp_del_br_2'):
            $ tmp_del_br_2 =True
            show sc i_Victoria_0_11 with my_dissolve
            "[Name]" "{i}(Wow, her legs are so sexy in those stockings...){/i}"

            "[Name]" "{i}(Is it even legal to be a teacher when you are this hot?){/i}"
            show sc i_Victoria_0_12 with my_dissolve
            "[Name]" "{i}(How can a simple man concenctrate on study beholding these...){/i}"
            "[Name]" "{i}(Will you step on me for a wrong answer, miss?){/i}"
            "[Name]" "{i}(I should stop staring before it gets too wierd...){/i}"
            jump Victoria_6_label_42
        "Check out her breasts" if not hasattr(store, 'tmp_del_br_1'):
            $ tmp_del_br_1 =True
            show sc i_Victoria_0_13 with my_dissolve
            "[Name]" "{i}(Oh my...){/i}"

            "[Name]" "{i}(Why would my eyes stop on her magnificent breasts?){/i}"
            show sc i_Victoria_0_14 with my_dissolve
            "[Name]" "{i}(I can't turn away from this beauty...){/i}"
            "[Name]" "{i}(But she'll notice my creepy stare.){/i}"
            "[Name]" "{i}(MUST. NOT. LOOK. AT. BOOBS.){/i}"
            jump Victoria_6_label_42

    jump Victoria_6_label_62


label Victoria_6_label_62:
    if hasattr(store, 'tmp_del_br_2'):
        $ del tmp_del_br_2
    if hasattr(store, 'tmp_del_br_1'):
        $ del tmp_del_br_1
    hide screen main_interface

    show sc i_Victoria_0_2 with my_dissolve

    "Victoria" "All right, [Name], stop flattering me."

    "Victoria" "Instead, you can help me with something."

    "[Name]" "Sure, how can I be useful, miss?"
    show sc i_Victoria_0_7 with my_dissolve
    "Victoria" "I have few overdue books I need to return to the library."
    "Victoria" "Would you carry them?"

    "[Name]" "No problem."
    "[Name]" "Great! Wait here."

    return

label Victoria_1_1_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)
    show sc i_Victoria_0_3 with Dissolve(.5)
    "Victoria" "Wait, Mr. [Surname], where are you going?"
    "[Name]" "To your basic magic class, of course."
    show sc i_Victoria_0_7 with my_dissolve
    "Victoria" "Not so fast."
    "Victoria" "Do you already {b}have your books{/b}?"
    "[Name]" "Well..."
    "[Name]" "Do you need them to listen and absorb knowledge?"
    show sc i_Victoria_0_4 with my_dissolve
    "Victoria" "That's not how we do things here."
    "Victoria" "{b}Get your books from the library{/b} and come back to class."
    "[Name]" "Okay."

    return


label Victoria_1_2_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)
    show sc i_Victoria_0_3 with Dissolve(.5)
    "Victoria" "Mr. [Surname]. I just gave you an assignment..."
    "Victoria" "Are you telling me that you've already found the source of the power?"
    show sc i_Victoria_0_6 with my_dissolve
    "[Name]" "Not yet, but I thought I'd listen to another lecture."
    "Victoria" "Don't waste your time with my lectures, look for the source of power."
    "[Name]" "I'm not sure I know how to..."
    show sc i_Victoria_0_3 with my_dissolve
    "Victoria" "I can't help you there."
    "Victoria" "Finding the source of power is a personal matter."
    "Victoria" "Good luck to you."

    return




label Victoria_7_label:
    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2

    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)

    scene sc i_Victoria_7_1 with Dissolve(.5)
    "Victoria" "Ugh... I think that's it."
    "[Name]" "{i}Whoa! And that's what you call 'a few books'?{/i}"
    "Victoria" "Uh-huh. Yeah."
    show sc i_Victoria_7_2 with my_dissolve
    "Victoria" "Is this pile too heavy for you, [Name]?"
    "[Name]" "Too heavy? Pfft, of course not, it's nothing."
    "Victoria" "Fine, then take it and follow me."
    "[Name]" "All right."
    show sc i_Victoria_7_3 with my_dissolve
    "[Name]" "I'm right behind you."
    "[Name]" "{i}(Ugh... How many years has she been hoarding the books?){/i}"
    "[Name]" "{i}(My back is about to snap.){/i}"
    show sc i_Victoria_7_4 with my_dissolve
    "[Name]" "{i}(Okay, I have nothing to complain about.){/i}"
    "[Name]" "{i}(I'm doing Miss Lapis a favor.){/i}"
    "[Name]" "{i}(I'm sure I'll get more credit for it.){/i}"
    show sc i_Victoria_7_5 with my_dissolve
    "Victoria" "Keep up, [Surname]."
    "Victoria" "If I'd known you're slower that a frozen snail, I would have used telekinesis."
    "[Name]" "{i}(What the hell? You could have just moved them with magic?){/i}"
    "[Name]" "{i}(Why torture me then?!){/i}"
    "[Name]" "{i}(Wait a minute... Maybe Miss Lapis wants to spend more time with me.){/i}"
    show sc i_Victoria_7_6 with my_dissolve
    "Victoria" "There you go."
    "[Name]" "Excuse me, Miss. I didn't know you were in a hurry."
    "Victoria" "Why wouldn't I be? A teacher at Cordale has a wide range of responsibilities."
    "[Name]" "I'm ashamed to admit it, but I never really thought about it."
    "[Name]" "The students should appreciate you and your work more."
    show sc i_Victoria_7_7 with my_dissolve
    "Victoria" "It's nice to have some gentlemen among the newcomers, [Name]."
    "Victoria" "If it weren't for your vulgar jokes, you'd be my favorite student."
    "[Name]" "If you laughed at them once in a while, you would be my favorite teacher."
    show sc i_Victoria_7_8 with my_dissolve
    "Victoria" "Maybe once in a while you'll be able to make a funny joke..."
    "[Name]" "{i}(Ouch...){/i}"
    "[Name]" "Yeah, I shouldn't put my finger in your mouth."
    "Victoria" "Maybe I like it that way..."
    "[Name]" "{i}(What the...){/i}"
    show sc i_Victoria_7_9 with my_dissolve
    "Victoria" "We're here."
    "Victoria" "Let me get the door for you..."
    scene expression '#000' with Dissolve(.5)
    scene sc i_Victoria_7_10 with Dissolve(.5)
    "Victoria" "Sometimes I'm so jealous of Amelia..."
    "[Name]" "Can you be jealous of anyone? You?!"
    "[Name]" "How so?"
    show sc i_Victoria_7_11 with my_dissolve
    "Victoria" "It's so cozy and beautiful here."
    "Victoria" "And there are so many books around... Can you smell them?"
    "[Name]" "I guess so..."
    show sc i_Victoria_7_12 with my_dissolve
    "Victoria" "That's what knowledge smells like..."
    "[Name]" "{i}(It seems Amelia isn't the only milf who's obsessed with books.){/i}"
    "[Name]" "{i}(I'll keep that in mind.){/i}"
    show sc i_Victoria_7_13 with my_dissolve
    "[Name]" "I totally agree with you. I love this place."
    "Victoria" "You're full of pleasant surprises, [Name]."
    "Victoria" "Come, Amelia must be waiting for me already."
    show sc i_Victoria_7_14 with my_dissolve
    "Victoria" "Amelia, sweetheart, I'm so happy to see you!"
    "Amelie" "Vicki! Have you finished already?!"
    "Victoria" "Well, you know me..."
    "Amelie" "What do you think of Gordo Brax's view on the theory of pegasus and unicorn kinship?"
    "Victoria" "It's fascinating. I never would have found those connections. How does he do it?"
    "Amelie" "I know! He's a genius and such a sweetheart..."
    show sc i_Victoria_7_15 with my_dissolve
    "[Name]" "Ahem, ahem!"
    "[Name]" "Excuse me, Miss Lapis, can I go now?"
    "Victoria" "Of course, [Name]!"
    "Victoria" "Thank you so much for your help."
    "Victoria" "You may go."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label Victoria_8_label:
    $ has_incendio = True
    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2

    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)
    show sc i_Victoria_1_1 with my_dissolve
    "Victoria" "Attention, students! Lesson is starting!"
    "Victoria" "Turn to page 67 of the Magic Fundamentals textbook."
    show sc i_Victoria_1_4 with my_dissolve
    "Victoria" "Todays topic: Advanced Attacking Spells."
    "Victoria" "You've all mastered the Combat Bolt."
    "Victoria" "Now we'll take a look at the more powerful spells."
    show sc i_Victoria_8_1 with my_dissolve
    "Joshi" "Excuse me! Can I ask you a question?"
    "Victoria" "Sure!"
    show sc i_Victoria_8_2 with my_dissolve
    "Joshi" "Why do we need all that?"
    "Joshi" "Don't you think your program is outdated?"
    show sc i_Victoria_8_3 with my_dissolve
    "Victoria" "I'm sorry, I don't understand your question."
    "Victoria" "What do you mean?"
    show sc i_Victoria_8_4 with my_dissolve
    "Joshi" "Why does modern man need destructive combat spells?"
    "Joshi" "We're not in the Middle Ages."
    show sc i_Victoria_8_5 with my_dissolve
    "Joshi" "I don't see why anything more dangerous would be used in a sparring match."
    "Joshi" "And if someone gets drunk, I'm good with a combat bolt."
    show sc i_Victoria_1_34 with my_dissolve
    "Victoria" "Well, you make a good point, Mr. Banks."
    "Victoria" "Indeed, such magic is seldom needed in modern society..."
    show sc i_Victoria_8_6 with my_dissolve
    "Victoria" "However! You're forgetting something."
    "Victoria" "The wizarding world is far more complex and dangerous than you can imagine."
    show sc i_Victoria_1_11 with my_dissolve
    "Victoria" "A battle bolt might be enough for a friendly sparring match."
    "Victoria" 'And it might even save you from the "drunken bastards."'
    "Victoria" "But what will you do if you are attacked by a mournful spirit?"
    "Victoria" "Or does your magical energy attract manpires?"
    show sc i_Victoria_1_5 with my_dissolve
    "Victoria" "You don't have to learn combat spells if you want."
    "Victoria" "But not all creatures are familiar with the pacifism of homosapiens."
    "[Name]" "{i}(Sounds convincing.){/i}"
    show sc i_Victoria_1_4 with my_dissolve
    "Victoria" "I hope I've answered your question."
    "Joshi" "Of course, miss!"
    "Victoria" "All right!"
    show sc i_Victoria_1_44 with my_dissolve
    "Victoria" "Then listen carefully:"
    "Victoria" "The moment you form a sphere in your mind."
    show sc i_Victoria_1_45 with my_dissolve
    "Victoria" "Begin to fill it with the energy of the element of fire."
    "Victoria" "To enhance the effect, the novice may also utter a verbal incantation."
    scene sc i_Victoria_8_7 with Dissolve(.5)
    "Victoria" "{b}Incendio!{/b}"
    "[Name]" "{i}(Is it that simple?){/i}"
    "[Name]" "{i}(I'm sure I can master it easily.){/i}"
    "[Name]" "{i}(I love Victoria's lessons...){/i}"
    show sc i_Victoria_8_6 with my_dissolve
    "Victoria" "Important rule!"
    "Victoria" "Freshmen are not allowed to practice Incendio without the teacher's supervision."
    "Victoria" "The element of fire is hard to curb."
    show sc i_Victoria_1_23 with my_dissolve
    "Victoria" "And burns have never looked good on any student."
    show sc i_Victoria_1_24 with my_dissolve
    "Victoria" "That's it for today!"
    scene image '#000' with Dissolve(.5)
    return

label Victoria_9_label:
    $ has_episkey = True
    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2

    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)

    show sc i_Victoria_1_5 with my_dissolve
    "Victoria" "Greetings, students!"
    "Victoria" "As you all know at this lessons we study Battle Magic."
    "Victoria" "But battle magic is not only about killing, burning and torture."
    "Victoria" "There is another, far more subtle and no less respected art!"
    show sc i_Victoria_1_3 with my_dissolve
    "Victoria" "A wizard who is able to rescue wounded comrades from the battlefield."
    "Gabriella" "Are we going to study healing?"
    "Joshi" "Boo-hoo-hoo!"
    show sc i_Victoria_1_33 with my_dissolve
    "Victoria" "Guys, what's the big deal?"
    "Victoria" "No, Gaby, not really."
    "Victoria" "Healing magic is a whole separate course."
    show sc i_Victoria_1_31 with my_dissolve
    "Victoria" "You'll be able to choose this optional course in your master's degree."
    "Victoria" "There is, however, a range of combat healing magic."
    "[Name]" "Something at the intersection of the two schools, right?"
    "Victoria" "That's right!"
    show sc i_Victoria_1_24 with my_dissolve
    "Victoria" "Today I'm going to teach you how to create a simple healing."
    "Victoria" "But to do so, I will need a volunteer who is not afraid of pain."
    menu:
        "Be silent":
            show sc i_Victoria_9_1 with my_dissolve
            "[Name]" "{i}(I don't want to be a guinea pig.){/i}"
            "Victoria" "What, nobody?"
            show sc i_Victoria_9_2 with my_dissolve
            "Victoria" "Then you go ahead, Mr. Banks."
            "Joshi" "Why me?"
            "Victoria" "Well, you needed to be cheered up, right?"
            "Joshi" "Fuck...Okay."
            show sc i_Victoria_9_3 with my_dissolve
            "Victoria" "All right! Face the class, Mr. Banks."
            "Victoria" "Are you ready?"
            "Joshi"   "For wha...?"
            "Victoria" "{b}Eviscera!{/b}"
            "Joshi" "Ouch! What the hell?!"
            show sc i_Victoria_9_4 with my_dissolve
            "Victoria" "I told you it would sting a little."
            show sc i_Victoria_9_5 with my_dissolve
            "Joshi" "YOU CUT MY FOREHEAD!"
            show sc i_Victoria_9_6 with my_dissolve
            "Victoria" "Don't whine, Mr. Banks. I'll take care of it."
            "Victoria" "The most important thing in healing magic is gentleness."
            "Victoria" "You don't have to stabilize the sphere you represent."
            show sc i_Victoria_9_7 with my_dissolve
            "Victoria" "Let it be soft and fluid, like a balloon filled with water."
            "Victoria" "And now add to it the healing power of nature."
            "Victoria" "It's as if a tree sprouted inside your balloon."
            "Victoria" "And now imagine it bursting."
            show sc i_Victoria_9_8 with my_dissolve
            "Victoria" "And its contents gently rain on the wounds of your target."
            show sc i_Victoria_9_9 with my_dissolve
            "Victoria" "Say the magic incantation: Episkey!"
            "Victoria" "Done."
            show sc i_Victoria_9_10 with my_dissolve
            "Joshi" "Whoa... not a trace! That's cool!"
            "Victoria" "Hope that wasn't boring."
            show sc i_Victoria_9_11 with my_dissolve
            "Victoria" "Have a seat, Mr. Banks."
        "Volunteer":

            show sc i_Victoria_1_24 with my_dissolve
            "[Name]" "{i}( Why wouldn't I? This could be interesting! ){/i}"
            show sc i_Victoria_9_12 with my_dissolve
            "[Name]" "I'm ready to assist you."
            "Victoria" "Never doubted you for a second, Mr. [Surname]."
            show sc i_Victoria_9_13 with my_dissolve
            "Victoria" "Come this way and... Face the class."
            show sc i_Victoria_9_14 with my_dissolve
            "Victoria" "Eviscera!"
            "[Name]" "{i}(Ouch... What's wrong?){/i}"
            show sc i_Victoria_9_15 with my_dissolve
            "[Name]" "{i}(My forehead is in pain.. Is that blood?!){/i}"
            "[Name]" "Is it supposed to be?"
            "Victoria" "Don't worry, Mr. [Surname]."
            "Victoria" "I'll take care of it."
            show sc i_Victoria_9_16 with my_dissolve
            "Victoria" "The most important thing in healing magic is gentleness."
            "Victoria" "You don't need to stabilize the sphere you represent."
            "Victoria" "Let it be soft and fluid, like a balloon filled with water."
            "Victoria" "And now add to it the healing power of nature."
            show sc i_Victoria_9_17 with my_dissolve
            "Victoria" "It's as if a tree sprouted inside your balloon."
            "Victoria" "And now imagine it bursting."
            show sc i_Victoria_9_18 with my_dissolve
            "Victoria" "And its contents gently rain on the wounds of your target."
            show sc i_Victoria_9_19 with my_dissolve
            "Victoria" "Say the magic incantation: Episkey!"
            "Victoria" "Done."
            show sc i_Victoria_9_20 with my_dissolve
            "[Name]" "Whoa... not a trace! Awesome!"
            "Victoria" "Glad you were so impressed!"
    show sc i_Victoria_9_21 with my_dissolve
    "Victoria" "Have a seat."
    show sc i_Victoria_1_23 with my_dissolve
    "Victoria" "And that's all for today."
    show sc i_Victoria_1_24 with my_dissolve
    "Victoria" "We'll practice Episkey more on the next practice lesson."
    scene image '#000' with Dissolve(.5)
    return

label Victoria_10_label:
    $ has_rictusempra = True
    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2

    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)
    show sc i_Victoria_1_5 with my_dissolve
    "Victoria" "Today's lesson is about concussion bolt."
    "Victoria" "More known among students as Rictusempra."
    "Victoria" "It's the empowered version of the usuall combat bolt."
    "Victoria" "That can temporarily stun your target."
    show sc i_Victoria_1_33 with my_dissolve
    "Victoria" "Believe me - this small trick can bedazzle even the most powerful mage."
    "[Name]" "(Sounds like something that can come in handy.)"
    show sc i_Victoria_1_26 with my_dissolve
    "Victoria" "In order to create Rictusempra you need to imagine whirlwind."
    "Victoria" "While whispering the spell itself."
    show sc i_Victoria_1_7 with my_dissolve
    "Gabriella" "Miss Lapis!"
    "Victoria" "Yes, Gabriella?"
    show sc i_Victoria_1_30 with my_dissolve
    "Gabriella" "I was wondering - if this bolt causes concussion.,,"
    "Gabriella" "Is it safe to use in in duels?"
    show sc i_Victoria_1_39 with my_dissolve
    "Victoria" "Good question."
    "Victoria" "Considering your powers and medical treatment we can provide..."
    "Victoria" "I can assure you that it;s 100%% safe for you to use anything we learn here in duels."
    "Gabriella" "Thank you."
    show sc i_Victoria_1_5 with my_dissolve
    "Victoria" "Alright. Class, open page 82. "
    "Victoria" "Let's take a look at the situations where Rictusempra is recommended for use."
    "[Name]" "Fighting giant acid-spitting spiders?!"
    "[Name]" "ARE THERE THINGS LIKE THAT?!"
    show sc i_Victoria_1_34 with my_dissolve
    "Victoria" "The world is a wounderful place. Isn't it?"
    "Victoria" "Except giant spiders, are there any situations that needs loud vocalizing?"
    "[Name]" "No. I'm sorry."
    show sc i_Victoria_1_4 with my_dissolve
    "Victoria" "Good. Now it's time to talk about the history of Rictusempra."
    "[Name]" "In other words, it's time for me to take a nap..."
    return