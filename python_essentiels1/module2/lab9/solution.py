hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here

## First solution
endhour = hour + dura // 60
endminute = mins + dura % 60

endhour = endhour + endminute // 60

endhour = endhour % 24 
endminute = endminute % 60

print(endhour,":",endminute)

## Second solution 
endhour = hour + dura // 60
endminute = mins + dura % 60

if endhour > 24 / 
	endhour = endhour + endminute // 60

if endminute > 60 :
	endhour = endhour % 24 
	endminute = endminute % 60

print(endhour,":",endminute)
