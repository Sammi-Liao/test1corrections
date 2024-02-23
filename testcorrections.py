# Part 2: Proteins
proteins1 = ['PF13411.1', 'PF12728.1', 'PF01381.2',
            'PF00205.2', 'PF10875.1', 'PF05766.1',
            'PF00860.2', 'PF10766.1', 'PF11812.1']
proteins2 = ['PF13411.1', 'PF13411.4', 'PF01381.2',
            'PF00205.2', 'PF10875.1', 'PF05766.1',
            'PF00860.2', 'PF10766.1', 'PF11819.1']


# 1) function should consist of no more than two lines
def count_unique_proteins(proteinslist):
    return len(set([i.split('.')[0] for i in proteinslist]))

# 2) 
def count_proteins(proteinslist):
    dict = {}
    for i in proteinslist:
        familynum = i.split('.')[0]
        dict[familynum] = dict.get(familynum, 0) + 1
    return dict


# 3) Write a function that accepts 2 arguments, both dictionaries of protein
# counts, as produced by the functino in Q2, and returns the two dictionaires
# combined into a single dictionary. The function should return a dictionary
# of tuples whose values are the counts from both of the original dictionaries
# If the key is absent from one dictionary, report its count as 0
def merge_protein_counts(proteins1, proteins2):
    '''Return a dictionary of tuples'''
    tupledict = proteins1
    for name2, value2 in proteins2.items():
        if name2 in list(tupledict.keys()):
            tupledict[name2] = (tupledict[name2], value2)
    for name, value in tupledict.items():
        if type(value) != tuple:
            tupledict[name] = (tupledict[name], 0)
    for name2, value2 in proteins2.items():
        if name2 not in list(tupledict.keys()):
            tupledict[name2] = tupledict.get(name2, 0) + 1
            tupledict[name2] = (0, tupledict[name2])
    return tupledict



# prints for Part 2
print(count_unique_proteins(proteins1))
print(count_unique_proteins(proteins2))
print()
print(count_proteins(proteins2))
print()
print(merge_protein_counts(count_proteins(proteins1), 
                    count_proteins(proteins2)))
print()


# Part3: Dates
dates_list = ['February 6, 1992', 'February 18, 1992', 'February 27, 1992',
              'September 6, 1994', 'December 1, 1993']

# 1)Write a funciton that takes a list of dates formated as in dates_list and
# returns a list of the same datas in ISO 8601 format, 'YYYY-MM-DD'. Do not use
# pandas in your function, you should be able to write your answer using methods
# for lists, strings, tuples, dictionaries, or sets
def dates_to_iso8601(dates_list):
    isolist = []
    for i in dates_list:
        newlist = i.split(' ')
        mon = newlist[0]
        unclearday = newlist[1]
        day = unclearday[: len(unclearday) - 1]
        year = newlist[2]
        if len(day) == 1:
            day = '0' + day
        if mon == 'January':
            mon = '01'
        if mon == 'February':
            mon = '02'
        if mon == 'March':
            mon = '03'
        if mon == 'April':
            mon = '04'
        if mon == 'May':
            mon = '05'
        if mon == 'June':
            mon = '06'
        if mon == 'July':
            mon = '07'
        if mon == 'August':
            mon = '08'
        if mon == 'September':
            mon = '09'
        if mon == 'October':
            mon = '10'
        if mon == 'November':
            mon = '11'
        if mon == 'December':
            mon = '12'
        datestr = year + '-' + mon + '-' + day
        isolist.append(datestr)
    return isolist


# 2) Write a function that accepts a list of dates formatted as in dates_list
# , returns a list with the same dates, sorted in chronological order. Do not
# use pandas, you should be able to write your answer using methods for lists,
# strings, tuples, dictionaries, or sets
def sort_dates(dates_list):
    iso_list = dates_to_iso8601(dates_list)
    sorted_isolist = sorted(iso_list)
    new_list = []
    for i in sorted_isolist:
        year, mon, day = i.split('-')[0], i.split('-')[1], i.split('-')[2]
        if mon == '01':
            mon = 'January'
        if mon == '02':
            mon = 'February'
        if mon == '03':
            mon = 'March'
        if mon == '04':
            mon = 'April'
        if mon == '05':
            mon = 'May'
        if mon == '06':
            mon = 'June'
        if mon == '07':
            mon = 'July'
        if mon == '08':
            mon = 'August'
        if mon == '09':
            mon = 'September'
        if mon == '10':
            mon = 'October'
        if mon == '11':
            mon = 'November'
        if mon == '12':
            mon = 'December'
        if day[0] == '0':
            day = day[1:]
        new_str = mon + ' ' + day + ', ' + year
        new_list.append(new_str)
    return new_list

print(dates_to_iso8601(dates_list))
print()
print(sort_dates(dates_list))
