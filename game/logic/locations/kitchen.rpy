










label kitchen_label:

label i_1_023_test:
    scene expression 'images/main_interface/locations/kitchen.png' with Dissolve(1)
    $ renpy.pause(9999999999)




    python:
        try:
            
            pos_track_now = float(renpy.music.get_pos('music')) - 2
        except:
            pos_track_now = 0
    stop music fadeout 1.0
    play music 'audio/new/Music/background_music1.mp3' fadein 10.0
    play sound_2 'audio/new/Music/intro1.mp3' fadein 1.0

    scene sc i_1_023 with Dissolve(.5)
    $ renpy.pause(11.96, hard = True)



    $ renpy.pause(9999999999)




    scene sc i_1_026 with Dissolve(.5)
    "[Name]" "Sam! What are you doing here?"
    $ renpy.stop_predict()
    show sc i_1_026 with my_dissolve
    "Samantha" "Try to guess. You have one try!"
    show sc i_1_026 with my_dissolve
    "[Name]" "Hm..."
    show sc i_1_026 with my_dissolve
    "Samantha" "Tea, of course. Can I pour you one?"
    show sc i_1_025 with my_dissolve
    "[Name]" "No, thanks."
    show sc i_1_025 with my_dissolve
    "[Name]" "I'm not really in the mood for tea..."
    show sc i_1_025 with my_dissolve
    "Samantha" "What's going on? Did you have another fight with Olivia and Don?"
    show sc i_1_025 with my_dissolve
    "Samantha" "You want me to try and talk to them..."
    show sc i_1_026 with my_dissolve
    "[Name]" "Sam, you don't have to take care of me all the time!"
    show sc i_1_026 with my_dissolve
    "[Name]" "They just figured I was working my ass off for the fun of it."
    show sc i_1_026 with my_dissolve
    "[Name]" "And they offered to give them all the money in the form of rent."
    show sc i_1_025 with my_dissolve
    "Samantha" "Stop it with your jokes!"
    show sc i_1_025 with my_dissolve
    "Samantha" "You're... You're joking, right?"
    show sc i_1_026_2 with my_dissolve
    "Samantha" "I can't believe they'd do that to you! What's gotten into them?"
    show sc i_1_026_2 with my_dissolve
    "[Name]" "Don's punishing me for not going to university."
    show sc i_1_026_2 with my_dissolve
    "[Name]" "Teaching me to be independent."
    show sc i_1_026_3 with my_dissolve
    "Samantha" "Wait a minute. You almost saved up for college, what do you care?"
    show sc i_1_026_3 with my_dissolve
    "[Name]" "They're going to rob me blind with their new business plan."
    show sc i_1_026_4 with my_dissolve
    "[Name]" "There's not enough money for both rent and an education."
    show sc i_1_026_5 with my_dissolve
    "Samantha" "Did you tell them that? I'm sure Dad will understand."
    show sc i_1_026_4 with my_dissolve
    "[Name]" "{i}(What kind of a jerk is he? I doubt it.){/i}"
    show sc i_1_026_4 with my_dissolve
    "[Name]" "I dunno. To this moment we failed to come to any undestranding."
    show sc i_1_026_5 with my_dissolve
    "Samantha" "I almost forgot! Did you check our mailbox today?"
    show sc i_1_026_4 with my_dissolve
    "[Name]" "Why would I check it? I don't expect letters from anyone."
    show sc i_1_026_6 with my_dissolve
    "Samantha" "I'm pretty sure I saw an envelope for you there."
    show sc i_1_026_4 with my_dissolve
    "[Name]" "That's something new. You've intrigued me!"
    show sc i_1_026_4 with my_dissolve
    "[Name]" "I'll swing by a mailbox, see you later!"
    $ Event('StreetStnd',       'street',    'street_label')
    $ location_now = 'street'
    scene expression '#000' with Dissolve(1)
    jump street_label


label kitchen_label_2:
    stop music_2 fadeout 1.0
    play music 'audio/new/Music/background_music1.mp3' fadein 1.0
    scene sc i_1_032 with Dissolve(1)
    $ renpy.pause(9999999)
    scene sc i_1_034 with Dissolve(.5)
    "Olivia" "Heard you talked to Don."
    show sc i_1_034 with my_dissolve
    "Olivia" "How'd it go?"
    show sc i_1_032 with my_dissolve
    "[Name]" "We're not done talking yet."
    show sc i_1_032 with my_dissolve
    "[Name]" "Do you know where Samantha went? I need to find her."
    show sc i_1_036 with my_dissolve
    "Olivia" "Take your time, [Name]."
    show sc i_1_036 with my_dissolve
    "Olivia" "Let me take a look at that letter you're holding in your hands."
    show sc i_1_037 with my_dissolve
    "[Name]" "But there's nothing interesting here."
    show sc i_1_037 with my_dissolve
    "[Name]" "It's just a stupid prank from Samantha."
    show sc i_1_038 with my_dissolve
    "Olivia" "I see you've already read it..."
    show sc i_1_039 with my_dissolve
    "[Name]" "Yeah. It's addressed to me."
    show sc i_1_038 with my_dissolve
    "Olivia" "How long ago did it come?"
    show sc i_1_039 with my_dissolve
    "[Name]" "I have no idea. I just got it out of the mailbox."
    show sc i_1_040 with my_dissolve
    "Olivia" "I need to talk to Don right away. I'll hold on to it for now."
    play sound 'audio/new/gameplay/footsteps_on_stairs.mp3'
    show sc i_1_041 with my_dissolve
    "[Name]" "{i}(Olivia's been acting weird lately. She should stop drinking.){/i}"
    show sc i_1_041_2 with my_dissolve
    "[Name]" "{i}(I wonder what made her so crazy about that stupid letter?){/i}"
    show sc i_1_041_3 with my_dissolve
    stop sound fadeout 1.0
    "[Name]" "{i}(Oh my! At least I've got something of this letter already.){/i}"
    show sc i_1_042 with my_dissolve
    "[Name]" "{i}(I should follow her and try to listen in on what are they talking about.){/i}"
    scene expression '#000' with Dissolve(1)
    $ location_now = 'corridor'
    hide screen main_interface

    jump corridor_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
