# Anakin-assignment

* This assignment is to fetch and give the latitudes and longitudes of all the restaurants on [this](https://food.grab.com/sg/en/) page. <br>
* For this I used a python package called [selenium-wire](https://github.com/wkeeling/selenium-wire#response-objects) that extends Selenium's Python bindings to give you access to the underlying requests made by the browser. You author your code in the same way as you do with Selenium, but you get extra APIs for inspecting requests and responses and making changes to them on the fly.

To run the code: <br>
1. clone the repo
2. run `pip install -r requirements.txt`
3. run the python script `python script.py`

Find the extracted coordinates [here](https://github.com/blaze-fire/Anakin-assignment/blob/main/restaurants.json).

Here is the exact [code](https://github.com/blaze-fire/Anakin-assignment/blob/main/script.py)

## Logic:

* As mentioned in the assignment we have to load more restaurants in page by keep clicking load more button.
* So first find the load more element and keep clicking it with some delay in order to load the page.
* For every time you click the load more button, in networks tab of chrome developers tool you can observe a **post** request being made to the url `https://portal.grab.com/foodweb/v2/search`, which contains all kinds of information regarding the restaurants.
* We are only interested in coordinates so we first filter the responses and then get the required data, which is in bytes and decode the data and format it as json.
* Then we get the required fields from the response and save it in an array and then save all the unique rstaurants in a json file.  