from typing import List, Dict


def prompt_single_yes_no_question(question:str, code:str) -> str:
    question_template = f"""Does the following smart contract code "{question}"? Answer only "Yes" or "No".

{code}
    """
    return question_template


def prompt_multiple_choice_scenarios(scenarios:List[str], code:str) -> str:
    question_template="""Given the following smart contract code, answer the questions below and organize the result in a json format like {"""
    
    for index, scenario in enumerate(scenarios):
        question_template += f'"{index+1}": "Yes" or "No"'
        if index != len(scenarios)-1:
            question_template += ', '

    question_template += f'}}.\n'

    for index, scenario in enumerate(scenarios):
        question_template += f'"{index+1}": Does it "{scenario}"?\n'
    
    question_template += f'\n{code}'
    
    return question_template
