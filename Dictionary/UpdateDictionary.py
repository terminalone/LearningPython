AppleProductPrices={"IPhone":1000,"Imac":2000,"AirPods":2000}
new_prices={"IPhone":2000,"Imac":3000,"AirPods":5000,"iphone se":250}

AppleProductPrices.update(new_prices)
print(AppleProductPrices)

a=AppleProductPrices.pop("IPhone")#Removes IPhone
print(a)
print(AppleProductPrices)

print(AppleProductPrices.values()) #print values in dict
print(AppleProductPrices.keys())
print(AppleProductPrices.items())