label set_auto_events_dale:
    $ dow = 'SAT'
    if 'Gordon_1_label' not in events:
        $ Event('Gordon_1_label', 'dale_shop', 'Gordon_1_label', time = [1,2, 3])
        $ Event('mina_1_label', 'dale_hotel', 'mina_1_label', time = [1,2, 3])
        $ Event('Jill_1_label', 'dale_spa', 'Jill_1_label', time = [1,2, 3])
    if 'adele_1_label' not in events:
        $ Event('adele_1_label', 'dale_club', 'adele_1_label', time = [1,2, 3, 4])
    hide screen arthur_2_0_screen
    hide screen arthur_2_45_screen 
    with Dissolve(.5)
    
    $ change_location(location = 'dale_mainstreet')
    jump main_interface_label

label arthur_2:
    
    $ load_image_now = 'Haley_7'
    call pre_load_web_image from _call_pre_load_web_image_3
    $ load_image_now = 'Elijah_2'
    call pre_load_web_image from _call_pre_load_web_image_4
    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface


    scene expression '#000'
    with Dissolve(1)
    if hasattr(store, 'Q_Arthur') and Q_Arthur>1:
        jump arthur_2_0

    #$ check_arthur_2 = True

    if renpy.music.get_playing():
        stop music fadeout 1
        play music_2 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif renpy.music.get_playing('music_2'):
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2
    elif True:
        stop music_2 fadeout 1
        play music 'audio_ep2/SC/'+renpy.random.choice(['8. Beautiful people.mp3', '9. Hot coffee.mp3', '11. Cosy song.mp3', '12. Fluids.mp3', '19. Endless Adventure.mp3', '23. Live Neutral.mp3', '28. Spring time.mp3', '34. Flirt.mp3', '35. Sadness.mp3',]) fadein 2



    play sound 'audio/new/gameplay/phone_calling2.mp3'
    'Ring, ring...' ""
    scene sc i_Haley_7_1 with Dissolve(.5)
    "[Name]" "Hello?"
    "Elijah" "Yo, [Name]! Rise and shine!"
    "[Name]" "What the hell, Isn't it too early?"
    "Elijah" "If you don't want to miss the principal's speech, it's not."
    show sc i_Haley_7_4 with my_dissolve
    "[Name]" "Shit. I'll be in the hall in a minute."
    "Elijah" "Alright, I'm waiting for you."
    show sc i_Elijah_2_1 with my_dissolve
    "Arthur" "Greetings, students!"
    "Arthur" "I'm sure you're wondering why I've gathered you all here today!"
    show sc i_Elijah_2_2 with my_dissolve
    "Arthur" "Every Saturday morning, we summarise the results of our traditional house tournament."
    "Arthur" "In a few moments, we will announce the final results."
    show sc i_Elijah_2_4 with my_dissolve
    "Arthur" "But first, I'd like to speak on behalf of Ñordale's council."
    "Arthur" "We are incredibly proud of your dedication and hard work."
    show sc i_Elijah_2_8 with my_dissolve
    "Arthur" "Competition is, indeed, one of the keys to unlock your full potential."
    "Arthur" "By participating in it, you can show your diligence and strength."
    "Arthur" "We are happy to be a part of your winding path of discovering true power."
    show sc i_Elijah_2_2 with my_dissolve
    "Arthur" "We've calculated the total points for each House."
    if not hasattr(store, 'wins_house'):

        $ wins_house = get_all_collest_home()
    if wins_house  == 'Leonheart':
        $ pass
    elif True:
        jump arthur_2_32
    
    show sc i_Elijah_2_2 with my_dissolve
    "Arthur" "This week's winner house is {b}Leonheart{/b}!"
    show sc i_Elijah_2_13 with my_dissolve
    "[Name]" "Yahoo! We won!"
    "Elijah" "Great job, everyone!"
    show sc i_Elijah_2_8 with my_dissolve
    "Arthur" "Congratulations to Leonheart! The path to Dale is now open to you."
    "Arthur" "Your ship to Dale leaves soon."
    "Arthur" "Please, seek assistance from Mister Frollo after this meeting"
    show sc i_Elijah_2_5 with my_dissolve
    "Arthur" "To all the other students who haven't won this week: try to keep up your spirits!"
    "Arthur" "You will have a chance to visit Dale next time."
    "Arthur" "All you need is to put more effort and win next week's competition!"
    show sc i_Elijah_2_2 with my_dissolve
    "Arthur" "Take care, everyone, and have a lovely weekend!"
    "[Name]" "Well, that was informative."
    "[Name]" "Now I need to find mister Frollo"
    jump arthur_2_3

