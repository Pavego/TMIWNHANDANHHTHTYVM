label p1_start:
    $ nat_curr_outfit = 2
    scene bg natsukiroom_morning
    show natsuki 1w zorder 2 at h33
    play music t6
    n "{i}yawn{/i}"
    n 1d "Good morning, [player]!"
    menu:
        "Good morning, Natsuki!":
            pass
        "...":
            pass
    n 1l "I had a great dream last night!"
    n 1z "I was sitting in a garden, surrounded by pink fluffy kittens!"
    n "They were so adorable!"
    n 1c "It almost made me wish I could stay asleep..."
    n 1l "But I have a feeling today is going to be great!"
    n "Father went on a business trip.."
    n 1z "(To the recycle bin...)"
    n 1d "And I'm going to [protag_name]'s house to bake cupcakes for the festival!"
    n 1c "Okay, let's see..."
    n "First, I need to get myself in order."
    n "I can't go there looking as messy as Sayori..."
    n "Seriously, why doesn't she care about her appearance in the slightest?"
    n "I also need to put all the stuff we'll need in my bag."
    n "I'm not sure if I can trust [protag_name] with getting the right ingredients..."
    n "And I should also rearrange my manga collection."
    n 1g "..."
    n 1d "Oh, I completely forgot about you!"
    n "You know what?"
    n "I'll let you do the routine planning part!"
    python:
        time_display = "Time not calculated"
        current_time = 7 * 60 + 0
        timeSkips = [7 * 60 + 0, 11 * 60 + 0, 15 * 60 + 0, 19 * 60 + 0]
        X = [0, 0]
        outfit_choices = [0, 0, 0]
        outfit_choice_count=0
        currently_read_manga=0
        asked_for_recipe=0
        decision = None
    jump bedroom_loop

label update_time_display:
    $ time_display = tdc(current_time)
    return

label update_bg_part_1(dayState=0):
    if dayState < 2:
        scene bg natsukiroom_night
        return
    if dayState == 2:
        scene bg natsukiroom_morning
        return
    if dayState < 5:
        scene bg natsukiroom_day
        return
    if dayState == 5:
        scene bg natsukiroom_evening
        return
    scene bg natsukiroom_night
    return
    

label bedroom_loop:
    $ timeState = current_time // (60 * 3)
    call update_bg_part_1(timeState % 8)
    show natsuki 1a zorder 2 at h33
    if current_time >= 11 * 60 + 45:
        if current_time >= 31 * 60:
            jump super_late_ending
        jump late_ending
    if current_time < 7 * 60:
        jump cheater_ending
    call update_time_display
    menu:
        "Time: [time_display]"
        "Change clothes":
            menu:
                "School uniform":
                    $ decision = 0
                "Casual":
                    $ decision = 1
                "Pyjamas":
                    $ decision = 2
            if decision == nat_curr_outfit:
                n 1z "I\'m already wearing that, dummy!"
                n 1a"{nw}"
            else:
                $ outfit_choice_count += 1
                if outfit_choice_count == 20:
                    n 4b "Jeez, can you make up your mind already?"
                hide natsuki
                $ renpy.pause(1.0, hard=True)
                $ nat_curr_outfit = decision
                if decision == 0:
                    show natsuki 4b zorder 2 at h33
                    n "I'm not going to school today, [player]..."
                elif decision == 1:
                    show natsuki 1c zorder 2 at h33
                    n "Well...back to square one."
                else:
                    show natsuki 1c zorder 2 at h33
                    n "Just FYI, you CAN affect what outfit I'll be wearing. There is a wrong choice, but there are at least 2 right ones."
        "Check bus schedule":
            call check_bus_schedule
        "Go...":
            menu:
                "To the bathroom":
                    if chores[0]:
                        n 1z "I already did what I need to do there!"
                    else:
                        hide natsuki
                        n "You stay outside! I'm not giving you details about my bathroom routine!"
                        n "Not to mention we don't have a bathroom CG..."
                        $ renpy.pause(2.0, hard=True)
                        "Ten minutes and a toilet flush later..."
                        $ current_time += 10
                        $ chores[0]=True
                "To the kitchen":
                    jump kitchen_loop_start
                "Back to bed":
                    if decision == None:
                        n 1d "Well, if you say so..."
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
                show natsuki 1b zorder 2 at h33
                n "Hey! Are you listening to me?"
                n "We need to put the manga back in order!"
                n "Here, take this box and sort the manga in it alphabetically first and numerically second!"
                call mangasort
                show natsuki 1b zorder 2 at h33
                $ chores[2] = True
                scene bg bedroom
                if difficulty == 0:
                    n 1c "Oh, they're already sorted?"
                    $ current_time += 5
                else:
                    python:
                        _a,_b = divmod(progress, difficulty)
                        _result = _a + int(_b != 0)
                    $ current_time += 5 * _result
                    if _result <= 2:
                        show natsuki 1d zorder 2 at h11
                        n "You're already done? Great!"
                    elif _result <= 6:
                        show natsuki 1d zorder 2 at h11
                        n "We're done!"
                    else:
                        show natsuki 1b zorder 2 at h11
                        n "What took you so long?"
            else:
                jump manga_talk
    jump bedroom_loop

