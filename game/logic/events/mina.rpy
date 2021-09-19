label mina_1_label:


    hide screen show_hide_locations
    hide screen show_hide_locations_2
    hide screen text_animation_up_screen_3
    hide screen main_interface 
    scene image '#000' with Dissolve(.5)
    #show sc i_dale_hotel_1_1 with my_dissolve
    "[Name]" "{i}(I think it's a local hotel.){/i}"
    
    #show sc i_Mina_anim_1 with my_dissolve
    "[Name]" "Hi!"
    show sc i_Mina_1_1 with my_dissolve
    
    #show sc i_Mina_anim_1_z with my_dissolve
    "[Name]" '{i}(I wonder if they have student discounts.){/i}'
    "[Name]" "{i}(Oh, it looks like it's going to be pretty cozy to sleep here.){/i}"
    "Unknown Girl" "Hello! Welcome to the Daily Ly Apartments!"
    show sc i_Mina_1_1 with my_dissolve
    "Unknown Girl" "My name is Mina. How may I address you?"
    "[Name]" "Nice to meet you. My name is [Name]."
    "Mina" "[Name], are you looking for a room for the night?"
    show sc i_Mina_1_2 with my_dissolve
    "[Name]" "You're not a magician by any chance, are you?"
    "Mina" "No, why?"
    "[Name]" "It's just that you read my mind so skillfully!"
    show sc i_Mina_1_3 with my_dissolve
    "Mina" "Hee hee."
    "[Name]" '{i}(What a cutie.){/i}'
    show sc i_Mina_1_2 with my_dissolve
    "Mina" "Most of our rooms are being renovated right now."
    "Mina" "The mage party after the elementalist conference got out of hand."
    "[Name]" "I'm sorry to hear that."
    "Mina" "It happens. The peculiarities of doing business in Dale."
    show sc i_Mina_1_4 with my_dissolve
    "Mina" "So right now we only have simple one-bed rooms available."
    "[Name]" "I see. What are your rates?"
    "Mina" "$5 a night."
    "[Name]" "I see. Thank you."
    show sc i_Mina_1_5 with my_dissolve
    "Mina" "Is there anything else I can help you with?"
    $ dltttttt = [False, False]
label mina_1_label_24:
    if all(dltttttt):
        $ del dltttttt
        jump mina_1_label_44
    menu:
        "What are you reading" if not dltttttt[0]:
            $ dltttttt[0] = True
            show sc i_Mina_1_5 with my_dissolve
            "[Name]" "You were reading so passionately that it made me want to read it myself."
            "[Name]" "Can you tell me what this book is called?"
            show sc i_Mina_1_6 with my_dissolve
            "Mina" "Oh, it's... It's nothing..."
            "[Name]" '{i}(Why are you blushing so much?){/i}'
            "[Name]" '{i}(I can still see the title of the book out of the corner of my eye...){/i}'
            "[Name]" "{i}(Delta of Venus? Isn't it a collection of porn novels?){/i}"
            "[Name]" "{i}(You're not as innocent as you look, Mina...){/i}"
            show sc i_Mina_1_7 with my_dissolve
            "[Name]" "That's a shame. I was just looking for some bedtime reading to help me sleep better."
            "Mina" "..."
            "Mina" "Sorry, nothing interesting comes to mind."
        "Student discounts" if not dltttttt[1]:
            $ dltttttt[1] = True
            show sc i_Mina_1_5 with my_dissolve
            "[Name]" "I was wondering if you have a discount for academy students."
            show sc i_Mina_1_8 with my_dissolve
            "Mina" "Oh, so you're a student?"
            "Mina" "You wouldn't know, I thought you were an adventurer..."
            "[Name]" '{i}(Hmm? Why would I be?){/i}'
            show sc i_Mina_1_2 with my_dissolve
            "[Name]" "The two don't interfere with each other."
            "Mina" "Of course it does not."
            "Mina" "In fact, we do have a multi-year agreement with Cordale."
            "Mina" "Freshmen can stay in simple rooms for free."
            "[Name]" "Oh, that's good to hear."
    jump mina_1_label_24

label mina_1_label_44:
    show sc i_Mina_1_2 with my_dissolve
    "Mina" "Is there anything else I can help you with?"
    "[Name]" "Probably not."
    "[Name]" "Thank you, Mina."
    "Mina" "Anytime."
    $ p_up('Mina', 1)
    $ Q_Mina = 1
    jump main_interface_label  