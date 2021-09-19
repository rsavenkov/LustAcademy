label restroom_stump_label:
    '[Name]' "{i}(Am I sure there's nothing I want to do before going downstairs?!){/i}"
    $ location_now = 'corridor'
    $ Event('RestroomStump',     'restroom',  'restroom_stump_label', True)
    jump change_location_label

label restroom_label:
    scene expression 'images/main_interface/locations/restroom.png' with Dissolve(.5)
    $ renpy.pause(9999999999)
    hide screen main_interface
    scene sc i_1_019_0 with Dissolve(.5)
    "[Name]" "Don, hi!"
    show sc i_1_019_0 with my_dissolve
    "[Name]" "How's it going, how's work?"
    show sc i_1_019 with my_dissolve
    "Don" "Get to the point, [Name]."
    show sc i_1_019 with my_dissolve
    "Don" "Don't waste my time."
    show sc i_1_019 with my_dissolve
    "Don" "Baseball's about to start, so hurry up and talk..."
    show sc i_1_019 with my_dissolve
    "Don" "What do you want?"
    show sc i_1_021 with my_dissolve
    "[Name]" "The thing is, Olivia came to see me..."
    show sc i_1_019 with my_dissolve
    "Don" "And?"
    show sc i_1_021 with my_dissolve
    "[Name]" "And? I'd like to discuss your rental idea..."
    show sc i_1_020 with my_dissolve
    "Don" "It's not an idea."
    show sc i_1_020 with my_dissolve
    "Don" "It's a fact you've been informed about."
    show sc i_1_020 with my_dissolve
    "Don" "If you don't want to study, then work."
    show sc i_1_022 with my_dissolve
    "Don" "And since you're 18 and working..."
    show sc i_1_022 with my_dissolve
    "Don" "Why should I sweat for another grown man?"
    show sc i_1_022 with my_dissolve
    "Don" "So pay up or get out."
    show sc i_1_022 with my_dissolve
    "Don" "Anything else?"
    show sc i_1_021 with my_dissolve
    "[Name]" "Hang on, Don. But I want to learn!"
    show sc i_1_019 with my_dissolve
    "Don" "I don't see you packing a suitcase full of books."
    show sc i_1_021 with my_dissolve
    "[Name]" "You know I was on an sport scholarship..."
    show sc i_1_019 with my_dissolve
    "Don" "So?"
    show sc i_1_019 with my_dissolve
    "[Name]" "If it wasn't for the injury, then..."
    show sc i_1_020_2 with my_dissolve
    "Don" "There are no \"If’s\" in history, boy."
    show sc i_1_020_2 with my_dissolve
    "Don" "You're 18. You don't study and you're sitting on my neck."
    show sc i_1_020_2 with my_dissolve
    "Don" "I'm tired of it, I won't allow it anymore."
    show sc i_1_020_2 with my_dissolve
    "Don" "These are the facts we have."
    scene sc i_1_019 with Dissolve(.5)
    menu:
        "Object politely" if True:
            $ pass
        "Object sharply" if True:
            jump restroom_menu_2_label
    scene sc i_1_021 with Dissolve(.5)
    "[Name]" "Let me try to change your mind!"
    show sc i_1_021 with my_dissolve
    "[Name]" "I'm not sitting idle at all!"
    show sc i_1_021 with my_dissolve
    "[Name]" "And I've been working all summer just to get an education."
    show sc i_1_021 with my_dissolve
    "[Name]" "To pay for college. You know what I mean?"
    show sc i_1_022 with my_dissolve
    "Don" "Okay. And?"
    show sc i_1_021 with my_dissolve
    "[Name]" "I was just working to pay for college."
    show sc i_1_021 with my_dissolve
    "[Name]" "And you want me to either study or pay you, right?"
    show sc i_1_022 with my_dissolve
    "Don" "You get the point."
    show sc i_1_021 with my_dissolve
    "[Name]" "But!"
    show sc i_1_021 with my_dissolve
    "[Name]" "If I have to pay your rent."
    show sc i_1_021 with my_dissolve
    "[Name]" "I'll never save up to go to collegel!"
    show sc i_1_019 with my_dissolve
    "[Name]" "And I'll have to keep paying you."
    show sc i_1_019 with my_dissolve
    "[Name]" "It's a vicious circle. You can't be serious... I mean..."
    show sc i_1_019 with my_dissolve
    "[Name]" "What do you think? I'm sure you can understand my situation..."
    show sc i_1_022 with my_dissolve
    "Don" "Of course I can. But I don't care."
    show sc i_1_020 with my_dissolve
    "Don" "It's time you learned how to be independent, kid."
    show sc i_1_020 with my_dissolve
    "Don" "Lesson one: you're 18 and your problems are your problems."
    show sc i_1_020_2 with my_dissolve
    "Don" "The world doesn't revolve around you."
    show sc i_1_020_2 with my_dissolve
    "Don" "Don't put your issues on me."
    show sc i_1_019_2 with my_dissolve
    "Don" "Pay your rent or find yourself a new place to live. What's it gonna be?"
    jump restroom_menu_3_label


