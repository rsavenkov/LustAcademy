    
    
label giant_dale_mainstreet_label:
    stop music_2 fadeout 1
    play music 'audio_ep2/SC/8. Beautiful people.mp3' fadein 1.0



    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface 
    scene image '#000' with Dissolve(.5)
    menu:
        "0 Come closer" if not hasattr(store, 'Q_Giant'):
            call giant_1_label from _call_giant_1_label

        "Stay away":
            jump main_interface_label

    

    jump main_interface_label        







label giant_1_label:

    show sc i_Giant_1_1  with my_dissolve
    "[Name]" "{i}(The creature looks at me strangely.){/i}"
    "[Name]" "{i}(It's bugging me.){/i}"
    "[Name]" "{i}(I need to find out what it wants.){/i}"
    show sc i_Giant_1_2 with my_dissolve
    "[Name]" "Hey..."
    "[Name]" "Hey... Man... You okay?"
    show sc i_Giant_1_3 with my_dissolve
    "[Name]" "{i}(I don't like this. He seems to be reaching out to me...){/i}"
    "[Name]" "{i}(I'll probably regret this...){/i}"
    show sc i_Giant_1_4 with my_dissolve
    "[Name]" "{i}(What kind of creature is this... Terrifying sight...){/i}"
    "[Name]" "Hey. Is there anything I can do to help?"
    show sc i_Giant_1_5 with my_dissolve
    "Giant" "Argh..."
    "[Name]" "{i}(What the hell... Did it try to grab and eat me?){/i}"
    show sc i_Giant_1_6 with my_dissolve
    "[Name]" "I warn you, I'm a wizard!"
    "Giant" "Argh... N-no... Don't hurt me!"
    show sc i_Giant_1_7 with my_dissolve
    "Giant" "Don't hurt! .... me...."
    "Giant" "LOOK WHAT THEY DID TO ME...."
    show sc i_Giant_1_8 with my_dissolve
    "Giant" "DO YOU SEE?!"
    "[Name]" "{i}(What the hell is going on... What is he doing?){/i}"
    show sc i_Giant_1_9 with my_dissolve
    "[Name]" "{i}(He looks like a lunatic...){/i}"
    "[Name]" "{i}(He also looks around to make sure we're alone...){/i}"
    show sc i_Giant_1_8 with my_dissolve
    "[Name]" "W... what do you want?!"
    "Giant" "Argh... I'm confused."
    "Giant" "Look..."
    show sc i_Giant_1_10 with my_dissolve
    "Giant" "You're not one of them, are you?!"
    "[Name]" "Who are you talking about?"
    "[Name]" "What happened?!"
    "Giant" "Argh.... I...will."
    show sc i_Giant_1_11 with my_dissolve
    "Giant" "But promise... help!"
    menu:
        "Say you'll help":
            $ pass
            "[Name]" "{i}(I hope I don't regret it...){/i}"
            show sc i_Giant_1_12 with my_dissolve
            "[Name]" "All right, all right! I'll help."
            "Giant" "{i}Y-you... Really?{/i}"
            "Giant" "Argh... You're a good man...."
            show sc i_Giant_1_10 with my_dissolve
            "Giant" "Words are hard for me. Talking...."
            "Giant" "I need a potion... To lift curses."
            "Giant" "Sabrina..."
            show sc i_Giant_1_12 with my_dissolve
            "[Name]" "Do you know Miss Spellman?"
            "[Name]" "{i}(Something's going on here.){/i}"
            "[Name]" "I'll talk to Sabrina and try to help."
            show sc i_Giant_1_8 with my_dissolve
            "Giant" "I'll be... argh... waiting!"
            "[Name]" "{i}((That was pretty weird...){/i}"
            show sc i_Giant_1_20 with my_dissolve
            "[Name]" "{i}(I've had enough adventures for one night. Gonna sleep it off.){/i}"
            $ Q_Giant = 1
    
            $ p_up('Giant', 1)
            $ change_location_2('dale_mainstreet', time_now+1)
            jump main_interface_label
        "Don't help":
            $ pass
    show sc i_Giant_1_11 with my_dissolve
    "[Name]" "Sorry, I'm not going to help a creepy stranger."
    show sc i_Giant_1_13 with my_dissolve
    "Giant" "You're with them!"
    "Giant" "You're one of them! YOU'RE ONE OF THEM!"
    show sc i_Giant_1_14 with my_dissolve
    "Giant" "WHAT HAVE YOU DONE TO ME!"
    "[Name]" "{i}(What the hell!){/i}"
    "[Name]" "{i}(I think he's really pissed off.){/i}"
    show sc i_Giant_1_15 with my_dissolve
    "Giant" "Ah-argh!"
    "[Name]" "That's it, I warned you!"
    show sc i_Giant_1_16 with my_dissolve
    "Giant" "Eat this!"
    "Giant" "Aaargh!"
    show sc i_Giant_1_17 with my_dissolve
    "Giant" "What have you done to me!!!"
    "Giant" "Argh! YOU!"
    show sc i_Giant_1_18 with my_dissolve
    "Giant" "Leave me alone!"
    "Giant" "Leave me alone!"
    "Giant" "Argh!!!"
    show sc i_Giant_1_19 with my_dissolve
    "[Name]" "{i}(He doesn't seem to be chasing me...){/i}"
    "[Name]" "{i}(But It's better not to wander the streets like this at night, by myself.){/i}"
    "[Name]" "{i}(I was lucky he was stopped by my feeble combat shell.){/i}"
    show sc i_Giant_1_20 with my_dissolve
    "[Name]" "{i}(Damn, that was even too close...){/i}"
    "[Name]" "{i}(His paws would have easily broken my bones.){/i}"
    "[Name]" "{i}(I need to lie down...){/i}"
    $ Q_Giant = .5
    $ change_location_2('dale_mainstreet', time_now+1)
    jump main_interface_label
