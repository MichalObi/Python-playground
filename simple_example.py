import random
import time
import datetime
import calendar

# global config
start_time = time.time()
defaultMinNumber = 1
defaultMaxNumber = 5
defaultNumber = random.randint(defaultMinNumber, defaultMaxNumber)

fruits = ['orange', 'banana', 'anananas']

iterationCopy= 'Iteration '
notNumberCopy = 'It is not a number'
defaultParamCopy = 'We will use default param'
forLoopCopy = 'Example of for loop: ==========>'
whileLoopCopy = 'Example of while loop: ==========>'
forLoopOutOfRangeCopy = 'No items in fruits array'
programStartCopy = 'Program initialized in '
programEndCopy = 'Program execution time - %s seconds'
currentDateFormat = '%Y-%m-%d %H:%M'
programNextInitCopy = 'Next program run '
displayDayCopy = ' (%s)'

class helperMsgClass:
    @staticmethod
    def printMsg(msgType, val):
        if (msgType == 'default_iteration'):
            print defaultParamCopy + ' ' + str(val)
        elif (msgType == 'for_loop'):
            print forLoopCopy
        elif (msgType == 'while_loop'):
            print whileLoopCopy

class defaultClass:
    def defaultIteration(self, x):
        helperMsgClass.printMsg('default_iteration', x)
        self.iterationsFn(x)

    def forLoopExample(self, x):
        helperMsgClass.printMsg('for_loop', x)
        for i in range(x):
            try:
                print iterationCopy + str(i) + ' fruit ' + fruits[i]
            except:
                print 'Iteration '+ str(i) + ' ' +  forLoopOutOfRangeCopy

    def whileLoopExample(self, x):
        helperMsgClass.printMsg('while_loop', x)
        while (x <= defaultMaxNumber):
            print iterationCopy + str(x)
            x = x + 1

    def iterationsFn(self, x):
        self.forLoopExample(x);
        self.whileLoopExample(x)

    def mainFn(self, x = defaultNumber):
        if (isinstance(x, int)):
            if (x is defaultNumber):
                self.defaultIteration(x)
            else:
                if (defaultMinNumber <= x <= defaultMaxNumber):
                    self.iterationsFn(x)
                else:
                    self.defaultIteration(defaultNumber)
        else:
            print notNumberCopy

if __name__ == "__main__":
    def currentDayName(number):
        return str(calendar.day_name[number])

    #inicialize class instance
    now = datetime.datetime.now()
    program = defaultClass()
    program.mainFn(5)

    programStartCopy = programStartCopy +  now.strftime(currentDateFormat) + displayDayCopy % currentDayName(datetime.datetime.today().weekday())
    programEndCopy = (programEndCopy % (time.time() - start_time))

    #script can run every 24h with cron - do not use Timer obj for this
    programNextInitCopy = programNextInitCopy + str(now + datetime.timedelta(hours=24)) + displayDayCopy % currentDayName(datetime.datetime.today().weekday() + 1)

    print programStartCopy
    print programEndCopy
    print programNextInitCopy

    #write start and end info to log file
    f = open('log.txt', 'a+')
    f.write(programStartCopy)
    f.write('\n')
    f.write(programEndCopy)
    f.write('\n')
    f.write(programNextInitCopy)
    f.write('\n')
    f.close()
