import json;
import urllib;

stationList = "http://appservices.citibikenyc.com/v1/station/list";
stationUpdates = "http://appservices.citibikenyc.com/v1/station/updates";

response = urllib.urlopen(stationList);
data = json.loads(response.reads());
print data.items()
