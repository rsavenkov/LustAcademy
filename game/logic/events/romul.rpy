label romul_dale_clubenter_label:
label romul_events_3_label:
    
    hide screen main_interface
    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    show screen black_tmp_screen_menu
    with Dissolve(.5)

    menu:
        "0 Enter the Club" if not hasattr(store, 'Q_Romul'):
            call romul_1_label from _call_romul_1_label
            scene image '#000' with Dissolve(.5)
            call romul_2_label from _call_romul_2_label
            $ Q_Romul = 2
            $ p_up('Romul', 1)
        "2 Enter the Club" if hasattr(store, 'Q_Romul') and Q_Romul == 2:
            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu
            $ change_location_2('dale_club', time_now)
            with Dissolve(.5)
            jump main_interface_label
            
        "Not now":
            show screen show_hide_locations_2
            show screen main_interface 
            hide screen black_tmp_screen_menu

            with Dissolve(.5)
            jump main_interface_label


    hide screen black_tmp_screen_menu


    jump main_interface_label
label romul_1_label:
    "[Name]" '{i}(It seems not everyone is welcomed here.){/i}'
    show sc i_Romul_1_1 with my_dissolve
    "Romul" "Are you in a hurry, young man?"
    "[Name]" "Just exploring the neighborhood."
    "[Name]" "Thought about checking out the club."
    show sc i_Romul_1_2 with my_dissolve
    "Romul" "Go get another walk under the fresh air, little man."
    "Romul" "You're not going in."
    "[Name]" "Why not?!"
    show sc i_Romul_1_3 with my_dissolve
    "Romul" "You don't meet the standards."
    "[Name]" "What standards?!"
    "Romul" "My personal standards."
    "Romul" "I don't like your face."
    show sc i_Romul_1_4 with my_dissolve
    "[Name]" '{i}(What the hell?!){/i}'
    "[Name]" '{i}(You need to control yourself.){/i}'
    "[Name]" "{i}(I don't think anyone at the academy would approve of beating up a club security guard.){/i}"
    show sc i_Romul_1_5 with my_dissolve
    "Romul" "Hmmm... Maybe I overreacted."
    "Romul" "Maybe you don't suck and you should be allowed in the club."
    "[Name]" "{i}(I see where he's going with this...){/i}"
    show sc i_Romul_1_6 with my_dissolve
    "Romul" "I can't decide..."
    "Romul" "On the one hand, you don't meet my standards."
    show sc i_Romul_1_7 with my_dissolve
    "Romul" "On the other, I believe in capitalism and second chances!"
    show sc i_Romul_1_19 with my_dissolve
    "Romul" "Maybe something can help tip the scales of my decision on your side..."
    "[Name]" "How much?"
    "Romul" "$50"
    "[Name]" '{i}(Holy fuck... That much? He has not hesitated at all before saying that.){/i}'
    scene sc i_Romul_1_7 with Dissolve(.5)
