label sheet_31:
    $ Q_Elijah = 1
    show sc i_1_285 with my_dissolve
    "[Name]" "Sam?"
    "Samantha" "Hey! What's up, buddy?"
    show sc i_1_286 with my_dissolve
    "[Name]" "Just saw our living room."
    "Samantha" "What do you think?"
    "[Name]" "Pretty cozy."
    "[Name]" "Where are you?"
    "Samantha" "Just catching up with an old friend."
    "Samantha" "Checking in on you."
    "Samantha" "[Name]?"
    "[Name]" "What?"
    show sc i_1_287 with my_dissolve
    "Samantha" "I always knew you were a Leonheart!"
    "Samantha" "At least I hoped so."
    "[Name]" "Oh, come on."
    "[Name]" "I might as well be an Adderin."
    "Samantha" "Hey! Don't joke about that!"
    show sc i_1_286 with my_dissolve
    "[Name]" "Okay, okay. Take it easy."
    show sc i_1_287 with my_dissolve
    "[Name]" "Honestly, the ritual took a lot out of me."
    "Samantha" "That's okay."
    "[Name]" "Really?{w} How was your ritual?"
    "Samantha" "That's a weird question."
    show sc i_1_286 with my_dissolve
    "Samantha" "It's just like everyone else's."
    "[Name]" "What're the details?"
    "Samantha" "I found myself in a strange forest."
    "Samantha" "There were four founders."
    "Samantha" "Each of them had a few words for me..."
    show sc i_1_288 with my_dissolve
    "[Name]" "And?"
    "Samantha" "And then three of them left, and Leona invited me to Leonheart."
    "[Name]" "Invited you?"
    "Samantha" "Well, yeah."
    "Samantha" "And she hugged me at the end."
    show sc i_1_286 with my_dissolve
    "[Name]" "So that's it."
    "Samantha" "What's the big deal?"
    "[Name]" "I was just wondering if everyone had the same ritual."
    "[Name]" "Now I know we did."
    show sc i_1_288 with my_dissolve
    "Samantha" "Hmm. I've never wondered how other people's rituals went before."
    "Samantha" "I always said you had an unusual mind!"
    "[Name]" "You didn't usually say that as a compliment."
    "Samantha" "Details..."
    show sc i_1_288 with my_dissolve
    "[Name]" "Shall we meet?"
    "[Name]" "Where are you now?"
    "Samantha" "I'm busy today."
    "Samantha" "And you must be tired after the ritual."
    "Samantha" "Let's meet in the morning."
    "[Name]" "Alright."
    "Samantha" "Get a good night's sleep."
    show sc i_1_286 with my_dissolve
    "[Name]" "All right, then. I'll see you later."
    "Samantha" "Bye-bye!"
    scene expression '#000' with Dissolve(.5)
    scene sc i_1_289 with Dissolve(.5)
    "[Name]" "{i}(Get some sleep? Easy to say...){/i}"
    "[Name]" "{i}(The strangest day in my life. It still does not fit in my head...){/i}"
    "[Name]" "{i}(I am a wizard. Hell, why not? That sounds very cool!){/i}"

