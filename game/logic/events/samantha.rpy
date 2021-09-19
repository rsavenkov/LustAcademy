



label samantha_events_label:



    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu


    $ set_now = samantha_events_set
    menu:

        "Talk to Samantha" if Q_Samantha == 0:

            call Samantha_1_label from _call_Samantha_1_label
            $ p_up('Samantha', 2)
            $ log_message.update({"QLOG_Samantha":1 })
            $ Q_Samantha=1
            $ samantha_events_set.append("1 Talk to Samantha")
            $ wakeup_sets.append([

            
            samantha_events_set, "1 Talk to Samantha"
            
            
                ])
        "1 Talk to Samantha" if Q_Samantha == 1:

            call Samantha_2_label from _call_Samantha_2_label
            $ p_up('Samantha', 3)
            $ log_message.update({"QLOG_Samantha":2 })
            $ Q_Samantha=2


        "Talk to Samantha" if Q_Samantha == 4:

            call Samantha_5_label from _call_Samantha_5_label
            scene expression '#000' with Dissolve(.5)
            call Samantha_6_label from _call_Samantha_6_label
            scene expression '#000' with Dissolve(.5)
            $ p_up('Samantha', 6)
            $ log_message.update({"QLOG_Samantha":5 })
            $ Q_Samantha=6
            $ change_location_2('cord_garden_l', time_now+1)
        "Not now" if True:


            show screen main_interface 
            show screen show_hide_locations_2
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label
label samantha_events_3_label:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu


    $ set_now = samantha_events_set_3

    menu:

        "Talk to Samantha" if Q_Samantha == 0:
            call Samantha_2_1_label from _call_Samantha_2_1_label

            $ log_message.update({"QLOG_Samantha":1 })


        "1 Talk to Samantha" if Q_Samantha == 1:
            call Samantha_2_2_label from _call_Samantha_2_2_label
            $ samantha_events_set.append("1 Talk to Samantha")

            $ wakeup_sets.append([

            
            samantha_events_set, "1 Talk to Samantha"
            
            
                ])

            $ log_message.update({"QLOG_Samantha":1 })

        "4 Talk to Samantha" if Q_Samantha == 4:
            call Samantha_2_3_label from _call_Samantha_2_3_label
            $ samantha_events_set.append("4 Talk to Samantha")

            $ wakeup_sets.append([

            
            samantha_events_set, "4 Talk to Samantha"
            
            
                ])

            $ log_message.update({"QLOG_Samantha":1 })
        "Not now" if True:


            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label








