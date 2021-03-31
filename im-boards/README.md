# im-boards

## Motivation
This project was motivated by the Commander-in-Chief's statement regarding the Philippine oligarchy:
<p align="center">
<a href="http://www.youtube.com/watch?v=0btAPWEA_Cs&t=51s">
<img src="http://img.youtube.com/vi/0btAPWEA_Cs/0.jpg" alt="I dismantled the oligarchy that controlled PH economy"/></a></p>

## PSE Board/Director Overlap
This project aimed to determine whether the said oligarchy exists based on board overlap among companies in the Philippine Stock Exchange.

## Methodology
1. Data was gathered by scraping management data from the PSE using my PSE API.
2. A graph representation was generated using Gephi with each Board Member/Director pointing to respective companies.
3. Each node was scaled according to out-degree and colored according to modularity class.
4. To better visualize the graph, Yifan Hu Proportional and Noverlap were performed.
5. The resulting graph can be seen below or [accessed here]().

<p align="center">
<img src="https://github.com/kgreyy/stonks-miniprojects/blob/master/PSE Board Director Overlap.JPG?raw=true" alt="Graph of PSE Board Director Overlap"/>
</p>
