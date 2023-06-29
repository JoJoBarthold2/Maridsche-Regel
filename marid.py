

def MaridscheRegel():
    your_age = int(input("State your age in years:\n"))
    partner_age = int( input("State your partners age in years: \n"))
    older_age = max(your_age,partner_age)
    younger_age = min(partner_age, your_age)
    compare_age = older_age/2 +7
    if(compare_age > younger_age):
        print("Marid sagt nein")
    else:
        print("All good")


MaridscheRegel()