label romul_1_label_menu_bribe:
    menu:
        "!Bribe ($50)" if money < 50:
            $ pass
        "Bribe ($50)" if money >= 50:
            $ pass
            if money < 50:
                jump romul_1_label_menu_bribe
            $ money -= 50
            show sc i_Romul_1_8 with my_dissolve
            "[Name]" "The hell with you, Nimesis."
            "Romul" "What does that eveb mean?"
            "[Name]" "Don't try to think too hard, it's not good for you."
            "[Name]" "Can I go in?"
            show sc i_Romul_1_9 with my_dissolve
            "Romul" "Go before I change my mind."
            "Romul" "You know..."
            show sc i_Romul_1_20 with my_dissolve
            "Romul" "I've changed my mind."
            "[Name]" "What the hell, man?"
            "Romul" "I'm not in the mood for some punk-ass jokes today."
            "[Name]" "I paid you!"
            show sc i_Romul_1_21 with my_dissolve
            "Romul" "For advice!"
            "Romul" "You want to get in? Be polite, pay quietly and smile."
            "Romul" "And for Merlin's sake, put some decent clothes on!"
            "Romul" "That's it, get out."
            show sc i_Romul_1_22 with my_dissolve
            "Romul" "Or do you want to do it another way?!"
        "Walk away.":
            $ pass
    show sc i_Romul_1_10 with my_dissolve
    "[Name]" "It's not worth it."
    "[Name]" "Ciao."
    "Romul" "Get out of here, sucker."
    show sc i_Romul_1_11 with my_dissolve
    "[Name]" '{i}(I really want to try the combta bolt on him...){/i}'
    "[Name]" "{i}(Shit, I don't think I'm going to the club tonight.){/i}"
    show sc i_Romul_1_12 with my_dissolve
    "[Name]" "(Hmm, what a strange man.)"
    "[Name]" '{i}(I wonder what the boogeyman at the door will tell him.){/i}'
    "[Name]" "{i}(I can't contain my curiosity...){/i}"
    "[Name]" '{i}(Need to eavesdrop!){/i}'
    show sc i_Romul_1_13 with my_dissolve
    "Romul" "Sorry, man, your VIP isn't helping here."
    "Romul" "The girls complained, so you're banneded from entering forever."
    show sc i_Romul_1_14 with my_dissolve
    "Unknown Man" "I don't need to go in."
    "Unknown Man" "Here's the..."
    show sc i_Romul_1_15 with my_dissolve
    "Romul" "Whoa! There's..."
    "Romul" "It's got..."
    show sc i_Romul_1_16 with my_dissolve
    "Unknown Man" "Shh! It's all yours."
    "Unknown Man" "Just pretend tonight that you didn't hear anything."
    "Unknown Man" "And you didn't see anybody."
    show sc i_Romul_1_17 with my_dissolve
    "[Name]" "{i}(Something ain't right here.){/i}"
    "[Name]" "{i}(How could that moron agree to this?){/i}"
    show sc i_Romul_1_18 with my_dissolve
    "[Name]" "{i}(Wait a minute, that guy wasn't even going to the club...){/i}"
    "[Name]" "{i}(That's very strange... I should follow him.){/i}"
    #show sc i_Romul_1_18 with my_dissolve
    "[Name]" "{i}(I'm always getting into trouble...){/i}"
    "[Name]" "{i}(But I can't just leave it at that, can I?){/i}"
    return

