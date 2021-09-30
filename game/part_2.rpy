label p2_start:
    $ current_time+=45 #between ??? and 12:45
    scene bg residential_day
    play music t5
    if n_outfit_mode==2:
        show natsuki 1d zorder 2 at h32
    else:
        show natsuki 1bd zorder 2 at h32
    call char_s(ch_natsuki,'And here we are!',1,'d')
    $ mc_arrival_time=12*60
    n "Let me just check the time..."
    call update_time_display
    n "[time_display]..."
    if current_time<mc_arrival_time:
        n "[protag_name] is still at Sayori's place..."
        n "I have time to read some manga I brought with me while waiting for [protag_name] to show up..."
        $ temp=(mc_arrival_time-current_time)//30
        $ currently_read_manga+=temp
        $ persistent.next_parfait+=temp
        $ current_time=mc_arrival_time # 12:00
        $ pause(3)
        show protag 4c zorder 3 at h33
        protag "Oh, you're already here!"
    else:
        n "[protag_name] should be home by now..."
        n "I'll let him know I'm here!"
        $ pause(1)
        $ current_time+=5 # between 12:05 and 12:50
        show protag 4c zorder 3 at h33
        n "'Sup?"
        protag "...Hey."
    stop music
    call char_s(ch_natsuki,"Wait, we have to do this first...",1,'c')
    call showpoem(protag_credit, music=False, revert_music=False)
    call char_s(ch_natsuki,"And this too...",1,'c')
    call showpoem(protag_casual_credit, music=False, revert_music=False)
    call char_s(ch_natsuki,"Also, SligtlySimple made the sprite you saw in the menu.",1,'d')
    call char_s(ch_natsuki,"There's also a new MC sprite, but that one just didn't seem right to me.".format(protag_name),1,'b')
    call char_s(ch_natsuki,"Okay, we can continue now!",1,'d')
    play music t5
    protag 1n "..."
    call char_s(ch_natsuki,"Jeez, don't make it feel so awkward already!",4,'c')
    n "It's gonna be a long afternoon, so don't be weird just because you're not used to seeing me outside of school."
    n "Anyway, I'm coming in."
    scene bg kitchen
    with wipeleft
    if n_outfit_mode==2:
        show natsuki 1j zorder 2 at h21
    else:
        show natsuki 1bj zorder 2 at h21
    show protag 1a zorder 2 at t22
    protag 1c "I see you brought a lot of stuff..."
    call char_s(ch_natsuki,"Well, I didn't want to come all this way to find out that your kitchen isn't equipped for the job.",2,'j')
    n "You bought everything I asked you to, right?"
    protag 1d "Yeah, I did."
    call char_s(ch_natsuki,"Good!",2,'l')
    n "Glad I could count on you to do your part."
    protag 2i "Well...of course."
    protag 1i "Anyway, let's go to the kitchen..."
    $ current_time+=5 # between 12:05 and 12:55
    menu:
        "Carry the bag yourself":
            protag 3i"That bag looks pretty big. Are you sure you don't want me to carry it for you?"
            call char_s(ch_natsuki,"No, I got it. Why?",1,'c')
        "Ask [protag_name] to do it for you":
            call char_s(ch_natsuki,"What, you're not even gonna offer to take this heavy bag from me?",2,'y')
            n "Where's your hospitality, [protag_name]?"
            protag "Come on..."
            protag "Since when did I need to be a gentleman?"
            $ pause(1)
            protag 1shock "Ghk--"
            protag 1r"This is ridiculously heavy--!"
            call char_s(ch_natsuki,"Ahaha!",4,'z')
            n "I carried that all the way here."
            call char_s(ch_natsuki,"Are you impressed?",4,'l')
            protag 2d "I see now..."
            protag 4c "Yeah, I am impressed, Natsuki."
            protag 3l "It seems like I always underestimate you."
            call char_s(ch_natsuki,"Ehehe~",2,'y')
            $ current_time+=10 # between 12:05 and 13:05
    n "It's because I'm so small, isn't it?"
    call char_s(ch_natsuki,"You jerk.",2,'a')
    protag 1k "Hey, hey."
    protag 1c "Your size has nothing to do with it."
    protag 1d "Do you really hate being small that much?"
    call char_s(ch_natsuki,"Eh?",1,'k')
    n "Um..."
    call char_s(ch_natsuki,"It's not like I hate it...",1,'c')
    n "I mean, sometimes I like proving people wrong when they only think I'm worth my size."
    call char_s(ch_natsuki,"It's fun when I get to be small and also better than other people.",1,'a')
    n "But..."
    call char_s(ch_natsuki,"...Jeez, never mind!",5,'w')
    n "What are you making me say?"
    call char_s(ch_natsuki,"Don't think you can make me talk about weird things just because we're not at school!",5,'q')
    n "Are we getting started, or what? There's a lot of stuff I gotta teach you."
    protag 1l "Ahaha."
    call char_s(ch_natsuki,"What??",5,'n')
    protag 1c "That's a little bit more like you."
    protag "You're more fun when you just speak your mind like that."
    call char_s(ch_natsuki,"H-Hey!",1,'m')
    n "Now you {i}are{/i} treating me like a kid!"
    n "I was just trying to be a little nicer to you, you know."
    call char_s(ch_natsuki,"And just because I don't have a mature and sexy figure like Yuri doesn't mean you should treat me like--",1,'r')
    stop music
    protag 1d "..."
    call char_s(ch_natsuki,"A-Ah--",1,'o')
    n "{i}(I really shouldn't have said that...){/i}"
    protag 1d "Natsuki..."
    call char_s(ch_natsuki,"Forget it!",1,'p')
    n "I didn't say anything!"
    protag 1s "I should apologize."
    call char_s(ch_natsuki,"Eh?",1,'h')
    play music t9
    protag "I appreciate that you were trying to be nicer."
    protag "I should have been a little more considerate, too."
    protag 1d "But also..."
    protag "If that's what you're thinking, then you should know that there are tons of guys who are into body types like yours."
    call char_s(ch_natsuki,"Ah...",1,'q')
    n "How would...you know that, anyway?"
    protag 1c "Just trust me on this one."
    stop music
    n "..."
    call char_s(ch_natsuki,"...Gross.",5,'x')
    play music t7
    protag 1shock "Hey!"
    protag "Was that to me?"
    call char_s(ch_natsuki,"Who else?",5,'w')
    protag 1d "Man..."
    protag "Let's just get started already."
    call char_s(ch_natsuki,"Ahaha!",2,'l')
    n "You get all sour when a girl calls you gross."
    call char_s(ch_natsuki,"I finally found your weakness, {}.".format(protag_name),2,'d')
    protag 1f "Please spare me..."
    $ current_time+=10 # between 12:15 and 13:15
    stop music
    call recipe_quiz
    
    scene bg kitchen
    play music t5
    $ current_time+=45 # between 13:00 and 14:00
    n "Before long, the whole kitchen is a mess."
    n "Spoons, dirty bowls, flour, spilled fluid, and plastic bags are strewn about every countertop."
    n "The mixer isn't big enough to make all the batter at once, so we've had to do it several times."
    n "Meanwhile, I am making sure [protag_name] doesn't mess up my cupcakes..."
    if n_outfit_mode==2:
        show natsuki 1k zorder 2 at h31
    else:
        show natsuki 1bk zorder 2 at h31
    call char_s(ch_natsuki,"{nw}",2,'k')
    n "[protag_name], where did you put the food coloring?"
    n "The batter's going in the oven soon, so I need to fill the trays."
    show protag 4d zorder 2 at t33
    protag 4d "I think it's still in the bag next to the table."
    protag "What are you using it for?"
    call char_s(ch_natsuki,"To color the batter, of course!",4,'l')
    call char_s(ch_natsuki,"I'm making each tray a different color.",4,'j')
    n "That way, even if the flavors aren't different, everyone can still pick their favorite."
    protag 3c "Ah, that's a cute idea."
    protag "Are we doing anything like that with the icing?"
    menu:
        "Of course!":
            call char_s(ch_natsuki,"Of course!",4,'d')
            n "(I separate the batter into smaller bowls and put a few drops of food coloring into each.)"
            protag "Ah, that looks pretty cool."
        "Do you want to?":
            call char_s(ch_natsuki,"Do you want to?",4,'k')
            protag 3d "Ah..."
            protag "You're asking me?"
            protag 3b "I don't really have a preference, so..."
            call char_s(ch_natsuki,"Come on...",1,'m')
            n "You're not putting any heart into this at all!"
            n "Can't you at least try to have fun?"
            protag 3d "I'm having fun..."
            n "(Meanwhile, I separate the batter into smaller bowls and put a few drops of food coloring into each.)"
            protag 3c "Ah, that does look pretty cool."
        "Nah, we're good.":
            call char_s(ch_natsuki,"Nah, we're good.",4,'c')
            protag 3c "Okay, I'll just finish the icing here..."
            jump p2_colorend
    $ current_time+=30 # between 13:00 and 14:30
    call char_s(ch_natsuki,"See?",2,'j')
    n "It's not like baking is just about following instructions."
    n "The presentation is where you get to be creative and have the most fun."
    n "It's a million times more worth it in the end if just looking at it makes everyone's eyes lighten up."
    protag 2k "Like the ones you made on my first day, huh?"
    n "(Sayori and Monika were delighted to see them.)"
    n "(I just wish I could say the same for Yuri...)"
    call char_s(ch_natsuki,"Yeah...",2,'c')
    protag "Maybe I will use the food coloring, then."
    call char_s(ch_natsuki,"Sounds like you're starting to understand.",4,'j')
    n "Just make sure you completely finish mixing the icing before you mess with the food coloring."
    protag "Yeah, it's getting there."
