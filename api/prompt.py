def prompt_template(cards, current_play):
    return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

    ### Instruction:
    Find the smallest integer in the playlist that is greater than or equal to the current play. If no such number exists, return 0.

    ### Input:
    \"play_list\":{cards} \"current_play\": {current_play}""" 