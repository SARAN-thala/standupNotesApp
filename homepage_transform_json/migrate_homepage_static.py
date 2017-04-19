import json
import os
from collections import OrderedDict

base_path = '/Users/saranraj/digital-tw/tw.prod.content'
content_state = ['draft', 'public']
relative_path = 'homepage/home_page.json'
relative_path_new = 'homepage/home_page_static.json'
locales = ['cn','de','en','es','pt']

def migrate():
    for state in content_state:
        for locale in locales:
            with open(os.path.join(base_path, state, locale, relative_path)) as data_file:
                data = json.load(data_file)
                created_data = create_static_data(data)
                create_transformed_json(os.path.join(base_path, state, locale, relative_path_new), created_data)

def create_static_data(data):
    created_data = OrderedDict([('page_header_title',data['page_header_title']),
                                ('insights_section_title',data['insights_section_title']),
                                ('read_more', data['read_more']),
                                ('latest_news', data['latest_news']),
                                ('more_news', data['more_news'])])
    # created_data('page_header_title', data['page_header_title'])
    # created_data['insights_section_title']= data['insights_section_title'],
    # created_data['read_more']= data['read_more'],
    # created_data['latest_news']= data['latest_news'],
    # created_data['more_news']= data['more_news']
    # created_data = {
    #                     'page_header_title': data['page_header_title'],
    #                     'insights_section_title': data['insights_section_title'],
    #                     'read_more': data['read_more'],
    #                     'latest_news': data['latest_news'],
    #                     'more_news': data['more_news']
    #                 }
    return created_data

def create_transformed_json(full_path_to_file, data):
    json_data = json.dumps(data, ensure_ascii= False).encode('utf8')
    print full_path_to_file
    with open(full_path_to_file, 'w+') as f:
        f.write(json_data)

if __name__ == "__main__":
    migrate()
