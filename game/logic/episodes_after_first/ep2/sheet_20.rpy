label sheet_20:
    scene sc i_1_130 with Dissolve(.5)
    "Jacob" "Welcome to the Cordale Academy of Magic and Wizardry!"
    show sc i_1_130 with my_dissolve
    "[Name]" "{i}(This place looks so epic!){/i}"
    show sc i_1_130 with my_dissolve
    "[Name]" "Excuse me, can we look around here?"
    show sc i_1_130 with my_dissolve
    "Jacob" "Impressive, isn't it?"
    show sc i_1_130 with my_dissolve
    "Jacob" "We are proud of the history of our academy. "
    show sc i_1_130_2 with my_dissolve
    "Jacob" "Many great wizards are depicted on murals and gobelins throughout the institution!"
    show sc i_1_130_2 with my_dissolve
    "Jacob" "But it would be better, if you dont get distracted by this majesty."
    show sc i_1_130_2 with my_dissolve
    "Jacob" "Better focus on your exam."
    show sc i_1_130_2 with my_dissolve
    "Jacob" "You'll have plenty of time to gaze all these over later..."
    show sc i_1_130_3 with my_dissolve
    "[Name]" "{i}(Wait...){/i}"
    show sc i_1_130_3 with my_dissolve
    "[Name]" "{i}(Who is that gorgeous girl behind him?){/i}"
    show sc i_1_130_3 with my_dissolve
    "Jacob" "Oh, Miss Lapis!"





    python:
        try:
            
            pos_track_now = float(renpy.music.get_pos('music_2')) - 2
        except:
            pos_track_now = 0






    play sound 'audio/new/gameplay/Woman_footsteps.mp3'
    scene 1_130_victoria with Dissolve(.5)
    $ renpy.pause(5, hard = True)
    $ renpy.pause(999999)



    scene sc i_1_131 with Dissolve(.5)
    "Jacob" "Good evening, Victoria. The applicants have arrived."
    show sc i_1_131 with my_dissolve
    "Victoria" "I know, Jacob. "
    show sc i_1_131 with my_dissolve

    "Victoria" "But what are you doing here? "

    "Victoria" "It's up to examiner to meet the applicants."
    show sc i_1_131 with my_dissolve
    "Victoria" "I am the examiner."
    "Victoria" "So this is my task."
    "Victoria" "Care to explain yourself?"
    show sc i_1_132 with my_dissolve
    "Jacob" "Right. "
    "Jacob" "So the deal is..."
    "Jacob" "Headmaster had a hard time reaching you..."
    show sc i_1_133 with my_dissolve
    "Jacob" "...and he asked me to meet the students."
    "Jacob" "Just in case you won't be able to make it."
    "Jacob" "Don't overthink it."
    show sc i_1_133_2 with my_dissolve
    "Victoria" "How strange. I didn't receive any messages from him."
    "Victoria" "Thank you, Jacob. From this point I'll take the lead."
    show sc i_1_134 with my_dissolve
    "Jacob" "Sure. "
    show sc i_1_134 with my_dissolve
    "Jacob" "I will inform the headmaster that you have shown up."
    show sc i_1_134 with my_dissolve
    "Jacob" "Good luck at the exam, Vicky."
    show sc i_1_134_2 with my_dissolve
    "Victoria" "Applicants!"
    show sc i_1_135 with my_dissolve
    "Victoria" "Please, gather around me."
    show sc i_1_136 with my_dissolve
    "Victoria" "My name is Victoria Lapis. I am a teacher of battle magic and your examiner."
    show sc i_1_136 with my_dissolve
    "Victoria" "Surely you've noticed the mural behind me!"








    show sc i_1_136_2 with my_dissolve
    "Victoria" "It depicts the legendary Melissa Owlsight!"
    show sc i_1_136_2 with my_dissolve
    "Victoria" "The first mage to ever set her foot on the lands of North America."
    show sc i_1_136_2 with my_dissolve
    "Victoria" "And the teacher of four founders of Cordale Academy."
    show sc i_1_136_2 with my_dissolve
    "Victoria" "When Melissa was on her deathbed."
    show sc i_1_136_2 with my_dissolve
    "Victoria" "She united four of her students to continue her path."
    show sc i_1_136_2 with my_dissolve
    "Victoria" "And with her dying breath...{w} She conjured the first stone for this building."
    show sc i_1_136_2 with my_dissolve
    "Victoria" "Only the most diligent students will ever reach her greatness."
    show sc i_1_136_2 with my_dissolve
    "Victoria" "Every mage who used to study in Cordale Academy..."
    show sc i_1_136_2 with my_dissolve
    "Victoria" "...dreams of finding the way to obtain her hidden knowledge."
    show sc i_1_136_2 with my_dissolve
    "Victoria" "Who knows, maybe one of you can do it!"





    show sc i_1_136 with my_dissolve
    "Victoria" "But first you'll have to prove yourself worthy."
    show sc i_1_136 with my_dissolve
    "Victoria" "By passing my exam.{w} Good luck with that!"
    show sc i_1_136 with my_dissolve
    "Victoria" "Knowing Jacob, I'll assume..."
    show sc i_1_136 with my_dissolve
    "Victoria" "...that he came up with an excuse not to answer your questions, so I'll have to."
    show sc i_1_136 with my_dissolve
    "Victoria" "Ask your questions!"
    show sc i_1_137 with my_dissolve
    "Unknown Girl" "You said you teach \"battle magic\"..."
    show sc i_1_137 with my_dissolve
    "Unknown Girl" "What is that?"
    show sc i_1_138 with my_dissolve

    "Victoria" "That's right."





    play music_fire 'audio/new/sounds/Fire_loop.mp3'
    scene sc i_1_138_2 with Dissolve(.5)




    "Victoria" "Here!"


    "[Name]" "{i}(Holy shit!){/i}"

    "[Name]" "{i}(This IS real!){/i}"

    "[Name]" "{i}(Freaking fireball!){/i}"

    "Victoria" "Take a good look, applicants!"

    "Victoria" "This is what my lessons are about!"

    "Victoria" "I will teach you attacking and defending spells."
    stop music_fire
    play sound 'audio/new/sounds/Fire_end.mp3'
    show sc i_1_139 with my_dissolve
    "Victoria" "So that you can stand up for yourself."
    show sc i_1_139 with my_dissolve
    "Victoria" "The world of magic is far from harmless."
    show sc i_1_139 with my_dissolve
    "Victoria" "Other questions?"
    $ tmp_list = [0, 0, 0, 0, 0, 0]
