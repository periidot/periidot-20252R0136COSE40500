# Dedicated for my bsf with the loveliest OCs (if you're taking peeks at code ily). I've drawn them a 100 times

$ renpy.music.set_volume(0.15,0,"audio")
define x = Character("Pokki")
define g = Character("???")
define mc = Character("[You]")
define y = Character("Stranger")

default affinity = 5
default spc = 0
default chaos = 0
default foob = 0

default he = "he"
default hes = "he's"
default doesnt = "doesn't"
default him = "him"
default his = "his"
default is_ = "is"
default was = "was"
default has = "has"
default s = "s"
default es = "es"
default ies = "ies"
default self = "self"
default He = "He"
default Hes = "He's"
default Doesnt = "Doesn't"
default Him = "Him"
default His = "His"
default boy = "boy"
default Boy = "Boy"
default Hiss = "His"
default hiss ="His"
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist
                self.child = child
                
            def __call__(self, t, sizes):                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)


label start:

    menu:
        "My pronouns are..."
        "She/her!":
            jump she
        "They/them!":
            jump they
        "He/him!":
            jump continue

label she:
    $ he, him, his, boy, hes, doesnt, hiss = "she", "her", "her", "girl", "she's", "doesn't", "hers"
    $ He, Him, His, Boy, Hes, Doesnt, Hiss = "She", "Her", "Her", "Girl", "She's", "Doesn't", "Hers"
    jump continue

label they:
    $ he, him, his, boy, hes, doesnt, hiss = "they", "them", "their", "pet", "they're", "don't", "theirs"
    $ He, Him, His, Boy, Hes, Doesnt, Hiss = "They", "Them", "Their", "Pet", "They're", "Don't", "Theirs"
    $ is_, was, s, es = "are", "were", "", ""
    $ ies, has = "y", "have"
    jump continue


image bruh:
    contains:
        "bg.webp"
    contains:
        "curtains.webp"

