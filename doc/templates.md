
## Template Files
When processing whatever file you provide,  you can additionally provide a template file.
If you do not define a template, a default template is utilised. This template is compatible out of the box with the javascript provided within the `/js` folder. The template file defines what should be inserted into the document in place of any "encrypted" tags.
Template files should consist of valid HTML, and will be processed and inserted in full into the page at the point where a tag is to be encrypted. As a result, it's recommended not to include any dependencies within the tempalte file, as they will be included multiple times - instead include these more generally.

## Template Tags
Multiple strings can be included within a template, which will be substituted for their respective values while using the command line tool.

| Tag      | Description |
| ----------- | ----------- |
| %%ENCRYPTED_HTML%%     | The encrypted HTML tag, in Base64 format.      |
| %%IV%%  | The IV used while encrypting the respective tag.        |
| %%SALT%% | The salt used while encrypting the respective tag. |
| %%ELEMENT_ID%% | The ID of the HTML tag that's been encrypted. If no ID was set, this will be a random hex identifier instead. |

These values are only replaced where they are present within the template provided. They will *not* be replaced if included in the page.