screen empty_screen:
    $ pass
label corridor_label:
    scene sc i_0_002 with Dissolve(.5)
    play sound ["<silence .25>",'audio/new/gameplay/Sex_voice1.mp3']
    "Ashley" "Ahh… Uhm… Uh…"

    show sc i_0_002 with my_dissolve
    "[Name]" "{i}(Hmm. Looks like these sounds are coming from Ashley's room!){/i}"
    show sc i_0_002 with my_dissolve

    "[Name]" "{i}(Maybe she has twisted her ancle. Should I check out?){/i}"





    scene sc i_0_004 with Dissolve(.5)

    menu:
        "Sneak a peek" if True:
            "[Name]" "{i}(Just to be sure she's okay.){/i}"
        "Walk away" if True:

            "[Name]" "{i}(It's none of my business.){/i}"
            "[Name]" "{i}(I wonder how Olivia missed that moaning though.){/i}"
            "[Name]" "{i}(Why was she sho pshyched about that prank letter?){/i}"
            "[Name]" "{i}(I need to hurry up if I want to find out.){/i}"
            if persistent.from_gallery:

                scene expression '#000' with Dissolve(1)
                $ renpy.full_restart()
            jump i_need_to_hurry_if





label ashlie_room_label_2:

    if persistent.from_gallery:
        $ renpy.block_rollback()

    $ renpy.start_predict('images/video/1_043_*.webm')



    stop music fadeout 1.0
    scene expression '#000' with Dissolve(1)
    play music_2 'audio/new/Music/Pina Colada.mp3' fadein 1.0
    $ renpy.pause(1, hard = True)
    scene sc i_1_043_1 with Dissolve(1)
    menu:
        "Jackpot" if True:
            $ pass
            $ i_1_043_1_var = True
            $ unlock_gallery('images/ero/1.png')
        "Leave" if True:
            if persistent.from_gallery:

                scene expression '#000' with Dissolve(1)
                $ renpy.full_restart()
            jump before_i_need_to_hurry_if



    "[Name]" "{i}(Jackpot!){/i}"

    play sound 'audio/new/gameplay/Sex_voice1.mp3'
    "Ashley" "Um…"

    "[Name]" "{i}(Wow, Ashley is so...){/i}"

    "Ashley" "Uhh…"

    scene sc i_1_043_2 with Dissolve(.5)
    $ renpy.pause(99999)
    "[Name]" "{i}(Mature...){/i}"
    play sound 'audio/new/gameplay/Sex_voice4.mp3'

    "Ashley" "Um… umh…"

    "Ashley" "Ahh… Uhm…"

    scene sc i_1_043_3 with Dissolve(.5)
    $ renpy.pause(99999)
    "[Name]" "{i}(What a beautiful sight!){/i}"

    "[Name]" "{i}(She tries so hard to keep her moans silent.){/i}"

    play sound 'audio/new/gameplay/Sex_voice2.mp3'
    "Ashley" "Ah…"

    scene sc i_1_043_2 with Dissolve(.5)
    $ renpy.pause(99999)
    "[Name]" "{i}(It makes it even sexier when she fails to do so!){/i}"

    "Ashley" "Ah… ah…"

    "[Name]" "{i}(Poor little thing is so horny...){/i}"

    scene sc i_1_043_3 with Dissolve(.5)
    $ renpy.pause(99999)
    play sound 'audio/new/gameplay/Sex_voice3.mp3'
    "Ashley" "Um… umh… ah…"

    "[Name]" "{i}(If only I knew you needed assistance with your \"training\" sessions, Ashley.){/i}"

    "[Name]" "{i}(Maybe next time...){/i}"

    "Ashley" "Ah… ah… ah…"

    "[Name]" "{i}(She's almost there...){/i}"

    play sound 'audio/new/gameplay/Sex_voice2.mp3'
    scene sc i_1_043_1 with Dissolve(.7)
    $ renpy.pause(99999)
    "Ashley" "Ah… A-Ah…"

    "Ashley" "Mmhm... uh... yeah..."

    scene sc i_1_043_2 with Dissolve(.7)
    $ renpy.pause(99999)
    "[Name]" "{i}(Good job, baby!){/i}"

    "[Name]" "{i}(Next time I'll show you an exercise for two!){/i}"
    if persistent.from_gallery:

        scene expression '#000' with Dissolve(1)
        $ renpy.full_restart()
    scene sc i_1_043_1 with Dissolve(.7)
    $ renpy.pause(99999)
    "[Name]" "{i}(Oh shit, I completely forgot about Olivia.){/i}"

    "[Name]" "{i}(I need to hurry if I want to catch anything.){/i}"
    jump i_need_to_hurry_if
label before_i_need_to_hurry_if:
    "[Name]" "{i}(Woah!){/i}"
    "[Name]" "{i}(Alright, I shouldn’t be seeing it.){/i}"
    "[Name]" "{i}(I need to hurry up if I want to find out why was Olivia so pshyched!){/i}"
label i_need_to_hurry_if:
    $ renpy.stop_predict()
    $ renpy.start_predict('images/video/1_061_a*.webm')




    stop music_2 fadeout 1.0


    scene expression '#000' with Dissolve(1)
    play music 'audio/new/Music/background_music1.mp3' fadein 1.0
    $ renpy.pause(1, hard = True)
    scene sc i_1_044 with Dissolve(1)
    "Olivia" "Disaster! This is a disaster!"
    show sc i_1_044 with my_dissolve
    "Olivia" "It’s hard enough to deal with that boy! And now \"this\"!"
    show sc i_1_044 with my_dissolve
    "Olivia" "Doesn't it bother you, Don? Don't you understand what kind of situation we are in?"
    show sc i_1_045 with my_dissolve
    "Don" "Calm down, Olivia. Why do you think this is bad news?"
    show sc i_1_045_2 with my_dissolve
    "Olivia" "Are you not listening to me? He got a letter! This means that he is one of {i}\"them\"!{/i}"
    show sc i_1_045_2 with my_dissolve
    "Olivia" "How can I make him obey now?{w} He was contradicting every word I said before, but now..."
    show sc i_1_045 with my_dissolve
    "Don" "Now he's not your problem."
    show sc i_1_046 with my_dissolve
    "Olivia" "What do you mean by that?"
    show sc i_1_047 with my_dissolve
    "Don" "What I'm trying to say is that this bastard isn't our headache anymore!"
    show sc i_1_047 with my_dissolve
    "Don" "We need to help him pack his bags and pray that they will accept him."
    show sc i_1_046 with my_dissolve
    "Olivia" "I don't understand you, Don."
    show sc i_1_047 with my_dissolve
    "Don" "If he gets accepted into the academy, he will be out of our home at least until the end of the year."
    show sc i_1_047 with my_dissolve
    "Don" "And in the long term, he may finally find his place in life and get off my neck."
    show sc i_1_047 with my_dissolve
    "Don" "Just be nicer to him now. Just in case…"
    show sc i_1_048 with my_dissolve
    "Olivia" "Ah, Don! You're so clever!"


    scene sc i_1_049 with Dissolve(.5)
    $ renpy.pause(9999)
    "[Name]" "{i}(Hm, I wonder why Olivia got so bothered with that stupid letter...){/i}"
    show sc i_1_049 with my_dissolve
    "Samantha" "And what are you doing here, exactly?"
    play sound 'audio/new/gameplay/gg_fall.mp3'
    show sc i_1_050 with my_dissolve
    "[Name]" "Fuck!"