label arthur_2_32:
    
    show sc i_Elijah_2_2 with my_dissolve
    "Arthur" "This week's winner house is {b}[wins_house]{/b}!"
    show sc i_Elijah_2_7 with my_dissolve
    "[Name]" "Crap, we've lost this week..."
    "Elijah" "Never mind, there're plenty of weeks ahead of us to win once or twice."
    "[Name]" "You're not very optimistic about us."
    show sc i_Elijah_2_8 with my_dissolve
    "Arthur" "Congratulations to [wins_house]! The path to Dale is now open to you."
    "Arthur" "After this meeting, please follow Mister Frollo."
    show sc i_Elijah_2_5 with my_dissolve
    "Arthur" "He will help you to get to the ferry"
    "Arthur" "To all the other students who haven't won this week: try to keep up your spirits!"
    "Arthur" "You will have a chance to visit Dale next time."
    show sc i_Elijah_2_2 with my_dissolve
    "Arthur" "All you need is to put more effort and win next week's competition!"
    show sc i_Elijah_2_6 with my_dissolve
    "Arthur" "Take care, everyone, and have a lovely weekend!"
    "[Name]" "Well, that was informative."
    "[Name]" "Now I can get back and sleep a little longer..."
label arthur_2_45:
    scene expression '#000'
    show screen arthur_2_45_screen 

    with Dissolve(.5)
    $ renpy.pause(99999999999)

    $ day_now -= 1
    $ time_now = 4
    hide screen arthur_2_0_screen
    hide screen arthur_2_45_screen 
    with Dissolve(.5)
    
    $ change_location_2(location_now, time_now +1, sleep = True)
    $ p_up('Arthur', 2)
    $ Q_Arthur=2
    if wins_house  == 'Leonheart':
        jump set_auto_events_dale
        $ change_location(location = 'dale_mainstreet')
    jump main_interface_label


screen arthur_2_45_screen:
    vbox xalign .5 yalign .5:
        text 'At the moment, weekend activities are only available in Dale. To check them out - win a weekly house tournament' xalign .5
        text "For now, we'll skip the weekends and get straight back to Monday." xalign .5

screen arthur_2_0_screen:
    vbox xalign .5 yalign .5:
        text "At the moment, weekend activities are only available in Dale. To check them out - win a weekly house tournament" xalign .5
        text "For now, we'll skip the weekends and get straight back to Monday." xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label arthur_2_0:
    show sc i_Elijah_2_1 with my_dissolve
    "Arthur" "Greetings, students!"
    "Arthur" "As usual, we're gathered you here to announce the results of our traditional house tournament."
    "Arthur" "We've calculated the total points for each House. And the winner is..."
    if not hasattr(store, 'wins_house'):

        $ wins_house = get_all_collest_home()
    if wins_house  == 'Leonheart':
        $ pass
    elif True:
        jump arthur_2_0_18
    show sc i_Elijah_2_2 with my_dissolve
    "Arthur" "{b}Leonheart{/b}!"
    show sc i_Elijah_2_13 with my_dissolve
    "[Name]" "Yahoo! We won!"
    "Elijah" "Great job, everyone!"
    show sc i_Elijah_2_8 with my_dissolve
    "Arthur" "Congratulations to Leonheart! The path to Dale is now open to you."
    "Arthur" "Your ship to Dale leaves soon."
    "Arthur" "Please, seek assistance from Mister Frollo after this meeting"
    show sc i_Elijah_2_5 with my_dissolve
    "Arthur" "To all the other students who haven't won this week: try to keep up your spirits!"
    "Arthur" "You will have a chance to visit Dale next time."
    "Arthur" "All you need is to put more effort and win next week's competition!"
    show sc i_Elijah_2_2 with my_dissolve
    "Arthur" "Take care, everyone, and have a lovely weekend!"
    "[Name]" "Well, that was informative."
    "[Name]" "Now I need to find mister Frollo"
    jump arthur_2_3
