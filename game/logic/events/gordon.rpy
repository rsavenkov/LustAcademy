
label gordon_dale_shop_1_label:
    # stop music_2 fadeout 1
    # play music 'audio_ep2/SC/8. Beautiful people.mp3' fadein 1.0


#    if Q_Elijah == 4:


    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.1)
    menu:
        "1 Go Fishing" if Q_Gordon == 1:
            call Gordon_2_label from _call_Gordon_2_label
            $ Q_Gordon = 2
            $ change_location_2(location_now, time_now+1)

        "4 Go Fishing" if Q_Gordon == 2:
            hide screen show_hide_locations
            hide screen show_hide_locations_2
            hide screen text_animation_up_screen_3
            hide screen main_interface
            scene image '#000' 
            with Dissolve(.5)
            
        "4 Ask for Willow" if Q_Elijah == 4:
            call Elijah_5_label from _call_Elijah_5_label
            $ p_up('Elijah', 6)
            $ Q_Elijah = 5
        "Not now" if True:

            show screen main_interface 
            show screen show_hide_locations_2
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    #jump main_interface_label



    # else:
    #     hide screen show_hide_locations
    #     hide screen show_hide_locations_2
    #     hide screen text_animation_up_screen_3
    #     hide screen main_interface 
    #     scene image '#000' with Dissolve(.5)
        
    #     "Not available in Alpha"



