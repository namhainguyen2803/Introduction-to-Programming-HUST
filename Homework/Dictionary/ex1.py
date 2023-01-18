'''
In US, the president is not elected by direct vote, but by a two-level vote. First, elections are held in each state and the winner of the elections in that state is determined. Then state elections are held: in these elections, each state has a certain number of votes - the number of electors from that state. In practice, all state electors vote according to the results of intra-state voting, that is, states with a different number of votes vote in the final stage of elections. You know who each state voted for and how many votes were cast by that state. Summarize the results of the elections: for each of the voting participants, determine the number of votes cast for him.

Input:

Each line of the input file contains the name of the candidate for which the electors of that state are voting, then separated by a space is the number of electors who voted for this candidate.

Output:

Print the surnames of all candidates in lexicographic order, then the number of votes cast for them.
'''
text = []
while True:
    try:
        text.append(input().split(' '))
    except:
        break

lis_name = []
lis_score = []

for tex in text:
  if tex[0] not in lis_name:
    lis_name.append(tex[0])
for name in lis_name:
  score = 0
  for tex in text:
    if name == tex[0]:
      score = score + int(tex[1])
  lis_score.append(score)
lis_score_name = list(zip(lis_name,lis_score))
lis_score_name.sort()
for name in lis_score_name:
  print(str(name[0])+ ' '+ str(name[1]))


'''
McCain 10
AcCain 5
Obama 9
Obama 8
EcCain 1
'''