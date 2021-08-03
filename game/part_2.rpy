python:
    F=open('images/protag/README.txt')
    TXT=F.read()
    F.close()
    protag_credit=Poem(author="Childish-N",name="Credit for MC sprite",text=TXT)

label p2_start:
    $ time+=75
    scene bg residential_day
    play music t2
    show natsuki 1bd zorder 3 at h32
    call pose_1d('And here we are! esdoflmfperdsmgviopredfnmgioprdfngwasd')
    $ mc_arrival_time=12*60
    n "Let me just check the time..."
    call update_time_display
    n "[time_display]..."
    if time<mc_arrival_time:
        n "[protag_name] is still at Sayori's place..."
        n "I have time to read some manga I brought with me while waiting for MC to show up..."
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
        n "'Sup?"
        protag "...Hey."
    stop music
    call pose_1c("Wait, we have to do this first...")
    call showpoem(protag_credit, music=False, revert_music=False)
    call pose_1b("There's also a new MC sprite, but that one just didn't seem right to me.")
    call pose_1d("Okay, we can continue now!")
    call pose_1a("{nw}")
    play music t2
    protag 1n ""
    $ pause(5)
    call pose_4c("Jeez, don't make it feel so awkward already!")
    n "It's gonna be a long afternoon, so don't be weird just because you're not used to seeing me outside of school."
    n "Anyway, I'm coming in."
    scene bg kitchen
    show natsuki 1bj zorder 2 at t11
    with wipeleft
    protag "I see you brought a lot of stuff..."
    call pose_2j("Well, I didn't want to come all this way to find out that your kitchen isn't equipped for the job.")
    n "You bought everything I asked you to, right?"
    protag "Yeah, I did."
    call pose_2l("Good!")
    n "Glad I could count on you to do your part."
    protag "Well...of course."
    protag "Anyway, let's go to the kitchen..."
    menu:
        "Carry the bag inside":
            protag "That bag looks pretty big. Are you sure you don't want me to carry it for you?"
            call pose_1c("No, I got it. Why?")
        "Ask MC to do it for you":
            call pose_2y("What, you're not even gonna offer to take this heavy bag from me?")
            n "Where's your hospitality, [protag_name]?"
            protag "Come on..."
            protag "Since when did I need to be a gentleman?"
            $ pause(1)
            protag "Ghk--"
            protag "This is ridiculously heavy--!"
            n 4bz "Ahaha!"
            n "I carried that all the way here."
            n 4bl "Are you impressed?"
            protag "I see now..."
            protag "Yeah, I am impressed, Natsuki."
            protag "It seems like I always underestimate you."
            call pose_2y("Ehehe~")
    n "It's because I'm so small, isn't it?"
    call pose_2a("You jerk.")
    protag "Hey, hey."
    protag "Your size has nothing to do with it."
    protag "Do you really hate being small that much?"
    n 1bk "Eh?"
    n "Um..."
    n 1bc "It's not like I hate it..."
    n "I mean, sometimes I like proving people wrong when they only think I'm worth my size."
    n 1ba "It's fun when I get to be small and also better than other people."
    n "But..."
    n 5bw "...Jeez, never mind!"
    n "What are you making me say?"
    n 5bq "Don't think you can make me talk about weird things just because we're not at school!"
    n "Are we getting started, or what? There's a lot of stuff I gotta teach you."
    protag "Ahaha."
    n 5bn "What??"
    protag "That's a little bit more like you."
    protag "You're more fun when you just speak your mind like that."
    n 1bm "H-Hey!"
    n "Now you {i}are{/i} treating me like a kid!"
    n "I was just trying to be a little nicer to you, you know."
    n 1br "And just because I don't have a mature and sexy figure like Yuri doesn't mean you should treat me like--"
    n 1bo "A-Ah--"
    n "{i}(I really shouldn't have said that...){/i}"
    protag "Natsuki..."
    n 1bp "Forget it!"
    n "I didn't say anything!"
    protag "I should apologize."
    n 1bh "Eh?"
    protag "I appreciate that you were trying to be nicer."
    protag "I should have been a little more considerate, too."
    protag "But also..."
    protag "If that's what you're thinking, then you should know that there are tons of guys who are into body types like yours."
    n 1bq "Ah..."
    n "How would...you know that, anyway?"
    protag "Just trust me on this one."
    n "..."
    n 5bx "...Gross."
    protag "Hey!"
    protag "Was that to me?"
    n 5bw "Who else?"
    protag "Man..."
    protag "Let's just get started already."
    n 2bl "Ahaha!"
    n "You get all sour when a girl calls you gross."
    n 2bd "I finally found your weakness, [player]."
    protag "Please spare me..."
    call recipe_quiz
    $ renpy.quit()
    "Well, if Natsuki decides to dish out more insults like that, there's no way I'm not fighting back."
    "But she's satisfied enough for now, finally starting to pull things out of her bag so we can get started."