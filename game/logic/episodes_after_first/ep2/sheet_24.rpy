# label sheet_24:

#     stop music_2   fadeout 1.0
#     play music 'audio/new/Music/Mini_game_music.mp3' fadein 1.0



#     scene sc i_1_196_2 with Dissolve(1)
#     "Victoria" "Once you've started casting a spell..."
#     show sc i_1_196_2 with my_dissolve
# label sheet_24_repeat_rules:
#     "Victoria" "...concentrate and try to form a magic glyph."
#     show sc i_1_196_2 with my_dissolve
#     "Victoria" "Channel your magic powers into this glyph."
#     show sc i_1_196_2 with my_dissolve
#     "Victoria" "Your goal is to be as accurate as you can."
#     show sc i_1_196_2 with my_dissolve
#     "Victoria" "This way your spell is the strongest."
#     show sc i_1_196_2 with my_dissolve
#     "Victoria" "You'll have three tries to prove, that your magic source has potential."
#     show sc i_1_196_2 with my_dissolve
#     "Victoria" "Got it?"


#     menu:
#         "No" if True:
#             $ pass
#         "Yes" if True:
#             "[Name]" "Yes, ma'am. I'm ready!"
#             "Victoria" "Show us what you got, Mr. [Surname]!"

#             jump pre_sheet_24_MagicMiniGameLabel_start
#     show sc i_1_196_2 with my_dissolve
#     "[Name]" "Can you please repeat rules once more?"
#     show sc i_1_196_2 with my_dissolve
#     "[Name]" "Wanna make sure I've got everything right."
#     show sc i_1_196_2 with my_dissolve
#     "Victoria" "No problem. As I've said..."

#     jump sheet_24_repeat_rules
# label pre_sheet_24_MagicMiniGameLabel_start:
#     $ game_now  = 1
#     $ difficulty = 'Easy'
#     $ timer_now = TimerClass(3)
#     $ s = 2
#     $ timer      = 0
#     $ timer_hide = False
#     $ timer     = 10
#     $ timer_now = TimerClass(10)
# label sheet_24_MagicMiniGameLabel_start:
#     scene bg_magic_test with Dissolve(.5)
#     $ unhovered_variable = 0
#     $ unhovered_variable_2 = 1
#     $ circles_animation  = [[8, 'down']]
#     $ a = [ [1053, 469], [1080, 520], [1090, 579], [1070, 632], [1050, 686], [970, 735], 
#             [880, 760], [790, 745], [751, 700], [700, 650], [679, 575], [669, 515], [669, 454], 
#             [688, 398], [713, 347], [749, 305], [802, 276], [856, 253], [914, 240], [974, 242], 
#             [1032, 260], [1086, 290], [1137, 331], [1173, 382], [1204, 448], [1222, 511], [1228, 575], 
#             [1227, 636], [1200, 713], [1180, 757], [1115, 798], [1060, 840], [1010, 860]]


# label sheet_24_game_1:

#     #$ mmg = MagicMiniGame([], True, a, timer = timer_hide)
#     #show screen MagicMiniGameScreen(win_circles = a, timer = timer, click_warning = False) with Dissolve(.75)

#     $ renpy.pause(.5)
#     # $ b = renpy.call_screen('MagicMiniGameScreen', win_circles = a, timer = timer)
#     $ d = 1
#     # python:
#     #     d = 0
#     #     if len(b) == 3 and b[2]:
#     #         d = 1
#     #     if len(b) == 4:
#     #         d = 2
#     #     c = b[1]
#     #     b = b[0]
#     # $ stss = mmg.check_win()
#     # $ mmg.mouse_down = False
#     # $ mmg.timer      = False
#     # $ mmg.only_watch = True

#     # $ mmg.only_watch_win_image = [



#     # [987, 469, False, False], [1021, 519, False, False], [1038, 571, False, False], [1036, 631, False, False], [996, 679, False, False], [936, 708, False, False], [874, 714, False, False], [816, 700, False, False], [763, 669, False, False], [717, 633, False, False], [685, 585, False, False], [670, 526, False, False], [669, 463, False, False], [691, 402, False, False], [721, 348, False, False], [777, 306, False, False], [831, 273, False, False], [906, 258, False, False], [975, 256, False, False], [1030, 276, False, False], [1086, 303, False, False], [1138, 337, False, False], [1171, 387, False, False], [1203, 436, False, False], [1234, 496, False, False], [1222, 555, False, False], [1209, 612, False, False], [1192, 673, False, False], [1167, 732, False, False], [1125, 774, False, False], [1080, 816, False, False], [1029, 846]]


#     # hide screen MagicMiniGameScreen
#     # hide screen m_line_max_screen 

#     $ b = renpy.call_screen('test_glyph_episode_2_2', 'combat_bolt')

