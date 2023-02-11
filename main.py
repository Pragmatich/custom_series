def custom_series():
    steps = 2
    step_sizes = []
    range_list = [1, 5, 0, 10]
    final_list = [[]]

    for i in range(0, len(range_list), 2):
        step_sizes.append(int((range_list[i+1] - range_list[i]) / steps))
        final_list[0].append(range_list[i])
        final_list[0].append(range_list[i] + step_sizes[int(i/2)])

    remaining_enter = len(range_list) - 1
    final_list_2 = final_list[0].copy()

    def range_stepper(remaining_enter, final_list_2):
        i = len(range_list) - remaining_enter - 1

        # If i is odd
        if i % 2:
            step = step_sizes[int((i-1)/2)]
            from_range = final_list_2[i-1] + step
            to_range = range_list[i] + step
        
        # If i is even
        else:
            step = step_sizes[int(i/2)]
            from_range = range_list[i]
            to_range = range_list[i+1]

        final_list_0 = []

        for j in range(from_range, to_range, step):
            final_list_2[i] = j
            final_list_1 = []

            if remaining_enter:
                final_list_1 = range_stepper(remaining_enter - 1, final_list_2).copy()
                for element in final_list_1:
                    final_list_0.append(element.copy())
            else:
                final_list_0.append(final_list_2.copy())

        return final_list_0

    final_list = range_stepper(remaining_enter, final_list_2).copy()

    print(final_list)

custom_series()
