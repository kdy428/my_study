# 상태를 나타내는 플래그(각 상태가 하나의 비트를 활용)
Walk = 1 << 0
Attack = 1 << 1
Jump = 1 << 2
# 점프 하면서 공격하고 있다.
character_state = 0

def set_state(state, flag):
    return state | flag
def unset_state(state, flag):
    return state & ~flag
def is_state_active(state, flag):
    return state & flag != 0

character_state = set_state(character_state, Walk)
character_state = set_state(character_state, Jump)

print("현재 캐릭터의 상태 :")
if is_state_active(character_state, Walk):
    print("- 걷고 있습니다.")
if is_state_active(character_state, Jump):
    print("- 점프 중입니다.")