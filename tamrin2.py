class Time:
    def __init__(self , hour , minute , seconds):
        self.hour = hour
        self.minute = minute
        self.seconds = seconds

    def sum_time(self , guest):
        result = Time(None , None , None)
        result.hour = self.hour + guest.hour
        result.minute = self.minute + guest.minute
        result.seconds = self.seconds + guest.seconds
        return result

    def sub_time(self , guest):
        result = Time(None , None , None)
        result.hour = self.hour - guest.hour
        result.minute = self.minute - guest.minute
        result.seconds = self.seconds - guest.seconds
        return result

    def second_to_time(self):
        self.hour = second / 3600
        self.minute = (second % 3600) / 60
        self.seconds = (second % 3600) % 60

    def time_to_second(self):
        second = self.hour * 3600 + self.minute *60 + self.seconds
        print('Second: ' , second)

    def show_time(self):
            if self.seconds >= 60:
                self.seconds -= 60
                self.minute += 1
            if self.minute >= 60:
                self.minute -= 60
                self.hour += 1
            if self.hour >= 24:
                self.hour -= 24
            if self.seconds < 0:
                self.minute -= 1
                self.seconds += 60
            if self.minute < 0:
                self.hour -= 1
                self.minute += 60
            if self.hour < 0:
                self.hour += 24
            if self.hour >= 24:
                self.hour -= 24
            print(str(int(self.hour)).zfill(2),":",str(int(self.minute)).zfill(2),":",str(int(self.seconds)).zfill(2))

time1 = input('Please enter  first time :  {hour:minute:second } : ')
time1 = time1.split(':')
time1 = Time(int(time1[0]) , int(time1[1]) , int(time1[2]))

time2 = input('Please enter second time : {hour:minute:second  } : ')
time2 = time2.split(':')
time2 = Time(int(time2[0]) , int(time2[1]) , int(time2[2]))

while True:
    print('1- sum of times ?  ')
    print('2- submite of times ?  ')
    print('3- second to time   ')
    print('4- time to second   ')
    print('5- do you want exit ?  ')
    choice = int(input('Please enter your choose: '))
    if choice == 1:
        res = time1.sum_time(time2)
        res.show_time()
    elif choice == 2:
        res = time1.sub_time(time2)
        res.show_time()
    elif choice == 3:
        second = int(input("Please enter second: "))
        res = Time(None , None , second)
        res.second_to_time()
        res.show_time()
    elif choice == 4:
        time1.time_to_second()
        time2.time_to_second()
    elif choice == 5:
        exit()
    else:
        print('Some thing Wrong . Try again.')