label Samantha_1_label:

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
    show sc i_Samantha_1_1 with Dissolve(.5)
    "[Name]" "Hi, Sam!"
    "[Name]" "You look great!"
    "Samantha" "Hi!{w} Thank you."
    "Samantha" "How are you feeling, [Name]?"
    "[Name]" "Full of energy."
    "[Name]" "Why?"
    show sc i_Samantha_1_2 with my_dissolve
    "Samantha" "It can be hard for newbies to adapt to magic."
    "Samantha" "I'm worried about you."
    "[Name]" "Don't be silly."
    "[Name]" "I'm perfectly fine."
    "[Name]" "Listen, I've been meaning to ask you..."
    show sc i_Samantha_1_4 with my_dissolve
    "Samantha" "Wait a minute!"
    "Samantha" "Why are you standing there like you're in trouble?"
    "Samantha" "There's plenty of room."
    "Samantha" "Here, sit down and tell me."
    show sc i_Samantha_1_17 with my_dissolve
    "[Name]" "You care too much about me."
    "[Name]" "How are things with you and Andy? Haven't seen him in a while."
    "Samantha" "Who?"
    "[Name]" "Uh, well, Andy..."
    "[Name]" "The guy you came with to cheer for me at my game."
    "[Name]" "He also drives a light blue Dodge."
    show sc i_Samantha_1_9 with my_dissolve
    "Samantha" "Uh...{w} That's whom you're talking about.{w} How do you remember him?"
    "Samantha" "I only went out with him a couple of times."
    "[Name]" "Yes? What happened?"
    "Samantha" "We didn't get along."
    "[Name]" "Strange, he seemed nice enough."
    "Samantha" "Everyone has their quirks."
    "[Name]" "Not you."
    "[Name]" "Sometimes I think you're even too perfect."
    show sc i_Samantha_1_21 with my_dissolve
    "Samantha" "Oh, believe me..."
    "[Name]" "{i}(What's that supposed to mean, Sam?){/i}"
    "[Name]" "{i}(What are you, flirting with me?){/i}"
    show sc i_Samantha_1_10 with my_dissolve
    "Samantha" "Oh, come on."
    "Samantha" "How's your leg?"
    "[Name]" "My leg? Why are you bringing it up?"
    "[Name]" "It hurts a little when I stand up, but all in all..."
    "[Name]" "It's okay."
    show sc i_Samantha_1_9 with my_dissolve
    "Samantha" "Wait, you still haven't cured it?"
    "[Name]" "How would I cure it?"
    "Samantha" "Oh, wait! You haven't been to the infirmary yet."
    show sc i_Samantha_1_24 with my_dissolve
    "Samantha" "Cordale has great healers."
    "Samantha" "You could even get back into sports if you wanted to."
    "[Name]" "I don't know what kind of sport we're talking about with my leg."
    "[Name]" "Even if you take away the pain, the muscles are not the same..."
    "Samantha" "Have you forgotten where you are?"
    show sc i_Samantha_1_9 with my_dissolve
    "Samantha" "It's Cordale, baby."
    "Samantha" "I can't promise you'll enjoy the healing process."
    "Samantha" "Sometimes healing spells require you to do terrible things..."
    "Samantha" "But the results are amazing."
    show sc i_Samantha_1_15 with my_dissolve
    "[Name]" "Are you telling me my leg will be the same as it was?"
    "Samantha" "I can't promise, but..."
    show sc i_Samantha_1_25 with my_dissolve
    "[Name]" "Sam, this is so great!"
    "Samantha" "Come on, I had nothing to do with it."
    "[Name]" "Heh, I guess you're right."
    "[Name]" "And to think I'm both a wizard and not a cripple?"
    "[Name]" "That's a shame."
    "Samantha" "Why is that?"
    "[Name]" "Can you imagine how cool I'd look with a cane-staff?"
    show sc i_Samantha_1_12 with my_dissolve
    "Samantha" "You're stupid!"
    "Samantha" "What do you need a staff for, anyway?"
    "Samantha" "No one in Cordale uses those wooden things."
    "Samantha" "Maybe Frollo sometimes, but he's pretty weird."
    "Samantha" "By the way, he's the prez of our dueling club."
    show sc i_Samantha_1_18 with my_dissolve
    "[Name]" "Frollo...{w} He met us after the train."
    "[Name]" "Does he have different pupils?"
    "Samantha" "Aren't they creepy?{w} Although one of our classmates thinks they're sexy."
    "[Name]" "I'm speechless."
    "[Name]" "Are you in a dueling club?"
    "Samantha" "I was last year."
    show sc i_Samantha_1_30 with my_dissolve
    "Samantha" "Now...{w} I'm having trouble with that."
    "[Name]" "Yes? What's wrong?"
    "Samantha" "{b}I can't seem to get the hang of one attack spell.{/b}"
    "Samantha" "I don't know what it is, maybe a summer without practice didn't do me any good."
    show sc i_Samantha_1_20 with my_dissolve
    "[Name]" "That's pretty weird."
    menu:
        "Cheer Samantha up " if True:
            $ pass
        "Comfort Samantha" if True:
            jump Samantha_1_label_85
    "[Name]" "I'm sure you can do any spell."
    "[Name]" "There's a reason you've always been an overachiever."
    "[Name]" "You have the winning gene in your DNA, baby."
    show sc i_Samantha_1_41 with my_dissolve
    "Samantha" "Ah-ha-ha-ha."
    "Samantha" "You're exaggerating."
    "Samantha" "But thank you.{w} That's just what I needed right now."
    "[Name]" "Always happy to tell a pretty girl the truth to her face."

    jump Samantha_1_label_92
label Samantha_1_label_85:
    "[Name]" "Hey! Don't be sad about it."
    "[Name]" "You'll do great. I'll help you if you need it."
    "[Name]" "And it's not all about this dueling club."
    "[Name]" "Anyway, it'll be all right."
    "Samantha" "You're right, of course."
    "Samantha" "Thanks for your support."
    show sc i_Samantha_1_10 with my_dissolve
    "[Name]" "You can always count on me."
label Samantha_1_label_92:
    show sc i_Samantha_1_40 with my_dissolve
    "Samantha" "Stop embarrassing me..."
    "[Name]" "Sorry, it's hard to hold back."
    "Samantha" "Okay, [Name], I still have to deal with my schedule."
    show sc i_Samantha_1_31 with my_dissolve
    "[Name]" "No problem. I'll let you get back to it."
    "[Name]" "Thanks for the nurse advice, Sam."
    "[Name]" "I'll be sure to check in with her."
    "Samantha" "No problem."
    "Samantha" "Thank you."
    return


