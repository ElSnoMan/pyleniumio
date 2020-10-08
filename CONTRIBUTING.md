# Contributing to Pylenium

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:


The following is a set of guidelines for contributing to Pylenium on GitHub. These are mostly guidelines, not rules.
Use your best judgment, and feel free to propose changes to this document in a pull request.

#### Table of Contents

* [Code of Conduct](./CODE_OF_CONDUCT.md)
* [What should I know before getting started?](#what-should-i-know-before-getting-started)
* [How can I Contribute?](#how-can-i-contribute)
    * [Setup the Project](#setup-the-project-to-start)
    * [Report a Bug](#report-a-bug)
        * [Before submitting a Bug](#before-submitting-a-bug-report)
        * [How do I submit a (good) Bug](#how-do-i-submit-a-good-bug-report)
    * [Suggesting Enhancements](#suggesting-enhancements)
        * [Before submitting an Enhancement](#before-submitting-an-enhancement-suggestion)
        * [How do I submit a (good) Enhancement?](#how-do-i-submit-a-good-enhancement-suggestion)
    * [Your first Code Contribution](#your-first-code-contribution)
* [Pull Requests (PR)](#pull-requests)
    * [PR Templates](#pr-templates)
        * [Requirements for contributing a Bugfix](#requirements-for-contributing-a-bug-fix)
            * [Bug Template](#bug-template)
        * [Requirements for contributing Documentation](#requirements-for-contributing-documentation)
            * [Documentation Template](#documentation-template)
        * [Requirements for contributing adding, changing, or removing a Feature](#requirements-for-adding-changing-or-removing-a-feature)
            * [Enhancement Template](#enhancement-template)
    * [Style Guides](#style-guides)
        * [Git Commit Messages](#git-commit-messages)
        * [Python Styleguide](#python-styleguide)

## Code of Conduct

This project and everyone participating in it is governed by the [Pylenium Code of Conduct](CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report unacceptable behavior to Carlos Kidman (@ElSnoMan).

## What should I know before getting started?

Pylenium is a wrapper of Selenium, not Cypress.
However, like Cypress, we want Pylenium to be an all-in-one solution that comes with everything you need and expect from a robust Test Automation Solution.

Most features should be "plug and play" for the user to make it easy for them, but we also need to keep it extendable
so they can customize or swap components, like a reporting tool, if they want to. However, some components cannot be changed.

For example:

* Selenium (for obvious reasons)
* pytest as the Testing Framework

## How can I Contribute?

### Setup the Project to Start

This [Guide in our Documentation][clone and setup]
gives you the steps to clone and setup the project.

From there, open the [Issues Tab][Issues Tab] and check out the [Pull Requests Guide](#pull-requests)!

### Report a Bug

This section guides you through submitting a bug report for Pylenium. Following these guidelines helps maintainers
and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

When you are creating a bug report, please [include as many details as possible](#how-do-i-submit-a-good-bug-report).
Following this and providing the information it asks for helps us resolve issues faster.

> **Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.

#### Before Submitting A Bug Report

* **Perform a cursory search** to see if the problem has already been reported.
If it has **and the issue is still open**, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Bug Report?

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/).
Create an issue on this repository and explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible. For example, start by explaining how you started Pylenium or ran a test(s), e.g. which command exactly you used in the terminal. When listing steps, **don't just say what you did, but explain how you did it**. For example, running tests via the IDE's UI behaves differently than the Terminal.
* **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem. If you use the keyboard while following the steps, **record the GIF with the [Keybinding Resolver](https://github.com/atom/keybinding-resolver) shown**. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
* **If you're reporting that Pylenium crashed, quits, or doesn't run tests**, include a stack trace and the Project Structure in the issue in a [code block](https://help.github.com/articles/markdown-basics/#multiple-lines), a [file attachment](https://help.github.com/articles/file-attachments-on-issues-and-pull-requests/), or put it in a [gist](https://gist.github.com/) and provide link to that gist.

Provide more context by answering these questions:

* **Can you reproduce the problem in the Terminal?** Sometimes Test issues are IDE-specific and not necessarily Selenium or Pytest.
* **Did the problem start happening recently** (e.g. after updating to a new version of Pylenium) or was this always a problem?
* If the problem started happening recently, **can you reproduce the problem in an older version of Pylenium?** What's the most recent version in which the problem doesn't happen?
* **Can you reliably reproduce the issue?** If not, provide details about how often the problem happens and under which conditions it normally happens.

Include details about your configuration and environment:

* **Which version of Pylenium are you using?** You can get the exact version by running `pylenium --version` in your terminal.
* **What's the name and version of the OS you're using**?
* **Are you running Tests in locally vs the Cloud?** If so, which tools or software are you using and which operating systems and versions are used for the host and the guest?
* **Have you checked the Browser, Drivers, or Selenium about WebDriver issues?** Remember, Pylenium is a wrapper of Selenium, so something like Drag and Drop not working may be a WebDriver or Browser issue.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for Pylenium, including completely new features and minor improvements to existing functionality or documentation.
Following these guidelines helps maintainers and the community understand your suggestion :pencil: and find related suggestions :mag_right:.

Before creating enhancement suggestions, please check [this list](#before-submitting-an-enhancement-suggestion) as you might find out that you don't need to create one.
When you are creating an enhancement suggestion, please [include as many details as possible](#how-do-i-submit-a-good-enhancement-suggestion)
and the steps that you imagine you would take if the feature you're requesting existed.

#### Before Submitting An Enhancement Suggestion

* **Check the [Pylenium Docs](https://elsnoman.gitbook.io/pylenium/)** for tips and commands — you might discover that the enhancement is already available. Most importantly, check if you're using the latest version of Pylenium.
* **Perform a cursory search in the Issues Tab** to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue on this repository and provide the following information:

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps**. Include copy/pasteable snippets which you use in those examples, as [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Include screenshots and animated GIFs** which help you demonstrate the steps or point out the part of Pylenium which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
* **Explain why this enhancement would be useful** to most Pylenium users and isn't something that can or should be implemented on your own or on another package, like a pytest plugin.
* **List some other automation tools or applications where this enhancement exists.**
* **Specify which version of Pylenium you're using.** You can get the exact version by running `pylenium --version` in your terminal.
* **Specify the name and version of the OS you're using.**

### Your First Code Contribution

Unsure where to begin contributing to Pylenium? You can start by looking through `beginner` and `help-wanted` issues:

* Beginner issues - Labeled with `beginner`, these issues should only require a few lines of code, and a test or two.
* Help wanted issues - Labeled with `help wanted`, these issues should be a bit more involved than `beginner` issues.

## Pull Requests

The process described here has several goals:

- Maintain Pylenium's quality or improve it
- Fix problems that are important to users
- Engage the community in working toward the best possible Pylenium
- Enable a sustainable system for Pylenium's maintainers to review contributions

Please follow these steps to have your contribution considered by the maintainers:

1. Follow all instructions in [the template](#pr-templates)
2. Follow the [style guides](#style-guides)
3. After you submit your pull request, verify that all [status checks](https://help.github.com/articles/about-status-checks/) are passing <details><summary>What if the status checks are failing?</summary>If a status check is failing, and you believe that the failure is unrelated to your change, please leave a comment on the pull request explaining why you believe the failure is unrelated. A maintainer will re-run the status check for you. If we conclude that the failure was a false positive, then we will open an issue to track that problem with our status check suite.</details>

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

## PR Templates

### Requirements for Contributing a Bug Fix

* Fill out the template below. Any pull request that does not include enough information to be reviewed in a timely manner may be closed at the maintainers' discretion.
* The pull request must only fix an existing bug. To contribute other changes, you must use a different template.
* The pull request must update the test suite to demonstrate the changed functionality.
* After you create the pull request, all status checks must be pass before a maintainer reviews your contribution.

#### Bug Template

1. Identify the Bug

    > Link to the issue describing the bug that you're fixing.

    If there is not yet an issue for your bug, please open a new issue and then link to that issue in your pull request.
    Note: In some cases, one person's "bug" is another person's "feature." If the pull request does not address an existing issue with the "bug" label, the maintainers have the final say on whether the current behavior is a bug.

2. Description of the Change

    > We must be able to understand the design of your change from this description.

    If we can't get a good idea of what the code will be doing from the description here, the pull request may be closed at the maintainers' discretion.
    Keep in mind that the maintainer reviewing this PR may not be familiar with or have worked with the code here recently, so please walk us through the concepts.

3. Alternate Designs

    > Explain what other alternates were considered and why the proposed version was selected

4. Possible Drawbacks

    > What are the possible side-effects or negative impacts of the code change?

5. Verification Process

    > What process did you follow to verify that the change has not introduced any regressions?
    
    Describe the actions you performed (including buttons you clicked, text you typed, commands you ran, etc.),
    and describe the results you observed.

6. Release Notes

    > Please describe the changes in a single line that explains this improvement in
    terms that a user can understand. This text will be used in Pylenium's release notes.

    If this change is not user-facing or notable enough to be included in release notes you may use the strings "Not applicable" or "N/A" here.

    Examples:

    - The GitHub package now allows you to add co-authors to commits.
    - Fixed an issue where multiple cursors did not work in a file with a single line.
    - Increased the performance of searching and replacing across a whole project.

### Requirements for Contributing Documentation

* Fill out the template below. Any pull request that does not include enough information to be reviewed in a timely manner may be closed at the maintainers' discretion.
* The pull request must only contribute documentation (for example, markdown files or API docs). To contribute other changes, you must use a different template.

#### Documentation Template

1. Description of the Change

    > We must be able to understand the purpose of your change from this description.
    
    If we can't get a good idea of the benefits of the change from the description here, the pull request may be closed at the maintainers' discretion.

2. Release Notes

     > Please describe the changes in a single line that explains this improvement in
     terms that a user can understand.  This text will be used in Pylenium's release notes.

    If this change is not user-facing or notable enough to be included in release notes
    you may use the strings "Not applicable" or "N/A" here.

    Examples:

    - The GitHub package now allows you to add co-authors to commits.
    - Fixed an issue where multiple cursors did not work in a file with a single line.
    - Increased the performance of searching and replacing across a whole project.

### Requirements for Adding, Changing, or Removing a Feature

* Fill out the template below. Any pull request that does not include enough information to be reviewed in a timely manner may be closed at the maintainers' discretion.
* The pull request must contribute a change that has been endorsed by the maintainer team. See details in the template below.
* The pull request must update the test suite to exercise the updated functionality.
* After you create the pull request, all status checks must be pass before a maintainer reviews your contribution.

#### Enhancement Template

1. Issue or RFC Endorsed by Pylenium's Maintainers

    > Link to the issue or RFC that your change relates to.

    To contribute an enhancement that isn't endorsed, please follow our guide for Suggesting Enhancements.

    To contribute other changes, you must use a different template.

2. Description of the Change

    > We must be able to understand the design of your change from this description.

    If we can't get a good idea of what the code will be doing from the description here, the pull request may be closed at the maintainers' discretion.
    Keep in mind that the maintainer reviewing this PR may not be familiar with or have worked with the code here recently, so please walk us through the concepts.

3. Alternate Designs

    > Explain what other alternates were considered and why the proposed version was selected.

4. Possible Drawbacks

    > What are the possible side-effects or negative impacts of the code change?

5. Verification Process

    > What process did you follow to verify that your change has the desired effects?

    - How did you verify that all new functionality works as expected?
    - How did you verify that all changed functionality works as expected?
    - How did you verify that the change has not introduced any regressions?

    Describe the actions you performed (including buttons you clicked, text you typed, commands you ran, etc.), and describe the results you observed.

6. Release Notes

    > Please describe the changes in a single line that explains this improvement in
    terms that a user can understand. This text will be used in Atom's release notes.

    If this change is not user-facing or notable enough to be included in release notes
    you may use the strings "Not applicable" or "N/A" here.

    Examples:

    - The GitHub package now allows you to add co-authors to commits.
    - Fixed an issue where multiple cursors did not work in a file with a single line.
    - Increased the performance of searching and replacing across a whole project.


### Style Guides

#### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

Consider starting the commit message with an applicable emoji:

* 🎨 :art: when improving the format/structure of the code
* 🐎 :racehorse: when improving performance
* 🚱 :non-potable_water: when plugging memory leaks
* 📝 :memo: when writing docs
* 🐧 :penguin: when fixing something on Linux
* 🍎 :apple: when fixing something on macOS
* 🏁 :checkered_flag: when fixing something on Windows
* 🐛 :bug: when fixing a bug
* 🔥 :fire: when removing code or files
* 💚 :green_heart: when fixing the CI build
* ✅ :white_check_mark: when adding tests
* 🔒 :lock: when dealing with security
* ⬆ :arrow_up: when upgrading dependencies
* ⬇ :arrow_down: when downgrading dependencies
* 👕 :shirt: when removing linter warnings

#### Python Styleguide

`pep8` is the styleguide and `flake8` is the linter in CI.

* Indents are 4 spaces (turn your tabs to spaces!)
* Type Hint as much as possible, but it should make sense
* Docstrings are _valuable_ because Pylenium is a library. Help the user stay in code rather than looking up docs all the time
* Docstrings follow the Google format

```python
def first() -> Element:
    """ Get the first element from this list. """
    return _elements[0]

# --- over ---

def first():
    return _elements[0]
```

[clone and setup]: https://elsnoman.gitbook.io/pylenium/contribute/clone-and-setup-the-project
[Issues Tab]: https://github.com/ElSnoMan/pyleniumio/issues