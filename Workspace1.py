from textblo

text = ("Football is a good game. It has many health benefit")
text_blob_object = TextBlob(text)
print(text_blob_object.words.pluralize())