Since it's fairly rare to revise this bio, I would not bother to automate PDF generation.

1. Open repository homepage in browser.
2. Toggle development tool.
3. Paste and run

  ```
  x = document.querySelector('.Box-body'); document.body.innerHTML = ''; document.body.appendChild(x)
  ```

4. Print the page into PDF.
