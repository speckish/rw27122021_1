default eileen_points = 0
default zachary_points = 0

label dating_sim:
    # To test this out, add the line "jump dating_sim to the top of your start label.
    show screen dating_points
    menu:
        "Complement Eileen":
            "Eileen you look great today!"
            $ eileen_points += 1
        "Be mean to Eileen":
            "Eileen you look terrible today!"
            $ eileen_points -= 1
        "Complement Zachary":
            "Zachary I guess you're okay..."
            $ zachary_points += 1
        "Be mean to Zachary":
            "Ew, go away Zachary!"
            $ zachary_points -= 1
        "Finish the game":
            jump evaluate_dating_points
    jump dating_sim

label evaluate_dating_points:
    if eileen_points < 0 and zachary_points < 0:
        "They both hate you."
        "Guess you'll die alone!"
    elif eileen_points == 0 and zachary_points == 0:
        "They are both very neutral to you."
        "Neutral isn't very romantic. Neither one of them noticed you."
    elif eileen_points > zachary_points and eileen_points > 3:
        "Eileen likes you enough to give you a shot!"
    elif eileen_points < zachary_points and zachary_points > 3:
        "Zachary likes you enough to give you a shot!"
    elif eileen_points == zachary_points:
        "Eileen and Zachary both like you...which is how they realized they actually have a lot in common."
        "They're dating now, and you're alone on a Saturday night."
    else:
        "Some people think you're nice but you didn't really sweep anyone one off their feet."
        "Friends are nice though! For now you're happy with being friends."
    return


screen dating_points:
    vbox:
        text "Eileen points: [eileen_points]"
        text "Zachary points: [zachary_points]"
