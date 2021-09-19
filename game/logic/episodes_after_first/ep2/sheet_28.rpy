label sheet_28:



    "[Name]" "Where am I?"
    scene sc i_1_229_2 with Dissolve(.5)
    "???" "Name!"
    "[Name]" "What?"
    "???" "Say your name."
    "[Name]" "[Name].{w} [Name] [Surname]."
    "[Name]" "And who are you?"
    "???" "Come closer, [Name]."
    show sc i_1_229_3 with my_dissolve
    "[Name]" "{i}(Oh...){/i}"
    "[Name]" "{i}(They don't look like humans...){/i}"
    "[Name]" "Hey, I was just..."
    show sc i_1_230 with my_dissolve
    "Frida" "Silence."
    show sc i_1_230 with my_dissolve
    "Frida" "Let me take a look..."
    show sc i_1_231 with my_dissolve
    "Frida" "Pfff."
    show sc i_1_231 with my_dissolve
    "Frida" "Nothing interesting."
    show sc i_1_232 with my_dissolve
    "Jaina" "Oh, what a shame..."
    show sc i_1_232 with my_dissolve
    "Jaina" "At first I thought I sensed something within you."
    show sc i_1_233 with my_dissolve
    "Jaina" "But you're too boring."
    show sc i_1_233 with my_dissolve
    "Jaina" "Sorry."
    show sc i_1_234 with my_dissolve
    "[Name]" "Boring?!"
    show sc i_1_234 with my_dissolve
    "[Name]" "Wait a minute, lady..."
    show sc i_1_235 with my_dissolve
    "Leona" "Don't pay attention to them. "
    show sc i_1_235 with my_dissolve
    "Leona" "They are too blind to notice!"
    show sc i_1_235_2 with my_dissolve
    "Leona" "Since the first moment I saw you..."
    show sc i_1_235_2 with my_dissolve
    "Leona" "I can feel...{w} your potential."
    show sc i_1_236 with my_dissolve
    "Katrina" "Yes. "
    show sc i_1_236 with my_dissolve
    "Katrina" "Pure blood flows in you."
    show sc i_1_236 with my_dissolve
    "Katrina" "You are, indeed, an interesting one..."
    show sc i_1_237 with my_dissolve
    "[Name]" "What's going on..."
    show sc i_1_237 with my_dissolve
    "[Name]" "Am I dreaming?"
    show sc i_1_238 with my_dissolve
    "Leona" "Shh!"
    show sc i_1_238 with my_dissolve
    "Leona" "Stop with all these questions."
    show sc i_1_238 with my_dissolve
    "Leona" "Look at me!"
    show sc i_1_239 with my_dissolve
    "Leona" "I see that you have an honourable soul."
    show sc i_1_242 with my_dissolve
    "Leona" "I can sense courage in your heart."
    show sc i_1_242 with my_dissolve
    "Leona" "You will become a Leonheart student."
    show sc i_1_242 with my_dissolve
    "Leona" "My protege."
    show sc i_1_243 with my_dissolve
    "Katrina" "Not so fast!"
    show sc i_1_243 with my_dissolve
    "Katrina" "Leona, I won't let you steal him."
    show sc i_1_243 with my_dissolve
    "Katrina" "Listen to me!"
    show sc i_1_244 with my_dissolve
    "Katrina" "Your blood is strong!"
    show sc i_1_244 with my_dissolve
    "Katrina" "And your character is not devoid of cunning and determination."
    show sc i_1_244 with my_dissolve
    "Katrina" "You can be the greatest!"
    show sc i_1_244 with my_dissolve
    "Katrina" "I'm assigning you to the Adderin House."
    show sc i_1_245 with my_dissolve
    "Leona" "Can't you see Katrina? [Name] is a brave Leoheart soul!"
    "Leona" "Leonheart will guide him on a just path!"
    show sc i_1_246 with my_dissolve
    "Katrina" "The only path for him is Adderin. He is a pureblood magician!"
    "Katrina" "We can fuel his potential!"
    show sc i_1_247 with my_dissolve
    "Leona" "I sense his loneliness and pain, Adderin will only hurt him more."
    "Leona" "He needs a family. He will find one at Leonheart."
    show sc i_1_247 with my_dissolve
    "Katrina" "I won't let you bury his potential!"
    show sc i_1_247 with my_dissolve
    "Katrina" "You wanna fight for him?"
    show sc i_1_249 with my_dissolve
    "Leona" "No need."
    show sc i_1_249 with my_dissolve
    "Katrina" "What do you suggest?"
    show sc i_1_249 with my_dissolve
    "[Name]" "Will somebody care to explain to me what's going on?"
    show sc i_1_250 with my_dissolve
    "Leona" "Be patient, darling."
    show sc i_1_250 with my_dissolve
    "Leona" "There's one way to decide..."
    show sc i_1_250 with my_dissolve
    "Leona" "Which one of us will be better for you."
    show sc i_1_250 with my_dissolve
    "Leona" "This \"way\" requires one test."
    show sc i_1_250 with my_dissolve
    "Leona" "But I think you won't regret it!"
    show sc i_1_251 with my_dissolve
    "Katrina" "You've got to be thankful."
    show sc i_1_251 with my_dissolve
    "Katrina" "You're the first student in a few decades that is so interesting."
    show sc i_1_251 with my_dissolve
    "Katrina" "To both of us."
    show sc i_1_251 with my_dissolve
    "Leona" "Usually, one of us is more persistent."
    show sc i_1_251 with my_dissolve
    "Leona" "But this time it seems to be a tie."
    show sc i_1_251 with my_dissolve
    "[Name]" "So what does it mean for me? "
    show sc i_1_251 with my_dissolve
    "[Name]" "I'm not going to be expelled because of that, won't I?"
    show sc i_1_252 with my_dissolve
    "Katrina" "Aha-ha..."
    show sc i_1_253 with my_dissolve
    "Katrina" "Only if you can't satisfy any of us..."
    show sc i_1_253 with my_dissolve
    "Katrina" "With that impressive cock!"
    if persistent.from_gallery:
        $ renpy.block_rollback()
    $ FileSave(19, confirm = False)()
    menu:
        "WTF? Stop it!" if True:
            if persistent.from_gallery:

                scene expression '#000' with Dissolve(1)
                $ renpy.full_restart()
            $ pass
        "Wait... What?" if True:
            $ unlock_gallery('images/ero/4.png')
            jump sheet_28_1_254
    scene sc i_1_254_2 with Dissolve(.5)
    "[Name]" "Stop it! Immediately!"
    show sc i_1_254_2 with my_dissolve
    "[Name]" "What the fuck is wrong with you two?"
    show sc i_1_254_2 with my_dissolve
    "[Name]" "We've just fucking met!"
    show sc i_1_254_3 with my_dissolve
    "Leona" "Interesting..."
    show sc i_1_254_3 with my_dissolve
    "[Name]" "What's now?"
    show sc i_1_254_4 with my_dissolve
    "Katrina" "What a waste of time."
    show sc i_1_254_4 with my_dissolve
    "Katrina" "You're too timid."
    show sc i_1_254_4 with my_dissolve
    "Katrina" "Make's me want to wommit."
    show sc i_1_254_4 with my_dissolve
    "Katrina" "To think of that I've almost invited you to Adderin! "
    show sc i_1_254_4 with my_dissolve
    "Katrina" "Ugh."
    show sc i_1_254_5 with my_dissolve
    "[Name]" "What a sudden change of opinion..."
    show sc i_1_254_5 with my_dissolve
    "Leona" "Don't mind her."
    show sc i_1_254_5 with my_dissolve
    "Leona" "She's just realized that you are not of her kin."
    show sc i_1_254_6 with my_dissolve
    "Leona" "It was very brave of you to stand up for your ideals."
    show sc i_1_254_6 with my_dissolve
    "Leona" "Refusing our magic and bodies..."
    show sc i_1_254_6 with my_dissolve
    "Leona" "I respect that.{w} It was the choice of your heart."
    show sc i_1_254_6 with my_dissolve
    "[Name]" "So..."
    $ i_1_254_6_var = True
    show sc i_1_254_6 with my_dissolve
    "Leona" "Yes. From now you are Leonheart. "

    jump jump_to_sheet_29


