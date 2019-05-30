# BIP39 GUI

After completing Jimmy Song's programming blockchain course I decided it would be a good learning experience to try and write my own implimentation of BIP-32 and BIP-39 from scratch using the documentation only.  With a few exceptions where I really hit a wall this is all my own code- excluding the ECDSA and bech32/p2pkh address generation functions that I took from the programming blockchain code and Peter Wuille's bech32 example.  My intention is to do the same with these parts of the code at a later date.  

Whilst doing this and experimenting with the transaction creation parts of the programming blockchain code I found it quite frustrating trying to find an easy-to-navigate source for test vectors covering all address types in testnet and mainnet I could use for evaluating my work.  This project is intended to provide a user friendly solution for future students and also to practice creating Qt Gui apps. 

## DEPENDENCIES
Tested with python version 3.6

```
PyQt5
pbkdf2
ecdsa
```

## FEATURES
![Screenshot](https://i.imgur.com/EORcZbE.png)

--Selection options for 3-24 words (simply putting the space separated words in the first word box will also work) along with a bip39 passphrase

--User input for total number of addresses desired

--Creation of P2PKH, P2SH, P2WPKH and P2WSH addresses along with xpiv and xpub as per BIP32 spec, using a word list as the starting point following the BIP39 standard.  

--Presets for BIP44, BIP49, BIP84 and BIP141 standards, along with custom user input for derivation path

--Option for Hardened or non-hardened addresses

--Option for Testnet private and public keys

--Output containing derivation path, private key in WIF, integer and hex format, public key address, public point on curve and 
scriptpubkey

--Results are output in a file titled 'wallet.txt' with the time addresses were generated, along with all information presented    
onscreen 

## ISSUES

This has not been tested with any other wordlist except the standard english version

This is intended as an educational tool and a portfolio project.  It's use on mainnet is not encouraged and is done so at your own risk.  