label sheet_20_menu_1:
    scene sc i_1_139 with Dissolve(.5)
    menu:
        "Ask about the Academy" if not tmp_list[0]:
            $ tmp_list[0] = 1
            jump sheet_20_menu_1_ans_1
        "Ask about exams" if not tmp_list[1]:
            $ tmp_list[1] = 1
            jump sheet_20_menu_1_ans_2
        "Flirt" if not tmp_list[2]:
            $ tmp_list[2] = 1
            jump sheet_20_menu_1_ans_3
        "No questions" if not tmp_list[3]:
            $ tmp_list[3] = 1
            jump sheet_20_menu_1_ans_4

label sheet_20_menu_1_ans_1:
    scene sc i_1_142 with Dissolve(.5)
    "[Name]" "Tell us about Cordale Academy."
    show sc i_1_140 with my_dissolve
    "Victoria" "Cordale is the oldest and most prestigious academy for magic and wizardry in New World."


    show sc i_1_140 with my_dissolve
    "Victoria" "Throughout 3 courses you will learn the basics of all schools of magic allowed in America."
    show sc i_1_140 with my_dissolve
    "Victoria" "You will discover your specialization!"
    show sc i_1_141 with my_dissolve
    "Victoria" "If, of course, you pass my exam and can stay here."
    show sc i_1_141 with my_dissolve
    "Victoria" "Anything else?"
    show sc i_1_142 with my_dissolve
    "[Name]" "How is it that everyone knows that Cordale is a prestigious educational institution..."
    show sc i_1_142 with my_dissolve
    "[Name]" "...yet most of the people think that magic is not real?"
    show sc i_1_142 with my_dissolve
    "[Name]" "I thought things like that fireball of yours would get viral or something..."
    show sc i_1_140 with my_dissolve
    "Victoria" "Magic!"
    show sc i_1_140 with my_dissolve
    "Victoria" "Well, more precisely — the painstaking work of the PR department. "
    show sc i_1_140 with my_dissolve
    "Victoria" "A-and a little bit of magic."
    show sc i_1_141 with my_dissolve
    "Victoria" "All your friends and family know that you are going to the Cordale!"
    show sc i_1_141 with my_dissolve
    "Victoria" "An elite Ivy League-level educational institution. "
    show sc i_1_141 with my_dissolve
    "Victoria" "All the rest is done for us in their imagination."
    show sc i_1_142 with my_dissolve
    "[Name]" "{i}(Hmm...It's strange.){/i}"
    show sc i_1_142 with my_dissolve
    "[Name]" "{i}(I am 99%% sure Don and Olivia know what's going on...){/i}"
    show sc i_1_142 with my_dissolve
    "[Name]" "{i}(Either your PR department is under-performing, or Sam told them...){/i}"
    show sc i_1_142 with my_dissolve
    "[Name]" "{i}(Next time I meet Samantha we should discuss this.){/i}"
    show sc i_1_141 with my_dissolve
    "Victoria" "Right now, they are certain that you are getting some respected profession."
    show sc i_1_141 with my_dissolve
    "Victoria" "Other questions?"
    jump sheet_20_menu_1

