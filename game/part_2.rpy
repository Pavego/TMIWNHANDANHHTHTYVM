label p2_start:
    $ time+=75
    scene bg residential_day
    play music t2
    if n_outfit_mode==2:
        show natsuki 1d zorder 2 at h32
    else:
        show natsuki 1bd zorder 2 at h32
    call pose_1d('And here we are!')
    $ mc_arrival_time=12*60
    n "Let me just check the time..."
    call update_time_display
    n "[time_display]..."
    if time<mc_arrival_time:
        n "[protag_name] is still at Sayori's place..."
        n "I have time to read some manga I brought with me while waiting for [protag_name] to show up..."
        $ temp=(mc_arrival_time-time)//30
        $ currently_read_manga+=temp
        $ persistent.next_parfait+=temp
        $ time=mc_arrival_time
        show protag 4c zorder 3 at h33
        protag "Oh, you're already here!"
    else:
        n "[protag_name] should be home by now..."
        n "I'll let him know I'm here!"
        $ pause(5)
        $ time+=5
        show protag 4c zorder 3 at h33
        n "'Sup?"
        protag "...Hey."
    stop music
    call pose_1c("Wait, we have to do this first...")
    call showpoem(protag_credit, music=False, revert_music=False)
    call pose_1b("There's also a new {} sprite, but that one just didn't seem right to me.".format(protag_name))
    call pose_1d("Okay, we can continue now!")
    play music t2
    protag 1n "..."
    call pose_4c("Jeez, don't make it feel so awkward already!")
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
    call pose_2j("Well, I didn't want to come all this way to find out that your kitchen isn't equipped for the job.")
    n "You bought everything I asked you to, right?"
    protag 1d "Yeah, I did."
    call pose_2l("Good!")
    n "Glad I could count on you to do your part."
    protag 2i "Well...of course."
    protag 1i "Anyway, let's go to the kitchen..."
    menu:
        "Carry the bag yourself":
            protag 3i"That bag looks pretty big. Are you sure you don't want me to carry it for you?"
            call pose_1c("No, I got it. Why?")
        "Ask [protag_name] to do it for you":
            call pose_2y("What, you're not even gonna offer to take this heavy bag from me?")
            n "Where's your hospitality, [protag_name]?"
            protag "Come on..."
            protag "Since when did I need to be a gentleman?"
            $ pause(1)
            protag 1shock "Ghk--"
            protag 1r"This is ridiculously heavy--!"
            call pose_4z("Ahaha!")
            n "I carried that all the way here."
            call pose_4l("Are you impressed?")
            protag 2d "I see now..."
            protag 4c "Yeah, I am impressed, Natsuki."
            protag 3l "It seems like I always underestimate you."
            call pose_2y("Ehehe~")
    n "It's because I'm so small, isn't it?"
    call pose_2a("You jerk.")
    protag 1k "Hey, hey."
    protag 1c "Your size has nothing to do with it."
    protag 1d "Do you really hate being small that much?"
    call pose_1k("Eh?")
    n "Um..."
    call pose_1c("It's not like I hate it...")
    n "I mean, sometimes I like proving people wrong when they only think I'm worth my size."
    call pose_1a("It's fun when I get to be small and also better than other people.")
    n "But..."
    call pose_5w("...Jeez, never mind!")
    n "What are you making me say?"
    call pose_5q("Don't think you can make me talk about weird things just because we're not at school!")
    n "Are we getting started, or what? There's a lot of stuff I gotta teach you."
    protag 1l "Ahaha."
    call pose_5n("What??")
    protag 1c "That's a little bit more like you."
    protag "You're more fun when you just speak your mind like that."
    call pose_1m("H-Hey!")
    n "Now you {i}are{/i} treating me like a kid!"
    n "I was just trying to be a little nicer to you, you know."
    call pose_1r("And just because I don't have a mature and sexy figure like Yuri doesn't mean you should treat me like--")
    call pose_1o("A-Ah--")
    n "{i}(I really shouldn't have said that...){/i}"
    protag 1d "Natsuki..."
    call pose_1p("Forget it!")
    n "I didn't say anything!"
    protag 1s "I should apologize."
    call pose_1h("Eh?")
    protag "I appreciate that you were trying to be nicer."
    protag "I should have been a little more considerate, too."
    protag 1d "But also..."
    protag "If that's what you're thinking, then you should know that there are tons of guys who are into body types like yours."
    call pose_1q("Ah...")
    n "How would...you know that, anyway?"
    protag 1c "Just trust me on this one."
    n "..."
    call pose_5x("...Gross.")
    protag 1shock "Hey!"
    protag "Was that to me?"
    call pose_5w("Who else?")
    protag 1d "Man..."
    protag "Let's just get started already."
    call pose_2l("Ahaha!")
    n "You get all sour when a girl calls you gross."
    call pose_2d("I finally found your weakness, {}.".format(protag_name))
    protag 1f "Please spare me..."
    call recipe_quiz
    
    scene bg kitchen
    n "Before long, the whole kitchen is a mess."
    n "Spoons, dirty bowls, flour, spilled fluid, and plastic bags are strewn about every countertop."
    n "The mixer isn't big enough to make all the batter at once, so we've had to do it several times."
    n "Meanwhile, I am making sure [protag_name] doesn't mess up my cupcakes..."
    if n_outfit_mode==2:
        show natsuki 1k zorder 2 at h33
    else:
        show natsuki 1bk zorder 2 at h33
    call pose_2k("{nw}")
    n "[protag_name], where did you put the food coloring?"
    n "The batter's going in the oven soon, so I need to fill the trays."
    show protag 4d zorder 2 at t22
    protag 4d "I think it's still in the bag next to the table."
    protag "What are you using it for?"
    call pose_4l("To color the batter, of course!")
    call pose_4j("I'm making each tray a different color.")
    n "That way, even if the flavors aren't different, everyone can still pick their favorite."
    protag 3c "Ah, that's a cute idea."
    protag "Are we doing anything like that with the icing?"
    menu:
        "Of course!":
            call pose_4d("Of course!")
            n "(I separate the batter into smaller bowls and put a few drops of food coloring into each.)"
            protag "Ah, that looks pretty cool."
        "Do you want to?":
            call pose_4k("Do you want to?")
            protag 3d "Ah..."
            protag "You're asking me?"
            protag 3b "I don't really have a preference, so..."
            call pose_1m("Come on...")
            n "You're not putting any heart into this at all!"
            n "Can't you at least try to have fun?"
            protag 3d "I'm having fun..."
            n "(Meanwhile, I separate the batter into smaller bowls and put a few drops of food coloring into each.)"
            protag 3c "Ah, that does look pretty cool."
        "Nah, we're good.":
            call pose_4c("Nah, we're good.")
            protag 3c "Okay, I'll just finish the icing here..."
            jump p2_colorend
    call pose_2j("See?")
    n "It's not like baking is just about following instructions."
    n "The presentation is where you get to be creative and have the most fun."
    n "It's a million times more worth it in the end if just looking at it makes everyone's eyes lighten up."
    protag 2k "Like the ones you made on my first day, huh?"
    n "(Sayori and Monika were delighted to see them.)"
    n "(I just wish I could say the same for Yuri...)"
    protag 2c "Yeah..."
    protag "Maybe I will use the food coloring, then."
    n "Sounds like you're starting to understand."
    n "Just make sure you completely finish mixing the icing before you mess with the food coloring."
    protag "Yeah, it's getting there."
