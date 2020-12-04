
from typing import List


def parse_records(records_raw:List[str]):
    """Turn list of raw string records (each record across multiple list entries)
    to list of dict structured output (one list entry per record)
    

    Parameters
    ----------
    records_raw : List[str]
        List of records. Records are seperated by '' entries.
        strings of the form: 'key1:value1 key2:value2' for any number of key-value pairs

    Returns
    -------
    records : List[dict]
        List of dicts, structuring the key-value pairs in the records

    """
    records,my_record = [],''
    for r in records_raw:
        if len(r)>0:
            my_record += ' '+r
        else:
            records += [dict([p.split(':') for p in my_record.split()])]
            my_record = ''
    return records

def validate1(record: dict):
    return all([(fld in set(record.keys())) for fld in ['byr','iyr','eyr','hgt','hcl','ecl','pid']])

def validate2(record: dict):
    is_valid = validate1(record)
    if not is_valid:
        return False
    is_valid &= record['byr'].isnumeric() and 1920<=int(record['byr'])<=2002
    is_valid &= record['iyr'].isnumeric() and 2010<=int(record['iyr'])<=2020
    is_valid &= record['eyr'].isnumeric() and 2020<=int(record['eyr'])<=2030
    is_valid &= ((record['hgt'][-2:]=='cm'
                  and 150<=int(record['hgt'][:-2])<=193)
                 or
                 (record['hgt'][-2:]=='in'
                  and 59<=int(record['hgt'][:-2])<=76)
                 )
    is_valid &= (record['hcl'][0]=='#'
                 and len(record['hcl'][1:])==6
                 and all([c in 'abcdef0123456789' for c in record['hcl'][1:]])
                 )
    is_valid &= record['ecl'] in ('amb','blu','brn','gry','grn','hzl','oth')
    is_valid &= record['pid'].isnumeric() and len(record['pid'])==9
    return is_valid
        

if __name__ == "__main__":

    with open("data.txt", "r") as f:
        records = [r.rstrip('\n') for r in f.readlines()]
    
    print('Number of valid records is {0}'.format(sum([validate1(r) for r in parse_records(records)])))
    print('Number of valid records using second rule is {0}'.format(sum([validate2(r) for r in parse_records(records)])))


