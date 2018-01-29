# GroupMe Mimic

## Markov chaining your GroupMe friends history

Generates a bot capable of mimicking a GroupMe friend's language based on their history in a specific chat.

### Getting Started

1. Clone the repository
2. In groupme-mimic/settings.json, define your bot parameters
    ```{
    "token": "" // enter token name,
    "group_name": "" // enter group chat name,
    "user_name": "" // enter username from that group,
    "bot_name": "" // give bot a name,
    "frequency_per_day": 4 // number of times to post a day
    }```
3. `$ groupme-mimic/register.py`
4. `$ groupme-mimic/script.py`
5. Deploy to a web server to run indefinitely!
### GroupMe Scraping

Provided the following parameters, the scraper is capable over reviewing many thousands of messages to compile a full history of the friend:
- GroupMe access token (found on GroupMe Dev)
- Groupchat ID
- User ID of the friend

Other options for tweaking the scraper include message count, message limit, filenames and pathnames.
The scraper will compile all the messages into 'novel' format, where each message follows the next with correct punctuation, making it more readable for the modeling mechanism.

### Markov Chaining

The modeling process takes each sentence of the message history file and generates a large Markov chain, built in a python dictionary. A Markov chain is a stochastic model that predicts the next event soley based on the previous event. Each word associates with many words which come after it, such as the following:
- 'red' -> 'apple'
- 'how' -> 'do' -> 'I'
- 'markov' -> 'chain'

Each following word is given a likelihood, based on the number of times it occurs after the previous word in the friend's messaging history.
We train the Markov model using the full messaging history we just scraped off GroupMe and use that in prediction.

### Prediction

We start at one of the many words that occur at the beginning of sentences (indicated by the state 'START') and end at one of the many words which end sentences (indicated by the state 'END'). At each iteration, we randomly choose the next word based on which words commonly follow the previous and their frequencies. The resulting sentences is a somewhat accurate depiction of the friend's historical language.


