



label jacob_events_label:


    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.5)

    $ set_now = jacob_events_set
    menu:

        "Samantha's problem" if Q_Samantha==2:

            call Samantha_3_label from _call_Samantha_3_label

            $ log_message.update({"QLOG_Samantha":3})

            $ Q_Samantha=3
        "Talk to Jacob" if Q_Jacob == 0:

            call Jacob_1_label from _call_Jacob_1_label
            $ p_up('Jacob', 1)
            $ log_message.update({"QLOG_Jacob":1 })
            $ Q_Jacob=1

            $ change_location_2(location_now, time_now +1)
        "Dueling Club" if Q_Jacob == 1:

            if Q_Victoria < 5:

                call Jacob_1_1_label from _call_Jacob_1_1_label

                $ log_message.update({"QLOG_Jacob":1 })
                $ jacob_events_set.append("Dueling Club")
                $ wakeup_sets.append([

                
                jacob_events_set, "Dueling Club"
                
                
                    ])
            elif True:


                call Jacob_2_label from _call_Jacob_2_label
                $ p_up('Jacob', 2)
                $ log_message.update({"QLOG_Jacob":2 })
                $ Q_Jacob=2


                $ change_location_2(location_now, time_now +1)
        "Dueling Club" if Q_Jacob > 1:
            $ log_message.update({"QLOG_Jacob":3 })
            jump test_duel_game_menu
            $ change_location_2(location_now, time_now +1)
        "Not now" if True:
            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label





label Samantha_3_label:

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

    show sc i_Jacob_0_7 with Dissolve(.5)
    "[Name]" "Mr. Frollo, may I have a moment of your time?"
    show sc i_Jacob_0_8 with my_dissolve
    "Jacob" "Be quick, I'm a busy man."
    "Jacob" "Come on, [Surname], spit it out."
    "Jacob" "I've got my hands full."
    "[Name]" "{i}(So how do I get him on the right topic without names...){/i}"
    "Jacob" "Well?"
    show sc i_Jacob_0_5 with my_dissolve
    "[Name]" "Yesterday a third-year student told us that magic can be exhausted."
    "Jacob" "What? What exactly was he saying?"
    show sc i_Jacob_0_7 with my_dissolve
    "[Name]" "He was telling us that a student from another school was getting sore hands."
    "[Name]" "When he was doing magic."
    "[Name]" "And then he lost the ability to do complex spells. At all."
    "[Name]" "Could that possibly be true?"
    show sc i_Jacob_0_10 with my_dissolve
    "Jacob" "Hmm. I've heard of such symptoms, but..."
    "Jacob" "Why, are you experiencing something similar?"
    show sc i_Jacob_0_7 with my_dissolve
    "[Name]" "No, not really. It's a story."
    "[Name]" "I'm just scared, to be honest."
    show sc i_Jacob_0_4 with my_dissolve
    "Jacob" "Don't get any ideas, [Surname]. These things don't just happen."
    "Jacob" "Is that all you wanted?"
    "Jacob" "I have better things to do than dispel student myths."
    show sc i_Jacob_0_3 with my_dissolve
    "[Name]" "Wait a minute!"
    "[Name]" "It's important for me to know what makes it happen. And how to treat it."
    show sc i_Jacob_0_8 with my_dissolve
    "Jacob" "You seem very interested in the subject, [Surname]."
    show sc i_Jacob_0_7 with my_dissolve
    "[Name]" "Curiosity and hypochondria are my greatest enemies."
    "[Name]" "I want to make sure this doesn't happen to me."
    "[Name]" "Otherwise I won't be able to sleep."
    show sc i_Jacob_0_8 with my_dissolve
    "Jacob" "You're not a convincing liar, Mr. [Surname]."
    "Jacob" "No wonder you go to Leonheart."
    "[Name]" "{i}(Damn, no fooling him.){/i}"
    "[Name]" "{i}(What to do?){/i}"
    scene sc i_Samantha_3_1 with Dissolve(.5)
    menu:
        "Read Frollo's mind" if True:
            $ pass
        "Ask politely" if True:
            show sc i_Samantha_3_5 with my_dissolve
            jump Samantha_3_label_43
    show sc i_Samantha_3_2 with my_dissolve
    "Jacob" "{i}(Unintelligible interference){/i}"
    show sc i_Samantha_3_3 with my_dissolve
    "Jacob" "{i}(Do you think you're the first student to have this gift?){/i}"
    "Jacob" "{i}(Getting into teachers' heads with your weak skill is unwise.){/i}"
    "Jacob" "{i}(Mr. [Surname].){/i}"
    "[Name]" "Ah-ah-ah... Damn, that hurt."
    show sc i_Samantha_3_4 with my_dissolve
    "[Name]" "What was that? Your voice in my head..."
    "Jacob" "Reading minds is just one of the skills of mind magic."
    "Jacob" "I hope you've learned your lesson."
    "[Name]" "I have."
    show sc i_Samantha_3_5 with my_dissolve
    "[Name]" "I apologize."
