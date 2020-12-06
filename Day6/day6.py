
from typing import List

def parse_boarding_passes(boarding_passes_raw: List[str],mode: str):
    """Takes list of str representation of question answers, and compiles
    into a list of one set of answers per group
    Groups in the input are ended by '' entries
    

    Parameters
    ----------
    boarding_passes_raw : List[str]
        list of individuals answers - groups are seperated by '' entries
    mode : str
        'union' or 'intersection' for type of aggregation used

    Returns
    -------
    passes_clean : List[set]
        list of sets of union answers per group

    """
    passes_clean = []
    is_first_in_grp = True
    for b_pass in boarding_passes_raw:
        if len(b_pass)>0:
            if is_first_in_grp:
                this_q = set(b_pass)
            else:
                if mode == 'union':
                    this_q.update(b_pass)
                else:
                    this_q.intersection_update(b_pass)
            is_first_in_grp = False
        else:
            passes_clean += [this_q]
            is_first_in_grp = True
    return passes_clean


if __name__ == '__main__':
    
    with open("data.txt", "r") as f:
        boarding_passes = [r.rstrip('\n') for r in f.readlines()]
    boarding_passes += [''] # add seperator on the end

    print('The sum of the counts using union is {0}'.format(sum([len(x) for x in parse_boarding_passes(boarding_passes,'union')])))
    print('The sum of the counts using intersection is {0}'.format(sum([len(x) for x in parse_boarding_passes(boarding_passes,'intersection')])))
