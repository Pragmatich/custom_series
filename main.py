def custom_series():
    steps = 2
    step_sizes = []
    range_list = [1, 5, 0, 10]
    final_list = []
    
    # Creat the step_sizes from ranger_list and steps
    for i in range(0, len(range_list), 2):
        step_sizes.append(int((range_list[i+1] - range_list[i]) / steps))
        final_list.append(range_list[i])
        final_list.append(range_list[i] + step_sizes[int(i/2)])
    
    # reamining_enter --> to define how much level necessary
    remaining_enter = len(range_list) - 1
    final_list_pre = final_list.copy()

    print(step_sizes)

    def range_stepper(remaining_enter, final_list_pre):
        i = len(range_list) - remaining_enter - 1
        print(f'remaining_enter: {remaining_enter}')

        # If i odd
        if i % 2:
            step = step_sizes[int((i-1)/2)]
            from_range = final_list_pre[i-1]
            to_range = range_list[i]
        
        # If i even
        else:
            step = step_sizes[int(i/2)]
            from_range = range_list[i]
            to_range = final_list_pre[i+1] + step
    

        for j in range(from_range, to_range, step):
            if remaining_enter:
                range_stepper(remaining_enter - 1, final_list_pre)
            final_list_pre[i] = j
            print(f'j: {j}')
            final_list.append(final_list_pre)
            
    remaining_enter = range_stepper(remaining_enter, final_list_pre)

custom_series()
