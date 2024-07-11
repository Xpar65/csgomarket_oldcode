import requests
import json
import random
import time
import copy
import itertools
from bs4 import BeautifulSoup
from collections import defaultdict
import os



trade_ups_example = [
        {
        'tradeupid': 0,
        'tier': 'Restricted',                      #covert 6 Restricted 5 .... # check what the csfloat inspect api uses. 
        'average_float': 0.14,  #  desired float
        'StatTrak': 'Normal' ,               # 0: normal/StatTrak
        'cases': [
            {'collection_name': 'The Shadow Collection', 'wear': 'Minimal Wear', 'skin_num': 4},             #Wear : FN=0... BS=4 
            {'collection_name': 'The Chroma Collection', 'wear': 'Factory New','skin_num': 6},
            # ... up to 10
        ],
    },

     {
        'tradeupid': 1,
        'tier': 'Mil-Spec Grade',                      #covert 6 Restricted 5 .... # check what the csfloat inspect api uses. 
        'average_float': 0.0699,  # desired float
        'StatTrak': 'Normal' ,               # 0: normal, 1: ST 2: SV StatTrakâ„¢
        'cases': [
            {'collection_name': 'The Shadow Collection', 'wear': 'Minimal Wear', 'skin_num': 4},             #Wear : FN=0... BS=4 
            {'collection_name': 'The Chroma Collection', 'wear': 'Factory New', 'skin_num': 6},
            # ... up to 10
        ],
    },

        {
        'tradeupid': 2,
        'tier': 'Mil-Spec',                      #covert 6 Restricted 5 .... # check what the csfloat inspect api uses. 
        'average_float': 0.3,  #  desired float (actual av comes out like 0.2999 with my calc)
        'StatTrak': 'StatTrak' ,               # 0: normal, 1: ST 2: SV StatTrakâ„¢
        'cases': [
            {'collection_name': 'The Shadow Collection', 'wear': 'Minimal Wear', 'skin_num': 1},    #stattrak scar 20
            {'collection_name': 'The Chroma 2 Collection', 'wear': 'Field-Tested','skin_num': 1},   #p250 valence
            {'collection_name': 'The Breakout Collection', 'wear': 'Well-Worn','skin_num': 1},      #ssg abyss
            {'collection_name': 'The Chroma 2 Collection', 'wear': 'Factory New','skin_num': 1},    #MP7 | Armor Core
            {'collection_name': 'The Gamma Collection', 'wear': ' Field-Tested','skin_num': 1},     #Nova | Exo
            {'collection_name': 'The Phoenix Collection', 'wear': 'Well-Worn','skin_num': 1},       #Negev | Terrain
            {'collection_name': 'The Glove Collection', 'wear': 'Well-Worn','skin_num': 1},         #Galil AR | Black Sand
            {'collection_name': 'The Phoenix Collection', 'wear': 'Field-Tested','skin_num': 1},    #Tec-9 | Sandstorm
            {'collection_name': 'The Gamma Collection', 'wear': 'Battle-Scarred','skin_num': 1},    #Five-SeveN | Scumbria
            {'collection_name': 'The Gamma 2 Collection', 'wear': 'Field-Tested','skin_num': 1},    #P90 | Grim
            
        ],
    },

            {
        'tradeupid': 2,
        'tier': 'Mil-Spec',                      #covert 6 Restricted 5 .... # check what the csfloat inspect api uses. 
        'average_float': 0.3,  #  desired float (actual av comes out like 0.2999 with my calc)
        'StatTrak': 'Souvenir' ,               # 0: normal, 1: ST 2: SV StatTrakâ„¢
        'cases': [
            {'collection_name': 'The Shadow Collection', 'wear': 'Minimal Wear', 'skin_num': 1},    #stattrak scar 20
            {'collection_name': 'The Chroma 2 Collection', 'wear': 'Field-Tested','skin_num': 1},   #p250 valence
            {'collection_name': 'The Breakout Collection', 'wear': 'Well-Worn','skin_num': 1},      #ssg abyss
            {'collection_name': 'The Chroma 2 Collection', 'wear': 'Factory New','skin_num': 1},    #MP7 | Armor Core
            {'collection_name': 'The Gamma Collection', 'wear': 'Factory New','skin_num': 1},       #Nova | Exo
            {'collection_name': 'The Phoenix Collection', 'wear': 'Well-Worn','skin_num': 1},       #Negev | Terrain
            {'collection_name': 'The Glove Collection', 'wear': 'Well-Worn','skin_num': 1},         #Galil AR | Black Sand
            {'collection_name': 'The Phoenix Collection', 'wear': 'Field-Tested','skin_num': 1},    #Tec-9 | Sandstorm
            {'collection_name': 'The Gamma Collection', 'wear': 'Battle-Scarred','skin_num': 1},    #Five-SeveN | Scumbria
            {'collection_name': 'The Gamma 2 Collection', 'wear': 'Field-Tested','skin_num': 1},    #P90 | Grim
            
        ],
    },
    
    #more trade-ups
]

