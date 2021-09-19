label sleep_events:




    hide screen main_interface 
    with Dissolve(.5)

    if Q_Leona==0:
        if Q_Victoria==2:
            $ unlock_gallery('images/ero/Leona.png')
            if renpy.music.get_playing():
                stop music fadeout 1
                play music_2 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
            elif renpy.music.get_playing('music_2'):
                stop music_2 fadeout 1
                play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
            elif True:
                stop music_2 fadeout 1
                play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2


            call Leona_1_label from _call_Leona_1_label
            if persistent.from_gallery:

                scene expression '#000' with Dissolve(1)
                $ renpy.full_restart()
            $ Q_Leona=1


image cord_class_1_door_1_t = 'locations_main/items/cord_class_1/cord_class_1_door_1.png'
label wakeup_events:






    hide screen main_interface 
    with Dissolve(.5)
    python:
        tmp_list_wakeup_sets = []
        for i in wakeup_sets:
            for x in i[1:]:
                tmp_list_wakeup_sets.append(x)
            for x in tmp_list_wakeup_sets:
                if x in i[0]:
                    i[0].remove(x)
    if Q_Haley==6 and 'dale' not in location_now:

        call Haley_7_label from _call_Haley_7_label
        $ p_up('Haley', 5)
        $ log_message.update({"QLOG_Haley":6})
        $ Q_Haley=7











    jump main_interface_label

label Haley_7_label:
    hide screen main_interface with Dissolve(.5)
    show expression '#000' with Dissolve(.5)
    scene sc i_Haley_7_1 with Dissolve(.5)
    "[Name]" "Hello?"
    "Haley" "[Name], hi. It's Haley!"
    show sc i_Haley_7_2 with my_dissolve
    "[Name]" "Haley? Hi!"
    "[Name]" "How did you get my number?"
    "Haley" "I asked Samantha."
    "[Name]" "Do you two know each other?"
    "Haley" "Of course we do! She's a legend!"
    show sc i_Haley_7_1 with my_dissolve
    "[Name]" "Wait... What?"
    "Haley" "She's a straight-A student and the pride of Leonheart!"
    "[Name]" "Uh... That's what you mean."
    "Haley" "Yeah. "
    "Haley" "Are you up yet?"
    show sc i_Haley_7_3 with my_dissolve
    "[Name]" "I'm about to."
    "Haley" "I stumbled across {b}something interesting in my potions textbook{/b}..."
    "[Name]" "Haley, please..."
    "Haley" "This is different! It's not part of the textbook."
    "Haley" "There are some really weird notes in the margins."
    "Haley" "I wanted to show them to you."
    "[Name]" "Sounds interesting."
    show sc i_Haley_7_4 with my_dissolve
    "Haley" "Can we meet?"
    "[Name]" "Sure."
    "Haley" "Great! After classes?"
    "[Name]" "Yeah. "
    "Haley" "Bye-bye!"

    return

