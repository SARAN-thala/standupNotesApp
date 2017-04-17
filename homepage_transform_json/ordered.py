import json
import os
from collections import OrderedDict

base_path = '/Users/saranraj/digital-tw/tw.qa.content'
content_state = ['draft', 'public']
relative_path = 'homepage/home_page.json'
relative_path_new = 'homepage/home_page_editable.json'
locales = ['cn', 'de', 'en', 'es', 'pt']

def migrate():
    for state in content_state:
        for locale in locales:
            with open(os.path.join(base_path, state, locale, relative_path)) as data_file:
                created_data = OrderedDict()
                data = json.load(data_file)
                created_data['metatags'] = create_metadata()
                created_data['uber_title'] = migrate_uber_title(data['uber_title'], data['uber_subtitle'])
                photo_card = migrate_photo_cards(data['photo_cards'])
                video = migrate_video(data['feature_block'])
                created_data['modules'] = [photo_card, video]
                create_migrated_json(os.path.join(base_path, state, locale, relative_path_new), created_data)

def create_metadata():
    return  {
            'title': 'ThoughtWorks | Creative technology consultants',
            'description': "We're a global technology consultancy. We help you invent what's next, and bring it to life with technology. In weeks, not years.",
            'keywords': "",
            'social_title': "ThoughtWorks | Creative technology consultants",
            'social_description': "ThoughtWorks is a global technology consultancy. We help you invent what's next, and bring it to life with technology. In weeks, not years.",
            'image': "https://dynamic.webteam.thoughtworks.com/homepage/social_image-fddb59ff7d1003cb5c58a951b94618bb.jpeg"
            }

def migrate_uber_title(title, subtitle):
    my_data = {}
    my_data['uber_title'] =  {'title': title, 'subtitle': subtitle }
    return my_data

def migrate_photo_cards(data):
    return {
                'type' : 'photo_card_grid',
                'data' : { 'photo_cards' : data }
            }

def migrate_video(data):
    return {
             'type' : 'video_content_editable',
             'data' : { "title": data['title'],
                        "description": data['lead'],
                        "wistia_id": data['video_id'],
                        "tencent_id": data['tencent_id'],
                        "background_color": data['background_color'],
                        "cta": {
                            "button_text": data['call_to_action'],
                            "button_color": "black",
                            "url_link": data['link'],
                            "tooltip": ""
                            },
                        "padding_toggle_top": True,
                        "padding_toggle_bottom": True
                    }
                }

def create_migrated_json(full_path_to_file, data):
    print data
    json_data = json.dumps(data, ensure_ascii= False).encode('utf8')
    with open(full_path_to_file, 'w+') as f:
        f.write(json_data)

if __name__ == "__main__":
    migrate()