label i_1_051_test:


    python:
        try:
            
            pos_track_now = float(renpy.music.get_pos('music')) - 2
        except:
            pos_track_now = 0
    stop music fadeout 1.0
    scene sc i_1_051 with Dissolve(.5)
    play music 'audio/new/Music/background_music1.mp3' fadein 10.0
    play sound_2 'audio/new/Music/intro1.mp3' fadein 1.0

    $ renpy.pause(10.66, hard = True)
    $ renpy.pause(999999999999)





    "[Name]" "Samantha! You can't scare people like that!"
    show sc i_1_053 with my_dissolve
    "Samantha" "The last time I checked, you can't spy on people either. "
    show sc i_1_053 with my_dissolve
    "Samantha" "Or did you not know that?"
    show sc i_1_054 with my_dissolve
    "[Name]" "Of course I know, but I have a good reason.{w} You won't rat me out to Don, will you? I beg you!"
    show sc i_1_055 with my_dissolve
    "Samantha" "Didn't even cross my mind. I hope you don't make eavesdropping a habit."
    show sc i_1_056 with my_dissolve
    "Samantha" "Did you already get the letter I was telling you about?"
    show sc i_1_057 with my_dissolve
    "[Name]" "Yes, but Olivia confiscated it and ran to Don. "
    show sc i_1_057 with my_dissolve
    "[Name]" "I'm just trying to understand what they are talking about…"
    show sc i_1_056 with my_dissolve
    "Samantha" "And you didn't have time to read it?"
    show sc i_1_057 with my_dissolve
    "[Name]" "I read it. And at first I was sure it was a stupid prank of yours."
    show sc i_1_057 with my_dissolve
    "[Name]" "But your parents reacted rather strangely."
    show sc i_1_055 with my_dissolve
    "Samantha" "Believe me, I wouldn't go through such a hassle for the sake of some kind of prank."
    show sc i_1_054 with my_dissolve
    "[Name]" "How would you react if you got an invitation to a school of wizardry?"
    show sc i_1_056 with my_dissolve
    "Samantha" "I understand you, I experienced it myself last year."
    show sc i_1_057 with my_dissolve
    "[Name]" "Hmm, I remember something like that. It wasn't a prank then?"
    show sc i_1_056 with my_dissolve
    "Samantha" "No, but I couldn't tell you about it."
    show sc i_1_056 with my_dissolve
    "Samantha" "It isn't customary to discuss our secrets outside the Academy."
    show sc i_1_057 with my_dissolve
    "[Name]" "Secret school of magic? Are you studying to become an illusionist there?"
    show sc i_1_056 with my_dissolve
    "Samantha" "No, not a illusionist. This is exactly what the letter says it is."
    show sc i_1_054 with my_dissolve
    "[Name]" "There aren't many details in it. What is Cordale? And what does this magic look like?"
    show sc i_1_056 with my_dissolve
    "Samantha" "You have a lot of questions but I cannot answer them..."
    show sc i_1_057 with my_dissolve
    "[Name]" "But why? What kind of mystery is this?"
    show sc i_1_056 with my_dissolve
    "Samantha" "It is strictly forbidden for all students to talk about the Academy outside of it."
    show sc i_1_057 with my_dissolve
    "[Name]" "Is it really that strict?"
    show sc i_1_057 with my_dissolve
    "Samantha" "If I blabber, they will turn me into a pig.{w} By the way, they'll have to turn you into one too..."
    show sc i_1_055 with my_dissolve
    "Samantha" "Just kidding! I will simply be expelled and the path to magic will be forever closed to me."
    show sc i_1_054 with my_dissolve
    "[Name]" "Wow, that sucks... Okay! Let's say I believe you. What is the plan?"
    show sc i_1_056 with my_dissolve
    "Samantha" "To be on time for the exam, you need to be at the train station tomorrow at noon..."
    show sc i_1_057 with my_dissolve
    "[Name]" "Woah. That's right, August 31st is tomorrow..."
    show sc i_1_056 with my_dissolve
    "Samantha" "That's what I'm saying! Pack your bags and go to bed, I'll wake you up in the morning."
    show sc i_1_057 with my_dissolve
    "[Name]" "Sounds reasonable. Until tomorrow then!"
    show sc i_1_058 with my_dissolve
    "[Name]" "{i}(I can't believe I'm being fooled by this...){/i}"
    show sc i_1_058 with my_dissolve
    "[Name]" "{i}(If this is a prank, then it is already going too far.){/i}"
    show sc i_1_058 with my_dissolve
    "[Name]" "Sam!"
    play sound 'audio/new/gameplay/Door_open1.mp3'
    show sc i_1_059 with my_dissolve
    "Samantha" "What, [Name]?"
    show sc i_1_059 with my_dissolve
    "[Name]" "Swear you're not messing with me."
    show sc i_1_060 with my_dissolve
    "Samantha" "I swear."
    show sc i_1_060 with my_dissolve
    "[Name]" "Okay. Good night, Samantha."
    scene expression 'images/main_interface/locations/corridor.png' with Dissolve(.5)
    "[Name]" "{i}(I wonder what's going on with Olivia and Don.){/i}"

    "[Name]" "{i}(I know I've promised Sam to stop eavesdropping...){/i}"
    "[Name]" "{i}(...but I don't want to miss anything!){/i}"
    "[Name]" "{i}(What should I do?){/i}"

    scene sc i_0_005 with Dissolve(.5)
    menu:
        "Sneak a peek" if True:
            "[Name]" "{i}(I guess one last time does not count!){/i}"
        "Go to your room" if True:

            "[Name]" "{i}(I'm a man of my word. I'd better go.){/i}"
            jump go_to_you_room_ep1
    scene expression '#000' with Dissolve(1)
    $ renpy.pause(1, hard=True)
    stop music fadeout 1.0
    play music_2 'audio/new/Music/sex_music.mp3' fadein 1.0

    if persistent.from_gallery:
        $ renpy.block_rollback()
    scene sc i_1_061 with Dissolve(1)
    menu:
        "Continue watching" if True:
            $ i_1_061_a1_var = True
            $ pass
            $ unlock_gallery('images/ero/2.png')
        "Leave" if True:
            if persistent.from_gallery:

                scene expression '#000' with Dissolve(1)
                $ renpy.full_restart()
            '[Name]' "{i}(Nah, I dont want to see this.){/i}"
            stop music_2 fadeout 1.0
            play music 'audio/new/Music/background_music1.mp3' fadein 1.0

            jump go_to_you_room_ep1
    "Don" "It's time to use your head as it was intented too!"
    show sc i_1_061_2 with my_dissolve
    "Don" "Because your chattering is giving me headache."
    show sc i_1_061_3 with my_dissolve
    "Olivia" "I'm..."

    "Don" "What are you saying? I can't hear you!"
    scene sc i_1_061_a1 with Dissolve(.5)
    $ renpy.pause(9999)

    "Olivia" "Mhghm..."
    scene sc i_1_061_a2 with Dissolve(.5)
    $ renpy.pause(9999)
    "Don" "Yeah bitch, do you say that you like the taste of my cock?"
    scene sc i_1_061_a3 with Dissolve(.5)
    $ renpy.pause(9999)
    "Olivia" "Mhghm..."
    show sc i_1_061_5 with my_dissolve
    "Don" "That's not all!"
    show sc i_1_061_6 with my_dissolve
    "Don" "Open your mouth wider!"

    scene expression 'images/video/1_061_a4_a.webp' with Dissolve(.5)
    "Don" "That's it! Eat it!"
    scene expression '#000' with Dissolve(.5)
    scene sc i_1_061_a4 with Dissolve(1)
    $ renpy.pause(9999)

    scene sc i_1_061_a5 with Dissolve(.5)
    $ renpy.pause(9999)
    "Don" "Yes! Yes!"
    scene sc i_1_061_a6 with Dissolve(.5)
    $ renpy.pause(9999)
    scene sc i_1_061_8 with Dissolve(.5)
    "Don" "Show me your boobs! Oh yeah!"
    scene sc i_1_061_9 with Dissolve(.5)
    $ renpy.pause(.5)
    scene sc i_1_061_10 with Dissolve(.5)
    $ renpy.pause(.5)
    scene sc i_1_061_11 with Dissolve(.5)
    $ renpy.pause(.5)
    scene sc i_1_061_12 with Dissolve(.5)
    $ renpy.pause(999999999)
    scene sc i_1_061_13 with Dissolve(.5)
    "[Name]" "{i}(Hmm. Olivia looks unsatisfied.){/i}"
    show sc i_1_061_13 with my_dissolve
    "Don" "I'm going to take a shower, clean yourself up."
    show sc i_1_061_13 with my_dissolve
    "[Name]" "{i}(I'd better go.){/i}"
    if persistent.from_gallery:

        scene expression '#000' with Dissolve(1)
        $ renpy.full_restart()
