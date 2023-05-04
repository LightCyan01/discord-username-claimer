# Discord Username Claimer
This is a Python script that claims your desired username on Discord.

## Requirements
* Python 3.x
* `requests` module
* `colorama` module

You can install the `requests` and `colorama` modules by running the following command:
```
pip install -r requirements.txt
```

## Usage
1. Clone the repository and navigate to the directory:

   ```
   git clone https://github.com/your-username/discord-username-claimer.git
   cd discord-username-claimer
   ```
 
2. Open ```claimer.py``` and enter your desired ```username``` and your ```auth token```.
3. Leave it on until you have successfully claimed your username.

## Status Codes
1. ```200 - Success```
2. ```429 - Too Many Attempts (Rate Limited)```
3. ```401 - Unauthorized (You are not yet eligible)```
4. ```400 - Username Taken```

## Disclaimer
This script is for educational purposes only. Use it at your own risk. The author is not responsible for any consequences that may result from using this script.