label continue:

    """Tip of the day: be nice"""

    scene dark

    "Ugh..."
    """
    The smell of sweat and uncomfortable humidity startled you awake. Your head groaned and pounded in a slow nauseating frequency.
    """
    """
    Soon enough, you felt beads of moisture trickling down from your forehead down into your hair strands, creating a sticky collection of keratin mass around your head.
    Discomfort and disgust of your predicament reawakened your brain to finally attempt to comprehed this situation...
    What the HELL even was my name?
    """

    python:
        mc = renpy.input("Enter your name!", length=69)
        mc = mc.strip()

        if not mc:
            mc = "Clown"    

    mc "[mc], [mc], [mc]. I got it"

    scene bruh
    show flex with sshake
    x "Hello!" 
    x "I've been sitting here for 6 hours waiting for you to wake up!"
    mc "!!!" 
    """Who the hell is this twig?"""
    hide flex
    show flexx
    x "I'm glad we get to finally see each other face to face. I've been waiting for this moment for a very long time"
    x "You should feel the same way, you don't understand how lucky you are right now. I'm very serious when I say that"
    hide flexx
    show norm
    mc "What the-"
    hide norm
    show aw
    x "I know it's a strange way to execute a meet cute. But just listen okay"
    hide aw
    show panicc
    x "{size=15}{w=0.05}I just don't know how to approach people at all. Since I'm very pretty and very charismatic, usually people get to approach me, instead of me. So I never learned those skills{/size}"
    hide panicc
    show panic
    x "Trust me, I tried... Many times. I've been looking over forums and, uhm... guides... to find the best, quickest ways to initiate some kind of contact with people. But that was too much of a hassle, in my very very humble opinion. I did borrow some advice though..."
    hide panic
    show hmyap
    x "Sooo... that's why you're in this predicament. Does that make you feel better?"
    hide hmyap
    show cls
    x "It had to be like this! No hard feelings, please." 
    hide cls
    show clss
    x "...Please?"
    hide clss
    show norm
    mc "..."
    mc "Dude-"
    hide norm
    show flex
    x "I had to shoot my shot, like you little plebians say. I mean I'm trying my best to understand all of you. So, I hope YOU understand!"


    """Hmm. So clearly a big mouth sociopath is sitting across me. Am I about to contribute to death statistics? Given that I'm ever even found. Where the hell am I?"""
    mc "Uh."
    mc "Who are you?"
    mc "Where even am I? Why is it so humid in here? What is happening? Am I a hostage? Did I do something bad to you, something that I don't remember???"
    """Too many questions flooded out of my mouth, releasing all my pent up confusion and frustration bubbling inside me. The stranger then cut me off"""

    x "Calm down, [mc]. You'll understand everything soon"
    show flex
    x "Don't I look familiar to you?"
    mc "no"
    #shake head
    hide flex
    show wot
    x "My name is Pokki! Never heard of that name before? Nothing rings a bell yet? I think it should by now, heh."

    mc "no"
    #shake head
    hide wot 
    show flex
    x "The owner and creator of the biggest tech conglomerate across every galaxy imaginable! Every device you people own are engineered by ME!"
    x "..."
    hide flex
    show flexx
    x "Does it not ring a bell?"

    mc "no"
    #shake head
    hide flexx
    show wot
    x "Oh. Huh."
    x "How unfortunate, no. How strange."

    """Something about him, or his behavior striked the 'usual' feelings within you"""
    """He suddenly felt so familiar, at a certain point of your life, this person, this feeling has been a constant. Although you never recalled ever seeing a face like his before"""
    """Where have I seen him before?"""
    hide wot
    scene sky with dissolve
    """As you strained you brain to recall anything, at the very least the day before. Your head began to pound again"""
    """Suddenly, you felt the ghostly feelings of frustration envelop you. It began to rain after another typical working day. Nothing particularly bad happened to you, but your lack of umbrella tipped you over at that day. Your neurotic state drew out some gazes, but you continued to look up"""
    """..."""
    y "Hey. Are you alright? You've just been standing here for a while, heh."
    mc "Uh?! Startled me haha..."
    mc "I forgot to check the weather forecast, so I'm just stuck here, silly me"
    y "Oh yeah?"
    scene out with dissolve
    show outpok with dissolve
    y "Here, let me give you some cover. I can walk you to whatever destination you have your eye on. Come over inside"
    mc "Oh. That's very nice of you?"
    """Oh god what is this response? This is just an extremely nice and kind patron! I'm the weirdo freakazoid in this situation, and the entire day. Do better, stupid"""
    mc "Um. What's your name?"
    y "My name?"
    y "Um, my name? My name is uh-"


    ##darkness

    hide outpok
    scene dark with dissolve

    """That's all I could recall-"""
    init:
        $ sshake = Shake((0, 0, 0, 0), 1.0, dist=10)
    scene bruh with sshake
    show flex


    x "Anyways, we are currently on what you call, dates. And I am very excited to spend my 10 minutes with you, and let us get to know each other a little!"
    x "I want to know the basics of your personality, and see if we are even compatible. I was tired of all the b-... people flocking around me, so I wanted to be the to try to cold approach someone."
    hide flex
    show hm
    x "Although..."
    hide hm
    show panicc
    x "{size=15}{w=0.05}I kind of already found you very extremely cute the first time I saw you{/size}" #fast small text
    hide panicc
    show yap
    x "Buuuut our time together is rather short for today since I'm a very busy and sophisticated person single-handedly running an entire company" 
    x "So, I'm just going to ask you simple short fun questions and you'll answer for me, got it?" 
    hide yap
    show norm

    menu yesno:

        "Fuck you >:(":
            jump a
        "*nod*":
            jump b

label a:
    hide norm
    show wot

    mc "Man, fuck you"
    mc "I don't even know you like that. I'm not gonna be answering your stupid questions!1!! And let me out of here!" #surprised pikachu face"

    hide wot
    show heh
    x "Fiesty. Rawr..."
    x "Normally, I enjoy to play around a bit, but I don't have all day since I'm on my daily grind all day all night 24/7, if you get me"
    hide heh
    show clss
    x "So, you will answer my questions. And you will not waste our precious time together, okay?" #knife on table permanently
    show gun with dissolve

    """Bro. Do I have no survival skills? What is wrong with me?"""
    mc "*NOD NOD*"

    hide clss
    show cls

    x "Good, good! Very good. You understand so so quickly! Very lovely. Our date is about to begin. Right now!"
    jump date

label b:

    mc "*nod*"
    """Better get on his good side before anything"""

    hide norm
    show cls
    x "I love your attitude! I am very sure that we are going to get along so very well!"
    jump date


label date:

    hide cls
    show nrd
    """DATE"""
    """START!"""

    x "Alright! First question"
    x "What kind of food do you like?"

    menu food:
        "Anything with a ton of meat":
            $ foob = 1
            jump normal
        "Anything with a ton of veggies":
            $ foob = 2
            jump normal
        "Anything with a ton of carbohydrates":
            $ foob = 3
            jump normal