#     if d == 1:
#         #show screen MagicMiniGameScreen(circles = c, win_circles = a, click = False) 
#         #$ renpy.pause(999999999)
#         "Score: [b]%%"
#     elif d == 2:
#         #scene bg_magic_test
#         #call screen MagicMiniGameScreen(circles = c, win_circles = a, click = False)
#         #show screen MagicMiniGameScreen(circles = c, win_circles = a, click = False) 

#         #hide screen m_line_max_screen

#         #show screen m_line_max_screen with Dissolve(.5)


#         "Score: [b]%%"
#     elif True:

#         #show screen MagicMiniGameScreen(circles = c, win_circles = a, click = False)
#         "Score: [b]%%"

#     if game_now == 1:
#         $ game_now = 2
#         if b >= 75:
#             scene sc i_1_196_5 with Dissolve(.5)
#             "Victoria" "Pleasant surprise, Mr. [Surname]. "
#             show sc i_1_196_5 with my_dissolve
#             "Victoria" "I can see you have good potential. "
#             show sc i_1_196_5 with my_dissolve
#             "[Name]" "{i}(Hell yes I do! That was too easy!){/i}"
#             show sc i_1_196_5 with my_dissolve
#             "Victoria" "Let's see if you can do even better."
#             show sc i_1_196_5 with my_dissolve
#             "[Name]" "{i}(Bring it on!){/i}"

#             $ difficulty = 'Medium'
#             $ timer     = 7
#             $ timer_now = TimerClass(7)
#             scene sc i_1_196_5
#             hide screen MagicMiniGameScreen 
#             hide screen m_line_max_screen 
#             with Dissolve(.5)

#         elif b >= 50:
#             scene sc i_1_196_4 with Dissolve(.5)
#             "Victoria" "Not bad for the first time!"
#             show sc i_1_196_4 with my_dissolve
#             "Victoria" "But I've had more capable students."
#             show sc i_1_196_4 with my_dissolve
#             "[Name]" "{i}(Not bad? I can do better than \"not bad\"! Come on, [Name]!){/i}"
#             show sc i_1_196_4 with my_dissolve
#             "Victoria" "Let's try to make it more difficult..."
#             $ difficulty = 'Medium'
#             $ timer     = 7
#             $ timer_now = TimerClass(7)
#             scene sc i_1_196_4
#             hide screen MagicMiniGameScreen 
#             hide screen m_line_max_screen 
#             with Dissolve(.5)
#         elif True:

#             scene sc i_1_196_3 with Dissolve(.5)
#             "Victoria" "[Surname], you're on the verge of failure."
#             show sc i_1_196_3 with my_dissolve
#             "Victoria" "That kind of concentration is no good!"
#             show sc i_1_196_3 with my_dissolve
#             "[Name]" "{i}(Crap... I need to focus! I won't lose this!){/i}"
#             show sc i_1_196_3 with my_dissolve
#             "Victoria" "Try again."
#             $ difficulty = 'Easy'
#             $ timer     = 10
#             $ timer_now = TimerClass(10)
#             scene sc i_1_196_3
#             hide screen MagicMiniGameScreen 
#             hide screen m_line_max_screen 
#             with Dissolve(.5)





#     elif game_now == 2:
#         $ game_now = 3
#         if b >= 75:

#             if timer == 7:
#                 scene sc i_1_196_5 with Dissolve(.5)
#                 "Victoria" "Very good, Mr. [Surname]! "
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "It is clear that you have potential."
#                 show sc i_1_196_5 with my_dissolve
#                 "[Name]" "{i}(Hell yes I do! That was too easy!){/i}"
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "Let's see how good you can use it right now."
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "Your last try! Go!"
#                 $ difficulty = 'Hard'
#                 $ timer     = 5
#                 $ timer_now = TimerClass(5)
#                 scene sc i_1_196_5
#                 hide screen MagicMiniGameScreen 
#                 hide screen m_line_max_screen 
#                 with Dissolve(.5)
#             elif True:

#                 scene sc i_1_196_5 with Dissolve(.5)
#                 "Victoria" "Not bad, [Surname]!"
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "I'm really interested to see what else you can do!"
#                 show sc i_1_196_5 with my_dissolve
#                 "[Name]" "{i}(Is this a dream, or am I really that good?!){/i}"
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "Last one will be even more difficult. Get ready!"
#                 show sc i_1_196_5 with my_dissolve
#                 "[Name]" "{i}(I am ready!){/i}"
#                 $ difficulty = 'Medium'
#                 $ timer     = 7
#                 $ timer_now = TimerClass(7)
#                 scene sc i_1_196_5
#                 hide screen MagicMiniGameScreen 
#                 hide screen m_line_max_screen 
#                 with Dissolve(.5)

#         elif b >= 50:

