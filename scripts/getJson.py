import sys,json

#workspace=sys.argv[1]
#Read Json file and load it into a variable
with open('testchannels.json','r') as f:
  getChannels = json.load(f)
  
print getChannels['parentname']
print getChannels['childchannels']['childchannel1']
