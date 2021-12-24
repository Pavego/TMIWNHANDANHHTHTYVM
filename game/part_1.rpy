label p1_start:
    scene bg natsukiroom_morning
    show natsuki 1pw zorder 2 at h33
    play music t6
    n "{i}yawn{/i}"
    n 1pd "Good morning, [player]!"
    menu:
        "Good morning, Natsuki!":
            pass
        "...":
            pass
    n 1pl "I had a great dream last night!"
    n 1pz "I was sitting in a garden, surrounded by pink fluffy kittens!"
    n "They were so adorable!"
    n 1pc "It almost made me wish I could stay asleep..."
    n 1pl "But I have a feeling today is going to be great!"
    n "Father went on a business trip.."
    n 1pz "(To the recycle bin...)"
    n 1pd "And I'm going to [protag_name]'s house to bake cupcakes for the festival!"
    n 1pc "Okay, let's see..."
    n "First, I need to get myself in order."
    n "I can't go there looking as messy as Sayori..."
    n "Seriously, why doesn't she care about her appearance in the slightest?"
    n "I also need to put all the stuff we'll need in my bag."
    n "I'm not sure if I can trust [protag_name] with getting the right ingredients..."
    n "And I should also rearrange my manga collection."
    n 1pg "..."
    n 1pd "Oh, I completely forgot about you!"
    n "You know what?"
    n "I'll let you do the routine planning part!"
    python:
        time_display="Time not calculated"
        current_time=7*60+0
        timeSkips=[7*60+0,11*60+0,15*60+0,19*60+0]
        X=[0,0]
        outfit_responses=[
            ["Well...back to square one.",1,'c'],["We don't have pyjama CGs yet so we reused these casual ones.",1,'c'],["I'm not going to school today, "+player+"...",4,'b']]
        outfit_choices=[0,0,0]
        outfit_choice_count=0
        currently_read_manga=0
        asked_for_recipe=0
        ch_natsuki['call']=n
    jump bedroom_loop

label update_time_display:
    $ time_display=tdc(current_time)
    return

label update_bg_part_1(dayState=0):
    if dayState<2:
        scene bg natsukiroom_night
        return
    if dayState==2:
        scene bg natsukiroom_morning
        return
    if dayState<5:
        scene bg natsukiroom_day
        return
    if dayState==5:
        scene bg natsukiroom_evening
        return
    scene bg natsukiroom_night
    return
    

label bedroom_loop:
    $ timeState=current_time//(60*3)
    call update_bg_part_1(timeState%8)
    call char_v(ch_natsuki,None,)
    if n_outfit_mode==2:
        show natsuki 1a zorder 2 at h33
    elif n_outfit_mode==0:
        show natsuki 1pa zorder 2 at h33
    else:
        show natsuki 1ba zorder 2 at h33
    if current_time>=11*60+45:
        if current_time>=31*60:
            jump super_late_ending
        jump late_ending
    if current_time<7*60:
        jump cheater_ending
    call update_time_display
    menu:
        "Time: [time_display]"
        "Change clothes":
            $ decision=-1
            menu:
                "Pyjamas":
                    $ decision=0
                "Casual":
                    $ decision=1
                "School uniform":
                    $ decision=2
            if decision==n_outfit_mode:
                call char_v(ch_natsuki,"I\'m already wearing that, dummy!",None,1,None,'z')
                call char_s(ch_natsuki,"{nw}",1,'a')
            else:
                $ outfit_choice_count+=1
                if outfit_choice_count==20:
                    call char_s(ch_natsuki,"Jeez, can you make up your mind already?",4,'b')
                hide natsuki
                python:
                    pause(1)
                    current_time+=5
                    n_outfit_mode=decision
                    ch_natsuki['outfit']=n_outfits[n_outfit_mode]
                    decision=outfit_responses[n_outfit_mode]
                    outfit_responses[n_outfit_mode]=None
                    if decision is not None:
                        decision.extend([None,None,None])
                if n_outfit_mode==2:
                    show natsuki 1b zorder 2 at h33
                elif n_outfit_mode==0:
                    show natsuki 1pb zorder 2 at h33
                else:
                    show natsuki 1bb zorder 2 at h33
                if decision is not None:
                    call char_s(ch_natsuki,decision[0],decision[1],decision[2])
        "Check bus schedule":
            call check_bus_schedule
        "Go...":
            menu:
                "To the bathroom":
                    if chores[0]:
                        call char_s(ch_natsuki,"I already did what I need to do there!",1,"z")
                    else:
                        hide natsuki
                        n "You stay outside! I'm not giving you details about my bathroom routine!"
                        n "Not to mention we don't have a bathroom CG..."
                        $ pause(2)
                        "Ten minutes and a toilet flush later..."
                        $ current_time+=10
                        $ chores[0]=True
                "To the kitchen":
                    jump kitchen_loop_start
                "Back to bed":
                    $ decision=outfit_responses[0]
                    if decision==None:
                        call char_s(ch_natsuki,"Well, if you say so...",1,'d')
                        hide natsuki
                        scene bg natsukiroom_night
                        "And so, Natsuki went back to sleep and dreamed about kittens and cupcakes."
                        "Congratulations, you got the bad ending-"
                        "Hold on."
                        "Sorry, my bad. This is the BED ending."
                        call ending("BedEnding", "Bed ending")
                "(Back)":
                    pass
        "Look at bookshelf":
            if not chores[2]:
                hide natsuki
                "Natsuki has a huge manga collection."
                "Most of it is Parfait Girls, but there are also other slice-of life novels as well as...{nw}"
                if n_outfit_mode==2:
                    show natsuki 1b zorder 2 at h33
                elif n_outfit_mode==0:
                    show natsuki 1pb zorder 2 at h33
                else:
                    show natsuki 1bb zorder 2 at h33
                call char_v(ch_natsuki,"Hey! Are you listening to me?",None,1,None,'b')
                n "We need to put the manga back in order!"
                n "Here, take this box and sort the manga in it alphabetically first and numerically second!"
                call mangasort
                $ chores[2]=True
                scene bg bedroom
                if difficulty==0:
                    call char_v(ch_natsuki,"Oh, they're already sorted?",None,1,None,'c')
                    $ current_time+=5
                else:
                    python:
                        _a,_b=divmod(progress, difficulty)
                        _result=_a+int(_b!=0)
                    $ current_time+=5*_result
                    if _result<=2:
                        call char_s(ch_natsuki,"You're already done? Great!",1,'d')
                    elif _result<=6:
                        call char_s(ch_natsuki,"We're done!",1,'d')
                    else:
                        call char_s(ch_natsuki,"What took you so long?",1,'b')
            else:
                jump manga_talk
    jump bedroom_loop

