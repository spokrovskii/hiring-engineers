from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}

initialize(**options)

title = 'Data Visualization'
widgets = [{
    'definition': {
        'type': 'timeseries',
        'requests': [
            {'q': 'my_metric{*} by {host}'}
        ],
        'title': 'My Custom Metric'
    }},
    {
    'definition': {
        'type': 'timeseries',
        'requests': [
            {'q': "anomalies(avg:mysql.performance.cpu_time{host:vagrant}, 'basic', 2)"},
        ],
        'title': 'MySQLS Metric w/Anomaly'
    }},
    {
    'definition': {
        'type': 'timeseries',
        'requests': [
            {'q': "my_metric{*}.rollup(sum, 3600)"}
        ],
        'title': 'All the Points for the Past Hour Summed Up With a Roll Up function'
    }}
]

layout_type = 'ordered'
description = 'A timeboard with memory info.'
is_read_only = True
notify_list = ['serge.pokrovskii@gmail.com']
template_variables = [{
    'name': 'host1',
    'prefix': 'host',
    'default': 'my-host'
}]

api.Dashboard.create(title=title,
                     widgets=widgets,
                     layout_type=layout_type,
                     description=description,
                     is_read_only=is_read_only,
                     notify_list=notify_list,
                     template_variables=template_variables)