label normal:
    x "Very lovely! Thank you for your cooperation. Lemme just take a note of that~"
    x "I will surprise you with something real cute, just hold on"
    jump datee

label datee:
    init:
        $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)


    hide nrd
    show norm

    """You felt something smell from the distance. You wondered where it came from"""
    #look down#
    mc "!!!"
    if foob == 1:
        show mit with dissolve
    if foob == 2:
        show veg with dissolve
    if foob == 3:
        show pie with dissolve
    if foob == 4:
        show piz with dissolve

        hide mit
        hide veg
        hide piz
        hide pie

    """What you say, has taken you by surprise. Out of nowhere you had a plate with food. You wondered how it slipped in here this fast"""

    #shake sfx
    """Everything has occured only at a second. Then you felt something prod your face."""
    """With food???"""
    show tents with sshake
    hide norm
    show cls
    mc "OOMF" #pokki happy
    """Yum :)"""
    hide cls
    show aw
    x "Sorry about that, [mc]. These things are still at an experimental stage, so they might be unecessarily rough" 
    x "I hope the meal is to your liking~"
    hide aw
    show hm
    x "{size=20}Might be your last meal after all. Alright, lets get back to the date{/size}" #small text, smug
    hide hm
    show norm
    """I'd shove it all down if it weren't for the awful circumstances I'm currently in and forced to endure. And if my mouth wasn't busted"""
    hide tents
    hide norm
    show yap


    x "I am very glad you're enjoying the meal. Let's move on~" #smile
    x "What is your favorite color?"
    hide yap
    show norm

    menu color:
        "Red":
            jump nice
        "Blue":
            jump nice
        "Yellow":
            jump nice
        "Green":
            jump nice
        "Pink":
            jump nice
        "Purple":
            jump nice
        "Black":
            jump nice
        "None of the above":
            jump notnice

label notnice:
    #screen goes dark and staticy
    show dark with dissolve
    g "Shut the fuck up and choose from the given options"
    hide dark
    $ spc += 1
    #return back to normal
    menu colour:
        "Red":
            jump nice
        "Blue":
            jump nice
        "Yellow":
            jump nice
        "Green":
            jump nice
        "Pink":
            jump nice
        "Purple":
            jump nice
        "Black":
            jump nice

label nice:

    hide norm
    show heh
    x "I knew you'd like it. The color truly suits you. I can see the kind of guess what kind of a person you are!"
    x "I'll take a quick note of that~"

    if spc == 1:
        hide heh
        show wot
        x "..."
        x "Are you okay? You seem a little pale..."

        mc "uh- I-"
        hide wot
        show cls
        x "Oh well, moving on!"
    hide heh
    show cls

    x "Alright,"
    x "What is your favorite way to relax after a loong day?"
    menu day:
        "Lay down and de-stress":
            jump lay
        "Invest in my interests":
            jump hob
        "Interact with people":
            jump hang
        "Eat":
            jump et

    hide cls
    show aw

label lay:
    x "Hehe. We have so much in common! I sure do love to lay down and decompress myself after a hard day of work scolding my lazy and ungrateful employees with the finest of wines. I totaly relate by the way~"
    jump dateee
label hob:
    x "Wow! You sound very productive, I admire people like you~"
    x "Especially in my work force. I'd totally love to have you as my employee, if it wasn't for our current very special circumstance"
    jump dateee
label hang:
    x "I also like spending time with my loveliest people who truly understand me and listen to me! And I like observing their bodies or parts interact with my ongoing research. We're so similar its crazy isn't it?"
    jump dateee
label et:
    x "How cute! I would just love to cook for you and make sure to keep you full! But I don't need to do that since I have people and things around me to do that. Still, you probably know what I mean, right?"
    jump dateee

    hide aw
    show flex

label dateee:
    x "Okay! Im going to ask you a personal question. I hope you don't mind~"
    x "What is your favorite love language?"

    hide flex
    show norm
    menu love:
        "Quality time":
            jump omg
        "Physical touch":
            jump im
        "Acts of service":
            jump so
        "Gift giving":
            jump trd
        "Words of affirmation":
            jump of
        "All of the above":
            jump ths

    hide norm
    show clss

label omg:
    x "Agreed!"
    x "There's no better way to bond with someone without spending some quality time together. I would really really love to open that little cranium of yours some day, maybe today, while you're awake during that duration of time with me as I observe what kind of silly little blippy thoughts you have compiled into that little head of yours. Therefore, spending quality time with me!"
    jump dateeee