label Samantha_3_label_43:

    "[Name]" "Mr. Frollo, the truth is, I can't tell you what I need this information for."
    "[Name]" "But it's a matter of life and death."
    show sc i_Samantha_3_6 with my_dissolve
    "[Name]" "If you help me, I'll be indebted to you."
    "[Name]" "Please..."
    "Jacob" "Now, that's a whole other conversation."
    show sc i_Jacob_0_8 with my_dissolve
    "Jacob" "Mr. [Surname], are you willing to make a {b}magic pact{/b} with me?"
    "[Name]" "Could you be more specific about what that means?"
    "Jacob" "You say you will be indebted to me, do you not?"
    "Jacob" "In the magical world, such words carry weight."
    "Jacob" "You and I will make a pact, and when the time comes, I will charge you for your service."
    show sc i_Jacob_0_7 with my_dissolve
    "[Name]" "And what happens to the one who breaks the contract?"
    show sc i_Jacob_0_8 with my_dissolve
    "Jacob" "Are you such a one?"
    "[Name]" "Of course not. But I wonder..."
    show sc i_Jacob_0_6 with my_dissolve
    "Jacob" "{b}His magic will be sealed forever.{/b}"
    show sc i_Samantha_3_7 with my_dissolve
    "[Name]" "All I ask is that you share your knowledge as a student teacher..."
    "Jacob" "Ah, excuse me."
    "Jacob" "It seemed to me that you were in urgent need of information that only I have."
    "Jacob" "But if you just wanted to learn, wait until your third year."
    "Jacob" "That's when we're going to go over this topic."
    show sc i_Samantha_3_8 with my_dissolve
    "Jacob" "Now don't waste my time."
    "[Name]" "Wait a minute."
    "[Name]" "I'm going to regret this."
    show sc i_Samantha_3_9 with my_dissolve
    "[Name]" "I agree."
    "Jacob" "Information for a favor. Let's shake on it."
    "Jacob" "That's great."
    "Jacob" "It's always nice to know an up-and-coming mage owes you a favor."
    show sc i_Jacob_0_1 with my_dissolve
    "[Name]" "If you say so. Now, please answer my questions."
    show sc i_Jacob_0_2 with my_dissolve
    "Jacob" "I don't know why you need this information so urgently."
    "Jacob" "But the symptoms you describe are consistent with..."
    "Jacob" "{b}...a ruptured magical ligament.{/b}"
    show sc i_Jacob_0_9 with my_dissolve
    "[Name]" "A what?!"
    "[Name]" "Magic ligament rupture? Is that like tearing a muscle?"
    show sc i_Jacob_0_10 with my_dissolve
    "Jacob" "Not exactly. But you get the gist."
    "Jacob" "When the magical ligaments are torn, it is impossible to perform complex spells."
    "Jacob" "The magic cannot stabilize and begins to destroy the sorcerer out of existence."
    show sc i_Jacob_0_9 with my_dissolve
    "[Name]" "This is terrible! Is there nothing you can do?"
    show sc i_Jacob_0_10 with my_dissolve
    "Jacob" "Of course there is. It is an unpleasant but not fatal injury."
    "Jacob" "All you have to do is make a {b}compress of night fairy pollen{/b} and a few herbs."
    "Jacob" "{b}Miss Victoria should have a whole set of them.{/b}"
    show sc i_Samantha_3_8 with my_dissolve
    "[Name]" "Thank you."
    show sc i_Jacob_0_6 with my_dissolve
    "Jacob" "[Surname]. Listen to me carefully."
    show sc i_Jacob_0_5 with my_dissolve
    "[Name]" "I'm sorry, I thought you were done..."
    show sc i_Jacob_0_6 with my_dissolve
    "Jacob" "You're looking for solutions to the consequences when you should be looking for the cause."
    show sc i_Jacob_0_5 with my_dissolve
    "[Name]" "What?"
    show sc i_Jacob_0_6 with my_dissolve
    "Jacob" "Magic ligament rupture doesn't just happen."
    "Jacob" "If you don't want a repeat, find the cause."
    show sc i_Jacob_0_5 with my_dissolve
    "[Name]" "And what could be the cause of such trauma?"
    show sc i_Jacob_0_6 with my_dissolve
    "Jacob" "Magic is unpredictable."
    "Jacob" "One thing I do know is that stirring the magical energy of beings of different essence is very dangerous."
    "Jacob" "It can kill whoever is doing it."
    "Jacob" "Whoever you're looking for answers for is lucky to have gotten away with it."
    show sc i_Jacob_0_5 with my_dissolve
    "[Name]" "What do you mean, \"different essence?\""
    show sc i_Jacob_0_6 with my_dissolve
    "Jacob" "There are different kinds of magic, [Surname]. Humans, pixies, dragons, succubi...."
    "Jacob" "Lots of different races and different magics. It can be very dangerous to mix them."
    show sc i_Jacob_0_9 with my_dissolve
    "[Name]" "Why are you telling me all this, Jacob?"
    show sc i_Jacob_0_10 with my_dissolve
    "Jacob" "You and I made a pact, [Surname]. And I always hold up my end of the bargain."
    show sc i_Jacob_0_9 with my_dissolve
    "[Name]" "Thank you... I have to go."
    "Jacob" "Oh no, Mr. [Surname]. It is I who thank you. Good luck, in your quest."
    return

