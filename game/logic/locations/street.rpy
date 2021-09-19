screen street_door():
    imagebutton:
        idle '#0000'
        hover '#0000'
        focus_mask True
        action Return()
label street_label:
    scene expression 'main_interface/locations/street.png' with Dissolve(.5)

    stop music fadeout 1.0
    play music_2 'audio/new/ambience/ambience_street_night.mp3' fadein 1.0
    $ renpy.pause(.5)
    scene sc i_1_028 with Dissolve(.5)
    $ renpy.pause(99999)
    scene sc i_1_029 with Dissolve(.5)
    "[Name]" "{i}(Sam was right. This letter is really addressed to me!){/i}"
    show sc i_1_029 with my_dissolve
    "[Name]" "{i}(Cordale Academy. Samantha studies there. Maybe they've just adressed it wrong?){/i}"
    show sc i_1_029 with my_dissolve
    "[Name]" "{i}(But that's my name, so I'll open the envelope and find out what's in there.){/i}"
    play sound 'audio/new/gameplay/Open_latter.mp3'
    scene sc i_1_030
    show expression Text(unicode(Name) + ' ' + unicode(Surname), font = 'fonts/name_sign.ttf', size = 18, color="#6b482c"):
        xpos 875
        ypos 388
    with Dissolve(.5)
    "[Name]" "Dear Mr. [Name] [Surname]."

    "[Name]" "You have been selected to take the entrance exam..."

    "[Name]" "...for an elite institution of higher education: the Cordale Academy of Magic and Wizardry."

    "[Name]" "To take the exam, you need to arrive at the central station at 12 pm, on August 31st."

    "[Name]" "Boarding the train to Cordale takes place before 12.30 pm. Do not miss!"

    "[Name]" "The exam will take place on the academy grounds, September 1st."

    "[Name]" "Please bring this letter and any personal belongings..."

    "[Name]" "...you may need in order to settle down at the Cordale Dorm."
    scene sc i_1_031 with Dissolve(.5)
    "[Name]" "{i}(The Academy of Magic and Wizardry? Ha ha, Sam. Very funny.){/i}"
    show sc i_1_031 with my_dissolve
    "[Name]" "{i}(Enough is enough, she won't be the third person mocking me today.){/i}"
    show sc i_1_031 with my_dissolve
    "[Name]" "{i}(I'll tell her that straight to her face!){/i}"


    $ location_now = 'kitchen'

    scene expression '#000' with Dissolve(1)

    $ renpy.pause(1, hard = True)


    jump kitchen_label_2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
