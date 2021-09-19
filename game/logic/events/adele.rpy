


label talk_to_adele:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.1)

    menu:
        'Talk to Adele' if Q_Adele == 1:
            hide screen show_hide_locations
            hide screen show_hide_locations_2
            hide screen text_animation_up_screen_3
            hide screen main_interface
            scene image '#000' 
            with Dissolve(.5)
            call adele_2_label from _call_adele_2_label
            $ Q_Adele = 2
        "!Sadira ($250)" if Q_Adele == 2 and money < 250:
            hide screen show_hide_locations
            hide screen show_hide_locations_2
            hide screen text_animation_up_screen_3
            hide screen main_interface
            scene image '#000' 
            with Dissolve(.5)
            call vip_sadira_1_label from _call_vip_sadira_1_label
        "Sadira ($250)" if Q_Adele == 2 and money > 250:
            hide screen show_hide_locations
            hide screen show_hide_locations_2
            hide screen text_animation_up_screen_3
            hide screen main_interface
            scene image '#000' 
            with Dissolve(.5)
            call vip_sadira_1_label from _call_vip_sadira_1_label_1
        "!Lucy ($250)" if Q_Adele == 2 and money < 250:
            hide screen show_hide_locations
            hide screen show_hide_locations_2
            hide screen text_animation_up_screen_3
            hide screen main_interface
            scene image '#000' 
            with Dissolve(.5)
            call vip_lucy_1_label from _call_vip_lucy_1_label
        "Lucy ($250)" if Q_Adele == 2 and money > 250:
            hide screen show_hide_locations
            hide screen show_hide_locations_2
            hide screen text_animation_up_screen_3
            hide screen main_interface
            scene image '#000' 
            with Dissolve(.5)
            call vip_lucy_1_label from _call_vip_lucy_1_label_1
        "Not now":



            #show screen main_interface 
            #show screen show_hide_locations_2
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            hide screen main_interface 
            jump main_interface_label

    hide screen black_tmp_screen_menu


    jump main_interface_label
