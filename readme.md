# ElementEncrypt

This set of Python Package and Javascript Library allows you to create static pages with encrypted elements. This is designed for platforms such as Github Pages, where you lack the ability to perform server side processing of passwords, however wish to store data on "password protected pages". Other uses exist, such as testing knowledge during a tutorial by requesting a value to unlock the rest of the page.

NOTE: This software uses AES-256-CBC encryption with a random and unique IV and salt for each element encrypted. By nature, the encrypted data is sent to the client upon loading the page - and can therefore be retained by the client indefinitely - if any vulnerabilties were to be found in AES in the future (which would be a Big Deal), data encrypted using this tool could potentially be accessed.

## Command Line Utility
Right now, the command line utility is only compatible with encrypting files provided to it.
Any element with a `data-elementencrypt-password` attribute will be encrypted with a random iv and salt using AES-256 CBC. The password provided is not included within the processed data; and in order to access the processed data, it must be decrypted using the same password, IV and salt.

[Template Files](/doc/templates.md) can be used in order to modify what is displayed in areas where encrypted data is present.
The default template file can be found [here](elementencrypt/template.html).

### Suggested Usage
For each file you wish to have encrypted on your website, run the command line tool against it, via `python main.py -o <destination path> <input path>`, place the resulting file into your site, and ***keep the initial input file out of the public site***. On GitHub Pages, this can be done through selecting a specific folder from which the GitHub site can be served.

***If using GitHub Pages, remember that if you commit your input files into a public repository, they can be viewed, and the password extracted from their source.***

## JavaScript
A basic JavaScript file is present within `js/element-encrypt.js`, which utilises crypto-js to decrypt the data provided, and is compatible with the default template used by this tool.


## Example
A functional example can be found at samples/basic_example.html, with the source page being found [here](samples/basic_example.html.ecry).

## License
This software is licensed under the [MIT license](LICENSE). 
