import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def initialize(self, rushing_data):
        self.rushing_data = rushing_data

    def get(self):
        # Start by parsing arguments
        sort_by = self.get_argument('sortBy', 'none')
        filter_by = self.get_argument('filterBy', '')
        export = self.get_argument('export', '')
        print('DEBUG: sortBy: {} filterBy: {} export: {}'.format(sort_by, filter_by, export))

        # Select appropriately sorted dataset
        data = self.rushing_data.get_dataset(sort_by)

        if export == 'on':
            self.export_csv(sort_by, filter_by)
        else:
            self.render('table_template.html',
                        rushing_fields=self.rushing_data.fields,
                        sort_by=sort_by,
                        name_filter=filter_by,
                        rushing_data=data)

    def export_csv(self, sort_by, filter_by):
        self.set_header('Content-Type','text/csv')
        self.set_header('content-Disposition','attachment; filename=rushing.csv')
        self.write(self.rushing_data.to_csv(sort_by, filter_by))
