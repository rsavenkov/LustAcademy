



label audrey_events_label:

    call hide_all_main_interfaces from _call_hide_all_main_interfaces_3

    $ set_now = audrey_events_set
    menu:

        "0 Talk to Audrey" if Q_Audrey==0:
            if Q_Molly < 2:

                call Audrey_1_1_label from _call_Audrey_1_1_label
            else:


                call Audrey_1_label from _call_Audrey_1_label

                call Audrey_2_label from _call_Audrey_2_label

                call Audrey_3_label from _call_Audrey_3_label
                $ p_up('Audrey', 2)
                $ Q_Audrey=3
                $ change_location_2(location_now, time_now+1)
    
        
        "3 Talk to Audrey" if Q_Audrey==3:

            call Audrey_1_2_label from _call_Audrey_1_2_label
            $ audrey_events_set.append("3 Talk to Audrey")
            $ wakeup_sets.append([

            
            audrey_events_set, "3 Talk to Audrey"
            
            
                ])
        "Not now" if True:
            show screen main_interface 
            hide screen black_tmp_screen_menu
            show screen show_hide_locations_2
            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label

label audrey_events_3_label:


    call hide_all_main_interfaces from _call_hide_all_main_interfaces_4

    $ set_now = audrey_events_set_3
    menu:

        "0 Talk to Audrey" if Q_Audrey==0:
            if Q_Molly < 2:

                call Audrey_2_1_label from _call_Audrey_2_1_label

                $ log_message.update({"QLOG_Audrey":1})
                $ audrey_events_set.append("0 Talk to Audrey")
                $ wakeup_sets.append([

            
            audrey_events_set, "0 Talk to Audrey"
            
            
                ])
            elif True:
                call Audrey_2_2_label from _call_Audrey_2_2_label

                $ log_message.update({"QLOG_Audrey":2})

        "3 Talk to Audrey" if Q_Audrey==3:
            call Audrey_4_label from _call_Audrey_4_label
            $ p_up('Audrey', 3)
            $ log_message.update({"QLOG_Audrey":5})
            $ Q_Audrey=4
            $ change_location_2(location_now, time_now+1)
        "Not now" if True:
            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label






label Audrey_1_label:
    $ load_image_now = 'Audrey_1'
    call pre_load_web_image from _call_pre_load_web_image_5
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
    show sc i_Audrey_1_3 with Dissolve(.5)
    "[Name]" "{i}(Oh, that's Samantha's hot friend!){/i}"
    show sc i_Audrey_1_1 with my_dissolve
    "[Name]" "Yo, Audrey!"
    "[Name]" "Good morning."
    "Audrey" "Morning."
    "[Name]" "What are you doing?"
    show sc i_Audrey_1_7 with my_dissolve
    "Audrey" "Doing yoga, can't you see?!"
    "Audrey" "What kind of stupid question is that?"
    show sc i_Audrey_1_13 with my_dissolve
    "Audrey" "Making coffee."
    "[Name]" "{i}(I still don't understand how you and Samantha became friends...){/i}"
    "[Name]" "{i}(She's so sweet and calm.){/i}"
    show sc i_Audrey_1_18 with my_dissolve


    "[Name]" "{i}(And you're as prickly as a cactus!){/i}"
    "[Name]" "{i}(Samantha couldn't stand people like that before...){/i}"
    "[Name]" "{i}(I doubt butt is your only asset.){/i}"
    show sc i_Audrey_1_27 with my_dissolve
    "[Name]" "{i}(Not likely to be the reason Samantha tolerates you.){/i}"
    "[Name]" "{i}(Although if it is, who's going to judge her?){/i}"
    "[Name]" "{i}(We're talking about ass like that.){/i}"
    "Audrey" "Oh, crap."
    "Audrey" "{b}We're out of cream.{/b}"
    "[Name]" "That's a shame."
    "[Name]" "Weird, I thought the fridge was magic."
    show sc i_Audrey_1_8 with my_dissolve
    "Audrey" "It is."
    "Audrey" "It only gives out what the students want."
    "Audrey" "But sometimes it gets weird with cream and persimmons and Jerusalem artichokes."
    "Audrey" "I have no idea why those particular products."
    show sc i_Audrey_1_12 with my_dissolve
    "Audrey" "El didn't tell you?"
    "[Name]" "Uh, no."
    "[Name]" "What a strange list of exceptions."
    "Audrey" "Well, you know."
    "Audrey" "The wizard who put it together had his quirks."
    show sc i_Audrey_1_19 with my_dissolve
    "Audrey" "Oh, man, this whole day is ruined."
    "[Name]" "Don't worry about it."
    "[Name]" "I'm sure your day will be fine without the artichokes."
    show sc i_Audrey_1_22 with my_dissolve
    "Audrey" "It's not funny."
    "Audrey" "{b}I just wanted a cup of coffee{/b} in the morning..."
    "Audrey" "Damn it, Elijah, I told you to take care of it!"
    show sc i_Audrey_1_21 with my_dissolve
    "[Name]" "Maybe you could stop by the coffee shop before class."
    "Audrey" "Hmm... No, I can't."
    "Audrey" "The cafe's only open in the afternoon."
    "Audrey" "Wait a minute!"
    show sc i_Audrey_1_25 with my_dissolve
    "Audrey" "Don't you work there part-time?"
    "[Name]" "From time to time."
    "[Name]" "But I don't have the keys."
    "Audrey" "So what?"
    "Audrey" "That girl who runs the place..."
    "Audrey" "What's her name?"
    "[Name]" "Molly?"
    show sc i_Audrey_1_24 with my_dissolve
    "Audrey" "That's right! Molly's been there since early this morning."
    "Audrey" "She probably won't say no to you."
    "Audrey" "{b}Would you go get some milk or cream?{/b}"
    "[Name]" "I don't know if I can do it now..."
    "Audrey" "I'll need it later too..."
    "Audrey" "The other store's in Dale anyway."
    "[Name]" "And there's nowhere else to get it but the cafe and the store."
    "Audrey" "It's so complicated."
    "Audrey" "Tell me about it."
    show sc i_Audrey_1_23 with my_dissolve
    "Audrey" "I just want to be able to make a cup of coffee with cream."
    "[Name]" "From the comfort of the campus."
    "[Name]" "I know."
    "Audrey" "So, can you help me out?"
    "[Name]" "I'll see what I can do."
    scene expression '#000' with Dissolve(.5)
    return




