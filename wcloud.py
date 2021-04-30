from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def plot_cloud(wordcloud):
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud)
    plt.axis("off");


def render(text):
    wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color='black', colormap='Set2', collocations=False, stopwords=STOPWORDS).generate(text)
    plot_cloud(wordcloud)
    wordcloud.to_file("wordcloud.png")


def render2image(text):
    wordcloud = WordCloud(width=1200, height=800, random_state=1, background_color='black', colormap='Set2', collocations=False, stopwords=STOPWORDS).generate(text)
    plot_cloud(wordcloud)
    return wordcloud.to_image()


def main():
    with open('input.txt', 'r') as file:
        text = file.read().replace('\n', '')
    render(text)


if __name__ == '__main__':
    main()
