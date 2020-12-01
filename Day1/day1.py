
def find_pair_with_sum(x,total):
    # Outputs pair of values from list x that sum to give total
    # Given list x and total int, outputs pair of values in x that sum to sum_constraint
    # If such a pair doesn't exist, outputs pair of None values
    # O(n) runtime
    x_set = set(x) # O(1) lookup
    if x.count(total/2)==1: # special case that breaks "is sum_constraint-me in set" below logic
        x_set.remove(total/2)
    for p1 in x:
        if total-p1 in x_set:
            return p1, total-p1
    return None, None # if no such pair exists

def find_triple_with_sum(x,total):
    # Given list x and sum_constraint int, finds triple of values in x that sum to sum_constraint
    # O(n^2) runtime
    for i in range(len(x)):
        p1,p2 = find_pair_with_sum(x[:i]+x[i+1:], total-x[i])
        if p1 is not None:
            return x[i], p1, p2


if __name__ == "__main__":

    with open("data.txt", "r") as f:
        expense_report = list(map(int, f.readlines()))
    total_expense = 2020

    a1 = find_pair_with_sum(expense_report,total_expense)
    a2 = find_triple_with_sum(expense_report,total_expense)
    print('Answer1: Product is {0}, elements are {1} and {2}.'.format(a1[0]*a1[1],*a1))
    print('Answer2: Product is {0}, elements are {1}, {2} and {3}.'.format(a2[0]*a2[1]*a2[2],*a2))
