grossary_list={}
while True:
    try:
        my_item=input().upper()
        if my_item in grossary_list:
            grossary_list[my_item]=grossary_list[my_item]+1
        else:
            grossary_list[my_item]=1
    except EOFError:
        print()
        for key,value in sorted(grossary_list.items()):
            print(value,key)
        break





