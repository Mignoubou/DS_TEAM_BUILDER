commander_names = ["Abathur", "Alarak", "Artanis", "Dehaka", "Fenix", "Han and Horner", "Karax", "Kerrigan", "Mengsk", "Nova", "Raynor", "Stetmann", "Stukov", "Swann", "Tychus", "Vorazun", "Zagara"]
number_of_matchup_categories = 5 #Keep it odd or it will break things (unless you know what you're doing), and keep Even in the middle
matchup_categories = {"Hard Counter": 0, "Favorable": 1, "Even": 2, "Unfavorable": 3, "Hard Countered": 4}
commanders = {}

for commander in commander_names:

    commanders[commander] = [[] for matchup_category in range(number_of_matchup_categories)]

def add_matchup(commander_1, commander_2, matchup_category):

    commanders[commander_1][matchup_categories[matchup_category]].append(commander_2)
    commanders[commander_2][number_of_matchup_categories - 1 - matchup_categories[matchup_category]].append(commander_1)

"""ABATHUR MATCHUPS"""
add_matchup("Abathur", "Abathur", "Even")
add_matchup("Abathur", "Alarak", "Even")
add_matchup("Abathur", "Artanis", "Even")
add_matchup("Abathur", "Dehaka", "Favorable")
add_matchup("Abathur", "Fenix", "Hard Countered")
add_matchup("Abathur", "Han and Horner", "Favorable")
add_matchup("Abathur", "Karax", "Favorable")
add_matchup("Abathur", "Kerrigan", "Even")
add_matchup("Abathur", "Mengsk", "Hard Countered")
add_matchup("Abathur", "Nova", "Favorable")
add_matchup("Abathur", "Raynor", "Hard Counter")
add_matchup("Abathur", "Stetmann", "Hard Countered")
add_matchup("Abathur", "Stukov", "Favorable")
add_matchup("Abathur", "Swann", "Favorable")
add_matchup("Abathur", "Tychus", "Unfavorable")
add_matchup("Abathur", "Vorazun", "Even")
add_matchup("Abathur", "Zagara", "Even")

"""ALARAK MATCHUPS"""
add_matchup("Alarak", "Alarak", "Even")
add_matchup("Alarak", "Artanis", "Favorable")
add_matchup("Alarak", "Dehaka", "Hard Countered")
add_matchup("Alarak", "Fenix", "Hard Countered")
add_matchup("Alarak", "Han and Horner", "Even")
add_matchup("Alarak", "Karax", "Hard Countered")
add_matchup("Alarak", "Kerrigan", "Even")
add_matchup("Alarak", "Mengsk", "Favorable")
add_matchup("Alarak", "Nova", "Even")
add_matchup("Alarak", "Raynor", "Unfavorable")
add_matchup("Alarak", "Stetmann", "Unfavorable")
add_matchup("Alarak", "Stukov", "Unfavorable")
add_matchup("Alarak", "Swann", "Even")
add_matchup("Alarak", "Tychus", "Hard Counter")
add_matchup("Alarak", "Vorazun", "Unfavorable")
add_matchup("Alarak", "Zagara", "Hard Counter")

"""ARTANIS MATCHUPS"""
add_matchup("Artanis", "Artanis", "Even")
add_matchup("Artanis", "Dehaka", "Unfavorable")
add_matchup("Artanis", "Fenix", "Hard Countered")
add_matchup("Artanis", "Han and Horner", "Hard Counter")
add_matchup("Artanis", "Karax", "Even")
add_matchup("Artanis", "Kerrigan", "Even")
add_matchup("Artanis", "Mengsk", "Even")
add_matchup("Artanis", "Nova", "Unfavorable")
add_matchup("Artanis", "Raynor", "Even")
add_matchup("Artanis", "Stetmann", "Favorable")
add_matchup("Artanis", "Stukov", "Hard Countered")
add_matchup("Artanis", "Swann", "Hard Counter")
add_matchup("Artanis", "Tychus", "Even")
add_matchup("Artanis", "Vorazun", "Unfavorable")
add_matchup("Artanis", "Zagara", "Favorable")