label adele_1_label:

    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface 
    scene image '#000' with Dissolve(.5)
    scene sc i_Club_1_1 with Dissolve(.5)
    "[Name]" "{i}(Oh là là!){/i}"
    "Adele" "Welcome to the Lady Luck, honey!"
    "Adele" "Don't be shy, come in!"
    show sc i_Club_1_2 with my_dissolve
    "Adele" "My name is Adele."
    "Adele" "It's nice to see you."
    show sc i_Club_1_3 with my_dissolve
    "Adele" "You look like a hero."
    "[Name]" "Come on, I'm just..."
    show sc i_Club_1_4 with my_dissolve
    "Adele" "You won't regreat you've stopped by."
    "[Name]" "{i}(Her hands are so soft...){/i}"
    "[Name]" "{i}(I never thought that a simple touch could be so pleasant...){/i}"
    show sc i_Club_1_5 with my_dissolve
    "[Name]" "I don't want to distract you..."
    "Adele" "Come on."
    "Adele" "The least I can do is give you a tour."
    "Adele" "Follow me."
    show sc i_Club_1_6 with my_dissolve
    "Adele" "There's a great view of the place from here."
    "Adele" "You like what you see?"
    "[Name]" "I guess so."
    show sc i_Club_1_7 with my_dissolve
    "Adele" "Come on."
    "Adele" "I'll show you around!"
    show sc i_Club_1_8 with my_dissolve
    "[Name]" "{i}(I'm already intrigued.){/i}"
    "[Name]" "{i}(I wonder if she dances, too.){/i}"
    "[Name]" "Where are we going?"
    show sc i_Club_1_9 with my_dissolve
    "Adele" "To meet these pretty girls!"
    "Adele" "Lucy is our young beauty from Europe."
    "Adele" "She's still very naive and young."
    show sc i_Club_1_10 with my_dissolve
    "Adele" "But you wouldn't know it from her body."
    "Adele" "I don't know if you'll have much to talk about."
    "Adele" "But you'll certainly have a lot to do together."
    show sc i_Club_1_11 with my_dissolve
    "Adele" "Let's continue!"
    "[Name]" "Whoa... I thought we were going to Lucy's table..."
    "Adele" "Silly, who makes a choice without looking at all the offers?"
    show sc i_Club_1_12 with my_dissolve
    "Adele" "The exotic beauty Sadira."
    "Adele" "She holds a lot of surprises."
    show sc i_Club_1_13 with my_dissolve
    "[Name]" "I can imagine...."
    "Adele" "A lot of people would kill to see her private show."
    "Adele" "But I'd rather have you pay than kill someone. "
    show sc i_Club_1_14 with my_dissolve
    "[Name]" "Alight-alright, No killing today."
    "[Name]" "{i}(This place looks very promising.){/i}"
    show sc i_Club_1_15 with my_dissolve
    "Adele" "At the top of the stairs situated our private VIP lounge."
    "Adele" "A VIP lounge, you say? What's so different about it?"
    "Adele" "Oh, honey."
    "Adele" "Believe me, depending on your generosity, a lot of things are possible in there."
    show sc i_Club_1_16 with my_dissolve
    "Adele" "A lot of things."
    "Adele" "All of our customers' fondest memories of the club are associated with this place."
    "Adele" "And many of my fondest memories, too."
    "[Name]" "Are you available in the VIP lounge, too?"
    show sc i_Club_1_16 with my_dissolve
    "Adele" "Not usually."
    show sc i_Club_1_17 with my_dissolve
    "Adele" "But for you, I can somehow make an exception."
    "Adele" "Later on..."
    "[Name]" "I'll remember that."
    show sc i_Club_1_18 with my_dissolve
    "Adele" "Anyway, if you want to watch a dance or go to a private room."
    "Adele" "You can come up to me, or you can go straight to the tables where the girls dance."
    show sc i_Club_1_19 with my_dissolve
    "Adele" "Is that clear?"
    "[Name]" "Yes, absolutely."
    "Adele" "Great. Then that concludes our tour."
    "[Name]" "Thank you very much."
    show sc i_Club_1_20 with my_dissolve
    "Adele" "One more thing!"
    "Adele" "Come on, I'll show you our bar."
    "Adele" "Vanessa always treats new customers to a complimentary drink."
    "[Name]" "Thank you!"
    show sc i_Club_1_21 with my_dissolve
    "[Name]" "{i}(Well... A free drink doesn't sound bad at all.){/i}"
    "[Name]" "{i}(I love this place!){/i}"
    show sc i_Club_1_22 with my_dissolve
    "[Name]" "{i}(Let's see what we have here.){/i}"
    "Adele" "So, here we are."
    show sc i_Club_1_24 with my_dissolve
    "Adele" "Vanessa, should be here any minute."
    "Adele" "By the way, I completely forgot to ask your name."
    "[Name]" "[Name]."
    show sc i_Club_1_25 with my_dissolve
    "Adele" "[Name], Sorry, but I have to run."
    "[Name]" "C'ya."
    "[Name]" "(I'll miss her company.)"
 
    scene sc i_Vanessa_anim_1 with Dissolve(.5)
    #stop music_2 fadeout 1.0
    #play music 'audio/new/Music/background_music1.mp3' fadein 10.0
    play sound_2 'audio/new/Music/intro1.mp3' fadein 1.0
    "[Name]" "(So, what do we have here...)"
    show sc i_Club_1_26 with my_dissolve
    "[Name]" "(Oh my!)"
    "[Name]" "(She looks... devilish...)"
    "Vanessa" "Hello there."
    "Vanessa" "Don't be so nervious."
    "[Name]" "{i}(What an unusual color in her eyes...){/i}"
    "[Name]" "What makes you think I'm nervous?"
    show sc i_Club_1_27 with my_dissolve
    "Vanessa" "Oh, that's easy."
    "Vanessa" "I can feel your blood chilling."
    "Vanessa" "I think I know what you need."
    "[Name]" "You do?"
    show sc i_Club_1_28 with my_dissolve
    "Vanessa" "Yeah. My signature cocktail."
    "[Name]" "What's in it?"
    "Vanessa" "Everything you need and not a pinch of unnecessary information."
    show sc i_Club_1_29 with my_dissolve
    "Vanessa" "Here you go..."
    "[Name]" "{i}(I can't figure out why, but this cocktail scares me...){/i}"
    menu:
        "Accept the drink":
            $ club_drink = 1
            show sc i_Club_1_30 with my_dissolve
            "[Name]" "{i}(What am I, a pussy?){/i}"
            show sc i_Club_1_31 with my_dissolve
            "[Name]" "{i}Cheers!{/i}"
            "[Name]" "{i}(Wow... That's not so bad!){/i}"
            show sc i_Club_1_32 with my_dissolve
            "[Name]" "Wow...O-o-oh..."
            "[Name]" "{i}(I don't know what's happening.){/i}"
            "[Name]" "{i}(It feels like everything inside me got so hot and cold at the same time...){/i}"
            show sc i_Club_1_33 with my_dissolve
            "Vanessa" "What happened, is it too strong for you?"
            "Vanessa" "I think I overestimated you."
            show sc i_Club_1_34 with my_dissolve
            "Vanessa" "It's okay, what you're feeling won't last long."
            "[Name]" "What's in this cocktail?"
            show sc i_Club_1_35 with my_dissolve
            "Vanessa" "Don't worry, handsome."
            "Vanessa" "You won't taste it anywhere else."
            show sc i_Club_1_36 with my_dissolve
            "Vanessa" "At first, a living person might find the taste unusual..."
            "[Name]" "A living person?"
            show sc i_Club_1_37 with my_dissolve
            "Vanessa" "Mmm..."
            "Vanessa" "It's good."
            "[Name]" "{i}(I almost died from a sip, and she didn't bat an eye!){/i}"
            show sc i_Club_1_38 with my_dissolve
            "Guy" "One more round for me and my friends, baby!"
            "Vanessa" "Uh..."
            show sc i_Club_1_39 with my_dissolve
            "Vanessa" "Sorry, kid. Work's calling."
            "Vanessa" "It was nice meeting you."
            "[Name]" "{i}(Isn't she gonna answer me?){/i}"
            show sc i_Club_1_40 with my_dissolve
            "Vanessa" "I'm on my way!"
            "[Name]" "But what was in the cocktail?"
            show sc i_Club_1_41 with my_dissolve
            "[Name]" "{i}(Who does that? Unbelievable!){/i}"
            "[Name]" "{i}(She's obviously no ordinary girl...){/i}"
            "[Name]" "{i}(Okay, I've had enough alcohol for one day.){/i}"
        "Ask for a beer":
            show sc i_Club_1_42 with my_dissolve
            "[Name]" "No, baby, thanks, but I only drink beer."
            "Vanessa" "You have no idea how much you're missing out on."
            show sc i_Club_1_43 with my_dissolve
            "Vanessa" "But what can I do, the customer is always right."
            "Vanessa" "There was a bottle of cold one in here somewhere...."
            show sc i_Club_1_44 with my_dissolve
            "Vanessa" "Here you go."
            "[Name]" "Thank you."
            show sc i_Club_1_45 with my_dissolve
            "[Name]" "To getting to know each other?"
            "Vanessa" "To getting to know you."
            show sc i_Club_1_46 with my_dissolve
            "Vanessa" "Still, you shouldn't have tried the cocktail."
            "Vanessa" "Our special is legendary around here."
            "[Name]" "Maybe some other time."
            show sc i_Club_1_37 with my_dissolve
            "Vanessa" "Your loss."
            "Vanessa" " Cheers!"
            "[Name]" "{i}(Maybe I shouldn't have trusted her.){/i}"
            "[Name]" "{i}(It looks really good from the outside.){/i}"
            show sc i_Club_1_38 with my_dissolve
            "Guy" "One more round for me and my friends, baby!"
            "Vanessa" "Uh..."
            show sc i_Club_1_39 with my_dissolve
            "Vanessa" "Sorry, kid. Work calls."
            "Vanessa" "It was nice to meet you."
            "[Name]" "Nice to meet you, too."
            show sc i_Club_1_40 with my_dissolve
            "Vanessa" "I'm on my way!"
            "[Name]" "{i}(Now I'm wondering what kind of cocktail this is.){/i}"
            show sc i_Club_1_41 with my_dissolve
            "[Name]" "{i}(Who does that? Unbelievable!){/i}"
            "[Name]" "{i}(She's obviously no ordinary girl...){/i}"
            "[Name]" "{i}(Okay, I've had enough alcohol for one day.){/i}"

        "Decline the drink":
            show sc i_Club_1_47 with my_dissolve
            "[Name]" "Sorry, I don't drink."
            "Vanessa" "At all?!"
            "[Name]" "I'm definitely gonna pass tonight."
            show sc i_Club_1_36 with my_dissolve
            "Vanessa" "You don't know what you're giving up."
            "Vanessa" "It's my greatest invention."
            show sc i_Club_1_37 with my_dissolve
            "Vanessa" "Mmm..."
            "Vanessa" "Yeah..."
            "[Name]" "{i}(Maybe I should have trusted her.){/i}"
            "[Name]" "{i}(It looks really good from the outside.){/i}"
            show sc i_Club_1_38 with my_dissolve
            "Guy" "One more round for me and my friends, baby!"
            "Vanessa" "Eh..."
            show sc i_Club_1_39 with my_dissolve
            "Vanessa" "Sorry, kid. Work calls."
            "Vanessa" "I don't get paid to talk."
            "[Name]" "{i}(Fair enough.){/i}"
            show sc i_Club_1_40 with my_dissolve
            "Vanessa" "I'm on my way!"
            "[Name]" "{i}(Maybe I should have agreed to a cocktail.){/i}"
            show sc i_Club_1_41 with my_dissolve
            "[Name]" "{i}(Okay, another time.){/i}"
            "[Name]" "{i}(For now, just enjoying the view.){/i}"
            "[Name]" "{i}(There's no problem at all with that.){/i}"
    show sc i_Club_1_48 with my_dissolve
    "[Name]" "{i}(Okay. Now I know what the club has to offer me.){/i}"
    "[Name]" "{i}(I just have to figure out what I want.){/i}"
    "[Name]" "{i}(And what I can afford.){/i}"

    $ p_up('Adele', 1)
    $ Q_Adele = 1
    jump main_interface_label

