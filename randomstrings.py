# I was giving a lesson on 'genetic clock,' the idea that we can date evolutionary divergence by number of
# mutations in junk DNA. I wished to run an activity where students looked at two strings of DNA, counted
# the number of differences, and used a formula to estimate the date of divergence. Actual rate of mutation
# is very slow, so to get the timescale I wanted, students would need to read thousands of real nucleotides.
# Instead, I generated two random nonsense strings side by side, where there was an 11% chance that a particular
# nucleotide would be generated separately for each string, otherwise giving the same value. 

import random

gen1 = str()
gen2 = str()

for i in range(0,100):
    a = random.random()
    b = random.random()
    if a<.11:
        c = random.random()
        if b<.25:
            gen1 += "A"
        elif b<.5:
            gen1 += "T"
        elif b<.75:
            gen1 += "G"
        else:
            gen1 += "C"
        if c<.25:
            gen2 += "A"
        elif c<.5:
            gen2 += "T"
        elif c<.75:
            gen2 += "G"
        else:
            gen2 += "C"
    else:
        if b<.25:
            gen1 += "A"
            gen2 += "A"
        elif b<.5:
            gen1 += "T"
            gen2 += "T"
        elif b<.75:
            gen1 += "G"
            gen2 += "G"
        else:
            gen1 += "C"
            gen2 += "C"

print(gen1)
print(gen2)

count = 0

for i in range(0,len(gen1)):
    if gen1[i]!=gen2[i]:
        count += 1

print(count)