label manga_talk:
    if currently_read_manga==0:
        call char_s(ch_natsuki,"We already sorted the manga!",1,'b')
        call char_s(ch_natsuki,"Although, I could read one new episode of Parfait Girls...",1,'c')
        menu:
            "Sure, why not?\n(Read Parfait Girls #[persistent.next_parfait])":
                $ pause(2)
                $ current_time+=30
                $ currently_read_manga+=1
                $ persistent.next_parfait+=1
                call char_s(ch_natsuki,"That was fun!",1,'d')
            "No.":
                call char_s(ch_natsuki,"Fine.",1,'b')
                jump bedroom_loop
    if currently_read_manga==1:
        call char_s(ch_natsuki,"Let's read another episode!",1,'c')
    if currently_read_manga<2:
        menu:
            "Sure, why not?\n(Read Parfait Girls #[persistent.next_parfait])":
                $ current_time+=30
                $ currently_read_manga+=1
                $ persistent.next_parfait+=1
            "No. We need to focus on the festival.":
                call char_s(ch_natsuki,"Fine.",1,'b')
                jump bedroom_loop
    $ loop_time=["Come on...","We have time for another one...","Let's read another episode!"]
    jump manga_loop_talk

label manga_loop_talk:
    $ loop_pop=loop_time.pop()
    call char_v(ch_natsuki,loop_pop,1,'c')
    menu:
        "Okay.\n(Read Parfait Girls #[persistent.next_parfait])":
            $ current_time+=30
            $ persistent.next_parfait+=1
        "No. We need to focus on the festival.":
            if loop_pop!="Come on...":
                jump manga_loop_talk
            call char_s(ch_natsuki,"Fine.",1,'b')
            jump bedroom_loop
    call char_s(ch_natsuki,"Let's read a few more!",1,'d')
    menu:
        "Yes.":
            pass
        "Yeah!":
            pass
        "Absolutely!":
            pass
        "You're not giving me a choice here, are you?":
            call char_s(ch_natsuki,"Nope!",1,'z')
        "Just Monika.":
            pass
        "...":
            pass
    hide natsuki
    $ persistent.next_parfait+=22
    "And so, Natsuki spent the rest of the day reading Parfait Girls."
    "Which was okay, because this reality is an illusion and there will be no consequences to her actions."
    "The Otaku Ending"
    call ending("MangaEnding", "The Otaku Ending")

label kitchen_loop_start:
    scene bg kitchen
    if n_outfit_mode==2:
        show natsuki 1a zorder 2 at h33
    elif n_outfit_mode==0:
        show natsuki 1pa zorder 2 at h33
    else:
        show natsuki 1ba zorder 2 at h33
    play music t6
    jump kitchen_loop

label kitchen_loop:
    if current_time>=11*60+45:
        jump late_ending
    call update_time_display
    menu:
        "Time: [time_display]"
        "Check bus schedule":
            call check_bus_schedule
        "Prepare supplies and ingredients":
            call prepare_supplies
        "Go back to bedroom":
            jump bedroom_loop
        "Go to [protag_name]'s house":
            jump p1_end
    jump kitchen_loop

