
label sabrina_events_label:
    $ tmp_variable_up_now = 'Q_Sabrina'
    $ tmp_QLOG_all        = ['QLOG_Sabrina', 2]

    call hide_all_main_interfaces from _call_hide_all_main_interfaces

    $ set_now = sabrina_events_set
    menu:
        "Attend lesson" if True:


            if not Q_Sabrina:
                if Q_Victoria < 1:
                    call Sabrina_1_1_label from _call_Sabrina_1_1_label

                    $ log_message.update({"QLOG_Sabrina":1 })
                    show screen main_interface 
                    hide screen black_tmp_screen_menu

                    with Dissolve(.5)
                    jump main_interface_label
                elif True:

                    call Sabrina_1_label from _call_Sabrina_1_label
                    $ p_up('Sabrina', 2)
            elif Q_Sabrina ==1:

                call Sabrina_2_label from _call_Sabrina_2_label
                $ p_up('Sabrina', 3)
            elif Q_Sabrina ==2:

                call Sabrina_3_label from _call_Sabrina_3_label
                $ p_up('Sabrina', 4)
            elif Q_Sabrina ==3:

                call Sabrina_4_label from _call_Sabrina_4_label
                #$ Q_Sabrina = 4
                $ p_up('Sabrina', 5)
            else:

                $ log_message.update({'QLOG_Sabrina': 3})
                $ p_up('Sabrina', 6)
                if renpy.music.get_playing():
                    stop music fadeout 1
                    play music_2 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
                elif renpy.music.get_playing('music_2'):
                    stop music_2 fadeout 1
                    play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
                elif True:
                    stop music_2 fadeout 1
                    play music 'audio_ep2/SC/25. Main Menu.mp3' fadein 2
                jump test_potion_makes_label
                jump exit_from_event
        "Not now" if True:
            show screen main_interface 
            show screen show_hide_locations_2
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    $ Q_Sabrina += 1

    $ log_message.update({'QLOG_Sabrina': 2})
    jump exit_from_event


label Sabrina_1_label:
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
    show sc i_Sabrina_1_1 with Dissolve(.5)
    "Sabrina" "Students!"
    "Sabrina" "Welcome to our first Potions class."
    "Sabrina" "My name is Miss Sabrina Spellman."
    "Sabrina" "I will be your teacher."
    show sc i_Sabrina_1_4 with my_dissolve
    "Sabrina" "What do you think of our interior design?"
    "Sabrina" "I can tell by your wide eyes that you've noticed."
    "Sabrina" "It's quite unusual, isn't it?"
    "Sabrina" "That's because our classroom..."
    show sc i_Sabrina_1_5 with my_dissolve
    "Sabrina" "...is the last remnant of the original academy."
    "Sabrina" "When Cordale was restored all the rooms were gradually modernized."
    "Sabrina" "All of them except this classroom."
    "Sabrina" "Its walls and floor are soaked in the fumes of hundreds of thousands of magical elixirs."
    "Sabrina" "And that somehow makes them indestructible."
    "Sabrina" "The headmaster has long wondered how to get rid of this effect."
    show sc i_Sabrina_1_20 with my_dissolve
    "Sabrina" "But so far no one has been able to find a way."
    "[Name]" "{i}(Can potions do that?){/i}"
    "[Name]" "{i}(Or is it just a story to justify the disrepair?){/i}"
    "[Name]" "{i}(I'll have to ask Elijah.){/i}"
    "Sabrina" "That concludes our forays into Cordale's history."
    show sc i_Sabrina_1_16 with my_dissolve
    "Sabrina" "Today you begin your study of the noble art of Potions."
    "Sabrina" "But I hasten to disappoint you! You won't be going near the cauldrons today!"
    "Sabrina" "Because a couple of years ago, some of the freshmen..."
    "Sabrina" "Didn't follow the safety instructions."
    "Sabrina" "There was a minor incident."
    show sc i_Sabrina_1_15 with my_dissolve
    "Sabrina" "And there were a few casualties."
    "[Name]" "{i}(What the fuck?){/i}"
    "[Name]" "{i}(She's saying it's more dangerous to make potions than to do magic.){/i}"
    "Sabrina" "So now the learning process has been relaxed."
    show sc i_Sabrina_1_20 with my_dissolve
    "Sabrina" "Today we start with theory."
    "Sabrina" "Then there's safety stuff."
    "Sabrina" "And only then will we begin the real magic..."
    "Sabrina" "...of the subject of potions."
    show sc i_Sabrina_1_15 with my_dissolve
    "Sabrina" "We're clear on that. Or are there any questions?"
    $ sabrina_set = set()