label arthur_2_0_18:
    show sc i_Elijah_2_2 with my_dissolve
    "Arthur" "{b}[wins_house]{/b}!"
    show sc i_Elijah_2_7 with my_dissolve
    "[Name]" "Crap, we've lost this week..."
    "Elijah" "Never mind, there're plenty of weeks ahead of us to win once or twice."
    "[Name]" "Well, that was informative."
    "[Name]" "Now I can get back and sleep a little longer..."
    scene expression '#000'
    show screen arthur_2_0_screen 

    with Dissolve(.5)
    $ renpy.pause(99999999999)

    $ day_now -= 1
    $ time_now = 4
    hide screen arthur_2_0_screen
    hide screen arthur_2_45_screen 
    with Dissolve(.5)
    
    $ change_location_2(location_now, time_now +1, sleep = True)
    if wins_house  == 'Leonheart':
        jump set_auto_events_dale
        $ change_location(location = 'dale_mainstreet')
    jump main_interface_label

label arthur_2_3:


    show sc i_Arthur_3_2 with my_dissolve
    "Jacob" "Mr. [Surname]!"
    "Jacob" "I think we're just waiting for you."
    "Jacob" "All right, let's not stall!"
    "Jacob" "The ferry leaves in half an hour."
    "Jacob" "Students, follow me."
    show sc i_Arthur_3_3 with my_dissolve
    "Haley" "Hello, [Name]!"
    "[Name]" "Haley, good morning!"
    show sc i_Arthur_3_4 with my_dissolve
    "Haley" "Do you have plans for Dale yet?"
    "[Name]" "I don't even know what's there."
    "Haley" "Neither do I. I'm gonna look into it. I hope the local library has a history of the town..."
    "[Name]" "I'm sure there is."
    show sc i_Arthur_3_5 with my_dissolve
    "Haley" "Oh, Lily, I was just looking for you!"
    "Haley" "Aren't you going to the library?"
    show sc i_Arthur_3_37 with my_dissolve
    "Haley" "See you later, [Name]!"
    "[Name]" "Bye..."
    show sc i_Arthur_3_38 with my_dissolve
    "[Name]" "(Hmm, so Haley's gonna be at the library all weekend?)"
    "[Name]" "(Sometimes I don't understand her interests.)"
    show sc i_Arthur_3_6 with my_dissolve
    "[Name]" "(I wonder what I'll be doing this weekend?)"
    scene image '#000' with Dissolve(.5)
    scene sc i_cord_pier_1 with Dissolve(.5)
    "[Name]" "Wow, wow, this is beautiful!"
    "Jacob" "Impressed?"
    "Jacob" "This ship is my pride."
    show sc i_Arthur_3_7 with my_dissolve
    "[Name]" "Why, sir?"
    "Jacob" "It's a system I designed."
    "[Name]" "What system?"
    "Jacob" "You'll hear about it in a moment. I think everyone needs this information."
    show sc i_Arthur_3_8 with my_dissolve
    "Jacob" "Students! Pay attention."
    "Jacob" "We at Cordale are well aware that..."
    "Jacob" "...students have to work hard to become great wizards."
    "Jacob" "So you need to get plenty of rest, too."
    show sc i_Arthur_3_9 with my_dissolve
    "Jacob" "You, as the winners of the house competition, can board the ship."
    "Jacob" "The journey to Dale is not very long."
    "Jacob" "And this ship has everything you need so you don't get bored while you're sailing."
    show sc i_Arthur_3_10 with my_dissolve
    "Lily" "But why a ship at all? We could just teleport..."
    "Jacob" "Thanks for that interesting point!"
    "Jacob" "Portal magic in Cordale territory is limited as much as possible."
    "Jacob" "It's a security measure."
    "Jacob" "But there is a special connection between the academy and Dale."
    show sc i_Arthur_3_11 with my_dissolve
    "Jacob" "The endless lake."
    "[Name]" "What is that?"
    "Jacob" "My own invention."
    show sc i_Arthur_3_12 with my_dissolve
    "Jacob" "The lake seems small, but anyone who decides to swim across it..."
    "Jacob" "You don't even want to know."
    show sc i_Arthur_3_13 with my_dissolve
    "Jacob" "The only vessel that can cross it is right here in front of you."
    "Jacob" "Just don't jump overboard unnecessarily."
    "Jacob" "Then the journey to Dale won't be a problem at all."
    "Jacob" "Any other questions?"
    show sc i_Arthur_3_14 with my_dissolve
    "Haley" "Can I get on board now?"
    "Jacob" "Of course. Come on in and take your seats."
    "Jacob" "We'll be departing in exactly 15 minutes."
    "Jacob" "Did you hear that?"
    "[Name]" "Yes, yes."
    scene image '#000' with Dissolve(.5)
    scene sc i_Arthur_3_15 with Dissolve(.5)
    "[Name]" "(Well, it's time to go to town!)"
    show sc i_Arthur_3_16 with my_dissolve
    "[Name]" "(Wow, I've never been on the ship before.)"
    "[Name]" "(I's shaking when people get on the deck... Should it be like that?)"
    "[Name]" "(Well, Haley doesn't look scared. I think it's alight.)"
    show sc i_Arthur_3_17 with my_dissolve
    "[Name]" "(Wow! What a view!)"
    "[Name]" "(Who might've thought that a boat trip could be so picturesque.)"
    "[Name]" "(I wish I had my camera with me.)"
    show sc i_Arthur_3_18 with my_dissolve
    "[Name]" "(It's so peaceful. That's how any weekend should start.)"
    "[Name]" "(I might start enjoying winning house tournaments.)"
    show sc i_Arthur_3_19 with my_dissolve
    "[Name]" "Ouch...Ough..."
    "[Name]" "(My head...)"
    show sc i_Arthur_3_20 with my_dissolve
    "[Name]" "(Fuck... What's happening?)"
    "[Name]" "(Am I seasick?)"
    scene sc i_Arthur_3_20_1 with Dissolve(.5)
    "[Name]" "Oouh..."
    "[Name]" "I'm gonna..."
    "[Name]" "..."
    scene image '#000' with Dissolve(.5)
    scene sc i_Arthur_3_21 with Dissolve(.5)
    "[Name]" "(What the fuck. Where am I?)"
    "[Name]" "(Is this the place from inside the Sorting Foliant?)"
    "[Name]" "(Why can't I move my arms and legs...)"
    "[Name]" "(Something moving squeezes my body...)"
    show sc i_Arthur_3_22 with my_dissolve
    "[Name]" "WHAT THE FUCK?!"
    "Katrina" "Oh yes... "
    show sc i_Arthur_3_40 with my_dissolve
    "Katrina" "That what I was waiting for."
    "Katrina" "What's the matter now?"
    "Katrina" " You're not so confident anymore!"
    show sc i_Arthur_3_23 with my_dissolve
    "[Name]" "Katrina? What the fuck is happening?!"
    "[Name]" "Where am I? "
    "[Name]" "Is this a dream?"
    show sc i_Arthur_3_24 with my_dissolve
    "Katrina" "Little puppy, why should I bother myself answering you?"
    "Katrina" "You've insulted my pride. Crushed my plans."
    "Katrina" "Chose my enemy and exceeded my house!"
    "Katrina" "You think someone can just do that to Katina Adderin and walk away?!"
    "[Name]" "Wait, let's talk..."
    show sc i_Arthur_3_25 with my_dissolve
    "Katrina" "You've said all you had to say. boy."
    "Katrina" "Enjoy your small victories wile you can."
    "Katrina" "But do not forget about me."
    "Katrina" "Because if I can get you from underworld..."
    "Katrina" "Imagine what I'll do to you when I get out of here!"
    show sc i_Arthur_3_26 with my_dissolve
    "[Name]" "(I... Can't... Breathe...)"
    "[Name]" "(It's over...)"
    "..." "Hey!"
    show sc i_Arthur_3_27 with my_dissolve
    "..." "Wake up."
    "..." "We're here!"
    "..." "Why are you shaking?"
    scene image '#000' with Dissolve(.5)
    scene sc i_Arthur_3_28 with Dissolve(.5)
    "Haley" "Are you okay? Wake up! "
    "Haley" "There you go. "
    show sc i_Arthur_3_29 with my_dissolve
    "Haley" "You where dreaming... Was it a nightmare? "
    "[Name]" "Yeah,  kind of."
    "Haley" "Well, not even the storm could wake you."
    "Haley" "I was worried."
    show sc i_Arthur_3_30 with my_dissolve
    "[Name]" "Where am I?"
    "Haley" "It's captain's cabin. We took you here when you got sick."
    "[Name]" "Thank you."
    "[Name]" "So... Are we there?"
    show sc i_Arthur_3_31 with my_dissolve
    "Haley" "Yeah. Everybody has already left for Dale."
    "Haley" "Captain said you have five minutes to get out/"
    "Haley" 'She was very pissed with your "moanings."'
    show sc i_Arthur_3_39 with my_dissolve
    "Haley" "Do you think it's hard to navigate the ship?"
    "[Name]" "Sorry, I'm not in the mood to hijack the ship."
    "Haley" "When will you learn to get when I'm joking and when I'm serious."
    show sc i_Arthur_3_32 with my_dissolve
    "[Name]" "We should spend more time together if you want me to do that."
    "Haley" "Are you offering me a date?"
    "[Name]" "I do not dare to stand between you and local library."
    "[Name]" "But maybe after you learn all about Dale."
    show sc i_Arthur_3_33 with my_dissolve
    "Haley" "Maybe. Who knows..."
    "[Name]" "You're killing me."
    "Haley" "Then I'd better get out of a crime scene."
    show sc i_Arthur_3_34 with my_dissolve
    "Haley" "And you'd better get going too."
    "Haley" "Captain said she'd feed you to sharks if you dont leave."
    "[Name]" "Do you think there are sharks in the lake?"
    "Haley" "Would you be suprised?"
    show sc i_Arthur_3_35 with my_dissolve
    "Haley" "Bye!"
    "[Name]" "(Maybe she's right.)"
    show sc i_Arthur_3_36 with my_dissolve
    "[Name]" "(Well, I should probably go too.)"
    "[Name]" "(I'll think about crazy old witch inside of my mind later.)"
    "[Name]" "(Don't want it to ruin my weekend.)"

    with Dissolve(.5)
    $ renpy.pause(99999999999)

    #$ day_now -= 1
    $ time_now = 2
    hide screen arthur_2_0_screen
    hide screen arthur_2_45_screen 
    with Dissolve(.5)
    
    #$ change_location_2(location_now, time_now +1, sleep = True)
    $ p_up('Arthur', 3)
    $ Q_Arthur=3
    if wins_house  == 'Leonheart':
        jump set_auto_events_dale
        $ change_location(location = 'dale_mainstreet')
    jump main_interface_label