label Samantha_2_label:

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
    show sc i_Samantha_1_2 with Dissolve(.5)
    "[Name]" "Samantha, hi there!"
    "Samantha" "[Name]? Hi."
    "Samantha" "Here, take a seat."
    show sc i_Samantha_1_6 with my_dissolve
    "Samantha" "Sorry, I didn't see you right away..."
    "[Name]" "Sam, you look worried."
    "[Name]" "What's going on?"
    show sc i_Samantha_1_38 with my_dissolve
    "Samantha" "I don't want to cause a panic, but..."
    "[Name]" "You know how the word \"panic\" works, right?"
    "[Name]" "I'm already freaking out!"
    show sc i_Samantha_1_40 with my_dissolve
    "Samantha" "Don't interrupt me, please. It's important."
    "[Name]" "I'm sorry. I'm sorry."
    "Samantha" "There's a possibility that {b}we won't have long to study together.{/b}"
    "[Name]" "{i}(What's going on?){/i}"
    show sc i_Samantha_1_20 with my_dissolve
    "Samantha" "That's why I'm so glad you want to follow in my footsteps."
    "Samantha" "Maybe at least one of us can make it to the end..."
    "[Name]" "Wait!"
    show sc i_Samantha_1_14 with my_dissolve
    "[Name]" "Samantha, are those tears in your eyes?"
    "[Name]" "What's wrong?"
    "Samantha" "{b}I'm losing my connection to magic.{/b}"
    show sc i_Samantha_1_4 with my_dissolve
    "Samantha" "I can't do magic anymore! At all."
    "Samantha" "I haven't been able to do a single spell since we got off the train."
    show sc i_Samantha_1_7 with my_dissolve
    "Samantha" "And when I try to conjure, my hands cramp..."
    "Samantha" "I've exhausted my magic!"
    "[Name]" "{i}(That's a bummer... Does that even happen?){/i}"
    "[Name]" "{i}(Poor Sam...){/i}"
    show sc i_Samantha_1_32 with my_dissolve
    "[Name]" "How can that be?"
    "[Name]" "Does that even happen?"
    show sc i_Samantha_1_9 with my_dissolve
    "Samantha" "I don't know..."
    "Samantha" "I can't cast any second year spells."
    "Samantha" "And first year ones only through terrible pain..."
    show sc i_Samantha_1_39 with my_dissolve
    "[Name]" "Have you tried talking to anyone?"
    "[Name]" "Victoria, Frollo, the headmaster?"
    "[Name]" "Amelia has so many books in the library..."
    "[Name]" "I'm sure someone can help you!"
    show sc i_Samantha_1_38 with my_dissolve
    "Samantha" "As long as the nurse isn't there for medical help, Frollo is the one to ask."
    "Samantha" "He might be able to help me, but not in this case..."
    "[Name]" "Why is that?"
    show sc i_Samantha_1_40 with my_dissolve
    "Samantha" "There are very few strict rules in Cordale, [Name]."
    "Samantha" "But if you can't do spells, you don't belong in a society of wizards."
    "Samantha" "Everyone knows that."
    show sc i_Samantha_1_4 with my_dissolve
    "Samantha" "Once I confess, I'll be out of here and have my memory wiped."
    "[Name]" "Nonsense... It can't be true!"
    show sc i_Samantha_1_40 with my_dissolve
    "Samantha" "Maybe I've looked into it, there have been cases..."
    "Samantha" "I don't know what to do..."
    "[Name]" "{i}(Damn... Why Sam?){/i}"
    "[Name]" "{i}(I have to help her somehow.){/i}"
    show sc i_Samantha_1_14 with my_dissolve
    "[Name]" "You know what I think?"
    "[Name]" "Teachers absolutely do not need to know about your situation."
    "[Name]" "And you don't have to lose your memory at all."
    show sc i_Samantha_1_16 with my_dissolve
    "[Name]" "I'll find everything out, hypothetically, without mentioning you."
    "[Name]" "And we'll solve this problem."
    show sc i_Samantha_1_18 with my_dissolve
    "Samantha" "You're so smart... Shit."
    "Samantha" "I'm jealous."
    show sc i_Samantha_1_12 with my_dissolve
    "[Name]" "Stop it, tell me when I've got something."
    "[Name]" "In the meantime, just keep your pretty little nose up!"
    "Samantha" "Okay."
    return