label Sabrina_1_label_34:
    menu:
        set sabrina_set
        "Are they dead?" if True:
            $ pass
        "Why do wizards need potions?" if True:
            jump Sabrina_1_label_44
        "No questions" if True:
            jump Sabrina_1_label_54

    show sc i_Sabrina_1_15 with my_dissolve
    "[Name]" "Excuse me! Did you say \"casualties\"?"
    "[Name]" "Is brewing potions that dangerous?!"
    show sc i_Sabrina_1_16 with my_dissolve
    "Sabrina" "Of course not!"
    "Sabrina" "It was a very unfortunate set of circumstances."
    "Sabrina" "There's nothing safer than brewing potions!"
    show sc i_Sabrina_1_19 with my_dissolve
    "Sabrina" "I've devoted my whole life to it and look at me."
    "Sabrina" "Not a scar, not a scratch!"
    "Sabrina" "So don't worry about that silly story!"
    "[Name]" "You've made me feel much better."
    jump Sabrina_1_label_34
label Sabrina_1_label_44:
    show sc i_Sabrina_1_15 with my_dissolve
    "[Name]" "I don't mean to sound ignorant."
    "[Name]" "But this whole world of magic is new to me."
    "[Name]" "If wizards can conjure, why would they need potions?"
    show sc i_Sabrina_1_20 with my_dissolve
    "Sabrina" "Oh."
    "Sabrina" "I confess, for a potions teacher, such a question is..."
    "Sabrina" "Insulting!"
    "Sabrina" "But I will forgive you."
    show sc i_Sabrina_1_19 with my_dissolve
    "Sabrina" "Especially since this is an important topic!"
    "Sabrina" "Which we will discuss during today's class."
    "[Name]" "Thank you very much."
    jump Sabrina_1_label_34
label Sabrina_1_label_54:

    "[Name]" "So far, everything is clear."
    show sc i_Sabrina_1_17 with my_dissolve
    "Sabrina" "The main topic of today's introductory class will be potions."
    "Sabrina" "And why you should learn the art of making these magical drinks."
    "Sabrina" "I'm sure Ms. Lapis has already told you about the sources of power."
    "Sabrina" "And that magic is as much a part of nature as you or me are."
    show sc i_Sabrina_1_10 with my_dissolve
    "Carter" "Yes, we've just been through that."
    "Grace" "But what does this have to do with potions?"
    show sc i_Sabrina_1_11 with my_dissolve
    "Sabrina" "Not all sources of magic are equally subject the power of mages."
    "Sabrina" "Especially since every mage's connection to the elements is individual."
    "Sabrina" "And with potions, any mage can overcome those laws."
    "Sabrina" "Potions help confuse enemies, enhance your skills, and heal wounds quickly."
    "Sabrina" "A skilled potion-maker can grant power and take life."
    "Sabrina" "With just one drop."
    show sc i_Sabrina_1_16 with my_dissolve
    "Sabrina" "The Potions course goal is..."
    "Sabrina" "...Is to teach you how to determine the magical properties of the ingredients."
    "Sabrina" "As well as how to mix and prepare them to obtain the desired effects."
    "Sabrina" "You all should have received your textbooks."
    "Sabrina" "They will be your trusty book of recipes and tips."
    "Sabrina" "Carry them to every class."
    show sc i_Sabrina_1_23 with my_dissolve
    "Sabrina" "Because you can only access the cauldron if you have the textbook."
    "Sabrina" "Safety precautions."
    "Sabrina" "Your home assigment is to..."
    "Sabrina" "Study paragraphs 1 and 2 in your textbooks."
    show sc i_Sabrina_1_22 with my_dissolve
    "Sabrina" "Memorize the ingredients for all the potions mentioned in the paragraphs."
    "Sabrina" "It's necessary so that we can go into practice."
    "Sabrina" "And brew the first real potion!"
    "Sabrina" "I'm looking forward to it myself!"
    "Sabrina" "Class dismissed!"
    return



