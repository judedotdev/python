# Caesar Cipher

This program Encrypts a message using the Caesar Cipher algorithm.

The program can also Decrypt encrypted messages.

Notice:

- Right shift is a positive integer
- Left shift is a negative integer

## Equation

- Encryption Phase with shift n:
  
  `En(x) = (x + n)mod 26`
- Decryption Phase with shift n:

    `Dn(x) = (x - n)mod 26`

## Example

Encrypting a Message:
  
If the plain text is `HELLO` and a right shift of 7 is used, the cypher/encrypted text will be `OLSSV`

Decrypting a Message:

If we have an encrypted text `OLSSV`, we will need a key to decrypt it. As the reciever of the message who knows that the key is a `right shift of 7` we can decrypt it by running this program, selecting `option 2` and `using a right shift of 7`.

After following this steps, we have successfully decrypted this encrypted text, and we have the result `Plain Text: HELLO`.
