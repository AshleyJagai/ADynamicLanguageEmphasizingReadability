#        Name: <Cyrine Ben Ayed, Aria Ramanathan, Ashlely Jagai >
# Course Info: CSC111 - Fall 2021
# Description: Submission for Assignment 03
#        Date: <10/15/2021>


def main():
  base_text = "Inside every text, and every word, there is a world of wonder! Sometimes, computer analysis can reveal interesting patterns in the texts that we read and write, as well as the patterns that we all follow when using written language. Another interesting fact is that when we count them, the number and types of words used follow very similar patterns even in different languages."
  print("The base text is \n", base_text)
  print()
  pre_process(base_text)
  word_list = pre_process (base_text)
  print("The processed list is \n", word_list)
  print()
  stats = word_stats(word_list)
  print("The stats are:")
  print("  num words: ", stats[0])
  print("  shortest word is: '{:s}', size: {:d}".format(stats[1], stats[2]))
  print("  longest word is: '{:s}', size: {:d}".format(stats[3], stats[4]))
  print("  mean word length: ", stats[5])
  # counts for testing
  count_and = frequency (word_list, "and")
  print ("The number of 'and' instances in the text was: ", count_and)
  count_is = frequency (word_list, "is")
  print ("The number of 'is' instances in the text was: ", count_is)
  count_the = frequency (word_list, "the")
  print ("The number of 'the' instances in the text was: ", count_the)
  count_in = frequency (word_list, "in")
  print ("The number of 'in' instances in the text was: ", count_in)

# Task 1
def pre_process (txt):
  if(txt == ""):
    return list()
  else:
    lowTxt = txt.lower()
    txtList = lowTxt.split(" ")
    newTxt = ""
    for i in range(0,len(txtList)):
      charCheck = txtList[i]
      for char in charCheck:
        idx = charCheck.find(char)
        if charCheck[idx].isalpha():
          newTxt += charCheck[idx]
      newTxt += " "
    return newTxt.split()
  
  

#Task 2


def word_stats (wrd_li):
  if wrd_li == "":
    return list()
  else:
    stats_list = list()
  #First value
    stats_list.append(len(wrd_li))
  #Second value
    second_value = min (wrd_li, key=len)
    stats_list.append(second_value)
  #Third value
    stats_list.append(len(second_value))
  #Fourth value
    fourth_value = max(wrd_li, key=len )
    stats_list.append(fourth_value)
  #Fith value
    stats_list.append(len(fourth_value))
  #Six value
    wordCount = len(wrd_li)
    addition = 0
    for word in wrd_li:
      ch = len(word)
      addition = addition + ch
    avg = addition / wordCount 
    stats_list.append(avg)
    return (stats_list) 


#Task 3
def frequency (wrd_li, string):
 if (wrd_li=="") or (string == ""):
	 return -1
 else:
    str_freq= 0
    for i in range (len(wrd_li)):
      str_freq += wrd_li[i].count(string)
    return str_freq  



if __name__ == "__main__":
   main()

# REFERENCES
#https://docs.python.org/2.5/lib/string-methods.html
