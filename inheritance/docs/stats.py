from sys import stdin

def userIn():
    for line in stdin:
        # numbers = [int(x) for x in line.split()]
        numbers = list(map(int, line.split()))
        print(numbers)
        return numbers
    
        #call print

def calculate(data):
    ans=[]
    i=0
    for x in data:
        num = int(data[i])
        
        ans.append(f'Case {i}: {printAns(data)}')
        i+=1
        return ans
        


def printAns(num_list:list):
    return f'{min(num_list)} {max(num_list)} {(max(num_list) - min(num_list))}'

def main1():
    
    numbas=userIn()
    print(f'mains nums:',numbas)
    out=calculate(numbas)
    printAns(out)
    #print(f'out:',out)

if __name__ =='__main__':
    main1()

