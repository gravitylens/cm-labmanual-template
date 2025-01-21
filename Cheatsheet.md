# Markdown Cheatsheet

## Headings
Use # to denote a heading.  You can add more #s to decrease the heading level.  Note markdown requires a space after the #.  Some markdown interpreters will render a heading appropriately if the space is omited.  A # without a space is sometimes interpreted as a #hashtag.

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```
Rendered:
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

---

## Text Formatting
```markdown
**Bold** or __Bold__
*Italic* or _Italic_
***Bold and Italic***
~~Strikethrough~~
`Inline code`
```
Rendered:
**Bold**
*Italic*
***Bold and Italic***
~~Strikethrough~~
`Inline code`

---

## Lists
### Unordered List
```markdown
- Item 1
  - Sub-item 1
  - Sub-item 2
- Item 2
```
Rendered:
- Item 1
  - Sub-item 1
  - Sub-item 2
- Item 2

### Ordered List
```markdown
1. First item
2. Second item
   1. Sub-item 1
   2. Sub-item 2
```
Rendered:
1. First item
2. Second item
   1. Sub-item 1
   2. Sub-item 2

---

## Links and Images
### Link
```markdown
[Link text](https://cyberark.com)
```
Rendered:
[Link text](https://cyberark.com)

### Image
```markdown
![Alt text](https://www.cyberark.com/wp-content/uploads/2024/10/cyberark-logo.svg)
```
Rendered:
![Alt text](https://www.cyberark.com/wp-content/uploads/2024/10/cyberark-logo.svg)

---

## Blockquotes
```markdown
> This is a blockquote.
> It can span multiple lines.
```
Rendered:
> This is a blockquote.
> It can span multiple lines.

---

## Code Blocks
### Inline Code
```markdown
`Inline code`
```

### Fenced Code Block
```markdown
```
Code block
with multiple lines
```
```

---

## Tables
```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1    | Data 1   | Data 2   |
| Row 2    | Data 3   | Data 4   |
```
Rendered:
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1    | Data 1   | Data 2   |
| Row 2    | Data 3   | Data 4   |

---

## Horizontal Rule
```markdown
---
***
___
```
Rendered:
---
***
___

---

## Checklists
```markdown
- [x] Task 1
- [ ] Task 2
- [ ] Task 3
```
Rendered:
- [x] Task 1
- [ ] Task 2
- [ ] Task 3

## Page Break
Markdown does support page breaks as they have no meaning in the way markdown files are intended to be used.  You can, however, include HTML in a markdown file and it will be rendered appropriately.  Unfortunately, it makes the markdown file more difficult to read unrendered.  To solve this the Python conversion script will replace ::: pagebreak ::: with the appropriate HTML during the build.  To include a page break simply use 
```markdown
::: pagebreak :::
```

## Include Files
To aid the  construction of very large lab manuals, you can include external files within another markdown file
```markdown
::: include filename.md :::
```
This will insert the entire content of that other markdown file at that point.

## Copyable Text
To denote text that can be copied from the guide into the Skytap machine by clicking on it, use double carets `^^` around the text. For example:
```markdown
^^copyable text^^
```
This will be converted to an `<x-copy-text>` tag in the HTML output, making it easy for users to copy the text by clicking on it.
