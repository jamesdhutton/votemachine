import json
import redis

def connect():
	
	config = {}
	
	with open("config.json") as config_file:
		config = json.load(config_file)
	
	return redis.StrictRedis (host=config["host"],
		       port=config["port"],
		       db=0,
		       ssl=config["ssl"],
		       password=config["password"])
			   
			   
def get_choices():
	
	config = {}
	
	with open("config.json") as config_file:
		config = json.load(config_file)
		
		return config["choices"]
		
	

			   
			   
			   