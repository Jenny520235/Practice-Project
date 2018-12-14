# 字符串的替换方式：
# 示例
poetry="远看成岭侧成峰，远进高低各不同.进"
print(poetry)
# 替换上述诗句中的错别字“进”，改为“近”
new_poetry=poetry.replace("进","近")
print(new_poetry)
# 不想把最后提出来的“进”替换掉，可用下列方法
new_poetry=poetry.replace("进","近",1)
print(new_poetry)
# 默认的是将所有都替换掉，如果你只想替换其中的某些，就可以选定替换的次数/个数
new_poetry=poetry.replace("进","近",2)
print(new_poetry)