label p2_colorend:
    show black zorder 3
    "Later..."
    scene bg kitchen
    hide black as fadeout
    n "Ahh, that smells so good!"
    "The cupcakes are ready to be pulled out of the oven."
    "As soon as Natsuki opens the oven door, a blast of sweet-smelling warm air fills the room."
    call pose_4l("Look at how cute they all look!")
    protag 3c "They'll look even better once we add the icing."
    call pose_2a("Not like you need to tell {i}me{/i} that!")
    n "I brought decorating stuff, so I hope you can get creative."
    n "Here, scoop the icing into these bags."
    call pose_2j("I have these nozzles that will make it look nice and fluffy.")
    n "This one can even make flowers!"
    n "We probably won't be using it this time, though."
    protag 1d "What's this one for?"
    call pose_4k("That one's really thin, so you can use it to make stripes or other patterns.")
    n "But you can also use it to write stuff on a cake."
    n "Like, 'happy birthday!' or whatever."
    protag 2d "Huh, I see..."
    protag 4c "That gives me an idea, actually."
    n "Eh?"
    protag "Well, it's a literature event, right?"
    protag "We could make it more literature-themed by writing a different word on each of the cupcakes."
    protag "It would be fun to see people choose their cupcake based on a word they like."
    call pose_1q("Uu...")
    protag 4d "Hm?"
    n "I was kind of expecting you to say something really stupid..."
    call pose_1s("But that's actually...a really cute idea, so...")
    protag 3l "Ahaha."
    protag "Maybe I'm getting it from you."
    call pose_5h("W-What's that supposed to mean?")
    n "I'm not cute!"
    protag 3c "Come on..."
    protag "We're not at school, nobody's judging."
    protag "You can't dress and act like this and not expect me to think you're cute."
    call pose_5s("W-Well...")
    n "Same with you..."
    protag 2d "Eh?"
    protag "Did you say something?"
    call pose_1w("N-No, nothing!")
    n "Let's just do the icing!"
    call pose_1h("There's a lot to do, so we shouldn't be wasting time!")
    n "Here, I'll show you how to do it."
    $ outcome=-1

    call cupcake_defense
    
    play music t2
    scene bg kitchen with wipeleft_scene
    "When the duo is finally finished, Natsuki puts them all side by side to admire their work."
    if n_outfit_mode==2:
        show natsuki 1l zorder 2 at h31
    else:
        show natsuki 1bl zorder 2 at h31
    n "Look at how pretty they are together!"
    show protag 4c zorder 2 at h33
    protag 4c "Yeah, they are, aren't they?"
    call pose_1m("Uu... I wish I could have one now!")
    protag "Well, there's no reason you can't, right?"
    protag 3a "I don't see any harm in that."
    call pose_1c("Well, yeah, but...")
    show sayori 1l zorder 2 at h32
    s "Hello everyone!"
    protag 1c "Hi, Sayori!"
    show protag 1a zorder 3 at h33
    n "Sayori! What are you doing here?"
    s 1q "Monika and I finished early, and I was in a sunny mood so..."
    s 4l "Hey, cupcakes are done!"
    "Sayori immediately proceeds to reach for a tray of cupcakes."
    call pose_4b("Hey! You can't do that!")
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
    protag 3c "I'm sorry, Natsuki, but I'm afraid I can't do that."
    call pose_4l("I'll do it myself, then!")
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
    protag 3b "Sayori, I can't let you take these cupcakes..."
    call pose_1d("YEAH!")
    protag 1c "...because I'm going to take them instead!"
    show sayori 1m zorder 2 at h32
    call pose_1c("WHAT?!?")
    "[protag_name] grabs a tray of cupcakes and escapes to the living room."
    hide protag 
    n "No, [protag_name]! You were supposed to bring balance to the literature club, not join her!"
    s 1j "You better not eat all of them yourself, you meanie!"
    hide sayori with wipeleft
    jump p2_either_win