label Audrey_2_label:

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
    scene image '#000'

    with Dissolve(.5)
    $ load_image_now = 'Molly_1'
    call pre_load_web_image from _call_pre_load_web_image_6
    show sc i_Audrey_3_1 with Dissolve(.5)

    "[Name]" "Good morning!"
    "Molly" "Excuse me, we're closed!"
    "[Name]" "Molly, it's me."
    show sc i_Molly_1_4 with my_dissolve
    "Molly" "Good morning, [Name]."
    "Molly" "I'm sorry, but we're closed."
    show sc i_Molly_1_3 with my_dissolve
    "[Name]" "I know."
    show sc i_Molly_1_3 with my_dissolve
    "[Name]" "I'm not here to sit in the cafe."
    show sc i_Molly_1_4 with my_dissolve
    "Molly" "Well, as you can see, there's no work for you right now either."
    show sc i_Molly_1_3 with my_dissolve
    "[Name]" "I figured as much."
    show sc i_Molly_1_4 with my_dissolve
    "Molly" "Drop by during the day or at night."
    show sc i_Molly_1_4 with my_dissolve
    "Molly" "I'm sure we could use an extra pair of hands."
    show sc i_Molly_1_6 with my_dissolve
    "[Name]" "Sure."
    "[Name]" "But I'm not here to work."
    show sc i_Molly_1_7 with my_dissolve
    "Molly" "Well, what is it then?"
    show sc i_Molly_1_6 with my_dissolve
    "[Name]" "We have a magic refrigerator in the living room with a quirk."
    "[Name]" "You can't get milk or cream."
    show sc i_Molly_1_2 with my_dissolve
    "Molly" "That's funny, that's the first I've heard of it."
    "[Name]" "Is yours working properly?"
    "Molly" "Thank the dendroids!"
    "Molly" "Imagine what a disaster it would be if we ran out of milk..."
    "Molly" "The students here practically live on lattes."
    show sc i_Molly_1_1 with my_dissolve
    "[Name]" "That's why I'm here, by the way."
    "[Name]" "Can I borrow a bottle from you?"
    "[Name]" "We've got a pretty girl dying of sadness in there."
    "Molly" "Sure."
    show sc i_Audrey_3_2 with my_dissolve
    "Molly" "There you go."
    "[Name]" "Oh, thank you."
    show sc i_Audrey_3_4 with my_dissolve
    "Molly" "Five dollars!"
    "[Name]" "Wait a minute..."
    "[Name]" "You're selling it to me?"
    show sc i_Audrey_3_5 with my_dissolve
    "Molly" "Yeah, I am."
    "[Name]" "I thought..."
    "Molly" "Have you ever heard of market relations?"
    "[Name]" "{i}(How can there be a market relationship with a magic refrigerator?){/i}"

    "[Name]" "Take it out of my paycheck."

    "Molly" "Hmm... Okay, I'll make an exception for an employee."
    show sc i_Molly_1_2 with my_dissolve
    "Molly" "By the way, congratulations!"
    "[Name]" "On what?"
    "Molly" "You're the first customer today."
    "[Name]" "Hooray..."
    show sc i_Audrey_3_6 with my_dissolve
    "Molly" "Now if you'll excuse me..."
    "Molly" "I have to finish getting ready for the opening."
    "[Name]" "Of course you do."
    show sc i_Audrey_3_7 with my_dissolve
    "[Name]" "I'll see you then."
    scene expression '#000' with Dissolve(.5)
    return


label Audrey_3_label:
    $ load_image_now = 'Audrey_1'
    call pre_load_web_image from _call_pre_load_web_image_7
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
    show sc i_Audrey_1_19 with Dissolve(.5)
    "[Name]" "Hello, hello, hello!"
    "[Name]" "Are you making coffee?"
    show sc i_Audrey_1_20 with my_dissolve
    "Audrey" "Yo."
    "Audrey" "Something like that."
    "[Name]" "I see."
    show sc i_Audrey_3_8 with my_dissolve
    "[Name]" "I thought you were missing something..."
    "Audrey" "Did you really go get the milk?"
    "Audrey" "For real?"
    "Audrey" "Holy shit."
    show sc i_Audrey_1_4 with my_dissolve
    "Audrey" "I underestimated you."
    "[Name]" "What do you mean?"
    "Audrey" "Samantha speaks too highly of you."
    "Audrey" "It pisses me off."
    show sc i_Audrey_1_16 with my_dissolve
    "Audrey" "I thought she was exaggerating."
    "Audrey" "But you're definitely not the worst person I've ever met."
    "[Name]" "Thank you.{w} I guess..."
    show sc i_Audrey_1_7 with my_dissolve
    "Audrey" "It's a compliment."
    "Audrey" "Haven't you ever been taught how to take a compliment?"
    "Audrey" "Shut up and be grateful."
    "[Name]" "Ah-ah-ha!"
    "[Name]" "I'll remember that."
    show sc i_Audrey_1_17 with my_dissolve
    "[Name]" "{i}(Maybe she's not so weird...){/i}"
    "[Name]" "{i}(Samantha, how do you manage to see the good in everyone?){/i}"
    "[Name]" "{i}(No matter how deep down it's buried...){/i}"
    "[Name]" "You're so sweet."
    show sc i_Audrey_1_7 with my_dissolve
    "Audrey" "What?"
    "Audrey" "What kind of nonsense is this?"
    "[Name]" "That's not how I was taught to take compliments."
    "Audrey" "..."
    show sc i_Audrey_1_15 with my_dissolve
    "Audrey" "Thank you."
    "[Name]" "I'm sorry to be blunt, but..."
    "[Name]" "You and Samantha are so different."
    show sc i_Audrey_1_5 with my_dissolve
    "Audrey" "What's your point?"
    "[Name]" "And yet you spend most of your time together."
    "Audrey" "So?"
    "[Name]" "What's the secret?"
    show sc i_Audrey_1_7 with my_dissolve
    "Audrey" "What secret?"
    "Audrey" "That's ridiculous. We're just friends."
    "Audrey" "I mean, it just happened."
    "Audrey" "Ok, now leave me alone, I've got things to do."
    "[Name]" "But I..."
    show sc i_Audrey_1_13 with my_dissolve
    "Audrey" "Sorry, I'll do it another time."
    "Audrey" "Adios!"
    "[Name]" "Okay, bye."
    "[Name]" "{i}(She made such a fuss when I brought up their friendship.){/i}"
    "[Name]" "{i}(And she was very confused by the word \"Secret\".){/i}"
    "[Name]" "{i}(There's obviously something wrong here.){/i}"
    "[Name]" "{i}(I'll figure it out...){/i}"


    $ log_message.update({"QLOG_Audrey":3})
    return


