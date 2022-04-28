from textblob import TextBlob


# ANALYSING SENTIMENT AND RATING THEM FROM -1 TO +1


def analyse_sentiment(df,term):
    f_list = df[term].to_list()
    pol = list()
    for l in f_list:
        analysis = TextBlob(l).sentiment
        t = analysis.polarity
        pol.append(t)
    df['sentiment'] = pol
    pol2 = list()
    for l in pol:
        if (l > 0):
            pol2.append("Positive")
        elif (l < 0):
            pol2.append("Negative")
        else:
            pol2.append("Neutral")
    df['roundoff'] = pol2
    df = df[df.sentiment != 0]
    return df


def pretty_txt(input_value):
    input_value = input_value.replace(" ", "")
    input_value = input_value.replace("-", "")
    input_value = input_value.replace("[^a-zA-Z#]", " ")
    return (input_value)