label manga_talk:
    if currently_read_manga == 0:
        n 1b "We already sorted the manga!"
        n 1c "Although, I could read one new episode of Parfait Girls..."
        menu:
            "Sure, why not?\n(Read Parfait Girls #[persistent.next_parfait])":
                $ renpy.pause(2.0, hard=True)
                $ current_time += 30
                $ currently_read_manga += 1
                $ persistent.next_parfait += 1
                n 1d "That was fun!"
            "No.":
                n 1b "Fine."
                jump bedroom_loop
    if currently_read_manga == 1:
        n 1c "Let's read another episode!"
    if currently_read_manga < 2:
        menu:
            "Sure, why not?\n(Read Parfait Girls #[persistent.next_parfait])":
                $ current_time += 30
                $ currently_read_manga += 1
                $ persistent.next_parfait += 1
            "No. We need to focus on the festival.":
                n 1b "Fine."
                jump bedroom_loop
    $ loop_time = ["Come on...", "We have time for another one...", "Let's read another episode!"]
    jump manga_loop_talk

label manga_loop_talk:
    $ loop_pop = loop_time.pop()
    n 1c "[loop_pop]"
    menu:
        "Okay.\n(Read Parfait Girls #[persistent.next_parfait])":
            $ current_time += 30
            $ persistent.next_parfait += 1
        "No. We need to focus on the festival.":
            if loop_pop != "Come on...":
                jump manga_loop_talk
            n 1b "Fine."
            jump bedroom_loop
    n 1d "Let's read a few more!"
    menu:
        "Yes.":
            pass
        "Yeah!":
            pass
        "Absolutely!":
            pass
        "You're not giving me a choice here, are you?":
            n 1z "Nope!"
        "Just Monika.":
            pass
        "...":
            pass
    hide natsuki
    $ persistent.next_parfait += 22
    "And so, Natsuki spent the rest of the day reading Parfait Girls."
    "Which was okay, because this reality is an illusion and there will be no consequences to her actions."
    "The Otaku Ending"
    call ending("MangaEnding", "The Otaku Ending")

label kitchen_loop_start:
    scene bg kitchen
    show natsuki 1a zorder 2 at h33
    play music t6
    jump kitchen_loop