label Audrey_4_label:

    
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
    $ load_image_now = 'Audrey_4'
    call pre_load_web_image from _call_pre_load_web_image_8
    $ load_image_now = 'Samantha_2'
    call pre_load_web_image from _call_pre_load_web_image_9

    $ load_image_now = 'Audrey_2'
    call pre_load_web_image from _call_pre_load_web_image_10
    show sc i_Samantha_2_5 with Dissolve(.5)
    "[Name]" "Hey, girls!"
    "Samantha" "Hey, [Name]!"
    "Audrey" "Yo."
    "[Name]" "Watcha doing?{w} Am I interrupting something?"
    show sc i_Samantha_2_12 with my_dissolve
    "Audrey" "You are."
    "Samantha" "Audrey!"
    "Audrey" "What? He asked!"
    "Samantha" "She's..."
    "[Name]" "She's kidding?{w} I know."
    "[Name]" "She and I are friends now."
    show sc i_Samantha_2_8 with my_dissolve
    "Samantha" "You two got to know each other more?"
    "Samantha" "I'm so happy!"
    "Audrey" "Well, not really..."
    show sc i_Audrey_4_1 with my_dissolve
    "Samantha" "It's like a load off my mind."
    "Samantha" "I was so afraid you two wouldn't get along."
    "[Name]" "Nonsense!"
    show sc i_Audrey_4_2 with my_dissolve
    "[Name]" "Did I ever not get along with anyone?"
    "Samantha" "Where do you want me to start with the list?"
    "[Name]" "You know me too well."
    "[Name]" "While I barely know you."
    show sc i_Audrey_4_3 with my_dissolve
    "Samantha" "What's the big deal?"
    "Samantha" "You know I'm an open book:"
    "Samantha" "Ask me anything and you'll find out."
    show sc i_Samantha_2_17 with my_dissolve
    "[Name]" "Oh, really?"
    "[Name]" "How did you and Audrey start being friends in the first place?"
    show sc i_Samantha_2_19 with my_dissolve
    "Audrey" "Hey!"
    "Audrey" "Don't talk about me like I'm not here."
    "Audrey" "And what kind of innuendo is that..."
    show sc i_Samantha_2_20 with my_dissolve
    "Audrey" "Do you think I can't be friends with Samantha?"
    "Samantha" "Don't get all pissed off, Audrey. I'm sure that's not what [Name] meant."
    "Samantha" "What do you mean how?"
    show sc i_Samantha_2_18 with my_dissolve
    "[Name]" "Don't get me wrong. It's just that you're so different..."
    "[Name]" "It's hard to imagine you two getting along right away."
    "[Name]" "Something must have happened..."
    show sc i_Samantha_2_17 with my_dissolve
    "Samantha" "Nonsense!"
    "Samantha" "You read too many mystery books."
    "[Name]" "And yet."
    "[Name]" "What exactly happened before you become friends?"
    "Samantha" "Well... Um..."
    "Samantha" "I seem to recall at the time..."
    "Samantha" "I'm sorry, I have to answer."
    show sc i_Audrey_2_1 with my_dissolve
    "Samantha" "Hello! Yes? Mister principal?"
    "[Name]" "What's up?"
    "Samantha" "Um...{w} I have no idea."
    "Samantha" "Principal called."
    "Samantha" "That's weird."
    "[Name]" "{i}(Weird indeed...){/i}"
    "[Name]" "{i}(And what a convinient moment it is for you.){/i}"
    show sc i_Audrey_2_2 with my_dissolve
    "Samantha" "It must be urgent."
    "Samantha" "Well, I gotta run. We'll continue this another time!"
    "Audrey" "Bye, babe."
    "Audrey" "I got a lot to do, too, so..."
    show sc i_Audrey_2_11 with my_dissolve
    "[Name]" "Wait a minute."
    "[Name]" "Why was Samantha so nervous?"
    show sc i_Audrey_2_3 with my_dissolve
    "Audrey" "Ask her."
    "[Name]" "You don't know?"
    show sc i_Audrey_2_5 with my_dissolve
    "Audrey" "I have no idea."
    "[Name]" "You don't?"
    show sc i_Audrey_2_12 with my_dissolve
    "Audrey" "Absolutely."
    "[Name]" "{i}(Who do you both think I am?){/i}"
    "[Name]" "{i}(Okay, no point in pressuring her now, she won't admit it...){/i}"
    "[Name]" "{i}(Maybe it's better to try to eavesdrop on what they're talking about in private.){/i}"
    show sc i_Audrey_4_4 with my_dissolve
    "[Name]" "Okay."
    "[Name]" "Sorry, I'm just really nosy."
    "Audrey" "I'd pick another word..."
    show sc i_Audrey_4_5 with my_dissolve
    "[Name]" "{i}If it's not ???sexy???, I don't even know...{/i}"
    "Audrey" "Hee hee!"
    "Audrey" "You're funny."
    "Audrey" "But I really have my hands full."
    "Audrey" "So..."
    "[Name]" "Of course, I understand."
    show sc i_Audrey_2_30 with my_dissolve
    "[Name]" "I'll see you later!"
    return



label Audrey_1_1_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)
    $ load_image_now = 'Audrey_1'
    call pre_load_web_image from _call_pre_load_web_image_11
    
    show sc i_Audrey_1_1 with Dissolve(.5)

    "[Name]" "Hi!"
    "Audrey" "Yo."
    "[Name]" "Audrey, you look unbelievably gorgeous today..."
    show sc i_Audrey_1_7 with my_dissolve
    "Audrey" "Don't even start."
    "Audrey" "I don't like non-self-reliant teenagers."
    "[Name]" "You think you know me, Audrey?"
    show sc i_Audrey_1_10 with my_dissolve
    "Audrey" "I have an instinct for this kind of guys."
    "[Name]" "I'll prove you wrong."
    "[Name]" "{i}(How do I prove her wrong?){/i}"
    "Audrey" "Heh, I don't think so."
    show sc i_Audrey_1_5 with my_dissolve
    "Audrey" "Apparently you're fine with being unemployed at that age."
    "Audrey" "But to me, a man without a job is pathetic."
    "Audrey" "And if you're too young to work."
    "Audrey" "You're no match for a real woman, are you?"
    show sc i_Audrey_1_4 with my_dissolve
    "Audrey" "Got it?"
    "[Name]" "Yes."

    $ log_message.update({"QLOG_Audrey":1})
    $ audrey_events_set.append("0 Talk to Audrey")
    $ wakeup_sets.append([


audrey_events_set, "0 Talk to Audrey"


    ])
    return




