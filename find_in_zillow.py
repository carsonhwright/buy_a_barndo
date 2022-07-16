import json

from driver_setup import Driver_Setup

def main():
    with open("zillow_search_urls.json", 'r') as json_read:
        counties = json.load(json_read)
    
    
    for county in counties:
        if county == "Actual Target Follow-on {}":
            not_500_error = True
            url_index = 2
            hard_coded_stop = 5
            # HARDCODED: Very inconsistent behavior beyond what I can get from pre-knowledge of index limit
            # for desired region, will need to programmatically extract max index number from initial
            # page
            while url_index < hard_coded_stop:
                temp_url = counties[county].format(str(url_index), str(url_index))
                html_source = driver_setup_func_formatted(temp_url)
                try:
                    not_500_error = get_not_html500_error(html_source)
                    with open(f'output/{county.format(str(url_index))}.html', 'w', encoding='utf-8') as g:
                        g.write(html_source)
                except AssertionError:
                    not_500_error = False
                
                url_index += 1
        else:
            html_source = driver_setup_func(counties[county])
            with open(f'output/{county}.html', 'w', encoding='utf-8') as g:
                g.write(html_source)

def driver_setup_func(url):
    zillow_driver = Driver_Setup()
    zillow_driver.init_driver()
    zillow_driver.search_zillow(url)
    html_source = zillow_driver.driver.page_source
    zillow_driver.driver.quit()
    return html_source

def driver_setup_func_formatted(url):
    zillow_driver = Driver_Setup()
    zillow_driver.init_driver()
    zillow_driver.search_zillow(url)
    html_source = zillow_driver.driver.page_source
    zillow_driver.driver.quit()
    return html_source
    
def get_not_html500_error(html_source):
    assert 'Error 500' not in html_source
    return True