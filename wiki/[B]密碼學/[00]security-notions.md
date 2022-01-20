# Security Notions

tags: `cryptography`

## Quick Look

---

**Link** :

1. [2001] Identity-Based Encryption from the Weil Pairing
2. [2012] Efficient revocable ID-based encryption with a public channel
3. [2007] General and Efficient Certificateless Public Key Encryption Constructions
4. [2015] Revocable Certificateless Public Key Encryption

**TLDR** : 透過四篇論文學習加密的安全性

---

## 安全概念

> **Security Notions = goals + attacks**

要確認一個密碼系統是否安全，需要說明系統針對誰安全或其安全原理

- 攻擊模型
- 安全目標

安全概念(Security notions)就是`安全目標`與`攻擊模型`的組合。

如果在給定模型下任何攻擊者都無法實現其安全目標，則我們的密碼戲通可以聲稱達到 `goals`-`attacks` 安全概念的要求，如 `IND-CCA` 。

## 攻擊模型

攻擊模型也可以稱為安全模型是一種假設，假設密碼系統的參與者一定存在攻擊者，而攻擊者所具備哪些能力。

- 攻擊者可以如何與密碼算法交互
- 攻擊者可以做什麼和不能做什麼

> _Remember that all models are wrong; the practical question is how wrong do they have to be to not be useful. —— 英國統計學家 George E. P. Box_

攻擊模型不需要完全符合實際情況；它們是一個近似值。正如統計學家 George E.P.Box 所說，"所有模型都是錯誤的。實際的問題是它們要錯到什麼程度才會沒法用。"

攻擊者 A 贏的概率

```python
𝐴𝑑𝑣(𝐴)=2∗|𝑃𝑟[𝐴𝑤𝑖𝑛𝑠]−1/2|
```

如果這個概率是可忽略的（negligible），那麼就說這個方案是 `goals`-`attacks` 安全的

### Kerckhoff's principle

所有模型中都有的一個假設就是所謂的 Kerckhoffs 原則，要求密碼系統的安全性不能依賴於算法的保密性，而只能依賴於密鑰的保密性。

### 主要的四種攻擊方式

1. 唯密文攻擊（Ciphtext Only Attack，COA）

   攻擊者通過同一密鑰加密的密文,恢復出明文或者密鑰

2. 已知明文攻擊（Known Plaintext Attack，KPA）

   攻擊者通過同一密鑰加密的明文/密文對,恢復出其他密文的明文或者密鑰

3. 選擇明文攻擊（Chosen Plaintext Attack，CPA）

   攻擊方的目的是識別出密文 `C` 中加密的是 `m0` 還是 `m1` 。其中的假設是攻擊者可以**選擇任意的明文讓（加密方）加密並能得到相應的密文**。

   選擇明文攻擊的經典例子來自二戰。日軍在珊瑚海戰後即將中途島確定為下一個攻擊目標，美海軍情報局由於破譯了日軍部分密碼，瞭解到了這一計劃，但是具體攻擊目標未能成功破譯(日軍密電中稱為'AF')，綜合其他因素推斷也不能明確，一部分人認為是中途島，另一部分人則認為是阿留申群島。後來，美軍想到一個絕妙的主意，他們通過無線電向珍珠港報告，說中途島上的海水淨化裝置故障導致島上缺水，不久從日軍截獲的密電中即出現了'AF'缺水的內容，從而明確了日軍目標即中途島。

4. 選擇密文攻擊（Chosen Ciphertext Attack，CCA）

   攻擊方的目的是識別出密文 `C` 中加密的是 `m0` 還是 `m1` 。其中的假設是攻擊者可以**選擇任意的密文並能得到相應的明文**。

## 安全目標

| English              | 中文       | 縮寫 |
| -------------------- | ---------- | ---- |
| Semantic security    | 語義安全性 | SS   |
| Indistinguishability | 不可區分性 | IND  |
| non-malleability     | 不可延展性 | NM   |

## IBE

> selective-identity attacks (sID)

不同於正常的 CCA ，因為攻擊者可以透過公開的 `Extract` 演算法獲取私鑰，所以必須允許攻擊者選擇任意 ID 產生的私鑰，這個動作叫 `private key extraction queries`, 安全概念 `IND-ID-CCA`

## 問題

- Q: 不理解 `語義安全性` 的目標是什麼，有些文章說 IND-CPA = SS
- Q: polynomially bounded (有界多項式的)
- Q: PPT adversary (Probabilistic Polynomial-Time Adversaries)

---

## References

- [Security Notions for Identity Based Encryption](https://eprint.iacr.org/2005/253.pdf)
- [密碼系統的安全性](https://www.cnblogs.com/xdyixia/p/11610091.html)
- [Easy explanation of "IND-" security notions?](https://crypto.stackexchange.com/questions/26689/easy-explanation-of-ind-security-notions)
- [誰能幫我解釋下“明文攻擊”的方法大概是什麼？](https://zhidao.baidu.com/question/590447598.html?qbl=relate_question_0)
- [Attack models in cryptography](https://xianmu.github.io/posts/2017-06-30-attack-models-in-cryptography.html)
- [密碼學小知識(5)：唯密文攻擊(COA)、已知明文攻擊(KPA)、選擇明文攻擊(CPA)，選擇密文攻擊(CCA)](https://blog.csdn.net/A33280000f/article/details/118304531?spm=1001.2101.3001.6650.14&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-14.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-14.no_search_link)
