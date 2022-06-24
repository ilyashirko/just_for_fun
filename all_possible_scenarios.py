# function take list(list1, list2, ..., listn) 
# and return all possible unique combinations of their elements

# EXAMPLE
# input  = [(1, 2), (2, 3)]
# output = [[1, 2], [1, 3], [2, 2], [2, 3]]


def all_possible_scenarios(input_list: list,
                           result: list = [],
                           scenario: list = [],
                           step: int = 0) -> list:
    for i in input_list[step]:
        new_scenario = scenario + [i]
        if step < len(input_list) - 1:
            all_possible_scenarios(input_list, result, new_scenario, step + 1)
        else:
            result.append(new_scenario)
    return result