label sheet_28_1_254:
    stop music_2 fadeout 20.0
    play music 'audio/new/sounds/Mistery_Forest_music.mp3'  fadein 5.0
    scene sc i_1_254 with Dissolve(.5)
    "[Name]" "Wait..."
    show sc i_1_254 with my_dissolve
    "[Name]" "What..."
    show sc i_1_254 with my_dissolve
    "[Name]" "What do you mean?"
    show sc i_1_255 with my_dissolve
    "Leona" "Don't get scared, honey."
    show sc i_1_255 with my_dissolve
    "Leona" "Relax, feel the energy in the air."
    show sc i_1_255_2 with my_dissolve
    "Leona" "Let it flow through you."
    show sc i_1_255_2 with my_dissolve
    "Leona" "I'm sure you won't disappoint me!"

    show sc i_1_255_2 with my_dissolve
    "Leona" "Let me take a closer look."
    show sc i_1_255_3 with my_dissolve
    "Leona" "What a marvellous magic wand you have!"
    show sc i_1_255_3 with my_dissolve
    "[Name]" "Don't I get to vote here?"
    show sc i_1_255_3 with my_dissolve
    "Leona" "I'm sorry, did I hear any objections?"
    show sc i_1_255_4 with my_dissolve
    "[Name]" "No, ma'am."
    show sc i_1_255_4 with my_dissolve
    "Leona" "That's a good boy."
    show sc i_1_255_4 with my_dissolve
    "Leona" "Show us the strength of your lion..."
    scene i_1_256_1 with Dissolve(1)
    $ renpy.pause(9999999)

    "Leona" "Ooh..."

    "Leona" "Yes..."
    scene sc i_1_256_2 with Dissolve(.5)
    "Leona" "Do you like it?"

    "[Name]" "{i}(It feels so good...){/i}"

    "[Name]" "{i}(It's been a while since I've got touched... there...){/i}"
    show sc i_1_257 with Dissolve(.5)
    "Leona" "It's getting bigger."

    "Leona" "I'm impressed."
    show sc i_1_257_2 with my_dissolve
    "Leona" "I wonder if it fits in my little mouth."
    show sc i_1_257_2 with my_dissolve
    "Leona" "Do you want me to try it?"
    show sc i_1_258 with my_dissolve
    "Katrina" "You're too shy, Leona!"
    show sc i_1_258 with my_dissolve
    "Katrina" "Let me help you!"
    show sc i_1_259 with my_dissolve
    "Katrina" "Here..."
    show sc i_1_259 with my_dissolve
    "Katrina" "Yes!"
    show sc i_1_259 with my_dissolve
    "Katrina" "Just like that."
    show sc i_1_259_2 with my_dissolve
    "Katrina" "Get him ready! "
    show sc i_1_259_2 with my_dissolve
    "Katrina" "For the main course."
    show sc i_1_259_2 with my_dissolve
    "Katrina" "Let me show you what Adderin has to offer, [Name]."

    scene sc i_1_259_3 with Dissolve(1)
    $ renpy.pause(999999)

    "Leona" "Mhm... Agh..."

    "[Name]" "{i}(It feels like her magic...){/i}"

    "[Name]" "{i}(...Wraps around my dick...){/i}"
    show sc i_1_259_4 with Dissolve(1.5)
    "[Name]" "{i}(...and fills me up with power...){/i}"

    "Leona" "Ahh..."

    "[Name]" "{i}(...giving real pleasure!){/i}"
    show sc i_1_260 with my_dissolve
    "Katrina" "Greedy as always."
    show sc i_1_260 with my_dissolve
    "Katrina" "Grabbing all the attention."
    show sc i_1_260_2 with my_dissolve
    "Leona" "You want your turn?"
    show sc i_1_260_2 with my_dissolve
    "Katrina" "How else would he get a first class blowjob?"
    show sc i_1_260_3 with my_dissolve
    "Leona" "Well..."
    show sc i_1_260_3 with my_dissolve
    "Leona" "If you are so confident..."
    show sc i_1_260_3 with my_dissolve
    "Leona" "Try it. I dare you!"
    show sc i_1_260_3 with my_dissolve
    "Leona" "Get on your knees."
    show sc i_1_260_3 with my_dissolve
    "Katrina" "I'm not afraid of this challenge, Leona!"
    show sc i_1_260_4 with my_dissolve
    "Leona" "Very good!"
    show sc i_1_260_4 with my_dissolve
    "Leona" "But first..."
    show sc i_1_260_5 with my_dissolve
    "Leona" "Let me show you a body of a real woman, [Name]."
    show sc i_1_260_5 with my_dissolve
    "Leona" "Now we're equal."
    show sc i_1_260_6 with my_dissolve
    "Leona" "But Katrina, love!"
    show sc i_1_260_6 with my_dissolve
    "Leona" "I think you'll need a better pose."
    show sc i_1_260_7 with my_dissolve
    "Leona" "I'll help you!"
    show sc i_1_260_7 with my_dissolve
    "Katrina" "What are you do...?"
    show sc i_1_260_8 with my_dissolve
    "Leona" "Shhh!"
    show sc i_1_260_8 with my_dissolve
    "Leona" "Don't talk, you'll hurt him with your teeth."
    show sc i_1_260_8 with my_dissolve
    "Leona" "Open your mouth wider, if you want to fit it in!"
    scene sc i_1_261_1 with Dissolve(1.5)
    $ renpy.pause(999999)


    "[Name]" "{i}(Oh yes...){/i}"

    "[Name]" "{i}(It's amazing!){/i}"
    scene sc i_1_261_2 with Dissolve(1.5)
    "Katrina" "Ahh... Ugh..."

    "[Name]" "{i}(Each time my dick hammers her throat...){/i}"
    scene sc i_1_261_3 with Dissolve(1.5)

    "Katrina" "Mhm..."

    "Katrina" "*Gulp!*"

    "[Name]" "{i}(I feel so much power!){/i}"
    scene sc i_1_262 with Dissolve(.5)

    "Katrina" "Ahh... Wow!"
    show sc i_1_262 with my_dissolve
    "Leona" "What do you think, Katrina?"
    show sc i_1_262_2 with my_dissolve
    "Leona" "Do you like it?"
    show sc i_1_262_2 with my_dissolve
    "Katrina" "It's amazing..."
    show sc i_1_262_3 with my_dissolve
    "Leona" "You've impressed her, [Name]!"
    show sc i_1_262_3 with my_dissolve
    "Leona" "But did she manage to impress you?"
    show sc i_1_262_3 with my_dissolve
    "[Name]" "I'm... Uhh..."
    show sc i_1_262_4 with my_dissolve
    "Leona" "Let me show you..."
    show sc i_1_262_4 with my_dissolve
    "Leona" "...what you can miss."
    show sc i_1_262_5 with my_dissolve
    "Leona" "I see how you look at us."
    show sc i_1_262_5 with my_dissolve
    "Leona" "This lust will give you power."
    show sc i_1_262_6 with my_dissolve
    "Leona" "But it's only the beginning..."
    show sc i_1_262_6 with my_dissolve
    "[Name]" "{i}(Is she really going to...){/i}"
    show sc i_1_262_7 with my_dissolve
    "[Name]" "{i}(...take off her bottom?..){/i}"
    show sc i_1_262_7 with my_dissolve
    "Leona" "Don't you like what you see?"
    show sc i_1_262_8 with my_dissolve
    "Leona" "Don't you want to choose... me?"
    show sc i_1_262_8 with my_dissolve
    "Leona" "Choose Leonheat!"
    show sc i_1_262_9 with my_dissolve
    "Katrina" "You sneaky little..."
    show sc i_1_262_9 with my_dissolve
    "Katrina" "Whore!"
    show sc i_1_262_10 with my_dissolve
    "Katrina" "You think you've got something I don't?"
    show sc i_1_262_10 with my_dissolve
    "Leona" "You wasted no time either. "
    show sc i_1_262_11 with my_dissolve
    "Leona" "Didn't you?"
    show sc i_1_262_11 with my_dissolve
    "Katrina" "I'm not going to step back so easily."
    show sc i_1_262_12 with my_dissolve
    "Katrina" "You and your touchy attitude."
    show sc i_1_262_12 with my_dissolve
    "Katrina" "Trying to take the initiative."
    show sc i_1_262_13 with my_dissolve
    "Katrina" "He'll be mine!"
    show sc i_1_262_13 with my_dissolve
    "Katrina" "Even if I have to go further."
    show sc i_1_262_13 with my_dissolve
    "Katrina" "Nothing you can do about it."
    show sc i_1_262_14 with my_dissolve
    "Leona" "Shut up!"
    show sc i_1_262_14 with my_dissolve
    "Leona" "Gosh, sometimes you get too loud!"
    show sc i_1_262_15 with my_dissolve
    "Leona" "[Name], our time is almost up."
    show sc i_1_262_15 with my_dissolve
    "Leona" "We have one final step to do."
    show sc i_1_262_15 with my_dissolve
    "Leona" "Together."
    show sc i_1_262_15 with my_dissolve
    "Leona" "Will you let us finish this once and for all?"

    menu:
        "No. It's enough." if True:
            $ pass
            if persistent.from_gallery:

                scene expression '#000' with Dissolve(1)
                $ renpy.full_restart()
        "Ready for action." if True:
            jump sheet_28_1_262_16
    scene sc i_1_254_7 with Dissolve(.5)
    "[Name]" "No!"
    "[Name]" "Enough is enough!"
    "[Name]" "I'm not interested in getting a girl so easily."
    show sc i_1_254_8 with my_dissolve
    "[Name]" "There's no challenge in that."
    "Leona" "I see...{w} Very well."
    "Katrina" "Very well?!"
    "Katrina" "Da fuck is very well?!"
    show sc i_1_254_9 with my_dissolve
    "Katrina" "How can you, mortal worm, decline me?"
    "Katrina" "Ught! "
    "Katrina" "To think that I'd almost invited you to Adderin!"
    show sc i_1_254_10 with my_dissolve
    "Katrina" "Fucking joke."
    "Katrina" "A waste of time!"
    "[Name]" "What's wrong with her?"
    show sc i_1_254_11 with my_dissolve
    "Leona" "Nevermind. "
    "Leona" "She could never take a \"no\" as an answer."
    "Leona" "But that's not important."
    "Leona" "The most important thing is that you've chosen with your heart."
    "Leona" "Despite the temptation you've felt..."
    "Leona" "I must say it was a painful denial."
    "Leona" "But i respect it."
    "Leona" "As I will respect any choice of a clean heart."
    "Leona" "It'd be my honor to invite you to Leonheart, [Name]."
    "[Name]" "Thank you."
    "[Name]" "And my honor is to accept this."
    jump jump_to_sheet_29