label go_to_you_room_ep1:
    stop music_2 fadeout 1.0
    play music 'audio/new/Music/background_music1.mp3' fadein 1.0
    scene expression '#000' with Dissolve(1)
    $ renpy.pause(1, hard = True)
    scene sc i_1_062 with Dissolve(1)
    $ renpy.pause(99999999)
    "[Name]" "{i}(I can't sleep...){/i}"
    show sc i_1_062 with my_dissolve
    "[Name]" "{i}(It's been a very strange day...){/i}"
    show sc i_1_063 with my_dissolve
    "[Name]" "{i}(I should check what the customer wrote about the photos...){/i}"
    show sc i_1_063 with my_dissolve
    "[Name]" "{i}(Though somehow that's the least of my worries right now.){/i}"
    show sc i_1_062 with my_dissolve
    "[Name]" "{i}(Is all of this for real?){/i}"
    show sc i_1_062 with my_dissolve
    "[Name]" "{i}(Cordale Academy of Magic and Wizardry... Huh!){/i}"
    show sc i_1_062 with my_dissolve
    "[Name]" "{i}(What kind of fool came up with that name?){/i}"
    show sc i_1_062 with my_dissolve
    "[Name]" "{i}(I can't wait to see Sam laughing at me in the morning.){/i}"
    show sc i_1_062 with my_dissolve
    "[Name]" "{i}(When I show up in the living room with my suitcase.){/i}"
    show sc i_1_062 with my_dissolve
    "[Name]" "{i}(Even though she swore to me It's not a prank...){/i}"

    $ renpy.stop_predict()




label morning_2:


    scene expression '#000' with Dissolve(2)


    play sound 'audio/Door_Knock.mp3'


    "Knock-Knock" ""
    scene sc i_1_064 with Dissolve(2)
    $ renpy.pause(9999)

    "[Name]" "Good morning, [Name] Junior! "
    show sc i_1_064 with my_dissolve
    "[Name]" "You seem to be enjoying our dream, too."
    show sc i_1_064_2 with my_dissolve
    "[Name]" "{i}(It's going to be a sunny day...){/i}"
    show sc i_1_064_2 with my_dissolve
    "[Name]" "{i}(It's a good luck!){/i}"
    show sc i_1_064_2 with my_dissolve
    "[Name]" "{i}(Gotta get ready if I'm gonna play along with Samantha's joke.){/i}"
    play sound 'audio/new/gameplay/Door_open1.mp3'
    show sc i_1_065 with my_dissolve
    "Samantha" "No thanks, I've already had breakfast, Ma."
    show sc i_1_065_2 with my_dissolve
    "Samantha" "We should be getting ready now. I'm just on my way to wake up [Name]!"
    show sc i_1_065_2 with my_dissolve
    "Samantha" "Don't worry, I won't miss the train because of him. I've got everything under control."
    scene sc i_1_066 with vpunch
    $ renpy.pause(99999)
    scene sc i_1_066_2 with Dissolve(.5)
    $ renpy.pause(99999)
    "[Name]" "Sam, where are your manners? Who taught you to barge in without knocking?"
    "Samantha" "But I... Would you... Cover him up!"
    scene sc i_1_067 with Dissolve(.5)
    $ renpy.pause(99999)

    show sc i_1_067 with my_dissolve
    "[Name]" "Do we have to go now?"
    show sc i_1_067 with my_dissolve
    "Samantha" "..."
    show sc i_1_067 with my_dissolve
    "[Name]" "Sam!"
    show sc i_1_068 with my_dissolve
    "Samantha" "..."
    show sc i_1_068 with my_dissolve
    "[Name]" "Samantha!"
    scene sc i_1_069_0 with Dissolve(.5)
    $ renpy.pause(9999)

    scene sc i_1_069 with Dissolve(.5)
    "Samantha" "Admit it, did you do it on purpose?"
    show sc i_1_069 with my_dissolve
    "[Name]" "I did what on purpose? Woke up in your bed?"
    show sc i_1_069 with my_dissolve
    "Samantha" "You met me undressed on purpose."
    show sc i_1_069 with my_dissolve
    "[Name]" "You broke in so fast, I didn't have time to think."
    show sc i_1_069 with my_dissolve
    "[Name]" "By the way, your cheeks look nice with a blush on them!"
    show sc i_1_070 with my_dissolve
    "Samantha" "Jerk! I got your invitation from my parents, because without it they wouldn't let you on the train."
    show sc i_1_070 with my_dissolve
    "Samantha" "Hurry up and get ready, we don't have time for this."
    show sc i_1_071 with my_dissolve
    "Samantha" "I've already called a taxi. I'll meet you downstairs with your things in ten minutes."

    show sc i_1_071_2 with my_dissolve
    "[Name]" "{i}(Is it just me, or could she not take her eyes off my cock?){/i}"
    show sc i_1_071_2 with my_dissolve
    "[Name]" "{i}(I'd better hurry...){/i}"




    stop music fadeout 3.0

    scene expression '#000' with Dissolve(1)
    $ renpy.pause(1, hard = True)
    scene sc i_1_072 with Dissolve(1)
    play music_2 'audio/new/ambience/ambience_platform1.mp3' fadein 2.0
    $ renpy.pause(1, hard = True)


    "[Name]" "{i}(Well. We're at the train station.){/i}"
    show sc i_1_072 with my_dissolve
    "[Name]" "{i}(Still can't believe it's true...){/i}"
    show sc i_1_072 with my_dissolve
    "[Name]" "{i}(Where did Sam go?){/i}"
    show sc i_1_072_2 with my_dissolve
    "Samantha" "Oh, my God! Audrey! Stay here, I'll introduce you!"
    show sc i_1_072_2 with my_dissolve
    "[Name]" "{i}(Who's that?){/i}"
    show sc i_1_072_3 with my_dissolve
    "[Name]" "{i}(Samantha is so excited to meet her.){/i}"
    show sc i_1_072_3 with my_dissolve
    "[Name]" "{i}(I've never seen her like this with any of her other girlfriends.){/i}"
    show sc i_1_072_4 with my_dissolve
    "[Name]" "{i}(Yeah, and this girl... Hot...){/i}"
    show sc i_1_072_4 with my_dissolve
    "[Name]" "{i}(But there's something wrong with her.){/i}"
