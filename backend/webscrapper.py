#takes the skills from differnece.py and then prints out a summary
#fitrst make a dictionary 

from pdfparser import fetch_topic_summary


def display_skills_summary(dict):
    #dict is the list that is returned by get_difference_in_skills method from Differences class (differnece.py)
    final_dict = {}
    for skill in dict:
        final_dict[skill] = fetch_topic_summary(skill)

    return final_dict