label Sabrina_2_label:
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

    show sc i_Sabrina_1_1 with Dissolve(.5)
    "Sabrina" "Students!"
    "Sabrina" "Take your seats, class is about to begin!"
    "Sabrina" "Now, what did I ask you to do... Oh, right!"
    show sc i_Sabrina_1_5 with my_dissolve
    "Sabrina" "I hope you all prepared and read paragraphs 1 and 2?"
    "[Name]" "{i}(We had an assigment?){/i}"
    "[Name]" "{i}(Damn, I totally forgot about that...){/i}"
    show sc i_Sabrina_1_4 with my_dissolve
    "Sabrina" "I don't think there's any need to waste time checking..."
    "Sabrina" "Except for some spot checks!"
    "Sabrina" "I was just about to brew myself a lesser healing potion."
    show sc i_Sabrina_1_21 with my_dissolve
    "Sabrina" "And I totally forgot what to put in it."
    "Sabrina" "Who wants to come to the kettle and help me?"
    show sc i_Sabrina_1_22 with my_dissolve
    "Sabrina" "Who can show me what we put in the lesser healing potion?"
    "[Name]" "{i}(I think I saw something like this when I opened the textbook.){/i}"
    "[Name]" "{i}(Should I try to remember?){/i}"

    menu:
        "Try to answer" if True:
            $ pass
        "Stay silent" if True:
            show sc i_Sabrina_1_23 with my_dissolve
            "[Name]" "{i}(I don't think I can remember what the composition is.){/i}"
            "Sabrina" "What, no one?"
            show sc i_Sabrina_1_8 with my_dissolve
            "Grace" "I can try..."
            show sc i_Sabrina_1_7 with my_dissolve
            "Sabrina" "That's great, honey! Don't be so shy!"
            "Sabrina" "Come here."
            show sc i_Sabrina_1_27 with my_dissolve
            "Grace" "{b}Tears of woodland deer, unicorn hair powder, Icelandic cetraria.{/b}"
            show sc i_Sabrina_1_28 with my_dissolve

            "Sabrina" "That's right! Great job, Grace!"

            "[Name]" "{i}(Damn, she's good...){/i}"
            "[Name]" "{i}(I'm shure I'd forgot about cetraria...){/i}"
            jump Sabrina_2_label_46



    show sc i_Sabrina_1_14 with my_dissolve
    "[Name]" "Ms. Spellman."
    "[Name]" "I think I know the answer."
    show sc i_Sabrina_1_17 with my_dissolve
    "Sabrina" "All right! Come to the pot and show me."
    "[Name]" "Just a minute."
    "[Name]" "{i}(There was definitely something about tears and hair...){/i}"
    menu:
        "Unicorn tears, deer hair, Norwegian moss" if True:


            show sc i_Sabrina_1_39 with my_dissolve
            "[Name]" "Unicorn tears, woodland deer hair powder, Norwegian moss."
            "[Name]" "{i}(From the look on her face, I assume I got it all wrong.){/i}"
            show sc i_Sabrina_1_43 with my_dissolve
            "Sabrina" "Alas, this is wrong."
            "[Name]" "{i}(Damn, how could I mess this up!){/i}"
        "Goat tears, mockingbird feather, birch bark" if True:

            show sc i_Sabrina_1_39 with my_dissolve
            "[Name]" "Mountain goat tears, mockingbird feather, and European birch bark."
            "Sabrina" "What kind of nonsense is that?{w}Totally wrong."
            show sc i_Sabrina_1_43 with my_dissolve
            "Sabrina" "Absolutely wrong."
            "[Name]" "{i}(Damn, I was sure I've got it!){/i}"
        "Tears of deer, unicorn hair, Icelandic lichen" if True:
            show sc i_Sabrina_1_37 with my_dissolve
            "[Name]" "{b}Tears of woodland deer, unicorn hair powder, Icelandic cetraria.{/b}"
            "Sabrina" "That's right!"
            show sc i_Sabrina_1_47 with my_dissolve
            "Sabrina" "Good work, [Surname]."
            "[Name]" "{i}(Simple as that.){/i}"
            "Sabrina" "You've even got it in right order, i'm impressed!"

    jump Sabrina_2_label_46

