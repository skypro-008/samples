def print_statistics(list_quest: list[Questions:]):
    """ calculate statistics and print it
    use list

    of class Questions objects
    """
    score_summ: int = 0
    right_counter: int = 0
    answer_counter: int = 0
    # tmp_q = Questions()
    for tmp_q in list_quest:
        if tmp_q.has_answer_requested:
            answer_counter += 1
            if tmp_q.is_correct():
                score_summ += tmp_q.get_points()
                right_counter += 1
    print("Вот и всё!")
    print(f"Отвечено на {right_counter} вопросов из {answer_counter}")
    print(f"Набрано баллов  {score_summ}")
