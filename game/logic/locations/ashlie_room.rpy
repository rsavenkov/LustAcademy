label ashlie_room_label:



    $ Event('AshlieRoomStnd',        'ashlie_room',  'ashlie_room_label', True)

    if hasattr(store, 'ashlie_look'):
        "[gg]" "{i}(Ashley's probably in the middle of the training session. I don't want to bother her.){i}"

        $ location_now = 'corridor'
        jump change_location_label


    "[Name]" "{i}(Ashley's usually in training at this time of day.){/i}"
    "[Name]" "{i}(I won't distract her.){/i}"
    "[Name]" "{i}(Although I could sneak a peek...){/i}"








    scene expression 'images/main_interface/locations/'+ str(location_now) + '.png'

    with Dissolve(.3)


    menu:
        "Sneak a peek" if not hasattr(store, 'ashlie_look'):

            scene expression '#000' with Dissolve(1)
            $ renpy.pause(1)


            $ ashlie_look = True
            stop music fadeout 1.0
            play music_2 'audio/new/Music/training_music2.mp3' fadein 1.0
            scene sc i_1_014 with Dissolve(.5)
            $ renpy.pause(5.16, hard = True)


            $ renpy.pause(999999)



            scene expression 'prologue/1_015.webp' with Dissolve(.5)
            "[Name]" "{i}(Oh...){/i}"
            "[Name]" "{i}(Ashley in her finest - so graceful!){/i}"
            "[Name]" "{i}(I could watch this forever...){/i}"
            scene expression 'prologue/1_014.webp' with Dissolve(.5)
            "[Name]" "{i}(Alas, Don won't wait for so long.){/i}"
            "[Name]" "{i}(I'd better go.){/i}"

            $ location_now = 'corridor'
            $ events['RestroomStump'].complete = True
            $ events['KitchenStump'].complete = True

            $ Event('RestroomStnd',      'restroom',   'restroom_label')

            $ Event('KitchenStnd',       'kitchen',    'kitchen_label')
            stop music_2 fadeout 1.0
            play music 'audio/new/Music/background_music1.mp3'  fadein 1.0
            if persistent.from_gallery:

                scene expression '#000' with Dissolve(1)
                $ renpy.full_restart()
            jump change_location_label
        "Walk away" if True:

            hide screen main_interface
            $ location_now = 'corridor'
            $ events['RestroomStump'].complete = True
            $ events['KitchenStump'].complete = True
            $ ashlie_look = True
            $ Event('RestroomStnd',      'restroom',   'restroom_label')

            $ Event('KitchenStnd',       'kitchen',    'kitchen_label')
            "[Name]" "{i}(Don's probably waiting for me in the living room.){/i}"
            if persistent.from_gallery:

                scene expression '#000' with Dissolve(1)
                $ renpy.full_restart()
            jump change_location_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