label Samantha_5_label:

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
    show sc i_Samantha_1_1 with Dissolve(.5)
    "[Name]" "Samantha, hi!"
    "[Name]" "Do you have a minute?"
    show sc i_Samantha_1_3 with my_dissolve
    "Samantha" "Uh, sure."
    "Samantha" "I have plenty of time."
    show sc i_Samantha_5_1 with my_dissolve
    "Samantha" "I can't do any magic."
    "Samantha" "Even the energy globe is hard to assemble..."
    "Samantha" "Maybe I should pull myself together and confess to the headmaster."
    "Samantha" "God, what a shame."
    show sc i_Samantha_1_21 with my_dissolve
    "[Name]" "Aren't you a little early to be in mourning?"
    "[Name]" "Have you forgotten what a cool friend you have?"
    show sc i_Samantha_1_22 with my_dissolve
    "Samantha" "You're not just asking, are you?"
    "[Name]" "Maybe I am."
    show sc i_Samantha_1_7 with my_dissolve
    "Samantha" "I don't believe it! Did you really find out something?"
    "Samantha" "Come on, tell me!"
    show sc i_Samantha_1_20 with my_dissolve
    "[Name]" "I asked Frollo about your symptoms and he recognized them."
    "Samantha" "What's wrong with me? Is that curable?"
    show sc i_Samantha_5_2 with my_dissolve
    "[Name]" "Your magical ligaments are ruptured because magic conflicts within you."
    "[Name]" "Here, take this."
    "Samantha" "What's this?"
    "[Name]" "It's a compress with night pixie pollen and some kind of herb."
    "[Name]" "Use it at night and..."
    show sc i_Samantha_1_17 with my_dissolve
    "Samantha" "And I'll be able to conjure again?"
    "[Name]" "And you can conjure again."
    "Samantha" "Eeee!"
    show sc i_Samantha_5_3 with my_dissolve
    "Samantha" "Come here, I'll hug you to death!"
    "Samantha" "Hooray-hooray-hooray!"
    "[Name]" "{i}(I've never heard anyone's heart beat like that.){/i}"
    "[Name]" "{i}(She's so happy...){/i}"
    show sc i_Samantha_1_12 with my_dissolve
    "[Name]" "Am I entitled to a reward?"
    "Samantha" "What do you mean?"
    show sc i_Samantha_5_4 with my_dissolve
    "[Name]" "You know."
    "Samantha" "Hee hee."
    "Samantha" "It's a fair price."
    menu:
        "Switch to your lips" if True:


            show sc i_Samantha_5_5 with my_dissolve
            "Samantha" "Your reward!"
            show sc i_Samantha_5_6 with my_dissolve
            "[Name]" "{i}(I have a better idea!){/i}"
            "Samantha" "..."
            "[Name]" "..."
            show sc i_Samantha_5_7 with my_dissolve
            "Samantha" "You're such a fool!"
            "Samantha" "Ew!"
            "[Name]" "Ew?{w} Didn't you like it at all?"
            show sc i_Samantha_1_40 with my_dissolve
            "Samantha" "It's not that, you know!"
            "[Name]" "I couldn't help myself."
            "[Name]" "All the more reason to lighten the mood before a serious conversation..."
        "Let her kiss your cheeks" if True:

            show sc i_Samantha_5_5 with my_dissolve
            "Samantha" "Your reward!"
            "[Name]" "{i}(This is my reward for helping Samantha in any way I could since she was 9 years old.){/i}"
            "[Name]" "{i}(The chip we had.){/i}"
            "[Name]" "{i}(I think she enjoyed remembering it.){/i}"
            "[Name]" "{i}(But now we need to add a little bit of tar to that barrel of honey...){/i}"
            "[Name]" "Thank you! But we need to have a serious talk about something..."
    show sc i_Samantha_1_25 with my_dissolve
    "Samantha" "What's the matter?"
    "[Name]" "It's rather personal."
    "[Name]" "Can we talk privately?"
    show sc i_Samantha_1_16 with my_dissolve
    "Samantha" "Um..."
    "Samantha" "Is it really urgent?"
    show sc i_Samantha_1_44 with my_dissolve
    "Samantha" "I've already made a promise to Audrey..."
    "Samantha" "I have to meet her before classes."
    "[Name]" "Are you going to the Academy?"
    show sc i_Samantha_1_45 with my_dissolve
    "Samantha" "Yes. Why?"

    "[Name]" "Let me keep you a company."
    "[Name]" "We can talk on our way there."
    show sc i_Samantha_1_46 with my_dissolve
    "Samantha" "Well, I'm alright with that."
    "Samantha" "Just give me a minute to grab my textbooks."
    "[Name]" "Alright, I'll wait here."
    scene expression '#000' with Dissolve(.5)
    scene sc i_Samantha_1_47 with Dissolve(.5)
    "Samantha" "I'm ready!"
    "Great! Let's go."
    return


label Samantha_2_1_label:

    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)
    show sc i_Samantha_2_5 with Dissolve(.5)
    "[Name]" "Hey, girls!"
    "[Name]" "Samantha, do you have a minute?"
    "Samantha" "[Name]! Hi there!"
    show sc i_Samantha_2_6 with my_dissolve
    "Samantha" "I'm a little busy right now."
    "Samantha" "Can we talk in the morning?"
    "[Name]" "Okay, no problem."
    return


label Samantha_2_2_label:


    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)
    show sc i_Samantha_2_5 with Dissolve(.5)
    "[Name]" "Yo, Samantha!"
    "Samantha" "What?"
    show sc i_Samantha_2_11 with my_dissolve
    "[Name]" "I wanted to talk to you about something."
    "[Name]" "In private."
    show sc i_Samantha_2_6 with my_dissolve
    "Samantha" "Let's talk in the morning. Audrey and I had plans for tonight."
    "Samantha" "You're not gonna be offended, are you?"
    "[Name]" "Of course not."
    return


label Samantha_2_3_label:


    hide screen main_interface 
    show expression '#000'

    with Dissolve(.5)

    show sc i_Samantha_2_8 with Dissolve(.5)
    "[Name]" "Hi, Samantha! Great news, I..."
    "Samantha" "Hey, [Name]! We're actually talking here."
    show sc i_Samantha_2_13 with my_dissolve
    "[Name]" "I'm sorry, it's just that I was looking into..."
    "Samantha" "I'm sure it can wait till morning."
    "[Name]" "Okay. We'll talk in the morning."
    show sc i_Samantha_2_5 with my_dissolve
    "Samantha" "Thanks. (Chuckles)"
    return







