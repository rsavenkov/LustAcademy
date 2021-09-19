label sheet_25:
    scene sc i_1_197_0 with Dissolve(1)
    $ renpy.pause(9999999)


    if hasattr(store, 'Hug_Haley') and Hug_Haley:
        scene sc i_1_197 with Dissolve(1)
        "Haley" "[Name]! Did you pass too? I'm so glad!"
        show sc i_1_197 with my_dissolve
        "Haley" "If not for you, I never would have succeeded!"
        show sc i_1_197 with my_dissolve
        "[Name]" "It's alright! I wouldn't leave you in trouble."
        show sc i_1_198 with my_dissolve
        "Haley" "Let's go to the Main Hall to get better seats."
        show sc i_1_198 with my_dissolve
        "Haley" "I've heard the headmaster will be giving the opening speech!"
        show sc i_1_198 with my_dissolve
        "[Name]" "Cool. Let's go!"
        scene expression '#000' with Dissolve(.5)
        jump sheet_26

    scene sc i_1_199 with Dissolve(.5)
    "Haley" "Did you pass too? Great! "
    "Haley" "Now I have someone to sit with. Let's go!"
    show sc i_1_200 with my_dissolve
    "[Name]" "Wait, shouldn't we wait for the others?"
    show sc i_1_201 with my_dissolve
    "Haley" "It will take forever!"
    show sc i_1_201 with my_dissolve
    "Haley" "We'd better go to the main hall and get seats."
    show sc i_1_201 with my_dissolve
    "Haley" "I heard that the headmaster will be giving the opening speech!"
    show sc i_1_202 with my_dissolve
    "[Name]" "Cool. Let's go!"
    scene expression '#000' with Dissolve(.5)
    jump sheet_26
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
