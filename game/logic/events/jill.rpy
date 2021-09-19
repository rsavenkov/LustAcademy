label faith_dale_spa_1_label:
label jill_events_label:


    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.1)
    if not hasattr(store, 'Q_Jill'):
        $ Q_Jill = 0
    #$ set_now = elijah_events_set
    menu:
        "!Order a massage ($75)" if (money <  75) and not (Q_Jill == 3  and dow == 'SAT'):
            $ pass
        "1 Order a massage ($75)" if Q_Jill == 1 and dow == 'SAT' and money >= 75:
            if money < 75:
                jump jill_events_label
            $ money -= 75
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
            call Jill_2_label from _call_Jill_2_label
            
            $ p_up('Jill', 2)
            $ Q_Jill=2
            $ change_location_2('dale_mainstreet', 3)

        "2 Order a massage ($75)" if Q_Jill == 2 and dow == 'SAT' and money >= 75:
            if money < 75:
                jump jill_events_label
            $ money -= 75
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
            call Jill_3_label from _call_Jill_3_label
            $ p_up('Jill', 3)
            $ Q_Jill=4
            $ change_location_2('dale_mainstreet', 3)

        "3 Order a massage" if Q_Jill == 3  and dow == 'SAT':
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
            call Jill_0_label from _call_Jill_0_label
        "Not now":

            show screen main_interface 
            show screen show_hide_locations_2
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label


label Jill_2_label:


    show sc i_Jill_1_1 with my_dissolve
    "[Name]" "You know, I think I'm going to try your famous massage."
    "Jill" "Yay, yay, yay! I'm sure you'll love it!"
    show sc i_Jill_1_16 with my_dissolve
    "Jill" "Go through that door over there and get ready."
    "Jill" "The massage therapist will be right with you."
    "[Name]" "Thank you, "
    scene image '#000' with Dissolve(.5)