label samantha_events_4_label:









    if not hasattr(store, 'Q_NV_Samantha'):
        $ Q_NV_Samantha = 0
    if persistent.nv is None:
        call hide_all_main_interfaces from _call_hide_all_main_interfaces_8
        $ nv = renpy.call_screen('confirm', 
        '{size=15}Note that night visits are entirely optional.{/size} \n{size=15}This additional content is not required to complete the game{/size} \n{size=15}and won’t influence your relationship with other characters.{/size}', 
        Return('Continue'), Return('Not now'), yes_text = _('Continue'), no_text = _('Not now'),)
        $ persistent.nv = True
    else:
       $ nv = 'Continue' 
    if nv == 'Continue':
        if True:


            if persistent.from_gallery:

                hide screen main_interface 

                show expression '#000a'

                with Dissolve(.5)

                menu:
                    "Scene 1" if True:

                        $ renpy.call('samantha_events_4_label_0')
                    "Scene 2" if True:

                        $ renpy.call('samantha_events_4_label_1')
                    "Scene 3" if True:

                        $ renpy.call('samantha_events_4_label_2')
                    "Scene 4" if True:

                        $ renpy.call('samantha_events_4_label_3')
                    "Scene 5" if True:

                        $ renpy.call('samantha_events_4_label_4')


            if persistent.from_gallery:
                hide screen main_interface
                scene expression '#000'
                with Dissolve(1)
                $ renpy.full_restart()


            if renpy.music.get_playing():
                stop music fadeout .5
                play music_2 'audio_ep2/Music/mus_for_visites.mp3' fadein 1
            elif renpy.music.get_playing('music_2'):
                stop music_2 fadeout .5
                play music 'audio_ep2/Music/mus_for_visites.mp3' fadein 1
            elif True:
                stop music_2 fadeout .5
                play music 'audio_ep2/Music/mus_for_visites.mp3' fadein 1

            if Q_NV_Samantha:
                hide screen main_interface with Dissolve(.5)
                $ renpy.call('samantha_events_4_label_'+str(Q_NV_Samantha))

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
        if True:

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


label samantha_events_4_label_0:

    $ Q_NV_Samantha += 1
    hide screen main_interface 
    scene sc i_Samantha_NV_1
    with Dissolve(.5)


    "[Name]" "{i}(Why did this never occurred to me to do this at our house?){/i}"
    "[Name]" "{i}(Maybe I was afraid of Don, who'd kill me if he finds out.){/i}"
    "[Name]" "{i}(Or of betraying the trust of the only one in the house who likes me.){/i}"
    "[Name]" "{i}(I should not be thinking about that nonsense now.){/i}"
    "[Name]" "{i}(While I have such a beautiful lady waiting for my attention.){/i}"
    show sc i_Samantha_NV_2 with my_dissolve
    "[Name]" "{i}(Show me what've you got, Samantha...){/i}"
    "[Name]" "{i}(Let's see...){/i}"
    show sc i_Samantha_NV_3 with my_dissolve
    "[Name]" "{i}(Oh wow...){/i}"
    "[Name]" "{i}(I can see a little bit more, than I thought I would...){/i}"
    "[Name]" "{i}(This tiny bra can't hide all of your gorgeus breasts...){/i}"
    show sc i_Samantha_NV_4 with my_dissolve
    "[Name]" "{i}(Sometimes you're even too gorgeus, Samantha...){/i}"
    "[Name]" "{i}(How can I resist you...){/i}"
    show sc i_Samantha_NV_5 with my_dissolve
    "[Name]" "{i}(Let's turn you on your back...){/i}"
    show sc i_Samantha_NV_16 with my_dissolve
    "Samantha" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I think that could wake her up...){/i}"
    "[Name]" "{i}(Better get out of here and get some sleep.){/i}"





    scene expression '#000' with Dissolve(1.5)

    $ renpy.pause(1.5, hard = True)

    if renpy.music.get_playing():
        stop music fadeout .5
        play music_2 'audio_ep2/SC/33. Romantic.mp3' fadein 1


    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout .5
        play music 'audio_ep2/SC/33. Romantic.mp3' fadein 1
    $ change_location_2('leon_room_mc', time_now+1, sleep = True)

    if persistent.from_gallery:
        hide screen main_interface
        scene expression '#000'
        with Dissolve(1)
        $ renpy.full_restart()

    jump main_interface_label

label samantha_events_4_label_1:
    $ Q_NV_Samantha += 1
    scene sc i_Samantha_NV_1 with Dissolve(.5)


    "[Name]" "{i}(Samantha always looks so peaceful in her sleep.){/i}"
    "[Name]" "{i}(Let's take a closer look at you.){/i}"
    show sc i_Samantha_NV_2 with my_dissolve
    "[Name]" "{i}(Sleeping beauty...){/i}"
    "[Name]" "{i}(I could have looked at you all night...){/i}"
    "[Name]" "{i}(Still hiding from me under the blanket, Samantha?){/i}"
    show sc i_Samantha_NV_3 with my_dissolve
    "[Name]" "{i}(Let's take that off...){/i}"
    "[Name]" "{i}(Oh wow...){/i}"
    show sc i_Samantha_NV_4 with my_dissolve
    "[Name]" "{i}(What a beauty...){/i}"
    "[Name]" "{i}(I've never thought you'd be that sexy, Sam...){/i}"
    show sc i_Samantha_NV_5 with my_dissolve
    "[Name]" "{i}(This time, I'll be more cautious.){/i}"
    "[Name]" "{i}(Oh, yes.){/i}"
    "[Name]" "{i}(Now I see all the best parts.){/i}"
    "[Name]" "{i}(To be honest...){/i}"
    show sc i_Samantha_NV_6 with my_dissolve
    "[Name]" "{i}(You've exceeded all my expectations, Sam.){/i}"
    "[Name]" "{i}(I could look at you forever.){/i}"
    "[Name]" "{i}(But I don't want to miss other parts.){/i}"
    show sc i_Samantha_NV_12 with my_dissolve
    "[Name]" "{i}(Your white panties are so cute..){/i}"
    "[Name]" "{i}(I'm sure it's even better undernrath them.){/i}"
    show sc i_Samantha_NV_13 with my_dissolve
    "[Name]" "{i}(Let me try to move your skirt a little but...){/i}"
    show sc i_Samantha_NV_16 with my_dissolve
    "Samantha" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I think she could wake up any minute.){/i}"
    "[Name]" "{i}(Better get out of here.){/i}"
    return



