## Encryption
Prior to encryption, data is encoded using the UTF-8 scheme, and is then padded using the pkcs7 scheme to be a multiple of 16 bytes long. 

The Encryption key is derived using PBKDF2 for `13337` rounds, with a 16 byte salt and a desired length of 32 bytes. The derived key can then be used for encryption and decryption using standard AES-256-CBC; and is used to encrypt the contents of the detected wrapped element.

After encryption, all data (IV, Salt and Encrypted Data) is encoded using Base64 before being inserted into the template.