label adele_2_label:



    show sc i_Adele_1_1 with my_dissolve
    "Adele" "What can I do for you, honey?"
    "Adele" "Walk you to a free table?"
    "Adele" "Or would you be more interested in going up to the VIP lounge?"
    scene sc i_Adele_1_2 with Dissolve(.5)
label adele_2_label_6:
    menu:
        "Free table":
            $ pass
        "VIP lounge":

            jump adele_2_label_30
    show sc i_Adele_1_2 with my_dissolve
    "[Name]" "I'd like to sit at a table and enjoy the dance."
    "Adele" "Sure, baby! Whatever you want!"
    show sc i_Adele_1_3 with my_dissolve
    "Adele" "Come to this table."
    "[Name]" "Oh, thank you."
    show sc i_Adele_1_4 with my_dissolve
    "Adele" "Which of the girls should I call for you, honey?"
    "[Name]" "{i}(What kind of view do I want to enjoy tonight?){/i}"
    show sc i_Adele_1_5 with my_dissolve
label adele_2_label_13:
    scene sc i_Adele_1_5 with Dissolve(.5)
    menu:
        "Sadira":

            call adele_2_label_14 from _call_adele_2_label_14
        "Lucy":
           
            call adele_2_label_17 from _call_adele_2_label_17
        "You" if not hasattr(store, 'adele_2_label_13_var'):
            $ adele_2_label_13_var = True
            show sc i_Adele_1_5 with my_dissolve
            "[Name]" "Why call someone, baby?"
            show sc i_Adele_1_7 with my_dissolve
            "[Name]" "I'm here for you."
            "Adele" "Aww..."
            show sc i_Adele_1_8 with my_dissolve
            "Adele" "That's so sweet, honey!"
            "Adele" "But also - not gonna happen."
            "[Name]" "Why not?"
            show sc i_Adele_1_9 with my_dissolve
            "Adele" "I'm not dancing. "
            "Adele" "Maybe later we can arrange a VIP lounge."
            "Adele" "But for now I'm not ready. Sorry."
            "Adele" "Pick someone else."
            jump adele_2_label_13
label adele_2_label_14:
    show sc i_Adele_1_5 with my_dissolve
    "[Name]" "I was thinking about something oriental..."
    show sc i_Adele_1_6 with my_dissolve
    "Adele" "Say no more, honey!"
    "Adele" "Sadira will be here in a moment..."
    call Sadira_1_label from _call_Sadira_1_label
    $ Q_Adele=2
    if not hasattr(store,'Q_Sadira'):
        call Sadira_2_label from _call_Sadira_2_label
        $ p_up('Sadira', 1)
        $ Q_Sadira = 1
        $ change_location_2(location_now, time_now+1, sleep = True)
        jump main_interface_label
    
    return
label adele_2_label_17:
    show sc i_Adele_1_5 with my_dissolve
    "[Name]" "Is Lucy working tonight?"
    show sc i_Adele_1_6 with my_dissolve
    "Adele" "For you - she will!"
    "Adele" "Lucy will be here in a moment..."
    call Lucy_1_label from _call_Lucy_1_label
    $ Q_Adele=2
    if not hasattr(store,'Q_Lucy'):
        call Lucy_2_label from _call_Lucy_2_label
        $ p_up('Lucy', 1)
        $ Q_Lucy = 1
        $ change_location_2(location_now, time_now+1, sleep = True)
        jump main_interface_label
    
    return
label adele_2_label_30:
    show sc i_Adele_1_2 with my_dissolve
    "[Name]" "I'll go straight to VIP."
    "Adele" "Alright, hon. "
    "Adele" "Which of the girls do you want to invnite with you?"
    menu:
        "!Sadira ($250)" if money <  250:
            $ pass
        "!Lucy ($250)"   if money <  250:
            $ pass
        "Sadira ($250)"  if money >= 250:
            "[Name]" "I was thinking about something oriental..."
            show sc i_Club_1_7 with my_dissolve
            "Adele" "Sadira it is."
            "Adele" "Come with me. She'll join us in a munte."
            scene image '#000' with Dissolve(.5)
            $ renpy.pause(.5)
            scene sc i_VIP_1_1 with Dissolve(.5)
            "[Name]" "{i}(Interesting setting...){/i}"
            "Adele" "The most comfortable and secluded place in our club."
            "Adele" "Available only to V.I.P. customers."
            "[Name]" "And what can you do here?"
            show sc i_VIP_1_2 with my_dissolve
            "Adele" "You're the one who decides what to do in this place, honey..."
            show sc i_VIP_1_3 with my_dissolve
            "Adele" "There's cold champagne in the bucket and whiskey at the bar especially for you."
            show sc i_VIP_1_4 with my_dissolve
            "[Name]" "{i}(I didn't expect that kind of service from a small-town club.){/i}"
            show sc i_VIP_1_5 with my_dissolve
            "[Name]" "{i}(I'm starting to like this place!){/i}"
            "[Name]" "So what's next?"
            "Adele" "Relax and get ready to forget all your problems."
            show sc i_VIP_1_6 with my_dissolve
            "Adele" "The show's about to start."
            "[Name]" "{i}(Let's see what you have to offer...){/i}"
            if (LGBTQ == 1):
                $ nv = renpy.call_screen('confirm', "Do you want Sadira to be a female or a shemale?", Return('Girl'), Return('Shemale'), yes_text = _("Girl"), no_text = _("Shemale"),)
            else: 
                $ nv = "Girl"
            $ Q_Adele=2
            call vip_sadira_1_label from _call_vip_sadira_1_label_2
        
        "Lucy ($250)"  if money >= 250:
            "[Name]" "Is Lucy working tonight?"
            show sc i_Club_1_7 with my_dissolve
            "Adele" "For you - she will!"
            "Adele" "Come with me. She'll join us in a munte."
            scene image '#000' with Dissolve(.5)
            $ renpy.pause(.5)
            scene sc i_VIP_1_1 with Dissolve(.5)
            "[Name]" "{i}(Interesting setting...){/i}"
            "Adele" "The most comfortable and secluded place in our club."
            "Adele" "Available only to V.I.P. customers."
            "[Name]" "And what can you do here?"
            show sc i_VIP_1_2 with my_dissolve
            "Adele" "You're the one who decides what to do in this place, honey..."
            show sc i_VIP_1_3 with my_dissolve
            "Adele" "There's cold champagne in the bucket and whiskey at the bar especially for you."
            show sc i_VIP_1_4 with my_dissolve
            "[Name]" "{i}(I didn't expect that kind of service from a small-town club.){/i}"
            show sc i_VIP_1_5 with my_dissolve
            "[Name]" "{i}(I'm starting to like this place!){/i}"
            "[Name]" "So what's next?"
            "Adele" "Relax and get ready to forget all your problems."
            show sc i_VIP_1_6 with my_dissolve
            "Adele" "The show's about to start."
            "[Name]" "{i}(Let's see what you have to offer...){/i}"
            $ Q_Adele=2
            call vip_lucy_1_label from _call_vip_lucy_1_label_2
        
        "You" if not hasattr(store, 'adele_2_label_30_var'):
            $ adele_2_label_30_var = True
            show sc i_Adele_1_2 with my_dissolve
            "[Name]" "I'm here for you, baby."
            "Adele" "Aww..."
            "Adele" "That's so sweet, honey!"
            show sc i_Adele_1_10 with my_dissolve
            "Adele" "Sorry to dissapoint you, but I'm not avaliable tonight."
            "[Name]" "Why not?"
            "Adele" "Sorry, a woman has to keep her secrets. Maybe in future."
            call adele_2_label_30 from _call_adele_2_label_30
        # // только 1 раз
        "Maybe later":
            show sc i_Adele_1_2 with my_dissolve
            "[Name]" "Hm... Come to think of it, I've changed my mind."
            "[Name]" "I think I'll check VIP out next time."
            show sc i_Adele_1_10 with my_dissolve
            "Adele" "That makes me so sad, honey."
            "Adele" "I hope you'll change your mind."
            "Adele" "Maybe a table. then?"
            menu:
                "Sadira":
                    call adele_2_label_14 from _call_adele_2_label_14_1
                "Lucy":
                    call adele_2_label_17 from _call_adele_2_label_17_1

    return






