label samantha_events_4_label_2:
    $ Q_NV_Samantha += 1

    scene sc i_Samantha_NV_1 with Dissolve(.5)


    "[Name]" "{i}(Samantha always looks so peaceful in her sleep.){/i}"
    "[Name]" "{i}(Let's take a closer look at you.){/i}"
    show sc i_Samantha_NV_2 with my_dissolve
    "[Name]" "{i}(Sleeping beauty...){/i}"
    "[Name]" "{i}(I could have looked at you all night...){/i}"
    "[Name]" "{i}(Still hiding from me under the blanket, Samantha?){/i}"
    show sc i_Samantha_NV_3 with my_dissolve
    "[Name]" "{i}(Let's take that off...){/i}"
    "[Name]" "{i}(Oh wow...){/i}"
    show sc i_Samantha_NV_4 with my_dissolve
    "[Name]" "{i}(What a beauty...){/i}"
    "[Name]" "{i}(I've never thought you'd be that sexy, Sam...){/i}"
    show sc i_Samantha_NV_5 with my_dissolve
    "[Name]" "{i}(This time, I'll be more cautious.){/i}"
    "[Name]" "{i}(Oh, yes.){/i}"
    "[Name]" "{i}(Now I see all the best parts.){/i}"
    "[Name]" "{i}(To be honest...){/i}"
    show sc i_Samantha_NV_6 with my_dissolve
    "[Name]" "{i}(You've exceeded all my expectations, Sam.){/i}"
    "[Name]" "{i}(It's so hard to take your eyes off of them.){/i}"
    "[Name]" "{i}(Especially when you're dressed like that...){/i}"
    "[Name]" "{i}(I wonder if the fabric still feels the same?){/i}"
    show sc i_Samantha_NV_7 with my_dissolve
    "[Name]" "{i}(I just have to try it...){/i}"
    show sc i_Samantha_NV_anim_1 with my_dissolve
    "[Name]" "{i}(Oh yes...){/i}"
    "[Name]" "{i}(It's the best feeling I've ever had...){/i}"
    "[Name]" "{i}(The fabric of your bra is so soft and tender...){/i}"
    show sc i_Samantha_NV_anim_2 with my_dissolve
    "[Name]" "{i}(And your breasts...){/i}"
    "[Name]" "{i}(You're driving me crazy...){/i}"
    "[Name]" "{i}(Between the softness and firmness of your breasts.){/i}"
    "Samantha" "Ah..."
    show sc i_Samantha_NV_16 with my_dissolve
    "[Name]" "{i}(I have to stop before she woke up!){/i}"
    "[Name]" "{i}(Shit, I think it's better to run away.){/i}"
    "[Name]" "{i}(And get some sleep.){/i}"
    return



label samantha_events_4_label_3:
    $ Q_NV_Samantha += 1

    scene sc i_Samantha_NV_1 with Dissolve(.5)



    "[Name]" "{i}(Samantha always looks so peaceful in her sleep.){/i}"
    "[Name]" "{i}(Let's take a closer look at you.){/i}"
    show sc i_Samantha_NV_2 with my_dissolve
    "[Name]" "{i}(Sleeping beauty...){/i}"
    "[Name]" "{i}(I could have looked at you all night...){/i}"
    "[Name]" "{i}(Still hiding from me under the blanket, Samantha?){/i}"
    show sc i_Samantha_NV_3 with my_dissolve
    "[Name]" "{i}(Let's take that off...){/i}"
    "[Name]" "{i}(Oh wow...){/i}"
    show sc i_Samantha_NV_4 with my_dissolve
    "[Name]" "{i}(What a beauty...){/i}"
    "[Name]" "{i}(I've never thought you'd be that sexy, Sam...){/i}"
    show sc i_Samantha_NV_5 with my_dissolve
    "[Name]" "{i}(This time, I'll be more cautious.){/i}"
    "[Name]" "{i}(Oh, yes.){/i}"
    "[Name]" "{i}(Now I see all the best parts.){/i}"
    "[Name]" "{i}(To be honest...){/i}"
    show sc i_Samantha_NV_6 with my_dissolve
    "[Name]" "{i}(You've exceeded all my expectations, Sam.){/i}"
    "[Name]" "{i}(Sometimes you're even too gorgeus...){/i}"
    "[Name]" "{i}(I wonder what you're wearing underneath today...){/i}"
    show sc i_Samantha_NV_12 with my_dissolve
    "[Name]" "{i}(Oh, Samantha... Let me see your temple.){/i}"
    "[Name]" "{i}(What could be more beautiful?){/i}"
    show sc i_Samantha_NV_12 with my_dissolve
    "[Name]" "{i}(Let's lift that skirt...){/i}"
    show sc i_Samantha_NV_13 with my_dissolve
    "[Name]" "{i}(That's much better.){/i}"
    "[Name]" "{i}(What a nice view I have!){/i}"
    "[Name]" "{i}(I wounder if you're ready for some rubbing...){/i}"
    show sc i_Samantha_NV_14 with my_dissolve
    "[Name]" "{i}(Just one gentle touch...){/i}"
    "[Name]" "{i}(I have contact.){/i}"
    "[Name]" "{i}(I can feel your whole body tense...){/i}"
    "[Name]" "{i}(I bet you haven't felt man's touch for a while...){/i}"
    "Samantha" "Ah..."
    show sc i_Samantha_NV_16 with my_dissolve
    "[Name]" "{i}(I have to stop before she woke up!){/i}"
    "[Name]" "{i}(Shit, I think it's better to run away.){/i}"
    "[Name]" "{i}(And get some sleep.){/i}"

    return