label i_1_072_5_test:
    python:
        try:
            
            pos_track_now = float(renpy.music.get_pos('music_2')) - 2
        except:
            pos_track_now = 0
    stop music_2 fadeout 1.0
    play sound_2 'audio/new/Music/intro1.mp3' fadein 1.0

    scene sc i_1_072_5 with Dissolve(.5)
    $ renpy.pause(7, hard = True)
    play music_2  '<from 13 to 54>audio/new/ambience/ambience_platform1.mp3' fadein 1.0
    $ renpy.pause(3.13, hard = True)
    $ renpy.pause(9999)


    scene sc i_1_072_7 with Dissolve(.5)
    "Audrey" "Yo. Sam, have you hooked up yet?"
    show sc i_1_072_6 with my_dissolve
    "[Name]" "Um, ahem, actually..."
    show sc i_1_072_6 with my_dissolve
    "Samantha" "She's just kidding!"
    show sc i_1_072_6 with my_dissolve
    "Samantha" "Audrey, this is my friend [Name]. Remember I told you about him?"
    show sc i_1_072_6 with my_dissolve
    "Samantha" "[Name], this is Audrey. My classmate and best friend."
    show sc i_1_072_6 with my_dissolve
    "[Name]" "Nice to meet you."
    show sc i_1_072_7 with my_dissolve
    "Audrey" "Whatever."
    show sc i_1_072_7 with my_dissolve
    "Audrey" "You're cute."
    show sc i_1_072_8 with my_dissolve
    "Audrey" "But you're cuter."

    show sc i_1_072_81 with my_dissolve



    "[Name]" "{i}(Strange.){/i}"
    "[Name]" "{i}(Why do I feel this troubling vibe around her?){/i}"
    "[Name]" "Thanks.{w} I guess."



    show sc i_1_072_8 with my_dissolve
    "Audrey" "I'll get us a compartment, babe."
    show sc i_1_072_8 with my_dissolve
    "Audrey" "Don't hang out here too long."
    show sc i_1_072_10 with my_dissolve
    "[Name]" "And this... is your best friend?"
    show sc i_1_072_10 with my_dissolve
    "Samantha" "Oh, shut up."











    show sc i_1_072_9 with my_dissolve
    "Samantha" "She just doesn't know how to make a first impression."
    show sc i_1_072_9 with my_dissolve
    "Samantha" "You need to get to know each other better!"
    stop music_2 fadeout 15.0
    play music 'audio/new/Music/background_music1.mp3' fadein 1.0 
    show sc i_1_073 with my_dissolve
    "[Name]" "Well, we've got a whole trip to do that..."
    show sc i_1_073 with my_dissolve
    "[Name]" "Let's go, show me where the compartment is."
    show sc i_1_075 with my_dissolve
    "Samantha" "Hold your horses, buddy!"
    show sc i_1_075 with my_dissolve
    "Samantha" "It's not that simple."
    show sc i_1_075 with my_dissolve
    "[Name]" "What's not so simple?"
    show sc i_1_074 with my_dissolve
    "Samantha" "See, there's a separate compartment for freshmen."
    show sc i_1_074 with my_dissolve
    "Samantha" "And I can't go in there."
    show sc i_1_074 with my_dissolve
    "Samantha" "And you can't join us."
    show sc i_1_074 with my_dissolve
    "Samantha" "It's academy policy."
    show sc i_1_077 with my_dissolve
    "[Name]" "That's ridiculous."
    show sc i_1_077 with my_dissolve
    "[Name]" "Why can't I go with you?"
    show sc i_1_079 with my_dissolve
    "Samantha" "So the sophomores don't tell you the secret of the entrance exam, of course."
    show sc i_1_079 with my_dissolve
    "[Name]" "The entrance ex..."
    show sc i_1_079 with my_dissolve
    "[Name]" "The entrance exam?!"
    show sc i_1_079_1 with my_dissolve
    "Samantha" "Ah-ha-ha!"
    show sc i_1_079_1 with my_dissolve
    "Samantha" "I was expecting that reaction from you."
    show sc i_1_079 with my_dissolve
    "[Name]" "This is funny for you?!"
    show sc i_1_079 with my_dissolve
    "[Name]" "How am I supposed to pass the school of magic entrance exam, Sam?"
    show sc i_1_079 with my_dissolve
    "[Name]" "I don't even know any card tricks..."
    show sc i_1_074 with my_dissolve
    "Samantha" "Relax, it's no big deal..."
    show sc i_1_075 with my_dissolve
    "Samantha" "But that's all I'm gonna tell you."
    show sc i_1_075 with my_dissolve
    "[Name]" "Samantha. Oh, please."
    show sc i_1_075 with my_dissolve
    "[Name]" "I'm sure you want me to pass and study with you."
    show sc i_1_074 with my_dissolve
    "[Name]" "You know how much I need this chance right now..."
    show sc i_1_074 with my_dissolve
    "[Name]" "Help me not to lose it!"
    show sc i_1_077 with my_dissolve
    "Samantha" "Shit, I can't resist you, you know that!"
    show sc i_1_077 with my_dissolve
    "Samantha" "Give me a goodbye kiss on the cheek."
    show sc i_1_077 with my_dissolve
    "[Name]" "What?"
    show sc i_1_077 with my_dissolve
    "Samantha" "Do as I say."
    show sc i_1_078 with my_dissolve
    "[Name]" "Okay."
    show sc i_1_078 with my_dissolve
    "Samantha" "I'll meet you on the platform when you arrive."
    show sc i_1_078 with my_dissolve
    "Samantha" "We'll have about ten minutes before they come to meet you."
    show sc i_1_078 with my_dissolve
    "Samantha" "So don't waste any time."
    show sc i_1_078 with my_dissolve
    "[Name]" "You got it."
    show sc i_1_076 with my_dissolve
    "Samantha" "Oh, look, I think I see your compartment."
    show sc i_1_076 with my_dissolve
    "[Name]" "Where?"
    show sc i_1_076 with my_dissolve
    "Samantha" "The second one behind you. It was listed in the letter."
    show sc i_1_076 with my_dissolve
    "[Name]" "That's great. What would I do without you, Sam?"
    show sc i_1_076_1 with my_dissolve
    "Samantha" "You'd have learned how to read letters yourself?"
    show sc i_1_076_1 with my_dissolve
    "Samantha" "You... You can read, can't you?"
    show sc i_1_076 with my_dissolve
    "[Name]" "Very funny."
    show sc i_1_074 with my_dissolve
    "Samantha" "Go be yourself. Such a charmer will easily make friends."
    show sc i_1_074 with my_dissolve
    "[Name]" "{i}(Friends like yours?){/i}"

    show sc i_1_074 with my_dissolve

    "[Name]" "Yeah, I could use some friends."

    show sc i_1_076 with my_dissolve

    "Samantha" "See you on the other side!"


    show sc i_1_076 with my_dissolve

    "[Name]" "Go on, then. Run to your girlfriend!"

    stop music fadeout 4.0
    play music_2 'audio/new/ambience/ambience_platform1.mp3' fadein 2.0 

    show sc i_1_080 with my_dissolve

    "[Name]" "{i}(It wouldn't be polite not to give your beloved friend a look...){/i}"

    show sc i_1_080 with my_dissolve

    "[Name]" "{i}(Especially since she's a real eye candy.){/i}"

    show sc i_1_080 with my_dissolve

    "[Name]" "{i}(Even her friend Audrey looked at her so predatory...){/i}"

    show sc i_1_080 with my_dissolve

    "[Name]" "{i}(I'd give anything to know what would happen in their compartment...){/i}"

    show sc i_1_080 with my_dissolve

    "[Name]" "{i}(Time to find out what awaits me in mine...){/i}"


    stop music_2 fadeout 2.0
    scene expression '#000' with Dissolve(.5)

    $ renpy.pause(1, hard = True)

label scene_16:

    play music 'audio/new/ambience/ambience_in_train.mp3' fadein 1.0 
    scene sc i_1_081 with Dissolve(1)





    "[Name]" "{i}(Where am I heading? I still can't believe it...){/i}"

    show sc i_1_081 with my_dissolve

    "[Name]" "{i}(Samantha was always very enthusiastic about Cordale...){/i}"

    show sc i_1_081 with my_dissolve

    "[Name]" "{i}(On the other hand, she lied that she was studying to become a lawyer. I even googled Cordale.){/i}"

    show sc i_1_081 with my_dissolve

    "[Name]" "{i}(The wiki says this is an ivy league elite educational institution.){/i}"

    show sc i_1_081_2 with my_dissolve

    "[Name]" "{i}(Yet there was nothing about magic... Is that true? Am I a wizard?){/i}"

    show sc i_1_081_2 with my_dissolve
    "Unknown Girl" "Excuse me, are these seats taken?"
    show sc i_1_081_2 with my_dissolve
    "[Name]" "Huh?{w} What?"
