# with open('test.txt','r') as f:
#     # for line in f:
#     #     print(line,end='')
#     size_to_read=10
#     content=f.read(size_to_read)
#     # print(content,end='')
#     while len(content)>0:
#         print(content,end='*')
#         content=f.read(size_to_read)

# with open('test.txt','r') as rf:
#     with open('example.log','w') as wf:
#         for line in rf:
#             wf.write(line)

# with open('test.txt', 'r') as f:
#     content = ''
#     while len(content) < 10:
#         chunk = f.read(10) # these will bring first 10 charcaters
#         if not chunk:
#             break
#         content += chunk  # Corrected line

# print(content[:100])  # Optional: trims if more than 100 characters

# player_score={}

# with open("scores.csv", "r") as f:
#     for line in f:
#         tokens=line.split(',')
#         player=tokens[0]
#         score=int(tokens[1])
#         print(tokens)
#         print(player)
        
#         if player in player_score:
#             player_score[player].append(score)
#         else:
#             player_score[player]=[score]


# for player, score_list in player_score.items():
#     max_score=min(score_list)
#     min_score=min(score_list)
#     avg_score=sum(score_list)/len(score_list)
#     print(f"{player}==>Min:{min_score}, Max:{max_score}, Avg{avg_score}")

# with open('check.txt','r') as f:
#     lis=[]
#     for line in f:
#         lis.append(line)

# print(lis)

# with open('check.txt','r') as f:
#     count=0
#     for lines in f:
#         count+=1

# print(count)

# with open('check.txt','r') as f:
#     counter={}
#     for line in f:
#         words = line.strip().split()  
#         print(words)
#         for word in words:
#             if word in counter:
#                 counter[word]+=1
#             else:
#                 counter[word]=1

# print(counter)

# with open('num.txt','w') as f:
#     f.write('12\n13\n12')
# with open('num.txt','r') as xf:
#         total=0
#         lines=xf.readlines()
#         lines_count=len(lines)
#         for line in lines:
#               total += int(line.strip())
        
      
# print(f'The sum for it {total}')
# print(f'Total Numbers are: {lines_count}')
# print(f'Average is {total / len(lines)}')

# with open('reverse.txt','r') as rf:
#     lines=rf.readlines()
#     lines.reverse()
    
#     with open('copy.txt','w') as wf:
      
#       for line in lines:
#          clean_lines=line.strip()
#          print(clean_lines)
#          wf.write(clean_lines + '\n')

##################################################Functions-File Handling##################################################### 
# Seek() 
'''These function basically returns the  Current position of Pointer in bytes from the beignning '''
# with open("check.txt", "r") as f:
#     print(f.tell())  # Likely 0 — at the start
#     f.read(5)
#     print(f.tell())  # 5 — after reading 5 characters
# Seek()
'''Seek Functions allow us to set a position from where we have to position it'''
# with open('copy.txt','r') as f:
#    print(f.tell())
#    f.seek(12)
#    print('Lets check')
#    print(f.read()) 

# truncate(size) – "Cut the file to a specific size"
# '''The truncate funions allwows the user to ressize the file to a given number by bytes where the file is
#  accessed through append Mode '''
# with open('copy.txt','r+') as f:
#     f.truncate(15)


##################################################Functions-File Handling Exercise##################################################### 
with open('scroll.txt','w') as f:
    f.write('Dear Majesty,\nYou are learning Python file handling.\nKeep ruling with code and logic!')
with open('scroll.txt','r') as f:
    print(f"Pointer at start: {f.tell()}")
    first_line = f.readline()
    print(f"First line: {first_line.strip()}")
    print(f"Pointer after reading first line: {f.tell()}")
    # Move pointer back to second line
    # second_line = f.readline()  # Read second line
    f.seek(len(first_line))     # Move pointer to start of second line
    print(f"Second line after seek: {f.readline().strip()}")

with open('scroll.txt','r+') as f:
    f.truncate(40)

with open('scroll.txt', 'r') as f:
    result = f.read()
    print("\n📄 File content after truncation:\n")
    print(result)

    
