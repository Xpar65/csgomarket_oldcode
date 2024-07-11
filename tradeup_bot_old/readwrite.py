import json

def load_json(folder_name, file_name):
    #file_path = f'Unittestfiles/mock_data/{folder_name}/{file_name}'
    file_path = f'C:/Users/liamc/Desktop/Folders/Projects/CSGO/csgomarket/csgomarket/tradeup_bot/Unittestfiles/mock_data/{folder_name}/{file_name}'
    with open(file_path, 'r') as file:
        return json.load(file)
    
def write_json(folder_name, file_name, data):
    file_path = f'C:/Users/liamc/Desktop/Folders/Projects/CSGO/csgomarket/csgomarket/tradeup_bot/Unittestfiles/mock_data/{folder_name}/{file_name}'
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

tradeup0 = [
            {
            'tradeid': 0,
            'tier': 'Restricted',                     
            'average_float': 0.14,  
            'ST,SV': 'Normal' ,               
            'cases': [
                {'collection_name': 'The Shadow Collection', 'wear': 'Minimal Wear', 'skin_num': 4}, 
                {'collection_name': 'The Chroma Collection', 'wear': 'Factory New','skin_num': 6},
                ],
            }
        ]
tradeup0_expected = [
    {
        'tradeid': 0, 
        'tier': 'Mil-Spec Grade',
        'average_float': 0.14,
        'ST,SV': 'Normal',
        'cases': [
            {
                'collection_name': 'The Shadow Collection',
                'wear': 'Minimal Wear',
                'skin_num': 6,
                'skin_loc': [
                        {'loc': 1, 'float': 0.10709764063358},
                        {'loc': 2, 'float': 0.11341650784016},
                        {'loc': 3, 'float': 0.14190302789211},
                        {'loc': 4, 'float': 0.12195196002722},
                        {'loc': 5, 'float': 0.12470516562462},
                        {'loc': 6, 'float': 0.13292105495930},
                        {'loc': 11, 'float': 0.13507166504860},
                            ],
                'inventory_count': 7,
            },
            {
                'collection_name': 'The Chroma Collection',
                'wear': 'Factory New',
                'skin_num': 4,
                'skin_loc': [
                        {'loc': 0, 'float': 0.05306274443865},
                        {'loc': 7, 'float': 0.05306274443865},
                        {'loc': 8, 'float': 0.05696008354425},
                        {'loc': 9, 'float': 0.05151280760765},
                        {'loc': 10, 'float': 0.06613752245903},
                ],
                'inventory_count': 4,
            }
        ],
    }
]
        

tradeup1 = [ 
            {
            'tradeid': 0,
            'tier': 'Mil-Spec',                      #covert 6 Restricted 5 .... # check what the csfloat inspect api uses. 
            'average_float': 0.3,  #  desired float (actual av comes out like 0.2999 with my calc)
            'ST,SV': 'ST' ,               # 0: normal, 1: ST 2: SV StatTrakâ„¢
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
                {'collection_name': 'The Gamma 2 Collection', 'wear': 'Field-Tested','skin_num': 1},    #P90 | Grim (has nametag)
                ],
            },
        ]

tradeup1_expected = [ 
    {
        'tradeid': 0,
        'tier': 'Mil-Spec',                      # covert 6 Restricted 5 .... # check what the csfloat inspect api uses. 
        'average_float': 0.3,  # desired float (actual av comes out like 0.2999 with my calc)
        'ST,SV': 'ST',               # 0: normal, 1: ST 2: SV StatTrakâ„¢
        'cases': [
            {
                'collection_name': 'The Shadow Collection', 
                'wear': 'Minimal Wear', 
                'skin_num': 1,
                'skin_loc': [ {'loc': 41, 'float': 0.14152178168297},]  # Empty list as required
            },    # stattrak scar 20
            {
                'collection_name': 'The Chroma 2 Collection', 
                'wear': 'Field-Tested',
                'skin_num': 1,
                'skin_loc': [{'loc': 40, 'float': 0.23431506752968},]  # Empty list as required
            },   # p250 valence
            {
                'collection_name': 'The Breakout Collection', 
                'wear': 'Well-Worn',
                'skin_num': 1,
                'skin_loc': [{'loc': 39, 'float': 0.39802956581116},]  # Empty list as required
            },      # ssg abyss
            {
                'collection_name': 'The Chroma 2 Collection', 
                'wear': 'Factory New',
                'skin_num': 1,
                'skin_loc': [{'loc': 38, 'float': 0.06373395025730},]  # Empty list as required
            },    # MP7 | Armor Core
            {
                'collection_name': 'The Gamma Collection', 
                'wear': 'Factory New',
                'skin_num': 1,
                'skin_loc': [{'loc': 37, 'float': 0.20614235103130},]  # Empty list as required
            },       # Nova | Exo
            {
                'collection_name': 'The Phoenix Collection', 
                'wear': 'Well-Worn',
                'skin_num': 1,
                'skin_loc': [{'loc': 36, 'float': 0.38057276606560},]  # Empty list as required
            },       # Negev | Terrain
            {
                'collection_name': 'The Glove Collection', 
                'wear': 'Well-Worn',
                'skin_num': 1,
                'skin_loc': [{'loc': 35, 'float': 0.43253821134567},]  # Empty list as required
            },         # Galil AR | Black Sand
            {
                'collection_name': 'The Phoenix Collection', 
                'wear': 'Field-Tested',
                'skin_num': 1,
                'skin_loc': [{'loc': 34, 'float': 0.26366665959358},]  # Empty list as required
            },    # Tec-9 | Sandstorm
            {
                'collection_name': 'The Gamma Collection', 
                'wear': 'Battle-Scarred',
                'skin_num': 1,
                'skin_loc': [{'loc': 33, 'float': 0.52928066253662},]  # Empty list as required
            },    # Five-SeveN | Scumbria
            {
                'collection_name': 'The Gamma 2 Collection', 
                'wear': 'Field-Tested',
                'skin_num': 1,
                'skin_loc': {'loc': 25, 'float': 0.34640833735466},  # Empty list as required
            },    # P90 | Grim (has nametag)
        ],
    },
]


write_json('loc_of_skins_files', 'tradeup0.json', tradeup0)
write_json('loc_of_skins_files', 'tradeup1.json', tradeup1)
write_json('loc_of_skins_files', 'tradeup0_expected.json', tradeup0_expected)
write_json('loc_of_skins_files', 'tradeup1_expected.json', tradeup1_expected)
