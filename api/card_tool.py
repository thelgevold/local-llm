from pydantic import Field

def get_lowest_next_number(current_play, selected_number: int = Field(description="""selected number""", default=0)):

    """
    Your task is to select a single number from a list of numbers called play list. The requirement is to select the first number from the play list that is greater than or equal to a number called current play.

    Follow the following requirements when selecting the number:
    
    The selected value must be the smallest value from the play list that is greater than or equal to current play

    The numbers in the play list are ordered in ascending order. This means you must traverse the play list left to right and select the first value that is greater than or equal to current play.

    Numbers must be compared based on the following rules: 2<3<4<5<6<7<8<9<10<11<12<13<14.
        
    After selecting the number, double check to be sure that the selected number is actually the smallest value from the play list that is greater than or equal to the current play. If that is not the case, you must correct the error.

    If you are unable to find a number that satisfies these requirements, you must select 0 to indicate that no value was selected.

    Here are some examples:
    If the current play is 7 and the numbers from the play list are [7, 9, 12] the correct number is 7 since it is the lowest number that satisfies the condition.
    If the current play is 7 and the numbers from the play list are [7, 8, 12] the correct number is 7 since it is the lowest number that satisfies the condition.
    If the current play is 5 and the numbers from the play list are [3, 7] the correct number is 7 since it is the lowest number that satisfies the condition.
    If the current play is 8 and the numbers from the play list are [6, 7, 12] the correct number is 12 since it is the lowest number that satisfies the condition.
    If the current play is 3 and the numbers from the play list are [3, 4, 7, 8, 11, 12, 13] the correct number is 3 since it is the lowest number that satisfies the condition.
    If the current play is 4 and the numbers from the play list are [5, 9, 12] the correct number is 5 since it is the lowest number that satisfies the condition.
    If the current play is 14 and the numbers from the play list are [6, 12, 12] the correct number is 0 since no numbers in the play are greater than or equal to the current play.
    If the current play is 9 and the numbers from the play list are [3, 6, 12] the correct number is 12 since it is the lowest number that satisfies the condition.

    If the current play is 7 and the the play list is [5] the selected number is 0 since none of the numbers in the play list are greater than or equal to the current play.
    If the current play is 9 and the numbers from the play list are [3, 4, 5] the correct number is 0 since no numbers in the play list are greater than or equal to the current play.
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
