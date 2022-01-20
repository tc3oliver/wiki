# Revocable Certificateless Public Key Encryption

---

## Encryption Scheme

![Encryption Scheme](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202111261305577.png)

1. System setup
2. Initial key extract
3. Time key update
4. Set secret value
5. Set public key
6. Set private key
7. Encryption
8. Decryption

## Security Notions

## RCL-IND-CCA game

### 六個查詢

1. Public-key retrieve query (ID)
2. Public-key replace query (ID, PK'ID)
3. Initial key extract query (ID)
4. Time key update query (ID, t)
5. Secret value extract query (ID)
6. Decryption query (ID, t, C)

### 四個角色

- Challenger 挑戰者
- Type I Adversary 攻擊者 1

  1. 不是系統的成員
  2. 可以從公共參數取任意身份的 `time update keys`
  3. 可以使用上面 6 個查詢

- Type II Adversary 攻擊者 2

  1. the honest-but-curious KGC(不懂)
  2. 知道 `system secret key s`
  3. 知道 `time update key`

- Type III Adversary 攻擊者 3

  1. 被撤銷的用戶
  2. 知道 `system secret key s`
  3. 不能取得最新的 `time update key`

### 遊戲過程

1. 攻擊者 A I 與 A II

   - A I 沒有透過 KGC 取得 master key(public key replacement attack)
   - A II 有透過 KGC 取得 master key(chosen ciphertext attack)

2. Setup: Challenger 使用 _Setup_ 演算法產生 `params` 及 `secret key s` ，所有攻擊者獲取公開的 `params`

3. A I 要求 partial key extract queries

---

1. Setup: Challenger 使用 _Setup_ 演算法產生 `params` 及 `secret key s` ，所有攻擊者獲取公開的 `params` ，挑戰者擁有 `secret key s`，並提供給，攻擊者 2

2. Phase 1: 攻擊者可以使用前面的六個查詢

   - 如果是 攻擊者 2 可以自己算 initial secret 及 time update keys(自己算跟使用查詢差在哪)

3. Challenge:

   - 攻擊者選擇 `identity ID∗`, `plaintext pair (m∗0, m∗1)`, 以及 `time period t∗`，針對不同攻擊者有些限制:

     1. 攻擊者 1 identity ID∗ 不允許在 Phase 1 `initial key extract query` 查過
     2. 攻擊者 2 identity ID∗ 不允許在 Phase 1 `secret value extract` 及 `public-key replace queries` 查過
     3. 攻擊者 3 (ID∗, t∗) 不允許在 Phase 1 `time key update query` 查過

   - 挑戰者隨機選擇 `b` (0 或 1) ，對 `M0` 或 `M1` 做加密，產出 `密文 C` 作為攻擊者的挑戰

4. Phase 2: 攻擊者發出更多額外的查詢，可以使用如 Phase 1 一樣的操作，條件是不能是 Phase 1 及 Challenge 階段產生參數
5. Guess: 攻擊者猜測 `b'`，如果 b' = b 則代表攻擊者獲勝

攻擊者 A 贏的概率

```python
𝐴𝑑𝑣(𝐴)=2∗|𝑃𝑟[𝐴𝑤𝑖𝑛𝑠]−1/2|
```

如果這個概率是可忽略的（negligible），那麼就說這個方案是 `RCL-IND-CCA` 安全的
