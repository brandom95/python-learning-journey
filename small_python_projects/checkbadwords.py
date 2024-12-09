from profanity_filter import ProfanityFilter


pf= ProfanityFilter()
print(pf.censor("fuck"))

print(pf.censor_word('tits'))