#             if timer == 7:
#                 scene sc i_1_196_4 with Dissolve(.5)
#                 "Victoria" "Mr. [Surname]! "
#                 show sc i_1_196_4 with my_dissolve
#                 "Victoria" "I recommend that you take this task more seriously."
#                 show sc i_1_196_4 with my_dissolve
#                 "[Name]" "{i}(I can do better, I know it!){/i}"
#                 show sc i_1_196_4 with my_dissolve
#                 "Victoria" "I'll give you one more try."
#                 scene sc i_1_196_4
#                 hide screen MagicMiniGameScreen 
#                 hide screen m_line_max_screen 

#                 with Dissolve(.5)
#                 $ difficulty = 'Hard'
#                 $ timer     = 5
#                 $ timer_now = TimerClass(5)
#             elif True:
#                 scene sc i_1_196_4 with Dissolve(.5)
#                 "Victoria" "Better. "
#                 show sc i_1_196_4 with my_dissolve
#                 "Victoria" "Bot not perfect."
#                 show sc i_1_196_4 with my_dissolve
#                 "[Name]" "{i}(I can nail this. Just need a little bit more focus.){/i}"
#                 show sc i_1_196_4 with my_dissolve
#                 "Victoria" "Let's make the task more difficult this time..."
#                 scene sc i_1_196_4
#                 hide screen MagicMiniGameScreen 
#                 hide screen m_line_max_screen 

#                 with Dissolve(.5)
#                 $ difficulty = 'Medium'
#                 $ timer     = 7
#                 $ timer_now = TimerClass(7)
#         elif True:


#             scene sc i_1_196_3 with Dissolve(.5)
#             "Victoria" "No, no, no... "
#             show sc i_1_196_3 with my_dissolve
#             "Victoria" "This is not the level I expect from my future students. "
#             show sc i_1_196_3 with my_dissolve
#             "[Name]" "Sorry, I've probably got disctracted. "
#             show sc i_1_196_3 with my_dissolve
#             "Victoria" "You still have one more try to impress me."
#             show sc i_1_196_3 with my_dissolve
#             "[Name]" "{i}(it's now or never!){/i}"
#             scene sc i_1_196_3
#             hide screen MagicMiniGameScreen 
#             hide screen m_line_max_screen 

#             with Dissolve(.5)
#             if timer == 7:
#                 $ difficulty = 'Medium'
#                 $ timer     = 7
#                 $ timer_now = TimerClass(7)
#             elif True:
#                 $ difficulty = 'Easy'
#                 $ timer     = 10
#                 $ timer_now = TimerClass(10)
#     elif game_now == 3:
#         $ game_now = 3
#         if timer == 10:
#             if b < 50:
#                 scene sc i_1_196_3 with Dissolve(.5)
#                 "Victoria" "You're a little bit bellow our standart level, mister [Surname]. "
#                 show sc i_1_196_3 with my_dissolve
#                 "[Name]" "{i}(....Shit.){/i}"
#                 show sc i_1_196_3 with my_dissolve
#                 "[Name]" "{i}(I was so close. Is this... the end?){/i}"
#                 show sc i_1_196_6 with my_dissolve
#                 "Victoria" "But you've still managed to form a solid glyph for an entrant."
#                 show sc i_1_196_7 with my_dissolve

#                 "[Name]" "Does this mean...?"
#                 show sc i_1_196_7 with my_dissolve
#                 "Victoria" "Yes, but it's not that simple."
#                 show sc i_1_196_7 with my_dissolve
#                 "Victoria" "You're enrolled."
#                 show sc i_1_196_7 with my_dissolve
#                 "Victoria" "For now."
#                 show sc i_1_196_7 with my_dissolve
#                 "Victoria" "But you'll have to show a special zeal for your studies."
#                 show sc i_1_196_7 with my_dissolve
#                 "Victoria" "If you want to stay at this academy."
#                 show sc i_1_196_7 with my_dissolve
#                 "[Name]" "I do."
#                 show sc i_1_196_7 with my_dissolve
#                 "[Name]" "I mean... I will. A special zeal from now on!"
#                 show sc i_1_196_7 with my_dissolve
#                 "[Name]" "Thank you!"
#                 scene sc i_1_196_7
#                 hide screen MagicMiniGameScreen 
#                 hide screen m_line_max_screen 

#                 with Dissolve(.5)
#             elif True:
#                 scene sc i_1_196_4 with Dissolve(.5)
#                 "Victoria" "Well..."
#                 show sc i_1_196_4 with my_dissolve
#                 "Victoria" "At least you achieved some result."
#                 show sc i_1_196_4 with my_dissolve
#                 "[Name]" "{i}(Does this mean...?){/i}"
#                 show sc i_1_196_6 with my_dissolve
#                 "Victoria" "You're enrolled."
#                 show sc i_1_196_6 with my_dissolve
#                 "Victoria" "For now."
#                 show sc i_1_196_6 with my_dissolve
#                 "Victoria" "But you'll have to show a special zeal for your studies."
#                 show sc i_1_196_6 with my_dissolve
#                 "Victoria" "If you want to stay at this academy."
#                 show sc i_1_196_6 with my_dissolve
#                 "[Name]" "I do."
#                 show sc i_1_196_6 with my_dissolve
#                 "[Name]" "I mean... I will. A special zeal from now on!"
#                 show sc i_1_196_6 with my_dissolve
#                 "[Name]" "Thank you!"
#                 scene sc i_1_196_6
#                 hide screen MagicMiniGameScreen 
#                 hide screen m_line_max_screen 

