# ConiBotti

Discord bot. Fetches data from an api, formats it and prints it out.

## Install & Usage

**Requires minimum of Python 3.12 to support PEP 701 style f-strings**

```bash
$ python -c "print(f'{object.__dict__['__doc__']}')"
# The base class of the class hierarchy.
#
# When called, it accepts no arguments and returns a new featureless
# instance that has no instance attributes and cannot be given any.
#
# ^ this means you can run this app 
```

```bash
$ python -c "print(f'{object.__dict__['__doc__']}')"
#   File "<string>", line 1
#     print(f'{object.__dict__['__doc__']}')
#                               ^^^^^^^
# SyntaxError: f-string: unmatched '['
#
# ^ this means you can not run this app
```

### TL;DR

```bash
$ git clone <repo_url> && cd <repo_name>
$ python -m venv .venv --upgrade-deps
$ .venv\Scripts\activate
$ python -m pip install -r requirements.txt --upgrade
$ python -m conibotti
```

## TODO

- implement more stuff
- add comments
- implement stubs
- database to cache api call results?
- this readme

## Thanks

Data source: [conit.fi – Suomen conitapahtumat][conit-fi] (GitHub: [Kompassi][kompassi-repo])

[conit-fi]: https://conit.fi/
[kompassi-repo]: https://github.com/con2/kompassi/

## Coding Conventions

This project follows (or at least makes reasonable effort to follow) the
philosophy described in [PEP 8][pep-ref], which is summarized in the quote below.

> ## A Foolish Consistency is the Hobgoblin of Little Minds[^pep-quote]
>
> [^pep-quote]: [PEP 8: A Foolish Consistency is the Hobgoblin of Little Minds][pep-ref-ch2]
>
> One of Guido’s key insights is that code is read much more often than it is
> written. The guidelines provided here are intended to improve the readability
> of code and make it consistent across the wide spectrum of Python code. As
> PEP 20 says, “Readability counts”.
>
> A style guide is about consistency. Consistency with this style guide is
> important. Consistency within a project is more important. Consistency
> within one module or function is the most important.
>
> However, know when to be inconsistent – sometimes style guide recommendations
> just aren’t applicable. When in doubt, use your best judgment. Look at other
> examples and decide what looks best. And don’t hesitate to ask!
>
> In particular: do not break backwards compatibility just to comply with this
> PEP!
>
> Some other good reasons to ignore a particular guideline:
>
> 1. When applying the guideline would make the code less readable, even for
>    someone who is used to reading code that follows this PEP.
> 2. To be consistent with surrounding code that also breaks it (maybe for
>    historic reasons) – although this is also an opportunity to clean up
>    someone else’s mess (in true XP style).
> 3. Because the code in question predates the introduction of the guideline
>    and there is no other reason to be modifying that code.
> 4. When the code needs to remain compatible with older versions of Python
>    that don’t support the feature recommended by the style guide.

[pep-ref]: https://peps.python.org/pep-0008/ "PEP 8 – Style Guide for Python Code"
[pep-ref-ch2]: https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds

