# python playground
import random

# global config variable
defaultMinNumber = 1
defaultMaxNumber = 5
defaultNumber = random.randint(defaultMinNumber, defaultMaxNumber)

iterationCopy= 'Iteration '
notNumberCopy = 'It is not a number'
defaultParamCopy = 'We will use default param'
forLoopCopy = 'Example of for loop: ==========>'
whileLoopCopy = 'Example of while loop: ==========>'
forLoopOutOfRangeCopy = 'No items in fruits array'

fruits = ['orange', 'banana', 'anananas']

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
    #inicialize class instance
    program = defaultClass()
    program.mainFn(5)
