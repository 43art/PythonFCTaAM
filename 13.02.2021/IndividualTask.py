n = int(input())
dictionary = {}

surname, vote = input().split()
vote = int(vote)
dictionary.update({surname: vote})

for i in range(1, n):
    surname, vote = input().split()
    vote = int(vote)
    flag = 0
    for j in dictionary.keys():
        if j == surname:
            new_vote = dictionary[j] + vote
            dictionary.update({surname: new_vote})
            flag = 1
            break
    if flag == 0:
        dictionary.update({surname: vote})

for t in sorted(dictionary):
    print(t, dictionary[t])