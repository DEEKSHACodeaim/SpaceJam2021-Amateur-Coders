def conjunctivitis():
    count=0
    for i in symp:
        if i=='7':
            count+=1
        if i=='8':
            count+=1
        if i=='13':
            count+=1
        else:
            continue
    if count>=2:
        print("Patient has been affected with CONJUNCTIVITIS!")
        print("Medications:\n Lubricant eye drops \n wash hands regularly \n remove contact lenses")


def AllergicRhinitis():
    count=0
    for i in symp:
        if i=='7':
            count+=1
        if i=='8':
            count+=1
        else: 
            continue
    if count>=1:
        print("Patient has been affected with ALLERGIC RHINITIS")
        print("Medications:\n Antihistamines \n corticosteroid nasal spray:")