label Jacob_1_label:

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


    show sc i_Jacob_0_1 with Dissolve(.5)
    "[Name]" "Mr. Frollo, sir! Good evening!"
    show sc i_Jacob_0_2 with my_dissolve
    "Jacob" "Good evening, Mr. [Surname]."
    "Jacob" "What can I do for you?"
    "[Name]" "I was just wondering what you were studying here."
    show sc i_Jacob_0_11 with my_dissolve
    "[Name]" "Is that pattern on the floor magical?"
    "Jacob" "That one? Huh, you're observant."
    "Jacob" "It's a Reverse Sun."
    "Jacob" "The mark of the devil that all magicians worship."
    show sc i_Jacob_0_8 with my_dissolve
    "Jacob" "Remind me..."
    "Jacob" "Have you sold your soul yet, or is this a second semester activity?"
    "[Name]" "A-are you serious?.."
    show sc i_Jacob_0_12 with my_dissolve
    "Jacob" "Ah-ha-ha-ha."
    "Jacob" "Relax. Of course not."
    "Jacob" "It's just a regular drawing."
    show sc i_Jacob_0_10 with my_dissolve
    "Jacob" "We're actually meeting members of the dueling club here."
    show sc i_Jacob_0_9 with my_dissolve
    "[Name]" "The dueling club?"
    show sc i_Jacob_0_10 with my_dissolve
    "Jacob" "The one and only."
    "Jacob" "Students fight anonymously for points for their houses."
    "Jacob" "It's the best way to practice the spells they've learned."
    "[Name]" "Sounds incredibly cool."
    "[Name]" "How do I join you?"
    show sc i_Jacob_0_6 with my_dissolve
    "Jacob" "Not so fast, Mr. [Surname]."
    "Jacob" "A man without experience can have a rough time with us."
    "[Name]" "I can handle it."
    "Jacob" "It would be fun to watch, but there are rules."
    "Jacob" "In order to gain access to duels, you must learn..."
    show sc i_Jacob_1_1 with my_dissolve
    "Gabriella" "Excuse me! Mr. Frollo, good evening."
    "Jacob" "Gabriella, I told you to call me Jacob."
    "Jacob" "Did you want something?"
    "Gabriella" "I learned the spell you were talking about."
    show sc i_Jacob_1_2 with my_dissolve
    "Jacob" "That's wonderful news!"
    "Gabriella" "Is there a sparring session at the club tonight? I'm ready!"
    "Jacob" "That's the spirit! Let me check."
    show sc i_Jacob_1_3 with my_dissolve
    "Gabriella" "Hi there! I'm Gabriella."
    "[Name]" "My name is [Name]. Nice to meet you."
    show sc i_Jacob_1_4 with my_dissolve
    "Gabriella" "Nice to meet you too. Do you want to join the dueling club, too?"
    "[Name]" "Me?{w} Thought I'd find out more about it, yeah."
    "Gabriella" "That's great! I'm looking forward to the first duel."
    "[Name]" "{i}(Hmm, I didn't know the dueling club had such hot chicks...){/i}"
    "[Name]" "{i}(I should probably pay a visit there.){/i}"
    show sc i_Jacob_1_5 with my_dissolve
    "Jacob" "I'm afraid I won't be able to find a match you tonight, Gaby..."
    "Gabriella" "Oh, no. What about him?"
    show sc i_Jacob_1_6 with my_dissolve
    "Jacob" "Mr. [Surname] is hardly ready."
    "[Name]" "I'm..."
    show sc i_Jacob_1_7 with my_dissolve
    "Jacob" "О! I've the perfect match for you, Gaby."
    "Jacob" "Hurry up and get ready for the arena. I'll catch up with you soon."
    show sc i_Jacob_1_8 with my_dissolve
    "Gabriella" "Okay, Mr. Frollo."
    "Gabriella" "Oh, well, I mean... Okay, Jacob."
    show sc i_Jacob_0_8 with my_dissolve
    "Jacob" "As for you, Mr. [Surname]..."
    "Jacob" "First, learn the Combat bolt spell."
    "Jacob" "It's the bare minimum required to join the dueling club."
    "Jacob" "When you're ready to give it a try, come see me."
    "Jacob" "I meet dueling club members here every night."
    "Jacob" "We'll see how you do."
    show sc i_Jacob_1_9 with my_dissolve
    "[Name]" "Thank you."
    "[Name]" "{i}(Arrogant prick...){/i}"
    "[Name]" "{i}(That Gaby was all right...){/i}"
    return


