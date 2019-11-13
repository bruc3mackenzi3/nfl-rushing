import json

'''
Fields data may be sorted by:
    Yds - Total Rushing Yards
    Lng - Longest Rush
    TD - Total Rushing Touchdowns

Fields data may be filtered on:
    Player
'''

class RushingData:
    def __init__(self):
        self.data = None
        self.data_yds = None
        self.data_lng = None
        self.data_td = None

        self.fields = [
            ('Player',),
            ('Team',),
            ('Pos',   'Position'),
            ('Att/G', 'Rushing Attempts Per Game Average'),
            ('Att',   'Rushing Attempts'),
            ('Yds',   'Total Rushing Yards'),
            ('Avg',   'Rushing Average Yards Per Attempt'),
            ('Yds/G', 'Rushing Yards Per Game'),
            ('TD',    'Total Rushing Touchdowns'),
            ('Lng',   'Longest Rush'),
            ('1st',   'Rushing First Downs'),
            ('1st%',  'Rushing First Downs Percentage'),
            ('20+',   'Rushing 20+ Yards Each'),
            ('40+',   'Rushing 40+ Yards Each'),
            ('FUM',   'Rushing Fumbles')
        ]

        self._filename = 'rushing.json'

        self.load_data()

    def load_data(self):
        with open(self._filename) as f:
            rushing_file = f.read()
        try:
            self.data = json.loads(rushing_file)
        except json.JSONDecodeError as e:
            print('Unable to load rushing.json due to invalid JSON. ' + str(e))
        
        self._clean_data()

        self._precache_sorted_data()
    
    def to_csv(self, dataset_name, name_filter=None):
        ''' Convert one of the datasets to a CSV with optional Player name
        filtering.
        '''

        dataset = self.get_dataset(dataset_name)

        # Pythonic one-liner to build the header list using the short form field
        # names
        csv_data = '\t'.join(list(map(lambda x: x[0], self.fields)))

        for record in dataset:
            # Filter feature - skip if the filter's set and there's no match
            if name_filter and not name_filter.lower() in record['Player'].lower():
                continue

            record_csv = '\n'
            for field in self.fields:
                record_csv += str(record[field[0]]) + '\t'
            csv_data += record_csv.rstrip('\t')

        return csv_data

    def get_dataset(self, dataset_name):
        '''Helper function to retrieve the appropriate dataset based on the
        corresponding name.
        
        To reflect the behaviour in the front-end a no match simply returns the
        original dataset.
        '''

        if dataset_name == 'total_rushing_yards':
            return self.data_yds
        elif dataset_name == 'longest_rush':
            return self.data_lng
        elif dataset_name == 'total_rushing_touchdowns':
            return self.data_td
        # Base case if sortBy is set to none, missing, or anything erroneous
        else:
            return self.data

    # Private helper function to clean data as it's loaded
    # Known issues with data include ints set as strings e.g. "Yds":"1,043"
    def _clean_data(self):
        for d in self.data:
            # Copy fields to preserve original data, then we can work off the
            # parsed integer for sorting but keep it hidden by displaying the
            # original data

            for field in ['Yds', 'Lng', 'TD']:
                if type(d[field]) == str:
                    d[field + '_int'] = int(d[field].replace(',', '').replace('T', ''))
                else:
                    d[field + '_int'] = d[field]

    def _precache_sorted_data(self):
        self.data_yds = sorted(self.data, key=lambda d: d['Yds_int'], reverse=True)

        self.data_lng = sorted(self.data, key=lambda d: d['Lng_int'], reverse=True)

        self.data_td = sorted(self.data, key=lambda d: d['TD_int'], reverse=True)
