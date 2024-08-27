def day_name(day: int) -> str:
    '''
    Returnes the name of the day the number of which was given.
    :param day:
    the nuber of the day
    :return:
    the name of the day
    '''
    days_list: list[str] = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    if type(day) != int:
        raise TypeError;
    elif day < 1 or day > 7:
        raise ValueError("no such week day");
    else:
        return days_list[day - 1];



