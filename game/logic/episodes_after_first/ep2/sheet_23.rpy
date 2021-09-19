label sheet_23:
    scene sc i_1_190 with Dissolve(1)

    $ renpy.pause(9999)

    "[Name]" "Good day, miss.{w} [Name] [Surname]."
    show sc i_1_190_2 with my_dissolve
    "Victoria" "Yeah, I've remembered you.{w} Come in. Go to the center of the room."
    "Victoria" "Stand across from the board."
    show sc i_1_191 with my_dissolve
    "Victoria" "Your task is to create a simple magical glyph in the air."
    show sc i_1_191 with my_dissolve
    "[Name]" "{i}(You're making it sound so easy...){/i}"
    show sc i_1_192 with my_dissolve
    "Victoria" "Are you ready?"
    scene sc i_1_192 with Dissolve(.5)
    menu:
        "Flirt" if True:
            $ pass
        "Always ready!" if True:
            jump sheet_23_menu_2

    show sc i_1_192 with my_dissolve
    "[Name]" "Maybe a good luck kiss?"
    show sc i_1_193 with my_dissolve
    "Victoria" "I'll assume that's just your stress talking, Mister [Surname]. "
    show sc i_1_193 with my_dissolve
    "Victoria" "Stop this childish behavior."
    show sc i_1_192 with my_dissolve
    "Victoria" "Are you ready?"
    show sc i_1_192 with my_dissolve
label sheet_23_menu_2:
    stop music   fadeout 2.0
    play music_2 'audio/new/Music/memories_music.mp3' fadein 2.0
    "[Name]" "{i}(Alright, let's focus on something you feel passionate about!){/i}"
    scene sc i_1_192_blur with Dissolve(.5)

    if hasattr(store, 'i_1_043_1_var') or hasattr(store, 'i_1_061_a1_var') or hasattr(store, 'i_1_101_9_var'):
        menu:
            "Ashley" if hasattr(store, 'i_1_043_1_var'):
                jump sheet_23_ashley
            "Olivia" if hasattr(store, 'i_1_061_a1_var'):
                jump sheet_23_olivia
            "Haley" if hasattr(store, 'i_1_101_9_var'):
                jump sheet_23_haley
            "Nothing" if True:
                $ pass


    scene sc i_1_192_blur with Dissolve(.5)

    "[Name]" "({i}It's been so long since I was with a girl.){/i}"
    show sc i_1_192_blur with my_dissolve
    "[Name]" "{i}(Maybe that waitress, after the cup match last march?){/i}"
    show sc i_1_192_blur with my_dissolve
    "[Name]" "{i}(No, I can barely remember her face...){/i}"
    show sc i_1_192_blur with my_dissolve
    "[Name]" "{i}(Maybe... Nah...){/i}"
    show sc i_1_192_blur with my_dissolve
    "[Name]" "{i}(Oh snap, I can't remember anything.){/i}"
    show sc i_1_192_blur with my_dissolve
    "[Name]" "{i}(Guess I'm gonna have a hard time.){/i}"

    scene expression '#000' with Dissolve(1)

    $ renpy.pause(1, hard = True)

    jump sheet_24







label sheet_23_ashley:


    "[Name]" "{i}(Fiery Ashley can ignite my passion any day anytime!){/i}"
    scene sc i_1_043_1 with Dissolve(1)
    $ renpy.pause(999999999)






    jump sheet_23_energy
label sheet_23_olivia:


    "[Name]" "{i}(One thought of Olivia godlike forms fills me with power!){/i}"

    scene sc i_1_061_a1 with Dissolve(.5)
    $ renpy.pause(9999)





    jump sheet_23_energy

label sheet_23_haley:


    "[Name]" "{i}(Haley is the most magical creature I've seen...){/i}"
    show sc i_1_101_7 with my_dissolve
    "[Name]" "{i}(Sweet transparent panties.){/i}"
    show sc i_1_101_8 with my_dissolve
    "[Name]" "{i}(Oh yes! You're even a little wet...){/i}"
    show sc i_1_101_9 with my_dissolve
    "[Name]" "{i}(What a neat, tight holes you've got...){/i}"
label sheet_23_energy:
    scene expression '#fff' with Dissolve(1.5)

    scene sc i_1_192

    "[Name]" "{i}(I feel so much energy!){/i}"

    scene expression '#000' with Dissolve(1)

    $ renpy.pause(1, hard = True)

    jump sheet_24
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