label restroom_menu_2_label:
    scene sc i_1_019 with Dissolve(.5)
    "[Name]" "Are you sure you got all the facts straight, Don?!"
    show sc i_1_019 with my_dissolve
    "[Name]" "Maybe I should remind you that I could have been at university now."
    show sc i_1_021 with my_dissolve
    "[Name]" "If someone hadn't saved money on my rehabilitation."
    show sc i_1_021 with my_dissolve
    "[Name]" "I'm not saying you had to..."
    show sc i_1_019_2 with my_dissolve
    "Don" "That's exactly what you're saying right now!"
    show sc i_1_019_2 with my_dissolve
    "Don" "And I suggest you shut up and think about your tone."
    show sc i_1_020_2 with my_dissolve
    "Don" "Where would you be if it wasn't for me?"
    show sc i_1_020_2 with my_dissolve
    "Don" "Haven't I worked hard enough to give you food, clothes and an education?"
    show sc i_1_020_2 with my_dissolve
    "Don" "Do you have any idea how much your rehabilitation would have cost?"
    show sc i_1_021 with my_dissolve
    "[Name]" "No."
    show sc i_1_021 with my_dissolve
    "[Name]" "All I’m saying is that I didn’t \"choose\" not to go to university."
    show sc i_1_021 with my_dissolve
    "[Name]" "It's hard to keep your emotions in check when you're being slung in the face."
    show sc i_1_022 with my_dissolve
    "Don" "Oh, you poor thing!"
    show sc i_1_022 with my_dissolve
    "Don" "Is that what you were expecting to hear?"
    show sc i_1_019 with my_dissolve
    "[Name]" "No, I..."
    show sc i_1_021 with my_dissolve
    "Don" "You're 18! Surprise! Nobody owes you anything."
    show sc i_1_021 with my_dissolve
    "Don" "Certainly not me."
    show sc i_1_020_2 with my_dissolve
    "Don" "So stop whining and learn to be helpful."
    show sc i_1_019_2 with my_dissolve
    "[Name]" "I hear you."
    show sc i_1_020_2 with my_dissolve
    "Don" "So it's a deal, then?"
label restroom_menu_3_label:
    $ renpy.start_predict('images/video/1_023.webm')
    scene sc i_1_021 with Dissolve(.5)
    "[Name]" "I... I need to think."
    show sc i_1_021 with my_dissolve
    "[Name]" "I'm sorry, I'm gonna..."
    show sc i_1_022 with my_dissolve
    "Don" "Go on, get out of here."
    show sc i_1_022 with my_dissolve
    "Don" "And welcome to adulthood, boy!"
    show sc i_1_019_0 with my_dissolve
    "[Name]" "{i}(Shove your \"welcome to adulthood\" up your ass.){/i}"
    show sc i_1_019_0 with my_dissolve
    "[Name]" "{i}(Fucking hypocrite.){/i}"
    show sc i_1_019_0 with my_dissolve
    "[Name]" "{i}(I'd like to see how you'd behave get Ashley hurt, not me.){/i}"
    $ location_now = 'kitchen'
    scene expression '#000' with Dissolve(1)


    jump kitchen_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