label Sadira_1_label:
    scene sc i_Sadira_1_1 with Dissolve(.5)
    "[Name]" "{i}(Wow! She looks like she's from a land from a faraway place.){/i}"
    show sc i_Sadira_1_2 with my_dissolve
    "[Name]" "{i}(This might be interesting.){/i}"
    show sc i_Sadira_1_3 with my_dissolve
    "[Name]" "{i}(Her outfit is very sexy...){/i}"
    show sc i_Sadira_1_3 with my_dissolve
    if (LGBTQ == 1):
        $ nv = renpy.call_screen('confirm', "Do you want Sadira to be a female or a shemale?", Return('Girl'), Return('Shemale'), yes_text = _("Girl"), no_text = _("Shemale"),)
    else: 
        $ nv = "Girl"
    if nv == "Girl":
        $ sadira_girl = True
        show sc i_Sadira_1_4 with my_dissolve
        "[Name]" "{i}(Looks like she likes my attention.){/i}"
        show sc i_Sadira_1_5 with my_dissolve
        show sc i_Sadira_1_6 with my_dissolve
        "[Name]" "{i}(She's so flexible.){/i}"
        show sc i_Sadira_1_7 with my_dissolve
        "[Name]" "{i}(Looks like bending like this is not a big deal for her.){/i}"
        show sc i_Sadira_1_8 with my_dissolve
        "[Name]" "{i}(Wow, look at that.){/i}"
        show sc i_Sadira_1_9 with my_dissolve
        "[Name]" "{i}(This baby know what to do with a pole. that's for sure.){/i}"
        show sc i_Sadira_1_10 with my_dissolve
        show sc i_Sadira_1_11 with my_dissolve
        show sc i_Sadira_1_12 with my_dissolve
        "[Name]" "{i}(Oh yes, that looks delicious!){/i}"
        show sc i_Sadira_1_13 with my_dissolve
        "[Name]" "{i}(I could eat her just like that.){/i}"
    else:
        $ sadira_girl = False
        show sc i_Sadira_1_14 with my_dissolve
        show sc i_Sadira_1_15 with my_dissolve
        "[Name]" "{i}(Looks like she likes my attention.){/i}"
        show sc i_Sadira_1_5 with my_dissolve
        show sc i_Sadira_1_16 with my_dissolve
        "[Name]" "{i}(So, you're even more exotic then I thought.){/i}"
        show sc i_Sadira_1_17 with my_dissolve
        "[Name]" "{i}(Interesting...){/i}"
        show sc i_Sadira_1_8 with my_dissolve
        "[Name]" "{i}(Wow, look at that.){/i}"
        show sc i_Sadira_1_9 with my_dissolve
        "[Name]" "{i}(This baby know what to do with a pole. that's for sure.){/i}"
        show sc i_Sadira_1_18 with my_dissolve
        show sc i_Sadira_1_11 with my_dissolve
        show sc i_Sadira_1_19 with my_dissolve
        "[Name]" "{i}(Oh yes, that looks delicious!){/i}"
        show sc i_Sadira_1_13 with my_dissolve
        show sc i_Sadira_1_20 with my_dissolve
        "[Name]" "{i}(I could eat her just like that.){/i}"

    return