label Jill_2_label_8:
    scene sc i_Massage_1_1 with Dissolve(.5)
    "[Name]" "{i}(What a nice vibe).{/i}"
    "[Name]" "{i}(And it smells incredible!){/i}"
    show sc i_Massage_1_2 with my_dissolve
    "[Name]" "{i}(But who's going to massage me?){/i}"
    "[Name]" "{i}(What am I supposed to do? Is there a bell?){/i}"
    show sc i_Massage_1_3 with my_dissolve
    "[Name]" "Excuse me, is there someone here?"
    "[Name]" "What... what should I do?"
    show sc i_Massage_1_4 with my_dissolve
    "Jill" "Oh! Excuse me! I'm on my way."
    "Jill" "Take your clothes off and lie down."
    "Jill" "Face down."
    show sc i_Massage_1_5 with my_dissolve
    "[Name]" "{i}(It isn't very comfortable to undress like this...){/i}"
    "[Name]" "Do I have to take all my clothes off?"
    "Jill" "You can leave your underwear on if you're embarrassed."
    "[Name]" "{i}(I don't have anything to be embarrassed about...){/i}"
    scene image '#000' with Dissolve(.5)
    scene sc i_Massage_1_6 with Dissolve(.5)
    "Jill" "Hi! I'm so sorry!"
    "Jill" "Lost track of time while planning a pra..."
    show sc i_Massage_1_7 with my_dissolve
    "Jill" "Nevermind. My name is Faith and I'm happy to relieve you."
    "[Name]" "What?"
    show sc i_Massage_1_8 with my_dissolve
    "Faith" "You know, your muscle pain."
    show sc i_Massage_1_9 with my_dissolve
    "Faith" "Your shoulders look stiff."
    "[Name]" "It hurts..."
    show sc i_Massage_1_10 with my_dissolve
    "Faith" "It hurts to see a beautiful body treated like this."
    "Faith" "It deserves some love..."
    show sc i_Massage_1_11 with my_dissolve
    "Faith" "Your legs..."
    "Faith" "You were a professional sportsman, weren't you?"
    "[Name]" "How do you know?"
    show sc i_Massage_1_12 with my_dissolve
    "Faith" "It's easy to tell if someone was pushing his muscles to the limits."
    "Faith" "But don't worry sweety! I know how to treat a man."
    "[Name]" "{i}(I swear to god she's fooling around with me!){/i}"
    show sc i_Massage_1_13 with my_dissolve
    "Faith" "Just relax and let my touch take your pain away..."
    "[Name]" "{i}(My leg...What's going on?){/i}"
    "[Name]" "It hurts..."
    show sc i_Massage_1_14 with my_dissolve
    "Faith" "I know... But I feel how brave you are."
    "Faith" "How strong you are..."
    "Faith" "I know you can take it..."
    "[Name]" "{i}(I don't know if it's sexy or creepy... Can it be both?){/i}"
    show sc i_Massage_1_15 with my_dissolve
    "Faith" "Are you comfortable?"
    "[Name]" "Um...Y-yes, I guess."
    "[Name]" "{i}(I swear I can feel her wet panties on my skin.){/i}"
    "[Name]" "That's an unusual position."
    "Faith" "You have such a broad back. There's no other way I can manage."
    show sc i_Massage_1_16 with my_dissolve
    "[Name]" "{i}(What kind of salon is this?){/i}"
    "Faith" "You're too tense... Ah..."
    show sc i_Massage_1_17 with my_dissolve
    "Faith" "Relax your shoulders... Ah... Now we'll give them a good..."
    "Faith" "Stretch them."
    show sc i_Massage_1_18 with my_dissolve
    "[Name]" "{i}(Is it me, or is she vibrating... there?){/i}"
    "Faith" "Oh... Yeah... What the hell is that...."
    show sc i_Massage_1_17 with my_dissolve
    "[Name]" "Is something wrong?"
    "Faith" "Sorry...It's just..."
    show sc i_Massage_1_19 with my_dissolve
    "Faith" "I can't get a feel for your chakras."
    "Faith" "Don't mind me."
    "Faith" "It's just a routine procedure..."
    "Faith" "Ah... Ah... And!.."
    show sc i_Massage_1_20 with my_dissolve
    "Faith" "That's it!"
    "[Name]" "That's it?"
    "Faith" "That's it! The massage is over... Sorry, I have to run."
    show sc i_Massage_1_21 with my_dissolve
    "Faith" "It's very urgent..."
    "[Name]" "Wait a minute!"
    show sc i_Massage_1_22 with my_dissolve
    "[Name]" "{i}(Yeah... She's weird.){/i}"
    "[Name]" "{i}(She only made me tense, but she didn't make it any easier!){/i}"
    scene image '#000' with Dissolve(.5)
    scene sc i_Massage_1_23 with Dissolve(.5)
    "[Name]" "Yeah... That's was a strange massage."
    "[Name]" "Hmm... Is no one here?"
    show sc i_Massage_1_24 with my_dissolve
    "[Name]" "{i}(Wait, I think I hear something...){/i}"
    "[Name]" "{i}(Is someone cursing behind the wall?){/i}"
    show sc i_Massage_1_25 with my_dissolve
    "Faith" "Are you crazy?!"
    "Faith" "You're embarrassing me in front of a new client!"
    "Faith" "Pranks have limits, too!"
    "Jill" "Come on. He's a young guy."
    "Jill" "I'm sure he liked everything."
    "Faith" "That's not the point!"
    "Jill" "I'm going for a walk. Your angry face is freaking me out.)"
    show sc i_Massage_1_26 with my_dissolve
    "[Name]" "{i}(Well, I'd better pretend I left earlier and didn't hear anything.){/i}"
    "[Name]" "{i}(I'll see what I can squeeze out of this situation next time.){/i}"


    return

label Jill_0_label:

    show sc i_Jill_1_9 with my_dissolve
    "[Name]" "Hey! I'm back for your famoust massage!"
    "Jill" "Hi there! "
    "Jill" "Let me see..."
    show sc i_Jill_1_13 with my_dissolve
    "Jill" "Sorry, I guess all hours for the next five days are booked."
    "[Name]" "Really?"
    show sc i_Jill_1_3 with my_dissolve
    "Jill" "Well, we are the best."
    "[Name]" "Huh. I guess I'll visit next time."
    "Jill" "We'll be waiting for you, sir."
    scene image '#000' with Dissolve(.5)

    return

