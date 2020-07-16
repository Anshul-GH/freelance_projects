'''
    4. King is preparing for the war and has decided to supply weapones to his soldiers.
    •  There are N weapones which are placed on each other (stacked) in a case, The                          weapones are either sword or spear.
    • Each soldier has his/her own expertise for the type of weapon. They are queued to receive their favorite weapon.
    • If the soldier finds that the weapon at the top of the case is NOT as per his/her expertise he/she will go back and rejoin the queue and process will continue.
    • If the soldier finds that the weapon at the top of the case is as per his/her expertise he/she will leave the queue along with the weapon at the top.
    • Estimate the number of soldiers who will not be able to get the weapon.

Input Format:
   Input 1: N denoting the number of soldiers and weapones.
   Input 2: An array/stack of N elements. each element denoting the type of weapon from top to bottom. Can be either 0 (sword) or 1 (spear).
   Input 3: An array/queue of N elements. each element denoting the soldier standing with expertise 0 (sword) or 1 (spear) from the start till the end of the queue.

Output Formats:
For the given input your code should output the number of soldiers who will not be able to get the weapon.

'''

def count_soldiers(cnt, weapon_type, soldier_pref):
    # count of the soldiers that remain without weapon at any given point of time
    rem_sold = cnt
    # maximum possible iterations of the while loop allowed
    max_iter = 2 * cnt
    # flag that tracks change of length for the list
    len_chg = False
    while (max_iter != 0) and (rem_sold != 0):                
        if soldier_pref[0] == weapon_type[0]:
            # dropping the soldier and weapon pref upon match
            soldier_pref = soldier_pref[1:]
            weapon_type = weapon_type[1:]
            
            # length changed
            len_chg = True
            rem_sold -= 1
        else:
            # length not changed
            len_chg = False
            
        if not len_chg:
            # rotating the list in circular fashion
            soldier_pref = soldier_pref[1:] + soldier_pref[:1]
            max_iter -= 1

    print("Number of soldiers without weapon:", rem_sold)
                



if __name__ == "__main__":
    print("Enter the number of soldiers/weapons:")
    cnt = int(input())
    weapon_type = []
    soldier_pref = []
    
    print("Enter the type of weapon 0 (sword) or 1 (spear)")
    print("(Please press return(enter) key after each number entered.):")
    for i in range(cnt):
        weapon_type.append(int(input()))
    
    print("Enter the preferences of soldiers 0 (sword) or 1 (spear)")
    print("(Please press return(enter) key after each number entered.):")
    for i in range(cnt):
        soldier_pref.append(int(input()))
    
    count_soldiers(cnt, weapon_type, soldier_pref)