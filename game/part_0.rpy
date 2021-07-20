label nat_welcome:
    $ silenceCount=0
    stop music
    m "Hello, [player]!"
    show monika_bg zorder 1
    play music m1 noloop
    m "How are you feeling today?"
    menu:
        "Great!":
            m "That's great to hear!"
        "Good.":
            m "Good to know!"
        "Okay...":
            menu:
                m "Are you sure?"
                "Yes.":
                    m "Well, I'll be here when you're ready to talk."
                "...No.":
                    m "It's okay, you don't have to pretend with me."
                    m "{b}*hugs*{/b} I am here for you."
                    $ pause(5.0)
        "...awful.":
            m "{b}*hugs*{/b} I am here for you."
            $ pause(5.0)
        "...":
            m "..."
            $ silenceCount+=1
    m "Now, where was I..."
    play music t7
    n "MONIKA!!!!!!!"
    show natsuki 1e zorder 2 at h22
    n "What are you doing here?"
    n "This is my mod and I get to talk to the player!"
    n 1w "I didn't spend all that time learning RenPy just so you can steal the show from me!"
    n "GET OUT!"
    stop music
    m "Okay, okay..."
    hide monika_bg
    call nat_welcoming
    call additional_questions
    call plot
    call proof_of_concept_intro
    return

label nat_welcoming:
    show monika_room zorder 0
    play music t3
    show natsuki 1c zorder 2 at t11
    n "Sorry about that, [player]."
    menu:
        "Hello, Natsuki!":
            n 1d "Hello, [player]!"
        "It's okay, Monika was nice.":
            n 4y "Oh, good... for her."
            n 4d "Anyway..."
        "Um, is Monika going to cause any trouble?":
            n 1d "I don't think so. She's been feeling a lot better ever since she has me to talk to."
            n 4d "Anyway..."
        "...":
            $ silenceCount+=1
    n 4d "Welcome to The Mod In Which Natsuki Has A Nice Day And Nothing Horrible Happens To Her, Thank You Very Much - a mod by yours truly!"
    menu:
        "Wow! You made this mod all by yourself?":
            n 1c "Well...MousePotatoDoesStuff helped me a bit..."
        "...":
            $ silenceCount+=1
            n 1l "Oh, and MousePotatoDoesStuff helped me a bit..."
    n 1c "...did most of the coding, actually..."
    n 1l "But I'm doing all the talking!"
    menu:
        "What is this mod, anyway?":
            n 4z "It's exactly what it says in the title, dummy!"
        "That title is, uhm...specific.":
            n 4z "I know, right? The mod pretty much describes itself!"
        "...":
            $ silenceCount+=1
            if silenceCount==4:
                n 1m "You know a dialogue is supposed to have two people talking?"
                n "Let's go back and try again..."
                jump nat_welcoming
            elif silenceCount==7:
                n 5w "I give up."
                n "Goodbye."
                $ persistent.endingsAchieved[1]+=1
                $ renpy.quit()
            else:
                n 1t "The mod pretty much describes itself!"
    n 1d "I intend to have a nice day with nothing horrible happening to me."
    n 1c "After so many mods using me for tragedy, I feel like I deserve at least that much..."
    return

label additional_questions:
    n 1d "Anything else you would like to know?"
    menu:
        "Is this a psychological horror mod?":
            player "Is the game going to pretend to be all nice and cutesy and then YOOOOOOOOOOOOOOOOOOOOOOOOOOO?"
            n 1b "No, it won't. That sounds like something Yuri would make, not me!"
            n 4b "You should know by now that I hate horror!"
            n 4i "Dummy..."
        "Will cupcakes be provided?":
            n 1z "Absolutely!"
            n 1d "In fact, they're a major part of the story!"
            n 5b "But I hope you didn't install this mod just for the cupcakes..."
        "I have some concerns about the lore...":
            n "We tried our best to adhere to the lore, but you might need to suspend your disbelief a little bit."
            n "After all, this is first and foremost a lighthearted slice-of-life mod."
        "Can I lewd you in this mod?":
            stop music
            play sound "sfx/slap.ogg"
            n 5e "{i}ABSOLUTELY NOT.{/i}"
            python:
                try: sys.modules['renpy.error'].report_exception("GET YOUR MIND OUT OF THE GUTTER!", False)
                except: pass
            $ renpy.quit()
        "...":
            n 4d "I'll take that as a sign you have no more questions."
            return
        "That's all for now.":
            n 4d "Okay, let's get started then!"
            return
    jump additional_questions

label nat_intro:
    show monika_room zorder 3
    n "Welcome back, [player]!"
    menu:
        n "How are you feeling today?"
        "Great!":
            n "That's great to hear!"
        "Good.":
            n "Good to know!"
        "Okay...":
            menu:
                n "Are you sure?"
                "Yes.":
                    n "Well, in that case "
                "...No.":
                    n "It's okay, you don't have to pretend with me."
                    n "{b}*hugs*{/b} I am here for you."
                    $ pause(5.0)
                    n "Uuuuuu..."
                    n "But it's not like I like you or anything!"
                    n "Let's just go on and pretend this didn't happen. GOT IT?"
        "...awful.":
            m "{b}*hugs*{/b} I am here for you."
            $ pause(5.0)
            m "Uuuuuu..."
            m "But it's not like I like you or anything!"
        "...":
            m "..."
            $ silenceCount+=1
    n "Let's jump straight into the plot!"
    return

label plot:
    n 1d "So, here's the plan:"
    n "We are going to skip the whole workweek and go straight to the Sunday chapter!"
    n 4d "Also, you won't be controlling MC in this mod..."
    n 4c "...not that you had much control to begin with..."
    n 4d "Instead, you'll be joining me!"
    n "That's right - I'm the true MC of this story!"
    n "Are you ready?"
    menu:
        "Yes.":
            n "Let's go, then!"
        "No.":
            n 4z "Well, too bad!"
    hide natsuki
    hide monika_room fadeout 2
    stop music
    $ pause(1)
    return

label proof_of_concept_intro:
    $ persistent.endingsAchieved[0]+=1
    $ a=persistent.endingsAchieved[0]
    $ b=persistent.endingsAchieved[1]
    moddev "This is the true ending of the demo."
    moddev "You completed this demo [a] times."
    if b!=0:
        moddev "You also ended the demo early with silence [b] times."
    moddev "I didn't track how many times you reached the bad \"ending\"."
    moddev "If it's more than zero, I'm going to give you the benefit of doubt and assume you did it out of curiosity."
    moddev "Thank you for playing this very early version of The Mod In Which Natsuki Has A Nice Day And Nothing Horrible Happens To Her, Thank You Very Much!"
    moddev "(TMIWNHANDANHHTHTYVM for short)"
    moddev "I hope you liked it..."
    moddev "All feedback is greatly appreciated!"
    moddev "Bye!"
    return