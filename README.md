## Inspiration
Depression has become **increasingly common** among teenagers – especially teen girls, who are now almost three times as likely as teen boys to have had recent experiences with depression.
One-in-five teenage girls – or **nearly 2.4 million** – had experienced at least one major depressive episode over the past year in 2017. By comparison, **7% of teenage boys** (or 845,000) had at least one **major depressive episode** in the past 12 months.
The total number of teenagers who recently experienced depression increased by 59% between 2007 and 2017. The rate of growth was faster for teen girls (66%) than for boys (44%).
![Graph depicting the rise in depression](http://cdn.statcdn.com/Infographic/images/normal/20052.jpeg)

## Symptoms
### 1. Emotional changes
- Feelings of sadness, which can include crying spells for no apparent reason
- Frustration or feelings of anger, even over small matters
- Feeling hopeless or empty
- Irritable or annoyed mood
- Loss of interest or pleasure in usual activities
- Loss of interest in, or conflict with, family and friends
- Low self-esteem
- Feelings of worthlessness or guilt
- Fixation on past failures or exaggerated self-blame or self-criticism
- Extreme sensitivity to rejection or failure, and the need for excessive reassurance
- Trouble thinking, concentrating, making decisions, and remembering things
- Ongoing sense that life and the future are grim and bleak
- Frequent thoughts of death, dying, or suicide

### 2. Behavioral changes
- Tiredness and loss of energy
- Insomnia or sleeping too much
- Changes in appetite — decreased appetite and weight loss, or increased cravings for food and weight gain
- Use of alcohol or drugs
- Agitation or restlessness — for example, pacing, hand-wringing or an inability to sit still
- Slowed thinking, speaking or body movements
- Frequent complaints of unexplained body aches and headaches, which may include frequent visits to the school nurse
- Social isolation
- Poor school performance or frequent absences from school
- Less attention to personal hygiene or appearance
- Angry outbursts, disruptive or risky behavior, or other acting-out behaviors
- Self-harm — for example, cutting, burning, or excessive piercing or tattooing
- Making a suicide plan or a suicide attempt

## What it does
It is very hard for youth in third-world countries to open up about depression or their mental state. So we created an algorithm that can **analyze if the user is depressed/suicidal** or **on the verge of depression** using his/her **day-to-day chat conversations**. The algorithm after analysis suggests the user **remedies to lighten/brighten up** the latter’s mood and **prevent depression**. The algo has **multilingual support**, which means you can analyze the mood of a **french/Japanese person** too.
The algorithm is **very easy to use** and can be **embedded in any chat app using Graphql API**. Moreover, **no user data is stored anywhere on the server**. The data is only used to understand the user’s sentiment and suggest the latter remedies accordingly. 

## How we built it
- Django Server: Cloud server based on python to process all the input chat data and suggest remedies accordingly.
- Language Corpus: We use NLTK, iNLTK, and Google databases for different language corpora.
- Heroku: To deploy the server container.
- Google Cloud: To deploy the website. 
- Javascript: Interface to showcase how it works.
- GraphQL: To build a stable API for public release.
- Google PostgreSQL: Database service to temporarily store users' chat records and analyze the data.

## Accomplishments that we're proud of
- The mood analysis and remedy suggestion algorithm is very accurate with an **accuracy score of 87%**.
- The algorithm works with many languages like English, Spanish, Hindi, Japanese, French etc.
- The Graphql API is very stable, efficient and can be used in any project or chat app.

## Challenges we ran into and what we learned
- It was very difficult for us to process languages other than English as the language corpora data is very limited for other languages.
- We learned a lot about Natural Language Processing and Sentiment Analysis in this project. It was our first time working with multi-language support.

## What's next for iHear
- We wish to collaborate with many doctors/therapists to build a more accurate analysis model and bring better suggestions to users.

## References
- https://www.webmd.com/depression/guide/teen-depression
- https://www.pewresearch.org/fact-tank/2019/07/12/a-growing-number-of-american-teenagers-particularly-girls-are-facing-depression/

## Collaborators
- [Harmanjit Singh](https://github.com/harmanjit14)
- [Manya Thaur](https://github.com/manya1712)
- [Mahira Moody](https://github.com/Mahiramodi)