label arthur_label:
    scene expression '#000' with Dissolve(2)
    $ renpy.pause(.1, hard = True)
    $ predict_locations_final_2 = True
    $ renpy.choice_for_skipping()
    $ renpy.free_memory()
    call change_location_optimisation_books_label_3 from _call_change_location_optimisation_books_label_3

    scene expression '#000'

    play sound 'audio/new/gameplay/phone_calling2.mp3'
    hide screen main_interface
    'Ring, ring...' ""




    scene sc i_Haley_7_1 with Dissolve(2)
    "[Name]" "Hello?"
    "Elijah" "Yo, [Name]! Rise and shine!"
    "[Name]" "Whoa, what time is it?"
    "Elijah" "Time to like my {b}Lustagram pic{/b}, dude!"
    "[Name]" "Are you kidding me? That's why you're calling?!"
    "Elijah" "A little bit. Seriously, I need that like."
    show sc i_Haley_7_4 with my_dissolve
    "[Name]" "All right, all right."
    "Elijah" "Oh, and by the way, don't stay on the phone too long."
    "Elijah" "I'll pick you up in, like, ten minutes."
    show sc i_Haley_7_4 with my_dissolve
    "[Name]" "What's that for?"
    "Elijah" "{b}The principal called a freshman meeting in the main hall.{/b}"
    "[Name]" "Ah..."
    show sc i_Haley_7_3 with my_dissolve
    "Elijah" "[Name], don't bother yourself with this crap!"
    "Elijah" "Focus on what's important."
    "Elijah" "{b}Give me a like{/b}. See you later."
    "[Name]" "{i}(Why is he so obsessed with his Lustagram?){/i}"
    "[Name]" "{i}Okay, I'll check it out after the meeting{/i}"
    $ log_message.update({"QLOG_Samantha":1 })
    scene image "#000" with Dissolve(.5)
    $ tutor   = True
    $ tutor_2 = True
   # call screen phone_interface_screen
    $ tutor   = False
    $ tutor_2 = False


    stop music_2 fadeout 1
    play music 'audio_ep2/Ambience/amb_castle_crowd.mp3' fadein 1
    scene expression "#000" with Dissolve(.5)
    $ renpy.pause(.5)

    scene sc i_Elijah_2_1 with Dissolve(.5)
    "Arthur" "Students! Hurry up and take your seats, our assembly is about to begin!"
    "Arthur" "We need to be quick if you want to be in time for your first classes."
    show sc i_Elijah_2_2 with my_dissolve
    "Arthur" "It's a joy to see our new students successfully joining Houses!"
    "Arthur" "Nothing brings young wizards closer together than the house."

    "Arthur" "I hope everyone is happy with where they are placed?"
    show sc i_Elijah_2_4 with my_dissolve
    "[Name]" "Why does he ask? Is it possible to change house?"
    "Elijah" "I've never heard of such a thing. Shh, let me listen!"
    show sc i_Elijah_2_2 with my_dissolve
    "Arthur" "In my practice, though, the founders have never been wrong."
    "Arthur" "After all, they see those corners of your soul that you have never seen before."
    "Arthur" "Anyway..."
    "Arthur" "What was I saying... Oh, yes!"
    show sc i_Elijah_2_5 with my_dissolve
    "Arthur" "I'm sure you're all wondering why I gathered you here!"
    "Arthur" "The fact is that the educational process at our Academy is quite unusual."
    "Arthur" "So I thought I'd tell you about the main features of Cordale."
    show sc i_Elijah_2_6 with my_dissolve
    "Elijah" "Oh, I remembered, he gave our course this kind of meeting too!"
    "[Name]" "Yes? So was that informative?"
    show sc i_Elijah_2_7 with my_dissolve
    "Elijah" "I don't know, I slept through mine. Let's hear it together."
    "[Name]" "How'd you even get to be the head student?!"
    "Elijah" "I don't know, Arthur loves me for something."
    show sc i_Elijah_2_5 with my_dissolve
    "Arthur" "Now, as you all know, there are four houses."
    "Arthur" "Leonheart, Martenden, Crowhive and Adderin."
    show sc i_Elijah_2_8 with my_dissolve
    "Arthur" "Each house is unique and stands on the ideals and beliefs of its founder."
    "Arthur" "And these houses are constantly competing with each other."
    "Arthur" "This spirit of healthy competition among the four houses..."
    "Arthur" "Is the cornerstone of Cordale Academy!"
    show sc i_Elijah_2_2 with my_dissolve
    "Arthur" "And now I will tell you the details of how this rivalry is expressed."
    "[Name]" "{i}(It's probably worth listening to attentively).{/i}"
    $ stmps = [0, 0, 0]