label sheet_28_1_262_16:
    scene sc i_1_262_16 with Dissolve(.5)
    "[Name]" "I'm always ready for action, girls!"
    show sc i_1_262_16 with my_dissolve
    "Katrina" "Mhmhmhm!"
    show sc i_1_262_16 with my_dissolve
    "Leona" "Oh! Look at him, Katrina."
    show sc i_1_262_17 with my_dissolve
    "Leona" "The boy speaks like a man."
    show sc i_1_262_17 with my_dissolve
    "Katrina" "Don't try to change the subject!"
    show sc i_1_262_17 with my_dissolve
    "Katrina" "You′ve just \"silenced\" me in front of my student!"
    show sc i_1_262_18 with my_dissolve
    "Katrina" "One more time and you're gonna regret it!"
    show sc i_1_262_19 with my_dissolve
    "Leona" "You're upset, I understand this."
    show sc i_1_262_19 with my_dissolve
    "Leona" "But look at him."
    show sc i_1_262_19 with my_dissolve
    "Leona" "Do you really want to keep that majestic cock waiting?"
    show sc i_1_262_19 with my_dissolve
    "Katrina" "You're right."
    show sc i_1_262_17 with my_dissolve
    "[Name]" "Girls! If you've settled your quarells..."
    show sc i_1_262_17 with my_dissolve
    "[Name]" "...let's get to business.{w} I'm getting cold."
    show sc i_1_262_20 with my_dissolve
    "Leona" "We're so sorry, dear..."
    "Leona" "Guess we'll have to beg for your forgivness..."
    show sc i_1_262_20 with my_dissolve
    "Leona" "Katrina, are you sorry?"
    show sc i_1_263 with my_dissolve
    "Katrina" "I am. "
    show sc i_1_263 with my_dissolve
    "Katrina" "Terribly sorry!"
    show sc i_1_263_2 with my_dissolve
    "Katrina" "But I'll try my best..."
    show sc i_1_263_2 with my_dissolve
    "Katrina" "...to do whatever I can..."
    show sc i_1_263_3 with my_dissolve
    "Katrina" "...to please a future Adderin member."
    show sc i_1_263_3 with my_dissolve
    "Leona" "Will you?"
    show sc i_1_263_4 with my_dissolve
    "Leona" "Even if [Name] chooses Leonheart?"
    show sc i_1_263_4 with my_dissolve
    "Katrina" "You're delusional if you still hope to get him, Leona."
    show sc i_1_263_4 with my_dissolve
    "Leona" "We'll see."
    show sc i_1_263_5 with my_dissolve
    "Leona" "Hey, champion."
    show sc i_1_263_5 with my_dissolve
    "Leona" "Are you lonely?"
    show sc i_1_263_5 with my_dissolve
    "Katrina" "Want us to keep you warm?"
    show sc i_1_263_6 with my_dissolve
    "[Name]" "Well, looking at you I've realised..."
    show sc i_1_263_6 with my_dissolve
    "[Name]" "...that I could use some heat..."
    show sc i_1_263_7 with my_dissolve
    "Leona" "From that icicle?"
    show sc i_1_263_7 with my_dissolve
    "Leona" "I′ll show you what is the real \"heat\"."
    show sc i_1_263_8 with my_dissolve
    "[Name]" "It feels like I'm interested."
    show sc i_1_263_8 with my_dissolve
    "Leona" "Yes?"
    show sc i_1_263_9 with my_dissolve
    "[Name]" "But I still need to think about what to chose."
    show sc i_1_263_9 with my_dissolve
    "[Name]" "And while I'm busy..."
    show sc i_1_263_10 with my_dissolve
    "[Name]" "...you both have work to do!"
    scene sc i_1_263_11_1 with Dissolve(1.5)
    $ renpy.pause(99999999)

    "Leona" "Ah!"
    "Katrina" "Yes, just like that!"


    scene sc i_1_263_11_2 with Dissolve(1.5)
    $ renpy.pause(99999999)

    "[Name]" "{i}(Both of them are channeling their energy...){/i}"
    "[Name]" "{i}(...through their tongues...){/i}"
    "[Name]" "{i}(If that's so good I wonder how sex feels...){/i}"

    scene sc i_1_263_11_3 with Dissolve(.5)
    $ renpy.pause(99999)
    "[Name]" "{i}(But her energy... has something special...){/i}"
    "[Name]" "{i}(It feels right...){/i}"
    scene sc i_1_263_11_4 with Dissolve(.5)
    $ renpy.pause(99999)


    "Leona" "Ahh... mmm..."
    "Katrina" "Mhm... ahhh!"
    show sc i_1_263_12 with my_dissolve
    "[Name]" "{i}(Adderin or Leonheart?){/i}"
    "[Name]" "{i}(I have to choose...){/i}"
    "[Name]" "{i}(Adderin is tempting, but...){/i}"
    "[Name]" "{i}(Sam is Leonheart, so does Haley. And that asian chick... Lily?){/i}"
    "[Name]" "{i}(And most importantly...){/i}"
    "[Name]" "{i}(...Leona sucks so much better!){/i}"
    show sc i_1_263_13 with my_dissolve
    "Katrina" "What did you just say?"
    "[Name]" "Me? Nothing!"
    "Katrina" "Don't you dare!"
    show sc i_1_263_14 with my_dissolve
    "Katrina" "You think I can't read your thoughts?"
    "Katrina" "You must be halfwitted!"
    show sc i_1_263_15 with my_dissolve
    "Katrina" "What a joke! "
    "Katrina" "And I've wasted my time on you?"
    show sc i_1_263_16 with my_dissolve
    "[Name]" "Wait... I've had no idea..."
    "[Name]" "What a disgrace!"
    show sc i_1_263_17 with my_dissolve
    "Katrina" "Congratulations, Leona. It seems that you've got..."
    "Katrina" "...another loser in Leonheart family."
    show sc i_1_263_17 with my_dissolve
    "[Name]" "I didn't mean to hurt her..."
    "[Name]" "I've just..."
    show sc i_1_264 with my_dissolve
    "Leona" "Hey!"
    "Leona" "Where are you looking at?"
    "Leona" "It's rude to ignore a girl who gives better blowjobs."
    "Leona" "Let me prove you that you're right."
    show sc i_1_264_2 with my_dissolve
    "Leona" "Let's get your magic wand ready for action!"
    "Leona" "Oh yes!"
    "Leona" "It's getting bigger and bigger."
    "Leona" "Is it your special magical talent?"
    "Leona" "Or you were just shy when we started?"
    show sc i_1_264_3 with my_dissolve
    "[Name]" "You want it to get really big?"
    "[Name]" "Then you need to talk less!"
    show sc i_1_264_4 with vpunch
    "[Name]" "And do MORE!"
    "Leona" "*Gulp!*"
    "[Name]" "I know you like the attitude!"
    scene sc i_1_264_5 with Dissolve(1.5)
    "Leona" "Ahhh... mmm.."
    "Leona" "Mhm..."
    scene sc i_1_264_6 with Dissolve(1.5)

    $ renpy.pause(9999)
    "Leona" "*Gulp!*"
    "[Name]" "{i}(I'm...){/i}"
    scene sc i_1_264_7 with Dissolve(1.5)

    "[Name]" "{i}(...going to...){/i}"
    "[Name]" "{i}(...CUM!){/i}"