label Audrey_1_2_label:
    hide screen main_interface 

    show expression '#000'
    with Dissolve(.5)
    $ load_image_now = 'Audrey_1'
    call pre_load_web_image from _call_pre_load_web_image_12
    
    show sc i_Audrey_1_1 with Dissolve(.5)
    "[Name]" "Audrey, hi!"
    "Audrey" "Yo."
    "[Name]" "I'm thinking about getting some coffee, too."
    "[Name]" "Can I keep you company?"
    show sc i_Audrey_1_3 with my_dissolve
    "Audrey" "No, I'm sorry. I'm in a hurry."
    "Audrey" "I promised Frollo I wouldn't be late for practice."
    "[Name]" "Oh... That's too bad..."
    "[Name]" "When are you going to be free?"
    show sc i_Audrey_1_13 with my_dissolve
    "Audrey" "It's none of your business, but tonight."
    "[Name]" "All right."


    return


label Audrey_2_1_label:
    hide screen main_interface 
    show expression '#000'
    with Dissolve(.5)
    $ load_image_now = 'Samantha_2'
    call pre_load_web_image from _call_pre_load_web_image_13
    
    show sc i_Samantha_2_5 with Dissolve(.5)
    "[Name]" "Hey, guys, how's it going?"
    "Samantha " "I'm great."
    "Audrey" "Yo."
    "[Name]" "Audrey, I was just coming to talk to you..."
    show sc i_Samantha_2_8 with my_dissolve
    "Audrey" "Not interested."
    "[Name]" "What do you mean?"
    "Audrey" "Leave me alone."
    "Audrey" "Can't you see we're talking?"
    show sc i_Samantha_2_11 with my_dissolve
    "Samantha " "Audrey..."
    "[Name]" "It's okay, Sam. I got it."
    "[Name]" "{i}(She wants to look cool in front of Sam.){/i}"
    "[Name]" "{i}(I'm not getting anywhere here. I'd better go see her in the morning.){/i}"
    show sc i_Samantha_2_12 with my_dissolve
    "[Name]" "I'll leave you to it."


    return




label Audrey_2_2_label:
    hide screen main_interface

    show expression '#000'
    with Dissolve(.5)
    $ load_image_now = 'Samantha_2'
    call pre_load_web_image from _call_pre_load_web_image_14
    show sc i_Samantha_2_5 with Dissolve(.5)
    "[Name]" "Audrey, can we talk?"
    "Audrey" "We? Talk?"
    show sc i_Samantha_2_8 with my_dissolve
    "Audrey" "Sorry, I'll pass."
    "[Name]" "Why not?"
    "Audrey" "There's nothing to talk about."
    "[Name]" "{i}(Just like that?!){/i}"
    "[Name]" "{i}(You don't have a heart...){/i}"
    show sc i_Samantha_2_13 with my_dissolve
    "[Name]" "Is she always like this?"
    "Samantha " "Leave me out of it."
    "[Name]" "I'm sorry."

    return













init python:
    def check_LGBT():
        global LGBTQ
        if hasattr(store, 'LGBTQ') and LGBTQ:
            return True

