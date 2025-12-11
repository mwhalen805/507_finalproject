import pandas
import requests
import comtradeapicall


subscription_key = '31a1bf3b6fb0436ca3e7ce4fc9d0883b'
# commented for safety to prevent running again 
# directory = '/Desktop/SI 507/Final Project'


## DO NOT RUN THIS AGAIN 
## 126 files downloaded 11/10/25
comtradeapicall.bulkDownloadFinalFile(
    subscription_key=subscription_key,
    directory=directory,
    typeCode='C',       # Commodity trade
    freqCode='A',       # Annual
    clCode='HS',        # HS classification
    period='2024',      # Year of interest
    reporterCode=None,  # All countries
    decompress=True     # Automatically extract ZIP files
)

df = comtradeapicall.getFinalData(subscription_key, typeCode='C',freqCode='A', 
                                  clCode='HS', period='2024', reporterCode=None, 
                                  cmdCode=None, flowCode='M', 
                                  partnerCode=None, partner2Code=None, customsCode=None, motCode=None, 
                                  maxRecords=250000, format_output='JSON', includeDesc=True)



print(df.head())
print(len(df), "records retrieved")