"""DEHAKA MATCHUPS"""
add_matchup("Dehaka", "Dehaka", "Even")
add_matchup("Dehaka", "Fenix", "Even")
add_matchup("Dehaka", "Han and Horner", "Even")
add_matchup("Dehaka", "Karax", "Hard Counter")
add_matchup("Dehaka", "Kerrigan", "Unfavorable")
add_matchup("Dehaka", "Mengsk", "Favorable")
add_matchup("Dehaka", "Nova", "Even")
add_matchup("Dehaka", "Raynor", "Unfavorable")
add_matchup("Dehaka", "Stetmann", "Even")
add_matchup("Dehaka", "Stukov", "Unfavorable")
add_matchup("Dehaka", "Swann", "Favorable")
add_matchup("Dehaka", "Tychus", "Favorable")
add_matchup("Dehaka", "Vorazun", "Hard Counter")
add_matchup("Dehaka", "Zagara", "Hard Counter")

"""FENIX MATCHUPS"""
add_matchup("Fenix", "Fenix", "Even")
add_matchup("Fenix", "Han and Horner", "Unfavorable")
add_matchup("Fenix", "Karax", "Even")
add_matchup("Fenix", "Kerrigan", "Favorable")
add_matchup("Fenix", "Mengsk", "Favorable")
add_matchup("Fenix", "Nova", "Unfavorable")
add_matchup("Fenix", "Raynor", "Favorable")
add_matchup("Fenix", "Stetmann", "Favorable") #Not the matchup on the guide but it was unclear so I've put that based on my opinion
add_matchup("Fenix", "Stukov", "Favorable")
add_matchup("Fenix", "Swann", "Hard Counter")
add_matchup("Fenix", "Tychus", "Unfavorable")
add_matchup("Fenix", "Vorazun", "Favorable")
add_matchup("Fenix", "Zagara", "Favorable")

"""HAN AND HORNER MATCHUPS"""
add_matchup("Han and Horner", "Han and Horner", "Even")
add_matchup("Han and Horner", "Karax", "Hard Counter")
add_matchup("Han and Horner", "Kerrigan", "Unfavorable")
add_matchup("Han and Horner", "Mengsk", "Hard Counter")
add_matchup("Han and Horner", "Nova", "Unfavorable")
add_matchup("Han and Horner", "Raynor", "Hard Counter")
add_matchup("Han and Horner", "Stetmann", "Favorable")
add_matchup("Han and Horner", "Stukov", "Even")
add_matchup("Han and Horner", "Swann", "Even")
add_matchup("Han and Horner", "Tychus", "Unfavorable")
add_matchup("Han and Horner", "Vorazun", "Even")
add_matchup("Han and Horner", "Zagara", "Hard Counter")

"""KARAX MATCHUPS"""
add_matchup("Karax", "Karax", "Even")
add_matchup("Karax", "Kerrigan", "Unfavorable")
add_matchup("Karax", "Mengsk", "Favorable")
add_matchup("Karax", "Nova", "Unfavorable")
add_matchup("Karax", "Raynor", "Unfavorable")
add_matchup("Karax", "Stetmann", "Unfavorable")
add_matchup("Karax", "Stukov", "Favorable")
add_matchup("Karax", "Swann", "Hard Counter")
add_matchup("Karax", "Tychus", "Unfavorable")
add_matchup("Karax", "Vorazun", "Unfavorable")
add_matchup("Karax", "Zagara", "Favorable")

"""KERRIGAN MATCHUPS"""
add_matchup("Kerrigan", "Kerrigan", "Even")
add_matchup("Kerrigan", "Mengsk", "Even")
add_matchup("Kerrigan", "Nova", "Favorable")
add_matchup("Kerrigan", "Raynor", "Unfavorable")
add_matchup("Kerrigan", "Stetmann", "Unfavorable")
add_matchup("Kerrigan", "Stukov", "Even")
add_matchup("Kerrigan", "Swann", "Favorable")
add_matchup("Kerrigan", "Tychus", "Hard Counter")
add_matchup("Kerrigan", "Vorazun", "Even")
add_matchup("Kerrigan", "Zagara", "Favorable")

