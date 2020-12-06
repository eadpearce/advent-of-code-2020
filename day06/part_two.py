import parser

question_answers = parser.parse_file('data.txt')

totals = []

for answers in question_answers:
    group = [list(a) for a in answers if a]
    common = set(group[0]).intersection(*group)
    lengths = [len(c) for c in common]
    totals.append(sum(lengths))

print(sum(totals))