label im:
    x "How sweet!"
    x "Sometimes non-verbal communication is important when words aren't enough to convey strong and passionate feelings. I would literally withhold my spending habits for a single day just to drag my tongue on that hairy greasy sweaty little scalp of yours, and get my daily dose of salt from just that alone. I still would never allow you to touch mine though~"
    jump dateeee
label so:
    x "How romantic~"
    x "Actions always ALWAYS speak louder than words. It is a perfect way to show love without communication that fluster your heart. I could just imagine how absolutely productive you would've been if you were my employee. So so unfortunate you're not, but this is still cute to know of course. I'd love to witness the extent you'd go for someone's (my) happiness"
    jump dateeee
label trd:
    x "A very thoughtful gesture indeed"
    x "The act of giving can truly show the will of one to invest and sacrifice into the relationship. The sight of someone tearing one self apart and pour in everything that they have in declaration of love and dedication to another, never EVER fails to make my heart squeeze and bleed. I love love people like that~"
    jump dateeee
label of:
    x "Oh, we might just be made for each other!"
    x "This is such a perfect way to REASSURE and remind your partner of your love and commitment to the relationship. Its so fluffy and wholesome, I can't imagine living with a person that would never bother to tell me, let me know that they still long for me and love me for even a little blip. Otherwise I'll just fucking-"
    x "Yip! Excuse my foul dirty mouth. We are so similar, it's like the fate has pitted us against each other~"
    jump dateeee
label ths:
    x "So adaptable to all kinds of love, aren't you? Just so much saccharine in this stuffy little space, all coming from YOU. I wouldn't be surprised if you had secret admirers. Like me, hehe"
    x "You should be lucky to bag yourself someone like me, even for a mip, you sugary ice cube"
    jump dateeee

    hide clss
    show flexx
label dateeee:
    x "Good good, I think I know more than enough about the kind of person you are!" 
    x "Our time is ticking, so I'll finally get to the good part and ask important questions! What I'm going to ask will probably ring some alarm bells in your head"
    x "But I really want to know if we're compatible or not through them, so please don't mind~"
    jump real_interview

label real_interview:
    hide flexx
    show heh
    x "Let's begin now!~"

    x "What would you do if you saw a person about to slip on a banana?"
    menu q1:
        "Watch":
            $ chaos += 2
            jump a1
        "Warn them":
            $ chaos
            jump a1
        "Ignore":
            $ chaos += 1
            jump a1

    hide heh
    show norm

label a1:

    x "Interesting! Moving onto..."
    hide norm
    hide heh
    show flex
    x "Even weirder question!"

    x "How would you feel if someone served their guests a cake in the shape of fecal matter?"
    menu q2:
        "Be weirded out":
            jump a2
        "Find it funny":
            $ chaos += 1
            jump a2

label a2:
    hide flex
    show yap
    x "Heheh, excretion jokes! You little people find that so funny, right?"
    x "Next question,"
    hide yap
    show cls
    x "A rival team is singing their national anthem. How would you feel if one of your teammates sang along with them?"
    menu q3:
        "I don't care":
            $ chaos += 1
            jump a3
        "It'd be a major fucking issue":
            jump a3

label a3:

    x "I'd sing along with them too if that were to happen~"
    hide cls
    show nrd
    x "I hope you know how to drive, or at least try to imagine yourself in this situation as accurately as possible!"

    x "You're driving late at night, and there's no one but you. You come to a red light at an empty intersection. Do you stop or do you go through it?"
    hide nrd
    show norm
    menu q4:
        "Stop":
            x "A straight law-abiding citizen, are you not? I can respect that"
            jump a4
        "Keep driving":
            $ chaos += 1
            x "Oh me heart! So rebellious!"
            jump a4

label a4:
    hide norm
    show yap
    x "Well, we made it almost half way! Hang in there, [mc]!"
    x "Im going to ask a few work related questions. I hope they don't hurt too much~"
    x "You found out that your workplace has a policy against decorations on desks,"
    x "Do you still follow the policy or would you secretly add your own personal touches?"
    hide yap
    show norm
    menu q5:
        "Stupid policy. Of course I would":
            $ chaos += 1
            jump a5
        "Won't risk it":
            jump a5

label a5:
    hide norm
    show yap
    x "Hehe. You're quite funny! Moving on,"
    x "During a work meeting, an employee pulls up a slide with 'meme' in their presentation to make their point, but it's slightly inappropriate for the setting. Is this acceptable?"
    hide yap
    show norm
    menu q6:
        "Cringe but yes":
            $ chaos += 1
            jump a6
        "NO!!!":
            jump a6

