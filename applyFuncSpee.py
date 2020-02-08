#vector vs. non vector operation speed!
import csv
import pandas



featureDf = pandas.read_csv("test_result.csv")
finalFeatureDf = featureDf
NameSwDown = 'swdown.nd.v.d03.raw'
NameCoszen = 'coszen.nd.v.d03.raw'
NameTemp = 't2.nd.v.d03.raw'
NameDerate = 'derate.calc.v.01.raw'

def coszenInv(x):
    if x>0.2:
        return 1/x
    else:
        return 0
    

def tempDerate(x):
    return (1-0.05*(x-293))


finalFeatureDf['invCoszen'] = finalFeatureDf[NameCoszen].apply(coszenInv)
finalFeatureDf['tempDerate'] = finalFeatureDf[NameTemp].apply(tempDerate)
finalFeatureDf[NameDerate] = finalFeatureDf['invCoszen']*finalFeatureDf[NameSwDown]*finalFeatureDf['tempDerate']


finalFeatureDf.to_csv("finalFeature_2.csv")