label Sadira_2_label:
    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface
    if sadira_girl:
        show sc i_Sadira_2_1 with my_dissolve
        "[Name]" "{i}(Her movements are as mesmerizing and intoxicating as desert heat.){/i}"
        "[Name]" "{i}(I never thought oriental dancing was so hot...){/i}"
        show sc i_Sadira_2_1_2 with my_dissolve
        "[Name]" "{i}(It's just amazing){/i}"
        "[Name]" "{i}(She crawls like a panther to me...){/i}"
        show sc i_Sadira_2_2 with my_dissolve
        "Sadira" "Well, hello..."
        show sc i_Sadira_2_3 with my_dissolve
        "Sadira" "What's your name, handsome?"
        show sc i_Sadira_2_3_2 with my_dissolve
        "[Name]" "Does it matter?"
        "Sadira" "Are you naughty?"
        show sc i_Sadira_2_4 with my_dissolve
        "Sadira" "Be a good boy, okay?"
        "Sadira" "You don't want to make me angry..."
        show sc i_Sadira_2_5 with my_dissolve
        "[Name]" "{i}(What the?){/i}"
        "Sadira" "It would be a pity if you couldn't fully enjoy my company..."
        "[Name]" "{i}(This might be interesting...){/i}"
        "[Name]" "My name is [Name]..."
        "Sadira" "[Name], would you like to be in an oriental fairy tale?"
        show sc i_Sadira_2_6 with my_dissolve
        "[Name]" "Depending on what you mean?"
        "Sadira" "I can show you why Arabian nights are considered the hottest..."
        "[Name]" "Go on..."
        show sc i_Sadira_2_7 with my_dissolve
        "Sadira" "I know a thousand and one fairy tales. And all will be unforgettable to you."
        "[Name]" "I'm all ears."
        "Sadira" "Ah-ha-ha-ha.  Honey, it's too crowdy here."
        "Sadira" "Why don't we go to a more quiet place?"
        "[Name]" "Like the VIP?"
        show sc i_Sadira_2_8 with my_dissolve
        "Sadira" "What do you say?"
        menu:
            "VIP lounge":
                "[Name]" "{i}(How can I resist such an extraordinary beauty?){/i}"
                "[Name]" "Let's see if your fairy tales are that good..."
                "Sadira" "Honey, go tell Adele you want me in VIP lounge."

            "Not tonight":
                
                "[Name]" "I think I'll pass, baby."
                show sc i_Sadira_2_9 with my_dissolve
                "[Name]" "I'll try your oriental charms another time."
                "[Name]" "Not in the mood today."
                show sc i_Sadira_2_10 with my_dissolve
                "Sadira" "Pfft. It's up to you..."
                "[Name]" "I know..."
                show sc i_Sadira_2_10_2 with my_dissolve
                "Sadira" "But you have no idea what you're missing."
                "Sadira" "Think about it next time."
                show sc i_Sadira_2_11 with my_dissolve
                "[Name]" "{i}(That's okay, I'll have time to catch up.){/i}"
       

    else:
        
        show sc i_Sadira_2_1 with my_dissolve
        "[Name]" "{i}(Her movements are as mesmerizing and intoxicating as desert heat.){/i}"
        "[Name]" "{i}(I never thought oriental dancing was so hot...){/i}"
        show sc i_Sadira_2_12 with my_dissolve
        "[Name]" "{i}(It's just amazing){/i}"
        "[Name]" "{i}(She crawls like a panther to me...){/i}"
        show sc i_Sadira_2_13 with my_dissolve
        "Sadira" "Well, hello..."
        show sc i_Sadira_2_3 with my_dissolve
        "Sadira" "What's your name, handsome?"
        show sc i_Sadira_2_14 with my_dissolve
        "[Name]" "Does it matter?"
        "Sadira" "Are you naughty?"
        show sc i_Sadira_2_15 with my_dissolve
        "Sadira" "Be a good boy, okay?"
        "Sadira" "You don't want to make me angry..."
        show sc i_Sadira_2_16 with my_dissolve
        "[Name]" "{i}(What the?){/i}"
        "Sadira" "It would be a pity if you couldn't fully enjoy my company..."
        "[Name]" "{i}(This might be interesting...){/i}"
        "[Name]" "My name is [Name]..."
        "Sadira" "[Name], would you like to be in an oriental fairy tale?"
        show sc i_Sadira_2_6 with my_dissolve
        "[Name]" "Depending on what you mean?"
        "Sadira" "I can show you why Arabian nights are considered the hottest..."
        "[Name]" "Go on..."
        show sc i_Sadira_2_7 with my_dissolve
        "Sadira" "I know a thousand and one fairy tales. And all will be unforgettable to you."
        "[Name]" "I'm all ears."
        "Sadira" "Ah-ha-ha-ha.  Honey, it's too crowdy here."
        "Sadira" "Why don't we go to a more quiet place?"
        "[Name]" "Like the VIP?"
        show sc i_Sadira_2_8 with my_dissolve
        "Sadira" "What do you say?"
        menu:
            "VIP lounge":
                "[Name]" "{i}(How can I resist such an extraordinary beauty?){/i}"
                "[Name]" "Let's see if your fairy tales are that good..."
                "Sadira" "Honey, go tell Adele you want me in VIP lounge."
            "Not tonight":
                "[Name]" "I think I'll pass, baby."
                show sc i_Sadira_2_9 with my_dissolve
                "[Name]" "I'll try your oriental charms another time."
                "[Name]" "Not in the mood today."
                show sc i_Sadira_2_10 with my_dissolve
                "Sadira" "Pfft. It's up to you..."
                "[Name]" "I know..."
                show sc i_Sadira_2_10_2 with my_dissolve
                "Sadira" "But you have no idea what you're missing."
                "Sadira" "Think about it next time."
                show sc i_Sadira_2_17 with my_dissolve
                "[Name]" "{i}(That's okay, I'll have time to catch up.){/i}"
    
    scene image '#000' with Dissolve(.5)
    return


label Lucy_1_label:
    show sc i_Lucy_1_1 with my_dissolve
    "[Name]" "{i}(Looks like she was waiting for some audience.){/i}"
    "[Name]" "{i}(Well, here I am.){/i}"
    show sc i_Lucy_1_2 with my_dissolve
    show sc i_Lucy_1_3 with my_dissolve
    show sc i_Lucy_1_4 with my_dissolve
    "[Name]" "{i}(She looks so young, yet so expirienced.){/i}"
    "[Name]" "{i}(She moves her hips like Shakira...){/i}"
    show sc i_Lucy_1_5 with my_dissolve
    "[Name]" "{i}(Makes me want to speak Spanis...){/i}"
    "[Name]" "{i}(Which is strange, cause Lucy sounds like a French name...){/i}"
    show sc i_Lucy_1_6 with my_dissolve
    "[Name]" "{i}(She looks French...){/i}"
    show sc i_Lucy_1_7 with my_dissolve
    "[Name]" "{i}(And astonishing!){/i}"
    show sc i_Lucy_1_8 with my_dissolve
    show sc i_Lucy_1_9 with my_dissolve
    "[Name]" "{i}(Oh yes...){/i}"
    "[Name]" "{i}(Show me dat ass!){/i}"
    show sc i_Lucy_1_10 with my_dissolve
    show sc i_Lucy_1_11 with my_dissolve
    "[Name]" "{i}(She looks perfect.){/i}"
    show sc i_Lucy_1_12 with my_dissolve
    show sc i_Lucy_1_13 with my_dissolve
    "[Name]" "{i}(Just like that, baby!){/i}"
    show sc i_Lucy_1_14 with my_dissolve
    "[Name]" "{i}(Let me have a good look.){/i}"
    "[Name]" "{i}(Now, let me see your pretty face again.){/i}"
    return

label Lucy_2_label:
    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface
    show sc i_Lucy_2_1 with my_dissolve
    "[Name]" "{i}(When she looks at me like this I feel like I'm the only man in the world.){/i}"
    "[Name]" "{i}(I wonder if they train them to look at men like that...){/i}"
    show sc i_Lucy_2_1_2 with my_dissolve
    "[Name]" "{i}(Each time she leans towards me I feel warmth...){/i}"
    "[Name]" "{i}(I think I've earned her attention. It looks like she's coming to me...){/i}"
    show sc i_Lucy_2_2 with my_dissolve
    "Lucy" "Hi there, handsome!"
    "[Name]" "{i}(Yeah, They definately know how to work with a client.){/i}"
    "[Name]" "Hey."
    show sc i_Lucy_2_3 with my_dissolve
    "Lucy" "You look like you know how to have some fun."
    "Lucy" "But I see in your eyes, that you think too much."
    "Lucy" "Enjoy the view, Alright? Don't think too much. Alright?"
    "[Name]" "Alright."
    show sc i_Lucy_2_4 with my_dissolve
    "[Name]" "{i}(Wow...){/i}"
    "[Name]" "{i}(She moves so natural...){/i}"
    "[Name]" "{i}(Are there people borned with natural talent to striptease?){/i}"
    show sc i_Lucy_2_5 with my_dissolve
    "[Name]" "{i}(If so, she's surely one of them...){/i}"
    "[Name]" "..."
    "Lucy" "Hey..."
    show sc i_Lucy_2_6 with my_dissolve
    "[Name]" "Yes?"
    "Lucy" "What's you name. handsome?"
    "[Name]" "Call me [Name]."
    show sc i_Lucy_2_7 with my_dissolve
    "Lucy" "I love how it sounds!"
    "Lucy" "I knew I'd like you."
    "[Name]" "How so?"
    show sc i_Lucy_2_8 with my_dissolve
    "Lucy" "You make me trembple when I llok at you."
    "Lucy" "I wonder what I'd feel when you touch me..."
    "[Name]" "We can test this."
    show sc i_Lucy_2_9 with my_dissolve
    "Lucy" "I'd love that."
    "Lucy" "But we can't do this right here."
    "[Name]" "I see what you're talking about..."
    menu:
        "VIP lounge":
            show sc i_Lucy_2_10 with my_dissolve
            "[Name]" "Let's take this conversation to the VIP lounge."
            "Lucy" "Oh, mon cher! I'm all yours."
            "[Name]" "Take me there, baby,"
            "Lucy" "You have to talk to Adele about booking me for VIP lounge, babe."
            "Lucy" "I'll be waiting for you!"
        "Not tonight":
            show sc i_Lucy_2_12 with my_dissolve
            "[Name]" "I think I'll pass, baby."
            "[Name]" "I'll try your french buns next time."
            show sc i_Lucy_2_13 with my_dissolve
            "Lucy" "Pfft. Your choice..."
            "Lucy" "But you have no idea what you're missing."
            show sc i_Lucy_2_14 with my_dissolve
            "[Name]" "{i}(That's okay, I'll have time to catch up.){/i}"

    return


























