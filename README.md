# Citation network

You can find our presentation from 27.10.2018 [here](https://drive.google.com/file/d/1leR89wB3OM3DSVMla8p6JeDPkKp1My1Z/view?usp=sharing)

## Part 1: getting data

[1](/images/zlevels_by_between_labelsize_by_indegree.png)

**[Here](/codes) you can find two Python-3 codes, which extract all references from a collection of articles and make extracted material ready for Gephy.**

> Codes require `bs4` module.
> You can get it using `pip install beutifulsoup4`.

We tried using two collections.

* The [`final_dialogue.py`](/codes/final_dialogue.py)
uses a collection of articles from [Dialogue conference](http://www.dialog-21.ru/).
It consists of 1748 articles in Russian and English, mostly in PDF format.

> It requires one more module: `PyPDF2`. You can also get it with `pip install`.
> So far, Russian PDF-files can't be read **at all** (*pyPDF2 is really bad at it*).

Due to some technical problems we were not able to get the citations from this collection, so we tried another one. In the future we may try using an existing Dialogue dataset.

* The [`final_cambridge.py`](/codes/final_cambridge.py)
uses a collection of articles from [Journal of Linguistics](https://www.cambridge.org/core/journals/journal-of-linguistics).
It consists of 934 articles in English from the [Most cited](https://www.cambridge.org/core/journals/journal-of-linguistics/most-cited) section.

***

### Progress for each collection

#### Dialogue

step|status
:---|:---
Crawler| done
Get/download articles| done
Get English texts from PDF-files| done
Get Russian texts from PDF-files| *is it even possible?*
Get all citations| NO
Output data in right format|in theory
User-friendly interface| almost

**FAIL**

#### Journal of Linguistics

step|status
:---|:---
Crawler| done
Get/download articles| done
Get all citations| done
Get authors' surnames right|almost
Output data in right format| done
User-friendly interface| done

**SUCCESS**

## Part 2: data managment

In the data we got from the previous step some autors' names were presented in different ways. Unfortunately, we couldn't get them all to  the same format, but we manually corrected some of them (see [a list of corrected authors](/output/list.txt)).

The final version of the ready-for-Gephi .csv file can be founf [here](/output/output_data_cambr_final.csv).

## Part 3: networks in Gephi

### Full data

The graph we got consisted of 20408 nodes (= authors) and about 60000 edges (= instances of referencing). 

We arranges and scaled the nodes by their in-degree (= by how many authors a certain person was referenced) and got the following graph, showing Noam Chomsky to be "the most popular" (he was referenced by 298 out of 948 authors, that's about third of them!)
![](/images/chomsky.png)

Well, we decided to delete Noam Chomsky from our network :)

However, this network was still too big to be analysed, so we filetered out some nodes:

+ "unpopular authors" - nodes, which in-degree was less than 20. Why 20? That allowed us to make the graph much smaller without losing too much relevant data, see:
![](/images/in-degree.png)

+ "short papers" - nodes, wich out-degree was less than 100. Why 100? Same answer as before, see:
![](/images/out-degree.png)

### Filetered out

Than we used the sandart clusterising function to get this:
![](/images/clusters.png)
*label size represents the in-degree, node size represents betweenness centrality*

As you can see, there are 7 main clusters.

## Analysing clusters

![](/colors/blue.png) Comparative linguistics
![](/colors/cyan.png) Syntax
![](/colors/light-green.png) Specialising in English (grammar mostly)
![](/colors/orange.png) Sociolinguistics & morphology (really mixed one, we think it shlould be sub-clusterised)
![](/colors/magenta.png) Typology
![](/colors/pink.png) Speech analysis and phonology
![](/colors/red.png) Specialising in Japanese & Oceanic syntax (in is questionable, whether A.M. Zwicky and G.K. Pullum soild be here)
> Im my opinion, they should be also deleted from this network at all (C) Anna Polyanskaya
![](/colors/dark-green.png) Morphology
![](/colors/grey.png) A very small and very specific cluster of two Canadian linguists from Quebec: Carole Paradis and Darlene Lacharité

However, this clusters are not comletely "clean": they are also affected by authors' region of origin and region of interest.

## Short note on centrality

Here you can see an unclusterised network of the same authors. Node size represents betweenness centrality, lable size and redness *(brightness of the red, to be percise)* represent closeness centrality. 

![](/images/centrality.png)

This information is to be analysed in the future.

## Conclusion

This method allowes us to:
+ find out most cited authors *(most important for linguists of any field of work)*
+ authomaticlly clusterise linguists by the field of their research *( it is still a WIP, but it does show some relevant results)*
+ establish reception of ideas in linguistic papers and see how those ideas came to be *(by analysing betweenness and closeness centrality)*

## Further work

## and a meme for y'all
![Source]

Noam Chomsky in linguistic world (oil, canvas). [Source].


[Source]: https://memepedia.ru/wp-content/uploads/2018/02/%D0%BC%D0%B0%D1%80%D0%B8%D0%BE%D0%BD%D0%B5%D1%82%D0%BA%D0%B8.jpg



*Presentation by Olga Vedenina*

*Output data mangment and presentation by Elizaveta Leonova*

*Code and presentation by [Alina Morse](http://vk.com/crtcldstnc) & [Anna Polyanskaya](http://vk.com/aglade)*

Feel free to contact [Anna](off.polyanskaya.a@gmail.com) for any questions.

HSE, 2018
