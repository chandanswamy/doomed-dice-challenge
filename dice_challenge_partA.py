def print_the_matrix(message, matrix):
    print(message)
    for row in matrix:
        print(row)

def count_the_occurances_of_sums_in_matrix(matrix):
    #Count the occurrences of sums in a matrix.
    dict_a = {}
    for row in matrix:
        for i in row:
            if i not in dict_a:
                dict_a[i] = 1
            else:
                dict_a[i] += 1
    return dict_a
    #Returns Dictionary with sums as keys and their occurrences as values.

def probability_calculator(occurances_of_sum_all_possible_combinations, total_combinations_of_dice_when_rolled_together):
    #Calculate and print the probability of each sum in the given combinations.
    
    dict_b = {}
    for key, value in occurances_of_sum_all_possible_combinations.items():
        probability = value / total_combinations_of_dice_when_rolled_together
        dict_b[key] = probability
        print(f"p(sum={key})= {probability} = {round(probability, 4)}")
    
    #Returns Dictionary with sums as keys and their probabilities as values.  
    return dict_b

def part_A(dice_A, dice_B):
    print("DOOMED DICE CHALLENGE : PART - A")
    #Perform part A of the experiment with two sets of dice.
    total_combinations_of_dice_when_rolled_together = 0
    distribution_matrix_of_all_possible_combinations = []
    distribution_matrix_of_sums_of_all_possible_combinations = []

    # Loop through each value in dice_A
    for i in dice_A:
        row_a = []
        row_b = []

        # Loop through each value in dice_B
        for j in dice_B:
            possible_combination = (i, j)

            sum_of_possible_combination = i + j
            
            #Calculates the total combinations.    
            total_combinations_of_dice_when_rolled_together += 1
            
            row_a.append(possible_combination)
            row_b.append(sum_of_possible_combination)
        
        #Creating the distribution matrix of all possible combinations.
        distribution_matrix_of_all_possible_combinations.append(row_a)
        
        #Creating the distribution matrix of sums of all possible combinations.
        distribution_matrix_of_sums_of_all_possible_combinations.append(row_b)

    #Prints the total combinations.
    result_total_combinations = "Total combinations of dice A and B rolled together: {}"
    print(result_total_combinations.format(total_combinations_of_dice_when_rolled_together))
    
    #Prints the distribution matrix of all possible combinations.
    message = "All possible combinations"
    print_the_matrix(message, distribution_matrix_of_all_possible_combinations)
    
    #Prints the distribution matrix of sums of all possible combinations.
    message = "Sum distributions"
    print_the_matrix(message, distribution_matrix_of_sums_of_all_possible_combinations)

    occurances_of_sum_all_possible_combinations = count_the_occurances_of_sums_in_matrix(distribution_matrix_of_sums_of_all_possible_combinations)

    probability_calculator(occurances_of_sum_all_possible_combinations, total_combinations_of_dice_when_rolled_together)


# Example usage
dice_A = [1, 2, 3, 4, 5, 6]
dice_B = [1, 2, 3, 4, 5, 6]

part_A(dice_A, dice_B)