label Jill_3_label:

    show sc i_Jill_1_1 with my_dissolve
    "[Name]" "Hey! I'm here for your famoust massage!"
    "Jill" "Nice to see you!"
    show sc i_Jill_1_16 with my_dissolve
    "Jill" "Go through that door over there and get ready."
    "Jill" "The massage therapist will be right with you."
    "[Name]" "Thank you, "
    show sc i_Massage_1_2 with my_dissolve
    "[Name]" "{i}(It still smells nice in here...){/i}"
    "[Name]" "{i}(It makes me feel so peaceful.){/i}"
    "[Name]" "Hi! I signed up for a massage."
    show sc i_Massage_1_4 with my_dissolve
    "Jill" "Come on in and get undressed!"
    "Jill" "I'll be right out."
    show sc i_Massage_2_1 with my_dissolve
    "[Name]" "{i}(Same voice...){/i}"
    "[Name]" "{i}(I wonder if she'll follow through this time.){/i}"
    "[Name]" "{i}(Although I don't mind feeling her body quiver with pleasure again...){/i}"
    show sc i_Massage_1_6 with my_dissolve
    "Jill" "{i}(Welcome!){/i}"
    "Jill" "My name is..."
    show sc i_Massage_2_10 with my_dissolve
    "[Name]" "{i}(Wait a minute... She was the one who wasn't the receptionist...){/i}"
    "[Name]" "{i}(And her name was definitely Jill.){/i}"
    "[Name]" "{i}(But last time the masseuse introduced herself to me...){/i}"
    show sc i_Massage_1_7 with my_dissolve
    "[Name]" "Faith, right?"
    "Faith" "Yes."
    "[Name]" "I was here before the other day."
    show sc i_Massage_2_2 with my_dissolve
    "Faith" "Oh, it's you..."
    "Faith" "I'm very sorry that your last massage was cut short..."
    show sc i_Massage_2_3 with my_dissolve
    "Faith" "It was because of... Well..."
    menu:
        "Tease her":
            show sc i_Massage_2_4 with my_dissolve
            "[Name]" "What do you mean? Isn't that part of the program?"
            "[Name]" "That's all I came back for!"
            "Faith" "Um... Well..."
            show sc i_Massage_2_5 with my_dissolve
            "[Name]" "Relax, I was just kidding."
            "[Name]" "I'll have a regular massage, please."
            show sc i_Massage_2_6 with my_dissolve
            "[Name]" "Just this once."
            "Faith" "If you say so."
        "Calm her ":
            show sc i_Massage_2_7 with my_dissolve
            "[Name]" "What do you mean? I don't remember anything like that."
            "Faith" "Well, I mean..."
            "[Name]" "It wasn't anything like that, Faith. Don't worry about it."
            show sc i_Massage_2_8 with my_dissolve
            "Faith" "Th-thank you..."
            "[Name]" "So, can you help me de-stress?"
            show sc i_Massage_2_9 with my_dissolve
            "Faith" "..."
            "[Name]" "{i}(I think I sent if too many mixed signals.){/i}"
            "[Name]" "Massage, baby. I mean massage."
            show sc i_Massage_2_6 with my_dissolve
            "Faith" "Àh... Ah-ha-ha!"
            "Faith" "Of course I can."
    show sc i_Massage_1_9 with my_dissolve
    "Faith" "Your shoulders look stiff."
    "[Name]" "It hurts..."
    "Faith" "It hurts to see a beautiful body treated like this."
    "Faith" "They deserve some love..."
    show sc i_Massage_1_10 with my_dissolve
    "Faith" "Your spine needs to be relieved."
    "Faith" "It carries such a big and beautiful body."
    "Faith" "So you have to treat it well."
    "[Name]" "{i}(She seems to be really good at this...){/i}"
    show sc i_Massage_1_11 with my_dissolve
    "Faith" "Let's work on your legs too."
    "Faith" "I know this place hurts, but you have to trust me on this."
    show sc i_Massage_1_13 with my_dissolve
    "[Name]" "Ouch..."
    "Faith" "Here we go."
    "Faith" "Now I can heal this spot..."
    show sc i_Massage_1_14 with my_dissolve
    "[Name]" "That feels... good...."
    "[Name]" "Thank you."
    "Faith" "My pleasure. That's it for today."
    show sc i_Massage_2_11 with my_dissolve
    "Faith" "I need to go, sorry,"
    "[Name]" "{i}(She's in a rush again...){/i}"
    show sc i_Massage_2_12 with my_dissolve
    "[Name]" "{i}(Well, at least this time she finished massage.){/i}"
    "[Name]" "{i}(It's time to go.){/i}"
    show sc i_Massage_2_13 with my_dissolve
    "Faith" "Wait, don't turn around..."
    "Faith" "I know you feel me... there..."
    show sc i_Massage_2_14 with my_dissolve
    "Faith" "Did you like it?"
    "[Name]" "I, uh, well...."
    "Faith" "My turn!"
    show sc i_Massage_2_15 with my_dissolve
    "Faith" "Wow...Yeah, you sure did enjoy my massage."
    "Faith" "You're definitely going to have to give up the stress here..."
    show sc i_Massage_2_16 with my_dissolve
    "Faith" "But next time..."
    "[Name]" "Wait!"
    show sc i_Massage_1_2 with my_dissolve
    "[Name]" "{i}(Damn... Where did she go?){/i}"
    "[Name]" "{i}(She's acting weird and going by two different names.){/i}"
    "[Name]" "{i}(I wonder what's really going on here...){/i}"
    "[Name]" "{i}(We'll have to come back here somehow...){/i}"

    scene image '#000' with Dissolve(.5)

    return