label Sabrina_2_label_46:
    hide screen main_interface

    show sc i_Sabrina_1_18 with my_dissolve
    "Sabrina" "We'll go through the making of all the basic potions step by step in practice. "
    "Sabrina" "In the meantime, let's move on."
    "Sabrina" "The topic of today's lesson: the basics of safety."
    show sc i_Sabrina_1_15 with my_dissolve
    "Sabrina" "Unfortunately, many students without proper experience, how shall I say it..."
    "Sabrina" "Treat potion-making like making soup."
    show sc i_Sabrina_1_20 with my_dissolve
    "Sabrina" "With creativity."
    "Sabrina" "Measuring a pinch of salt to taste, freaking out and adding an ingredient of their own..."
    "Sabrina" "Forget that nonsense, or you'll be suspended from potionsmithing."
    show sc i_Sabrina_1_16 with my_dissolve
    "Sabrina" "For your own safety."
    "Sabrina" "Pottery and Alchemy are exact sciences."
    "Sabrina" "All details are extremely important!"
    show sc i_Sabrina_1_2 with my_dissolve
    "Sabrina" "Every milligram can have a disastrous effect on the outcome."
    "Sabrina" "A regeneration potion with the wrong kind of moss turns into magic acid."
    "Sabrina" "Drink that and all your insides will fit in one vial."
    "[Name]" "{i}(Ouch...){/i}"
    show sc i_Sabrina_1_4 with my_dissolve
    "Sabrina" "That's why it's crucial that you know the recipes for potions."
    "Sabrina" "Grams are important, too."
    show sc i_Sabrina_1_9 with my_dissolve
    "Sabrina" "Suppose you drink a substandard invisibility potion."
    "Sabrina" "Hoping to get through Dragon's Gorge."
    "Sabrina" "And in the middle of the way, the veil falls off?"
    "Sabrina" "Congratulations, you are now a barbecue."
    "[Name]" "{i}(Ouch...){/i}"
    show sc i_Sabrina_1_12 with my_dissolve
    "Sabrina" "And finally."
    "Sabrina" "If you go overboard with the ingredients without knowing their properties."
    "Sabrina" "You might not live long enough to spill the potion."
    "Sabrina" "Don't get me wrong, these walls are indestructible."
    show sc i_Sabrina_1_20 with my_dissolve
    "Sabrina" "But I'm getting tired of scrubbing students's guts out of them..."
    "[Name]" "{i}(Ouch...){/i}"
    "Sabrina" "Because they ignored the simple rules in the recipes."
    show sc i_Sabrina_1_19 with my_dissolve
    "Sabrina" "I hope everyone understands me."
    "Sabrina" "That's it for today!"
    return



label Sabrina_3_label:
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



    show sc i_Sabrina_1_1 with Dissolve(.5)
    "Sabrina" "Students!"
    "Sabrina" "Take your seats, class is about to begin!"
    show sc i_Sabrina_1_2 with my_dissolve
    "Sabrina" "The topic of today's lesson will be: preparing the workplace."
    "Sabrina" "Yes, yes, I know that safety classes aren't the most fun."
    "Sabrina" "But in the last class I let you know that it's important."
    "Sabrina" "First and foremost for your own safety."
    show sc i_Sabrina_1_5 with my_dissolve
    "[Name]" "{i}(Sabrina looks so unhappy when she teaches theory.){/i}"
    "[Name]" "{i}(It will be interesting to see her when we start making potions.){/i}"
    show sc i_Sabrina_1_22 with my_dissolve
    "Sabrina" "So, your workstation should consist of:"
    "Sabrina" "A cauldron of the capacity indicated in the recipe."
    "Sabrina" "For studies, we use table cauldrons, like mine."
    "Sabrina" "So the consequences are more easily managed."
    show sc i_Sabrina_1_16 with my_dissolve
    "Sabrina" "Next, your potions textbook."
    "Sabrina" "The textbook must be for your year."
    "Sabrina" "No missing pages."
    "Sabrina" "Next, the WFAK set."
    show sc i_Sabrina_1_10 with my_dissolve
    "Carter" "I'm sorry, what is a WFAK?"
    show sc i_Sabrina_1_12 with my_dissolve
    "Sabrina" "Wizard First Aid Kit."
    "Sabrina" "It's given out at the beginning of the practicum."
    "Sabrina" "It's a little potion that freezes you in time."
    "Sabrina" "For a while until the nurse can repair the damage."
    show sc i_Sabrina_1_10 with my_dissolve
    "Sabrina" "After which we unfreeze you."
    "Carter" "Holy crap!"
    "Carter" "That sounds a little too cool..."
    show sc i_Sabrina_1_11 with my_dissolve
    "Sabrina" "No one said the experience won't leave a mark."
    "Sabrina" "So it's best to follow the safety precautions."
    show sc i_Sabrina_1_8 with my_dissolve
    "Sabrina" "Next, the alchemist's toolkit."
    "Sabrina" "It includes a scalpel, tweezers, a jeweler's hammer..."
    "Sabrina" "In short, everything you need to process the ingredients."
    "Sabrina" "It's given out at the beginning of the tutorial."
    show sc i_Sabrina_1_5 with my_dissolve
    "Sabrina" "If you wish to make a potion outside of class."
    show sc i_Sabrina_1_4 with my_dissolve
    "Sabrina" "It's best not to."
    "Sabrina" "Or at the very least consult me."
    show sc i_Sabrina_1_2 with my_dissolve
    "Sabrina" "Remember, these rules are not there to coddle you."
    "Sabrina" "You are mature enough."
    "Sabrina" "This is an attempt to keep young and talented wizards..."
    "Sabrina" "From dying young."
    show sc i_Sabrina_1_1 with my_dissolve
    "[Name]" "{i}(I thought Sabrina really didn't like theory...){/i}"
    "[Name]" "{i}(But despite that, she takes it very seriously.){/i}"
    "Sabrina" "That's it for today!"
    "Sabrina" "You're all free to go."
    return


