from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt').read()
story_words = []

for line in story.split():
        story_words.append(line)
        
print(story_words)