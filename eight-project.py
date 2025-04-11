# #   https://v6.exchangerate-api.com/v6/bef227b06198dd1a63079b97/latest/USD


# import requests

# url="https://v6.exchangerate-api.com/v6/bef227b06198dd1a63079b97/latest/USD"

# response=requests.get(url).json()
# conv_rate=response["conversion_rates"]

# for i in conv_rate:
#     print(i)
# # print(x)
# # print(response)


import requests

apiKey="bef227b06198dd1a63079b97"
base_url=f"https://v6.exchangerate-api.com/v6/{apiKey}/latest/"

def converter(amount,base,target):
    url=base_url+base
    response=requests.get(url).json()
    
    conv_rate=response["conversion_rates"]

    if target in conv_rate:
        converted_Amount=amount*conv_rate[target]
        print(converted_Amount)

base=input("Enter From Currency : ")
target=input("Enter To Currency : ")
amount=int(input("Enter Amount : "))

converter(amount,base,target)