label Sabrina_4_label:
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
    show sc i_Sabrina_1_18 with Dissolve(.5)
    "Sabrina" "Let's get this class started!"
    "Sabrina" "Good afternoon, students."
    show sc i_Sabrina_1_16 with my_dissolve
    "Sabrina" "Today we have a rather entertaining lesson."
    "Sabrina" "We are going to try to make a potion of regeneration together."
    "[Name]" "No way!"
    "[Name]" "Are we finally ready to make potions?"
    show sc i_Sabrina_1_19 with my_dissolve
    "Sabrina" "Ah-ha-ha."
    "Sabrina" "Mr. [Surname], please be serious."
    show sc i_Sabrina_1_17 with my_dissolve
    "Sabrina" "Of course it's too early for you to make your own potions."
    "Sabrina" "But you can already assist the potion-maker."
    show sc i_Sabrina_1_22 with my_dissolve
    "Sabrina" "The potion base is boiling in the cauldron on my table."
    "Sabrina" "Your task is to come and add the ingredient under my supervision."
    "Sabrina" "Before you do so, prepare it properly and measure the dosage."
    "Sabrina" "If you succeed, the potion will turn a light pink color."
    show sc i_Sabrina_1_14 with my_dissolve
    "[Name]" "What if it doesn't?"
    "Sabrina" "It depends on which ingredient you get wrong."
    show sc i_Sabrina_1_16 with my_dissolve
    "Sabrina" "It can go off..."
    "[Name]" "This potions class is like a minefield."
    show sc i_Sabrina_1_19 with my_dissolve
    "Sabrina" "Ah-ha-ha."
    "Sabrina" "Sorry, I couldn't resist."
    "Sabrina" "I didn't scare you for nothing for three lessons."
    "Sabrina" "Don't be scared. Everything's under control."
    "Sabrina" "Well, maybe Mr. [Surname] would like to volunteer, then."

    scene sc i_Sabrina_1_17 with Dissolve(.5)
    menu:
        "Find an excuse" if True:
            $ pass
        "Accept" if True:
            jump Sabrina_4_label_55
    show sc i_Sabrina_1_14 with my_dissolve
    "[Name]" "I can try..."
    show sc i_Sabrina_1_13 with my_dissolve
    "[Name]" "Oh, no, you know..."
    "Sabrina" "What's the matter, are you scared?"
    "[Name]" "Not at all, I'm just..."
    show sc i_Sabrina_1_15 with my_dissolve
    "Sabrina" "Not interested in trying your hand at potion brewing?"
    "Sabrina" "Maybe you find my subject boring?"
    "[Name]" "No, it's not, it's..."
    "[Name]" "{i}(Think of something!){/i}"
    "[Name]" "I just don't feel well!"
    "[Name]" "I've been nauseous and queasy all morning."
    show sc i_Sabrina_1_17 with my_dissolve
    "Sabrina" "[Name], why do you come to class in such a state?"
    "Sabrina" "Didn't your headmaster explain to you how it worls here?"
    "Sabrina" "We're not beasts, you should have stayed home..."
    show sc i_Sabrina_1_18 with my_dissolve
    "[Name]" "I thought I could handle it."
    "[Name]" "I didn't want to miss your class."
    show sc i_Sabrina_1_20 with my_dissolve
    "Sabrina" "It's a admirable initiative, but you should've thought it through carefully."
    "Sabrina" "Take care of your health, [Surname]."
    "Sabrina" "You're free to go."
    show sc i_Sabrina_1_8 with my_dissolve
    "Sabrina" "Grace, honey, will you step in?"
    "Grace" "Gladly!"
    show sc i_Sabrina_1_48 with my_dissolve
    "Grace" "Hey, [Name]!"
    "[Name]" "Yes?"
    show sc i_Sabrina_1_50 with my_dissolve
    "Grace" "Get well soon!"
    "[Name]" "Th-thank you..."
    "Grace" "Hi-hi..."
    show sc i_Sabrina_1_28 with my_dissolve
    "[Name]" "{i}(Strange, we've never talked to each other...){/i}"
    "[Name]" "{i}(But she's so nice to me...){/i}"
    "[Name]" "{i}(Alas, it's seems that today potions lesson is over for me.){/i}"

    return

