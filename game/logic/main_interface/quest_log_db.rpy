init -100 python:
    quest_log_big_avatars = []
    quest_log_big_avatars_tmp = [
    'Jill', 'Faith', 'Elijah', 'Don', 'Diego', 'Carter', 'Audrey', 'Ashley', 'Arthur', 'Amelie', 'Jaina', 'Frida', 'Grace',
    'Sabrina', 'Victoria', 'Vanessa', 'Lucy', 'Sadira', 'Adele', 'Romul', 'Gabriella', 'Giant', 'Leona', 'Katrina', 
    'Mushroom', 'Willow', 'Olivia', 'Samantha', 'Mina', 'Molly', 'Joshi', 'Lily', 'Haley', 'Naomi', 'Gordon', 'Jacob',

    ]
    chars_gender_table    = {
'Adele': {'gender': 'Girl', 'description': "She's the mysterious hostess of the strip club called Lady Luck. It seems like she's in charge there. She once almost got raped by Diego.", 'age': 28.0}, 
'Amelie': {'gender': 'Girl', 'description': "Amelie loves books and smart people more than anything else in the world. She doesn't seem to mind having affairs with young guys.", 'age': 38.0}, 
'Arthur': {'gender': 'Guy', 'description': 'Arthur Doorman is the headmaster of the school and a respected member of the Wizarding Society. He is an example to all. ', 'age': 92.0}, 
'Ashley': {'gender': 'Girl', 'description': "Olivia and Don's youngest daughter, Ashley, is a prominent athlete who competes in artistic gymnastics.", 'age': 18.0}, 
'Audrey': {'gender': '{size=13}Girl/Shemale{/size}', 'description': " Audrey is Samantha's best friend. I think she's hiding something and Samantha is in on it too. She has a pretty bad temper.", 'age': 19.0}, 
'Carter': {'gender': 'Guy', 'description': "Carter is almost 30. He's the oldest student in the academy despite being a freshman. He's not very talkative.", 'age': 29.0}, 
'Diego': {'gender': 'Guy', 'description': 'A nasty guy who fell in love with Adele after seeing her in a club. Tried to rape the girl, but was disgraced and sent running.', 'age': '28?'}, 
'Don': {'gender': 'Guy', 'description': "Don works as a mid-level manager at the largest car dealership in town. He's a total control freak, and I think he's cheating on Olivia.", 'age': 44.0}, 
'Elijah': {'gender': 'Guy', 'description': "Elijah is the cheerful swashbuckler, Leonheart's headman, and a hoarder who smuggles all sorts of forbidden things into the academy.", 'age': 20.0}, 
'Evelin': {'gender': 'Girl', 'description': None, 'age': None}, 
'Faith': {'gender': 'Girl', 'description': "Worker of Whistley's SPA. She gives excellent massages but it seems that there's something strange about her.", 'age': 22.0}, 
'Frida': {'gender': 'Girl', 'description': 'One of the four co-founders of Cordale Academy. Founder of Crowhive house and the keeper of knowledge.', 'age': '100+'}, 
'Gabriella': {'gender': 'Girl', 'description': 'Cheerful Latino-American student from Martenden. She likes dancing, duels, and living a life full of adventures.', 'age': 18.0}, 
'Giant': {'gender': '???', 'description': 'The strange monster that wonders on the night streets of Dale.', 'age': '???'}, 
'Gordon': {'gender': 'Guy', 'description': "A business-oriented dwarf. Owner of the only store in Dale. Willow's father. You can always make money from him by fishing.", 'age': 82.0}, 
'Grace': {'gender': 'Girl', 'description': "First year student of the house Crowhive. She's intelligent and shy. As far as I know, she likes visiting potions classes.", 'age': 18.0}, 
'Haley': {'gender': 'Girl', 'description': "The first person I met on my way to becoming a wizard. She's smart, beautiful, and funny. I wonder if we can be more than friends...", 'age': 18.0}, 
'Jacob': {'gender': 'Guy', 'description': 'The grimmest teacher in the academy. He runs a dueling club. He has a certain creepy vibe about him.', 'age': 48.0}, 
'Jaina': {'gender': 'Girl', 'description': 'One of the four co-founders of Cordale Academy. Founder of Martenden house and the keeper of Housefire.', 'age': '100+'}, 
'Jill': {'gender': 'Girl', 'description': "Owner of Whistley's SPA. She gives excellent massages but it seems that there's something strange about her.", 'age': 22.0}, 
'Joshi': {'gender': 'Guy', 'description': 'Joshi is a talkative young guy who clearly lives only to have a good time and relax.', 'age': 18.0}, 
'Katrina': {'gender': 'Girl', 'description': 'One of the four co-founders of Cordale Academy. Founder of Adderin house and the keeper of Success. ', 'age': '100+'}, 
'Leona': {'gender': 'Girl', 'description': 'One of the four co-founders of Cordale Academy. Founder of Leonheart house and the keeper of Justice.', 'age': '100+'}, 
'Lily': {'gender': 'Girl', 'description': 'Lily is a real diehard fan of Leonheart. She does a lot for its sake and gets thrilled when I help her with that.', 'age': 18.0}, 
'Lucy': {'gender': 'Girl', 'description': "Lucy is one of the dancers at Lady Luck night club. I think I'll get to know her better if I invite her to VIP.", 'age': 25.0}, 
'Marta': {'gender': 'Girl', 'description': None, 'age': None}, 
'Mina': {'gender': 'Girl', 'description': 'Mina is a very shy girl who manages a local hostel. I saw her reading porn novels, I wonder if she has any other secrets.', 'age': 18.0}, 
'Molly': {'gender': 'Girl', 'description': 'Molly is a hard-working businesswoman who keeps her café in Cordale. She helps me with a part-time job when I need money.', 'age': 20.0}, 
'Naomi': {'gender': 'Girl', 'description': "Naomi is a coldhearted rising queen of manipulation from Adderin and Lily's best friend. ", 'age': 18.0}, 
'Olivia': {'gender': 'Girl', 'description': "Olivia is Samantha and Ashley's mother, She's married to Don. I don't know if she has any hobbies except shopping and spending money. ", 'age': 42.0}, 
'Romul': {'gender': 'Girl', 'description': "A bouncer. He's a prick who asks for bribes to let you in the club. He tricked me and almost let Diego rape Adele.", 'age': 31.0}, 
'Sabrina': {'gender': 'Girl', 'description': 'Sabrina is the sweetest teacher in the Academy, and you can always see how happy she gets when she seems some dedication in her lessons.', 'age': 35.0}, 
'Sadira': {'gender': '{size=13}Girl/Shemale{/size}', 'description': "Sadira is one of the dancers at Lady Luck. She seems strange and exotic, I think I'll enjoy what she can offer in VIP.", 'age': 24.0}, 
'Samantha': {'gender': 'Girl', 'description': "Samantha is my best friend and Olivia's first child. She's kind and supportive and sees good even where no one else can.", 'age': 20.0}, 
'Vanessa': {'gender': 'Girl', 'description': "Vanessa is a barman at Lady Luck. She's mysterious and obsessed with her special cocktails.", 'age': 29.0}, 
'Victoria': {'gender': 'Girl', 'description': "Victoria is strict, but just teacher. Everyone respects her a lot. She makes it look like my flirting is useless, but I won't stop trying.", 'age': 36.0}, 
'Willow': {'gender': 'Fairy', 'description': "Willow is a cheerful and quirky daughter of Gordon. She's helpful when someone needs magical artifacts.", 'age': 18.0}, 
'Mushroom Girl': {'gender': '???', 'description': 'In the mushroom forest, I saw a mystical mushroom girl. I wonder who she is?', 'age': '???'}
}


    quest_log = {
1: 
{'Victoria': 
{
'Victoria_1': [['Q_Victoria','<',' 1','cord_class_1'], ['Q_Elijah','>',' 1','cord_class_1']],
'Victoria_2': [['Q_Victoria','==','1','cord_class_1']],
'Victoria_3': [['Q_Victoria','==','2','cord_class_1'], ['Q_Leona','==','1','cord_class_1']],
'Victoria_4': [['Q_Victoria','==','3','cord_class_1']],
'Victoria_5': [['Q_Victoria','==','4','cord_class_1']],
'Victoria_6': [['Q_Victoria','==','5','cord_class_1']],
'Victoria_8': [['Q_Victoria','==','7','cord_class_1']],
'Victoria_9': [['Q_Victoria','==','8','cord_class_1']],
'Victoria_10': [['Q_Victoria','==','9','cord_class_1']],


'Activity_Magery_1': [['Q_Victoria','==','6','cord_class_1']],
'Samantha_4': [['Q_Samantha','==','3','cord_class_1']]},

'Sabrina': 
{'Sabrina_1': [['Q_Sabrina','==','0','cord_class_2'], ['Q_Victoria','>=',' 1','cord_class_2']],'Sabrina_2': [['Q_Sabrina','==','1','cord_class_2']],'Sabrina_3': [['Q_Sabrina','==','2','cord_class_2']],'Sabrina_4': [['Q_Sabrina','==','3','cord_class_2']],'Alchemy_Practices_1': [['Q_Sabrina','==','4','cord_class_2']]},


'Haley': 
{
'Haley_1' : [['Q_Haley','==','0','cord_class_1']],
'Haley_4' : [['Q_Haley','==','3','cord_class_1']],
'Haley_12': [['Q_Haley','==','11','cord_library']]
},



'Samantha': 
{'Samantha_1': [['Q_Samantha','==','0','leon_living']],'Samantha_2': [['Q_Samantha','==','1','leon_living']],'Samantha_5': [['Q_Samantha','==','4','leon_living']]},'Audrey': 
{'Audrey_1': [['Q_Audrey','==','0','leon_living'], ['Q_Molly','>','1','leon_living']]},'Lily': 
{'Lily_1': [['Q_Lily','==','0','cord_class_1']],'Lily_2': [['Q_Lily','==','1','cord_class_1'], ['Q_Victoria','>=',' 1','cord_class_1']],'Lily_3': [['Q_Lily','==','2','cord_class_1'], ['Books_Send','>=','3','cord_class_1']]},'Naomi': 
{'Naomi_1': [['Q_Naomi','==','0','cord_class_1']],'Naomi_6': [['Q_Naomi','==','5','cord_class_1']]},'Amelie': 
{'Elijah_2': [['Q_Elijah','==','1','cord_library']],'Amelie_2': [['Q_Amelie','==','1','cord_library']],'Activity_Books_1': [['Q_Amelie','==','2','cord_library']]},'Elijah': 
{'Elijah_1': [['Q_Elijah','==','0','leon_living']]}},
2: 
{
'Victoria': 
{'Victoria_1': [['Q_Victoria','<',' 1','cord_class_1'], ['Q_Elijah','>',' 1','cord_class_1']],'Victoria_2': [['Q_Victoria','==','1','cord_class_1']],'Victoria_3': [['Q_Victoria','==','2','cord_class_1'], ['Q_Leona','==','1','cord_class_1']],'Victoria_4': [['Q_Victoria','==','3','cord_class_1']],'Victoria_5': [['Q_Victoria','==','4','cord_class_1']],'Victoria_6': [['Q_Victoria','==','5','cord_class_1']],'Activity_Magery_1': [['Q_Victoria','==','6','cord_class_1']],'Samantha_4': [['Q_Samantha','==','3','cord_class_1']]},'Sabrina': 
{'Sabrina_1': [['Q_Sabrina','==','0','cord_class_2'], ['Q_Victoria','>=',' 1','cord_class_2']],'Sabrina_2': [['Q_Sabrina','==','1','cord_class_2']],'Sabrina_3': [['Q_Sabrina','==','2','cord_class_2']],'Sabrina_4': [['Q_Sabrina','==','3','cord_class_2']],'Alchemy_Practices_1': [['Q_Sabrina','==','4','cord_class_2']]},'Naomi': 
{'Naomi_3': [['Q_Naomi','==','2','cord_class_2']]},'Amelie': 
{'Elijah_2': [['Q_Elijah','==','1','cord_library']],'Amelie_2': [['Q_Amelie','==','1','cord_library']],'Activity_Books_1': [['Q_Amelie','==','2','cord_library']]},'Molly': 
{'Molly_2': [['Q_Molly','==','1','cord_cafe']],'Activity_Work_1': [['Q_Molly','==','2','cord_cafe']]},


'Lily': 
{
'Lily_6': [['Q_Lily','==','5','cord_class_2']],

},





},
3: 
{'Haley': 
{
'Haley_2': [['Q_Haley','==','1','leon_room_hl']],
'Haley_8': [['Q_Haley','==','7','leon_room_hl']]

},


'Audrey': 
{'Audrey_4': [['Q_Audrey','==','4','leon_living']]},'Lily': 
{'Lily_4': [['Q_Lily','==','3','cord_garden_c'], ['Win_Adderin','>=',' 1','cord_garden_c']]},'Naomi': 
{'Naomi_2': [['Q_Naomi','==','1','cord_garden_c']],'Naomi_4': [['Q_Naomi','==','3','cord_garden_c']]},'Molly': 
{'Molly_2': [['Q_Molly','==','1','cord_cafe']],'Activity_Work_1': [['Q_Molly','==','2','cord_cafe']]},


'Naomi': 
{
'Naomi_7': [['Q_Naomi','==','6','cord_garden_c']],

},



'Elijah': 
{
'Elijah_3': [['Q_Elijah','==','2','!cofe_event_2'], ['Q_Sabrina','>',' 0','!cofe_event_2']],
'Elijah_4': [['Q_Elijah','==','3','!cofe_event_2'], ['Q_Gordon', '>',' 0','!cofe_event_2']],
'Elijah_5': [['Q_Elijah','==','4','!cofe_event_2'],]


},


'Jacob': 
{'Samantha_3': [['Q_Samantha','==','2','cord_entrance']],'Jacob_1': [['Q_Jacob','==','0','cord_entrance']],'Jacob_2': [['Q_Jacob','==','1','cord_entrance'], ['Q_Victoria','>',' 4','cord_entrance']],'Activity_Dueling_1': [['Q_Jacob','==','2','cord_entrance']]}},
4: 


{'Haley': 
{
'NV_Haley_1': [['Q_NV_Haley','==','0','leon_room_hl']],
'NV_Haley_2': [['Q_NV_Haley','==','1','leon_room_hl']],
'NV_Haley_3': [['Q_NV_Haley','==','2','leon_room_hl']],
'NV_Haley_4': [['Q_NV_Haley','==','3','leon_room_hl']]},


'Samantha': 
{'NV_Samantha_1': [['Q_NV_Samantha','==','0','leon_room_sa']],'NV_Samantha_2': [['Q_NV_Samantha','==','1','leon_room_sa']],'NV_Samantha_3': [['Q_NV_Samantha','==','2','leon_room_sa']],'NV_Samantha_4': [['Q_NV_Samantha','==','3','leon_room_sa']],'NV_Samantha_5': [['Q_NV_Samantha','==','4','leon_room_sa']]},'Audrey': 
{'NV_Audrey_1': [['Q_NV_Audrey','==','0','leon_room_sa']],'NV_Audrey_2': [['Q_NV_Audrey','==','1','leon_room_sa']],'NV_Audrey_3': [['Q_NV_Audrey','==','2','leon_room_sa']],'NV_Audrey_4': [['Q_NV_Audrey','==','3','leon_room_sa']]},'Lily': 
{'NV_Lily_1': [['Q_Lily','!=',' 4','leon_room_hl'], ['Q_NV_Lily','==','0','leon_room_hl']],'NV_Lily_2': [['Q_Lily','!=',' 4','leon_room_hl'], ['Q_NV_Lily','==','1','leon_room_hl'], ],'NV_Lily_3': [['Q_Lily','!=',' 4','leon_room_hl'], ['Q_NV_Lily','==','2','leon_room_hl'], ],'NV_Lily_4': [['Q_Lily','!=',' 4','leon_room_hl'], ['Q_NV_Lily','==','3','leon_room_hl'], ],'Lily_5': [['Q_Lily','==','4','leon_room_mc']]}}}









    def get_variables_debug(variables):
        if type(variables[0]) == type(''):
            print('!!')
            gtttr = getattr(store,variables[0], None)
            if 'NV' in variables[0]:
                return True
            
            if gtttr is None:
                
                
                
                return None
            
            if variables[1] == '==':
                if gtttr !=  int(variables[2]):
                    
                    return None
            elif variables[1] == '!=':
                if gtttr == int(variables[2]):
                    return None
            elif variables[1] == '>=':
                if gtttr <  int(variables[2]):
                    return None
            elif variables[1] == '<=':
                if gtttr >  int(variables[2]):
                    return None
            elif variables[1] == '>':
                if gtttr <=  int(variables[2]):
                    return None
            elif variables[1] == '<':
                if gtttr >=  int(variables[2]):
                    return None
            if variables[0] == 'Q_NV_Lily':
                print('!!!!!!!label ' + str(variables))
        else:
            for variable in variables:
                gtttr = getattr(store,variable[0], None)
                if 'NV' in variable[0]:
                    return True
                if gtttr is None:
                    return None
                
                if variable[1] == '==':
                    if gtttr != int(variable[2]):
                        return None
                elif variable[1] == '!=':
                    if gtttr == int(variable[2]):
                        return None
                elif variable[1] == '>=':
                    if gtttr < int(variable[2]):
                        return None
                elif variable[1] == '<=':
                    if gtttr > int(variable[2]):
                        return None
                elif variable[1] == '>':
                    if gtttr <= int(variable[2]):
                        return None
                elif variable[1] == '<':
                    if gtttr >= int(variable[2]):
                        return None
        
        
        return True

    def get_variables(variables):
        if type(variables[0]) == type(''):
            
            gtttr = getattr(store,variables[0], None)
            
            if 'NV' in variables[0]:
                return True
            if gtttr is None:
                
                
                
                return None
            
            if variables[1] == '==':
                if gtttr !=  int(variables[2]):
                    
                    return None
            elif variables[1] == '!=':
                if gtttr == int(variables[2]):
                    return None
            elif variables[1] == '>=':
                if gtttr <  int(variables[2]):
                    return None
            elif variables[1] == '<=':
                if gtttr >  int(variables[2]):
                    return None
            elif variables[1] == '>':
                if gtttr <=  int(variables[2]):
                    return None
            elif variables[1] == '<':
                if gtttr >=  int(variables[2]):
                    return None
            if variables[0] == 'Q_NV_Lily':
                print('!!!!!!!label ' + str(variables))
        else:
            for variable in variables:
                if 'NV' in variable[0]:
                    return True
                gtttr = getattr(store,variable[0], None)
                if gtttr is None:
                    return None
                
                if variable[1] == '==':
                    if gtttr != int(variable[2]):
                        return None
                elif variable[1] == '!=':
                    if gtttr == int(variable[2]):
                        return None
                elif variable[1] == '>=':
                    if gtttr < int(variable[2]):
                        return None
                elif variable[1] == '<=':
                    if gtttr > int(variable[2]):
                        return None
                elif variable[1] == '>':
                    if gtttr <= int(variable[2]):
                        return None
                elif variable[1] == '<':
                    if gtttr >= int(variable[2]):
                        return None
        
        
        return True
    def get_quest_log():
        return_arr = []
        for time in quest_log:
            for avatar in quest_log[time]:
                for label in quest_log[time][avatar]:
                    variables = quest_log[time][avatar][label]
                    vrr = get_variables(variables)
                    if vrr is not None:
                        
                        
                        return_arr.append([time, avatar, label, variables[0][3]])
        return return_arr
    def get_quest_log_time(time):
        return_arr = []
        for i in get_quest_log():
            
            if hasattr(store, i[1].lower()+'_events_set'):
                xs = getattr(store, i[1].lower()+'_events_set')
                if i[1].lower() == 'amelie' and i[2] in ['Activity_Books_1', 'Amelie_2'] and hasattr(store, 'books_gg') and not books_gg:
                    continue
                if len(getattr(store, i[1].lower()+'_events_set')) and i[0]not in [3,4]:
                    continue
            
            if i[0]==time:
                return_arr.append(i)
        return return_arr

    qstt          = 0
    qstt_location = 0

    array_quest_log = {
    1:0, 
    2:0, 
    3:0, 
    4:0,}
    def def_array_quest_log(i, j):
        global array_quest_log
        array_quest_log[i] += j 
    def check_copies_quest_log(i, next_page = False):
        tmp_q_t_n   = []
        tmp_q_t_n_r = []
        
        q_t_n = get_quest_log_time(i)
        xs = 0
        if next_page:
            xs += 7
        for x in q_t_n:
            if x[1] not in tmp_q_t_n:
                tmp_q_t_n.append(x[1])
                tmp_q_t_n_r.append(x)
        return tmp_q_t_n_r

