def double_evens(int_list):
    return [2*i if i%2==0  else i for i in int_list]

print(double_evens( range(10)))