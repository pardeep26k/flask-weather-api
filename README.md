# flask-weather-api
This is Flask framwork Api to get shipment data and Weather report of shipment Pin Code

## How to setup project in Locall
1. Clone The Repo
2. Setup Flask if not locally by following steps > https://flask.palletsprojects.com/en/2.3.x/installation/
3. run the command to start flask in localhost from project dir

```$
 flask --app index run or Debug mode flask --app index run --debug
 * Serving Flask app 'index'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

4. http://127.0.0.1:5000 Application start running at this url.



## API Endpoint

There are two api Endpoints > 

Search shipment by carreer 
1. http://127.0.0.1:5000/shipment/carreer_name
2. http://127.0.0.1:5000/order/order_id

Some dummy shipment data saved in `data.txt` for testing purpose

## Weather Api

1. I used https://www.visualcrossing.com/ api to get weather information of particular shipment by pincode.
2. Every time we do a call to api, I save weather data to json file with two hours advance time in file with pincode name.
3. Next time if we recieve  request for same pincode, first I check in directory if pincode file exist and data is still valid for 2 hours we return data from file or not again do the call to api service.

   
# Testing 
  There are unit test cases for both classes in test directory and you can excecute by running command
  
   `python -m unittest discover -s test -p "*_test.py"` 
