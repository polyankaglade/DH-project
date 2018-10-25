# DH-project
**Here you can find two Python-3 codes, which extract all references from a collection of articles and make extracted material ready for Gephy.**

We are currently using two collections.

* The [`final_dialogue.py`](/codes/final_dialogue.py)
uses a collection of articles from [Dialogue conference](http://www.dialog-21.ru/).
It consists of 1748 articles in Russian and English, mostly in FUCKING PDF format.

> So far, Russian PDF-files can't be read **at all** (*pyPDF2 is really bad at it*).

* The [`final_cambridge.py`](/codes/final_cambridge.py)
uses a collection of articles from [Journal of Linguistics](https://www.cambridge.org/core/journals/journal-of-linguistics).
It consists of 934 articles in English from the [Most cited](https://www.cambridge.org/core/journals/journal-of-linguistics/most-cited) section.

*Code written by [Alina Morse](), [Olga Vedenina]() & [Anna Polyanskaya](vk.com/aglade)*

~*Code written mostly by [Anna Polyanskaya](vk.com/aglade), except fot some inner parts:*~

~*`create_data()` written by [Other lady 1]()*~

~*`get_authors()` written by [Other lady 2]()*~

~*`get_citations(text)` written by [Other lady 3]()*~


HSE, 2018
___

# Progress so far

## Dialogue

step|status
:---|:---
Crawler| done
Get/download articles| done
Get English texts from PDF-files| done
Get Russian texts from PDF-files| *is it even possible?*
Get all citations| NO
Output data in right format| NO
User-friendly interface| almost

## Journal of Linguistics

step|status
:---|:---
Crawler| done
Get/download articles| done
Get all citations| done
Output data in right format| NO
User-friendly interface| almost