label p2_colorend:
    show black zorder 3
    "Later..."
    $ current_time+=60 # between 14:00 and 15:30
    scene bg kitchen
    hide black as fadeout
    if n_outfit_mode==2:
        show natsuki 1d zorder 2 at h31
    else:
        show natsuki 1bd zorder 2 at h31
    call char_s(ch_natsuki,"Ahh, that smells so good!",1,'d')
    "The cupcakes are ready to be pulled out of the oven."
    "As soon as Natsuki opens the oven door, a blast of sweet-smelling warm air fills the room."
    call char_s(ch_natsuki,"Look at how cute they all look!",4,'l')
    show protag 3c zorder 2 at h33
    protag 3c "They'll look even better once we add the icing."
    call char_s(ch_natsuki,"Not like you need to tell {i}me{/i} that!",2,'a')
    n "I brought decorating stuff, so I hope you can get creative."
    n "Here, scoop the icing into these bags."
    call char_s(ch_natsuki,"I have these nozzles that will make it look nice and fluffy.",2,'j')
    n "This one can even make flowers!"
    n "We probably won't be using it this time, though."
    protag 1d "What's this one for?"
    call char_s(ch_natsuki,"That one's really thin, so you can use it to make stripes or other patterns.",4,'k')
    n "But you can also use it to write stuff on a cake."
    n "Like, 'happy birthday!' or whatever."
    protag 2d "Huh, I see..."
    protag 4c "That gives me an idea, actually."
    n "Eh?"
    protag "Well, it's a literature event, right?"
    protag "We could make it more literature-themed by writing a different word on each of the cupcakes."
    protag "It would be fun to see people choose their cupcake based on a word they like."
    play music t6
    call char_s(ch_natsuki,"Uu...",1,'q')
    protag 4d "Hm?"
    n "I was kind of expecting you to say something really stupid..."
    call char_s(ch_natsuki,"But that's actually...a really cute idea, so...",1,'s')
    protag 3l "Ahaha."
    protag "Maybe I'm getting it from you."
    call char_s(ch_natsuki,"W-What's that supposed to mean?",5,'h')
    n "I'm not cute!"
    protag 3c "Come on..."
    protag "We're not at school, nobody's judging."
    protag "You can't dress and act like this and not expect me to think you're cute."
    call char_s(ch_natsuki,"W-Well...",5,'s')
    n "Same with you..."
    protag 2d "Eh?"
    protag "Did you say something?"
    call char_s(ch_natsuki,"N-No, nothing!",1,'w')
    n "Let's just do the icing!"
    stop music
    call char_s(ch_natsuki,"There's a lot to do, so we shouldn't be wasting time!",1,'h')
    n "Here, I'll show you how to do it."
    $ current_time+=30 # between 14:30 and 16:00
    $ outcome=-1

    call cupcake_defense
    
    play music t5
    scene bg kitchen with wipeleft_scene
    "When the duo is finally finished, Natsuki puts them all side by side to admire their work."
    if n_outfit_mode==2:
        show natsuki 1l zorder 2 at h31
    else:
        show natsuki 1bl zorder 2 at h31
    n "Look at how pretty they are together!"
    show protag 4c zorder 2 at h33
    protag 4c "Yeah, they are, aren't they?"
    call char_s(ch_natsuki,"Uu... I wish I could have one now!",1,'m')
    protag "Well, there's no reason you can't, right?"
    protag 3a "I don't see any harm in that."
    call char_s(ch_natsuki,"Well, yeah, but...",1,'c')
    show sayori 1l zorder 2 at h32
    play music t2
    s "Hello everyone!"
    protag 1c "Hi, Sayori!"
    show protag 1a zorder 3 at h33
    n "Sayori! What are you doing here?"
    s 1q "Monika and I finished early, and I was in a sunny mood so..."
    s 4l "Hey, cupcakes are done!"
    "Sayori immediately proceeds to reach for a tray of cupcakes."
    call char_s(ch_natsuki,"Hey! You can't do that!",4,'b')
    n "[protag_name], stop her!"
    if outcome==-1:
        jump p2_neither_win
    if outcome==0:
        jump p2_sayori_win
    if outcome==1:
        jump p2_protag_win
    if outcome==2:
        jump p2_neither_win