label Jill_1_label:


    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface 
    scene image '#000' with Dissolve(.5)
    $ Q_Jill = 1
    #show sc i_Анимация with my_dissolve
    
    scene sc i_Jill_1_anim_1 with Dissolve(.5)
    $ renpy.pause(5, hard = True)
    "[Name]" "{i}(Hmm, what an interesting design!){/i}"
    #show sc i_Последний кадр with my_dissolve
    show sc i_Jill_1_1 with my_dissolve
    
    "[Name]" "Hi!"
    show sc i_Jill_1_1 with my_dissolve
    "Jill" "Welcome to Whistley Spa and Massage."
    "Jill" "I'm Jill Whistley!"
    show sc i_Jill_1_2 with my_dissolve
    "[Name]" "Wow. So you're the owner?"
    "Jill" "It's a family business. It's like that in Dale almost everywhere."
    "[Name]" "It's an interesting feature."
    show sc i_Jill_1_3 with my_dissolve
    "Jill" "How may I address you?"
    "[Name]" "My name is [Name]."
    "Jill" "[Name]? What a beautiful name..."
    "[Name]" "{i}(Yeah, it's kind of ordinary...){/i}"
    show sc i_Jill_1_4 with my_dissolve
    "Jill" "How can I help you, [Name]?"
    "[Name]" "I'm just looking around."
    "[Name]" "I wanted to see what services are available here."
    show sc i_Jill_1_5 with my_dissolve
    "Jill" "Ta-da!"
    show sc i_Jill_1_6 with my_dissolve
    "Jill" "Our family practices many kinds of massages."
    "Jill" "Whistley Salon is known throughout the area."
    show sc i_Jill_1_4 with my_dissolve
    "Jill" "Each massage is individually tailored to the client's needs."
    "[Name]" "Wow, that sounds really great."
    show sc i_Jill_1_7 with my_dissolve
    "[Name]" "The last time I had a massage was at training camp before the Yellow Jackets game."
    "[Name]" "When I got injured..."
    show sc i_Jill_1_9 with my_dissolve
    "Jill" "Oh, so you're an athlete?"
    "[Name]" "Former."
    show sc i_Jill_1_10 with my_dissolve
    "Jill" "Then you should try our massages."
    "Jill" "Your muscles are more demanding than the average person."
    "Jill" "They need special care..."
    show sc i_Jill_1_11 with my_dissolve
    "[Name]" "{i}(I wouldn't say no to her care.){/i}"
    "[Name]" "How much does this service cost?"
    show sc i_Jill_1_12 with my_dissolve
    "Jill" "$75"
label order_a_message_jil:
    menu:
        "!Order a massage ($75)" if money <  75:
            $ pass
        "Order a massage ($75)"  if money >= 75:
            $ pass
            if money < 75:
                jump order_a_message_jil
            $ money -= 75
        "Not now":
            show sc i_Jill_1_12 with my_dissolve
            "[Name]" "Unfortunately, I can't right now."
            show sc i_Jill_1_13 with my_dissolve
            "Jill" "That's too bad. Is there nothing I can do to change your mind?"
            "[Name]" "Don't worry, I'll be sure to stop by again."
            show sc i_Jill_1_14 with my_dissolve
            "Jill" "I'll be happy to see you."
            scene image '#000' with Dissolve(.5)
            jump main_interface_label
    show sc i_Jill_1_12 with my_dissolve
    "[Name]" "You know, I think I'm going to try your famous massage."
    show sc i_Jill_1_15 with my_dissolve
    "Jill" "Yay, yay, yay! I'm sure you'll love it!"
    show sc i_Jill_1_16 with my_dissolve
    "Jill" "Go through that door over there and get ready."
    "Jill" "The massage therapist will be right with you."
    "[Name]" "Thank you, "
    call Jill_2_label_8 from _call_Jill_2_label_8
    $ p_up('Jill', 2)
    $ Q_Jill=2
    $ change_location_2('dale_mainstreet', 3)
    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface 
    scene image '#000' with Dissolve(.5)


    jump main_interface_label