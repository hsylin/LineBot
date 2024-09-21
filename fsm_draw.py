from transitions.extensions import GraphMachine
from functools import partial


class Model:

    def clear_state(self, deep=False, force=False):
        print("Clearing state ...")
        return True


model = Model()
machine = GraphMachine(model=model, states=[ 'choose',
        'menu',
        'location',
        'reserve_people',
        'reserve_time',
        'reserve_result',
        'employee',
        ],
                       transitions=[
                           {'trigger': 'advance', 'source': 'user', 'dest': 'choose', 'conditions': 'is_going_to_choose'},
        {'trigger': 'advance', 'source': 'choose', 'dest': 'menu', 'conditions': 'is_going_to_menu'},
        {'trigger': 'advance', 'source': 'choose', 'dest': 'location', 'conditions': 'is_going_to_location'},

         {'trigger': 'advance', 'source': 'choose', 'dest': 'employee', 'conditions': 'is_going_to_employee'},
        
        
        {'trigger': 'advance', 'source': 'choose', 'dest': 'reserve_people', 'conditions': 'is_going_to_reserve_people'},
        
        
        {'trigger': 'advance', 'source': 'reserve_people', 'dest': 'reserve_time', 'conditions':'is_going_to_reserve_time'},
        
        {'trigger': 'advance', 'source': 'reserve_time', 'dest': 'reserve_result', 'conditions': 'is_going_to_reserve_result'},
        
        
        
        
          {'trigger': 'advance', 'source': 'menu', 'dest': 'choose', 'conditions': 'go_back'},
          {'trigger': 'advance', 'source': 'location', 'dest': 'choose', 'conditions': 'go_back'},
          {'trigger': 'advance', 'source':  'reserve_result', 'dest': 'choose', 'conditions': 'go_back'},
          {'trigger': 'advance', 'source':  'employee', 'dest': 'choose', 'conditions': 'go_back'},

                       ],
                       initial='user', show_conditions=True)

model.get_graph().draw('my_state_diagram.png', prog='dot')
