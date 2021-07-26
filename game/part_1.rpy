label p1_start:
    scene bg bedroom
    show natsuki 1bw zorder 2 at h33
    play music t6
    n "{i}yawn{/i}"
    n 1bd "Good morning, [player]!"
    menu:
        "Good morning, Natsuki!":
            pass
        "...":
            pass
    n 1bl "I had a great dream last night!"
    n 1bz "I was sitting in a garden, surrounded by pink fluffy kittens!"
    n "They were so adorable!"
    n 1bc "It almost made me wish I could stay asleep..."
    n 1bl "But I have a feeling today is going to be great!"
    n "Father went on a business trip.."
    n 1bz "(To the recycle bin...)"
    n 1bd "And I'm going to MC's house to bake cupcakes for the festival!"
    n 1bc "Okay, let's see..."
    n "First, I need to get myself in order."
    n "I can't go there looking as messy as Sayori..."
    n "Seriously, why doesn't she care about her appearance in the slightest?"
    n "I also need to put all the stuff we'll need in my bag."
    n "I'm not sure if I can trust MC with getting the right ingredients..."
    n "And I should also rearrange my manga collection."
    n 1bg "..."
    n 1bd "Oh, I completely forgot about you!"
    n "You know what?"
    n "I'll let you do the routine planning part!"
    $ time_display="Time not calculated"
    $ time=7*60+0
    $ X=[0,0]
    $ outfit_responses=["Well...back to square one.","We don't have pyjama CGs yet so we reused these casual ones.","I'm not going to school today, "+player+"..."]
    $ outfit_choice_count=0
    $ currently_read_manga=0
    $ asked_for_recipe=0
    jump bedroom_loop

label update_time_display:
    $ time_display=tdc(time)
    return

label bedroom_loop:
    scene bg bedroom
    show natsuki 1ba zorder 2 at h33
    if time>=11*60+45:
        jump late_ending
    call pose_1a('{nw}')
    call update_time_display
    menu:
        "Time: [time_display]"
        "Change clothes":
            $ choice=-1
            menu:
                "Pyjamas":
                    $ choice=0
                "Casual":
                    $ choice=1
                "School uniform":
                    $ choice=2
            if choice==n_outfit_mode:
                call pose_1z("I\'m already wearing that, dummy!")
                call pose_1a("{nw}")
            else:
                $ outfit_choice_count+=1
                if outfit_choice_count==20:
                    call pose_4b("Jeez, can you make up your mind already?")
                hide natsuki
                python:
                    pause(1)
                    time+=5
                    n_outfit_mode=choice
                    n_outfit=n_outfits[n_outfit_mode]
                    choice=outfit_responses[n_outfit_mode]
                    outfit_responses[n_outfit_mode]="{nw}"
                show natsuki 1a zorder 2 at h33
                if choice!="":
                    if n_outfit_mode==0:
                        call pose_1c(choice)
                    elif n_outfit_mode==1:
                        call pose_4d(choice)
                    elif n_outfit_mode==2:
                        call pose_4b(choice)
        "Check bus schedule":
            call check_bus_schedule
        "Go...":
            menu:
                "To the bathroom":
                    hide natsuki
                    n "You stay outside! I'm not giving you details about my bathroom routine!"
                    n "Not to mention we don't have a bathroom CG..."
                    $ pause(2)
                    "Ten minutes and a toilet flush later..."
                    $ time+=10
                    $ chores[0]=True
                "To the kitchen":
                    jump kitchen_loop_start
                "Back to bed":
                    $ choice=outfit_responses[0]
                    "[choice]???"
                    if choice=="{nw}":
                        call pose_1d("Well, if you say so...")
                        hide natsuki
                        "And so, Natsuki went back to sleep and dreamed about kittens and cupcakes."
                        "Congratulations, you got the bad ending-"
                        "Hold on."
                        "Sorry, my bad. This is the BED ending."
                        $ renpy.quit()
                "(Back)":
                    pass
        "Look at bookshelf":
            if not chores[2]:
                hide natsuki
                "Natsuki has a huge manga collection."
                "Most of it is Parfait Girls, but there are also other slice-of life novels as well as...{nw}"
                show natsuki 1b zorder 2 at h11
                call pose_1b("Hey! Are you listening to me?")
                n "We need to put the manga back in order!"
                n "Here, take this box and sort the manga in it alphabetically first and numerically second!"
                call mangasort
                $ chores[2]=True
                scene bg bedroom
                if difficulty==0:
                    call pose_1c("Oh, they're already sorted?")
                    $ time+=5
                else:
                    python:
                        _a,_b=divmod(progress, difficulty)
                        _result=_a+int(_b!=0)
                    $ time+=5*_result
                    if _result<=2:
                        call pose_1d("You're already done? Great!")
                    elif _result<=6:
                        call pose_1d("We're done!")
                    else:
                        call pose_1b("What took you so long?")
            else:
                jump manga_talk
    jump bedroom_loop

