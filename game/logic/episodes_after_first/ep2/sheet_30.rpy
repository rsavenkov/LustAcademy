screen end_demo_screen:
    imagebutton idle '#0000' hover '#0000' action Return()

    viewport:
        xmaximum 290
        ymaximum 100
        xpos 660
        ypos 770

        imagebutton:
            idle '#0000'
            hover '#0000'
            action OpenURL('https://www.patreon.com/bearinthenight')

    viewport:
        xmaximum 290
        ymaximum 100
        xpos 970
        ypos 770

        imagebutton:
            idle '#0000'
            hover '#0000'
            action OpenURL('https://discord.gg/FgFp9NeKsz')




label sheet_30:
    scene sc i_1_276 with Dissolve(2)
    "[Name]" "{i}(Wow! So this is our dorm?){/i}"
    show sc i_1_276 with my_dissolve
    "[Name]" "{i}(Looks much more modern than I expected.){/i}"
    show sc i_1_277 with my_dissolve
    "Elijah" "Welcome to Leonheart, kids! "
    "Elijah" "Best conditions for best students!"
    "Elijah" "Make room!"
    "Elijah" "Choose any free room for yourself. This is your home now!"
    "Elijah" "But the main place in our house is this living room. Here..."
    "Elijah" "...is where real magic happens!"
    "Elijah" "Parties, get-togethers, live communication..."
    "Elijah" "Celebrating house victories in tournaments and competitions, orgies..."
    "Elijah" "Well, there haven't really been any orgies yet, but hey!"
    "Elijah" "You are new blood. Pioneers. I believe in you."
    "Elijah" "Just let me know in advance so that I can clear my plans for the day."
    show sc i_1_278 with my_dissolve
    "Elijah" "So. What have I forgotten... Oh yes. Do any of you have questions for me?"
    $ sheet_30_var_1 = 0
    $ sheet_30_var_2 = 0
    $ sheet_30_var_3 = 0

label sheet_30_menu:
    if all([sheet_30_var_1, sheet_30_var_2, sheet_30_var_3]):
        jump end_sheet_30
    scene sc i_1_278 with Dissolve(.5)
    menu:
        "Ask about the parties" if not sheet_30_var_1:
            $ sheet_30_var_1 = 1

        "Ask about the schedule" if not sheet_30_var_2:
            $ sheet_30_var_2 = 1
            jump sheet_30_menu_answ_2
        "Ask about competitions" if not sheet_30_var_3:
            $ sheet_30_var_3 = 1
            jump sheet_30_menu_answ_3

    "[Name]" "I don't see a bar here, how can we party without booze?"
    show sc i_1_279 with my_dissolve
    "Elijah" "The booze is all right here, trust me! We have our own sources."
    "Elijah" "You just have to live long enough to see our parties!"
    show sc i_1_279_2 with my_dissolve
    "Elijah" "And after that, you can die in peace!"
    jump sheet_30_menu

label sheet_30_menu_answ_2:

    "[Name]" "When is the best time to go to bed? "
    show sc i_1_278 with my_dissolve
    "[Name]" "What time do classes begin?"
    show sc i_1_280 with my_dissolve
    "Elijah" "Good question! Boring, but really important information:"
    "Elijah" "Your schedule and all news are sent directly to your mobile phone."
    show sc i_1_279_2 with my_dissolve
    "[Name]" "How does that work?"
    "Elijah" "If you want to make something of yourself here — you will attend classes."
    "Elijah" "And if you want to fail your training and get expelled — it's up to you."
    show sc i_1_281 with my_dissolve
    "Elijah" "I advise everyone to go to bed early and get a good night's sleep."
    "Elijah" "The magical energy that charged you up on the train is about to run out..."
    "Elijah" "...and no one likes to drag students... "
    "Elijah" "...who have passed out in the middle of the room to their bedrooms."
    jump sheet_30_menu
label sheet_30_menu_answ_3:

    "[Name]" "What victories were you talking about? "
    "[Name]" "Who is our house competing with?"
    show sc i_1_282 with my_dissolve
    "Elijah" "Great question! With other houses, of course!"
    "Elijah" "The best house in Cordale is selected each week."
    "Elijah" "It depends on how fun and rowdy you spend your weekend."
    "Elijah" "You are probably impressed by the academy, but! "
    "Elijah" "Only ghosts like to hang around these walls for a whole year."
    "Elijah" "And that's not a fact. I don't think they have a choice. But we do!"
    "Elijah" "Collect the most points — have fun in Dale!"
    "Elijah" "It's not saying much but trust me — it's worth being ready for class!"
    jump sheet_30_menu
label end_sheet_30:
    show sc i_1_279_2 with my_dissolve
    "Elijah" "Thank you all for your attention! Rest now, you were all great today."
    show sc i_1_283 with my_dissolve
    "Elijah" "[Name], I see you are an active guy. "
    show sc i_1_284 with my_dissolve
    "Elijah" "Come to the living room in the morning before class!"
    "Elijah" "I have some business for you."
    "[Name]" "Okay, of course."
    "Elijah" "Sweet! C'ya!"
    show sc i_1_284_2 with my_dissolve
    "[Name]" "{i}(This guy seems great.){/i}"
    "[Name]" "{i}(I hope my gut isn't lying about him.){/i}"
    "[Name]" "{i}(Alright. Where's my room?){/i}"
    "[Name]" "{i}(I just have to...){/i}"

    play sound 'audio/new/gameplay/phone_calling2.mp3'

    "[Name]" "..."
    jump sheet_31

label sheet_30_end:
    show sc i_1_284_3 with my_dissolve
    "[Name]" "{i}(Sam?){/i}"

    stop music_2 fadeout 1.0 
    play music 'audio/new/sounds/Mistery_Forest_music.mp3' fadein 1.0


    scene end_video
    show screen end_demo_screen
    with Dissolve(1.5)
    $ renpy.pause(999999999999999)

    scene expression '#000' with Dissolve(.5)

    stop music fadeout 1.0

    $ renpy.pause(1, hard = True)
    $ renpy.full_restart()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