label i_1_082a_test:
    stop music
    play sound_2 'audio/new/Music/intro1.mp3' fadein 1.0
    scene sc i_1_082 with Dissolve(1)
    $ renpy.pause(6.5, hard = True)
    play music 'audio/new/Music/background_music1.mp3' fadein 1.0
    $ renpy.pause(3.1, hard = True)
    $ renpy.pause(9999)



    "[Name]" "{i}(What a cutie!){/i}"

    "[Name]" "Oh, no, not really. Be my guest!"
    show sc i_1_083 with my_dissolve
    "Unknown Girl" "Excellent! You are my savior."
    scene sc i_1_085 with Dissolve(.5)
    menu:
        "Offer assistance" if True:
            $ pass
        "Enjoy the view" if True:
            jump train_menu_2
label train_menu_0:
    scene sc i_1_086_2 with Dissolve(.5)
    "[Name]" "Let me help you!"
label train_menu_1:
    scene sc i_1_086_2 with Dissolve(.5)
    "[Name]" "Here you go!"
    show sc i_1_086 with my_dissolve
    "Unknown Girl" "Thanks."
    show sc i_1_086 with my_dissolve
    "[Name]" "No problem, I'm always happy to help."
    show sc i_1_087 with my_dissolve
    "Unknown Girl" "Could you...{w} move over a little further?"
    show sc i_1_087 with my_dissolve
    "[Name]" "Oh. Yes, of course."

    jump train_menu_end

label train_menu_2:
    scene sc i_1_089 with Dissolve(.5)
    $ renpy.pause(9999999)
    menu:
        "Offer assistance" if True:
            jump train_menu_0
        "Continue enjoying the view" if True:
            $ pass
    show sc i_1_089 with my_dissolve
    "Unknown Girl" "Hey!!! What are you staring at? You'd better help me with my suitcase."
    show sc i_1_085 with my_dissolve
    "[Name]" "This is not what it looks like. I was just distracted by... Nevermind."
    jump train_menu_1
label train_menu_end:
    scene sc i_1_090 with Dissolve(.5)
    $ renpy.pause(99999999999)

    scene sc i_1_091 with Dissolve(.5)
    "[Name]" "Sorry... It got awkward..."
    show sc i_1_092 with my_dissolve
    "Unknown Girl" "Don't worry, all guys are a little perverted."
    show sc i_1_092 with my_dissolve
    "[Name]" "{i}(Well, I would not say \"a little\"...){/i}"
    show sc i_1_091 with my_dissolve
    "[Name]" "It is not true! I wasn't thinking of anything like that."
    show sc i_1_093 with my_dissolve
    "Unknown Girl" "Why?!"
    show sc i_1_094 with my_dissolve
    "[Name]" "Um, well..."
    show sc i_1_095 with my_dissolve
    "Unknown Girl" "Relax! I'm just kidding."
    show sc i_1_095 with my_dissolve
    "Unknown Girl" "By the way, my name is Haley! Yours?"
    show sc i_1_096 with my_dissolve
    "[Name]" "[Name]. Nice to meet you! You are funny."
    show sc i_1_096 with my_dissolve
    "Haley" "Thank you, [Name]! You are nice too."
    show sc i_1_096 with my_dissolve
    "[Name]" "Sorry if this question is a bit forward..."
    show sc i_1_096 with my_dissolve
    "[Name]" "...but didn't all the passengers take their seats an hour ago?"
    show sc i_1_096 with my_dissolve
    "[Name]" "How did it happen that you are coming here only now?"
    show sc i_1_097 with my_dissolve
    "Haley" "There's a rather extravagant girl in my compartment..."
    show sc i_1_097 with my_dissolve
    "Haley" "She drank a bottle of whiskey in the blink of an eye and started hitting on me."
    show sc i_1_097 with my_dissolve
    "Haley" "So I decided to get out of there!"
    show sc i_1_095 with my_dissolve
    "Haley" "And you are the only one who has a free seat in the couchette!"
    show sc i_1_095 with my_dissolve
    "Haley" "You don't mind if I join you, do you?"
    show sc i_1_095 with my_dissolve
    menu:
        "Of course not!" if True:
            $ pass
        "Two drunk girls!?" if True:
            jump train_menu_drunk_girls
    scene sc i_1_096 with Dissolve(.5)
    "[Name]" "Of course not! There is plenty of room here, and it is always more fun with company."
    show sc i_1_098 with my_dissolve
    "Haley" "Agreed! I hope you're not planning on getting drunk and harassing me?"
    show sc i_1_098 with my_dissolve
    "[Name]" "I am not."
    show sc i_1_098 with my_dissolve
    "Haley" "Thanks."
    show sc i_1_098 with my_dissolve
    "[Name]" "For now..."
    show sc i_1_096 with my_dissolve
    jump train_menu_after_drunk_girls
label train_menu_drunk_girls:
    "[Name]" "Wait! Are you saying that somewhere on the train there is a compartment with a drunk hottie?"
    show sc i_1_096 with my_dissolve
    "Haley" "Yes, couchette number 8. Why?"
    show sc i_1_093 with my_dissolve
    "[Name]" "I'll leave this compartment at your complete disposal."
    show sc i_1_093 with my_dissolve
    "[Name]" "I have urgent business in couchette number 8!"