label Leona_1_label:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3



    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/17. Dreams.mp3' fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/17. Dreams.mp3' fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/17. Dreams.mp3' fadein 2



    show expression '#000'
    with Dissolve(.5)
    scene sc i_Leona_1_1 with Dissolve(.5)


    "Leona" "Oh, my sweet [Name]..."
    "Leona" "How peacefully and sweetly you sleep."
    "Leona" "How I hate to interrupt your reverie..."
    "Leona" "Wake up, sweet prince!"
    "[Name]" "Mm-hmm."
    "Leona" "Wake up faster, sweetie!"
    "[Name]" "Mm-hmm..."
    "Leona" "My chosen one, answer my call!"
    "[Name]" "Mmmm..."
    "Leona" "HEY!"
    "Leona" "WAKE UP!"
    show sc i_Leona_1_2 with my_dissolve
    "[Name]" "What?!"
    "[Name]" "What? Where? When?"
    "[Name]" "Oh, shit!"
    "[Name]" "Did I fall asleep?"

    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/17. Dreams.mp3' fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/17. Dreams.mp3' fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/17. Dreams.mp3' fadein 2

    play sound_2 'audio/new/Music/intro1.mp3' fadein 1.0
    scene sc i_Leona_1_anim_11 with Dissolve(.5)
    $ renpy.pause(8.1, hard = True)

    "[Name]" "{i}(Wait...){/i}"
    "[Name]" "{i}(Who's that...){/i}"
    "Leona" "You have a sound sleep..."
    "[Name]" "LEONA?"
    "[Name]" "You... you?"
    "[Name]" "Are you real?"
    "Leona" "Hi, honey..."
    "Leona" "Missed me?"
    "[Name]" "Wait a minute!"
    "[Name]" "Is this a dream?"
    show sc i_Leona_1_3 with my_dissolve
    "[Name]" "And why are you naked?"
    "Leona" "I have nothing to be ashamed of. Or do I?"
    show sc i_Leona_1_46 with my_dissolve
    "Leona" "Don't you like what you see?"
    "[Name]" "It's not what I've meant..."
    "[Name]" "But I still don't understnad how is this possible..."
    "[Name]" "How?!"
    show sc i_Leona_1_48 with my_dissolve
    "Leona" "You have so many questions..."
    "Leona" "Which one should I answer first?"
    "[Name]" "Don't play dumb..."
    "[Name]" "Ugh."
    "[Name]" "How did you get in here?"
    show sc i_Leona_1_5 with my_dissolve
    "Leona" "Through you, silly."
    "Leona" "I told you, you're my chosen one."
    "Leona" "Thanks to you, I can {b}temporarily{/b} take material form."
    "Leona" "Alas, I can't stay in this form for long."
    "Leona" "But after centuries of being locked up in a book, that's something!"
    show sc i_Leona_1_48 with my_dissolve
    "[Name]" "Wait!{w} Not so fast."
    "[Name]" "Thanks to me, you can take material form?"
    show sc i_Leona_1_49 with my_dissolve
    "Leona" "Well, yes. Temporarily."
    "[Name]" "But how?!"
    show sc i_Leona_1_5 with my_dissolve
    "Leona" "I am the patroness of the Leonheart Faculty."
    "Leona" "My soul watches over all its members."
    "Leona" "But you are special."
    "Leona" "I've lusted after you for years."
    show sc i_Leona_1_49 with my_dissolve
    "[Name]" "But what's special about me?"
    "Leona" "There's an unbreakable bond between us..."
    "Leona" "All because of your extraordinary soul."
    "Leona" "Tell me about your parents!"
    "[Name]" "They died when I was a baby."
    show sc i_Leona_1_6 with my_dissolve
    "[Name]" "So I don't know much about them."
    "Leona" "I wonder..."
    "Leona" "They must have been wizards."
    "Leona" "{b}You are obviously a pureblood.{/b}"
    show sc i_Leona_1_7 with my_dissolve
    "[Name]" "Is there any way to tell for sure?"
    "Leona" "It's almost impossible."
    "Leona" "But Katrina's always had an instinct for it."
    "Leona" "And she thinks you're pureblood."
    show sc i_Leona_1_50 with my_dissolve
    "[Name]" "That's right, I think I remember something like that..."
    "Leona" "She's never wrong about that."
    "Leona" "All right, enough chitchat!"
    "Leona" "We don't have much time..."
    show sc i_Leona_1_8 with my_dissolve
    "[Name]" "Chitchat?"
    "[Name]" "You materialized in my room in the middle of the night."
    "[Name]" "I have a right to ask you a few questions."
    show sc i_Leona_1_9 with my_dissolve
    "Leona" "Of course, but my time is limited right now."
    "Leona" "{b}I've come to help you discover your power source!{/b}"
    "[Name]" "What?!"
    "[Name]" "You can do that?"
    "Leona" "Of course I can."
    show sc i_Leona_1_51 with my_dissolve
    "Leona" "There are many ways to activate a magical power source."
    "Leona" "Including experimental ones."
    "[Name]" "Shouldn't I discover my source of power myself?"
    "Leona" "Apprentices usually have no problem finding the source."
    "Leona" "But you have a very weak connection to the natural elements!"
    show sc i_Leona_1_8 with my_dissolve
    "[Name]" "What?{w} What do you mean?!"
    "Leona" "Are you asking me?"
    "Leona" "This is the first time I've seen a mage with such a huge pool of potential talent."
    "Leona" "And such a deafness to elemental magic!"
    show sc i_Leona_1_52 with my_dissolve
    "[Name]" "Oh, man..."
    "[Name]" "What should I do then?"
    "Leona" "Forget the elements!"
    "[Name]" "How's that?"
    show sc i_Leona_1_9 with my_dissolve
    "Leona" "Eventually you will master elemental magic."
    "Leona" "But to activate your potential, I will share my source."
    "Leona" "The power of the will."
    "Leona" "Given how tightly our souls are linked, that shouldn't be a problem."
    show sc i_Leona_1_53 with my_dissolve
    "Leona" "{b}All I have to do is perform the ritual.{/b}"
    "[Name]" "Okay. "
    "[Name]" "Is there anything I can do to help?"
    "Leona" "Oh, yes! You could..."
    show sc i_Leona_1_4 with my_dissolve
    "Leona" "The thing is, the classic ritual involves activating the soul."
    "Leona" "Through pain."
    "Leona" "The ritual I designed works the other way around."
    "[Name]" "It activates the pain through the soul?"
    show sc i_Leona_1_5 with my_dissolve
    "Leona" "Activates the soul through pleasure."
    "[Name]" "Oh... "
    "Leona" "Yes."
    show sc i_Leona_1_53 with my_dissolve
    "Leona" "In order for me to give you my power..."
    "Leona" "We must experience tremendous pain at the same time."
    "Leona" "It feels like death."
    "Leona" "Or great pleasure."
    show sc i_Leona_1_9 with my_dissolve
    "Leona" "Like an orgasm."
    "[Name]" "Leona..."
    "Leona" "Don't worry, darling."
    "Leona" "I can't force you to do anything..."
    "Leona" "The choice is yours."

    menu:
        "Reject pleasure" if True:
            show sc i_Leona_1_10 with my_dissolve
            "[Name]" "Leona..."
            "[Name]" "You're insanely attractive, but..."
            "[Name]" "I barely know you."
            "[Name]" "This isn't right."
            "[Name]" "I refuse to have sex with you."
            "[Name]" "I choose pain."
            show sc i_Leona_1_6 with my_dissolve
            "Leona" "I understand."
            "Leona" "So be it."
            "Leona" "Bite the blanket if you don't want to wake up the whole campus."
            "Leona" "It's gonna be a long night..."
            "[Name]" "{i}(She's planning on torturing me all night?!){/i}"
            "[Name]" "{i}(Heh! Come on!){/i}"
            "[Name]" "{i}(I can handle anything.){/i}"
            "Leona" "Are you ready, my champion?"
            "[Name]" "Anything that doesn't kill us makes us stronger."
            "[Name]" "Right?"
            show sc i_Leona_1_9 with my_dissolve
            "Leona" "Let's see what you have to say in the morning..."
            "Leona" "So, where did I put my Pear of Anguish?"
            "[Name]" "{i}(PEAR OF ANGUISH? Uh-oh!!!){/i}"
            scene expression '#000' with Dissolve(.5)


            if persistent.from_gallery:
                scene expression '#000' with Dissolve(1)
                $ renpy.full_restart()

            return
        "Accept pleasure" if True:
            $ pass





    show sc i_Leona_1_11 with my_dissolve
    "[Name]" "It seems to me to be a choice without a choice."
    "[Name]" "How could I say no to the founder of my house?"
    show sc i_Leona_1_12 with my_dissolve
    "[Name]" "Especially one so beautiful."
    "[Name]" "I would be honored to give you the pleasure."
    show sc i_Leona_1_13 with my_dissolve
    "Leona" "I confess, I had hoped you would make that choice."
    "Leona" "And with such fervor..."
    "Leona" "Hang onto it, because the ritual will suck you dry..."
    show sc i_Leona_1_14 with my_dissolve
    "Leona" "I'll make sure of that myself."
    "[Name]" "{i}(She's so persistent...){/i}"
    show sc i_Leona_1_15 with my_dissolve
    "[Name]" "{i}(She hasn't had a lover in a long time, so...){/i}"
    "[Name]" "{i}(I can't embarass myself!){/i}"
    "Leona" "I hope you can show intensity worthy of Leonheart..."
    show sc i_Leona_1_16 with my_dissolve
    "[Name]" "Try me!"
    "Leona" "Wow!"
    "Leona" "You're quick to prepare..."
    show sc i_Leona_1_17 with my_dissolve
    "Leona" "Well hello there!"
    "[Name]" "{i}(I can feel the heat inside her...){/i}"
    show sc i_Leona_1_18 with my_dissolve
    "Leona" "Mm-hmm..."
    "Leona" "Just what you need."
    show sc i_Leona_1_19 with my_dissolve
    "Leona" "Oh, yeah..."
    "Leona" "It's so swollen."
    show sc i_Leona_1_20 with my_dissolve
    "Leona" "Mmmm..."
    "[Name]" "{i}(Shit... Her mouth is so warm and soft...){/i}"
    show sc i_Leona_1_21 with my_dissolve
    "[Name]" "{i}(And her tongue...){/i}"
    "[Name]" "Ah..."
    show sc i_Leona_1_22 with my_dissolve
    "Leona" "Mmm... oh..."
    "Leona" "Impressive rod!"
    show expression 'images/video/Leona_1_anim_1_a.webp' with my_dissolve
    "Leona" "Let's see what magic it can do!"
    scene sc i_Leona_1_anim_1 with Dissolve(.5)
    "Leona" "Mmmm..."
    "Leona" "Mm-hmm... Uh..."
    "[Name]" "Ahh..."
    scene sc i_Leona_1_anim_2 with Dissolve(.5)
    "[Name]" "{i}(Damn, she's just too good...){/i}"
    "[Name]" "{i}(I've never experienced anything like this...){/i}"
    "[Name]" "{i}(My ex-girlfriends are nothing compared to this experience.){/i}"
    scene sc i_Leona_1_anim_3 with Dissolve(.5)
    "[Name]" "Ah... N-n-no way..."
    "Leona" "I'm just getting started..."
    "Leona" "Mmmm... Ugh..."
    "[Name]" "{i}(Crazy...){/i}"
    "[Name]" "Oh, yeah..."
    show sc i_Leona_1_23 with my_dissolve
    "Leona" "Let's stop the foreplay."
    "[Name]" "Was that foreplay?"
    show sc i_Leona_1_24 with my_dissolve
    "[Name]" "{i}(I almost came...){/i}"
    "Leona" "You're about to experience real pleasure!"
    show sc i_Leona_1_25 with my_dissolve
    "[Name]" "{i}(Oh gosh... She's not kidding...){/i}"
    "[Name]" "Come on, baby!"
    show expression 'images/video/Leona_1_anim_4_a.webp' with my_dissolve
    "Leona" "Ah... Oh...."
    scene sc i_Leona_1_anim_4 with Dissolve(.5)
    "Leona" "Feel that?"
    "Leona" "Perfect."
    "[Name]" "Ah..."
    "[Name]" "{i}(I don't know what the magic it is, but her pussy is so tight...){/i}"
    scene sc i_Leona_1_anim_5 with Dissolve(.5)
    "[Name]" "{i}(It's like fucking a teenager...){/i}"
    "Leona" "Do you like coming inside me?"
    "[Name]" "Yes..."
    scene sc i_Leona_1_anim_6 with Dissolve(.5)
    "Leona" "Yes?"
    "[Name]" "Then fill me with your huge cock!"
    "Leona" "Like no one has ever done before!"
    "Leona" "Deeper!"
    scene sc i_Leona_1_anim_7 with Dissolve(.5)
    "Leona" "More!{w} Deeper!"
    "Leona" "Show me what you've got!"
    show sc i_Leona_1_26 with my_dissolve
    "[Name]" "Do you want to go deeper?"
    "Leona" "Yes..."
    "[Name]" "Then I'll lead."
    show sc i_Leona_1_27 with my_dissolve
    "[Name]" "Look at me."
    "[Name]" "Open your legs wide!"
    show sc i_Leona_1_28 with my_dissolve
    "Leona" "Oh..."
    "Leona" "Oh, yeah! (Laughs)"
    "Leona" "I love it when you lead."
    show sc i_Leona_1_29 with my_dissolve
    "[Name]" "Are you ready?!"
    "Leona" "Yes..."
    show sc i_Leona_1_30 with my_dissolve
    "[Name]" "You like being in charge?"
    "Leona" "Ah... Yes..."
    show sc i_Leona_1_32 with my_dissolve
    "[Name]" "{i}(Her energy is transmitted through my cock...){/i}"
    "Leona" "Ah..."
    "[Name]" "{i}(I feel it with every throb...){/i}"

    "Leona" "Yes... fuck me!"
    "[Name]" "Whatever you say..."
    show expression 'images/video/Leona_1_anim_8_a.webp' with my_dissolve
    "[Name]" "{i}(Now I'll show you what I can do!){/i}"
    scene sc i_Leona_1_anim_8 with Dissolve(.5)
    "Leona" "Ah... ah..."
    "Leona" "Um... umh... ah..."
    "Leona" "Yes! More! Harder!"
    scene sc i_Leona_1_anim_9 with Dissolve(.5)
    "[Name]" "{i}(Unbelievable... With every thrust...){/i}"
    "[Name]" "{i}(Her magic seems to be transmitted to me...){/i}"
    "[Name]" "{i}(I've never felt so much power before!){/i}"
    "[Name]" "{i}(But I am now...){/i}"
    show sc i_Leona_1_anim_10 with my_dissolve
    "[Name]" "I'm about to cum..."
    "Leona" "Oh, my champion!"
    "Leona" "Cum wherever you want!"

    menu:
        "Cum on stomach" if True:

            show sc i_Leona_1_33 with my_dissolve
            "[Name]" "I'm...{w} I'm going to cum!"
            "Leona" "Me too... Oh, yeah!"
            "Leona" "Oh..."
            show sc i_Leona_1_34 with my_dissolve
            "[Name]" "Suck your tummy in!"
            "Leona" "Cover me with your cum..."
            show sc i_Leona_1_35 with my_dissolve
            "[Name]" "Oh yes..."
            "[Name]" "{i}(I can feel her power inside me...){/i}"
            "[Name]" "{i}(Pure, untainted energy...){/i}"
            show sc i_Leona_1_36 with my_dissolve
            "Leona" "Can you feel the ritual working yet?"
            "Leona" "Go to sleep, and when you wake up..."
            "Leona" "I..."
        "Cum on her face" if True:



            show sc i_Leona_1_37 with my_dissolve
            "[Name]" "I...{w} I'm going to cum!"
            "[Name]" "Show me your pretty face."
            show sc i_Leona_1_38 with my_dissolve
            "Leona" "Oh..."
            "Leona" "Oh, yeah..."
            show sc i_Leona_1_39 with my_dissolve
            "Leona" "Just what I needed."
            "[Name]" "That was incredible..."
            "[Name]" "{i}(I can feel her power inside me...){/i}"
            show sc i_Leona_1_40 with my_dissolve
            "[Name]" "{i}(Pure, untainted energy...){/i}"
            "Leona" "Can you feel the ritual working yet?"
            "Leona" "Go to sleep, and when you wake up..."
            "Leona" "I..."
        "Cum inside" if True:


            show sc i_Leona_1_41 with my_dissolve
            "[Name]" "I'm...{w} I'm going to cum!"
            "Leona" "Me too... Oh yes!"
            show sc i_Leona_1_42 with my_dissolve
            "Leona" "Oh..."
            "Leona" "Ah...{w} Ah...{w} Ah...{w}"
            "Leona" "Aaaaarh!"
            "[Name]" "That was incredible..."
            show sc i_Leona_1_43 with my_dissolve
            "Leona" "You filled me to the brim..."
            "Leona" "I wonder how strong your seed is?"
            "[Name]" "{i}(I can feel her power inside me...){/i}"
            "[Name]" "{i}(Pure, untainted by the elements...){/i}"
            "Leona" "Can you feel the ritual working already?"
            "Leona" "Go to sleep, and when you wake up..."
            "Leona" "I..."
    scene expression '#000' with Dissolve(.5)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