label Gordon_1_label:


    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface 
    scene image '#000' with Dissolve(.5)
    show sc i_Chompski_1_1 with my_dissolve
    "[Name]" '{i}(This must be a local store.){/i}'
    "[Name]" "{i}(It's seems like a nice place.){/i}"
    "[Name]" '{i}(I bet you can get a lot of useful stuff here.){/i}'
    show sc i_Chompski_1_2 with my_dissolve
    "[Name]" '{i}(But who do you get it from?){/i}'
    "[Name]" "{i}(Weird, the place isn't closed, but no one's here...){/i}"
    "[Name]" "Ahem......."
    show sc i_Chompski_1_3 with my_dissolve
    "[Name]" "Anybody here?"
    "[Name]" "HELLO! ANYBODY HERE ALIVE?!"
    "Unknown Man" "Yell in your own ears!"
    "[Name]" '{i}(Who said that?!){/i}'
    scene sc i_Chompski_1_anim_1 with Dissolve(.5)
    $ renpy.pause(1.5, hard = True)
    "[Name]" '{i}(Where is he?!){/i}'
    show sc i_Chompski_1_anim_1_z with my_dissolve
    "Unknown Man" "Can't you see everyone's busy?!"
    "Unknown Man" "As usuall with young people, no respect."
    "Unknown Man" "Can't you wait a minute?!"
    "[Name]" '{i}(What kind of creature is that? Is that a real dwarf?!){/i}'
    "Unknown Man" "Well, why aren't you talking now? Did you lose your voice?"
    show sc i_Chompski_1_4 with my_dissolve
    "Unknown Man" "What did you want?"
    "[Name]" "This is... It's a store, isn't it?"
    "Unknown Man" "A store? Huh!"
    "Unknown Man" "I'm Gordon Chompsky."
    show sc i_Chompski_1_5 with my_dissolve
    "Gordon" "And this is Chompsky's shop. Best store in Dale."
    "[Name]" "Is that so?"
    "Gordon" "Of course it's so. Dwarves never lie!"
    "Gordon" "That's why we make such great salesmen."
    show sc i_Chompski_1_6 with my_dissolve
    "Gordon" "What are you standing there for? "
    "Gordon" "Look around, pick, choose, ask, pay!"
    "[Name]" "I'm just looking around. I don't know what I want."
    "[Name]" "I'm from Cordale. Our house won the competition this week."
    "Gordon" "Whoa. What are you, an apprentice or something?"
    show sc i_Chompski_1_7 with my_dissolve
    "Gordon" "Heh-heh-heh!"
    "Gordon" "I love wizards! Your kind knows a good ingredient. Pays good money."
    "Gordon" "Not all of them, some of them are assholes..."
    "Gordon" "But you look like a good guy!"
    "[Name]" "Thanks. I guess."
    show sc i_Chompski_1_8 with my_dissolve
    "Gordon" "Willow! Willow! Baby, come here!"
    "Gordon" "We got a wizard in the house!"
    
    show sc i_Chompski_1_2 with my_dissolve
    
    "[Name]" '{i}(Whom is he talking too?){/i}'
    scene sc i_Chompski_1_anim_2 with Dissolve(.5)
    $ renpy.pause(6, hard = True)
    "Willow" "Hello."
    show sc i_Chompski_1_anim_2_z with my_dissolve
    
    "[Name]" '{i}(Whoa! Where did she come from?){/i}'
    "[Name]" '{i}(And what kind of creature is that, anyway? Is she a dwarf, too?){/i}'
    show sc i_Chompski_1_9 with my_dissolve
    "Willow" "Father, you called for me?"
    "Gordon" "Willow is my treasure, my blood."
    "Gordon" "She's half-fairy, if you know what I mean..."
    show sc i_Chompski_1_10 with my_dissolve
    "[Name]" "{i}(He's offering me to buy her, or whats going on?!){/i}"
    "[Name]" "Not really..."
    "Gordon" "Half-fairy, you jerk! Fairies are the best at magic, after all!"
    "[Name]" "{i}(I wonder if that's true...){/i}"
    "[Name]" "Really? I didn't know..."
    "Gordon" "Of course! Willow has felt magic like no one else since she was a little girl."
    show sc i_Chompski_1_11 with my_dissolve
    "Gordon" "If you ever need anything that my shop doesn't have, go to her!"
    show sc i_Chompski_1_12 with my_dissolve
    "Willow" "It's true, I could help you with anything unusual."
    "Willow" "I can sense magical objects from a great distance."
    "Willow" "And I find almost anything if I have to."
    "Willow" "That is, of course, if you can thank me enough."
    "[Name]" '{i}(Is it just me, or was it not about the money?){/i}'
    "[Name]" "Thank you."
    "[Name]" "I can't think of anything, but I'll keep that in mind."
    show sc i_Chompski_1_13 with my_dissolve
    "Willow" "It's a shame it gets so boring around here sometimes."
    "Willow" "I thought, at least I could play with you."
    show sc i_Chompski_1_14 with my_dissolve
    "Gordon" "Willow, daughter, don't harass the client!"
    "Gordon" "He said he doesn't want anything now."
    "Gordon" "Stay out of his way."
    "[Name]" "No, no, it's okay..."
    "Willow" "All right, Father."
    show sc i_Chompski_1_15 with my_dissolve
    "Willow" "See you later, man."
    "[Name]" "Bye..."
    show sc i_Chompski_1_16 with my_dissolve
    "[Name]" "You shouldn't have done that, she didn't get in my way at all."
    "Gordon" "Don't be modest."
    "Gordon" "I know how annoying she can be. She's half a fairy."
    "Gordon" "Her mother never left stoped talking. Blah-blah-blah..."
    "Gordon" "If you know what I mean. Heh-heh-heh!"
    show sc i_Chompski_1_17 with my_dissolve
    "Gordon" "All right, I've got pancakes freezing behind the counter."
    "Gordon" "Let me know if you're thinking of buying some."
    "[Name]" "I will."
    "Gordon" "Hm..."
    show sc i_Chompski_1_16 with my_dissolve
    "Gordon" "Oh, by the way, you seem like a tough guy. Can you hold a fishing rod?"
    "[Name]" "I guess so. Why?"
    show sc i_Chompski_1_18 with my_dissolve
    "Gordon" "See for yourself."
    "Gordon" "I need a pair of spare hands."
    show sc i_Chompski_1_18_1 with my_dissolve
    "Gordon" "If you need a part-time job, there's nobody better than Chompsky."
    "[Name]" "Really? Can you tell me more about that?"
    show sc i_Chompski_1_19 with my_dissolve
    "Gordon" "Heh! Sure!"
    "Gordon" "Not only do we have a shop here, but we also have a little bakery."
    "Gordon" "The locals really like the fish pies that Willow bakes."
    show sc i_Chompski_1_20 with my_dissolve
    "Gordon" "But the fish has to be very fresh and caught by hand!"
    "[Name]" "Hmmm... Don't the magic refrigerators in Dale work?"
    "Gordon" "That junk that goblins make for a few pennies?"
    "Gordon" "No, thank you. Dwarves don't eat that kind of crap."
    show sc i_Chompski_1_19 with my_dissolve
    "Gordon" "And judging by the popularity of Willow's pies, everyone can taste the difference."
    "Gordon" "So we always need few hands to toss the rod."
    "[Name]" "Catch a few fish? Sounds easy."
    "[Name]" "And will any fish do?"
    show sc i_Chompski_1_21 with my_dissolve
    "Gordon" "Of course! Our lake only has delicacies."
    "Gordon" "At least the ones that bite from the shore on a fishing pole."
    show sc i_Chompski_1_22 with my_dissolve
    "Gordon" "I'll mark on your map a great fishing spot on the lake."
    "Gordon" "Right away."
    show sc i_Chompski_1_23 with my_dissolve
    "Gordon" "And here, have a rod and bait."
    "[Name]" "Okay."
    "Gordon" "I'll pay you a dollar for each fish."
    show sc i_Chompski_1_24 with my_dissolve
    "[Name]" "Sounds fair."
    "Gordon" "Fair? I'm robbing myself for you!"
    show sc i_Chompski_1_25 with my_dissolve
    "Gordon" "All right, fine."
    "Gordon" "Just be careful when you're fishing in the evening."
    "Gordon" "Some lake dwellers hunt at dusk..."
    show sc i_Chompski_1_26 with my_dissolve
    "[Name]" "Who are you talking about?"
    "Gordon" "Just some town talk. Never mind."
    show sc i_Chompski_1_27 with my_dissolve
    "Gordon" "Just think about the catch."
    "Gordon" "I'll be waiting for you back with fresh fish."
    $ p_up('Gordon', 1)
    $ Q_Gordon=1
    jump main_interface_label  