label manga_talk:
    if currently_read_manga==0:
        call pose_1b("We already sorted the manga!")
        call pose_1c("Although, I could read one new episode of Parfait Girls...")
        menu:
            "Sure, why not?\n(Read Parfait Girls #[persistent.next_parfait])":
                $ pause(2)
                $ time+=30
                $ currently_read_manga+=1
                $ persistent.next_parfait+=1
                call pose_1d("That was fun!")
            "No.":
                call pose_1b("Fine.")
                jump bedroom_loop
    if currently_read_manga==1:
        call pose_1c("Let's read another episode!")
    if currently_read_manga<2:
        menu:
            "Sure, why not?\n(Read Parfait Girls #[persistent.next_parfait])":
                $ time+=30
                $ currently_read_manga+=1
                $ persistent.next_parfait+=1
            "No. We need to focus on the festival.":
                call pose_1b("Fine.")
                jump bedroom_loop
    $ loop_time=["Come on...","We got time for another one...","Let's read another episode!"]
    jump manga_loop_talk

label manga_loop_talk:
    $ loop_pop=loop_time.pop()
    call pose_1c(loop_pop)
    menu:
        "Okay.\n(Read Parfait Girls #[persistent.next_parfait])":
            $ time+=30
            $ persistent.next_parfait+=1
        "No. We need to focus on the festival.":
            if loop_pop!="Come on...":
                jump manga_loop_talk
            call pose_1b("Fine.")
            jump bedroom_loop
    call pose_1d("Let's read a few more!")
    menu:
        "Yes.":
            pass
        "Yeah!":
            pass
        "Absolutely!":
            pass
        "You're not giving me a choice here, are you?":
            call pose_1z("Nope!")
        "Just Monika.":
            pass
        "...":
            pass
    hide natsuki
    $ persistent.next_parfait+=22
    "And so, Natsuki spent the rest of the day reading Parfait Girls."
    "Which was okay, because this reality is an illusion and there will be no consequences to her actions."
    "Manga Ending" # ending
    $ renpy.quit()

label kitchen_loop_start:
    scene bg kitchen
    show natsuki 1ba zorder 2 at h33
    play music t6
    jump kitchen_loop

label kitchen_loop:
    if time>=11*60+45:
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
        "Go to MC's house":
            jump p1_end
    jump kitchen_loop

label check_bus_schedule:
    call pose_4b("There is a bus line passing near here every half an hour.")
    python:
        a,b=divmod(time,30)
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
    call pose_4d("Better make every second count!")
    $ time+=5
    return

label prepare_supplies:
    if asked_for_recipe==0:
        call pose_1c("Um..."+player+"?")
        $ os.delete("../characters/cupcake_recipe.txt")
        n "I can't find my cupcake recipe anywhere..."
        n "Can you check if it's in the game folder?"
        n "If you find it, copy it in the characters folder and choose this option again."
        $ asked_for_recipe=1
        $ time+=20
        return
    else:
        python:
            F=None
            try:
                F=renpy.file("../characters/cupcake_recipe.txt")
            except:
                F=None
        if F==None:
            call pose_1c("I still can't find my cupcake recipe...")
            n "Can you check if it's in the game folder?"
            n "If you find it, copy it in the characters folder and choose this option again."
            $ time+=20
            return
        call pose_1d("That's it!")
        n "Now I just have to put all the ingredients in my bag..."
        "{i}Natsuki proceeds to fill her bag with cooking ingredients and supplies.{/i}"
        "{i}...{/i}"
        "{i}HOW DID SHE FIT A WHOLE OVEN IN THERE?!?{/i}"
        $ chores[1]=True
        $ time+=60
    return

label late_ending:
    call pose_1b("We'll probably be late now...")
    call pose_4z("Might as well stay in and read Parfait Girls!")
    hide natsuki
    "The procrastinator's ending"
    $ renpy.quit()

label p1_end:
    if n_outfit_mode==0:
        call pose_4b("Seriously? In my pyjamas? Forget it!")
        jump kitchen_loop
    if not chores[0]:
        call pose_4b("I can't go to MC's house like this, I'm not Sayori!")
        jump kitchen_loop
    if not chores[1]:
        call pose_4b("And how exactly am I supposed to bake cupcakes without the ingredients?")
        n "It's not like I can magically bring cupcakes into existence or anything!"
        menu:
            "Okay, I got it.":
                jump kitchen_loop
            "...":
                pass
        call pose_4g("...")
        call pose_4c("Okay, I can do that...")
        call pose_4c("But that would defeat the whole point of going to MC's house to bake cupcakes!")
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
            $ time+=20
            return
    """