label p2_sayori_win:
    play music t7
    protag 3c "I'm sorry, Natsuki, but I'm afraid I can't do that."
    call char_s(ch_natsuki,"I'll do it myself, then!",4,'l')
    call char_s(ch_natsuki,None,4,'m')
    protag 1l "I can't let you do that, either..."
    show protag 1l zorder 3 at h42
    with wipeleft
    scene n_cg3_base
    show n_cg3_exp1
    with dissolve_cg
    hide sayori with wipeleft
    protag "Sayori, take the cupcakes and go in the living room! I'll be right behind you!"
    scene bg kitchen with dissolve_cg
    jump p2_either_win

label p2_protag_win:
    play music t8
    protag 3b "Sayori, I can't let you take these cupcakes..."
    call char_s(ch_natsuki,"YEAH!",1,'d')
    play music t7
    protag 1c "...because I'm going to take them instead!"
    show sayori 1m zorder 2 at h32
    call char_s(ch_natsuki,"WHAT?!?",1,'b')
    "[protag_name] grabs a tray of cupcakes and escapes to the living room."
    hide protag 
    n "No, [protag_name]! You were supposed to bring balance to the literature club, not join her!"
    s 1j "You better not eat all of them yourself, you meanie!"
    hide sayori with wipeleft
    jump p2_either_win