label Gordon_2_label:
    show sc i_Chompski_1_4 with my_dissolve
    "[Name]" "Hey Gordon!"
    "[Name]" "I was thinking about your job offer. Want to go fishing. "
    show sc i_Chompski_1_7 with my_dissolve
    "Gordon" "Heh! Glad to hear it!"
    "Gordon" "What's better than fresh fish cakes?"
    "[Name]" "I don't know. Probably a lot of things."
    show sc i_Chompski_1_22 with my_dissolve
    "Gordon" "Not when Williw bake them! "
    "Gordon" "Hang on, I'll get you a rod and bait."
    show sc i_Chompski_1_7 with my_dissolve
    "[Name]" "So all I have to do is catch a couple of fish? Sounds easy."
    "Gordon" "Simple and profitable, my friend!"
    "Gordon" "I'll mark for you on the map a great fishing spot on the lake."
    show sc i_Chompski_1_25 with my_dissolve
    "Gordon" "And there you have it, rod and bait."
    "[Name]" "Okay."
    "Gordon" "I'll pay you a $ for every fish."
    show sc i_Chompski_1_26 with my_dissolve
    "[Name]" "Sounds fair."
    "Gordon" "Fair? I'm robbing myself for you!"
    "Gordon" "All right, fine."
    "Gordon" "Just be careful when you're fishing in the evening."
    show sc i_Chompski_1_27 with my_dissolve
    "Gordon" "Some lake dwellers hunt at dusk..."
    "[Name]" "Who are you talking about?"
    "Gordon" "Just some town talk. Never mind."
    show sc i_Fishing_1_1 with my_dissolve
    "Gordon" "Waiting for you back with fresh fish."
    if time_now in (1, 2):
        show sc i_Fishing_1_2 with my_dissolve
        "[Name]" "{i}(I wonder why you can't just fish from the pier in town.){/i}"
        "[Name]" "{i}(Does the fish really taste better here?){/i}"
        "[Name]" "{i}(According to the map Gordon gave me, this path leads to the lake.){/i}"
        show sc i_Fishing_1_3 with my_dissolve
        "[Name]" "{i}(Gee, it really is a lake!){/i}"
        "[Name]" "{i}(Strange that no one else is fishing.){/i}"
        show sc i_Fishing_1_4 with my_dissolve
        "[Name]" "{i}(Maybe it's that sign.){/i}"
        "[Name]" "{i}(Is this what Gordon warned me about?){/i}"
        "[Name]" "{i}(Either way, I'm safe during the day.){/i}"
        show sc i_Fishing_1_5 with my_dissolve
        "[Name]" "{i}(Don never took me fishing with him.){/i}"
        "[Name]" "{i}(But I used to watch a TV show about fishing out of boredom.){/i}"
        "[Name]" "{i}(I hope I've got the right idea of how to throw a fishing rod...){/i}"
        show sc i_Fishing_1_6 with my_dissolve
        "[Name]" "{i}(Come on, [Name]. Time to get rich!){/i}"
    else:
        show sc i_Fishing_1_12 with my_dissolve
        "[Name]" "{i}(I wonder why you can't just fish from the pier in town.){/i}"
        "[Name]" "{i}(Does the fish really taste better here?){/i}"
        "[Name]" "{i}(According to the map Gordon gave me, this path leads to the lake.){/i}"
        show sc i_Fishing_1_13 with my_dissolve
        "[Name]" "{i}(Gee, it really is a lake!){/i}"
        "[Name]" "{i}(Strange that no one else is fishing.){/i}"
        show sc i_Fishing_1_14 with my_dissolve
        "[Name]" "{i}(Maybe it's that sign.){/i}"
        "[Name]" "{i}(Is this what Gordon warned me about?){/i}"
        "[Name]" "{i}(Either way, I'm not afraid of some mermaids.){/i}"
        show sc i_Fishing_1_15 with my_dissolve
        "[Name]" "{i}(Don never took me fishing with him.){/i}"
        "[Name]" "{i}(But I used to watch a TV show about fishing out of boredom.){/i}"
        "[Name]" "{i}(I hope I've got the right idea of how to throw a fishing rod...){/i}"
        show sc i_Fishing_1_16 with my_dissolve
        "[Name]" "{i}(Come on, [Name]. Time to get rich!){/i}"
        #show sc i_Activity_Fishing_1 with my_dissolve
    scene image '#000' with Dissolve(.5)

    jump fishing_start

    return

