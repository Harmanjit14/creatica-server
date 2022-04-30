from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from .translation import translate
import random
# function to print sentiments
# of the sentence.

verge = [
    'Exercise',
    'Sleep and Relax',
    'Spend more time with people you Love',
    'Try Dancing',
    'Try Sports',
]

gloomy = [
    'Eat comfort food',
    'Have fresh air',
    'Listen to new music',
    'Take a break',
    'Relive your childhood memories',
]

depression = [
    'Talk your heart out and contact a therapist',
    'Accomplish a small goal',
    'Challenge your negative thoughts',
    'Try zentangling:- form of doodling to reduce stress',
    'Meditate',
]


def sentiment_scores(sentence):

    sentence = translate(sentence)

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    val = sentiment_dict['compound']
    rand = random.sample(range(0, 5), 2)

    # print( gloomy[rand[0]])
    print(rand)
    if val > -0.10 and val < -0.05:
        a = gloomy[rand[0]]
        b = gloomy[rand[1]]
        return f"The User might be gloomy! @ {a} @ {b}"
    elif val < -0.10 and val > -0.2:
        a = verge[rand[0]]
        b = verge[rand[1]]
        return f"The User might be on the verge of depression! @ {a} @ {b}"
    elif val < -0.02 and val > -0.59:
        a = depression[rand[0]]
        b = depression[rand[1]]
        return f"The User might be depressed! @ {a} @ {b}"
    elif val < -0.59:
        return f"The User might be sucidal! @ Contact national suicide helpline @ Call a concerned speacialist"
    else:
        return f"User seems to be normal!"

    return "none"