label a6:
    hide norm
    show cls
    x "Loving your thought process, let's keep going"
    x "Is it acceptable for a manager to fire someone just because they called them by their first name?"
    menu q7:
        "Yes...?":
            jump a7
        "No...?":
            $ chaos += 1
            jump a7

label a7:
    hide cls
    show clss
    x "What's the unsure answer for? You're doing great, we're already done with work questions! just a few more left"
    x "A lecturer uses profanity in the classroom to connect with students better. Is this appropriate or crossing a line?"
    menu q8:
        "I literally don't care":
            $ chaos += 1
            jump a8
        "It's kinda inappropriate":
            jump a8

label a8:
    hide clss
    show flex
    x "Very fascinating! I just want to take a small little peek at your brain"
    x "Onwards!"
    hide flex
    show flexx
    x "If you saw a building covered in street art. Do you appreciate it, or do you feel that it has been desecrated?"
    menu q9:
        "The building is tarnished, it will never be the same. Cut the desecrators' hands off immediately":
            x "I suppose it is!"
            jump a9
        "I ogle at the wall with my mouth slightly open":
            $ chaos += 1
            x "Good for you <3"
            jump a9


label a9:
    hide flexx
    show aw
    x "I hope you don't mind... few possibly controversial questions. They are really important for me, so just hang in there and answer for me, mmkay?"
    x "So,"
    x "How do you think a society should be run?"
    menu q10:
        "If something is functioning well, there's no need to change it as its already difficult enough to adapt in this world. And authority figures are essential for maintaining order, as they understand the how, what, and why behind their choices":
            x "True! Sometimes the existing system effectively meets the needs of the majority, making it unnecessary to disrupt it"
        "Society should always adapt whenever necessary. What works for one person may not suit another, and anything in the position of authority should be questioned, scrutinized, or challenged, especially if lines have been crossed":
            $ chaos += 1
            x "I agree! What benefits one group might be detrimental to another, so society must always be responsive, therefore willing to listen and change"
        "There needs to be a balance between both to prevent things from spiraling out of control":
            x "Indeed! A balanced approach may encourage progress while respecting existing structures, whatever they are"

    jump final_act

label final_act:
    hide aw
    show flex
    x "I've really enjoyed spending time with you. Hearing your thoughts and perspectives, you strike me as someone smart, someone good!"
    hide flex
    show hmyap
    x "Before we finish, I have one last question for you"
    x "I know that many people are afraid to open their minds to new things. I completely understand them"
    hide hmyap
    show aw
    x "It's scary to step out of your comfort zone, when you've only just began to condition yourself in whats already familiar behind you. All the bad and all the good"
    x "Not everyone is ready or even capable to see beyond what they have given, even if it is something to their own benefit, maybe"
    x "I really hope you're not like that, [mc]. I like you too much already!"
    mc "..."
    hide aw
    show norm
    x "So."
    x "If you had the power to reshape everything, current structures, creating a future where many impossibilities could flourish and become possibilites for everyone in the future, even if it meant countless lives have been taken in the process of that good future"
    x "A future of something so great and unfamiliar that satiates all your curiosities, or something that nobody ever imagined. Would it be worth it? To have the incomprehensible accessible to all? Even at, but inital costs"

    menu question:
        "What the HELL are you even talking about":
            if chaos <= 8:
                jump death
            else:
                jump desperation
        "Yes":
            jump uhoh
    hide norm

label desperation:
    hide norm
    show aw
    x "I don't think you quite get me" 
    hide aw
    show flex
    x "The potential, the greatness that could be born from a just a small blip in the universe, a small cost. Progress always demands it"
    x "And yet people are always afraid of the unknown and cling onto their old, really decaying ways of thinking"
    x "Absolutely reluctant to change, even if its a necessaty at this point, until too late." 
    x "What if you just simply embraced the discomfort and your fears? And let that inspire you instead?"
    hide flex
    show aw
    x "Wouldn't you want to be part of that change? To be in that future of this current imperfect world, even if it means letting go of the past by any means necessary?"

    menu again:
        "Whaat are you even talking about? Aren't you like a CEO?":
            jump death
        "Yes":
            jump uhoh   

    hide aw 