label romul_2_label:
    scene sc i_Romul_2_1 with Dissolve(.5)
    "[Name]" "{i}(Hmm, this looks like a service exit from a nightclub.){/i}"
    show sc i_Romul_2_2 with my_dissolve
    "[Name]" "{i}(But why is he hanging around if he paid the security guard?){/i}"
    show sc i_Romul_2_3 with my_dissolve
    "[Name]" "{i}(The entrance clearly costs less than a whole envelope of dough...){/i}"
    show sc i_Romul_2_4 with my_dissolve
    "[Name]" "{i}(It seems someone is opening the door from the inside...){/i}"
    "[Name]" "{i}(Is he hiding?){/i}"
    "[Name]" "{i}(What's he up to?){/i}"
    show sc i_Romul_2_5 with my_dissolve
    "[Name]" "{i}(Someone comes out. A girl.){/i}"
    "[Name]" "{i}(Was he waiting for her?){/i}"
    show sc i_Romul_2_6 with my_dissolve
    "Unknown Man" "Adele!"
    show sc i_Romul_2_7 with my_dissolve
    "Adele" "Diego?"
    show sc i_Romul_2_8 with my_dissolve
    "Adele" "What are you doing here?"
    "Diego" "Adele, please, give me a chance to explain..."
    show sc i_Romul_2_9 with my_dissolve
    "Adele" "You're not allowed to come within 100 meters of me."
    "Adele" "Go away or you'll go to jail!"
    "Diego" "Adele, I can't forget you."
    "Diego" "You opened my eyes."
    "Adele" "I've heard that before. I'm leaving."
    show sc i_Romul_2_10 with my_dissolve
    "Diego" "Wait! I want you all to myself."
    "Adele" "Get your hands off me and get out of here!"
    show sc i_Romul_2_11 with my_dissolve
    "Diego" "Wait, baby, feel the heat of my love..."
    "Adele" "Let go! Asshole!"
    "Diego" "Don't fight it, you liked it then..."
    show sc i_Romul_2_12 with my_dissolve
    "Adele" "HELP!"
    "[Name]" "{i}(Shit, is he going to rape her?){/i}"
    "[Name]" "{i}(What should I do?){/i}"
    show sc i_Romul_2_12 with my_dissolve
    menu:
        "Do Nothing":
            $ romul_do_nothing = True
            show sc i_Romul_2_13 with my_dissolve
            "[Name]" "{i}(We'll see what happens next.){/i}"
            "[Name]" "{i}(I always have time to intervene.){/i}"
            "Diego" "Remember how you moaned?"
            show sc i_Romul_2_14 with my_dissolve
            "Adele" "Let go, asshole! That was work."
            "Diego" "You mean you were leaking like a bitch for money?!"
            show sc i_Romul_2_15 with my_dissolve
            "Adele" "YOU DISGUST ME AS A MAN!"
            "Adele" "YOU PATHETIC IMPOTENT!"
            show sc i_Romul_2_16 with my_dissolve
            "Diego" "You bitch!"
            show sc i_Romul_2_17 with my_dissolve
            "Adele" "Argh..."
            "Diego" "It's okay, I'm gonna make you pay!"
            "Diego" "You'll take it back..."
            show sc i_Romul_2_18 with my_dissolve
            "Adele" "No...."
            "Adele" "Argh..."
            show sc i_Romul_2_19 with my_dissolve
            "Diego" "Just relax and try to enjoy it!"
            "Adele" "I'VE SAID...."
            show sc i_Romul_2_20 with my_dissolve
            "Adele" "Get away from me!"
            "Diego" "Ouuch...."
            show sc i_Romul_2_21 with my_dissolve
            "[Name]" "{i}(WOW! What was that?){/i}"
            "[Name]" "{i}(Ugh... That must have hurt...){/i}"
            show sc i_Romul_2_22 with my_dissolve
            "[Name]" "{i}(I think she got him. Good for her.){/i}"
            "Diego" "Ooh-ooh-ooh-ooh..."
            "Adele" "That's right!"
            "Adele" "Get out of here, you miserable short-barreled baby-boy."
            show sc i_Romul_2_23 with my_dissolve
            "[Name]" "{i}(Damn, he's running towards me.){/i}"
            "[Name]" "{i}(It's good he's too busy to look around.){/i}"
            show sc i_Romul_2_24 with my_dissolve
            "[Name]" "{i}(Where'd she go?){/i}"
            "[Name]" "{i}(Probably went back inside...){/i}"
            show sc i_Romul_2_25 with my_dissolve
            "[Name]" "{i}(Um, something fell out of his pocket...){/i}"
            "[Name]" "{i}(What is it? A {b}VIP pass?{/b}){/i}"
            show sc i_Romul_2_26 with my_dissolve
            "[Name]" "{i}(I wonder. I could use it.){/i}"
            "[Name]" "{i}(Okay, I don't want anyone to see me sneaking around the alleys.){/i}"
            scene image '#000' with Dissolve(.5)
            return
        "Help":
            $ pass
    show sc i_Romul_2_13 with my_dissolve
    "[Name]" "{i}(I can't just stand by!){/i}"
    "[Name]" "{i}(I was just about to punch someone in the face!){/i}"
    show sc i_Romul_2_27 with my_dissolve
    "[Name]" "Get your hands off her, moose!"
    "[Name]" "{i}(I haven't thought about what I'm going to do next...){/i}"
    "[Name]" "{i}(Well... I can't back out now!){/i}"
    show sc i_Romul_2_28 with my_dissolve
    "Diego" "Who the fuck are you?"
    "[Name]" "The one who's about to kick your ass."
    "Diego" "Is this a joke?"
    show sc i_Romul_2_29 with my_dissolve
    "Diego" "Say your prayers!"
    menu:
        "Block the attack":
            $ romul_block_the_attack = True
            show sc i_Romul_2_30 with my_dissolve
            "[Name]" "{i}(Fuck! He's too quick!){/i}"
            "[Name]" "Ouch..."
            show sc i_Romul_2_31 with my_dissolve
            "[Name]" "{i}(That's gonna hurt for a while...){/i}"
            "[Name]" "{i}(Damn it, [Name], think of something...){/i}"
            "Diego" "You little bastard!"
            show sc i_Romul_2_32 with my_dissolve
            "[Name]" "{i}(Man, I am screwed...){/i}"
            "Diego" "How the fuck where YOU gonna kick my ass, clown?"
            show sc i_Romul_2_33 with my_dissolve
            "Adele" "Hey, cowboy!"
            "Diego" "Huh?"
            show sc i_Romul_2_34 with my_dissolve
            "Adele" "TAKE."
            "Adele" "THAT."
            "Diego" "Ough..."
            show sc i_Romul_2_35 with my_dissolve
            "[Name]" "{i}(What the fuck just happened?){/i}"
            "Diego" "Ough..."
            "Diego" "Gnghna-a-a..."
            show sc i_Romul_2_36 with my_dissolve
            "[Name]" "{i}(What's with her hand?){/i}"
            "Diego" "You'll pay for this!"
            "Adele" "Go cry to your moma, sucker!"
            show sc i_Romul_2_37 with my_dissolve
            "Adele" "Hey, are you alright?"
            "[Name]" "I'm....me..."
            "Adele" "Can you understand me?"
            "[Name]" "Your chest...."
            show sc i_Romul_2_38 with my_dissolve
            "Adele" "Oh, that?"
            "Adele" "He-he! O-ops!"
            show sc i_Romul_2_39 with my_dissolve
            "Adele" "Sorry for that. "
            "Adele" "Why am I not surprised that was the first thing you've noticed?"
            "[Name]" "I was just being polite."
            show sc i_Romul_2_40 with my_dissolve
            "Adele" "Look who's talking like a normal person again!"
            "Adele" "Here, let's get you up."
            "[Name]" "Thank you."
        "Use magic":
            $ pass
            show sc i_Romul_2_41 with my_dissolve
            "[Name]" "You should not mess with a wizard!"
            "[Name]" "{i}(Come on, I can do this!){/i}"
            show sc i_Romul_2_42 with my_dissolve
            "[Name]" "{i}(This is it. One moment. One opportunity.){/i}"
            "[Name]" "{i}(Will I capture it...Or just let it slip?){/i}"
            "[Name]" "TAKE THIS!"
            show sc i_Romul_2_43 with my_dissolve
            "Diego" "Ouch..."
            "[Name]" "{i}(It was not enough? Oh no...){/i}"
            "Diego" "Fuck! "
            show sc i_Romul_2_44 with my_dissolve
            "Diego" "That hurts, puta!"
            "Diego" "But not as much as I'm going to hurt you!"
            "Adele" "Hey, jackass!"
            show sc i_Romul_2_45 with my_dissolve
            "Diego" "I'll get back to you in a moment, hun...."
            "Diego" "What the...."
            show sc i_Romul_2_34 with my_dissolve
            "Adele" "TAKE."
            "Adele" "THAT."
            "Diego" "Ough..."
            show sc i_Romul_2_35 with my_dissolve
            "Diego" "Gnghna-a-a..."
            "[Name]" "{i}(What's with her hand?){/i}"
            "Diego" "FUCK! That hurts..."
            show sc i_Romul_2_36 with my_dissolve
            "Diego" "You'll pay for this!"
            "Adele" "Go cry to your moma, sucker!"
            show sc i_Romul_2_46 with my_dissolve
            "Adele" "Hey... Thank's a lot!"
            "[Name]" "It's nothing, really..."
            "[Name]" "{i}(In the end she did everything herrself....){/i}"
            "Adele" "I couldn't do it without you."
            "[Name]" "{i}(Do you think it's obvious that I stare at her boobs?){/i}"
            show sc i_Romul_2_47 with my_dissolve
            "Adele" "Oops! He-he. "
            "[Name]" "Sorry, I wasn't..."
            show sc i_Romul_2_48 with my_dissolve
            "Adele" "It's alright. I work here. I'm used to that kind of attention."
            "[Name]" "What about that guy?"
            "Adele" "Long story..."
    show sc i_Romul_2_49 with my_dissolve
    "[Name]" "Are you sure you're going to be alright?"
    "Adele" "Totaly. I have  a,lot of friends inside, "
    "Adele" "They'll take care of me."
    show sc i_Romul_2_50 with my_dissolve
    "[Name]" "Despite the circumstances, it was nice to meet you, catwoman."
    "Adele" "A-ha-ha."
    show sc i_Romul_2_51 with my_dissolve
    "Adele" "Here, I want you to have this."
    "[Name]" "What's that?"
    "Adele" "It's a {b}VIP pass?{/b} for club member."
    show sc i_Romul_2_52 with my_dissolve
    "Adele" "Our bouncer can be a pain in the ass. "
    "Adele" "Show him this and he won't bother you again."
    "[Name]" "Well, thank you."
    show sc i_Romul_2_53 with my_dissolve
    "Adele" "I've gotta go, hon. Thank's again!"
    "[Name]" "No problem."
    show sc i_Romul_2_54 with my_dissolve
    "[Name]" "{i}(Hm... {b}VIP pass?{/b}){/i}"
    "[Name]" "{i}(Not bad for a failed hero.){/i}"
    show sc i_Romul_2_55 with my_dissolve
    "[Name]" "{i}(I guess there's no reason to stay in this creepy place.){/i}"
    scene image '#000' with Dissolve(.5)
    return