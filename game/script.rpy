# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

default num_helped = 0
default elderly_people_collected = 0
default cars_punched = 0
# The game starts here.

label start:
    # Uncomment the line below to go to the "dating sim" instead of the car punching game.
    # jump dating_sim

    show screen hud
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bgg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "I would like help someone cross the street."

    e "What should I do?"

    menu:
        "Look for an older person.":
            e "Let's hold hands and make a chain together so the cars can see us better!"
            jump collect_elderly_people
        "Try to stop the cars with my bare hands.":
            jump punch_cars

    e "Hmm, that sounds like a good idea."
    return

label collect_elderly_people:
    "Should we grab another elderly person?"
    menu:
        "Yes":
            $ elderly_people_collected += 1
            "Okay grabbed one more."
            jump collect_elderly_people
        "No":
            e "Okay, I guess we have enough."
            jump make_a_chain

label make_a_chain:
    e "Let's try stopping traffic with our human chain now!"
    if elderly_people_collected >= 4:
        # sucessful case
        $ num_helped += elderly_people_collected
        e "Yay! No one died!"
        jump good_end
    else:
        e "Oh no, this did not go according to plan."
        $ num_helped -= elderly_people_collected
        $ num_helped -= 1
        # we failed
        jump bad_end

default time = 0
default timer_range = 3
label punch_cars:
    $ time = timer_range
    call screen punch_cars

label good_end:
    call screen end_screen

label bad_end:
    call screen end_screen

image black = "#000000"


label count_cars:
    e "Let's count up the cars now!"
    if cars_punched > 20:
        # sucess
        $ num_helped += cars_punched/2
        e "We helped so many people!"
        e "Fuck the cars!"
    else:
        # fail
        $ num_helped = -1
        e "Oh no, I've died!"
        e "I guess that was a bad idea after all."
    call screen end_screen

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen punch_cars():
    add "black"
    textbutton "Punch A Car":
        action SetVariable("cars_punched", cars_punched+1)
        text_size 128
        align (0.5, 0.5)
    vbox:
        text "You have punched [cars_punched] cars."
        text "Time left: [time]"
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Jump("count_cars")])
    # bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

screen end_screen():
    add "black"
    text "Game Over":
        size 128
        align (0.5, 0.5)
    vbox:
        align (0.5, 0.75)
        text "You helped [num_helped] people in total."
        if num_helped < 0:
            $ final_message = "Very bad job, you should feel bad about yourself."
        elif num_helped == 1:
            $ final_message = "You tried your best. Maybe you should try again tomorrow. "
        else:
            $ final_message = "Okay, pretty good job."
        text final_message

# < 0 = Very bad job, you should feel bad about yourself.
# == 1 You tried your best. Maybe you should try again tomorrow.
# > 1 Okay, pretty good job.


screen hud():
    vbox:
        text "Number of people collected: [elderly_people_collected]"
        text "Number of people helped: [num_helped]"
