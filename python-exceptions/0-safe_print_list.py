#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):          # x dəfə cəhd edirik
            print(my_list[i], end='')  # IndexError burada yaranacaq
            count += 1              # uğurla çap edilənləri sayırıq
    except IndexError:
        pass                        # xəta olsa sakitcə davam et
    print()
    return count                    # neçə element çap edilibsə onu qaytar