label audrey_events_4_label:
    






    if not hasattr(store, 'Q_NV_Audrey'):
        $ Q_NV_Audrey = 0
        $ audrey_shemale = 0
    if persistent.nv is None:
        call hide_all_main_interfaces from _call_hide_all_main_interfaces_11
        $ nv = renpy.call_screen('confirm', 
        '{size=15}Note that night visits are entirely optional.{/size} \n{size=15}This additional content is not required to complete the game{/size} \n{size=15}and won???t influence your relationship with other characters.{/size}', 
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

                        $ renpy.call('Audrey_events_4_label_0')
                    "Scene 2" if True:

                        $ renpy.call('Audrey_events_4_label_2')
                    "Scene 3" if True:

                        $ renpy.call('Audrey_events_4_label_3')
                    "Scene 4" if True:

                        $ renpy.call('Audrey_events_4_label_4')

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

            if Q_NV_Audrey:
                hide screen main_interface with Dissolve(.5)
                $ renpy.call('Audrey_events_4_label_'+str(Q_NV_Audrey))

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
            show screen main_interface 
            show screen show_hide_locations_2
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            if persistent.from_gallery:
                hide screen main_interface
                scene expression '#000'
                with Dissolve(1)
                $ renpy.full_restart()

            jump main_interface_label

label Audrey_events_4_label_0:

    hide screen main_interface 
    show expression '#000a'
    with Dissolve(.5)
    if not hasattr(store, 'LGBTQ'):

        $ nv = renpy.call_screen('confirm', 
        'Do you want to enable LGBTQ+ and hardcore fetishes?', 
        Return('Yes'), Return('No'), yes_text = _('Yes'), no_text = _('No'),)



        if nv == 'Yes':

            $ LGBTQ = True
        else:
            $ LGBTQ = False









    $ Q_NV_Audrey += 2
    if LGBTQ:

        $ nv = renpy.call_screen('confirm', 
        'Do you want Audrey to be a female or a shemale?', 
        Return('Girl'), Return('Shemale'), yes_text = _("Girl"), no_text = _("Shemale"),)

        if nv == "Girl":

            $ audrey_shemale = 0
        else:
            $ audrey_shemale = 1
            jump audrey_events_4_label_shemale



    hide screen main_interface 


    scene sc i_Audrey_NV_1
    with Dissolve(.5)
    "[Name]" "{i}(Wow. When she's alseep she does not look that angry.){/i}"
    "[Name]" "{i}(Hell! She's even cute..){/i}"
    show sc i_Audrey_NV_2 with my_dissolve
    "[Name]" "{i}(Maybe I should take a clother look?){/i}"
    "[Name]" "{i}(I have to be careful, though. She'll kill me if she wakes up.){/i}"
    "[Name]" "{i}(So what are you hiding here, Audrey...){/i}"
    show sc i_Audrey_NV_3 with my_dissolve
    "[Name]" "{i}(Let's see...){/i}"
    "[Name]" "{i}(Oh my!){/i}"
    "[Name]" "{i}(So you are a free spirit type?){/i}"
    "[Name]" "{i}(I must say I totaly agree with your decission.){/i}"
    "[Name]" "{i}(Who needs a bra anyway?){/i}"
    show sc i_Audrey_NV_4 with my_dissolve
    "[Name]" "{i}(And what do we have her...){/i}"
    "[Name]" "{i}(Panties? Well...){/i}"
    "[Name]" "{i}(It'd be too good to be true, if you were a nudist.){/i}"
    "[Name]" "{i}(Now, let's try to...){/i}"
    show sc i_Audrey_NV_16 with my_dissolve
    "Audrey" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I don't want her to wake up and see me.){/i}"
    "[Name]" "{i}(I should go to bed.){/i}"






    if persistent.from_gallery:
        hide screen main_interface
        scene expression '#000'
        with Dissolve(1)
        $ renpy.full_restart()
    scene expression '#000' with Dissolve(1.5)
    $ renpy.pause(1.5, hard = True)
    if renpy.music.get_playing():
        stop music fadeout .5
        play music_2 'audio_ep2/SC/33. Romantic.mp3' fadein 1


    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout .5
        play music 'audio_ep2/SC/33. Romantic.mp3' fadein 1

    $ change_location_2('leon_room_mc', time_now+1, sleep = True)
    jump main_interface_label



label audrey_events_4_label_shemale:




    show sc i_Audrey_NV_1 with my_dissolve
    "[Name]" "{i}(Wow. When she's alseep she does not look that angry.){/i}"
    "[Name]" "{i}(Hell! She's even cute..){/i}"
    show sc i_Audrey_NV_2 with my_dissolve
    "[Name]" "{i}(Maybe I should take a clother look?){/i}"
    "[Name]" "{i}(I have to be careful, though. She'll kill me if she wakes up.){/i}"
    "[Name]" "{i}(So what are you hiding here, Audrey...){/i}"
    show sc i_Audrey_NV_3 with my_dissolve
    "[Name]" "{i}(Let's see...){/i}"
    "[Name]" "{i}(Oh my!){/i}"
    "[Name]" "{i}(So you are a free spirit type?){/i}"
    "[Name]" "{i}(I must say I totaly agree with your decission.){/i}"
    "[Name]" "{i}(Who needs a bra anyway?){/i}"
    show sc i_Audrey_NV_4 with my_dissolve
    "[Name]" "{i}(And what do we have her...){/i}"
    "[Name]" "{i}(Panties? Well...){/i}"
    "[Name]" "{i}(It'd be too good to be true, if you were a nudist.){/i}"
    "[Name]" "{i}(Now, let's try to...){/i}"
    show sc i_Audrey_NV_16 with my_dissolve
    "Audrey" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I don't want her to wake up and see me.){/i}"
    "[Name]" "{i}(I should go to bed.){/i}"





    if persistent.from_gallery:
        hide screen main_interface
        scene expression '#000'
        with Dissolve(1)
        $ renpy.full_restart()

    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/33. Romantic.mp3' fadein 2


    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/33. Romantic.mp3' fadein 2
    scene expression '#000' with Dissolve(.5)
    $ change_location_2('leon_room_mc', time_now+1, sleep = True)
    jump main_interface_label

label Audrey_events_4_label_1:
    $ Q_NV_Audrey += 1
    if audrey_shemale:

        jump Audrey_events_4_label_1_shemale

    scene sc i_Audrey_NV_1 with Dissolve(.5)


    "[Name]" "{i}(Wow. When she's alseep she does not look that angry.){/i}"
    "[Name]" "{i}(Hell! She's even cute..){/i}"
    show sc i_Audrey_NV_2 with my_dissolve
    "[Name]" "{i}(Maybe I should take a clother look?){/i}"
    "[Name]" "{i}(I have to be careful, though. She'll kill me if she wakes up.){/i}"
    "[Name]" "{i}(So what are you hiding here, Audrey...){/i}"
    show sc i_Audrey_NV_3 with my_dissolve
    "[Name]" "{i}(Let's see...){/i}"
    "[Name]" "{i}(Oh my!){/i}"
    "[Name]" "{i}(So you are a free spirit type?){/i}"
    "[Name]" "{i}(I must say I totaly agree with your decission.){/i}"
    "[Name]" "{i}(Who needs a bra anyway?){/i}"
    show sc i_Audrey_NV_4 with my_dissolve
    "[Name]" "{i}(And what do we have her...){/i}"
    "[Name]" "{i}(Panties? Well...){/i}"
    "[Name]" "{i}(It'd be too good to be true, if you were a nudist.){/i}"
    "[Name]" "{i}(Now, let's try to...){/i}"
    show sc i_Audrey_NV_16 with my_dissolve
    "Audrey" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I don't want her to wake up and see me.){/i}"
    "[Name]" "{i}(I should go to bed.){/i}"
    scene expression '#000' with Dissolve(.5)
    return

label Audrey_events_4_label_1_shemale:


    scene sc i_Audrey_NV_1 with Dissolve(.5)
    "[Name]" "{i}(Wow. When she's alseep she does not look that angry.){/i}"
    "[Name]" "{i}(Hell! She's even cute..){/i}"
    show sc i_Audrey_NV_2 with my_dissolve
    "[Name]" "{i}(Maybe I should take a clother look?){/i}"
    "[Name]" "{i}(I have to be careful, though. She'll kill me if she wakes up.){/i}"
    "[Name]" "{i}(So what are you hiding here, Audrey...){/i}"
    show sc i_Audrey_NV_3 with my_dissolve
    "[Name]" "{i}(Let's see...){/i}"
    "[Name]" "{i}(Oh my!){/i}"
    "[Name]" "{i}(So you are a free spirit type?){/i}"
    "[Name]" "{i}(I must say I totaly agree with your decission.){/i}"
    "[Name]" "{i}(Who needs a bra anyway?){/i}"
    show sc i_Audrey_NV_4 with my_dissolve
    "[Name]" "{i}(And what do we have her...){/i}"
    "[Name]" "{i}(Panties? Well...){/i}"
    "[Name]" "{i}(It'd be too good to be true, if you were a nudist.){/i}"
    "[Name]" "{i}(Now, let's try to...){/i}"
    show sc i_Audrey_NV_16 with my_dissolve
    "Audrey" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I don't want her to wake up and see me.){/i}"
    "[Name]" "{i}(I should go to bed.){/i}"
    scene expression '#000' with Dissolve(.5)
    return



label Audrey_events_4_label_2:
    $ Q_NV_Audrey += 1
    if audrey_shemale:

        jump Audrey_events_4_label_2_shemale

    scene sc i_Audrey_NV_1 with Dissolve(.5)



    "[Name]" "{i}(Still can't believe how cute Audrey looks while she asleep.){/i}"
    "[Name]" "{i}(You are an interesting lady, Audrey.){/i}"
    show sc i_Audrey_NV_2 with my_dissolve
    "[Name]" "{i}(Let's not waste time on talking.){/i}"
    "[Name]" "{i}(I have a feeling that you don't need that blanket.){/i}"
    show sc i_Audrey_NV_4 with my_dissolve
    "[Name]" "{i}(Let's take that off...){/i}"
    "[Name]" "{i}(Oh wow...){/i}"
    show sc i_Audrey_NV_5 with my_dissolve
    "[Name]" "{i}(Your breasts are surely happy to see me.){/i}"
    "[Name]" "{i}(Don't worry, I'll be gentle with them.){/i}"
    "[Name]" "{i}(Let me try...){/i}"
    show sc i_Audrey_NV_6 with my_dissolve
    "[Name]" "{i}(To feel them.){/i}"
    "[Name]" "{i}(Ah, that's what I was hoping for...){/i}"
    "[Name]" "{i}(Audrey, your breasts are amazing.){/i}"
    "[Name]" "{i}(I bet you're not just beautiful on top...){/i}"
    "[Name]" "{i}(It's not fair that your tits got all the attention. ){/i}"
    show sc i_Audrey_NV_10 with my_dissolve
    "[Name]" "{i}(What about your other significant part?){/i}"
    "[Name]" "{i}(Why are you legs so close to each other? Are you shy?){/i}"
    show sc i_Audrey_NV_11 with my_dissolve
    "[Name]" "{i}(Don't be! Here, let me just move your leg...){/i}"
    show sc i_Audrey_NV_16 with my_dissolve
    "Audrey" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I don't want her to wake up and see me.){/i}"
    "[Name]" "{i}(I should go to bed.){/i}"

    scene expression '#000' with Dissolve(.5)
    return


label Audrey_events_4_label_2_shemale:

    scene sc i_Audrey_NV_1 with Dissolve(.5)




    "[Name]" "{i}(Still can't believe how cute Audrey looks while she asleep.){/i}"
    "[Name]" "{i}(You are an interesting lady, Audrey.){/i}"
    show sc i_Audrey_NV_2 with my_dissolve
    "[Name]" "{i}(Let's not waste time on talking.){/i}"
    "[Name]" "{i}(I have a feeling that you don't need that blanket.){/i}"
    show sc i_Audrey_NV_4 with my_dissolve
    "[Name]" "{i}(Let's take that off...){/i}"
    "[Name]" "{i}(Oh wow...){/i}"
    show sc i_Audrey_NV_5 with my_dissolve
    "[Name]" "{i}(Your breasts are surely happy to see me.){/i}"
    "[Name]" "{i}(Don't worry, I'll be gentle with them.){/i}"
    "[Name]" "{i}(Let me try...){/i}"
    show sc i_Audrey_NV_6 with my_dissolve
    "[Name]" "{i}(To feel them.){/i}"
    "[Name]" "{i}(Ah, that's what I was hoping for...){/i}"
    "[Name]" "{i}(Audrey, your breasts are amazing.){/i}"
    "[Name]" "{i}(I bet you're not just beautiful on top...){/i}"
    "[Name]" "{i}(It's not fair that your tits got all the attention. ){/i}"
    show sc i_Audrey_NV_18 with my_dissolve
    "[Name]" "{i}(What about your other significant part?){/i}"
    "[Name]" "{i}(Oh my gosh,,, Was I too quick to call you lady?){/i}"
    show sc i_Audrey_NV_19 with my_dissolve
    "[Name]" "{i}(It's too intersting, I have to take a closer look...){/i}"
    show sc i_Audrey_NV_16 with my_dissolve
    "Audrey" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I don't want her to wake up and see me.){/i}"
    "[Name]" "{i}(I should go to bed.){/i}"

    scene expression '#000' with Dissolve(.5)
    return

label Audrey_events_4_label_3:
    $ Q_NV_Audrey += 1
    if audrey_shemale:

        jump Audrey_events_4_label_3_shemale
    scene sc i_Audrey_NV_1 with Dissolve(.5)



    "[Name]" "{i}(Still can't believe how cute Audrey looks while she asleep.){/i}"
    "[Name]" "{i}(You are an interesting lady, Audrey.){/i}"
    show sc i_Audrey_NV_2 with my_dissolve
    "[Name]" "{i}(Let's not waste time on talking.){/i}"
    "[Name]" "{i}(I have a feeling that you don't need that blanket.){/i}"
    show sc i_Audrey_NV_4 with my_dissolve
    "[Name]" "{i}(Let's take that off...){/i}"
    "[Name]" "{i}(Oh wow...){/i}"
    show sc i_Audrey_NV_5 with my_dissolve
    "[Name]" "{i}(Your breasts are surely happy to see me.){/i}"
    "[Name]" "{i}(Don't worry, I'll be gentle with them.){/i}"
    "[Name]" "{i}(Let me try...){/i}"
    show sc i_Audrey_NV_6 with my_dissolve
    "[Name]" "{i}(To feel them.){/i}"
    "[Name]" "{i}(Ah, that's what I was hoping for...){/i}"
    "[Name]" "{i}(Audrey, your breasts are amazing.){/i}"
    show sc i_Audrey_NV_7 with my_dissolve
    "[Name]" "{i}(But I can't be sure untill I try both...){/i}"
    "[Name]" "{i}(Oh yes.){/i}"
    show sc i_Audrey_NV_8 with my_dissolve
    "[Name]" "{i}(That's what I'm talking about.){/i}"
    "[Name]" "{i}(Your nipples are getting hard.){/i}"
    "[Name]" "{i}(Are you dreaming about me squeezing them?){/i}"
    "[Name]" "{i}(I know you do.){/i}"
    "[Name]" "{i}(But I think I have a better idea.){/i}"
    show sc i_Audrey_NV_10 with my_dissolve
    "[Name]" "{i}(Let's try to take a look at your blossom now.){/i}"
    show sc i_Audrey_NV_11 with my_dissolve
    "[Name]" "{i}(Just move your leg a little bit...){/i}"
    show sc i_Audrey_NV_12 with my_dissolve
    "[Name]" "{i}(Don't be so shy.){/i}"
    "[Name]" "{i}(Here we go.){/i}"
    show sc i_Audrey_NV_13 with my_dissolve
    "[Name]" "{i}(Now I can see what's you've been hiding here...){/i}"
    "[Name]" "{i}(I think your panties are very sexy.){/i}"
    "[Name]" "{i}(And your skin... Amazingly soft and tender...){/i}"
    show sc i_Audrey_NV_14 with my_dissolve
    "[Name]" "{i}(Should I move my hand a little bit higher?!){/i}"
    show sc i_Audrey_NV_16 with my_dissolve
    "Audrey" "Mhm... mmm..."
    "[Name]" "{i}(Shit, I think she could wake up any minute.){/i}"
    "[Name]" "{i}(Better get out of here and get some sleep.){/i}"
    scene expression '#000' with Dissolve(.5)
    return


label Audrey_events_4_label_3_shemale:

    scene sc i_Audrey_NV_1 with Dissolve(.5)


    "[Name]" "{i}(Still can't believe how cute Audrey looks while she asleep.){/i}"
    "[Name]" "{i}(You are an interesting lady, Audrey.){/i}"
    show sc i_Audrey_NV_2 with my_dissolve
    "[Name]" "{i}(Let's not waste time on talking.){/i}"
    "[Name]" "{i}(I have a feeling that you don't need that blanket.){/i}"
    show sc i_Audrey_NV_4 with my_dissolve
    "[Name]" "{i}(Let's take that off...){/i}"
    "[Name]" "{i}(Oh wow...){/i}"
    show sc i_Audrey_NV_5 with my_dissolve
    "[Name]" "{i}(Your breasts are surely happy to see me.){/i}"
    "[Name]" "{i}(Don't worry, I'll be gentle with them.){/i}"
    "[Name]" "{i}(Let me try...){/i}"
    show sc i_Audrey_NV_6 with my_dissolve
    "[Name]" "{i}(To feel them.){/i}"
    "[Name]" "{i}(Ah, that's what I was hoping for...){/i}"
    "[Name]" "{i}(Audrey, your breasts are amazing.){/i}"
    show sc i_Audrey_NV_7 with my_dissolve
    "[Name]" "{i}(But I can't be sure untill I try both...){/i}"
    "[Name]" "{i}(Oh yes.){/i}"
    show sc i_Audrey_NV_8 with my_dissolve
    "[Name]" "{i}(That's what I'm talking about.){/i}"
    "[Name]" "{i}(Your nipples are getting hard.{/i}"
    "[Name]" "{i}(Are you dreaming about me squeezing them?){/i}"
    "[Name]" "{i}(I know you do.){/i}"
    "[Name]" "{i}(But I think I have a better idea.){/i}"
    show sc i_Audrey_NV_18 with my_dissolve
    "[Name]" "{i}(Let's try to take a look at your manly parts now.){/i}"
    show sc i_Audrey_NV_19 with my_dissolve
    "[Name]" "{i}(I still can't beileve this is real.){/i}"
    show sc i_Audrey_NV_20 with my_dissolve
    "[Name]" "{i}(Don't be so shy.){/i}"
    "[Name]" "{i}(Here we go.){/i}"
    show sc i_Audrey_NV_21 with my_dissolve
    "[Name]" "{i}(Now I can see what's you've been hiding here...){/i}"
    "[Name]" "{i}(I can't say that I'm not interested.){/i}"
    "[Name]" "{i}(And your skin... Amazingly soft and tender...){/i}"
    show sc i_Audrey_NV_22 with my_dissolve
    "[Name]" "{i}(What are you exactly?!){/i}"
    show sc i_Audrey_NV_16 with my_dissolve
    "Audrey" "Mhm... mmm..."
    "[Name]" "{i}(Shit, I think I have no time to explore, she's waking up.){/i}"
    "[Name]" "{i}(Better get out of here and get some sleep.){/i}"
    scene expression '#000' with Dissolve(.5)
    return



label Audrey_events_4_label_4:

    $ unlock_gallery('images/ero/NV_Audrey.png')

    if audrey_shemale:

        jump Audrey_events_4_label_4_shemale
    scene sc i_Audrey_NV_1 with Dissolve(.5)
    "[Name]" "{i}(Still can't believe how cute Audrey looks while she asleep.){/i}"
    "[Name]" "{i}(You are an interesting lady, Audrey.){/i}"
    show sc i_Audrey_NV_2 with my_dissolve
    "[Name]" "{i}(Let's not waste time on talking.){/i}"
    "[Name]" "{i}(I have a feeling that you don't need that blanket.){/i}"
    show sc i_Audrey_NV_4 with my_dissolve
    "[Name]" "{i}(Let's take that off...){/i}"
    "[Name]" "{i}(Oh wow...){/i}"
    show sc i_Audrey_NV_5 with my_dissolve
    "[Name]" "{i}(Your breasts are surely happy to see me.){/i}"
    "[Name]" "{i}(Don't worry, I'll be gentle with them.){/i}"
    "[Name]" "{i}(Let me try...){/i}"
    show sc i_Audrey_NV_6 with my_dissolve
    "[Name]" "{i}(To feel them.){/i}"
    "[Name]" "{i}(Ah, that's what I was hoping for...){/i}"
    "[Name]" "{i}(Audrey, your breasts are amazing.){/i}"
    show sc i_Audrey_NV_7 with my_dissolve
    "[Name]" "{i}(But I can't be sure untill I try both...){/i}"
    "[Name]" "{i}(Oh yes.){/i}"
    show sc i_Audrey_NV_8 with my_dissolve
    "[Name]" "{i}(That's what I'm talking about.){/i}"
    "[Name]" "{i}(Your nipples are getting hard.){/i}"
    show sc i_Audrey_NV_9 with my_dissolve
    "[Name]" "{i}(Are you dreaming about me squeezing them?){/i}"
    "[Name]" "{i}(I know you do.){/i}"
    show sc i_Audrey_NV_anim_1 with my_dissolve
    "[Name]" "{i}(And I'm happy to deliever this pleasure to you.){/i}"
    "[Name]" "{i}(Yeah, that's what I was talking about){/i}"
    "Audrey" "Ah..."
    show sc i_Audrey_NV_anim_2 with my_dissolve
    "[Name]" "{i}(I knew you like it...){/i}"
    "[Name]" "{i}(Are you getting turned on already?){/i}"
    "Audrey" "Ah... Yes..."
    show sc i_Audrey_NV_17 with my_dissolve
    "[Name]" "{i}(Oh shit... Did she just talked through her sleep?){/i}"
    "[Name]" "{i}(What a horny little lioness...){/i}"
    show sc i_Audrey_NV_13 with my_dissolve
    "[Name]" "{i}(Now, let's see if you are wet already.){/i}"
    "[Name]" "{i}(I'll just gently move my hand...){/i}"
    show sc i_Audrey_NV_14 with my_dissolve
    "[Name]" "{i}(And here we are.){/i}"
    "[Name]" "{i}(Oh yes, you are a little bit wet...){/i}"
    "[Name]" "{i}(Are you ready to turn this bed into a lake, then?){/i}"
    show sc i_Audrey_NV_15 with my_dissolve
    "[Name]" "{i}(If I'm right, your clit should be right here...){/i}"
    "[Name]" "{i}(Let's start with a gentle press...){/i}"
    "Audrey" "Ah..."
    "[Name]" "{i}(She clearly likes it...){/i}"
    "[Name]" "{i}(I wonder how far this can go...){/i}"
    "Audrey" "Ah... ah..."
    "[Name]" "{i}(This must be your sweetest dream in a long time...){/i}"
    "[Name]" "{i}(Push a little harder...){/i}"
    show sc i_Audrey_NV_16 with my_dissolve
    "Audrey" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I think she might wake up...){/i}"
    "[Name]" "{i}(Better get out of here.){/i}"
    scene expression '#000' with Dissolve(.5)
    return


