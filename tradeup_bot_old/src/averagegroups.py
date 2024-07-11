import itertools
def findgroups(reqcollections, matchingskins, targetfloat, maxiterations=10000):
    def initialize_group(reqcollections):
        group = []
        for collection in reqcollections:
            for _ in range(collection["numberofskins"]):
                group.append({"float": float('inf'), "collection": collection["collection"], "wear": collection["wear"], "used": False})
        return group

    def calculate_average_float(group):
        return sum(item["float"] for item in group) / len(group)


    def is_collection(collection, item2):
        # Returns true if it is viable
        return collection['collection'] == item2['collection'] and collection['wear'] == item2['wear'] and item2['used']== False

    def Get_all_group_combos(items_by_type, reqcollections, current_group=[], current_index=0):
        # This function determines all the possible combinations for the avaiable skins and the required collections in the tradeup. 
        # It functions by determining all of the combinations for each skin sorted by its collection and wear (type of skin) , with the amount of that collection in the tradeup. 
        if current_index == len(items_by_type):
            yield current_group  # All skin types processed, yield current group composition
            return

        for combination in itertools.combinations(items_by_type[current_index], reqcollections[current_index]['numberofskins']):
            # For each combination of the current type, recurse to process the next type
            yield from Get_all_group_combos(items_by_type, reqcollections, current_group + list(combination), current_index + 1) #yeild from expands the whole for loop ty gpt

       
    def find_a_group(all_groups, targetfloat, maxcombinations):
        #this funciton works by searching a given amount of combinations and returning the first one that meets the criteria. 
        i = 0
        # all_groups = itertools.filterfalse(lambda combo: any(skin['used'] for skin in combo), all_groups)
        for combo in all_groups:
            i+=1
            if i > maxcombinations:
                er = "max iterations reached, cannot find group at desired float"
                return None, er
            avg_float = calculate_average_float(combo)
            floattoleratancescalingfac = ((maxiterations - i) / maxiterations)
            if targetfloat * 0.9 * floattoleratancescalingfac <= avg_float <= targetfloat: #need to think about what criteria you want to use, mayebe it should be adjustable
                for skin in combo:
                    skin['used']= True
                return combo, None
        er= "searched whole search space, no float solution for group"
        return None, er
        
    
    def get_items_by_type(reqcollections, matchingskins):
        items_by_type = []
        for collection in reqcollections:
            itemsofcollection = [skin for skin in matchingskins if is_collection(collection, skin)]
            items_by_type.append(itemsofcollection)
        return items_by_type

    def remainingskins(reqcollections, matchingskins):
        #this fucntion should return false when there is not enough skins to achieve another tradeup
        items_by_type = get_items_by_type(reqcollections, matchingskins) #returns only unused skins
        for i, type in enumerate(items_by_type):
            # print(f'num needed per collection{reqcollection[i]['numberofskins']} num remaining {len(type)}')
            # print()
            if reqcollection[i]['numberofskins'] > len(type):
                return False
        return True


    groups = []
    while remainingskins(reqcollections, matchingskins):
        items_by_type = get_items_by_type(reqcollections,matchingskins)
        all_groups = Get_all_group_combos(items_by_type, reqcollections)
        a_group, er = find_a_group(all_groups, targetfloat, maxiterations)
        if a_group:
            groups.append(a_group) # after finding the first one it takes forever to find the second one becuase the items were used. we need to filter out the used ones. I think there will be a methods based upon how combinations are sorted. 
        # print(f'\n group: \n {a_group}')
        if er:
            break
    return groups, er



# Example usage
items = random_numbers = [
    0.1145775959863069,
    0.10926674815358756,
    0.11673988413973654,
    0.08393774331929273,
    0.09389904619329893,
    0.13251237330298184,
    0.1192016495784261,
    0.08652774787173292,
    0.12721156920667463,
    0.17957912960545815,
    0.09852473026160515,
    0.08766323992522157,
    0.10624922259167973,
    0.1366869390455721,
    0.10197293356925668,
    0.08557034198207625,
    0.07623875833451102,
    0.09431275966075626,
    0.0979826562460538,
    0.11240280834747006,
    0.14372255393622945,
    0.03227544756462467,
    0.02996597042240016,
    0.09227363556277757,
    0.10805554878527118,
    0.11880111482346476,
    0.17332599420123606,
    0.18567137478931865,
    0.08175557624963784,
    0.10255680203565917,
    0.11959038849043992,
    0.09384746721593557,
    0.10683679268556745,
    0.08988672456949556,
    0.1658214414266628,
    0.08915958609487647,
    0.11449791564761847,
    0.11532905393289973,
    0.11912814516559339,
    0.12171230644608448
]


def av_val(group):
    total = sum(num['float'] for num in group)
    return total / len(group) if group else 0



numbers = []
for idx, num in enumerate(items):
    if idx in range(0,16):
        numbers.append({"loc": idx, "float": num,"used": False, "collection": "Shadow", "wear": "Factory New" })
    else:
        numbers.append({"loc": idx, "float": num,"used": False, "collection": "Chroma", "wear": "Minimal Wear" })

reqcollection = [{"collection": "Chroma","wear": "Minimal Wear", "numberofskins": 6, }, {"collection": "Shadow", "wear": "Factory New", "numberofskins": 4}]

targetfloat = 0.0001
print(f"\ntarget float:{targetfloat}")

groups, er = findgroups(reqcollection, numbers, targetfloat)
print(er)
for group in groups:
    print(f'group {group} avfloat {av_val(group)}')
    print('END SKIN _______________________________________________')


# # Original list
# my_list  = [
#     0.1145775959863069,
#     0.10926674815358756,
#     0.11673988413973654,
#     0.08393774331929273,
#     0.09389904619329893,
#     0.13251237330298184,
#     0.1192016495784261,
#     0.08652774787173292,
#     0.12721156920667463,
#     0.17957912960545815,
#     0.09852473026160515,
#     0.08766323992522157,
#     0.10624922259167973,
#     0.1366869390455721,
#     0.10197293356925668,
#     0.08557034198207625]

# # Slice the list to keep elements from index 2 to 6 (exclusive of 7)
# my_list = my_list[2:7]

# # Now my_list is permanently changed to the slice
# print(my_list)

# # List of mutable elements (lists)
# items = [[1], [2], [3]]

# # Generate combinations
# combos = itertools.combinations(my_list, 6)

# # Change an element in the original list
# items[0][0] = 2

# # The change is reflected in the generated combinations
# print("Combinations after changing the original list:")
# for combo in combos:
#     print(combo)

# # Directly modifying an element within a combination
# combos[0][0][0] = 20  # This changes the content of the first list in the first combination
# print("\ combos after modifying a combination:")
# for combo in combos:
#     print(combo)

# # This change is also reflected back in the original list
# print("\nOriginal list after modifying a combination:")
# print(items)