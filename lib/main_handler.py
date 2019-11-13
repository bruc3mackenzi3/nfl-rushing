import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def initialize(self, rushing_data):
        self.rushing_data = rushing_data

    def get(self):
        # Start by parsing arguments
        sort_by = self.get_argument('sortBy', 'none')
        print('DEBUG: sort: ' + sort_by)

        if sort_by == 'total_rushing_yards':
            data = self.rushing_data.data_yds
        elif sort_by == 'longest_rush':
            data = self.rushing_data.data_lng
        elif sort_by == 'total_rushing_touchdowns':
            data = self.rushing_data.data_td
        # Base case if sortBy is set to none, missing, or anything erroneous
        else:
            data = self.rushing_data.data

        self.render('table_template.html',
                    title='NFL Rushings',
                    rushing_fields=self.rushing_data.fields,
                    rushing_data=data)