label train_menu_after_drunk_girls:

    show sc i_1_099 with my_dissolve
    "Haley" "Wait, what?!"

    "[Name]" "Relax, it was just a joke."
    show sc i_1_100 with my_dissolve
    "[Name]" "{i}(Although the prospect is not the worst.){/i}"
    show sc i_1_092 with my_dissolve
    "Haley" "You are funny. I didn’t know that the Academy had a faculty of humorists."
    show sc i_1_094 with my_dissolve
    "[Name]" "Someone has to take care of the future world of stand-up!"
    show sc i_1_094 with my_dissolve

    "[Name]" "Besides, no stand-up works without a bit of magic!"
    show sc i_1_092 with my_dissolve
    "Haley" "Wait, are you kidding me? Or are you serious?"
    show sc i_1_092 with my_dissolve
    "Haley" "What do you know about magic?"
    show sc i_1_092 with my_dissolve
    "Haley" "I've been digging around the Internet and the city library all week..."
    show sc i_1_098 with my_dissolve
    "Haley" "...but I haven't found any specifics!"
    show sc i_1_098 with my_dissolve
    "Haley" "But I won't give up. I'm sure the information I found there will still be useful to me."
    show sc i_1_095 with my_dissolve
    "Haley" "What do you think, which people were closest to learning the theory of magic?"
    show sc i_1_094 with my_dissolve
    "[Name]" "Uh... Winx fairies?"
    show sc i_1_098 with my_dissolve
    "Haley" "Do you know anything about magic at all?"
    show sc i_1_096 with my_dissolve
    "[Name]" "Actually, my friend is in her sophomore year in Cordale."
    show sc i_1_098 with my_dissolve
    "Haley" "Did she tell you anything? Please, share with me!"
    show sc i_1_099 with my_dissolve
    "[Name]" "She didn't tell me anything! "
    show sc i_1_099 with my_dissolve
    "[Name]" "It is all very secret and they are forbidden to talk about the details."
    show sc i_1_099 with my_dissolve
    "Haley" "What friend leaves her pal in ignorance like that?"
    show sc i_1_094 with my_dissolve
    "[Name]" "Don't say that! I will meet up with her when I arrive and she will help me."
    show sc i_1_092 with my_dissolve
    "Haley" "Okay, okay! Excuse me, I got excited."
    show sc i_1_092 with my_dissolve
    "Haley" "I'm so delighted that magic exists..."
    show sc i_1_092 with my_dissolve
    "Haley" "...I can barely contain myself."
    show sc i_1_098 with my_dissolve
    "Haley" "You should know how many theories I have!"
    show sc i_1_098 with my_dissolve
    "Haley" "What if magic is..."
    show sc i_1_096 with my_dissolve
    "For the next few hours Haley shares her crazy theories about the Academy..."
    show sc i_1_101_2 with my_dissolve
    "...until you manage to convince her that it's worth getting some sleep before the big day."
    stop music fadeout 2.0
    scene expression '#000' with Dissolve(1)



    play music 'audio/new/ambience/ambience_in_train.mp3' fadein 1.0 
    $ renpy.pause(1, hard = True)
    scene sc i_1_101_3 with Dissolve(1)
    "[Name]" "{i}(It was getting quite dark outside the window.){/i}"
    show sc i_1_101_3 with my_dissolve
    "[Name]" "{i}(And I still haven't fallen asleep.){/i}"
    show sc i_1_101_3 with my_dissolve
    "[Name]" "{i}(Time to do something about this insomnia.){/i}"
    show sc i_1_101_4 with my_dissolve
    "[Name]" "{i}(But who can blame me?){/i}"
    show sc i_1_101_4 with my_dissolve
    "[Name]" "{i}(It's hard to fall asleep when your dick's on fire.){/i}"
    show sc i_1_101_4 with my_dissolve
    "[Name]" "{i}(I haven't fucked since I broke my leg.){/i}"
    show sc i_1_101_4 with my_dissolve
    "[Name]" "{i}(And here...){/i}"
    show sc i_1_101_5 with my_dissolve
    "[Name]" "{i}(Such a hottie!){/i}"
    show sc i_1_101_5 with my_dissolve
    "[Name]" "{i}(Flirting with me all day long.){/i}"
    show sc i_1_101_5 with my_dissolve
    "[Name]" "{i}(And now she's flashing her naked feet...){/i}"
    show sc i_1_101_6 with my_dissolve
    "[Name]" "{i}(I can't take it anymore!){/i}"
    show sc i_1_101_6 with my_dissolve
    "[Name]" "{i}(I need to satisfy my curiosity.){/i}"
    show sc i_1_101_6 with my_dissolve
    "[Name]" "{i}(Maybe I should take a closer look. What's the big deal?){/i}"
    show sc i_1_101_6 with my_dissolve
    "[Name]" "{i}(What should I do?){/i}"
    if persistent.from_gallery:
        $ renpy.block_rollback()
    $ FileSave(19, confirm = False)()
label test_choice_menu:

    menu:
        "Take a look Haley" if True:

            $ unlock_gallery('images/ero/3.png')
            $ pass
        "Don't risk" if True:


            if persistent.from_gallery:

                scene expression '#000' with Dissolve(1)
                $ renpy.full_restart()



            jump train_end_16_1



    menu:
        "Look under her skirt" if True:


            $ pass
        "Turn her on her back" if True:


            jump train_not_too_big
        "Stop & go to sleep" if True:


            jump train_end_16_1

    scene sc i_1_101_7 with Dissolve(.5)

    "[Name]" "{i}(What have we here...){/i}"

    show sc i_1_101_7 with my_dissolve

    "[Name]" "{i}(Well, hello there!){/i}"

    "[Name]" "{i}(Sweet transparent panties. Nice choice for the train!){/i}"

    show sc i_1_101_7 with my_dissolve

    "[Name]" "{i}(It makes me want to touch...){/i}"

    scene sc i_1_101_7 with Dissolve(.5)





    menu:
        "Touch" if True:


            $ pass
        "Turn her on her back" if True:


            jump train_not_too_big
        "Stop & go to sleep" if True:


            jump train_end_16_1

    scene sc i_1_101_8 with Dissolve(.5)

    "[Name]" "{i}(Oh, yes! You're even a little wet...){/i}"

    show sc i_1_101_8 with my_dissolve

    "[Name]" "{i}(Maybe you're dreaming about me?){/i}"

    show sc i_1_101_8 with my_dissolve

    "[Name]" "{i}(Shall I take a closer look at you?){/i}"

    scene sc i_1_101_8 with Dissolve(.5)

    menu:
        "Move her panties" if True:

            $ i_1_101_9_var = True
            $ pass
        "Turn her on her back" if True:


            jump train_not_too_big
        "Stop & go to sleep" if True:


            jump train_end_16_1

    scene sc i_1_101_9 with Dissolve(.5)

    "[Name]" "{i}(What a neat, tight holes you've got...){/i}"

    show sc i_1_101_9 with my_dissolve

    "[Name]" "{i}(You must be a virgin.){/i}"

    show sc i_1_101_9 with my_dissolve

    "[Name]" "{i}(For now...){/i}"

    scene sc i_1_101_9 with Dissolve(.5)

    menu:
        "Turn her on her back" if True:


            $ pass
        "Stop & go to sleep" if True:


            jump train_end_16_1

label train_not_too_big:

    scene sc i_1_101_10 with Dissolve(.5)

    "[Name]" "{i}(Not too big.){/i}"

    show sc i_1_101_10 with my_dissolve

    "[Name]" "{i}(But not too flat either.){/i}"

    scene expression 'images/prologue/1_101_11.webp' with Dissolve(.5)

    "[Name]" "{i}(The golden mean!){/i}"



    "[Name]" "{i}(I wonder how it fits in my hand?){/i}"



    menu:
        "Grab it" if True:


            $ pass
        "Stop & go to sleep" if True:


            jump train_end_16_1

    scene sc i_1_101_12 with Dissolve(.5)

    "[Name]" "{i}(It's so soft to the touch!){/i}"

    show sc i_1_101_12 with my_dissolve

    "[Name]" "{i}(And so warm.){/i}"

    show sc i_1_101_12 with my_dissolve

    "[Name]" "{i}(I must find out how firm it is!){/i}"

    scene sc i_1_101_12 with Dissolve(.5)

    menu:
        "Rub her breasts" if True:


            $ pass
        "Stop & go to sleep" if True:


            jump train_end_16_1

    scene sc i_1_101_13 with Dissolve(.5)

    "[Name]" "{i}(Oh, yes! Divine.){/i}"

    show sc i_1_101_13 with my_dissolve

    "[Name]" "{i}(Even through clothes, I can feel how firm they are...){/i}"

    show sc i_1_101_13 with my_dissolve

    "[Name]" "{i}(Is it my imagination, or did Haley just moved?){/i}"

    show sc i_1_101_13 with my_dissolve

    "[Name]" "{i}(Better not take any chances.){/i}"

    show sc i_1_101_14 with my_dissolve

    "[Name]" "{i}(Hmm.){/i}"

    show sc i_1_101_14 with my_dissolve

    "[Name]" "{i}(I think she's just tossing and turning in her sleep.){/i}"

    show sc i_1_101_14 with my_dissolve

    "[Name]" "{i}(Even though I'm afraid to wake you up, Haley...){/i}"

    show sc i_1_101_14 with my_dissolve

    "[Name]" "{i}(I don't know if I can resist looking at your nipple...){/i}"

    scene sc i_1_101_14 with Dissolve(.5)

    menu:
        "Bare nipple" if True:


            $ pass
        "Stop & go to sleep" if True:


            jump train_end_16_1

    scene sc i_1_101_15 with Dissolve(.5)

    "[Name]" "{i}(Gently pinch the edge of her blouse with a finger...){/i}"

    show sc i_1_101_15 with my_dissolve

    "[Name]" "{i}(And... Voila!){/i}"

    show sc i_1_101_16 with my_dissolve

    "[Name]" "{i}(Hello, hello!){/i}"

    show sc i_1_101_16 with my_dissolve

    "[Name]" "{i}(It's so neat.){/i}"

    show sc i_1_101_16 with my_dissolve

    "[Name]" "{i}(Haley, you're really beautiful...){/i}"

    show sc i_1_101_17 with my_dissolve

    "[Name]" "{i}(Huh?){/i}"

    show sc i_1_101_17 with my_dissolve

    "[Name]" "{i}(Turned away from me.){/i}"

    show sc i_1_101_17 with my_dissolve

    "[Name]" "{i}(Probably tired of our \"games\".){/i}"

    show sc i_1_101_17 with my_dissolve

    "[Name]" "{i}(I'm not gonna push my luck anymore.){/i}"

    show sc i_1_101_6 with my_dissolve

    "[Name]" "{i}(You're done for the day.){/i}"
    if persistent.from_gallery:

        scene expression '#000' with Dissolve(1)
        $ renpy.full_restart()
    show sc i_1_101_6 with my_dissolve

    "[Name]" "{i}(But we'll get back to it!){/i}"

    show sc i_1_101_6 with my_dissolve

    "[Name]" "{i}(Won't we?){/i}"

    show sc i_1_101_5 with my_dissolve

    "[Name]" "{i}(What a rush of emotion...){/i}"



    "[Name]" "{i}(My heart's beating like crazy.){/i}"

