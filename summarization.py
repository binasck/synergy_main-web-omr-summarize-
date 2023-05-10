from transformers import  pipeline
summarizer = pipeline("summarization")



def calling_transsum(text):
    to_tokenize = text
    to_tokenize = to_tokenize.split(".")

    ummarized = summarizer(to_tokenize, min_length=15, max_length=1500)
    print(ummarized)
    return ummarized


# calling_transsum("""Mohandas Karamchand Gandhi was born on October 2, 1869 in Porbandar, India. He became one of the most respected spiritual and political leaders of the 1900's. Gandhi helped free the Indian people from British rule through nonviolent resistance, and is honoured by Indians as the father of the Indian Nation. He was highly influenced by Thoreau, Tolstoy, Ruskin, and above all the life of Jesus Christ. The Bible, precisely the Sermon of the Mount and the Bagavad -Gita had a great influence on him. The Indian people called Gandhi 'Mahatma', meaning Great Soul. At the age of 13 Gandhi married Kasturba, a girl the same age.""")