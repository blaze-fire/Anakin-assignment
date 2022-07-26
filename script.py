import json
from time import sleep
from seleniumwire import webdriver
from seleniumwire.utils import decode

driver = webdriver.Chrome(executable_path="./chromedriver")

# url launch
url = "https://food.grab.com/ph/en/restaurants"
driver.get(url)

# to store all the names and coordinates of restaurants
arr = []

while True:
    try:
        driver.implicitly_wait(5)

        # to find load more button and click
        button = driver.find_elements(
            by="xpath", value="//button[@class='ant-btn ant-btn-block']")
        button[0].click()
        sleep(10)
        driver.implicitly_wait(5)

        # to get specific responses which contains the required fields
        for request in driver.requests:
            if request.response and request.url.startswith("https://portal.grab.com/foodweb/v2/search"):
                response = request.response

                # the response is in bytes and have to manually decode
                body = decode(response.body, response.headers.get(
                    'Content-Encoding', 'identity'))

                # decode response as json
                decoded_body = body.decode('utf-8')
                json_data = json.loads(decoded_body)

                # get required name and cordinates and save in a list
                for result in json_data['searchResult']['searchMerchants']:
                    data = {'name': result['address']['name'],
                            'coordinates': result['latlng']}
                    arr.append(data)

    except:

        # when all entries stored than save only unique entries
        with open("restaurants.json", "w+") as json_file:
            res = []
            [res.append(x) for x in arr if x not in res]
            json.dump(res, json_file)
        driver.quit()
        break