#                 with Dissolve(.5)
#         elif timer == 7:
#             if b < 75:
#                 scene sc i_1_196_4 with Dissolve(.5)
#                 "Victoria" "Well..."
#                 show sc i_1_196_4 with my_dissolve
#                 "Victoria" "At least you achieved some result."
#                 show sc i_1_196_4 with my_dissolve
#                 "[Name]" "{i}(Does this mean...?){/i}"
#                 show sc i_1_196_6 with my_dissolve
#                 "Victoria" "You're enrolled."
#                 show sc i_1_196_6 with my_dissolve
#                 "Victoria" "For now."
#                 show sc i_1_196_6 with my_dissolve
#                 "Victoria" "But you'll have to show a special zeal for your studies."
#                 show sc i_1_196_6 with my_dissolve
#                 "Victoria" "If you want to stay at this academy."
#                 show sc i_1_196_6 with my_dissolve
#                 "[Name]" "I do."
#                 show sc i_1_196_6 with my_dissolve
#                 "[Name]" "I mean... I will. A special zeal from now on!"
#                 show sc i_1_196_6 with my_dissolve
#                 "[Name]" "Thank you!"
#             elif True:

#                 scene sc i_1_196_5 with Dissolve(.5)
#                 "Victoria" "Congratulations, Mr. [Surname]! "
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "You have passed this exam. "
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "You have good potential! "
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "Someday you may even become a worthy wizard!"
#                 show sc i_1_196_5 with my_dissolve
#                 "[Name]" "Thank you, miss Lapis!"
#                 show sc i_1_196_5 with my_dissolve
#                 "[Name]" "I won't dissapoint you!"
#         elif True:




#             if b < 90:

#                 scene sc i_1_196_5 with Dissolve(.5)
#                 "Victoria" "Don't feel bad, Mr. [Surname]. "
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "I see such results on this test very rarely."
#                 show sc i_1_196_5 with my_dissolve
#                 "[Name]" "Was it that bad?"
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "On the contrary!"
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "A very decent result. But I think you can do better!"
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "You're accepted. "
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "You'll need a lot of practice to get even better."
#                 show sc i_1_196_5 with my_dissolve
#                 "[Name]" "I'm looking forward to it!"
#                 show sc i_1_196_5 with my_dissolve
#                 "Victoria" "Nice zeal, don't lose it!"
#             elif True:

#                 scene sc i_1_196_6 with Dissolve(.5)
#                 "Victoria" "Great result, [Name]! "
#                 show sc i_1_196_6 with my_dissolve
#                 "Victoria" "You are definitely accepted!"
#                 show sc i_1_196_6 with my_dissolve
#                 "Victoria" "You have a great future ahead of you. "
#                 show sc i_1_196_6 with my_dissolve
#                 "Victoria" "And I will do my best to help you reach your potential!"
#                 show sc i_1_196_6 with my_dissolve
#                 "[Name]" "Thank you, miss Lapis!"
#                 show sc i_1_196_6 with my_dissolve
#                 "[Name]" "That's an honor to hear this!"
#         jump sheet_24_end_game


#     jump sheet_24_MagicMiniGameLabel_start
# label sheet_24_end_game:
#     hide screen MagicMiniGameScreen
#     hide screen m_line_max_screen
#     scene sc i_1_196_8
#     with Dissolve(.5)
#     if hasattr(store, 'mmg'):
#         $ del mmg




#     "Victoria" "Alright! "
#     show sc i_1_196_8 with my_dissolve
#     "Victoria" "Congratulations, you're now officialy part of Cordale academy."
#     show sc i_1_196_8 with my_dissolve
#     "[Name]" "{i}(I DID IT! Fuck yeah!){/i}"
#     show sc i_1_196_8 with my_dissolve
#     "[Name]" "Thank you, Victoria."


#     show sc i_1_196_81 with my_dissolve
#     "Victoria" "Mr. [Surname]! "
#     "Victoria" "I understand that you're happy, but mind your language!"
#     "Victoria" "I'm miss Lapis for you."
#     show sc i_1_196_82 with my_dissolve
#     "Victoria" "You have to be much better at magic to call me \"Victoria\"..."
#     "[Name]" "{i}(Whoa, was that a clue, or was I imagine it?){/i}"