label sheet_20_menu_1_ans_2:
    scene sc i_1_142 with Dissolve(.5)
    "[Name]" "What will be on the exam?"
    show sc i_1_140 with my_dissolve
    "Victoria" "You all might have noticed something unusual after your trip on our train."
    show sc i_1_140 with my_dissolve
    "Victoria" "Right now you are all overwhelmed with magical power! "
    show sc i_1_140 with my_dissolve
    "Victoria" "All that's left is for you to show me how you use it. During the examination."
    show sc i_1_142 with my_dissolve
    "[Name]" "How can I show something that I have never done before?"
    show sc i_1_142 with my_dissolve
    "Victoria" "Trust me, if you have the potential, it will happen. More questions?"
    jump sheet_20_menu_1

label sheet_20_menu_1_ans_3:
    scene sc i_1_142 with Dissolve(.5)
    "[Name]" "What spell have you used to seduce me?"
    show sc i_1_142 with my_dissolve
    "[Name]" "It's working, I feel it!"
    show sc i_1_143 with my_dissolve
    "Victoria" "Really?"
    show sc i_1_144 with my_dissolve
    "Victoria" "What's your name?"
    show sc i_1_145 with my_dissolve
    "[Name]" "[Name]. "
    show sc i_1_145 with my_dissolve
    "[Name]" "[Name] [Surname]."
    show sc i_1_144 with my_dissolve
    "Victoria" "That sounds familiar. "
    show sc i_1_144 with my_dissolve
    "Victoria" "Do you have any family members who studied here, in Cordale?"

    show sc i_1_145 with my_dissolve
    "[Name]" "I don't know. I'm an orphan."

    show sc i_1_145 with my_dissolve
    "[Name]" "My friend and flatmate Samantha Rose studies here."
    show sc i_1_144 with my_dissolve
    "Victoria" "Is that so? Well in that case..."
    show sc i_1_144 with my_dissolve
    "Victoria" "It would be a pity if the friend of my most talented student was kicked out of the academy..."
    show sc i_1_144 with my_dissolve
    "Victoria" "...just because he decided to make fun of the examiner before the exam. "
    show sc i_1_144 with my_dissolve
    "Victoria" "What do you think?"
label sheet_20_menu_2:
    scene sc i_1_145 with Dissolve(.5)
    menu:
        "Apologize" if True:
            jump sheet_20_menu_2_ans_1
        "Give a witty answer" if True:
            jump sheet_20_menu_2_ans_2


label sheet_20_menu_2_ans_1:
    scene sc i_1_145 with Dissolve(.5)
    "[Name]" "I'm sorry, I didn't mean to offend you."
    show sc i_1_146 with my_dissolve
    "Victoria" "Don't forget that Cordale is an elite educational institution."
    show sc i_1_146 with my_dissolve
    "Victoria" "Respect for teachers is part of our customs.{w} More questions?"
    jump sheet_20_menu_1

label sheet_20_menu_2_ans_2:
    scene sc i_1_146 with Dissolve(.5)
    "[Name]" "But then you will lose the chance to teach your new most talented student."
    show sc i_1_147 with my_dissolve
    "Victoria" "Mr. [Surname], you have a sharp tongue."
    show sc i_1_147 with my_dissolve
    "Victoria" "Let's hope that this is not your only talent if you want to pass my exam."
    show sc i_1_147 with my_dissolve
    "Victoria" "Do you still have questions?"
    jump sheet_20_menu_1

label sheet_20_menu_1_ans_4:
    scene sc i_1_142 with Dissolve(.5)
    "[Name]" "No more questions! I am ready!"
    show sc i_1_148 with my_dissolve
    "Victoria" "I'm afraid we can't make people wait much longer."
    show sc i_1_148 with my_dissolve
    "Victoria" "I hope I managed to answer your questions."
    show sc i_1_148 with my_dissolve
    "Victoria" "Applicants, please follow me!"
    scene expression '#000' with Dissolve(1)
    $ renpy.pause(1, hard = True)

    stop music   fadeout 1.0
    play music_2 'audio/new/ambience/fountain_ambience.mp3' fadein 1.0

    jump sheet_21
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
