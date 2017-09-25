# -*- coding: utf-8 -*-

def gen_rule_str(a, b, val=None, val_fmt='{:.3f}', sep=" = "):
    text = "{} => {}".format(a, b)
    if val:
        text = "conf(" + text + ")"
        text += sep + val_fmt.format(val)
    return text

def print_rules(rules):
    if type(rules) is dict or type(rules) is defaultdict:
        from operator import itemgetter
        ordered_rules = sorted(rules.items(), key=itemgetter(1), reverse=True)
    else: # Assume rules is iterable
        ordered_rules = [((a, b), None) for a, b in rules]
    for (a, b), conf_ab in ordered_rules:
        print(gen_rule_str(a, b, conf_ab))

english_text = """
But I must explain to you how all this mistaken idea
of denouncing of a pleasure and praising pain was
born and I will give you a complete account of the
system, and expound the actual teachings of the great
explorer of the truth, the master-builder of human
happiness. No one rejects, dislikes, or avoids
pleasure itself, because it is pleasure, but because
those who do not know how to pursue pleasure
rationally encounter consequences that are extremely
painful. Nor again is there anyone who loves or
pursues or desires to obtain pain of itself, because
it is pain, but occasionally circumstances occur in
which toil and pain can procure him some great
pleasure. To take a trivial example, which of us
ever undertakes laborious physical exercise, except
to obtain some advantage from it? But who has any
right to find fault with a man who chooses to enjoy
a pleasure that has no annoying consequences, or
one who avoids a pain that produces no resultant
pleasure?

On the other hand, we denounce with righteous
indignation and dislike men who are so beguiled and
demoralized by the charms of pleasure of the moment,
so blinded by desire, that they cannot foresee the
pain and trouble that are bound to ensue; and equal
blame belongs to those who fail in their duty
through weakness of will, which is the same as
saying through shrinking from toil and pain. These
cases are perfectly simple and easy to distinguish.
In a free hour, when our power of choice is
untrammeled and when nothing prevents our being
able to do what we like best, every pleasure is to
be welcomed and every pain avoided. But in certain
circumstances and owing to the claims of duty or
the obligations of business it will frequently
occur that pleasures have to be repudiated and
annoyances accepted. The wise man therefore always
holds in these matters to this principle of
selection: he rejects pleasures to secure other
greater pleasures, or else he endures pains to
avoid worse pains.
"""

latin_text = """
Sed ut perspiciatis, unde omnis iste natus error sit
voluptatem accusantium doloremque laudantium, totam
rem aperiam eaque ipsa, quae ab illo inventore
veritatis et quasi architecto beatae vitae dicta
sunt, explicabo. Nemo enim ipsam voluptatem, quia
voluptas sit, aspernatur aut odit aut fugit, sed
quia consequuntur magni dolores eos, qui ratione
voluptatem sequi nesciunt, neque porro quisquam est,
qui dolorem ipsum, quia dolor sit amet consectetur
adipisci[ng] velit, sed quia non numquam [do] eius
modi tempora inci[di]dunt, ut labore et dolore
magnam aliquam quaerat voluptatem. Ut enim ad minima
veniam, quis nostrum exercitationem ullam corporis
suscipit laboriosam, nisi ut aliquid ex ea commodi
consequatur? Quis autem vel eum iure reprehenderit,
qui in ea voluptate velit esse, quam nihil molestiae
consequatur, vel illum, qui dolorem eum fugiat, quo
voluptas nulla pariatur?

At vero eos et accusamus et iusto odio dignissimos
ducimus, qui blanditiis praesentium voluptatum
deleniti atque corrupti, quos dolores et quas
molestias excepturi sint, obcaecati cupiditate non
provident, similique sunt in culpa, qui officia
deserunt mollitia animi, id est laborum et dolorum
fuga. Et harum quidem rerum facilis est et expedita
distinctio. Nam libero tempore, cum soluta nobis est
eligendi optio, cumque nihil impedit, quo minus id,
quod maxime placeat, facere possimus, omnis voluptas
assumenda est, omnis dolor repellendus. Temporibus
autem quibusdam et aut officiis debitis aut rerum
necessitatibus saepe eveniet, ut et voluptates
repudiandae sint et molestiae non recusandae. Itaque
earum rerum hic tenetur a sapiente delectus, ut aut
reiciendis voluptatibus maiores alias consequatur
aut perferendis doloribus asperiores repellat.
"""

#print("First 100 characters:\n  {} ...".format(latin_text[:100]))

'''
2.0.1
Complete the following function, normalize_string(s), which should take a string 
(str object) s as input and returns a new string with all characters converted to 
lowercase and all non-alphabetic, non-space characters removed.
'''
def normalize_string(s):
    assert type (s) is str
    return ''.join(c for c in s.lower() if c.isalpha() or c.isspace())