#final
trade_ups_example_aftergrouping = [
    {
        'tradeupid': 0, 
        'tier': 'Mil-Spec Grade',
        'average_float': 0.0699,
        'StatTrak': 'Normal',
        'cases': 
        [
            {
                'collection_name': 'The Shadow Collection',
                'wear': 'Minimal Wear',
                'skin_num': 4,
                'skins': [
                        {'loc': 0, 'float': 0.07},
                        {'loc': 1, 'float': 0.06},
                        {'loc': 2, 'float': 0.65, 'unused': True},
                        # ... more skins
                            ],
            },
            {
                'collection_name': 'The Chroma Collection',
                'wear': 'Factory New',
                'skin_num': 6,
                'skins': [
                        {'loc': 0, 'float': 0.07},
                        {'loc': 1, 'float': 0.06},
                        {'loc': 1, 'float': 0.65, 'unused': True},
                        # ... more skins
                            ],
            },
            # ... up to 10 cases
        ],
        'trades': 
        [
            {
            'tradeid': 0,
            'trade_av_float': 0.06374734,
                    'skins': [
                        {'loc': 0, 'float': 0.07},
                        # ... 10 skins
                            ],
            }
                #more trades
        ]
    }
    #more tradeup entries
]


def load_json(folder_name, file_name):
    #file_path = f'Unittestfiles/mock_data/{folder_name}/{file_name}'
    file_path = f'C:/Users/liamc/Desktop/Folders/Projects/CSGO/csgomarket/csgomarket/{folder_name}/{file_name}'
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(filedata, folder_name, file_name):
    #file_path = f'Unittestfiles/mock_data/{folder_name}/{file_name}'
    # Ensure the directory exists (creates if not)
    file_path = f'C:/Users/liamc/Desktop/Folders/Projects/CSGO/csgomarket/csgomarket/{folder_name}/{file_name}'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
            json.dump(filedata, file, indent=4)

class SkinManager:
    def __init__(self, inventory):
        self.inventory = inventory

    def update_skin(self, loc, new_details):
        if 0 <= loc < len(self.inventory['descriptions']):
            self.inventory['descriptions'][loc].update(new_details)

    def get_skin(self, loc):
        if 0 <= loc < len(self.inventory['descriptions']):
            return self.inventory['descriptions'][loc]
        return None


def setupdesc(inventory):
    def assetidfinder(inventory, classid):
        # This function will return the description of a given asset id from original
        for item in inventory['descriptions']:
            if classid == item['classid']:
                return item
        return None
    #this function makes the 'descriptions' have the same amount of skins in the right order of the actual inventory. (It doesn't show skins which are the same.)
    pastclassids = []
    new_desc = inventory['descriptions'] #have to do this bc we are changing size of current dict. 
    for idx, item in enumerate(inventory['assets']):
        classid = item['classid']
        if pastclassids:
            if classid in pastclassids:
                    newdict = assetidfinder(inventory, classid) #this assumes that they are all in a line. We need to fix this. 
                    newdict_copy = copy.deepcopy(newdict)
                    new_desc.insert(idx, newdict_copy)
                    #print(f"Inserted {inventory['descriptions'][idx]['name']} id:{classid} idx:{idx}")
        pastclassids.append(classid)
    inventory['descriptions'] = new_desc # update old inventory with new one. 

def deletenonweaponskins(inventory):
    def item_viability(item):
        item_type = item['type']
        viable_types = ('Covert', 'Classified', 'Restricted', 'Mil-Spec', 'Industrial', 'Consumer')

        return any(viable_type in item_type for viable_type in viable_types)

#this fucntion ensures that only weapons skins will be in desc, similar to the tradeup menu. 
    to_delete = []
    for idx, item in enumerate(inventory['descriptions']):
        if not item_viability(item):
            to_delete.append(idx)
    for idx in reversed(to_delete):
        del inventory['descriptions'][idx]
        del inventory['assets'][idx]