label Jacob_2_label:

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

    show sc i_Jacob_0_1 with Dissolve(.5)
    "[Name]" "Good evening, Mr. Frollo."
    show sc i_Jacob_0_2 with my_dissolve
    "Jacob" "Oh, it's you, Mr. [Surname]."
    "Jacob" "Still trying to become a duelist?"
    show sc i_Jacob_0_1 with my_dissolve
    "[Name]" "You bet I am."
    show sc i_Jacob_0_3 with my_dissolve
    "[Name]" "In fact, I've already learned the Combat Bolt spell."
    "[Name]" "And I'm ready to become the new Cordale champion."
    show sc i_Jacob_0_12 with my_dissolve
    "Jacob" "Huh..."
    "Jacob" "Ha-ha-ha-ha-ha."
    show sc i_Jacob_0_8 with my_dissolve
    "Jacob" "You really are a joker, Mr. [Surname]."
    "Jacob" "Probably want to repeat your friend Samantha's successes."
    show sc i_Jacob_0_9 with my_dissolve
    "[Name]" "And surpass them, too."
    show sc i_Jacob_0_10 with my_dissolve
    "Jacob" "That's very interesting."
    "Jacob" "I commend you on your persistence."
    "Jacob" "Let me tell you how the fights go."
    show sc i_Jacob_0_9 with my_dissolve
    "[Name]" "I'm all ears."
    show sc i_Jacob_0_2 with my_dissolve
    "Jacob" "There are three traditional dueling stances."
    "Jacob" "Boulder, Silk and Blade."
    "Jacob" "At the beginning of each round, you choose a stance."
    "Jacob" "Each stance is superior to one and inferior to the other."
    "Jacob" "This determines which contestant will cast the spell first."
    "[Name]" "Like \"rock, paper, scissors?\""
    show sc i_Jacob_0_3 with my_dissolve
    "Jacob" "What's that?"
    show sc i_Jacob_0_4 with my_dissolve
    "[Name]" "Well, it's a children's game..."
    show sc i_Jacob_0_3 with my_dissolve
    "Jacob" "That's the first I've heard of it. Don't interrupt!"
    show sc i_Jacob_0_6 with my_dissolve
    "Jacob" "If your stance wins, you can choose a spell."
    "Jacob" "Or use elixirs and scrolls. If you have them with you."
    "Jacob" "The duel continues until..."
    "Jacob" "Until one of the contestants falls breathless."
    "[Name]" "What the fuck, Mr. Frollo? Is it possible to get killed here?"
    show sc i_Jacob_0_7 with my_dissolve
    "[Name]" "Is this an academy of magic or a gladiator school?"
    show sc i_Jacob_0_8 with my_dissolve
    "Jacob" "Relax, magic can heal you as well."
    "Jacob" "Besides, I didn't say the duel was to the death."
    "Jacob" "The loser simply falls senseless, having used up all his energy."
    "Jacob" "And we're pretty quick to bring him back to his senses here."
    "[Name]" "It's still kind of weird."
    show sc i_Jacob_0_5 with my_dissolve
    "[Name]" "I'm going to be passed out and someone's going to be doing magic on my body?"
    "[Name]" "I don't like the sound of that."
    show sc i_Jacob_0_6 with my_dissolve
    "Jacob" "Mr. [Surname], I suggest you go and think about it."
    "Jacob" "We don't force anyone into the dueling club."
    "Jacob" "Combat mages are an elite group, and they have no need for insecure weaklings."
    "Jacob" "I'm sure you're not one of those, but I can see that today you're not morally ready."
    "Jacob" "Come back another time when you've thought it over."
    "Jacob" "Come up, name your opponent's department, and we'll go to the arena without further ado."
    "[Name]" "I will. Thank you very much."
    show sc i_Jacob_1_1 with my_dissolve
    "Gabriella" "Jacob, good evening."
    show sc i_Jacob_1_2 with my_dissolve
    "Jacob" "Gaby! Great fight last night. I'm glad you mastered your new move."
    "Gabriella" "I'm shocked it worked out for me. But it was so cool!"
    "Gabriella" "Is there an opponent for me today?"
    "Jacob" "Did you get your strength back so quickly?"
    "Gabriella" "Of course I did."
    show sc i_Jacob_1_8 with my_dissolve
    "Jacob" "Then let's go see what I can offer you."
    "Gabriella" "Uh-huh."
    "[Name]" "{i}(Hmm... If even a pretty little thing like that isn't afraid of the arena...){/i}"
    "[Name]" "{i}(Why am I suddenly worried?){/i}"
    "[Name]" "{i}(I should be able to kick some ass.){/i}"
    return


