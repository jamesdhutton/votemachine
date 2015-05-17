#Vote Machine

This project demonstrates how to connect a Raspberry Pi to the cloud.
It turns your Raspberry Pi into an electronic voting booth. 
You decide what choices are on the ballot, then set up one or
more Raspberry Pis to act as voting booths. The Pis send the 
votes to a central Redis Cache in the cloud, which you can create
using Azure or other cloud providers. 

##Installation:

Get pip if you don't already have it:
```
sudo curl https://bootstrap.pypa.io/get-pip.py | sudo python
```

Install redis:
```
sudo pip install redis
```

Install matplotlib. On a Raspberry Pi, use apt-get rather than pip:

```
sudo apt-get install python-matplotlib
```

##Configuration:

Start by configuring a Redis Cache using Azure or your favourite cloud provider.
Then, on each Raspberry Pi you want to use as a voting booth:

1. Edit `host` and `password` entries in `config.json` so that they point to your server
2. Edit the `choices` entry to contain the choices you want on the ballot

##Running an election

Initialize the election (do this only once):

```
python initelection.py
```

Start a voting booth:
```
python initelection.py
```

Get results:
```
python results.py
```