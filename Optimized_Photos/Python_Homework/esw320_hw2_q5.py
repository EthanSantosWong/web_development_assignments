johnday = int(input("How may days has John worked?"))
johnhour = int(input("How may hours has John worked?"))
johnmin = int(input("How may minutes has John worked?"))
billday = int(input("How may days has Bill worked?"))
billhour = int(input("How may hours has Bill worked?"))
billmin = int(input("How may minutes has Bill worked?"))

cdays = johnday + billday
chours = johnhour + billhour
cmin = johnmin + billmin

# calc days

tmin = cmin // 60
leftmin = cmin % 60

mhours = tmin + chours

thours = mhours//24
lefthours = mhours % 24

mdays = thours + cdays


# if thours > 1 add back into tday

# work = days + hours + minutes
print("Both John and Bill has worked a total of:", mdays, "days,", lefthours, "hours and", leftmin, "minutes.")