label p2_either_win:
    play music t8
    if n_outfit_mode==2:
        show natsuki 1l zorder 2 at h11
    else:
        show natsuki 1bl zorder 2 at h11
    call char_s(ch_natsuki,"You can't tell which one of them is worse...",4,'c')
    call char_s(ch_natsuki,"They really are made for each other, aren't they?",4,'d')
    call char_s(ch_natsuki,"I'll order some pizza so they back off the cupcakes.",4,'z')
    jump p2_pizza

label p2_neither_win:
    play music t8
    protag 1b "She's right, Sayori."
    protag "These cupcakes are for the festival."
    protag 1a "Let's order pizza instead."
    n "Thank you, [protag_name]."
    hide protag
    hide sayori
    if outcome==2:
        jump p2_monika_win
    jump p2_pizza

label p2_monika_win:
    play music t7g
    "A munching sound can be heard in the background."
    n "MONIKA?!?"
    n "WHAT ARE YOU DOING HERE?"
    m "Our world is a spare piece of a finished puzzle in a children's book."
    m "Nothing we do matters."
    m "Let me eat cupcakes in peace."
    protag 2t "Did you understand any of that?"
    s "Nope. Let's just leave them alone and order our pizza."
    jump p2_pizza

label p2_pizza:
    $ timeState=current_time//(60*3)
    call update_bg_part_2(timeState%8)
    with wipeleft_scene
    $ current_time+=30 # between 15:00 and 16:30
    show sayori 4x zorder 3 at h31
    stop music
    s "Finally..."
    s "I have you all to myself!"
    s "And I won't let anyone get between us~"
    s 4q "(Sayori picks up the last piece of pizza.)"
    play music t8
    show natsuki 1c zorder 3 at h32
    menu:
        "Ignore her.":
            protag 1l "You can forget about getting that slice now, Natsuki."
            show protag 1a zorder 3 at h33
        "Let [protag_name] know.":
            call char_s(ch_natsuki,"Hey, {}!".format(protag_name),1,'b')
            n "Your girlfriend is being a food yandere again!"
            show protag 1a zorder 3 at h33
            protag 1l "You can forget about getting that slice now, Natsuki."
            s 4o "Wait, did you just say..."
            call char_s(ch_natsuki,"Oh.",1,'c')
            n "You see, Sayori..."
            n "{i}Yandere{/i} is a term used for a person who is initially loving and caring to someone they have a strong affec{nw}"
            s 4m "No, not that word! The... uh... the g-word!"
            show protag 1j zorder 3 at h33
            s "Did you tell her we're dating, [protag_name]?"
            call char_s(ch_natsuki,"Oh, you two are finally admitting it?",1,'y')
            protag 1h "Huh?"
            call char_s(ch_natsuki,"You two have been acting like a couple for a year now!",1,'l')
            call char_s(ch_natsuki,"Walking to school together...",1,'d')
            n "Eating snacks together..."
            n "Seeing a therapist together..."
            n "Not to mention it took both you AND Monika to convince him to help one of us instead of you!"
            call char_s(ch_natsuki,"I call you Mr. and Mrs. Dense!",1,'l')
            show protag 1n zorder 3 at h33
            s 4w "Hey! I'm not dense!"
            n "Don't worry, Sayori - [protag_name] is dense and you just got his last name, hehe."
            s 4v "Still, that feels mean to [protag_name]"
            protag 1o "It's okay, I don't mind."
            protag 1m "But I'm glad to know you care, Sayori."
            s 1q "Of course I do, you lovable dummy!"
    jump p2_conversation_start