label check_bus_schedule:
    call char_s(ch_natsuki,"There is a bus line passing near here every half an hour.",4,'c')
    python:
        a,b=divmod(current_time,30)
        nextbus=(a+int(b!=0))*30
        nb2=nextbus+30
        nb3=nb2+30
        dis_1=tdc(nextbus)
        dis_2=tdc(nb2)
        dis_3=tdc(nb3)
    n "Next few times are [dis_1], [dis_2] and [dis_3]."
    n "It will take me some time to carry the bag there..."
    n "...about 15 minutes, I guess..."
    n "...and if I don't make it on the 12:00 bus, we won't have enough time for baking."
    call char_s(ch_natsuki,"Better make every second count!",4,'d')
    $ current_time+=5
    return

label prepare_supplies:
    if asked_for_recipe==0:
        call char_s(ch_natsuki,"Um..."+player+"?",1,'c')
        python:
            F=open(config.basedir + "/characters/cupcake_recipe.txt","w")
            F.close()
            os.remove(config.basedir + "/characters/cupcake_recipe.txt")
        n "I can't find my cupcake recipe anywhere..."
        n "Can you check if it's in the game folder?"
        n "If you find it, copy it in the characters folder and choose this option again."
        $ asked_for_recipe=1
        $ current_time+=20
        return
    else:
        python:
            F=None
            try:
                F=renpy.file("../characters/cupcake_recipe.txt")
            except:
                F=None
        if F==None:
            call char_s(ch_natsuki,"I still can't find my cupcake recipe...",1,'c')
            n "Can you check if it's in the game folder?"
            n "It's named cupcake_recipe.txt"
            n "If you find it, copy it in the characters folder and choose this option again."
            $ current_time+=20
            return
        call char_s(ch_natsuki,"That's it!",1,'d')
        n "Now I just have to put all the ingredients in my bag..."
        "{i}Natsuki proceeds to fill her bag with cooking ingredients and supplies.{/i}"
        "{i}...{/i}"
        "{i}HOW DID SHE FIT A WHOLE OVEN IN THERE?!?{/i}"
        $ chores[1]=True
        $ current_time+=60
    return

label late_ending:
    call char_s(ch_natsuki,"We'll probably be late now...",1,'c')
    call char_s(ch_natsuki,"Might as well stay in and read Parfait Girls!",4,'z')
    hide natsuki
    $ persistent.next_parfait+=18
    "The procrastinator's ending"
    call ending("LateEnding", "The procrastinator's ending")
    $ renpy.quit()

label super_late_ending:
    call char_s(ch_natsuki,"How did you manage to spend 24 ingame hours on this part of the mod?!?",1,'b')
    hide natsuki
    $ persistent.next_parfait+=18
    "The dedicated time waster's ending"
    call ending("SuperLateEnding", "The dedicated time waster's ending")
    $ renpy.quit()

label cheater_ending:
    call char_s(ch_natsuki,"Wait a minute.",1,'b')
    call char_s(ch_natsuki,"You somehow cheated to lower the time!",4,'b')
    call char_s(ch_natsuki,"How - and more importantly, why - did you do this?",4,'b')
    $ delete_all_saves()
    call char_s(ch_natsuki,"Never mind. I just deleted all your saves.",5,'b')
    call char_s(ch_natsuki,"Goodbye.",5,'b')
    hide natsuki
    $ persistent.next_parfait+=18
    "The cheater's ending"
    call ending("CheaterEnding", "The cheater's ending")
    $ renpy.quit()

label p1_end:
    call char_s(ch_natsuki,None,4,'b')
    if n_outfit_mode==0:
        call char_s(ch_natsuki,"Seriously? In my pyjamas? Forget it!",)
        jump kitchen_loop
    if not chores[0]:
        call char_s(ch_natsuki,"I can't go to [protag_name]'s house like this, I'm not Sayori!")
        jump kitchen_loop
    if not chores[1]:
        call char_s(ch_natsuki,"And how exactly am I supposed to bake cupcakes without the ingredients?")
        n "It's not like I can magically bring cupcakes into existence or anything!"
        menu:
            "Okay, I got it.":
                jump kitchen_loop
            "...":
                pass
        call char_s(ch_natsuki,"...",4,'g')
        call char_s(ch_natsuki,"Okay, I can do that...",4,'c')
        call char_s(ch_natsuki,"But that would defeat the whole point of going to [protag_name]'s house to bake cupcakes!",4,'c')
        n "Let's just go back and get the ingredients, dummy!"
        jump kitchen_loop
    return

python:
    """ Unused broken code
        python:
            import hashlib
            _m=hashlib.sha256()
            _m.update(F.read())
            _c=_m.digest()
            _m=None
        if _c!="@qó-í&Œ£øªYAódáô-P­IÓÉ*":
            n "I don't think that's the recipe..."
            $ current_time+=20
            return
    """