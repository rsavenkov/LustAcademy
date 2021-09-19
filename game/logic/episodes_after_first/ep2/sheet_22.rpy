label sheet_22:
    scene sc i_1_172_0 with Dissolve(1)
    $ colors_names["Unknown Girl"] = "#5ccc00"
    $ renpy.pause(99999999999999)


    python:
        try:
            
            pos_track_now = float(renpy.music.get_pos('music')) - 2
        except:
            pos_track_now = 0
    stop music fadeout 1.0
    play music 'audio/new/Music/background_music1.mp3' fadein 10.0
    play sound 'audio/new/Music/intro1.mp3' fadein 1.0




    scene sc i_1_172_2_video with Dissolve(1)
    $ renpy.pause(9, hard = True)
    $ renpy.pause(99999999999999)
    scene sc i_1_172 with Dissolve(.5)

    "Unknown Girl" "How can you dream of getting into Leonheart? They're losers!"
    show sc i_1_172 with my_dissolve
    "Unknown Girl" "What will you achieve with kindness and self-sacrifice?"
    show sc i_1_172 with my_dissolve
    "Unknown Girl" "These are not fairy tales, but life, Lily!"
    show sc i_1_173 with my_dissolve
    "Lily" "How can you be happy if for the sake of success..."
    show sc i_1_173 with my_dissolve
    "Lily" "...you have to sacrifice friends, cheat, lie and deceive?"
    show sc i_1_173 with my_dissolve
    "Lily" "Who can dream of getting into Adderin?"
    show sc i_1_174 with my_dissolve
    "Unknown Girl" "Hey, you!"
    show sc i_1_175 with my_dissolve
    "[Name]" "Who, me?"
    show sc i_1_176 with my_dissolve
    "Unknown Girl" "Yes, you. {w}Arbitrate us."
    show sc i_1_177 with my_dissolve
    "Lily" "We're arguing about houses. Which one is better?"
    show sc i_1_177 with my_dissolve
    "Lily" "I think that there's nothing better than getting into Leonheart."
    show sc i_1_176 with my_dissolve
    "Unknown Girl" "And I believe that Adderin is a cut above any other!"
    show sc i_1_176 with my_dissolve
    "Unknown Girl" "All successful magicians have been a part of our house. And what do you think?"
    show sc i_1_177 with my_dissolve
    "Lily" "Well?"
    show sc i_1_178 with my_dissolve
    "[Name]" "Who are you anyway? What are these \"houses\"?"
    show sc i_1_179 with my_dissolve
    "Lily" "Sorry, we seem to get too caught up in the argument. My name is Lily."
    show sc i_1_180 with my_dissolve
    "Unknown Girl" "And I'm Naomi. What's your name?"
    show sc i_1_178 with my_dissolve
    "[Name]" "I am [Name] [Surname]. Nice to meet you."
    show sc i_1_176 with my_dissolve
    "Naomi" "Sorry for jumping on you like that, [Name]."
    show sc i_1_176 with my_dissolve
    "Naomi" "We were discussing the houses we want to enter and argued a lot."
    show sc i_1_178 with my_dissolve
    "[Name]" "No problem. So what houses are we talking about?"
    show sc i_1_177 with my_dissolve
    "Lily" "Have you never heard of the four great houses? "
    show sc i_1_177 with my_dissolve
    "Lily" "You are probably not one of the hereditary magicians, right?"
    show sc i_1_176 with my_dissolve
    "Naomi" "I have heard that most magicians only learn about magic when they are invited to study it."
    show sc i_1_176 with my_dissolve
    "Naomi" "Is that so?"
    show sc i_1_178 with my_dissolve
    "[Name]" "Yeah. Isn't it how it should be for everyone?"
    show sc i_1_177 with my_dissolve
    "Lily" "Actually, yes. Rules are for everyone."
    show sc i_1_177 with my_dissolve
    "Lily" "But our families are hereditary purebred sorcerers."
    show sc i_1_177 with my_dissolve
    "Lily" "We know some of the secrets of this world since childhood."
    show sc i_1_178 with my_dissolve
    "[Name]" "Hmm. It turns out that you have an advantage over us."
    show sc i_1_176 with my_dissolve
    "Naomi" "Just a little."
    show sc i_1_177 with my_dissolve
    "Lily" "Yes, only in theory."
    show sc i_1_177 with my_dissolve
    "Lily" "Purebred children, like other magicians, are strictly forbidden to practice magic..."
    show sc i_1_177 with my_dissolve
    "Lily" "...before entering the wizarding academy."
    show sc i_1_178 with my_dissolve
    "[Name]" "I see. And yet, what are the houses?"
    show sc i_1_181 with my_dissolve
    "Lily" "The academy was founded by four powerful sorceresses."
    show sc i_1_181 with my_dissolve
    "Lily" "Each has created its own house and taught students as they saw fit."
    show sc i_1_182 with my_dissolve
    "Naomi" "House selection is the most important thing in Cordale! You choose your future connection..."
    show sc i_1_181 with my_dissolve
    "Lily" "Friends..."
    show sc i_1_182 with my_dissolve
    "Naomi" "Reputation!"
    show sc i_1_181 with my_dissolve
    "Lily" "And drinking pals!"
    show sc i_1_183 with my_dissolve
    "[Name]" "Incredibly interesting, but don't you think we have a bigger concern right now?"
    show sc i_1_183 with my_dissolve
    "Lily" "What are you talking about? What could be more important than the house?!"
    show sc i_1_184 with my_dissolve
    "[Name]" "Entrance examination? "
    show sc i_1_184 with my_dissolve
    "[Name]" "How do you plan to get into the house if you don't get to go to the academy?"
    show sc i_1_185 with my_dissolve
    "Naomi" "That's easy!"
    show sc i_1_186 with my_dissolve
    "Lily" "Consider that we have already entered."
    show sc i_1_184 with my_dissolve
    "[Name]" "Why such confidence?"
    show sc i_1_186 with my_dissolve
    "Lily" "Pureblood wizards always do good on exams."
    show sc i_1_187 with my_dissolve
    "Naomi" "The magic is in our blood."
    show sc i_1_187 with my_dissolve
    "Naomi" "We won't have any problems on the exam."
    show sc i_1_187 with my_dissolve
    "Naomi" "So the house is what's most important!"
    show sc i_1_187 with my_dissolve
    "[Name]" "I'm glad for you, but it won't help me."
    show sc i_1_187 with my_dissolve
    "Victoria" "Next!"
    show sc i_1_187_2 with my_dissolve

    "[Name]" "{i}(Oh, crap!){/i}"
    show sc i_1_187_2 with my_dissolve
    "[Name]" "{i}(I've completly lost track of the line.){/i}"
    show sc i_1_187_2 with my_dissolve
    "[Name]" "{i}(Should I ask someone or should I just go?){/i}"
    $ colors_names["Unknown Girl"] = "#FFF"
    show sc i_1_188 with my_dissolve
    "Unknown Girl" "Hey, who was after Haley?"
    show sc i_1_188 with my_dissolve
    "[Name]" "Oh shit, it's me!"
    show sc i_1_188 with my_dissolve
    "Lily" "Good luck!"
    show sc i_1_188 with my_dissolve
    "Naomi" "Bye!"
    show sc i_1_189 with my_dissolve
    "[Name]" "{i}(Well, here we go...){/i}"
    show sc i_1_189 with my_dissolve
    "[Name]" "{i}(I literally feel goosebumps right now...){/i}"
    show sc i_1_189_2 with my_dissolve
    "[Name]" "{i}(My first magic exam...){/i}"
    show sc i_1_189_2 with my_dissolve
    "[Name]" "{i}(Come on, [Name]! Let's not make it our last one!){/i}"

    scene expression '#000' with Dissolve(1)

    $ renpy.pause(1, hard = True)

    jump sheet_23
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
