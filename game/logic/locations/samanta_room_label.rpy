label samanta_room_label:
    hide screen main_interface
    $ location_now = 'corridor'
    scene expression 'images/main_interface/locations/'+ str(location_now) + '.png'
    '[Name]' "{i}(Samantha's clearly not at her place. I wonder where she went.){/i}"
    $ Event('SamantaRoomStnd', 'samanta_room', 'samanta_room_label', True)
    jump change_location_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
