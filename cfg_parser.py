import nltk
from nltk import CFG, ChartParser

# Define the CFG grammar rules
atis_grammar = CFG.fromstring("""
S -> WH NP VP
S -> VP
WH -> 'what'
WH -> 'show'
NP -> Det N
NP -> N
NP -> Pronoun
NP -> NP PP
NP -> ProperNoun
NP -> ProperNoun ProperNoun
NP -> Det ProperNoun
NP -> Det N PP
VP -> V
VP -> V NP
VP -> VP PP
VP -> V Adj
VP -> V Pronoun NP
PP -> Preposition NP

Det -> 'a'
Det -> 'the'
N -> 'flight'
N -> 'flights'
N -> 'ticket'
V -> 'are'
V -> 'is'
V -> 'have'
V -> 'want'
V -> 'find'
V -> 'show'
V -> 'available'
Adj -> 'available'
Preposition -> 'from'
Preposition -> 'to'
ProperNoun -> 'boston'
ProperNoun -> 'dallas'
ProperNoun -> 'chicago'
ProperNoun -> 'new'
ProperNoun -> 'york'
ProperNoun -> 'san'
ProperNoun -> 'francisco'
ProperNoun -> 'denver'
Pronoun -> 'me'
Pronoun -> 'i'
""")

# Initialize the parser with the grammar
parser = ChartParser(atis_grammar)

# Read tokenized sentences from file
with open('ATIS_list.txt', 'r') as f:
    lines = f.readlines()

# Parse each sentence and print the first parse tree if available
for idx, line in enumerate(lines):
    tokens = eval(line.strip())  # Convert string representation of list back to list
    print(f"\nSentence {idx+1}: {' '.join(tokens)}")
    try:
        trees = list(parser.parse(tokens))
        if trees:
            # Print only the first parse tree
            trees[0].pretty_print()
        else:
            print("No parse tree found.")
    except Exception as e:
        print("Error parsing:", e)