label train_end_16_1:
    if persistent.from_gallery:

        scene expression '#000' with Dissolve(1)
        $ renpy.full_restart()
    scene sc i_1_101_3 with Dissolve(.5)

    "[Name]" "{i}(I'd better turn away from temptation...){/i}"

    show sc i_1_101_3 with my_dissolve
    "[Name]" "{i}(...and try to sleep...){/i}"







    stop music fadeout 3.0
    scene expression '#000' with Dissolve(2)

    $ renpy.pause(1, hard = True)
    play music 'audio/new/ambience/ambience_in_train.mp3' fadein 5.0 

    "Haley" "Hey, [Name], wake up!"


    "[Name]" "Well, just a few more minutes..."



    "Haley" "{i}(Hmm, he's cute when he sleeps.{/i})"




    scene sc i_1_102 with Dissolve(2.5)

    $ renpy.pause(1)


    "[Name]" "Did you say something?"



    show sc i_1_102 with my_dissolve

    "Haley" "I said WAKE UP! You won't believe your eyes!"

    show sc i_1_102 with my_dissolve

    "[Name]" "{i}(I'm sure she just called me cute...){/i}"

    show sc i_1_102 with my_dissolve

    "[Name]" "{i}(Was that what she was thinking?){/i}"

    show sc i_1_103 with my_dissolve

    "[Name]" "Haley, what happened?"

    show sc i_1_103 with my_dissolve

    "[Name]" "I was sleeping so sweet..."

    show sc i_1_103 with my_dissolve

    "Haley" "Tell me you're seeing this, too. I'm not hallucinating, am I?"

    show sc i_1_103_2 with my_dissolve

    "[Name]" "Holy crap!"

    show sc i_1_103_2 with my_dissolve

    "[Name]" "Am I still dreaming?"


    play sound 'audio/new/gameplay/dragon_scream_in_train.mp3'
    show sc i_1_104 with my_dissolve


    "[Name]" "Fucking dragons!"

    show sc i_1_104 with my_dissolve

    "[Name]" "Unbelievable..."

    show sc i_1_104 with my_dissolve

    "Haley" "Magical..."
    play sound 'audio/new/gameplay/dragon_scream_in_train3.mp3'
    show sc i_1_105 with my_dissolve

    "Haley" "I've only seen these in movies."

    show sc i_1_105 with my_dissolve

    "[Name]" "Yeah..."

    show sc i_1_105 with my_dissolve

    "Haley" "Do you think they can attack a train?"
    stop music fadeout 1.0
    play music_2 'audio/new/ambience/ambience_out_Train.mp3' fadein 1.0

    show sc i_1_104_2 with my_dissolve

    "[Name]" "Those cuties?"


    play sound 'audio/new/gameplay/dragon_scream_on_street2.mp3'
    show sc i_1_104_2 with my_dissolve

    "[Name]" "I don't think so!"

    show sc i_1_104_2 with my_dissolve

    "[Name]" "They seem pretty peaceful."

    stop music_2  fadeout 1.0
    play music 'audio/new/ambience/ambience_in_train.mp3' fadein 1.0

    show sc i_1_104 with my_dissolve

    "Haley" "I don't know, it's kind of creepy."

    show sc i_1_104 with my_dissolve

    "Haley" "I thought all dragons were predators!"

    show sc i_1_106 with my_dissolve

    "[Name]" "Haley, don't worry about it."

    show sc i_1_106 with my_dissolve

    "[Name]" "They would have attacked a long time ago!"

    show sc i_1_107 with my_dissolve

    "Haley" "I guess you're right."

    show sc i_1_107 with my_dissolve

    "Haley" "Sorry, I'm a little afraid of all lizards..."

    show sc i_1_107 with my_dissolve

    "Haley" "Especially flying ones."

    show sc i_1_106 with my_dissolve

    "[Name]" "I wonder what other surprises this day has in store for us."

    show sc i_1_107 with my_dissolve

    "Haley" "I guess we're about to find out!"