label Jacob_1_1_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)

    show sc i_Jacob_0_1 with Dissolve(.5)
    "[Name]" "Good evening, Mr. Frollo."
    show sc i_Jacob_0_2 with my_dissolve
    "Jacob" "Oh, it's you, Mr. [Surname]."
    show sc i_Jacob_0_2 with my_dissolve
    "Jacob" "Do you have something to tell me, or are you just passing through?"
    show sc i_Jacob_0_1 with my_dissolve
    "[Name]" "I'd like to try my hand at dueling sooner."
    "Jacob" "Have you learned the spell we spoke of?"
    show sc i_Jacob_0_5 with my_dissolve
    "[Name]" "No, but I'm a fast learner. Just show it to me."
    show sc i_Jacob_0_6 with my_dissolve
    "Jacob" "Mr. [Surname], you' re not getting cocky, are you?"
    "Jacob" "Don't you think I have other things to do?!"
    show sc i_Jacob_0_1 with my_dissolve
    "[Name]" "I was hoping it would be quick..."
    show sc i_Jacob_0_8 with my_dissolve
    "Jacob" "Slow and steady wins the race, mister [Surname]."
    "Jacob" "I can't allow you to duel. Safety rules."
    show sc i_Jacob_0_8 with my_dissolve
    "Jacob" "It was clearly stated that you had to learn a combat spell."
    show sc i_Jacob_0_8 with my_dissolve
    "Jacob" "Please don't take up my time."
    show sc i_Jacob_0_7 with my_dissolve
    "[Name]" "But, Mr. Frollo!"
    show sc i_Jacob_0_6 with my_dissolve
    "Jacob" "This is not up for discussion."
    "Jacob" "If you want to join the club so badly, take Victoria's class."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
