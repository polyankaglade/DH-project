# DH-project
**[Here](/codes) you can find two Python-3 codes, which extract all references from a collection of articles and make extracted material ready for Gephy.**

If you don't want to deal with Python, you can use theese [ready-for-Gephi .csv files](/output).

> Codes require `bs4` module.
> You can get it using `pip install beutifulsoup4`.

We are currently using two collections.

* The [`final_dialogue.py`](/codes/final_dialogue.py)
uses a collection of articles from [Dialogue conference](http://www.dialog-21.ru/).
It consists of 1748 articles in Russian and English, mostly in ~~FUCKING~~ PDF format.

> It requires one more module: `PyPDF2`. You can also get it with `pip install`.
> So far, Russian PDF-files can't be read **at all** (*pyPDF2 is really bad at it*).

* The [`final_cambridge.py`](/codes/final_cambridge.py)
uses a collection of articles from [Journal of Linguistics](https://www.cambridge.org/core/journals/journal-of-linguistics).
It consists of 934 articles in English from the [Most cited](https://www.cambridge.org/core/journals/journal-of-linguistics/most-cited) section.

*Visualisation by [Olga Vedenina]()
*Code written by [Alina Morse](http://vk.com/crtcldstnc) & [Anna Polyanskaya](http://vk.com/aglade)*


HSE, 2018

***

# Progress so far

## Dialogue

step|status
:---|:---
Crawler| done
Get/download articles| done
Get English texts from PDF-files| done
Get Russian texts from PDF-files| *is it even possible?*
Get all citations| NO
Output data in right format|in theory
User-friendly interface| almost

## Journal of Linguistics

step|status
:---|:---
Crawler| done
Get/download articles| done
Get all citations| done
Get authors' surnames right|almost
Output data in right format| done
User-friendly interface| done

look!
![](/images/first_try.png)
