#read config file all lines

import yaml

with open('deployment_cfg.yml', 'r') as cfgFile:
    deploy_cfg = yaml.load(cfgFile)

#print deploy_cfg['Connection']['Weather']

weather_dmz_host = deploy_cfg['Connection']['Weather'].split(',')[0]
weather_dmz_port = deploy_cfg['Connection']['Weather'].split(',')[1]

print weather_dmz_host
print weather_dmz_port


feature_list = deploy_cfg['Parameters']['WeatherFeatures']

print feature_list

for key in feature_list:
    print key
    print feature_list[key]

print feature_list.keys()
print feature_list.values()

assetId = 303939
target = deploy_cfg['Parameters']['Measurement']
CDMflag = str(deploy_cfg['Parameters']['CDMflag']).upper()
if CDMflag =='FALSE':
    sptAGID = deploy_cfg['FarmGeography'][int(assetId)].split(',')[0]
    ycap = float(deploy_cfg['FarmGeography'][int(assetId)].split(',')[1])


print target," ",CDMflag," ",sptAGID," ",ycap
print deploy_cfg['Parameters']['WeatherFeatures']['COSZN']