label test_sheet_28_face:
    menu:
        "Face" if True:
            jump sheet_28_1_266
        "Mouth" if True:
            $ pass
    scene sc i_1_265 with Dissolve(.5)
    "[Name]" "Take that!"
    "Leona" "Ahhh... *Gulp!*"
    show expression '#fff' with Dissolve(.4)
    $ renpy.pause(.1, hard = True)

    show sc i_1_265_2
    hide expression '#fff' with Dissolve(.5)
    "[Name]" "TAKE..."
    "[Name]" "...IT..."
    show expression '#fff' with Dissolve(.4)
    $ renpy.pause(.1, hard = True)


    hide expression '#fff' with Dissolve(.5)
    "[Name]" "...ALL!"





    show sc i_1_265_3 with my_dissolve


    "[Name]" "YES! "
    "Leona" "Oh yes!"
    show sc i_1_265_4 with my_dissolve
    "Leona" "It tastes like pure magic!"
    show sc i_1_265_4 with my_dissolve
    "[Name]" "Phew..."
    show sc i_1_265_4 with my_dissolve
    "Leona" "You've chosen with your heart."
    show sc i_1_265_4 with my_dissolve

    "Leona" "May it continue to lead you, because it is in the heart that passion arises."
    show sc i_1_265_4 with my_dissolve
    "Leona" "You're a Leonheart now!"

    jump jump_to_sheet_29

