import random

R_EATING = "I don't like eating anything because I am a bot, obviously!"
R_ADVICE = "I suggest doing more python projects to build your portfolio!"

def unknown():
    response = ['Could you please re-phrase that?',
                "...",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response