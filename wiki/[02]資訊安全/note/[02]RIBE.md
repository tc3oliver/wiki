# Efficient Revocable ID-Based Encryption with a Public Channel

---

## Encryption Scheme

![Encryption Scheme](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202111261056758.png)

1. Setup
2. Extract
3. Time key update
4. Encrypt
5. Decrypt

## Security Notions

> selective-identity attacks (sID)

不同於正常的 CCA ，因為攻擊者可以透過公開的 `Extract` 演算法獲取私鑰，所以必須允許攻擊者選擇任意 ID 產生的私鑰，這個動作叫 `private key extraction queries`, 安全概念 `IND-ID-CCA`

## IND-ID-CPA game

兩個角色

- Challenger 挑戰者
- Adversary 攻擊者

遊戲過程

1. Setup: Challenger 使用 _Setup_ 演算法產生 `params` 及 `Master key` ，攻擊者獲取公開的 `params` ，挑戰者擁有 `Master key`

2. Phase 1: 攻擊者發出 m (q1...qm) 個查詢，每個查詢(q)都使用兩個演算法

   1. _Extract_ : 挑戰者使用 _Extract_ 演算法，並將 `Did` 私鑰發送給攻擊者
   2. _Time key update_ : 挑戰者使用 _Time key update_ 演算法，輸入 `time period i` 及 `identity ID(公鑰)`，並將輸出 `TID,i` 發送給攻擊者

3. Challenge:

   1. 攻擊者選擇兩個相等長度的明文 $M_{0}$、$M_{1}$，及一個 ($ID_{*}$ , $i_{*}$)，條件是 $ID$ 在第一階段的查詢中沒被查過
   2. 挑戰者隨機選擇 `b` (0 或 1) ，對 $M_{0}$ 或 $M_{1}$ 做加密，產出 `密文 C` 作為攻擊者的挑戰

4. Phase 2: 攻擊者發出更多額外的查詢 queries $q_{m+1}{\cdots}q_{n}$，可以使用如 Phase 1 一樣的操作，條件是不能是 Challenge 階段產生的 $ID_{*}$ 及 ($ID_{*}$ , $i_{*}$)

5. Guess: 攻擊者猜測 `b'`，如果 b' = b 則代表攻擊者獲勝

攻擊者 A 贏的概率

$$ 𝐴𝑑𝑣(𝐴) = 2 * | 𝑃𝑟[𝐴𝑤𝑖𝑛𝑠] − \frac{1}{2} | $$

如果這個概率是可忽略的（negligible），那麼就說這個方案是 `IND-RID-CPA` 安全的

## IND-RID-CCA

兩個角色

- Challenger 挑戰者
- Adversary 攻擊者

遊戲過程

1. Setup: Challenger 使用 _Setup_ 演算法產生 `params` 及 `Master key` ，攻擊者獲取公開的 `params` ，挑戰者擁有 `Master key`

2. Phase 1: 攻擊者發出 m (q1...qm) 個查詢，每個查詢(q)都使用兩個演算法

   1. _Extract_ : 攻擊者選擇(ID)，挑戰者使用 _Extract_ 演算法，並將 `Did` 私鑰發送給攻擊者
   2. _Time key update_ : 攻擊者選擇(ID, i)，挑戰者使用 _Time key update_ 演算法，輸入 `time period i` 及 `identity ID(公鑰)`，並將輸出 `TID,i` 發送給攻擊者
   3. _Decrypt_ : 攻擊者選擇(ID, i, C)，挑戰者使用 _Decrypt_ 演算法，將 密文 C 解密，並將解密後的`明文 D(DID,i, C)`發送給攻擊者(**_差異_**)

3. Challenge:

   1. 攻擊者選擇兩個相等長度的明文 $M_{0}$、$M_{1}$，及一個 ($ID_{*}$ , $i_{*}$)，條件是 ID 在第一階段的查詢中沒被查過
   2. 挑戰者隨機選擇 `b` (0 或 1) ，對 $M_{0}$ 或 $M_{1}$ 做加密，產出 `密文 C` 作為攻擊者的挑戰

4. Phase 2: 攻擊者發出更多額外的查詢 queries $q_{m+1}{\cdots}q_{n}$，可以使用如 Phase 1 一樣的操作，條件是不能是 Challenge 階段產生的 $ID_{*}$ 及 ($ID_{*}$ , $i_{*}$)

5. Guess: 攻擊者猜測 `b'`，如果 b' = b 則代表攻擊者獲勝

攻擊者 A 贏的概率

$$ 𝐴𝑑𝑣(𝐴) = 2 * | 𝑃𝑟[𝐴𝑤𝑖𝑛𝑠] − \frac{1}{2} | $$

如果這個概率是可忽略的（negligible），那麼就說這個方案是 `IND-RID-CCA` 安全的

## 差異

攻擊者可不可以執行 解密演算法

## 注意事項

![Q1](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202111261157195.png)

攻擊者不能同時查詢 initial key extract query on ID∗ 及 a time key update query on (ID∗, i∗)，因為這樣攻擊者就可以拿到完整的解密私鑰 `Did`

- 查詢 (ID∗, i∗) 模擬外部用戶
- 查詢 ID∗ 模擬被撤銷的用戶

## References

- Efficient Revocable ID-Based Encryption with a Public Channel
- [Security Notions for Identity Based Encryption](https://eprint.iacr.org/2005/253.pdf)
- [Boneh-Franklin Identity Based Encryption Scheme](https://slideplayer.com/slide/13288472/)