label update_bg_part_2(dayState=0):
    if dayState<2:
        scene bg living_room_night
        return
    if dayState==2:
        scene bg living_room_morning
        return
    if dayState<5:
        scene bg living_room_day
        return
    if dayState==5:
        scene bg living_room_evening
        return
    scene bg living_room_night
    return

label p2_conversation_start:
    python:
        bringable_topics_def=['first_date_natsuki','weather','poems']
        silent_topics_def=['first_date_protag','new_uses','unfinished']
        bringable_topics=bringable_topics_def[:]
        silent_topics=silent_topics_def[:]
        talkativity=5
        repeat_topics=True

label p2_conversation_loop:
    $ timeState=current_time//(60*3)
    call update_bg_part_2(timeState%8)
    if n_outfit_mode==2:
        show natsuki 1a zorder 2 at h32
    else:
        show natsuki 1ba zorder 2 at h32
    show sayori 1a zorder 2 at h31
    show protag 1a zorder 2 at h33
    if current_time>=18*60:
        jump talkative_ending
    if current_time<12*60:
        jump cheater_ending_2
    menu:
        "(Lead the conversation.)":
            $ talkativity+=0
            if talkativity>10:
                call protag_and_sayori_talk
            else:
                call natsuki_talk
        "(Let them bring up a topic.)":
            if talkativity==0:
                "..."
                n "(Maybe I should bring up a topic?)"
            else:
                $ talkativity-=0
                call protag_and_sayori_talk
        "(Politely excuse yourself.)":
            n "This was nice, but I have to go home now."
            s 1x "Bye, Natsuki!"
            protag 1c "Take care on the way home!"
            jump p2_end_cleanup
        "(Impolitely excuse yourself.)":
            n "Okay, I'm bored. Bye everyone!"
            s 1s "Bye, Natsuki!"
            protag 1h "...???"
            jump p2_end_cleanup
    jump p2_conversation_loop

