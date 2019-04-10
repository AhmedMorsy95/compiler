from dfaState import  state
from min_state import  min_state
import queue

symbols_list = ['a', 'b', 'm', 'e', 'r', 'n', 'c']
no=0
dic ={} # for mappinhg same state
def check(c):
    no=0
    for i in range(0,len(c.nodes_of_this_class)):
        if not i in dic:
           dic[i]=no
           no += 1
        for j in range(i+1,len(c.nodes_of_this_class)):
              ans  = c.is_same()
              if ans == True:
                  dic[j]=dic[i]

def minimization_states():
    initial_accepted_state=[]
    initial_unaccepted_state=[]
    number_of_states = len(state.state_Nodes)
    for s in state.state_Nodes:
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
       check(c)
       for i in range(1,no):
        l={}
        for keys,values in dic:
          if values==i:
            flag=1
            l.append(c.nodes_of_this_class[i])
            c.nodes_of_this_class.pop(i)
        if len(l) != 0:
            class_temp= min_state(l)
            q.put(class_temp)
            class_temp.map_state_to_id()

        if flag ==0:
            break
        else:
            flag=1
        dic.clear()




