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

with open('test.txt', 'r') as f:
    content = ''
    while len(content) < 10:
        chunk = f.read(10) # these will bring first 10 charcaters
        if not chunk:
            break
        content += chunk  # Corrected line

print(content[:100])  # Optional: trims if more than 100 characters