label natsuki_talk:
    python:
        if bringable_topics==[] and repeat_topics:
            bringable_topics=bringable_topics_def[:]
        topic=random.choice(bringable_topics)
        bringable_topics.remove(topic)
    call expression "p2_talktopic_"+topic
    return

label protag_and_sayori_talk:
    python:
        if silent_topics==[] and repeat_topics:
            silent_topics=silent_topics_def[:]
        topic=random.choice(silent_topics)
        silent_topics.remove(topic)
    call expression "p2_talktopic_"+topic
    return

label talkative_ending:
    call char_s(ch_natsuki,"Wait, is it already dark?",1,'c')
    call ending("TalkativeEnding", "The talkative ending")

label p2_talktopic_first_date_protag:
    protag 1c "Do you remember our first date, Sayori?"
    s 1x "How could I forget?"
    s 1x "..."
    protag "Wait...you actually forgot?"
    call char_s(ch_natsuki,"(Let's hope no one notices this part was hastily done in the last minute.)",1,'d')
    call char_s(ch_natsuki,"(...)",1,'c')
    call char_s(ch_natsuki,"(Did I think this out loud?)",1,'p')
    return

label p2_talktopic_new_uses:
    s "I need your help with something, [protag_name]..."
    protag "What is it, cinnamon bun?"
    s "Well, there's this piece of rope I didn't see any use for since last year..."
    s "And I found some art ideas online I really like!"
    s "I just can't try some things from it myself..."
    s "Can you come to my house next weekend and help me with it?"
    protag "Sure, I'll gladly help you with your art project!"
    return

label p2_talktopic_first_date_natsuki:
    call char_s(ch_natsuki,"Do you two remember your first date?",1,'d')
    s 1x "How could I forget?"
    s 1x "..."
    protag "Wait...you actually forgot?"
    call char_s(ch_natsuki,"(Let's hope no one notices this part was hastily done in the last minute.)",1,'d')
    call char_s(ch_natsuki,"(...)",1,'c')
    call char_s(ch_natsuki,"(Did I think this out loud?)",1,'p')
    return

label p2_talktopic_poems:
    n "So, what did you have in mind for poems?"
    mc "Oh, I just found something online I'll try to recite."
    s "I tried a new style of poem!"
    n "Really?"
    s "Yeah! I wanted to challenge myself by trying something new!"
    protag "Can we hear it?"
    s "Sure!"
    "Sayori pulls out a piece of paper and clears her throat."
    s "GET OUT OF MY HEAD GET OUT OF MY HEAD GET OUT OF MY HEAD GET OUT OF MY HEAD{nw}"
    s "GET OUT OF MY HEAD GET OUT OF MY HEAD GET OUT OF MY HE-{nw}"
    n "FOR THE LOVE OF SALVATO, STOP THIS RIGHT NOW!"
    "..."
    s "But a poem is never finished."
    s "It just stops moving."
    protag "Uhhhhh..."
    n "...Maybe you should stick to your old style."
    return

label p2_talktopic_unfinished:
    s "Why aren't our faces moving?"
    n "Because this part has been rushed due to a self-imposed deadline on the mod release. Hopefully this will be fixed by release day."
    protag "What are you two talking about?"
    return

label p2_talktopic_weather:
    s "Nice weather, huh?"
    protag "Yeah!"

label p2_end_cleanup:
    hide sayori
    hide natsuki
    hide protag
    hide bg
    return