label sheet_28_1_266:
    scene sc i_1_266 with Dissolve(.5)
    "[Name]" "Here it comes!"
    "Leona" "Yes! "
    show expression '#fff' with Dissolve(.4)
    $ renpy.pause(.1, hard = True)
    show sc i_1_266_2
    hide expression '#fff' with Dissolve(.5)

    "[Name]" "Ahhh!"

    show sc i_1_266_3 with my_dissolve
    "Leona" "Shower me with your glorious semen!"
    "[Name]" "Do you like that?"
    "Leona" "Mmm... Oh yes!"
    "[Name]" "Well then..."
    show expression '#fff' with Dissolve(.4)
    $ renpy.pause(.1, hard = True)
    show sc i_1_266_4
    hide expression '#fff' with Dissolve(.5)
    "[Name]" "I've got some more for you!"
    show sc i_1_266_5 with my_dissolve
    "Leona" "Ooh! Aha-ha!"
    "Leona" "Oh my!"
    "Leona" "Look at me!"
    show sc i_1_266_6 with my_dissolve
    "Leona" "I'm so messy..."
    "[Name]" "Phew..."
    show sc i_1_266_6 with my_dissolve
    "Leona" "[Name], It's been a real pleasure."
    show sc i_1_266_6 with my_dissolve
    "Leona" "And the most pleasant thing is..."
    "Leona" "...that you've chosen with your heart."
label sheet_28_1_265_6:
    show sc i_1_266_6 with my_dissolve
    "Leona" "May it continue to lead you, because it is in the heart that passion arises."
    show sc i_1_266_6 with my_dissolve
    "Leona" "You're a Leonheart now!"

    jump jump_to_sheet_29


label jump_to_sheet_29:

    stop music   fadeout 1.0
    stop music_2 fadeout 1.0
    play sound 'audio/new/sounds/Win_line.mp3'
    play music_3 'audio/new/sounds/Crowd1.mp3' fadein 3.0
    show expression '#fff' with Dissolve(.4)
    $ renpy.pause(.1, hard = True)
    if persistent.from_gallery:

        scene expression '#000' with Dissolve(1)
        $ renpy.full_restart()

    jump sheet_29



label end_gallery:
    if persistent.from_gallery:

        scene expression '#000' with Dissolve(1)
        $ renpy.full_restart()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
