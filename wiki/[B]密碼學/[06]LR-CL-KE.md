# LR-CL-KE

## Quick Look

---

**Link** :

1. [2018] Leakage-Resilient Certificateless Key Encapsulation Scheme

**TLDR** : 防洩漏無證書密鑰封裝方案

---

## Framework of LR-CL-KE Schem

1. _Setup_
   - 輸入: security parameter
   - 輸出:
     1. the first system secret key ($SK_{0, 1}$,$SK_{0, 2}$)
     2. the public parameters PP
2. _Initial key extract_

   - 輸入: i-th user with identity $ID$
   - 輸出: the first initial key ($DID_0$,$QID$)

     This algorithm consists of two sub-algorithms **Extract-1** and **Extract-2** defined below, in which the current system secret key ($SK_{i−1,1}$,$SK_{i−1,2}$) is used and is updated to ($SK_{i,1}$,$SK{i,2}$).

     1. Extract-1  
        Given a random number $γ$ ,$SK_{i−1,1}$ and the user’s identity $ID$, this subalgorithm generates $QID$ and temporary information $TI_{IE}$, and updates $SK_{i−1,1}$ to $SK_{i,1}$.
     2. Extract-2  
        Given $TI_{IE}$, and $SK_{i−1,2}$, this sub-algorithm generates $DID_0$ and updates $SK_{i−1,2}$ to $SK_{i,2}$

3. _Set secret value_

   - 輸入: performed by a user with identity $ID$
   - 輸出:
     1. the user’s secret key $SID_0$
     2. the partial public key $RID$

4. _Set private key_

   - 輸入:
     1. performed by a user with identity $ID$
     2. the first initial key ($DID_0$,$QID$)
     3. secret key $SID_0$
   - 輸出: private key (($DID_{0,1}$,$DID_{0,2}$), ($SID_{0,1}$,$SID_{0,2}$))

5. _Set public key_

   - 輸入:
     1. performed by a user with identity $ID$
     2. initial key ($DID_0$,$QID$)
     3. partial public key $RID$
   - 輸出: public key $PID = (QID,RID)$

6. _Encrypt_

   - 輸入:
     1. plain-message $msg$
     2. public key $PID = (QID,RID)$
   - 輸出:
     1. random value $C$
     2. encryption key $K$, $CT = E_K(msg)$
     3. $(C,CT)$ is sent to the receiver.

7. _Decrypt_
   - 輸入: private key (($DID_{0,1}$,$DID_{0,2}$), ($SID_{0,1}$,$SID_{0,2}$))
   - 輸出: This algorithm consists of two sub-algorithms Decrypt-1 and Decrypt-2, run by a receiver.
     1. Decrypt-1: Given $DID_{j−1,1}$and $SID_{j−1,1}$, this algorithm outputs $DID_{j,1}$, $SID_{j,1}$ and the temporary information $TI_D$
     2. Decrypt-2: Given $C,\ CT,\ TID,\ DID_{j−1,2},\ SID_{j−1,2}$, this algorithm generates $DID_{j,2}$ and $SID_{j,2}$ while obtaining the encryption key $K$. Finally, the receiver can obtain the plain message $msg$ by $D_K(CT)$ using the decryption function $D()$ of a symmetric cryptosystem

- system secret key ($SK_{0, 1}$,$SK_{0, 2}$)
- the public parameters PP
- initial key ($DID_0$,$QID$)
- user’s secret key $SID_0$
- private key (($DID_{0,1}$,$DID_{0,2}$), ($SID_{0,1}$,$SID_{0,2}$))
- public key $PID = (QID,RID)$
