#my code but copy-paste from ai...

matches = []

while True:
    match = input("Enter match details: ").lower()

    if match == "done":
        break
    else:
        matches.append(match)

teams = {}

for match in matches:

    home, away, result = match.split(";")

    # create teams if not already present
    if home not in teams:
        teams[home] = {
            "MP": 0,
            "W": 0,
            "D": 0,
            "L": 0,
            "P": 0
        }

    if away not in teams:
        teams[away] = {
            "MP": 0,
            "W": 0,
            "D": 0,
            "L": 0,
            "P": 0
        }

    # both teams played one match
    teams[home]["MP"] += 1
    teams[away]["MP"] += 1

    # if home team wins
    if result == "win":

        teams[home]["W"] += 1
        teams[home]["P"] += 3

        teams[away]["L"] += 1

    # if home team loses
    elif result == "loss":

        teams[home]["L"] += 1

        teams[away]["W"] += 1
        teams[away]["P"] += 3

    # draw
    elif result == "draw":

        teams[home]["D"] += 1
        teams[away]["D"] += 1

        teams[home]["P"] += 1
        teams[away]["P"] += 1

# sorting
sorted_teams = sorted(
    teams.items(),
    key=lambda x: (-x[1]["P"], x[0])
)

# table heading
print(f"{'Team':30} | MP |  W |  D |  L |  P")

# print teams
for team, stats in sorted_teams:

    print(
        f"{team:30} | "
        f"{stats['MP']:2} | "
        f"{stats['W']:2} | "
        f"{stats['D']:2} | "
        f"{stats['L']:2} | "
        f"{stats['P']:2}"
    )

#solution...

"""
Exercism solution for "tournament"
"""
from operator import itemgetter
from typing import Counter, DefaultDict, List, Sequence, Tuple, Union

ROW_FORMAT = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
OUTCOME_MAP = {"win": "loss", "loss": "win", "draw": "draw"}


Cell = Union[str, int]
Row = Tuple[str, Cell, Cell, Cell, Cell, Cell]

def tally(results: Sequence[str]) -> List[str]:
    """
    Tally a football tournament.
    """
    teams: DefaultDict[str, Counter[str]] = DefaultDict(Counter)
    for result in results:
        home, away, outcome = result.split(";")
        teams[home][outcome] += 1
        teams[away][OUTCOME_MAP[outcome]] += 1

    table: List[Row] = []
    for team, record in sorted(teams.items()):
        wins, draws, losses = record["win"], record["draw"], record["loss"]
        matches, points = wins + draws + losses, 3 * wins + draws
        table.append((team, matches, wins, draws, losses, points))
    table.sort(key=itemgetter(-1), reverse=True)

    table.insert(0, ("Team", "MP", "W", "D", "L", "P"))
    return [ROW_FORMAT.format(*row) for row in table]
