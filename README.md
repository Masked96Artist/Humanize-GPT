# Humanize-GPT

Now, as more and more internet posts are created with its help, various sites use complex analytical tools to distinguish the text created with AI, such as GPT. With this program, there is a solution to the bothersome question of how to make texts written by an AI sound more natural and less obviously produced by a machine. The tool employed from the NLP natural language processing incorporates techniques such as synonym substitution as well as alteration of the word order in the sentences. This makes it easier to read while at the same time trying to retain the intended information that was passed on. Whether you are blogger, a student or an employee this tool enable you to write in a more natural way which in turn makes it difficult for content-checking systems to identify your work as AI generated work.

## Working

  - Input Reading: The program reads the content of an input text file containing the text you want to humanize.

  - Sentence Tokenization: It splits the text into individual sentences and processes each sentence separately.

  - Word Tokenization: Within each sentence, the program tokenizes the text into individual words for detailed processing.

  - Synonym Replacement: For each word, the program randomly decides (with a certain probability) whether to replace it with a synonym from the WordNet database, preserving the original meaning.

  - Sentence Reconstruction: After processing the words, the program reconstructs the sentences with the replaced words, creating a new, humanized version.

  - Line Preservation: The program maintains the original line breaks and formatting of the text to ensure the output resembles the input structure.

  - Output Writing: Finally, the humanized content is written to a specified output text file, ready for review or use.

## Modules

  - The random module is a built-in Python library that allows for random selection and number generation. In the text humanizer program, it randomly picks synonyms for words, introducing variability and making the output more human-like.

  - The Natural Language Toolkit (NLTK) is a powerful library for natural language processing in Python. It includes functions for tokenization, which the program uses to break sentences into words for processing. NLTK also ensures that necessary resources, like the Punkt tokenizer and WordNet, are available.

  - The nltk.corpus.wordnet module connects to WordNet, a lexical database that groups words into synonyms. The program uses this module to retrieve synonyms, allowing for meaningful word replacement while preserving the original message, effectively humanizing the text.

## Installation

1. Git clone
   
   ```
   git clone https://github.com/kavin-surya/Humanize-GPT.git

   cd Humanize-GPT
   ```
2. Pip Install

   ```
   pip install nltk
   ```
3. Run the Program

   ```
   python3 script.py
   ```


   ``` NOTE : Replace the location of Input and Output & The Input should be in Text File ```
