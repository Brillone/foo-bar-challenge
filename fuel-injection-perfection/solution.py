def devide(current_pallets):
    return current_pallets/2


def add(current_pallets):
    return current_pallets + 1


def remove(current_pallets):
    return current_pallets - 1


# actions
actions = dict(
    devide=devide,
    add=add,
    remove=remove
)


def act(current_pallets, action):
    action_func = actions.get(action)

    return action_func(current_pallets)


def solution(n):
    n = int(n)
        
    visited_states = []
    current_states = [n]
    step = 0
    finished = False

    while not finished:

        next_states = []
        
        current_states = set(current_states)
        visited_states = set(visited_states)
        
        if 1 in current_states:
            return str(step)

        step = step + 1

        for state_i in current_states:
            visited_states.add(state_i)

            for action in actions.keys():
                if state_i % 2 == 0 and action=='devide':
                    action_next_state = act(state_i, action)
                elif state_i % 2 != 0 and action!='devide':
                    action_next_state = act(state_i, action)
                else:
                    continue
                
                if (not action_next_state in visited_states) and action_next_state>0:
                    next_states.append(action_next_state)

        current_states = next_states


if __name__ == "__main__":
    assert solution('15') == '5'
    assert solution('4') == '2'