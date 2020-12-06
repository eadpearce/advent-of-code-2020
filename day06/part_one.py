import parser

strings = parser.parse('data.txt')

lengths = [len(set(s)) for s in strings]

print(sum(lengths))