"""MENGSK MATCHUPS"""
add_matchup("Mengsk", "Mengsk", "Even")
add_matchup("Mengsk", "Nova", "Unfavorable")
add_matchup("Mengsk", "Raynor", "Favorable")
add_matchup("Mengsk", "Stetmann", "Favorable")
add_matchup("Mengsk", "Stukov", "Favorable")
add_matchup("Mengsk", "Swann", "Favorable")
add_matchup("Mengsk", "Tychus", "Unfavorable")
add_matchup("Mengsk", "Vorazun", "Even")
add_matchup("Mengsk", "Zagara", "Unfavorable")

"""NOVA MATCHUPS"""
add_matchup("Nova", "Nova", "Even")
add_matchup("Nova", "Raynor", "Favorable")
add_matchup("Nova", "Stetmann", "Unfavorable")
add_matchup("Nova", "Stukov", "Even")
add_matchup("Nova", "Swann", "Favorable")
add_matchup("Nova", "Tychus", "Hard Counter")
add_matchup("Nova", "Vorazun", "Favorable")
add_matchup("Nova", "Zagara", "Even")

"""RAYNOR MATCHUPS"""
add_matchup("Raynor", "Raynor", "Even")
add_matchup("Raynor", "Stetmann", "Even")
add_matchup("Raynor", "Stukov", "Hard Counter")
add_matchup("Raynor", "Swann", "Favorable")
add_matchup("Raynor", "Tychus", "Even")
add_matchup("Raynor", "Vorazun", "Hard Counter")
add_matchup("Raynor", "Zagara", "Unfavorable")

"""STETMANN MATCHUPS"""
add_matchup("Stetmann", "Stetmann", "Even")
add_matchup("Stetmann", "Stukov", "Even")
add_matchup("Stetmann", "Swann", "Hard Counter")
add_matchup("Stetmann", "Tychus", "Unfavorable")
add_matchup("Stetmann", "Vorazun", "Hard Counter")
add_matchup("Stetmann", "Zagara", "Favorable")

"""STUKOV MATCHUPS"""
add_matchup("Stukov", "Stukov", "Even")
add_matchup("Stukov", "Swann", "Favorable")
add_matchup("Stukov", "Tychus", "Even")
add_matchup("Stukov", "Vorazun", "Unfavorable")
add_matchup("Stukov", "Zagara", "Even")

"""SWANN MATCHUPS"""
add_matchup("Swann", "Swann", "Even")
add_matchup("Swann", "Tychus", "Unfavorable")
add_matchup("Swann", "Vorazun", "Unfavorable")
add_matchup("Swann", "Zagara", "Unfavorable")

"""TYCHUS MATCHUPS"""
add_matchup("Tychus", "Tychus", "Even")
add_matchup("Tychus", "Vorazun", "Even")
add_matchup("Tychus", "Zagara", "Favorable")

"""VORAZUN MATCHUPS"""
add_matchup("Vorazun", "Vorazun", "Even")
add_matchup("Vorazun", "Zagara", "Even")

"""ZAGARA MATCHUPS"""
add_matchup("Zagara", "Zagara", "Even")

def status_to_list(commander_1, commander_2): #Comment commander_1 gere les matchups de commander_2

    status_list = []

    for matchup_category_1 in range(number_of_matchup_categories):

        for commander_ in commanders[commander_1][matchup_category_1]:

            for matchup_category_2 in range(number_of_matchup_categories):

                if (commander_ in commanders[commander_2][matchup_category_2]):

                    status_list.append((number_of_matchup_categories - 1) / 2 - matchup_category_2)

    for i in range(len(status_list)):

        status_list[i] *= 1.2 ** i + 1

    return status_list

def best_teams():

    list_of_best_commanders = []

    for commander_1 in commander_names:

        for commander_2 in commander_names:

            for commander_3 in commander_names:

                commanders = [commander_1, commander_2, commander_3]
                status = sum(status_to_list(commander_2, commander_1)) + sum(status_to_list(commander_3, commander_2), sum(status_to_list(commander_1, commander_3)))

                list_of_best_commanders.append((commanders, status))

    return sorted(list_of_best_commanders, key=lambda status: status[1], reverse = True)

for team in best_teams()[:15]:

    print(team)