#     show sc i_1_196_9 with my_dissolve
#     "Victoria" "All accepted students are invited to our annual welcoming feast."
#     show sc i_1_196_9 with my_dissolve
#     "Victoria" "Go back to the Inner Garden..."
#     show sc i_1_196_9 with my_dissolve
#     "Victoria" "And find the door opposite to the Front Hall."
#     show sc i_1_196_9 with my_dissolve
#     "Victoria" "That's all. Dismissed."
#     show sc i_1_196_9 with my_dissolve
#     "[Name]" "Alright. Have a good one!"
#     scene expression '#000' with Dissolve(.5)
#     stop music  fadeout 1.0
#     play music_2  'audio/new/ambience/fountain_ambience.mp3' fadein 1.0





#     jump sheet_25
# # Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

















label sheet_24:

    stop music_2   fadeout 1.0
    play music 'audio/new/Music/Mini_game_music.mp3' fadein 1.0



    scene sc i_1_196_2 with Dissolve(1)
    "Victoria" "Once you've started casting a spell..."
    show sc i_1_196_2 with my_dissolve
label sheet_24_repeat_rules:
    "Victoria" "...concentrate and try to form a magic glyph."
    show sc i_1_196_2 with my_dissolve
    "Victoria" "Channel your magic powers into this glyph."
    show sc i_1_196_2 with my_dissolve
    "Victoria" "Your goal is to be as accurate as you can."
    show sc i_1_196_2 with my_dissolve
    "Victoria" "This way your spell is the strongest."
    show sc i_1_196_2 with my_dissolve
    "Victoria" "You'll have three tries to prove, that your magic source has potential."
    show sc i_1_196_2 with my_dissolve
    "Victoria" "Got it?"


    menu:
        "No" if True:
            $ pass
        "Yes" if True:
            "[Name]" "Yes, ma'am. I'm ready!"
            "Victoria" "Show us what you got, Mr. [Surname]!"

            jump pre_sheet_24_MagicMiniGameLabel_start
    show sc i_1_196_2 with my_dissolve
    "[Name]" "Can you please repeat rules once more?"
    show sc i_1_196_2 with my_dissolve
    "[Name]" "Wanna make sure I've got everything right."
    show sc i_1_196_2 with my_dissolve
    "Victoria" "No problem. As I've said..."

    jump sheet_24_repeat_rules
label pre_sheet_24_MagicMiniGameLabel_start:
    $ game_now  = 1
    $ difficulty = 'Easy'
    $ timer_now = TimerClass(3)
    $ s = 2
    $ timer      = 0
    $ timer_hide = False
    $ timer     = 10
    $ timer_now = TimerClass(10)
label sheet_24_MagicMiniGameLabel_start:
    scene bg_magic_test with Dissolve(.5)
    $ unhovered_variable = 0
    $ unhovered_variable_2 = 1
    $ circles_animation  = [[8, 'down']]
    $ a = [ [1053, 469], [1080, 520], [1090, 579], [1070, 632], [1050, 686], [970, 735], 
            [880, 760], [790, 745], [751, 700], [700, 650], [679, 575], [669, 515], [669, 454], 
            [688, 398], [713, 347], [749, 305], [802, 276], [856, 253], [914, 240], [974, 242], 
            [1032, 260], [1086, 290], [1137, 331], [1173, 382], [1204, 448], [1222, 511], [1228, 575], 
            [1227, 636], [1200, 713], [1180, 757], [1115, 798], [1060, 840], [1010, 860]]