label vip_lucy_1_label:



    show sc i_VIP_Lucy_1_1 with my_dissolve
    "[Name]" "{i}(I adore how Lucy moves on the pole.){/i}"
    show sc i_VIP_Lucy_1_2 with my_dissolve
    "[Name]" "{i}(But I hope there's something more on the menu.){/i}"
    show sc i_VIP_Lucy_1_3 with my_dissolve
    "[Name]" "{i}(Wow... What a move...){/i}"
    "[Name]" "{i}(She's so sexy!){/i}"
    show sc i_VIP_Lucy_1_4 with my_dissolve
    "[Name]" "{i}(Oh yes, that look again. Like I'm the only man in the world.){/i}"
    "[Name]" "{i}(And those little breasts... Breathtaking.){/i}"
    show sc i_VIP_Lucy_1_5 with my_dissolve
    "[Name]" "{i}(Just like that.){/i}"
    show sc i_VIP_Lucy_1_6 with my_dissolve
    "[Name]" "{i}(She likes to touch her nipples.){/i}"
    "[Name]" "{i}(I can sence how turned on she get's each time she touches it.){/i}"
    show sc i_VIP_Lucy_1_7 with my_dissolve
    show sc i_VIP_Lucy_1_8 with my_dissolve
    "[Name]" "{i}(She's gonna take those off.){/i}"
    "[Name]" "{i}(It's about time!){/i}"
    show sc i_VIP_Lucy_1_9 with my_dissolve
    "[Name]" "{i}(Oh là là!){/i}"
    show sc i_VIP_Lucy_1_10 with my_dissolve
    show sc i_VIP_Lucy_1_11 with my_dissolve
    "[Name]" "Hello again,"
    show sc i_VIP_Lucy_1_12 with my_dissolve
    "Lucy" "Do you like the show, baby?"
    "[Name]" "I'm not sure."
    "[Name]" "Is it all you've got?"
    show sc i_VIP_Lucy_1_13 with my_dissolve
    "[Name]" "{i}(Let's see how nice this place is to VIP customers.){/i}"
    "Lucy" "No, silly! It was just the warm-up."
    "[Name]" "Was it?"
    show sc i_VIP_Lucy_1_14 with my_dissolve
    "Lucy" "Sure!"
    "Lucy" "I am here to make sure you're pleased."
    "Lucy" "Just relax and enjoy it."
    show sc i_VIP_Lucy_1_15 with my_dissolve
    "[Name]" "{i}(She seems to be ready to take things to another level,){/i}"
    "[Name]" "{i}(I like this attitude.){/i}"
    "Lucy" "Now we're going to have some fun."
    show sc i_VIP_Lucy_1_16 with my_dissolve
    "Lucy" "Are you ready?"
    menu:
        "Stop it":
            "[Name]" "Stop."
            show sc i_VIP_Lucy_1_17 with my_dissolve
            "[Name]" "I don't really wanna do this."
            show sc i_VIP_Lucy_1_18 with my_dissolve
            "Lucy" "Why?"
            "Lucy" "Is something wrong. honey?"
            show sc i_VIP_Lucy_1_17 with my_dissolve
            "[Name]" "It's not your fault. Get back to dacing, baby."
            "Lucy" "As you wish."
        "Go on, baby":
            "[Name]" "Go on, baby."
            show sc i_VIP_Lucy_1_19 with my_dissolve
            "Lucy" "That's what I wanted to hear!"
            "Lucy" "Let's see what you've got here!"
            show sc i_VIP_Lucy_1_20 with my_dissolve
            "Lucy," "Oh my, what a massive toy you have."
            "Lucy" "I haven't played with things like THAT in a while..."
            "Lucy" "That's gonna be fun!"
            show sc i_VIP_Lucy_1_21 with my_dissolve
            "[Name]" "{i}(Oh wow... Her hands are so soft.){/i}"
            "[Name]" "{i}(The way she uses them.){/i}"
            "[Name]" "{i}(She knows what to do.){/i}"
            "Lucy" "Do you like it?"
            "[Name]" "Oh yes..."
            show sc i_VIP_Lucy_1_anim_1_a with my_dissolve
            "[Name]" "Good girl."
            "[Name]" "Go on."
            show sc i_VIP_Lucy_1_anim_1 with my_dissolve
            "Lucy" "It's so big and tense."
            "Lucy" "Just lean back and relax."
            "Lucy" "Let me relieve your stress."
            show sc i_VIP_Lucy_1_anim_2 with my_dissolve
            "[Name]" "{i}(I can't believe what she can do with just her hands...){/i}"
            "[Name]" "{i}(None of my exes could do that...){/i}"
            "[Name]" "{i}(What european technique is that?){/i}"
            show sc i_VIP_Lucy_1_anim_3 with my_dissolve
            "Lucy" "Can you feel the stress receding?"
            "[Name]" "Oh yeah...."
            show sc i_VIP_Lucy_1_anim_4_a with my_dissolve
            "[Name]" "{i}(What is she doing?){/i}"
            "[Name]" "{i}(Her nipples are gently touching my dick..){/i}"
            show sc i_VIP_Lucy_1_anim_4 with my_dissolve
            "Lucy" "Your cock is throbbing so nicely..."
            "Lucy" "And I have very sensitive nipples."
            show sc i_VIP_Lucy_1_anim_5 with my_dissolve
            "Lucy" "I couldn't help myself..."
            "[Name]" "It's okay... I like the feeling."
            "Lucy" "Me too...  Ah..."
            show sc i_VIP_Lucy_1_anim_6 with my_dissolve
            "[Name]" "{i}(It feels too good...){/i}"
            "[Name]" "{i}(I don't know how long I can hold on...){/i}"
            show sc i_VIP_Lucy_1_22 with my_dissolve
            "[Name]" "I think I'm about to cum."
            "Lucy" "Then pour your seed all over me!"
            show sc i_VIP_Lucy_1_23 with my_dissolve
            "[Name]" "Ohh!"
            "[Name]" "..."
            show sc i_VIP_Lucy_1_24 with my_dissolve
            "Lucy" "Unbelievable!"
            "Lucy" "Ha-ha-ha!"
            show sc i_VIP_Lucy_1_25 with my_dissolve
            "[Name]" "It's not over yet!"
            "Lucy" "Oh!"
            show sc i_VIP_Lucy_1_26 with my_dissolve
            "Lucy" "Where do you keep that much?"
            "[Name]" "He-he-he."
            show sc i_VIP_Lucy_1_27 with my_dissolve
            "[Name]" "What can I say,,,,"
            "Lucy" "Oh wow! It's still pulsating."
            "Lucy" "You have so much energy, [Name]!"
            show sc i_VIP_Lucy_1_28 with my_dissolve
            "Lucy" "Mhm-mhm..."
            "Lucy" "Tastes good."
            "Lucy" "I'm looking forward to having some more fun time with you."
            "[Name]" "Me too..."
    
    $ p_up('Lucy', 1)
    $ change_location_2(location_now, time_now+1, sleep = True)
    return