#print(latin_text[:100], "...\n=>", normalize_string(latin_text[:400]), "...")
norm_latin_text = normalize_string(latin_text)

'''
2.0.2
Implement the following function, get_normalized_words(s): given a string 
(str object) s, returns a list of its words, normalized per the definition of 
normalize_string().
'''
def get_normalized_words (s):
    assert type (s) is str
    return s.split()
#print ("First five words:\n{}".format (get_normalized_words (latin_text)[:5]))
norm_latin_words = get_normalized_words(norm_latin_text)

'''
2.0.3
Implement a function, make_itemsets, that given a list of strings converts the 
characters of each string into an itemset, returning the list of itemsets.
'''
def make_itemsets(words):
    return [set(w) for w in words]
norm_latin_itemsets = make_itemsets(norm_latin_words)

'''2.0.4
Start by implementing a function that enumerates all item-pairs within an itemset 
and updates a table in-place that tracks the counts of those item-pairs.
You may assume all items in the given itemset (itemset argument) are distinct, 
i.e., that you may treat it as you would any set-like collection. You may also 
assume pair_counts is a default dictionary.
'''
from collections import defaultdict
from itertools import combinations # Hint!

def update_pair_counts (pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type (pair_counts) is defaultdict
    for p in combinations(sorted(itemset), 2):
        pair_counts[p] += 1
        pair_counts[p[::-1]] += 1

# `update_pair_counts_test`: basic test sequence
itemset_1 = set("error")
itemset_2 = set("dolor")
pair_counts = defaultdict(int)
#update_pair_counts(pair_counts, itemset_1)
#update_pair_counts(pair_counts, itemset_2)
#print(dict(pair_counts))

'''
2.0.5
As with the previous exercise, you may assume all items in the given itemset (itemset) 
are distinct, i.e., that you may treat it as you would any set-like collection. 
You may also assume the table (item_counts) is a default dictionary.
'''
def update_item_counts(item_counts, itemset):
 #Assume all items in the given itemset (itemset) are distinct, i.e. a set-like collection. 
 #Assume the table (item_counts) is a default dictionary.
    for i in itemset:
        item_counts[i]+=1 

#test
item_counts = defaultdict(int)
#update_item_counts(item_counts, itemset_1)
#update_item_counts(item_counts, itemset_2)
#print(dict(item_counts))

'''
2.0.6
Given tables of item-pair counts and individual item counts, as well as a confidence 
threshold, return the rules that meet the threshold. The returned rules should be 
in the form of a dictionary whose key is the tuple,  (a,b)(a,b)  corresponding to the 
rule  a⇒ba⇒b , and whose value is the confidence of the rule,  conf(a⇒b)conf(a⇒b) .
You may assume that if  (a,b)(a,b)  is in the table of item-pair counts, then both  
a and b are in the table of individual item counts.
'''
def filter_rules_by_conf (pair_counts, item_counts, threshold, min_count=0):
    '''
    Inputs are dictionaries of:
        -number of times items appear in sets
        -number of times item pairs (a,b) appear in sets
    Output is a dictionary giving the occurrence rates for b given a; ie. P(b|a), 
    filtered to produce only those pairs with P(b|a) meeting or exceeding the
    input 'threshold' value
    '''
    rules = {} # (item_a, item_b) -> conf (item_a => item_b)
    for pc in pair_counts:
        ab = pair_counts[pc]
        a = item_counts[pc[0]]
        if (ab/a) >= threshold and a>=min_count:
            rules[pc]=ab/a
    return rules
rules = filter_rules_by_conf (pair_counts, item_counts, 0.5)
#print(rules)
#print_rules(rules)

'''
2.0.7
Using the building blocks you implemented above, complete a function find_assoc_rules 
so that it implements the basic association rule mining algorithm and returns a 
dictionary of rules.
In particular, your implementation may assume the following:
-As indicated in its signature, below, the function takes two inputs: receipts and threshold.
-The input, receipts, is a collection of itemsets: for every receipt r in receipts, 
 r may be treated as a collection of unique items.
-The input threshold is the minimum desired confidence value. That is, the function 
 should only return rules whose confidence is at least threshold.
The returned dictionary, rules, should be keyed by tuples (a,b) corresponding 
to the rule a⇒b; each value should record the confidence conf(a⇒b) of the rule.
'''
def find_assoc_rules(receipts, threshold, min_count=0):
    '''
    Input 'receipts' is a list of sets containing items such as letters occurring 
    in words or goods appearing on receipts.
    Intermediate product is pair of dictionaries tallying frequencies.
    Output is a dictionary giving the occurrence rates for finding b in a set if a 
    is present; ie. P(b|a), filtered to produce only those pairs with P(b|a) 
    meeting or exceeding the input 'threshold' value.
    '''
    pair_counts = defaultdict(int)
    item_counts = defaultdict(int)
    for i in receipts:
        update_pair_counts(pair_counts, i)
        update_item_counts(item_counts, i) 
    return filter_rules_by_conf (pair_counts, item_counts, threshold, min_count), pair_counts, item_counts

'''
2.0.8
For the Latin string, latin_text, use your find_assoc_rules() function to compute the 
rules whose confidence is at least 0.75. Store your result in a variable named latin_rules.
'''
latin_rules, pc, ic=find_assoc_rules(norm_latin_itemsets, 0.75)
#print_rules(latin_rules)
#print([[a,b,c] for (a,b),c in R.items()][:5]) 
#import csv
#with open('letter_pairs.csv','w') as f:
#    w = csv.writer(f)
#    w.writerows([k1,k2,v] for (k1, k2), v in latin_rules.items())

'''
2.0.9
Write a function that, given two dictionaries, finds the intersection of their keys.
'''
def intersect_keys(d1, d2):
    assert type(d1) is dict or type(d1) is defaultdict
    assert type(d2) is dict or type(d2) is defaultdict
    s1 = set(d1)
    s2 = set(d2)
    return s1.intersection(s2)

'''
2.0.10
Write some code that finds all high-confidence rules appearing in both the Latin text 
and the English text. Store your result in a list named common_high_conf_rules whose 
elements are (a,b) pairs corresponding to the rules a⇒b.
'''
def produce_itemsets_from_text(orig_text):
    """ 
    produce itemsets tabulating word letter sets from a space separated input text
    """
    norm_text = normalize_string(orig_text) #''.join(c for c in s.lower() if c.isalpha() or c.isspace())
    norm_words = get_normalized_words (norm_text) #s.split()
    return make_itemsets(norm_words)   #[set(w) for w in words]
        
english_set = produce_itemsets_from_text(english_text)
Pba_english, pc, ic = find_assoc_rules(english_set, 0.75)
latin_set = produce_itemsets_from_text(latin_text)
Pba_latin, pc, ic = find_assoc_rules(latin_set, 0.75)
common_high_conf_rules = intersect_keys(Pba_english, Pba_latin)
#print("High-confidence rules common to _lorem ipsum_ in Latin and English:")
#print_rules(common_high_conf_rules)    

'''
2.0.11


here's a code snippet to download the data, which is a text file:'''
#import requests
#response = requests.get ('https://cse6040.gatech.edu/datasets/groceries.csv')
#groceries_file = response.text  # or response.content for raw bytes
#OR
with open('groceries.csv','r') as f:
    groceries_file=f.read()
#print (groceries_file[0:250] + "...\n... (etc.) ...") # Prints the first 250 characters only
'''Each line of this file is some customer's shopping basket. The items that the 
customer bought are stored as a comma-separated list of values.

Mine this dataset for pairwise association rules. In particular, your code should produce (no 
pun intended!) a final dictionary, basket_rules, that meet these conditions (read carefully!):
1. The keys are pairs (a,b), where a and b are item names (as strings).
2. The values are the corresponding confidence scores, conf(a⇒b).
3. Only include rules a⇒b where item a occurs at least MIN_COUNT times and 
   conf(a⇒b) is at least THRESHOLD.
'''
THRESHOLD = 0.5
MIN_COUNT = 10

norm_receipts = groceries_file.split('\n')    
grocery_itemsets = [set(r.split(',')) for r in norm_receipts]
basket_rules, pc, ic = find_assoc_rules(grocery_itemsets, THRESHOLD, MIN_COUNT)

#Summary:
#.1. norm_latin_text = normalize_string(latin_text)
# 2. norm_latin_words = get_normalized_words (norm_latin_text)
# 3. norm_latin_itemsets = make_itemsets(norm_latin_words)
#    pair_counts = defaultdict(int)
# 4. update_pair_counts (pair_counts, itemset)
#    item_counts = defaultdict(int)
# 5. update_item_counts(item_counts, itemset)
# 6. filter_rules_by_conf (pair_counts, item_counts, 0,5)
# 7. find_assoc_rules(receipts, threshold)
# 8. latin_rules=find_assoc_rules(norm_latin_itemsets, 0.75)
  # input 'receipt' is a list of sets containing items such as letters occurring 
  # in words or goods appearing on receipts
  # output is a list of item pairs which occur at least as often as the input 'threshold'
# 9. intersect_keys(d1, d2)

