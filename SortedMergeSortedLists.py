def sorted_merge_sorted_list(list1, list2):

#the question stated that the function should just merge the two lists into 1 sorted list. I assumed that
#this meant you wanted the function to return the merged list. If that was not the case then the line
# below each "#1" should be replaced with "print(merged_list)".

    index1=index2=0
    len_list1=len(list1)
    len_list2=len(list2)
    len_merge_list_target=len_list1+len_list2
    merged_list=[]

    if len_list1==0:
        merged_list=list2
        #1
        return merged_list
    elif len_list2==0:
        merged_list=list1
        #1
        return merged_list

    while len(merged_list)<len_merge_list_target:
        if list1[index1]<=list2[index2]:
            merged_list.append(list1[index1])
            index1+=1
        else:
            merged_list.append(list2[index2])
            index2+=1
        if index1==len_list1:
            merged_list+=list2[index2:]
            break
        if index2==len_list2:
            merged_list+=list1[index1:]
            break
    return merged_list