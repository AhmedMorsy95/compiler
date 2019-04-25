from .dfaState import  state
from .min_state import  min_state
from .DFA import DFA
from .NodeGenerator import NodeGenerator
import queue
from string import ascii_letters

symbols_list = []
for char in ascii_letters:
    symbols_list.append(char)
for i in range(0,9):
    symbols_list.append(str(i))

no=0
dic ={} # for mappinhg same state
def check(c):
    no=0
    for i in range(0,len(c.nodes_of_this_class)):
        print(i)
        if not i in dic:
           dic[i]=no
           no += 1
        for j in range(i+1,len(c.nodes_of_this_class)):
              ans  = c.is_same(c.nodes_of_this_class[i],c.nodes_of_this_class[j],symbols_list)
              if ans == True:
                  dic[j]=dic[i]
    print(dic)
    return no
def minimization_states():
    initial_accepted_state=[]
    initial_unaccepted_state=[]
    nothing = []
    number_of_states = len(state.state_instances)
    print("number of states",number_of_states)
    for s in state.state_instances:
        if s.isAccept():
            initial_accepted_state.append(s)
        else:
            initial_unaccepted_state.append(s)
    q = queue.Queue()
    class1 = min_state(initial_unaccepted_state)
    class2 = min_state(initial_accepted_state)
    q.put(class1)
    q.put(class2)
    cnt=0
    class1.map_state_to_id()
    class2.map_state_to_id()
    while(not q.empty()):
       flag=0
       total_flag=0
       c = q.get()
       no= check(c)
       for i in range(1,no):
        l=[]

        for keys,values in dic.items():
          if values==i:
            flag=1
            l.append(c.nodes_of_this_class[i])
            c.nodes_of_this_class.pop(i)
        if len(l) != 0:
            class_temp= min_state(l)
            q.put(class_temp)
            class_temp.map_state_to_id()

        q.put(c)

        if flag ==0:
            cnt+=1;
        else:
            flag=0
            cnt=0
        if cnt == number_of_states:
            break
        dic.clear()
    for ins in min_state.class_instance:
        node= ins.nodes_of_this_class[0]
        for symbol in symbols_list:
            ins.add_destination(symbol,min_state.map_state_to_class[node.destinations[symbol]])

        for nodes in ins.nodes_of_this_class:
            if nodes.isAccept() == True :
                ins.accept_state= True
                break
    print(len(min_state.class_instance))