label kitchen_loop:
    if current_time >= 11 * 60 + 45:
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
    n 4c "There is a bus line passing near here every half an hour."
    python:
        a, b = divmod(current_time, 30)
        nextbus = (a + int(b != 0)) * 30
        nb2 = nextbus + 30
        nb3 = nb2 + 30
        dis_1 = tdc(nextbus)
        dis_2 = tdc(nb2)
        dis_3 = tdc(nb3)
    n "Next few times are [dis_1], [dis_2] and [dis_3]."
    n "It will take me some time to carry the bag there..."
    n "...about 15 minutes, I guess..."
    n "...and if I don't make it on the 12:00 bus, we won't have enough time for baking."
    n 4d "Better make every second count!"
    $ current_time += 5
    return

label prepare_supplies:
    python:
        if not os.path.isfile(user_dir + "/game/cupcake_recipe.txt"): open(user_dir + "/game/cupcake_recipe.txt", "wb").write(renpy.file("cupcake_recipe_template.txt").read())
    if not asked_for_recipe:
        n 1c "Um... [player]?"
        python:
            if os.path.isfile(user_dir + "/characters/cupcake_recipe.txt"): os.remove(user_dir + "/characters/cupcake_recipe.txt")
        n "I can't find my cupcake recipe anywhere..."
        n "Can you check if it's in the game folder?"
        n "If you find it, copy it in the characters folder and choose this option again."
        $ asked_for_recipe = 1
        $ current_time += 20
        return
    else:
        if not os.path.isfile(user_dir + "/characters/cupcake_recipe.txt"):
            n 1c"I still can't find my cupcake recipe..."
            n "Can you check if it's in the game folder?"
            n "It's named cupcake_recipe.txt"
            n "If you find it, copy it in the characters folder and choose this option again."
            $ current_time += 20
            return
        python:
            if os.path.isfile(user_dir + "/game/cupcake_recipe.txt"): os.remove(user_dir + "/game/cupcake_recipe.txt")
        n 1d "That's it!"
        n "Now I just have to put all the ingredients in my bag..."
        "{i}Natsuki proceeds to fill her bag with cooking ingredients and supplies.{/i}"
        "{i}...{/i}"
        "{i}HOW DID SHE FIT A WHOLE OVEN IN THERE?!?{/i}"
        $ chores[1] = True
        $ current_time += 60
    return

label late_ending:
    n 1c "We'll probably be late now..."
    n 4z "Might as well stay in and read Parfait Girls!"
    hide natsuki
    $ persistent.next_parfait += 18
    "The procrastinator's ending"
    call ending("LateEnding", "The procrastinator's ending")
    $ renpy.quit()

label super_late_ending:
    n 1b "How did you manage to spend 24 ingame hours on this part of the mod?!?"
    hide natsuki
    $ persistent.next_parfait += 18
    "The dedicated time waster's ending"
    call ending("SuperLateEnding", "The dedicated time waster's ending")
    $ renpy.quit()

label cheater_ending:
    n 1b "Wait a minute."
    n 4b "You somehow cheated to lower the time!"
    n "How - and more importantly, why - did you do this?"
    $ delete_all_saves()
    n 5b "Never mind. I just deleted all your saves."
    n "Goodbye."
    hide natsuki
    $ persistent.next_parfait += 18
    "The cheater's ending"
    call ending("CheaterEnding", "The cheater's ending")
    $ renpy.quit()

label p1_end:
    if nat_curr_outfit == 2:
        n 4b "Seriously? In my pyjamas? Forget it!"
        jump kitchen_loop
    if not chores[0]:
        n 4b "I can't go to [protag_name]'s house like this, I'm not Sayori!"
        jump kitchen_loop
    if not chores[1]:
        n 4b "And how exactly am I supposed to bake cupcakes without the ingredients?"
        n "It's not like I can magically bring cupcakes into existence or anything!"
        menu:
            "Okay, I got it.":
                jump kitchen_loop
            "...":
                pass
        n 4g "..."
        n 4c "Okay, I can do that..."
        n "But that would defeat the whole point of going to [protag_name]'s house to bake cupcakes!"
        n "Let's just go back and get the ingredients, dummy!"
        jump kitchen_loop
    return