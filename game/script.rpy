# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

default num_helped = 0
default elderly_people_collected = 0
# The game starts here.

label start:
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
            pass

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
    else:
        e "Oh no, this did not go according to plan."
        $ num_helped -= elderly_people_collected
        $ num_helped -= 1
        # we failed
        jump bad_end

label bad_end:
    call screen bad_end_screen


image black = "#000000"

screen bad_end_screen():
    add "black"
    text "Game Over"


screen hud():
    vbox:
        text "Number of people collected: [elderly_people_collected]"
        text "Number of people helped: [num_helped]"
