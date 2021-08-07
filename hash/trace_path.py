def trace_path(my_dict):  # A Map object
    # Start node = node that is not in values
    
    e = [ e for e in my_dict.keys() if not e in my_dict.values() ][0]

    out = [] 

    while len(out)<len(my_dict.keys()):
        out.append([e,my_dict[e]])
        e=my_dict[e]
    return (out)

city = {'NewYork': 'Chicago','Boston': 'Texas', 'Missouri': 'NewYork', 'Texas': 'Missouri'}

print(trace_path(city))