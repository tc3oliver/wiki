# Transformer

論文： [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

在2017年，Google AI團隊發表了一篇題為「Attention Is All You Need」的論文，該論文介紹了一種稱為Transformer的模型架構，並將自注意力機制（self-attention mechanism）作為其核心組件，用於處理序列到序列的任務。Transformer透過自注意力機制的應用，能夠同時捕捉序列中每個詞與其他所有詞之間的相互關係，這使得模型能夠更全面、靈活地理解輸入序列的內容和長距離相依性。

在自然語言處理任務中，Transformer模型展現出卓越的表現，如在機器翻譯、語言模型和文本生成等領域取得了顯著成果。這一模型的引入對於自然語言處理領域產生了重要影響，其自注意力機制的應用開創了序列建模的新方向，啟發了後續眾多基於注意力機制的模型，例如BERT和GPT-3等。Transformer的革新性設計和卓越性能使其成為當代自然語言處理領域不可忽視的重要里程碑，值得深入研究和廣泛討論。

## Attention Is All You Need

- 關鍵技術: 自注意力機制(self-attention mechanism)
- 輸入: Transformer 模型的輸入是兩個平行的序列:源序列和目標序列。模型基於此生成目標序列的翻譯或重構。
- 輸出: Transformer 模型的輸出更精確的說是根據源序列生成的目標序列翻譯或重構。
- 損失函數: Transformer 模型通常使用的損失函數是交叉熵損失,用於衡量模型輸出的目標序列與真實目標序列的差異。
- 貢獻: 「Attention Is All You Need」是自然語言處理領域具有里程碑意義的工作,它提出了一種開創性的模型架構 Transformer,並在各種任務上實現最優的效果。Transformer 的提出對 NLP 領域產生了深遠影響,值得深入研究和探討。