label sheet_24_game_1:

    $ mmg = MagicMiniGame([], True, a, timer = timer_hide)
    show screen MagicMiniGameScreen(win_circles = a, timer = timer, click_warning = False) with Dissolve(.75)

    $ renpy.pause(.5)
    $ b = renpy.call_screen('MagicMiniGameScreen', win_circles = a, timer = timer)

    python:
        d = 0
        if len(b) == 3 and b[2]:
            d = 1
        if len(b) == 4:
            d = 2
        c = b[1]
        b = b[0]
    $ stss = mmg.check_win()
    $ mmg.mouse_down = False
    $ mmg.timer      = False
    $ mmg.only_watch = True

    $ mmg.only_watch_win_image = [



    [987, 469, False, False], [1021, 519, False, False], [1038, 571, False, False], [1036, 631, False, False], [996, 679, False, False], [936, 708, False, False], [874, 714, False, False], [816, 700, False, False], [763, 669, False, False], [717, 633, False, False], [685, 585, False, False], [670, 526, False, False], [669, 463, False, False], [691, 402, False, False], [721, 348, False, False], [777, 306, False, False], [831, 273, False, False], [906, 258, False, False], [975, 256, False, False], [1030, 276, False, False], [1086, 303, False, False], [1138, 337, False, False], [1171, 387, False, False], [1203, 436, False, False], [1234, 496, False, False], [1222, 555, False, False], [1209, 612, False, False], [1192, 673, False, False], [1167, 732, False, False], [1125, 774, False, False], [1080, 816, False, False], [1029, 846]]


    hide screen MagicMiniGameScreen
    hide screen m_line_max_screen 

    if d == 1:
        show screen MagicMiniGameScreen(circles = c, win_circles = a, click = False) 
        $ renpy.pause(999999999)
        "Score: [b]%%"
    elif d == 2:
        scene bg_magic_test
        call screen MagicMiniGameScreen(circles = c, win_circles = a, click = False)
        show screen MagicMiniGameScreen(circles = c, win_circles = a, click = False) 

        hide screen m_line_max_screen

        show screen m_line_max_screen with Dissolve(.5)


        "Score: [b]%%"
    elif True:

        show screen MagicMiniGameScreen(circles = c, win_circles = a, click = False)
        "Score: [b]%%"

    if game_now == 1:
        $ game_now = 2
        if b >= 75:
            scene sc i_1_196_5 with Dissolve(.5)
            "Victoria" "Pleasant surprise, Mr. [Surname]. "
            show sc i_1_196_5 with my_dissolve
            "Victoria" "I can see you have good potential. "
            show sc i_1_196_5 with my_dissolve
            "[Name]" "{i}(Hell yes I do! That was too easy!){/i}"
            show sc i_1_196_5 with my_dissolve
            "Victoria" "Let's see if you can do even better."
            show sc i_1_196_5 with my_dissolve
            "[Name]" "{i}(Bring it on!){/i}"

            $ difficulty = 'Medium'
            $ timer     = 7
            $ timer_now = TimerClass(7)
            scene sc i_1_196_5
            hide screen MagicMiniGameScreen 
            hide screen m_line_max_screen 
            with Dissolve(.5)

        elif b >= 50:
            scene sc i_1_196_4 with Dissolve(.5)
            "Victoria" "Not bad for the first time!"
            show sc i_1_196_4 with my_dissolve
            "Victoria" "But I've had more capable students."
            show sc i_1_196_4 with my_dissolve
            "[Name]" "{i}(Not bad? I can do better than \"not bad\"! Come on, [Name]!){/i}"
            show sc i_1_196_4 with my_dissolve
            "Victoria" "Let's try to make it more difficult..."
            $ difficulty = 'Medium'
            $ timer     = 7
            $ timer_now = TimerClass(7)
            scene sc i_1_196_4
            hide screen MagicMiniGameScreen 
            hide screen m_line_max_screen 
            with Dissolve(.5)
        elif True:

            scene sc i_1_196_3 with Dissolve(.5)
            "Victoria" "[Surname], you're on the verge of failure."
            show sc i_1_196_3 with my_dissolve
            "Victoria" "That kind of concentration is no good!"
            show sc i_1_196_3 with my_dissolve
            "[Name]" "{i}(Crap... I need to focus! I won't lose this!){/i}"
            show sc i_1_196_3 with my_dissolve
            "Victoria" "Try again."
            $ difficulty = 'Easy'
            $ timer     = 10
            $ timer_now = TimerClass(10)
            scene sc i_1_196_3
            hide screen MagicMiniGameScreen 
            hide screen m_line_max_screen 
            with Dissolve(.5)





    elif game_now == 2:
        $ game_now = 3
        if b >= 75:

            if timer == 7:
                scene sc i_1_196_5 with Dissolve(.5)
                "Victoria" "Very good, Mr. [Surname]! "
                show sc i_1_196_5 with my_dissolve
                "Victoria" "It is clear that you have potential."
                show sc i_1_196_5 with my_dissolve
                "[Name]" "{i}(Hell yes I do! That was too easy!){/i}"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "Let's see how good you can use it right now."
                show sc i_1_196_5 with my_dissolve
                "Victoria" "Your last try! Go!"
                $ difficulty = 'Hard'
                $ timer     = 5
                $ timer_now = TimerClass(5)
                scene sc i_1_196_5
                hide screen MagicMiniGameScreen 
                hide screen m_line_max_screen 
                with Dissolve(.5)
            elif True:

                scene sc i_1_196_5 with Dissolve(.5)
                "Victoria" "Not bad, [Surname]!"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "I'm really interested to see what else you can do!"
                show sc i_1_196_5 with my_dissolve
                "[Name]" "{i}(Is this a dream, or am I really that good?!){/i}"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "Last one will be even more difficult. Get ready!"
                show sc i_1_196_5 with my_dissolve
                "[Name]" "{i}(I am ready!){/i}"
                $ difficulty = 'Medium'
                $ timer     = 7
                $ timer_now = TimerClass(7)
                scene sc i_1_196_5
                hide screen MagicMiniGameScreen 
                hide screen m_line_max_screen 
                with Dissolve(.5)

        elif b >= 50:

            if timer == 7:
                scene sc i_1_196_4 with Dissolve(.5)
                "Victoria" "Mr. [Surname]! "
                show sc i_1_196_4 with my_dissolve
                "Victoria" "I recommend that you take this task more seriously."
                show sc i_1_196_4 with my_dissolve
                "[Name]" "{i}(I can do better, I know it!){/i}"
                show sc i_1_196_4 with my_dissolve
                "Victoria" "I'll give you one more try."
                scene sc i_1_196_4
                hide screen MagicMiniGameScreen 
                hide screen m_line_max_screen 

                with Dissolve(.5)
                $ difficulty = 'Hard'
                $ timer     = 5
                $ timer_now = TimerClass(5)
            elif True:
                scene sc i_1_196_4 with Dissolve(.5)
                "Victoria" "Better. "
                show sc i_1_196_4 with my_dissolve
                "Victoria" "Bot not perfect."
                show sc i_1_196_4 with my_dissolve
                "[Name]" "{i}(I can nail this. Just need a little bit more focus.){/i}"
                show sc i_1_196_4 with my_dissolve
                "Victoria" "Let's make the task more difficult this time..."
                scene sc i_1_196_4
                hide screen MagicMiniGameScreen 
                hide screen m_line_max_screen 

                with Dissolve(.5)
                $ difficulty = 'Medium'
                $ timer     = 7
                $ timer_now = TimerClass(7)
        elif True:


            scene sc i_1_196_3 with Dissolve(.5)
            "Victoria" "No, no, no... "
            show sc i_1_196_3 with my_dissolve
            "Victoria" "This is not the level I expect from my future students. "
            show sc i_1_196_3 with my_dissolve
            "[Name]" "Sorry, I've probably got disctracted. "
            show sc i_1_196_3 with my_dissolve
            "Victoria" "You still have one more try to impress me."
            show sc i_1_196_3 with my_dissolve
            "[Name]" "{i}(it's now or never!){/i}"
            scene sc i_1_196_3
            hide screen MagicMiniGameScreen 
            hide screen m_line_max_screen 

            with Dissolve(.5)
            if timer == 7:
                $ difficulty = 'Medium'
                $ timer     = 7
                $ timer_now = TimerClass(7)
            elif True:
                $ difficulty = 'Easy'
                $ timer     = 10
                $ timer_now = TimerClass(10)
    elif game_now == 3:
        $ game_now = 3
        if timer == 10:
            if b < 50:
                scene sc i_1_196_3 with Dissolve(.5)
                "Victoria" "You're a little bit bellow our standart level, mister [Surname]. "
                show sc i_1_196_3 with my_dissolve
                "[Name]" "{i}(....Shit.){/i}"
                show sc i_1_196_3 with my_dissolve
                "[Name]" "{i}(I was so close. Is this... the end?){/i}"
                show sc i_1_196_6 with my_dissolve
                "Victoria" "But you've still managed to form a solid glyph for an entrant."
                show sc i_1_196_7 with my_dissolve

                "[Name]" "Does this mean...?"
                show sc i_1_196_7 with my_dissolve
                "Victoria" "Yes, but it's not that simple."
                show sc i_1_196_7 with my_dissolve
                "Victoria" "You're enrolled."
                show sc i_1_196_7 with my_dissolve
                "Victoria" "For now."
                show sc i_1_196_7 with my_dissolve
                "Victoria" "But you'll have to show a special zeal for your studies."
                show sc i_1_196_7 with my_dissolve
                "Victoria" "If you want to stay at this academy."
                show sc i_1_196_7 with my_dissolve
                "[Name]" "I do."
                show sc i_1_196_7 with my_dissolve
                "[Name]" "I mean... I will. A special zeal from now on!"
                show sc i_1_196_7 with my_dissolve
                "[Name]" "Thank you!"
                scene sc i_1_196_7
                hide screen MagicMiniGameScreen 
                hide screen m_line_max_screen 

                with Dissolve(.5)
            elif True:
                scene sc i_1_196_4 with Dissolve(.5)
                "Victoria" "Well..."
                show sc i_1_196_4 with my_dissolve
                "Victoria" "At least you achieved some result."
                show sc i_1_196_4 with my_dissolve
                "[Name]" "{i}(Does this mean...?){/i}"
                show sc i_1_196_6 with my_dissolve
                "Victoria" "You're enrolled."
                show sc i_1_196_6 with my_dissolve
                "Victoria" "For now."
                show sc i_1_196_6 with my_dissolve
                "Victoria" "But you'll have to show a special zeal for your studies."
                show sc i_1_196_6 with my_dissolve
                "Victoria" "If you want to stay at this academy."
                show sc i_1_196_6 with my_dissolve
                "[Name]" "I do."
                show sc i_1_196_6 with my_dissolve
                "[Name]" "I mean... I will. A special zeal from now on!"
                show sc i_1_196_6 with my_dissolve
                "[Name]" "Thank you!"
                scene sc i_1_196_6
                hide screen MagicMiniGameScreen 
                hide screen m_line_max_screen 

                with Dissolve(.5)
        elif timer == 7:
            if b < 75:
                scene sc i_1_196_4 with Dissolve(.5)
                "Victoria" "Well..."
                show sc i_1_196_4 with my_dissolve
                "Victoria" "At least you achieved some result."
                show sc i_1_196_4 with my_dissolve
                "[Name]" "{i}(Does this mean...?){/i}"
                show sc i_1_196_6 with my_dissolve
                "Victoria" "You're enrolled."
                show sc i_1_196_6 with my_dissolve
                "Victoria" "For now."
                show sc i_1_196_6 with my_dissolve
                "Victoria" "But you'll have to show a special zeal for your studies."
                show sc i_1_196_6 with my_dissolve
                "Victoria" "If you want to stay at this academy."
                show sc i_1_196_6 with my_dissolve
                "[Name]" "I do."
                show sc i_1_196_6 with my_dissolve
                "[Name]" "I mean... I will. A special zeal from now on!"
                show sc i_1_196_6 with my_dissolve
                "[Name]" "Thank you!"
            elif True:

                scene sc i_1_196_5 with Dissolve(.5)
                "Victoria" "Congratulations, Mr. [Surname]! "
                show sc i_1_196_5 with my_dissolve
                "Victoria" "You have passed this exam. "
                show sc i_1_196_5 with my_dissolve
                "Victoria" "You have good potential! "
                show sc i_1_196_5 with my_dissolve
                "Victoria" "Someday you may even become a worthy wizard!"
                show sc i_1_196_5 with my_dissolve
                "[Name]" "Thank you, miss Lapis!"
                show sc i_1_196_5 with my_dissolve
                "[Name]" "I won't dissapoint you!"
        elif True:




            if b < 90:

                scene sc i_1_196_5 with Dissolve(.5)
                "Victoria" "Don't feel bad, Mr. [Surname]. "
                show sc i_1_196_5 with my_dissolve
                "Victoria" "I see such results on this test very rarely."
                show sc i_1_196_5 with my_dissolve
                "[Name]" "Was it that bad?"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "On the contrary!"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "A very decent result. But I think you can do better!"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "You're accepted. "
                show sc i_1_196_5 with my_dissolve
                "Victoria" "You'll need a lot of practice to get even better."
                show sc i_1_196_5 with my_dissolve
                "[Name]" "I'm looking forward to it!"
                show sc i_1_196_5 with my_dissolve
                "Victoria" "Nice zeal, don't lose it!"
            elif True:

                scene sc i_1_196_6 with Dissolve(.5)
                "Victoria" "Great result, [Name]! "
                show sc i_1_196_6 with my_dissolve
                "Victoria" "You are definitely accepted!"
                show sc i_1_196_6 with my_dissolve
                "Victoria" "You have a great future ahead of you. "
                show sc i_1_196_6 with my_dissolve
                "Victoria" "And I will do my best to help you reach your potential!"
                show sc i_1_196_6 with my_dissolve
                "[Name]" "Thank you, miss Lapis!"
                show sc i_1_196_6 with my_dissolve
                "[Name]" "That's an honor to hear this!"
        jump sheet_24_end_game


    jump sheet_24_MagicMiniGameLabel_start