label sheet_31_menu:
    if all(stmps):
        jump sheet_31_76
    scene sc i_Elijah_2_2 with Dissolve(.5)
    menu:
        "About classes" if not stmps[0]:
            $ stmps[0] = 1
            show sc i_Elijah_2_2 with my_dissolve
            "Arthur" "As at any educational institution, classes are the basis of everything."
            "Arthur" "In the first year, you have {b}Basic Magic{/b} and {b}Potions{/b} available to you."
            "Arthur" "{b}You can attend classes in the mornings and afternoons on weekdays.{/b}"
            show sc i_Elijah_2_14 with my_dissolve
            "Arthur" "Unlike many other schools, we don't set any limits."
            "Arthur" "You can attend class or you can make time for other activities."
            "Arthur" "Instead, {b}we encourage attendance with housepoints.{/b}"
            jump sheet_31_menu
        "About weekends" if not stmps[1]:
            $ stmps[1] = 1
            show sc i_Elijah_2_2 with my_dissolve
            "Arthur" "Every week, on Saturday morning, we sum up the results of the house competition."
            "Arthur" "And the house with the most points gets {b}special privileges.{/b}"
            show sc i_Elijah_2_4 with my_dissolve
            "Arthur" "Like a {b}trip to the beautiful town of Dale.{/b}"
            "Arthur" "After which our academy is partly named."
            show sc i_Elijah_2_11 with my_dissolve
            "[Name]" "What is that town?"
            "Elijah" "Oh, believe me... Dale is worth it."
            "Elijah" "It's the closest thing to civilization that's within walking distance."
            "Elijah" "There's plenty to do there."
            "Arthur" "There's no classes on the weekends and you're on your own."
            jump sheet_31_menu
        "How to earn housepoints" if not stmps[2]:
            $ stmps[2] = 1
            show sc i_Elijah_2_2 with my_dissolve
            "Arthur" "You're probably wondering how you can earn housepoints."
            "Arthur" "Besides attending classes."
            "Arthur" "Well, I hear that our charming {b}librarian Miss Amelie{/b}..."
            "Arthur" "...would be happy to {b}reward you with points for a little help.{/b}"
            show sc i_Elijah_2_8 with my_dissolve
            "Arthur" "Also, you can {b}apply to Mr. Frollo to join the dueling club.{/b}"
            "Arthur" "But be careful!"
            "Arthur" "There are not only winners in duels, but also losers."
            "Arthur" "And losing students lose housepoints."
            jump sheet_31_menu



label sheet_31_76:
    scene sc i_Elijah_2_2 with Dissolve(.5)
    "Arthur" "Well, well, what else I wanted to say..."
    "Arthur" "Eh, being old isn't a joy..."
    show sc i_Elijah_2_12 with my_dissolve
    "Elijah" "By the way, [Name]."
    "[Name]" "What?"
    "Elijah" "I forgot to tell you that {b}I need to meet you on campus{/b} after the meeting."
    "[Name]" "Okay. What for?"
    show sc i_Elijah_2_13 with my_dissolve
    "Elijah" "To give you {b}your student ID card{/b}, dummy."
    "Elijah" "So you can start getting into this whole house battle."
    "[Name]" "A-ha-ha..."
    "[Name]" "All right."
    show sc i_Elijah_2_14 with my_dissolve
    "Arthur" "And remember, wizards must behave with dignity!"
    "Arthur" "Teachers have the right to remind you of this and to levy housepoints..."
    "Arthur" "...for undignified behavior."
    show sc i_Elijah_2_4 with my_dissolve
    "[Name]" "Oh, that's unpleasant."
    "Elijah" "Don't sweat it. You have to try really, really hard to get your points taken away."
    show sc i_Elijah_2_2 with my_dissolve
    "Arthur" "I guess that's it!"
    "Arthur" "I won't hold you up on your first day of study!"
    show sc i_Elijah_2_15 with my_dissolve
    "Arthur" "Hurry up so you're not late for class."
    show sc i_Elijah_2_16 with my_dissolve
    "[Name]" "{i}(Damn, I was in such a hurry I forgot to put on my underwear...){/i}"
    "[Name]" "{i}(It's uncomfortable and chilly.){/i}"
    "[Name]" "{i}(Gotta get back to the room.){/i}"
    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.5)
    scene expression 'images/locations_main/leon_room_mc_1.png' with Dissolve(.5)

    "[Name]" "{i}(That's much better.){/i}"
    "[Name]" "{i}(It's much more cozy in underpants.){/i}"
    "[Name]" "{i}(Now, let's get back to Elijah.){/i}"
    scene image '#000' with Dissolve(.5)
    $ renpy.pause(.5, hard = True)
    $ hide_interface = True
    scene tutorial_hud_interface_1 with Dissolve(.5)
    $ Q_Arthur=1
    $ Q_Elijah = 0
    $ ep2start = True
    $ time_now = 1
    $ location_now  = 'leon_room_mc'
    $ locations_now = copy.copy(locations_campus)
    $ log_message.update({"QLOG_Elijah":1 })
    $ p_up('Elijah', 1)
    play music 'audio_ep2/SC/33. Romantic.mp3' fadein 1
    $ tutor   = False
    $ tutor_2 = False
    $ SetVariable('tutorial_bb', 0)() 
    $ Hide('tutorial_screen')() 
    call screen tutorial_screen(what_tutor = 'HUD INTERFACE')
    scene image '#000' with Dissolve(.5)
    $ hide_interface = False
    $ renpy.pause(.5, hard = True)
    #show screen show_hide_locations 
    jump main_interface_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
