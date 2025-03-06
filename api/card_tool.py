from pydantic import Field

def get_lowest_next_number(current_play: int = Field(description="""current play"""), selected_number: int = Field(description="""selected number""", default=0)):

    """
    Your task is to select a number from a play list that consists of a series of numbers where the set of all possible values is limited to the following set of positive integers [3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14].
    Select the lowest number in the play list that is greater than or equal to the current play. Select 0 if you are unable to find a number in the play list that is greater than or equal to the current play.
    Examine the numbers from the play list that are greater than or equal to the current play first, then select the smallest one. 
    You must alway give priority to selecting numbers from the play list that are equal to the current play over numbers that are greater than the current play.
        
    After selecting, run a sanity check to ensure that the selected number is actually greater than or equal to the current play.

    Here are some examples:
    If the current play is 7 and the numbers from the play list are [7, 9, 12] the correct number is 7 since it is the lowest number that satisfies the condition.
    If the current play is 5 and the numbers from the play list are [7, 3] the correct number is 7 since it is the lowest number that satisfies the condition.
    If the current play is 8 and the numbers from the play list are [7, 12, 6] the correct number is 12 since it is the lowest number that satisfies the condition.
    If the current play is 3 and the numbers from the play list are [3, 2, 2, 3, 4, 7, 8, 11, 12, 13] the correct number is 3 since it is the lowest number that satisfies the condition.
    If the current play is 4 and the numbers from the play list are [5, 9, 12] the correct number is 5 since it is the lowest number that satisfies the condition.
    If the current play is 14 and the numbers from the play list are [6, 12, 12] the correct number is 0 since no numbers in the play are greater than or equal to the current play.
    If the current play is 9 and the numbers from the play list are [12, 6, 3] the correct number is 7 since it is the lowest number that satisfies the condition.
    If the current play is 7 and the the play list is [5] the selected number is 0 since none of the numbers in the play list are greater than or equal to the current play.
    If the current play is 9 and the numbers from the play list are [5, 4, 3] the correct number is 0 since no numbers in the play list are greater than or equal to the current play.
    """
    # print(current_number)
    # print(selected_number)
    # print(reason_why_the_number_was_selected)
   
    return selected_number 

def get_two_or_ten(selected_number: int = Field(description="""selected number""", default=0)):

    """
    Given the play list, your task is to:

    Check if the number 2 exists in the array.
    If 2 exists, select it.
    If 2 does not exist but 10 exists, select 10.
    If neither 2 nor 10 exists, select 0.
    """
    # print(current_number)
    # print(selected_number)
    # print(reason_why_the_number_was_selected)
   
    return selected_number 