def addfloatinfo(inventory, steamID, max_retries = 3):
    
    def API_retrieval(inspectlink):
        try:
            if isinstance(inspectlink, dict):
                # Handle bulk request
                API_bulk_endpoint = "http://127.0.0.1:80/bulk"
                headers = {'Content-Type': 'application/json'}
                response = requests.post(API_bulk_endpoint, json=inspectlink, headers=headers)
            else:
                # Handle single request
                API_float_endpoint = "http://127.0.0.1:80/?url=" + inspectlink
                response = requests.get(API_float_endpoint)

            response.raise_for_status()
            floatdata = response.json()
            return floatdata, None  # Returning data and None for the error

        except Exception as e:
            return {}, str(e)  # Returning empty dict and error message
        

    error_occurred = False
    for idx, item in enumerate(inventory['descriptions']):
        delay = 1
        assetid = inventory['assets'][idx]['assetid']
        inspectlink = item['actions'][0]['link'].replace("%owner_steamid%", steamID).replace("%assetid%", assetid)
        retries = 0
        while retries < max_retries:
            floatdata, error = API_retrieval(inspectlink)
            if not error:
                item.update(floatdata) #why is this not updating properly. we get the same float data appended to similar types of skins and it makes no sense.
                inventory['descriptions'][idx]['assetid'] = assetid
                #print(f"idx: {idx}, assetid:  {assetid}")
                #print(inspectlink) 
                #print(floatdata)
                #print('ENDOFSKIN___________________________') 
                break
            else:
                retries += 1 
                print(f"Error occurred in API: {error}. Retrying... ({retries}/{max_retries}), delay: {delay}sec ")
                time.sleep(delay)
                delay *= 2
            if retries == max_retries:
                print("Max retries reached. Plz fix")
                error_occurred = True
                return error_occurred 
    return error_occurred

def calculate_max_tradeups(tradeups):
    
    def calculate_single_max_trades(tradeup):
        mintrades = float('inf')  
        for case in tradeup['cases']:
            if case['skin_num'] > 0:  #avoid division by zero
                maxtrades = case['inventory_count'] // case['skin_num']
                if maxtrades < mintrades: #we are just looking for smallest num
                    mintrades = maxtrades
        #incase 
        if mintrades == float('inf'):
            mintrades = 0

        return mintrades
    # Calculate the maximum number of trades for each tradeup
    for tradeup in tradeups:
        tradeup['max_trades'] = calculate_single_max_trades(tradeup)
    for i, current_tradeup in enumerate(tradeups):
        # Store the reduction in inventory counts for the current tradeup
        inventory_reduction = {}
        for case in current_tradeup['cases']:
            reduction = case['skin_num'] * current_tradeup['max_trades']
            inventory_reduction[(case['collection_name'], case['wear'])] = reduction # this makes the dictuonary in this format { ('shadow', 0.07): 6 }....

        # appliwa inventory reductions to subsequent tradeups
        for subsequent_tradeup in tradeups[i+1:]:#skips
            for case in subsequent_tradeup['cases']:
                case_key = (case['collection_name'], case['wear'])
                if case_key in inventory_reduction:
                    case['inventory_count'] = max(case['inventory_count'] - inventory_reduction[case_key], 0)
                    tradeup['max_trades'] = calculate_single_max_trades(tradeup)

def loc_of_skins(inventory, tradeups):
    #this function returns the location (inorder) and the float of each skin for each individual case of each trade for future use.
    skin_details_dict = {} 
    for tradeup in tradeups:
        for case in tradeup['cases']:
            case['skin_loc'] = []
            for idx, skin in enumerate(inventory['descriptions']):
                tier_match = tradeup['tier'] in skin['tags'][4]['localized_tag_name']
                st_sv_match = tradeup['StatTrak'] in skin['tags'][3]['localized_tag_name']
                wear_match = case['wear'] == skin['tags'][5]['localized_tag_name']
                collection_match = case['collection_name'] == skin['tags'][2]['localized_tag_name']

                if tier_match and st_sv_match and wear_match and collection_match:
                    skindeets = {'loc': idx, 'float': skin['iteminfo']['floatvalue'], 'collection': skin['tags'][2]['localized_tag_name'], 'wear': case['wear'], 'used': False}
                    case['skin_loc'].append(skindeets)
            # count = len(case['skin_loc'])
            # case['inventory_count'] = count 

def get_allskinsintradeup(tradeup):
    all_skins = []
    for case in tradeup['cases']:
        if 'skin_loc' in case:
            for skin in case['skin_loc']:
                    all_skins.append(skin)
    return all_skins

