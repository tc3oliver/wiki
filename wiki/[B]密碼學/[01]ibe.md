# Identity-Based Encryption from the Weil Pairing

---

## Encryption Scheme

![Encryption Scheme](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202111260928361.png)

1. Setup
2. Extract
3. Encrypt
4. Decrypt

## Security Notions

> selective-identity attacks (sID)

不同於正常的 CCA ，因為攻擊者可以透過公開的 `Extract` 演算法獲取私鑰，所以必須允許攻擊者選擇任意 ID 產生的私鑰，這個動作叫 `private key extraction queries`, 安全概念 `IND-ID-CCA`

## IND-ID-CCA game

兩個角色

- Challenger 挑戰者
- Adversary 攻擊者

遊戲過程

1. Setup: Challenger 使用 _Setup_ 演算法產生 **`params`** 及 **`Master key`**，攻擊者獲取公開的 **`params`** ，挑戰者擁有 **`Master key`**

2. Phase 1: 攻擊者發出 m (q1...qm) 個查詢，每個查詢(qi)都使用兩個演算法

   1. _Extract_ : 攻擊者選擇(IDi)，挑戰者使用 _Extract_ 演算法，並將 `Did` 私鑰發送給攻擊者
   2. _Decrypt_ : 攻擊者選擇(IDi, Ci)，挑戰者使用 _Decrypt_ 演算法，將 密文 Ci 解密，並將解密後的`明文`發送給攻擊者

3. Challenge:

   1. 攻擊者選擇兩個相等長度的明文 `M0`, `M1`，及一個 `user ID (公鑰)` ，條件是 ID 在第一階段的查詢中沒被查過
   2. 挑戰者隨機選擇 `b` (0 或 1) ，對 `M0` 或 `M1` 做加密，產出 `密文 C` 作為攻擊者的挑戰

4. Phase 2: 攻擊者發出更多額外的查詢 queries `qm+1...qn`，可以使用如 Phase 1 一樣的操作，條件是不能是 Challenge 階段產生的 ID, C

5. Guess: 攻擊者猜測 `b'`，如果 b' = b 則代表攻擊者獲勝

攻擊者 A 贏的概率

```latex
𝐴𝑑𝑣(𝐴)=2∗|𝑃𝑟[𝐴𝑤𝑖𝑛𝑠]−1/2|
```


---

## References

- [Security Notions for Identity Based Encryption](https://eprint.iacr.org/2005/253.pdf)
- [Boneh-Franklin Identity Based Encryption Scheme](https://slideplayer.com/slide/13288472/)
