#my code...

scores=[]
titles=[]
while True:
    try:
        user=int(input("Enter your score(type 'done' to stop): "))
        title=input("Match name: ")
        scores.append(user)
        titles.append(title)
    except ValueError:
        break
book=list(zip(scores,titles))
want=input("want to know what is the highest score in your list?(y/n) ")
if want=="y":
    if len(scores)>0:
        print(max(scores))
        print("top three score from your list:",sorted(scores, reverse=True)[:3])#from duck ai lol...
        print("your last score was:",scores[len(scores)-1])
    else:
        print("No scores!!")
else:
    print("sure as you wish!")
print("playbook:",book)

#solution...

class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        return sorted(self.scores, reverse=True)[:3]