label Audrey_events_4_label_4_shemale:

    scene sc i_Audrey_NV_1 with Dissolve(.5)
    "[Name]" "{i}(Still can't believe how cute Audrey looks while she asleep.){/i}"
    "[Name]" "{i}(You are an interesting lady, Audrey.){/i}"
    show sc i_Audrey_NV_2 with my_dissolve
    "[Name]" "{i}(Let's not waste time on talking.){/i}"
    "[Name]" "{i}(I have a feeling that you don't need that blanket.){/i}"
    show sc i_Audrey_NV_4 with my_dissolve
    "[Name]" "{i}(Let's take that off...){/i}"
    "[Name]" "{i}(Oh wow...){/i}"
    show sc i_Audrey_NV_5 with my_dissolve
    "[Name]" "{i}(Your breasts are surely happy to see me.){/i}"
    "[Name]" "{i}(Don't worry, I'll be gentle with them.){/i}"
    "[Name]" "{i}(Let me try...){/i}"
    show sc i_Audrey_NV_6 with my_dissolve
    "[Name]" "{i}(To feel them.){/i}"
    "[Name]" "{i}(Ah, that's what I was hoping for...){/i}"
    "[Name]" "{i}(Audrey, your breasts are amazing.){/i}"
    show sc i_Audrey_NV_7 with my_dissolve
    "[Name]" "{i}(But I can't be sure untill I try both...){/i}"
    "[Name]" "{i}(Oh yes.){/i}"
    show sc i_Audrey_NV_8 with my_dissolve
    "[Name]" "{i}(That's what I'm talking about.){/i}"
    "[Name]" "{i}(Your nipples are getting hard.){/i}"
    show sc i_Audrey_NV_9 with my_dissolve
    "[Name]" "{i}(Are you dreaming about me squeezing them?){/i}"
    "[Name]" "{i}(I know you do.){/i}"
    show sc i_Audrey_NV_anim_1 with my_dissolve
    "[Name]" "{i}(And I'm happy to deliever this pleasure to you.){/i}"
    "[Name]" "{i}(Yeah, that's what I was talking about){/i}"
    "Audrey" "Ah..."
    show sc i_Audrey_NV_anim_2 with my_dissolve
    "[Name]" "{i}(I knew you like it...){/i}"
    "[Name]" "{i}(Are you getting turned on already?){/i}"
    "Audrey" "Ah... Yes..."
    show sc i_Audrey_NV_17 with my_dissolve
    "[Name]" "{i}(Oh shit... Did she just talked through her sleep?){/i}"
    "[Name]" "{i}(What a horny little lion...){/i}"
    show sc i_Audrey_NV_21 with my_dissolve
    "[Name]" "{i}(Now, let's see if your manly parts are happy to see me.){/i}"
    "[Name]" "{i}(I'll just gently move my hand...){/i}"
    show sc i_Audrey_NV_22 with my_dissolve
    "[Name]" "{i}(And here we are.){/i}"
    "[Name]" "{i}(What's the matter? I thought you liked my teasing...){/i}"
    "[Name]" "{i}(Or do you need a special treatment?){/i}"
    show sc i_Audrey_NV_23 with my_dissolve
    "[Name]" "{i}(Let me get a good grasp...){/i}"
    "[Name]" "{i}(Oh, it's erected. A little bit.){/i}"
    "Audrey" "Ah..."
    "[Name]" "{i}(So you like it, don't you?){/i}"
    "[Name]" "{i}(Alright, I'll jerk you off...){/i}"
    "Audrey" "{i}(You'd do the same for me if you were on my place.){/i}"
    "[Name]" "{i}(Let's try to get those panties off...){/i}"
    show sc i_Audrey_NV_16 with my_dissolve
    "Audrey" "Mhm... mmm..."
    "[Name]" "{i}(Damn, I think she might wake up...){/i}"
    "[Name]" "{i}(Better get out of here and get some sleep.){/i}"

    scene expression '#000' with Dissolve(.5)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