def get_reqcollections(tradeup):
    #reqcollection = [{"collection": "Chroma","wear": "Minimal Wear", "skin_num": 6, }, {"collection": "Shadow", "wear": "Factory New", "skin_num": 4}]
    reqcollections = []
    for case in tradeup['cases']:
        collection = {"collection": case['collection_name'],"wear": case['wear'], "skin_num": case['skin_num'] }
        reqcollections.append(collection)
    return reqcollections

def calc_av_group_float(group):
        return sum(item["float"] for item in group) / len(group)
def findgroups(tradeup, targetfloat, maxiterations=10000):
    def is_collection(collection, item2):
        #returns true if it is viable
        return collection['collection'] == item2['collection'] and collection['wear'] == item2['wear'] and item2['used']== False

    def Get_all_group_combos(items_by_type, reqcollections, current_group=[], current_index=0):
        if current_index == len(items_by_type):
            yield current_group  # All types processed, yield current group composition
            return

        for combination in itertools.combinations(items_by_type[current_index], reqcollections[current_index]['skin_num']):
            # For each combination of the current type, recurse to process the next type
            yield from Get_all_group_combos(items_by_type, reqcollections, current_group + list(combination), current_index + 1)

       
    def find_a_group(all_groups, targetfloat, maxiterations):
        #
        i = 0
        er = 0
        all_groups = itertools.filterfalse(lambda combo: any(skin['used'] for skin in combo), all_groups)
        for combo in all_groups:
            i+=1
            if i > maxiterations:
                er = "max iterations reached, cannot find group at desired float"
                return None, er
            avg_float = calc_av_group_float(combo)
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
        return items_by_type #this will be a set of skins sorted by collection. 

    def remainingskins(reqcollections, matchingskins):
        #this fucntion should return false when there is not enough skins to achieve another tradeup
        items_by_type = get_items_by_type(reqcollections, matchingskins) #returns only unused skins
        for i, type in enumerate(items_by_type):
            # print(f'num needed per collection{reqcollection[i]['skin_num']} num remaining {len(type)}')
            # print()
            if reqcollections[i]['skin_num'] > len(type):
                return False
        return True

    reqcollections = get_reqcollections(tradeup)
    all_skins_in_tradeup = get_allskinsintradeup(tradeup)
    groups = []
    while remainingskins(reqcollections, all_skins_in_tradeup):
        items_by_type = get_items_by_type(reqcollections, all_skins_in_tradeup)
        all_groups = Get_all_group_combos(items_by_type, reqcollections)

        # for i, group in enumerate(all_groups):
        #     print(f'group {i}: \n {group}')
        a_group, error = find_a_group(all_groups, targetfloat, maxiterations)
        #print(f'test error: {error}')
        if a_group:
            groups.append(a_group) # after finding the first one it takes forever to find the second one becuase the items were used. we need to filter out the used ones. I think there will be a methods based upon how combinations are sorted. 
        # print(f'\n group: \n {a_group}')
        if error:
            break
    return groups, error


def trade_viabililty(tradeup): 
    #this function ensures that the tradeup made in tradeups are viable to complete. 
    for case in tradeup['cases']:
        amountofunusedskins= len([skin for skin in case['skin_loc'] if skin['used']==False])
        #print(f'tradeupid: {tradeup['tradeupid']} amount of unused skins: {amountofunusedskins}')
        if not case['skin_loc']: #does it have any skins
            #print('here')
            return False
        #print(case['collection_name'])
        if amountofunusedskins < case['skin_num']: #does it have enough skins left to use
            return False
    return True

def groups_to_tradeup(all_groups, tradeup):
    for idx, group in enumerate(all_groups):
       trade_entry = {
            'tradeid': idx,
            'trade_av_float': calc_av_group_float(group),
            'skins': group
        }
       tradeup['trades']=[trade_entry]
    
def update_used_tag(tradeups, tradeup):
    all_skins = get_allskinsintradeup(tradeup)
    for tradeup1 in tradeups:
        for case in tradeup1['cases']:
            if 'skin_loc' in case:
                for skin in case['skin_loc']:
                    for updatedskin in all_skins:
                        if skin['loc'] == updatedskin['loc']:
                            skin['used'] = updatedskin['used']

