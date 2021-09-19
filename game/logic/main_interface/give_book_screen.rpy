
init -2:
    style pref_slider:


        right_bar "#0000"
        left_bar "#0000"
        thumb "main_interface/give_book/give_book_slider_tm.png"

init python:
    def return_books_change(value = None):
        if value is None:
            return 0
        else:
            return SetVariable('books_send_tmp', value)
    def check_value_return_book(books_send_tmp):
        global books_gg
        if books_gg != 1:
            if int(float(books_send_tmp)/100) > books_gg:
                return books_gg
            else:
                return int(float(books_send_tmp)/100)
        else:
            if books_send_tmp:
                return 1
            else:
                return 0
screen give_book_screen:
    default books_send_tmp = 0
    add 'give_book_top' ypos 430 xalign .5

    viewport:
        xmaximum 100
        ymaximum 50
        add '#0000'
        ypos 475 xalign .52
        hbox:
            xalign .5
            yalign .5
            text '+ ' font 'fonts/h_font.ttf' size 18 color '#fff'
            if books_gg != 1:
                if int(float(books_send_tmp)/100) > books_gg:
                    text str(books_gg) font 'fonts/h_font.ttf' size 18 color '#FFE0C2'
            
                else:
                    text str(int(float(books_send_tmp)/100)) font 'fonts/h_font.ttf' size 18 color '#FFE0C2'
            
            else:
                if books_send_tmp:
                    text str(1) font 'fonts/h_font.ttf' size 18 color '#FFE0C2'

                else:
                    text str(0) font 'fonts/h_font.ttf' size 18 color '#FFE0C2'

            text ' points' font 'fonts/h_font.ttf' size 18 color '#fff'
    viewport:
        xmaximum 670
        ymaximum 380
        #image '#000a'
        add 'give_book_down' 
        xalign .5 yalign .5
        

    
        viewport:
            xalign .5
            yalign .5
            xmaximum 435
            ymaximum 145
            image '#0000'
            text 'Chose the quantity:' xalign .5 ypos 10 font 'fonts/h_font.ttf' size 18 color '#FFEEDE'
            if books_gg != 1:
                if int(float(books_send_tmp)/100) > books_gg:
                    text str(books_gg) + '/' + str(books_gg) xalign .5 ypos 40 font 'fonts/h_font.ttf' size 18 color '#503F6B'
                else:
                    text str(int(float(books_send_tmp)/100)) + '/' + str(books_gg) xalign .5 ypos 40 font 'fonts/h_font.ttf' size 18 color '#503F6B'
            else:
                if books_send_tmp:
                    text str(1) + '/' + str(books_gg) xalign .5 ypos 40 font 'fonts/h_font.ttf' size 21 color '#503F6B'
                else:
                    text str(0) + '/' + str(books_gg) xalign .5 ypos 40 font 'fonts/h_font.ttf' size 21 color '#503F6B'

            viewport:
                xmaximum 131
                ymaximum 31
                add '#0000'
                imagebutton:
                    idle 'give_book_button'
                    hover im.MatrixColor('main_interface/give_book/give_book_button_hover.png', im.matrix.brightness(.3))
                    action Return(0)
                add 'give_book_back' xalign .1 yalign .5
                text 'Cancel' xalign .5 yalign .5 font 'fonts/h_font.ttf' size 13 color '#FFEEDE'
                xalign .2 yalign .85
            if check_value_return_book(books_send_tmp):
                viewport:
                    xmaximum 131
                    ymaximum 31
                    add '#0000'

                    imagebutton:
                        idle 'give_book_button'
                        hover im.MatrixColor('main_interface/give_book/give_book_button_hover.png', im.matrix.brightness(.3))
                        action Return(check_value_return_book(books_send_tmp))
                    text 'Confirm' xalign .5 yalign .5 font 'fonts/h_font.ttf' size 13 color '#FFEEDE'
                    xalign .8 yalign .85

            bar xpos 48 ypos 70 value ScreenVariableValue('books_send_tmp', (books_gg+1)*100) style "pref_slider" xmaximum 345
            imagebutton:
                idle  Transform('main_interface/give_book/give_book_arrow.png', xzoom = -1)
                hover Transform(im.MatrixColor('main_interface/give_book/give_book_arrow.png', im.matrix.brightness(.3)), xzoom = -1)
                ypos 68
                xpos 30
                if books_send_tmp > 0:
                    action SetScreenVariable('books_send_tmp', books_send_tmp-100)
                else:
                    action NullAction()


            imagebutton:
                idle  'main_interface/give_book/give_book_arrow.png'
                hover im.MatrixColor('main_interface/give_book/give_book_arrow.png', im.matrix.brightness(.3))
                ypos 68
                xpos 390
                if books_send_tmp < (books_gg-1)*100:
                    action SetScreenVariable('books_send_tmp', books_send_tmp+100)
                else:
                    action SetScreenVariable('books_send_tmp', (books_gg+1)*100)


                #xpos 147
                #ypos 187
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