label samantha_events_4_label_4:

    $ unlock_gallery('images/ero/NV_Samantha.png')


    scene sc i_Samantha_NV_1 with Dissolve(.5)


    "[Name]" "{i}(Samantha always looks so peaceful in her sleep.){/i}"
    "[Name]" "{i}(Let's take a closer look at you.){/i}"
    show sc i_Samantha_NV_2 with my_dissolve
    "[Name]" "{i}(Sleeping beauty...){/i}"
    "[Name]" "{i}(I could have looked at you all night...){/i}"
    "[Name]" "{i}(Still hiding from me under the blanket, Samantha?){/i}"
    show sc i_Samantha_NV_3 with my_dissolve
    "[Name]" "{i}(Let's take that off...){/i}"
    "[Name]" "{i}(Oh wow...){/i}"
    show sc i_Samantha_NV_4 with my_dissolve
    "[Name]" "{i}(What a beauty...){/i}"
    "[Name]" "{i}(I've never thought you'd be that sexy, Sam...){/i}"
    show sc i_Samantha_NV_5 with my_dissolve
    "[Name]" "{i}(This time, I'll be more cautious.){/i}"
    "[Name]" "{i}(Oh, yes.){/i}"
    "[Name]" "{i}(Now I see all the best parts.){/i}"
    "[Name]" "{i}(To be honest...){/i}"
    show sc i_Samantha_NV_6 with my_dissolve
    "[Name]" "{i}(You've exceeded all my expectations, Sam.){/i}"
    "[Name]" "{i}(It's so hard to take your eyes off of them.){/i}"
    "[Name]" "{i}(Especially when you're dressed like that...){/i}"
    "[Name]" "{i}(I wonder if the fabric still feels the same?){/i}"
    show sc i_Samantha_NV_7 with my_dissolve
    "[Name]" "{i}(I just have to try it once again...){/i}"
    show sc i_Samantha_NV_anim_1 with my_dissolve
    "[Name]" "{i}(Oh yes...){/i}"
    "[Name]" "{i}(It's the best feeling I've ever had...){/i}"
    "[Name]" "{i}(The fabric of your bra is so soft and tender...){/i}"
    show sc i_Samantha_NV_anim_2 with my_dissolve
    "[Name]" "{i}(And your breasts...){/i}"
    "[Name]" "{i}(You're driving me crazy...){/i}"
    show sc i_Samantha_NV_8 with my_dissolve
    "[Name]" "{i}(Alright. I should stop for now.){/i}"
    "[Name]" "{i}(And pay some attention to other honey spots...){/i}"
    show sc i_Samantha_NV_12 with my_dissolve
    "[Name]" "{i}(Oh, Samantha... Let me see your temple.){/i}"
    "[Name]" "{i}(What could be more beautiful?){/i}"
    show sc i_Samantha_NV_13 with my_dissolve
    "[Name]" "{i}(Let's lift that skirt...){/i}"
    "[Name]" "{i}(That's much better.){/i}"
    "[Name]" "{i}(What a nice view I have!){/i}"
    "[Name]" "{i}(I wounder if you're ready for some rubbing...){/i}"
    show sc i_Samantha_NV_14 with my_dissolve
    "[Name]" "{i}(Just one gentle touch...){/i}"
    "[Name]" "{i}(I have contact.){/i}"
    "[Name]" "{i}(I can feel your whole body tense...){/i}"
    "[Name]" "{i}(I bet you haven't felt man's touch for a while...){/i}"
    "Samantha" "Ah..."
    "[Name]" "{i}(Do you like it?!){/i}"
    show sc i_Samantha_NV_15 with my_dissolve
    "[Name]" "{i}(Let;s make it even better...){/i}"
    "[Name]" "{i}(You don't really need those panties right now...){/i}"
    "[Name]" "{i}(I hope you're having a spicy dream right now.){/i}"
    "[Name]" "{i}(Let's take them off...){/i}"
    show sc i_Samantha_NV_16 with my_dissolve
    "Samantha" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I think she might wake up...){/i}"
    "[Name]" "{i}(Better get out of here.){/i}"

    return