def get_button_array(tradeups, inventory):
    
    ''' 
    this function outputs the positions of the items when they need to be traded up
        Considers changes to location due:
            - previous trades
            - tier of trade 
            - stattrak 
    '''

    def get_firstintradebutton(trade, inventory):
        to_del = []
        for idx, skin in enumerate(inventory['descriptions']):
            if trade['skins'][0]['float'] == skin['iteminfo']['floatvalue']:
                to_del.append(idx)
                break
        for i in reversed(to_del):
            del inventory['descriptions'][i]
            del inventory['assets'][i]
    
        return idx
    
    def sort_statrakntype(trade, inventory, tradeup):
        #delete all the things that are not the right type.
        pass
    
    def button_finder(trade, inventory, tradeup):
        #this function will return the a list of new positions of the skins in trade after the other tiers and skins are removed from the function
        to_del=[]
        buttons=[] 
        for idx, skin in enumerate(inventory['descriptions']):
            for tradeskin in trade['skins'][1:]:
                if tradeskin['float'] == skin['iteminfo']['floatvalue']:
                    to_del.append(idx)
                    continue
        
        for i in reversed(to_del):
            del inventory['descriptions'][i]
            del inventory['assets'][i]

        for x, pos in enumerate(to_del):
            newpos = pos - x
            buttons.append(newpos)

        return buttons
    
    def updateinventorycopy(trade, inventory2):
        to_del = []
        for idx, skin in enumerate(inventory2['descriptions']):
                for tradeskin in trade['skins']:
                    if tradeskin['float'] == skin['iteminfo']['floatvalue']:
                        to_del.append(idx)
                        continue
        
        for i in reversed(to_del):
            del inventory2['descriptions'][i]
            del inventory2['assets'][i]
        



    inventory2 = inventory.copy()
    buttonorder = []
    new_item = {'your_key': 'your_value'}
    for tradeup in tradeups:
        for trade in tradeup['trades']:
            trade['skins'].sort(key=lambda skin: skin['loc']) #sorts smallest to largest based on loc
            copied_inv = inventory2.copy()
            firstitembutton = get_firstintradebutton(trade, inventory)
            buttonorder.append(firstitembutton)
            sort_statrakntype(trade, copied_inv, tradeup)
            buttons = button_finder(trade, copied_inv, tradeup)
            buttonorder.append(buttons)
            updateinventorycopy(trade, inventory2)
    
    return buttonorder



#these are the main functions:
def setupinv(inventory, steamID):
    setupdesc(inventory)
    deletenonweaponskins(inventory)
    addfloatinfo(inventory, steamID)  #Pings API to append float info to each skin
   
def determinetradeups(tradeups, inventory):
    #calculate_max_tradeups(tradeups)    #not actually needed lol
    #loc_of_skins(inventory, tradeups)   #passes the location of each skin in the inventory to each type of tradeup
    for tradeup in tradeups:
        if trade_viabililty(tradeup):
            all_groups, error = findgroups(tradeup, tradeup['average_float'])         #makes the average of the sum of the skins atleast equal to the minimum. We should change this so that this is calculated each time we determine a tradeup. Because at the moment, a bunch of skins might be labelled unused and not be able to be used in future types of tradeups
            if error:
                print(f'tradeupid:{tradeup['tradeupid']} error msg: {error}')
                continue
            groups_to_tradeup(all_groups, tradeup)  #moves new groups to appropriate tradeuo
            update_used_tag(tradeups, tradeup) #ensured that all the skins across every tradeup are counted as used if put into a group.
        else:
            pass
            #need to lablel nonviable trades as non viable. 

        

    

def main():

       # URL of the steaminv JSON endpoint
    url = 'https://steamcommunity.com/inventory/76561198039620934/730/2' 
    api_key= '19488106D7EDE1FBAE0169ABA1604C39'
    csfloat_key = 'Dl63vjtpRDu-tU38erAuI-JfiMI760Yl'
    steamID = '76561198039620934'
    logs = ''
    # response = requests.get(url)
    # inventory = response.json() #things that appear in the desc that we will need to filter for: Base Grade Graffiti ,Extraordinary Collectible, Service Medal, High Grade Music Kit, Exceptional Agent, Distinguished Agent,Base Grade Tool, Base Grade Container

    inventory= load_json('logs', 'myinventoryaftersetupinv.json')
    tradeups= load_json('logs', 'tradeupsafterlocofskins.json')
    
    #loc_of_skins(inventory, tradeups)
    determinetradeups(tradeups, inventory)
    buttonarray = get_button_array(tradeups, inventory)
    print(buttonarray)

    save_json(tradeups, 'logs', 'tradeupsaftergrouping.json')
   

if __name__ == "__main__":
    main()
    None

# command to launch API: node index.js
# http://127.0.0.1:80/?url=steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198039620934A35244263600D12415877210425859785

#differences in items in assets and descriptions
    #I think that the onles iwth the same classid only appear once in the descriptions 
    # class id changes when a sticker is on a skin which we can't control 