label sheet_24_end_game:
    hide screen MagicMiniGameScreen
    hide screen m_line_max_screen
    scene sc i_1_196_8
    with Dissolve(.5)
    if hasattr(store, 'mmg'):
        $ del mmg




    "Victoria" "Alright! "
    show sc i_1_196_8 with my_dissolve
    "Victoria" "Congratulations, you're now officialy part of Cordale academy."
    show sc i_1_196_8 with my_dissolve
    "[Name]" "{i}(I DID IT! Fuck yeah!){/i}"
    show sc i_1_196_8 with my_dissolve
    "[Name]" "Thank you, Victoria."


    show sc i_1_196_81 with my_dissolve
    "Victoria" "Mr. [Surname]! "
    "Victoria" "I understand that you're happy, but mind your language!"
    "Victoria" "I'm miss Lapis for you."
    show sc i_1_196_82 with my_dissolve
    "Victoria" "You have to be much better at magic to call me \"Victoria\"..."
    "[Name]" "{i}(Whoa, was that a clue, or was I imagine it?){/i}"



    show sc i_1_196_9 with my_dissolve
    "Victoria" "All accepted students are invited to our annual welcoming feast."
    show sc i_1_196_9 with my_dissolve
    "Victoria" "Go back to the Inner Garden..."
    show sc i_1_196_9 with my_dissolve
    "Victoria" "And find the door opposite to the Front Hall."
    show sc i_1_196_9 with my_dissolve
    "Victoria" "That's all. Dismissed."
    show sc i_1_196_9 with my_dissolve
    "[Name]" "Alright. Have a good one!"
    scene expression '#000' with Dissolve(.5)
    stop music  fadeout 1.0
    play music_2  'audio/new/ambience/fountain_ambience.mp3' fadein 1.0





    jump sheet_25
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
