import pandas
import json

with open('pr.json') as file:
    raw_pull_requests = json.load(file)

sorted_pull_requests = []

for item in raw_pull_requests:
    if item['state'] == 'MERGED':
        sorted_pull_requests.append(item)
    else:
        pass


pr_data_frame = pandas.DataFrame(sorted_pull_requests)

pr_data_frame = pr_data_frame['closedDate'].astype('datetime64')

histogram = pr_data_frame.groupby(pr_data_frame.dt.isocalendar().week)

histogram = histogram.count().plot(kind='bar',
                                   figsize=(16, 9),
                                   xlabel='Week',
                                   ylabel='Pull requests')

for column in histogram.patches:
    histogram.annotate(str(column.get_height()),
                       (column.get_x() + 0.05, column.get_height() + 0.5)
                       )

figure = histogram.get_figure()

figure.savefig('histogram.png', dpi=300)