label vip_sadira_1_label:
    if getattr(store, 'sadira_girl', True):
        show sc i_VIP_Sadira_1_1 with my_dissolve
        "[Name]" "{i}(The beautiful Sadira strikes again with her movements at the pole.){/i}"
        show sc i_VIP_Sadira_1_2 with my_dissolve
        show sc i_VIP_Sadira_1_3 with my_dissolve
        "[Name]" "{i}(And her lingerie is maddening.){/i}"
        "[Name]" "{i}(But I'd like to see underneath...){/i}"
        show sc i_VIP_Sadira_1_4 with my_dissolve
        show sc i_VIP_Sadira_1_5 with my_dissolve
        "[Name]" "{i}(Oh, yes! What gorgeous boobs!){/i}"
        show sc i_VIP_Sadira_1_6 with my_dissolve
        "[Name]" "{i}(They're just the perfect shape.){/i}"
        show sc i_VIP_Sadira_1_7 with my_dissolve
        show sc i_VIP_Sadira_1_8 with my_dissolve
        "[Name]" "{i}(She was so clever with her panties in the dance...){/i}"
        "[Name]" "Bravo!"
        show sc i_VIP_Sadira_1_9 with my_dissolve
        "[Name]" "{i}(I think I got her attention!){/i}"
        "[Name]" "(She's coming to me.)"
        show sc i_VIP_Sadira_1_10 with my_dissolve
        show sc i_VIP_Sadira_1_11 with my_dissolve
        show sc i_VIP_Sadira_1_12 with my_dissolve
        "Sadira" "Are you ready now?"
        "[Name]" "For what?"
        "Sadira" "To get what you deserve..."
        "[Name]" "What's that? {w} Woah..."
        show sc i_VIP_Sadira_1_13 with my_dissolve
        "Sadira" "Do you mind if I sit here?"
        "[Name]" "Not at all..."
        show sc i_VIP_Sadira_1_14 with my_dissolve
        "Sadira" "You've been a good boy."
        "Sadira" "And earned a treat,"
        "[Name]" "What's that?"
        show sc i_VIP_Sadira_1_15 with my_dissolve
        "Sadira" "A night full of pleasure."
        "[Name]" "І'm intrigued."
        show sc i_VIP_Sadira_1_16 with my_dissolve
        "[Name]" "What do I have to do?"
        "Sadira" 'You just have to say "yes", baby.'
        show sc i_VIP_Sadira_1_17 with my_dissolve
        menu:
            "No":
                "[Name]" "Well in that case..."
                show sc i_VIP_Sadira_1_18 with my_dissolve
                "[Name]" 'Ill have to say "No" this time.'
                "Sadira" "But... Why?"
                "[Name]" "I'm not in the mood, sorry,"
                show sc i_VIP_Sadira_1_19 with my_dissolve
                "Sadira" "It's your loss."
                "Sadira" "We still have time, so I'll get back to dancing."
                show sc i_VIP_Sadira_1_20 with my_dissolve
                "[Name]" "{i}(She definitely got the moves...){/i}"
                "[Name]" "{i}(Maybe next time I'll try her other services.){/i}"
                #return
            "Yes":
                show sc i_VIP_Sadira_1_17 with my_dissolve
                "[Name]" "Yes..."
                show sc i_VIP_Sadira_1_21 with my_dissolve
                "Sadira" "One look at your cock makes me tremble."
                "Sadira" "I'm all wet aready."
                show sc i_VIP_Sadira_1_anim_1_a with my_dissolve
                "Sadira" "Are you ready, darling?"
                "[Name]" "Show me what you've got."
                show sc i_VIP_Sadira_1_anim_1 with my_dissolve
                "Sadira" "That's just the beginning."
                "Sadira" "But it drove a lot of men crazy, too."
                "[Name]" "I'm not that easy to impress."
                "Sadira" "We'll see."
                show sc i_VIP_Sadira_1_anim_2 with my_dissolve
                "Sadira" "[Name], I must say..."
                "Sadira" "You have an incredible cock."
                "Sadira" "You can feel the power in it..."
                "Sadira" "It makes me want to sit on you..."
                show sc i_VIP_Sadira_1_anim_3 with my_dissolve
                "[Name]" "So what are you waiting for?"
                "Sadira" "You're right, this is much better."
                show sc i_VIP_Sadira_1_anim_4_a with my_dissolve
                "[Name]" "I thought you were gonna sit on my dick...."
                "Sadira" "Oh... It's not time yet, baby."
                show sc i_VIP_Sadira_1_anim_4 with my_dissolve
                "Sadira" "Sex is just the tip of the iceberg."
                "Sadira" "We enjoy each other completely... Ahh..."
                "Sadira" "With every inch of our bodies."
                "Sadira" "And only then - sex!"
                show sc i_VIP_Sadira_1_anim_5 with my_dissolve
                "[Name]" "I confess, it's incredibly satisfying..."
                "Sadira" "This is what I wanted to hear."
                "Sadira" "But this night was only the first of my many tales."
                show sc i_VIP_Sadira_1_anim_6 with my_dissolve
                "[Name]" "Then I want to enjoy them all..."
                "Sadira" "All in good time."
                show sc i_VIP_Sadira_1_22 with my_dissolve
                "[Name]" "Oh yes, just like that,"
                "[Name]" "I'm going to cum..."
                show sc i_VIP_Sadira_1_23 with my_dissolve
                "Sadira" "Me too..."
                "Sadira" "Oh yes! "
                show sc i_VIP_Sadira_1_24 with my_dissolve
                "Sadira" "Shower me with your cum!"
                "Sadira" "Give it all to me!"
                show sc i_VIP_Sadira_1_25 with my_dissolve
                "Sadira" "Yes! That's it!"
                "[Name]" "Oh yes!"
                show sc i_VIP_Sadira_1_26 with my_dissolve
                "Sadira" "Ah...Yes, more!"
                "Sadira" "You came so much..."
                show sc i_VIP_Sadira_1_27 with my_dissolve
                "Sadira" "We can't waste your precious liquids."
                "[Name]" "What else whould you use it for..."
                "Sadira" "Mmm... That's what I like."
                show sc i_VIP_Sadira_1_28 with my_dissolve
                "[Name]" "{i}(What a slut...){/i}"
                "[Name]" "Thanks..."
                "Sadira" "C'ya around, honey,"
    else:
        show sc i_VIP_Sadira_T_1_1 with my_dissolve
        "[Name]" "{i}(The beautiful Sadira strikes again with her movements at the pole.){/i}"
        show sc i_VIP_Sadira_1_2 with my_dissolve
        show sc i_VIP_Sadira_T_1_2 with my_dissolve
        show sc i_VIP_Sadira_T_1_3 with my_dissolve
        "[Name]" "{i}(And her lingerie is maddening.){/i}"
        "[Name]" "{i}(But I'd like to see underneath...){/i}"
        show sc i_VIP_Sadira_1_4 with my_dissolve
        show sc i_VIP_Sadira_T_1_5 with my_dissolve
        "[Name]" "{i}(Oh, yes! What gorgeous boobs!){/i}"
        show sc i_VIP_Sadira_1_6 with my_dissolve
        "[Name]" "{i}(They're just the perfect shape.){/i}"
        show sc i_VIP_Sadira_T_1_6 with my_dissolve
        show sc i_VIP_Sadira_T_1_7 with my_dissolve
        "[Name]" "{i}(She was so clever with her panties in the dance...){/i}"
        show sc i_VIP_Sadira_T_1_8 with my_dissolve
        "[Name]" "Bravo!"
        show sc i_VIP_Sadira_T_1_9 with my_dissolve
        "[Name]" "{i}(I think I got her attention!){/i}"
        show sc i_VIP_Sadira_1_10 with my_dissolve
        show sc i_VIP_Sadira_1_11 with my_dissolve
        show sc i_VIP_Sadira_T_1_10 with my_dissolve
        "Sadira" "Do you like to watch me dance, sweety?"
        "Sadira" "Do you like what you see?"
        show sc i_VIP_Sadira_T_1_11 with my_dissolve
        "[Name]" "Oh yes."
        "Sadira" "Tell me, how much do you like it,"
        show sc i_VIP_Sadira_T_1_12 with my_dissolve
        "[Name]" "You're a dream come true, baby. What else can I say?"
        "Sadira" "Tell me that I'm beautiful."
        show sc i_VIP_Sadira_T_1_13 with my_dissolve
        "[Name]" "{i}(Oh wow... She's so close to me.){/i}"
        "[Name]" "You're beautiful. It's true."
        show sc i_VIP_Sadira_T_1_14 with my_dissolve
        "Sadira" "I'm so happy to hear it..."
        "Sadira" "I can barely restrain myself."
        show sc i_VIP_Sadira_T_1_15 with my_dissolve
        "Sadira" "Just one word, and we'll start the fun."
        "Sadira" "Do you want to have a night of your life?"
        menu:
            "No":
                $ pass
                "[Name]" "Well... No."
                show sc i_VIP_Sadira_1_18 with my_dissolve
                "[Name]" "Not now, that's for sure."
                "Sadira" "What a waste of time..."
                show sc i_VIP_Sadira_1_19 with my_dissolve
                "[Name]" "Don't get mad, baby. I'm just not in the mood."
                "[Name]" "Get back to dancing."
                show sc i_VIP_Sadira_T_1_16 with my_dissolve
                "[Name]" "{i}(She definitely got the moves...){/i}"
                "[Name]" "{i}(Maybe next time I'll try her other services.){/i}"
            "Yes":
                $ pass
                show sc i_VIP_Sadira_T_1_15 with my_dissolve
                "[Name]" "Yes!"
                "Sadira" "Then you came to the right person."
                "[Name]" "I hope you're right."
                "[Name]" "You have a nice tool."
                "Sadira" "Thank you, baby."
                "Sadira" "But I'm much more interested in yours."
                show sc i_VIP_Sadira_T_1_anim_1_a with my_dissolve
                "Sadira" "Just like that."
                "[Name]" "{i}(She's got a nice touch.){/i}"
                show sc i_VIP_Sadira_T_1_anim_1 with my_dissolve
                "Sadira" "[Name], I must say..."
                "Sadira" "You have an incredible cock."
                "Sadira" "I love how it feels in my hands."
                "[Name]" "Thank you."
                show sc i_VIP_Sadira_T_1_anim_2 with my_dissolve
                "Sadira" "It's so hot..."
                "Sadira" "You can feel the power in it..."
                "Sadira" "I'm jealous."
                show sc i_VIP_Sadira_T_1_anim_3 with my_dissolve
                "[Name]" "How does your dick feel in hand?"
                "Sadira" "Try it yourself, baby."
                "[Name]" "Alright."
                show sc i_VIP_Sadira_T_1_anim_4_a with my_dissolve
                "Sadira" "Oh yes... I can feel your grasp, [Name]."
                "[Name]" "I can feel your touch too."
                show sc i_VIP_Sadira_T_1_anim_4 with my_dissolve
                "Sadira" "Stroke it at the time I stroke yours..."
                "[Name]" "Like this?"
                "Sadira" "Oh yes..."
                "Sadira" "Keep going, baby."
                show sc i_VIP_Sadira_T_1_anim_5 with my_dissolve
                "[Name]" "You too."
                "[Name]" "(I've never felt anything like this...)"
                "Sadira" "Yes, yes... Do you feel it?"
                "[Name]" "What?"
                show sc i_VIP_Sadira_T_1_anim_6 with my_dissolve
                "Sadira" "The exctasy..."
                "[Name]" "Oh yes..."
                show sc i_VIP_Sadira_T_1_17 with my_dissolve
                "[Name]" "I can't wait any longer."
                "[Name]" "I'm going to cum!"
                show sc i_VIP_Sadira_T_1_18 with my_dissolve
                "Sadira" "Look me in the eyes."
                "Sadira" "Yes! Yes! Yes!"
                show sc i_VIP_Sadira_T_1_19 with my_dissolve
                "Sadira" "That's what I like!"
                "Sadira" "Oh yes!"
                show sc i_VIP_Sadira_T_1_20 with my_dissolve
                "Sadira" "I'm cuming too!"
                "Sadira" "Ah...Yes...."
                show sc i_VIP_Sadira_T_1_21 with my_dissolve
                "Sadira" "There's only one problem."
                "[Name]" "What?"
                show sc i_VIP_Sadira_1_27 with my_dissolve
                "Sadira" "You came so much..."
                "[Name]" "He-he."
                "Sadira" "We can't waste your precious liquids."
                show sc i_VIP_Sadira_1_28 with my_dissolve
                "Sadira" "Mmm... That's what I like."
                "[Name]" "{i}(What a slut...){/i}"
                "[Name]" "Thanks..."
                "Sadira" "C'ya around, honey,"

    $ p_up('Sadira', 1)
    $ change_location_2(location_now, time_now+1, sleep = True)
    return