label Sabrina_4_label_55:

    show sc i_Sabrina_1_19 with my_dissolve
    "[Name]" "Of course!"
    "[Name]" "What do I need to do?"
    "Sabrina" "Commendable zeal, [Surname]!"
    show sc i_Sabrina_1_22 with my_dissolve
    "Sabrina" "Come to my table."
    "Sabrina" "Do you see a board and a knife?"
    show sc i_Sabrina_1_42 with my_dissolve
    "Sabrina" "Please chop the cetraria according to the recipe and add it to the cauldron."
    "[Name]" "No problem. Where's the recipe?"
    show sc i_Sabrina_1_47 with my_dissolve
    "Sabrina" "In your head, of course."
    "[Name]" "Wait a minute...{w} What about the handbook on the table?"
    "[Name]" "Isn't that required by safety rules?"
    show sc i_Sabrina_1_41 with my_dissolve
    "Sabrina" "Well done, [Surname]!"
    "Sabrina" "You didn't fall into my trap."
    "Sabrina" "Here, take a textbook."
    "[Name]" "Thank you."
    show sc i_Sabrina_1_24 with my_dissolve
    "[Name]" "{i}(Three and a half grams? Piece of cake.){/i}"
    "[Name]" "{i}(Add...){/i}"
    "[Name]" "..."
    "[Name]" "{i}(Now a deer hair...){/i}"
    show sc i_Sabrina_1_25 with my_dissolve
    "[Name]" "{i}(Add...){/i}"
    "[Name]" "..."
    show sc i_Sabrina_1_38 with my_dissolve
    "Sabrina" "Well, let's see what you got, shall we?"
    "Sabrina" "It's gorgeous!"
    show sc i_Sabrina_1_41 with my_dissolve
    "Sabrina" "Look at that delicate shade of yellow."
    "[Name]" "Yes, it's beautiful."
    "Sabrina" "I'm impressed, [Surname]!"
    show sc i_Sabrina_1_47 with my_dissolve
    "Sabrina" "By the way, you can keep this potion for yourself.{w} That's a custom around here."
    "[Name]" "Thank you, ma'am! This is my first magical trophy!"
    "[Name]" "{i}(Damn, I'm good!){/i}"
    return


label Sabrina_1_1_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)
    show sc i_Sabrina_0_3 with Dissolve(.5)
    "Sabrina" "Where are you going, young man?"
    "[Name]" "To learn the basics of alchemy and potions, of course."
    "Sabrina" "I'm glad to hear you're interested in my subject."
    "Sabrina" "{b}Have you been to Victoria's introductory lecture yet?{/b}"
    "[Name]" "Um..."
    "[Name]" "No, do I have to?"
    "Sabrina" "Alas, yes."
    "[Name]" "The rule is that all students must attend an introductory lecture..."
    show sc i_Sabrina_0_4 with my_dissolve
    "Sabrina" "...before attending any other classes."
    "Sabrina" "{b}Come back when you attend Victoria's class.{/b}"
    scene expression '#000' with Dissolve(.5)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
