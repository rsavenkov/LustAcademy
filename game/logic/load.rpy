
init 20 python:
    import threading, zipfile, shutil, cPickle



    disk_lock = threading.RLock()

    def custom_preload(version):
        version = str(version)
        global android_load
        if renpy.android:
            file = os.path.join(renpy.config.gamedir, 'include', 'versions_load', version +'.save')
        else:
            file = os.path.join(renpy.config.gamedir, 'versions_load', version +'.save')
        with disk_lock:
            
            zf = zipfile.ZipFile(file, "r")
            rv = zf.read("log")
            print('!@!' + str(type(rv)))
            
            zf.close()
            
            return rv

    def custom_load(version):
        
        roots, log = cPickle.loads(custom_preload(version))
        log.unfreeze(roots)

    sc_list = renpy.get_ordered_image_attributes('sc')
    def get_all_images_by_name(name):
        r_list = []
        for i in sc_list:
            if name.lower() in i.lower():
                r_list.append(i)
        return r_list


label pre_load_web_image:
    if web_version:
        scene image '#000' 
        show screen predict_load_screen_web(show_loading=False)
        with Dissolve(.5)
        
        python:
            for i in get_all_images_by_name(load_image_now):
                if i not in web_version_load_list:
                    web_version_load_list.append(i)
                    renpy.show('sc ' + i)
                    renpy.with_statement(Fade(0.0, 0.0, 0.0))
        hide screen predict_load_screen_web 
        scene image '#000'
        with Dissolve(.5)

    return