label p2_either_win:
    if n_outfit_mode==2:
        show natsuki 1l zorder 2 at h11
    else:
        show natsuki 1bl zorder 2 at h11
    call pose_4c("You can't tell which one of them is worse...")
    call pose_4d("They really are made for each other, aren't they?")
    return

label p2_neither_win:
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
    scene bg kitchen
    with wipeleft_scene
    s "Finally..."
    s "I have you all to myself!"
    s "And I won't let anyone get between us~"
    s "(Sayori picks up the last piece of pizza.)"
    menu:
        "Ignore her.":
            pass
        "Let [protag_name] know.":
            n "Hey, [protag_name]!"
            n "Your girlfriend is being a food yandere again!"
            protag 1l "You can forget about getting that slice now, Natsuki."
            # sayori shocked
            s "Wait, did you just say..."
            n "Oh."
            n "You see, Sayori..."
            n "{i}Yandere{/i} is a term used for a person who is initially loving and caring to someone they have a strong affec{nw}"
            s "No, not that word! The... uh... the g-word!"
            s "Did you tell her we're dating, [protag_name]?"
            n "Oh, you two are finally admitting it?"
            protag "Huh?"
            n "You two have been acting like a couple for a year now!"
            n "Not to mention it took both you and Monika to convince him to help one of us instead of you..."
    return