label test_label_ep1_1:

    show sc i_1_107 with my_dissolve
    "Haley" "There's a tunnel ahead."
    play sound 'audio/new/music/Magic_train.mp3'
    scene sc i_1_108 with Dissolve(.5)



    $ renpy.pause(999999)

    stop music  fadeout 1.0
    play music 'audio/new/ambience/ambience_train_in_tunnel.mp3' fadein 1.0
    scene expression '#000' with Dissolve(.5)

    "[Name]" "...What a long tunnel..."

    "Haley" "It's like an eternity."

    "Haley" "In some cultures, a dark tunnel symbolizes the passage between worlds."

    "Haley" "Or the afterlife..."

    "[Name]" "How do you know all this?"

    "Haley" "My mother's a librarian."

    show sc i_1_108_2 with my_long_dissolve


    "Haley" "Look, I think we're almost there!"



    "[Name]" "Yeah, I think dragons were a strong hint."



    show sc i_1_108_3 with my_dissolve
    stop music  fadeout 2.0
    play music_2 'audio/new/ambience/ambience_platform3.mp3' fadein 2.0
    play sound "audio/new/Music/train_stoping.mp3"

    "Haley" "You never know..."


    show sc i_1_108_3 with my_dissolve

    "Radio" "Applicants for the Cordale entrance exam..."

    show sc i_1_108_3 with my_dissolve

    "Radio" "...please gather in the lobby of the station within 10 minutes. Don't be late."

    show sc i_1_108_3 with my_dissolve

    "Haley" "So, into the unknown?"

    show sc i_1_109 with my_dissolve

    "Haley" "[Name], hey, you coming?"

    show sc i_1_109 with my_dissolve

    "[Name]" "Go without me."

    show sc i_1_109 with my_dissolve

    "[Name]" "I have to meet a friend."

    show sc i_1_109 with my_dissolve

    "[Name]" "I'll find you later."

    scene expression '#000' with Dissolve(1.5)

    $ renpy.pause(1, hard = True)


    scene sc i_1_108_3 with Dissolve(1.5)

    "[Name]" "{i}(I need to find Samantha. Where was the meeting point?){/i}"






    scene sc i_1_109_2 with Dissolve(1)

    "[Name]" "{i}(Ah! Think of the devil and here is!){/i}"

    show sc i_1_109_2 with my_dissolve

    "Samantha" "[Name], there you are!"

    show sc i_1_110 with my_dissolve

    "Samantha" "Let's step aside."

    show sc i_1_110 with my_dissolve

    "[Name]" "Samantha! I was just looking for you!"

    show sc i_1_110 with my_dissolve

    "Samantha" "Not here."

    show sc i_1_110 with my_dissolve

    "Samantha" "Follow me."


    stop music_2  fadeout 20.0

    play music 'audio/new/Music/background_music2.mp3' fadein 4.0

    show sc i_1_113 with my_dissolve

    "[Name]" "Sam, wait up! Where are we going?"

    show sc i_1_111 with my_dissolve

    "Samantha" "Shh! Speak quietly. "

    show sc i_1_111 with my_dissolve

    "Samantha" "I came to warn you."

    show sc i_1_111 with my_dissolve

    "Samantha" "As I've promised I will."

    show sc i_1_117 with my_dissolve

    "[Name]" "About what?"

    show sc i_1_118 with my_dissolve

    "Samantha" "About the entrance exam. "

    show sc i_1_118 with my_dissolve

    "Samantha" "Did you notice anything unusual while on the train?"

    show sc i_1_117 with my_dissolve

    "[Name]" "You mean like dragons outside the window?"

    show sc i_1_117 with my_dissolve

    "[Name]" "Of course I noticed dragons, they are freaking dragons, come on!"

    show sc i_1_118 with my_dissolve

    "Samantha" "I'm not talking about that, you fool. "

    show sc i_1_118 with my_dissolve

    "Samantha" "Did you notice anything unusual behind you?"

    show sc i_1_118 with my_dissolve

    "Samantha" "Did you feel... powerful?"

    show sc i_1_117 with my_dissolve

    "[Name]" "{i}(I thought I could hear Haley's thoughts.){/i}"

    show sc i_1_117 with my_dissolve

    "[Name]" "{i}(Should I tell Sam about this?){/i}"

    scene sc i_1_117 with Dissolve(.5)

    menu:
        "I heard thoughts" if True:


            $ pass
        "No, nothing" if True:


            jump end_no_nothing

    scene sc i_1_119_2 with Dissolve(.5)

    "Samantha" "Is that true? What am I thinking right now?"
    jump Read_Samanthas_thoughts_label
label end_no_nothing:
    scene sc i_1_117 with Dissolve(.5)
    "Samantha" "Don't be afraid of me, pal. I am trying to help."
    show sc i_1_118 with my_dissolve
    "[Name]" "I'm not even sure anything happened."
    show sc i_1_117 with my_dissolve
    "Samantha" "What could have happened?"
    show sc i_1_117 with my_dissolve
    "Samantha" "Sparks from your fingers?"
    show sc i_1_117 with my_dissolve
    "Samantha" "Did you shatter glass just by looking at it?"
    show sc i_1_117 with my_dissolve
    "Samantha" "Did you read someone's thoughts?"
    show sc i_1_118 with my_dissolve
    "[Name]" "How did you know?"
    show sc i_1_119_2 with my_dissolve
    "Samantha" "I know everything! Remember that. Come on, read my mind!"
    show sc i_1_117 with my_dissolve
    "[Name]" "I don't know how to do it on purpose..."
    show sc i_1_117 with my_dissolve
    "[Name]" "I'm not at all sure that that happened."
    show sc i_1_119 with my_dissolve
    "Samantha" "Make sure you remember one thing: in this place nothing \"seems\" a certain way without reason."
    show sc i_1_119 with my_dissolve
    "Samantha" "Concentrate and look me in the eyes."
label Read_Samanthas_thoughts_label:
    scene sc i_1_119_2 with Dissolve(.5)
    menu:
        "Read Samantha's thoughts" if True:
            $ pass
    scene sc i_1_119_2 with Dissolve(.5)
    "{i}Sam is humming Avril Lavigne - Girlfriend in her mind.{/i}"
    show sc i_1_115 with my_dissolve
    "[Name]" "You have terrible taste in music."
    show sc i_1_115 with my_dissolve
    "Samantha" "Very cool! Try again!"
    scene sc i_1_119_2 with Dissolve(.5)
    menu:
        "Read Samantha's thoughts" if True:
            $ pass
    scene sc i_1_119_2 with Dissolve(.5)
    "{i}Samantha's thoughts: (Inaudible interference.){/i}"
    show sc i_1_119_2 with my_dissolve
    "[Name]" "I... I can't..."
    show sc i_1_114 with my_dissolve
    "Samantha" "This is called a \"mental block.\""
    show sc i_1_114 with my_dissolve
    "Samantha" "A telepath of your level will not be able to read the thoughts of a talented magician like me."
    show sc i_1_114 with my_dissolve
    "Samantha" "The first time I “let” you do it."
    show sc i_1_113 with my_dissolve
    "[Name]" "Sounds like a useless ability."
    show sc i_1_114 with my_dissolve
    "Samantha" "You will have plenty of time to practise your skill."
    show sc i_1_121 with my_dissolve
    "Samantha" "If you don't fail the entrance exams..."
    show sc i_1_121 with my_dissolve
    "Samantha" "...and your memory isn't erased."
    show sc i_1_121 with my_dissolve
    "[Name]" "My memory isn't erased?!"
    show sc i_1_119 with my_dissolve
    "Samantha" "Damn, that's why I was looking for you."
    show sc i_1_119 with my_dissolve
    "Samantha" "Listen!"
    show sc i_1_112 with my_dissolve
    "Samantha" "All freshmen will have an entrance exam in magic. "
    show sc i_1_112 with my_dissolve
    "Samantha" "If you fail, your memory will be erased and you'll be sent back to the world without magic."
    show sc i_1_112 with my_dissolve
    "Samantha" "And you will never be able to come here again. Ever."
    show sc i_1_112_2 with my_dissolve
    "[Name]" "What should I do?"
    show sc i_1_119_2 with my_dissolve
    "Samantha" "Don't fail the exam."
    show sc i_1_119_2 with my_dissolve
    "[Name]" "And this is your wise advice?!"
    show sc i_1_120 with my_dissolve
    "Samantha" "Let me finish, you goof!"
    show sc i_1_116 with my_dissolve
    "Samantha" "Magic is powered by Passion. Remember this during the exam."
    show sc i_1_116 with my_dissolve
    "Samantha" "Focus on something that you have a passion for and you will definitely succeed."
    show sc i_1_118 with my_dissolve
    "[Name]" "But why am I just now... starting to read minds?"
    show sc i_1_117 with my_dissolve
    "Samantha" "This is no ordinary train. "
    show sc i_1_117 with my_dissolve
    "Samantha" "To prepare students for the difficult exam..."
    show sc i_1_116 with my_dissolve
    "Samantha" "...the Cordale train saturates everything inside with magical power."
    show sc i_1_116 with my_dissolve
    "Samantha" "While you slept, it charged you with power, like a battery."
    show sc i_1_122 with my_dissolve
    "Radio" "First year students..."
    show sc i_1_122 with my_dissolve
    "Radio" "...who do not appear on the platform within a minute..."
    show sc i_1_122 with my_dissolve
    "Radio" "...will lose the opportunity to take part in the entrance exam."
    show sc i_1_123 with my_dissolve
    "[Name]" "Damn, I gotta run! Thanks for the advice!"
    show sc i_1_124 with my_dissolve
    "Samantha" "Wait."
    show sc i_1_125 with my_dissolve
    "Samantha" "Good luck!"
    show sc i_1_125 with my_dissolve
    "[Name]" "{i}(This is exactly what you can be passionate about.){/i}"


    jump sheet_19
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
