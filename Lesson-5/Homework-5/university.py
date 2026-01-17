universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    number = []
    tuition = []
    for uni in universities:
        number.append(uni[1])
        tuition.append(uni[2])
    return number, tuition

enrollment_list, tuition_list = enrollment_stats(universities)

def mean(numbers):
    return round(sum(numbers) / len(numbers), 2)

def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(numbers)
    mid = n // 2
    if n % 2 == 1:
        return sorted_nums[mid]
    else:
        return (sorted_nums[mid-1] + sorted_nums[mid]) / 2
    
print(f"Total students: {sum(enrollment_list):,}")
print(f"Total tuition: ${sum(tuition_list):,}")
print()
print(f"Student mean: {mean(enrollment_list):,}")
print(f"Student median: {median(enrollment_list):,}")
print()
print(f"Tuition mean: ${mean(tuition_list):,}")
print(f"Tuition median: ${median(tuition_list):,}")







