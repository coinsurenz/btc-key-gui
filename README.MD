# BTC KEY GUI

After completing Jimmy Song's "Programming Blockchain" course I decided it would be a good learning experience to try and write my own implimentation of BIP-32 and BIP-39 from scratch using the documentation only.  With a few exceptions where I really hit a wall this is all my own code- excluding the ECDSA and bech32/p2pkh address generation functions that I took from the programming blockchain code and Peter Wuille's bech32 example.  My intention is to do the same with these parts of the code at a later date.

Whilst doing this and experimenting with the transaction creation parts of the programming blockchain code I found it quite frustrating trying to find an easy-to-navigate source for test vectors covering all address types in testnet and mainnet I could use for evaluating my work.  This project is intended to provide a user friendly solution for future students and also to practice creating Qt Gui apps. 

## DEPENDENCIES
Tested with python version 3.6

```
PyQt5
pbkdf2
ecdsa
pytest

```
## USAGE
<pre>
Clone the repo with git clone

create venv in repo folder
cd btc-key-gui
source btc-key-gui/bin/activate
python3 -m venv btc-key-gui

install dependencies
pip install -r requirements.txt

run the app
python3 bip39_gui.py

Windows users-
Standalone .exe can be found in the releases section

Appimage and standalone app for Mac will be added in the near future
</pre>


## FEATURES
![Screenshot](https://i.imgur.com/EUP7qHc.png)

--Selection options for 3-24 words, along with a bip39 passphrase

--User input for total number of addresses desired

--Creation of P2PKH, P2SH, P2WPKH and P2WSH addresses along with xpiv and xpub as per BIP32 spec, using a word list as the starting point following the BIP39 standard.

--Create custom multisig addresses with up to 16 public keys and 16 signatures required

--Presets for BIP44, BIP49, BIP84 and BIP141 standards, along with custom user input for derivation path

--Option for Hardened or non-hardened addresses

--Option for Testnet private and public keys

--Output containing derivation path, private key in WIF, integer and hex format, public key address, public point on curve and scriptpubkey

--Results are output in a file titled 'data.txt' with the time addresses were generated, along with all information presented on screen 


## Usage- generating single sig addresses

* Select the number of words you wish to use
![Screenshot](https://i.imgur.com/QKtRMOh.png)

* Enter the words in the relevant boxes
![Screenshot](https://i.imgur.com/7xYZD1F.png)

* If you wish to use a passphrase check the box and enter it in the passphrase box
![Screenshot](https://i.imgur.com/Yh1c6K1.png)  

* Enter the derivation path
![Screenshot](https://i.imgur.com/bOdS4oJ.png)

* Select the address type you wish to generate- presets for bip44, bip49, bip84 will set the address type automatically
![Screenshot](https://i.imgur.com/Q9WDulq.png)

* Select if want the addresses to be hardened or not
![Screenshot](https://i.imgur.com/M5prLGi.png)

* Select testnet or mainnet
![Screenshot](https://i.imgur.com/sOgmCGh.png)

* Select whether you want to output the results to a text file or not.  If selected the results, including the seed words used will be output to a file titled data.txt in the current working directory. Further output will contine to be added to this same file when this checkbox is selected.
![Screenshot](https://i.imgur.com/z85R8A8.png)

* Select the number of addresses you wish to generate
![Screenshot](https://imgur.com/KnkwYuw.png)

* Click the OK button to generate the addresses, and click the cancel button when you wish to clear the current data displayed
![Screenshot](https://imgur.com/UvKlAfT.png)



## Usage- generating multi sig addresses
![Screenshot](https://i.imgur.com/eTtq82U.png)

This opperates differently to the single sig address generation.  We need to generate the single sig addresses first and then use those public keys to generate the multisig addresses.  This is done individually using the output of the single sig generation method above.

* First generate the single sig addresses as above or by other means.  We will need the public point that corresponds to the private key we wish to use for the multisig.

* Check the multisig box
![Screenshot](https://imgur.com/Jj1MwJr.png)

* Enter the public point in the word boxes for each of the possible signers.  For example "036889e5873ed5a78666cde9b0f623d0bde8807ecda551222e2943800b0fb1e47d" would correspond to the public key "18g5SfgpLxtFSRikqrk4wYu1WAP7A81gSS" used in the example screen shot above.
![Screenshot](https://imgur.com/jpHTMrJ.png)

* Select the threshold number of signers required to sign the transaction using the "Number of Addresses/M-sig sigs Required" spinner.  For example for a 2 of 3 multisig we would have 3 public points in the word boxes and set this spinner to 2.
![Screenshot](https://imgur.com/KnkwYuw.png)

* Select the address type you wish to generate- either p2sh or p2wsh
![Screenshot](https://imgur.com/Q9WDulq.png)

* Select the output to text file box if you wish to output the results to a text file
![Screenshot](https://imgur.com/z85R8A8.png)


* Click the OK button to generate the addresses
![Screenshot](https://imgur.com/UvKlAfT.png)


## ISSUES

This has not been tested with any other wordlist except the standard english version

This is intended as an educational tool and a portfolio project.  It's use on mainnet is not encouraged and is done so at your own risk.