label uhoh:
    hide norm
    show wot
    x "What?"
    x "Are you being serious?"
    mc "..."
    hide wot
    show flex
    x "Haha, im truly the luckiest little bloom of a flower! I'm glad to know there's someone out there who sees my vision, someone so so relatable and cute like me. I think we were meant for each other!"
    hide flex
    show wao
    x "Wait..."
    x "I shouldn't get to excited! I have one last and the most important question for you!"
    hide wao
    show hehh
    x "Do..."
    x "Do you like me?"

    menu notfinallmao:
        g "Do you like him?"

        "Yes":
            jump end0
        "I don't even know your name, man":
            if chaos <= 8:
                jump death
            jump sad
    hide hehh

label sad:
    show sigh
    x "Oh..."
    x "I told you my name, no? Its Pokki..."
    hide sigh
    show hehh
    x "Am I not good enough for you? I thought we were compatible! You ticked all the boxes in my questionnare! We're basically a biblical match up that should be whispered and written literature about! I don't understand..."
    mc "We just met-"
    hide hehh
    show pup
    x "No. No I understand, I should probably let you go..."
    x ""
    x "Here, let me untie you"
    hide pup
    #BG BLACK
    jump end3


label end0:

    hide hehh
    show wao
    x "Oh!"
    hide wao
    show aw
    x "Oh im so glad! Thank goodness!"
    hide aw
    show flex
    x "I will treat you so well, [mc]! I apologize for my lack of patience but we should absolutely marry each other today. I'll contact my lawyer and get the paper work in about 5 minutes"
    hide flex
    show flexx
    x "And to hell with this job. I deserve a vacation! I'm mentally so exhausted from scolding my fellow incompotent employees, I'm like a single mother to clueless toddlers. I want to know all that is there of you, right now!"
    x "I'll get you off the ropes right away, stay still for me"

    hide flexx
    hide gun
    hide mit
    hide veg
    hide piz
    hide pie
    show dark with dissolve

    """What have I gotten myself into?"""

    x "I don't bite, and I don't smoke. Don't you worry about that small cake of yours"
    x "..."
    mc "What?"
    x "I know you might just be pretending"
    x "Going along with whatever I say, because you're afraid. Am I wrong?"

    menu sex:
        "...":
            jump bruh
        "He has money. He has money. He has money in this economy":
            jump rizz

label rizz:
    """I mean a hustle is a hustle, no matter the opinions"""
    mc "You kinda bad though, heh..."
    x "uh"
    x "...What?"
    mc "You heard me"
    x "..."
    x "Aha.."
    x "You're so bold and so so really crazy, and this is coming from someone like me"
    x "..."

    x "I promise that I will make you the happiest person alive. Mark my words"
    jump end1


label bruh:
    x "Still, I appreciate you for at least being nice enough to play along!"
    x "At least you won't cause any fuss or complications between us"
    x "I'll make sure to savor this little spark within me while it lasts"
    jump end2


label death:
    x "I see..."
    x "It seems we have nothing in common. I kinda a little bit wasted my time then" 
    hide aw
    show hehh
    x "Im sorry it has to end this way..."
    x "I really really liked you, but I must protect my peace, especially with all those red flags around me. My boundaries are to be respected"
    #screen shake. blood everywhere. commotion. baby crying car crash windows breaking aaaa

    hide mit
    hide veg
    hide piz
    hide pie
    scene dark with sshake#ADD BG FOR ENDINGS
    

    """YOU DIED LMAO"""
    """End 0"""
    return 


label end1:
    hide mit
    hide veg
    hide piz
    hide pie
    scene end1 with dissolve
    ''
    g "You two kinda lived happily ever after"
    g "Congratulations. A match made in hell"
    """End 1!!!"""
    #happi png
    return



label end2:
    hide mit
    hide veg
    hide piz
    hide pie
    scene end2 with dissolve
    ''
    g "You two lived somewhat happily every after"
    g "My utmost condolences, [mc]"
    """End 2!!!"""
    #happi? png
    return


label end3:
    hide gun
    hide mit
    hide veg
    hide piz
    hide pie
    scene sky with dissolve
    ''
    mc "Huh?"
    """What? Did I just hallucinate?"""
    mc "Crap" 
    """It's still raining. I gotta hide somewhere..."""
    scene dark with dissolve
    """This was one of the weirdest experience of my life"""
    """Im not sure if I simply just imagined all of that. Either way I never was able to sleep like I used to"""
    g "Have fun trying to repress all that. You will never be completely off the hook"
    mc "What??"
    scene end3 with dissolve
    """End 3!!!"""

    #reuse scrapped bg from 2 years ago or msth
    #sad

    return