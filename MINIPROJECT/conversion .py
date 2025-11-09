print("TEMPERATURE CONVERTION")


print("CONVERT FROM CELSIUS TO FAHRENHEIT, KELVIN, REAMUR, RANKINE")


celsius=int(input("enter celsius:"))

celciustofahrenheit=((celsius*9/5)+32)

celsiustokelvin=(celsius+273.15)

celsiustoreaumur=(celsius*4/5)

celsiustorankine=(celsius+273.15)*9/5


print(f"fahrenheit={celciustofahrenheit}")

print(f"kelvin={celsiustokelvin}")

print(f"reamur={celsiustoreaumur}")

print(f"rankine={celsiustorankine}")



print("CONVERT FROM FAHRENHEIT TO CELSIUS, KELVIN, REAMUR, RANKINE")


fahrenheit=int(input("enter a farenheit:"))

fahrenheittocelsius=((fahrenheit-32)*5/9)

fahrenheittokelvin=((fahrenheit-32)*5/9+273.15)

fahrenheittoreamur=((fahrenheit-32)*4/9)

fahrenheittorankine=((fahrenheit-32)*5/9+273.15)

print(f"celsius ={fahrenheittocelsius}")

print(f"kelvin ={fahrenheittokelvin}")

print(f"reamur ={fahrenheittoreamur}")

print(f"rankine ={fahrenheittorankine}")



print("CONVERT FROM KELVIN TO CELSIUS, FAHRENHEIT, REAMUR, RANKINE")


kelvin=int(input("enter a kelvin:"))

kelvintocelsius=(kelvin-273.15)

kelvintofahrenheit=((kelvin-273.15)*9/5+32)

kelvintoreamur=((kelvin-273.15)*4/5)

kelvintorankine=(kelvin*9/5)

print(f"celsius ={kelvintocelsius}")

print(f"farenheit ={kelvintofahrenheit}")

print(f"reamur ={kelvintoreamur}")

print(f"rankine ={kelvintorankine}")


