import time



def main(first_file,second_file):

    mistake,correct = 0,0
    unidenfily = 0
    start = time.time()
    with open(first_file,'r') as f1:
        with open(second_file,'r') as f2:
            main = f1.readline()
            maker = f2.readline()
            for l1,l2 in zip(main,maker):
                
                if '�' in l2:
                    unidenfily +=1

                if l1!=l2:
                    mistake +=1
                elif l1==l2:
                    correct +=1
                
                else:
                    print("Kima bi na ho rh h.")
    end = time.time()
    print("This is the time taken by this function :",end-start)
    print(f"This is the correct letter : {correct} and the mistake letter : {mistake}")
    print("there is also some enidwentify symoal",unidenfily)


first_file = 'word.txt'
second_file = 'result.txt'

main(first_file,second_file)
