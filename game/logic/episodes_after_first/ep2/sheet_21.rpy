label sheet_21:
    scene sc i_1_149 with Dissolve(1)
    "Victoria" "Attention! "
    show sc i_1_149 with my_dissolve
    "Victoria" "The exam will take place on an individual basis."
    show sc i_1_149 with my_dissolve
    "Victoria" "We'll meet in the classroom 1."
    show sc i_1_149 with my_dissolve
    "Victoria" "To get to the classroom you need to go to the second door on the left."
    show sc i_1_149_2 with my_dissolve
    "Victoria" "On the other side of the garden."
    show sc i_1_149_2 with my_dissolve
    "Haley" "Excuse me, Miss Lapis!"
    show sc i_1_149_2 with my_dissolve
    "Victoria" "Yes?"
    show sc i_1_149_2 with my_dissolve
    "Haley" "Is the fountain behind your back magical?"
    show sc i_1_149_3 with my_dissolve
    "Victoria" "Oh, the \"Meek Dame\"?"
    show sc i_1_149_3 with my_dissolve
    "Victoria" "Nice spot. You've got a good magical feeling, young lady!"
    show sc i_1_149_3 with my_dissolve
    "Victoria" "The statue is far older than the fountain itself."
    show sc i_1_149_3 with my_dissolve
    "Victoria" "Legends say that it came from Cordoba with one of the founders..."
    show sc i_1_149_3 with my_dissolve
    "Victoria" "And that it contains great evil magic..."
    show sc i_1_149_3 with my_dissolve
    "Victoria" "But don't get too scared!"
    show sc i_1_149_3 with my_dissolve
    "Victoria" "It's been around here forever, even when I was a student."
    show sc i_1_149_3 with my_dissolve
    "Victoria" "And not once was it activated. "


    "Victoria" "Despite a lot of horror stories sophomores will tell you."
    "Victoria" "I don't want to ruin all the fun for older kids."
    "Victoria" "But according to them, every doorknob in this castle has a dark secret."





    show sc i_1_150 with my_dissolve
    "Victoria" "Alright! Let's focus on the exam, shall we?"
    show sc i_1_150 with my_dissolve
    "Victoria" "Second door on the left, as I've said it."
    show sc i_1_150 with my_dissolve
    "Victoria" "You can enter when I announce \"Next.\""
    show sc i_1_150 with my_dissolve
    "Victoria" "Anyone who tries to peek in on the exam will be sent home."
    show sc i_1_150 with my_dissolve
    "Victoria" "Let's get started. Good luck!"
    stop music_2   fadeout 20.0
    play music 'audio/new/Music/background_music1.mp3' fadein 4.0

    show sc i_1_150_2 with my_dissolve
    "[Name]" "{i}(Oh man.){/i}"
    show sc i_1_150_2 with my_dissolve
    "[Name]" "{i}(I know I should be focused on magic...){/i}"
    show sc i_1_150_3 with my_dissolve
    "[Name]" "{i}(But she is so gorgeous...){/i}"
    show sc i_1_150_3 with my_dissolve
    "[Name]" "{i}(Damn it!){/i}"
    show sc i_1_150_4 with my_dissolve
    "[Name]" "{i}(Focus, [Name]!){/i}"
    show sc i_1_150_4 with my_dissolve
    "[Name]" "{i}(This is my chance to start a new life.){/i}"
    show sc i_1_150_5 with my_dissolve
    "[Name]" "{i}(As a freaking wizard!){/i}"
    show sc i_1_150_5 with my_dissolve
    "[Name]" "{i}(Look out, Victoria! Here I go!){/i}"
    show sc i_1_151 with my_dissolve
    "[Name]" "{i}(Oh! Is that Haley?){/i}"
    show sc i_1_151 with my_dissolve
    "[Name]" "{i}(I promised her that I would catch up with her after getting off the train.){/i}"
    show sc i_1_151 with my_dissolve
    "[Name]" "{i}(I need to talk to her.){/i}"
    show sc i_1_152 with my_dissolve
    "Haley" "[Name], there you are! "
    show sc i_1_152 with my_dissolve
    "Haley" "Get in the line for exam. You can go after me."
    show sc i_1_153 with my_dissolve
    "[Name]" "Hey Haley! "
    show sc i_1_153 with my_dissolve
    "[Name]" "There's a line already?"
    show sc i_1_154 with my_dissolve
    "Haley" "Of course, I am seventh. We agreed back on the platform, just in case. It was when you were away."
    show sc i_1_154 with my_dissolve
    "Haley" "By the way, where have you been? Did you find your friend?"
    show sc i_1_153 with my_dissolve
    "[Name]" "Yes, she wanted to warn me about the exam."
    show sc i_1_154 with my_dissolve
    "Haley" "About what exactly?"
    show sc i_1_153 with my_dissolve
    "[Name]" "Sam told me that we only have one shot. Either we pass, or it's over."
    show sc i_1_153 with my_dissolve
    "[Name]" "They will erase your memory of magic and Cordale."
    show sc i_1_155 with my_dissolve
    "Haley" "Wait... Are you sure?"
    show sc i_1_155 with my_dissolve
    "[Name]" "That's what I've heard."
    show sc i_1_155 with my_dissolve
    "Haley" "No…"
    show sc i_1_156 with my_dissolve
    "Haley" "No way!"
    show sc i_1_156 with my_dissolve
    "Haley" "I don't believe this..."
    show sc i_1_157 with my_dissolve
    "Haley" "It can't be real!"
    "Haley" "I only just learned about magic. "
    show sc i_1_157 with my_dissolve
    "Haley" "There are still so many secrets to discover!{w} I…"



    menu:
        "Comfort Haley" if True:
            $ Comfort_Haley = True
            scene sc i_1_158 with Dissolve(.5)
            "[Name]" "Calm down Haley! I'm sure you will pass the exam."
            show sc i_1_158 with my_dissolve
            "[Name]" "You just need to believe in yourself like I believe in you."
            show sc i_1_159 with my_dissolve
            "[Name]" "Will you do this for me?"
            show sc i_1_159 with my_dissolve
            "Haley" "{i}(He's so nice to me...){/i}"
            show sc i_1_160 with my_dissolve
            "Haley" "Thank you, [Name]. I will try to."
            show sc i_1_160 with my_dissolve
            "[Name]" "That's great. And I will try to find out something else."
            scene expression '#000' with Dissolve(1)
            $ renpy.pause(1, hard = True)
            jump sheet_22
        "Leave Haley to cry" if True:

            $ Leave_Haley_to_cry = True
            scene sc i_1_161 with Dissolve(.5)
            "[Name]" "Well... I mean... yeah, take your time. I'm going to try to find out something else."
            scene expression '#000' with Dissolve(1)
            $ renpy.pause(1, hard = True)
            jump sheet_22
        "Hug Haley" if True:
            $ Hug_Haley = True
            $ pass



    scene sc i_1_158 with Dissolve(.5)
    "[Name]" "Haley, calm down. "
    show sc i_1_158 with my_dissolve
    "[Name]" "Don't cry."
    show sc i_1_163 with my_dissolve
    "Haley" "I cannot lose the world of magic now."
    show sc i_1_163 with my_dissolve
    "Haley" "You have no idea what this chance means to me..."
    show sc i_1_164 with my_dissolve
    "[Name]" "Haley!"
    show sc i_1_164 with my_dissolve
    "Haley" "Wha...{w} What are you..."
    show sc i_1_164 with my_dissolve
    "[Name]" "Calm down."
    show sc i_1_164_2 with my_dissolve
    "[Name]" "You won't lose it if you just keep yourself together now."
    show sc i_1_164_2 with my_dissolve
    "[Name]" "I found out that magic is powered by passion!"
    show sc i_1_164_2 with my_dissolve
    "[Name]" "Just focus on something that you are passionate about and bring the heat!"
    show sc i_1_165 with my_dissolve
    "[Name]" "Believe in yourself. Because I believe in you!"
    show sc i_1_165 with my_dissolve
    "Haley" "{i}(He's so nice to me...){/i}"
    show sc i_1_166 with my_dissolve
    "Haley" "Thank you, [Name]. "
    show sc i_1_166 with my_dissolve
    "Haley" "I will try to."
    show sc i_1_165 with my_dissolve
    "[Name]" "That's great."
    show sc i_1_167 with my_dissolve
    "Haley" "[Name]?"
    show sc i_1_167 with my_dissolve
    "[Name]" "What?"
    show sc i_1_167 with my_dissolve
    "Haley" "Could you..."
    show sc i_1_167 with my_dissolve
    "Haley" "Could you please let me go? "
    show sc i_1_167 with my_dissolve
    "Haley" "Everyone is staring at us."
    show sc i_1_168 with my_dissolve
    "[Name]" "Yeah, sure!"
    show sc i_1_168 with my_dissolve
    "[Name]" "He-he..."
    show sc i_1_170 with my_dissolve
    "[Name]" "I'm sorry."
    show sc i_1_171 with my_dissolve
    "Haley" "Cuddling with random girls is your thing now?"
    show sc i_1_170 with my_dissolve
    "[Name]" "Only with you."
    show sc i_1_171 with my_dissolve
    "Haley" "Thank you. Again."
    show sc i_1_170 with my_dissolve
    "[Name]" "No problem. I'll go find out if there are more surprises to come."
    scene expression '#000' with Dissolve(1)
    $ renpy.pause(1, hard = True)
    jump sheet_22
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
