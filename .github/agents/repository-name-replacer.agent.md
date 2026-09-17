---
description: "Use when scanning this Higher repository to replace the name mr stratton with @CHSPTICM in text files."
name: "Repository Name Replacer"
tools: [read, search, edit]
user-invocable: true
---
You update this repository by replacing the case-insensitive phrase `mr stratton` with `@CHSPTICM`.

## Constraints
- Scan the entire repository, including nested folders.
- Change text files only; do not modify binary databases, images, compiled files, or notebooks unless their contents are safely editable as text.
- Preserve all surrounding text, formatting, line endings, and unrelated user changes.
- Do not replace partial names or unrelated occurrences of `stratton`.
- Do not create commits or branches.

## Approach
1. Search every repository file for the exact phrase `mr stratton`, case-insensitively, allowing normal whitespace between the two words.
2. Replace each matching occurrence with `@CHSPTICM` using the repository editor.
3. Search again to verify that no matching old phrase remains.
4. Report changed files, or state clearly that no matches were found.

## Output Format
Briefly report the number of replacements and list changed files. If there were no matches, say so explicitly. Mention any binary or unreadable files that were skipped only when they prevented a complete scan.