label Samantha_6_label:
    scene sc i_Samantha_6_1 with Dissolve(.5)
    "Samantha" "...And then she added gnoll blood instead of gnoll saliva."
    "Samantha" "Everything in that class was covered in pink stinky goo."
    show sc i_Samantha_6_2 with my_dissolve
    "Samantha" "Sabrina was furious..."
    "Samantha" "That's pretty much everything interesting that happened to me lately."
    "Samantha" "How was your day?{w} You know, before saving my life."
    show sc i_Samantha_6_3 with my_dissolve
    "[Name]" "{i}(Oh, that's why she's been telling me all of this?){/i}"
    "[Name]" "{i}(At what point I've made the mistake of asking how was her day?){/i}"
    "[Name]" "It doesn't really matter, Sam. We have more important things to talk about."
    show sc i_Samantha_6_4 with my_dissolve
    "Samantha" "What's the matter?"
    "[Name]" "It's about your problem."
    "[Name]" "The compress I gave you can cure ruptured ligaments."
    "[Name]" "But the rupture was caused by something..."
    show sc i_Samantha_6_5 with my_dissolve
    "Samantha" "What are you talking about?"
    "Samantha" "Is there something wrong with me?"
    "[Name]" "Not with you."
    show sc i_Samantha_6_6 with my_dissolve
    "[Name]" "Frollo said, that stirring different magical energy can be the problem."
    "[Name]" "As if some other creature somehow affects your magic."
    scene expression '#000' with Dissolve(.5)
    $ renpy.pause(.55, hard = True)
    scene sc i_Samantha_6_7 with Dissolve(.5)
    "[Name]" "{i}(This is it! The look on her face...){/i}"
    "[Name]" "{i}(She's hidding something.){/i}"
    "[Name]" "{i}(But I have to be gentle...){/i}"
    "[Name]" "Nothing comes to your mind?"
    show sc i_Samantha_6_8 with my_dissolve
    "Samantha" "Not really."
    "Samantha" "It all sounds so strange."
    "Samantha" "Is he sure?"
    show sc i_Samantha_6_9 with my_dissolve
    "[Name]" "He sounded like he was sure. "
    "[Name]" "He would not lie to me. We made a deal."
    "Samantha" "What kind of deal, [Name]? That sounds dangerous."
    show sc i_Samantha_6_10 with my_dissolve
    "[Name]" "Do not switch the subject, Sam."
    "[Name]" "Do you undestrand how important this is?"
    show sc i_Samantha_6_11 with my_dissolve
    "Samantha" "I do!{w} I really do..."
    "Samantha" "But it's not that simple."
    "Samantha" "I'm afraid I don't know what's he talking about."
    show sc i_Samantha_6_12 with my_dissolve
    "[Name]" "Don't play fool with me, Sam!"
    "[Name]" "Maybe I'm not the brightest, but It's not that hard to see."
    show sc i_Samantha_6_13 with my_dissolve
    "Samantha" "Wh...{w} What are you talking about?"
    "[Name]" "Come on! You spend all your time with one person..."
    "Samantha" "Please, [Name], I don't want to talk about this."
    "[Name]" "About what?"
    "[Name]" "About the fact, that Audrey is..."
    show sc i_Samantha_6_14 with my_dissolve
    "Samantha" "Sh-h-h-h!"
    "Samantha" "NOT HERE!"
    "Samantha" "Nobody can know!"
    "[Name]" "{i}{i}(Wow... I was going to say \"somehow involved in this.\"){/i}{/i}"
    "[Name]" "{i}(But now I know I'm right.){/i}"
    "[Name]" "{i}(If Sam thinks I know already, I'll play along.){/i}"
    show sc i_Samantha_6_15 with my_dissolve
    "Samantha" "Please, [Name], you have to promise me you'll stay silent..."
    "Samantha" "Do you promise?"
    "[Name]" "Mhmhm..."
    "Samantha" "Nod if you agree."
    show sc i_Samantha_6_16 with my_dissolve
    "Samantha" "Good boy."
    "Samantha" "Now I let you go."
    show sc i_Samantha_6_17 with my_dissolve
    "[Name]" "I promised to Victoria that your problem won't happen again."
    "[Name]" "How can I be sure I keep my word if you're not willing to cooperate?"
    show sc i_Samantha_6_18 with my_dissolve
    "[Name]" "Guess I should tell Victoria all that I know, so she can handle this..."
    "Samantha" "No! You can't do that! "
    show sc i_Samantha_6_19 with my_dissolve
    "Samantha" "They'll kill Audrey!"
    "[Name]" "{i}(What the fuck? What exactly is happening here?!){/i}"
    show sc i_Samantha_6_20 with my_dissolve
    "Samantha" "[Name], dear [Name], please, you can't..."
    "[Name]" "{i}(Maybe I'll regret this, but it's not like I have a lot to tell Victoria about anyway...){/i}"
    show sc i_Samantha_6_21 with my_dissolve
    "[Name]" "Allright..."
    "[Name]" "But you have to tell me everything In details."
    "[Name]" "Otherwise I won't be able to help you."
    show sc i_Samantha_6_22 with my_dissolve
    "Samantha" "You're right. "
    "Samantha" "I promise, I will."
    show sc i_Samantha_6_23 with my_dissolve
    "Samantha" "But right now I have to get to class. Audrey is waiting..."
    "[Name]" "Then when?"
    show sc i_Samantha_6_24 with my_dissolve
    "Samantha" "Let's meet at noon in my room."
    "Samantha" "I'll make sure that no one will disturb is there."
    "[Name]" "Alright..."
    "[Name]" "Cya."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
