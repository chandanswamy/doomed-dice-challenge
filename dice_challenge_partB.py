from array import array

# Function to calculate the sum of elements in an array
def sumOfArray(array):
  sum_of_combination = 0
  for element in array:
    sum_of_combination += element
  return sum_of_combination

# Function to generate a 2D array representing the sum distribution of two dice
def sum_Distribution(Dice_A, Dice_B):
  # creating a 2d array and initializing with 0
  sum_Array = [[0 for i in range(len(Dice_A))] for j in range(len(Dice_B))]
  for a in range(len(Dice_A)):
    for b in range(len(Dice_B)):
      sum_Array[a-1][b-1] = Dice_A[a-1] + Dice_B[b-1]

  return sum_Array

# Function to calculate the probability of a specific sum in the sum distribution
def single_probability(Dice_A, Dice_B, sum):
  # to find the probability of any number passed as the sum parameter
  sum_Array = sum_Distribution(Dice_A, Dice_B)
  count = 0
  for rows in sum_Array:
    for column in rows:
      if(column == sum):
        count = count + 1
  probability = count / 36
  return probability

# Function to calculate the probabilities for all possible sums
def all_probabilities(Dice_A, Dice_B):
  prob_dict = {
    "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0
  }
  for i in range(2, 13):
    prob_dict[str(i)] = round(single_probability(Dice_A, Dice_B, i), 4)
  return prob_dict

# Function to calculate all possible combinations of dice based on certain restrictions
def posibilities_Calc(curr, free_space, input_values, posibilities, fixed_values, repetition=True):
  # base case
  if(0 == free_space):
    curr = sorted(curr)
    posibilities.add(tuple(curr))
    return posibilities

  # if the repetition of the elements is allowed, below block runs
  if(repetition):
    for input_value in input_values:
      posibilities_Calc(curr + [input_value], free_space - 1, input_values, posibilities, fixed_values, True)

  # if repetition not allowed, then below block runs
  else:
    for i in range(len(input_values)):
      remaining_input_values = input_values[:i] + input_values[i + 1:]
      posibilities_Calc(curr + [input_values[i]], free_space - 1, remaining_input_values, posibilities, fixed_values, False)
  return posibilities

# Final function that returns the new dice based on specified rules
def transform(dice_a, dice_b):
  original_possibilities = all_probabilities(dice_a, dice_b)

  # These are fixed values because 1 is needed to get the sum 2 (no other possible ways and similarly for 12, we need 4)
  fixed_values_A = [1, 4]
  input_values_A = [1, 2, 3, 4]

  # Free space indicates the required no.of elements needed to make the dice complete
  free_space_A = 4

  # Possibilities are converted to sets since I got multiple duplicates of the same array 
  posibilities_A = set()

  new_dice_A_possibility = posibilities_Calc(fixed_values_A.copy(), free_space_A, input_values_A, posibilities_A, fixed_values_A, True)

  # Similiar to die A, the 1 is needed to get 2 as the sum, and the 8 is the only option for the 12 to be returned. Also, can be empty and still work fine.
  fixed_values_B = [1, 8]

  # Any number more than 8 will give the sum greater than 12. So the values are capped to a maximum of 8, and the 1 & 8 are fixed, reducing the values to 2 to 7.
  input_values_B = [2, 3, 4, 5, 6, 7]

  free_space_B = 4
  posibilities_B = set()

  # Repetition is set False as the rule only states that it can have as many spots but not as many sides with the same spots, reducing the space required and time too.
  new_dice_B_possibility = posibilities_Calc(fixed_values_B.copy(), free_space_B, input_values_B, posibilities_B, fixed_values_B, False)

  for a in new_dice_A_possibility:
    for b in new_dice_B_possibility:
      # As the sum of all spots of a six-sided die is 21, and 2 dice give 42, so if the sum of both dice does not add up to 42, the set will be ignored.
      if((sumOfArray(a) + sumOfArray(b)) == 42):
        new_sum_possibility = all_probabilities(array('i', a), array('i', b))
        # Checking every answer to find if any one matches the original probabilities, if matches, returning it
        if(original_possibilities == new_sum_possibility):
          New_Dice_A = a
          New_Dice_B = b
          return New_Dice_A, New_Dice_B

# Example usage
Dice_A = [1, 2, 3, 4, 5, 6]
Dice_B = [1, 2, 3, 4, 5, 6]

print("New Dice are")
New_Dice_A, New_Dice_B = transform(Dice_A, Dice_B)

print(f"New Dice A: {New_Dice_A}")
print(f"New Dice B: {New_Dice_B}")
