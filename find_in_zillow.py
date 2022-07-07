import json

from driver_setup import Driver_Setup

def main():
    with open("zillow_search_urls.json", 'r') as json_read:
        counties = json.load(json_read)
    
    
    for county in counties:
        try:
            zillow_driver = Driver_Setup()
            zillow_driver.init_driver()
            zillow_driver.search_zillow(counties[county])
            html_source = zillow_driver.driver.page_source
            with open(f'output/{county}.html', 'w', encoding='utf-8') as g:
                g.write(html_source)
            zillow_driver.driver.quit()
        except:
            zillow_driver.driver.quit()