label Gordon_fishing_label:
    if time_now in (1, 2):
        scene sc i_Fishing_1_7
    else:
        scene sc i_Fishing_1_8 
    with Dissolve(.5)
    
#     "// ?????????????? ???????? 1-5
# // ?????????????? ???????? 6-20
# // ?????????????? ???????? 21+"

#    menu:
#        '1-5':
#            scene sc i_Fishing_1_9 with Dissolve(.5)
#            "Gordon" "And you call that a catch? I can catch that much with my bare hands!"
#            "[Name]" "What can I say? No bite..."
#            "Gordon" "All right, just like we agreed, $ per fish."
#            "Gordon" "Don't go crazy with that kind of crazy money, kid."
#            $ money_now += 5
#        '6-20':
#            scene sc i_Fishing_1_10 with Dissolve(.5)
#            "Gordon" "Now that's what I'm talking about! This fish already looks delicious!"
#            "Gordon" "Good job, boy!"
#            "[Name]" "Thank you, I've tried my best."
#            "Gordon" "Here's your reward!"
#            $ money_now += 10
#        '21+':
#
#            scene sc i_Fishing_1_11 with Dissolve(.5)
#            "Gordon" "Mother of God! How many of them are there? Unbelievable!"
#            "[Name]" "He-he-heh, I've tried my best."
#            "Gordon" "I'm gonna get rich with your help, boy!"
#            "Gordon" "Here's your payment. Good job!"
#            $ money_now += 21
    

    return