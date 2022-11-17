print("Нажмите стоп, чтобы выйти из цикла")

do_continue = True

while do_continue:
    user_input = input()
    if user_input.lower() in ["стоп", "хватит", "stop"]:
        do_continue = False
    else:
        print("продолжаем")

print("закончили")
